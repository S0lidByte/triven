"""Parent-owned streams must retain parent ownership during episode playback cleanup."""

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from program.media.item import MediaItem
from program.media.state import States


class FakeStream:
    def __init__(self, stream_id: int, infohash: str):
        self.id = stream_id
        self.infohash = infohash
        self.raw_title = "shared-stream.mkv"

    def __eq__(self, other: object) -> bool:
        return getattr(other, "id", None) == self.id

    __hash__ = object.__hash__


@pytest.mark.asyncio
@patch("sqlalchemy.orm.object_session")
@patch("program.media.item.object_session")
@patch("routers.secure.items.db_session")
@patch("routers.secure.items.apply_item_mutation")
async def test_blacklisting_parent_owned_active_stream_resets_only_episode(
    mock_apply_mutation,
    mock_db_session,
    mock_media_object_session,
    mock_orm_object_session,
):
    """Episode teardown must not clear the Season's active playback state."""
    from program.program import Program
    from routers.secure.items import blacklist_stream

    stream = FakeStream(7, "a" * 40)
    season = SimpleNamespace(
        id=10,
        log_string="Season 1",
        streams=[stream],
        blacklisted_streams=[],
        active_stream=stream,
        parent=None,
    )
    episode = SimpleNamespace(
        id=42,
        log_string="Episode 1",
        streams=[],
        blacklisted_streams=[],
        active_stream=stream,
        parent=season,
        media_entry=None,
        filesystem_entries=[MagicMock()],
        subtitles=[MagicMock()],
        scraped_at=object(),
        scraped_times=2,
        failed_attempts=1,
        store_state=MagicMock(),
    )

    session = MagicMock()
    session.execute.return_value.unique.return_value.scalar_one_or_none.return_value = (
        episode
    )
    session.query.return_value.filter_by.return_value.first.return_value = None
    mock_db_session.return_value.__enter__.return_value = session
    mock_media_object_session.return_value = session
    mock_orm_object_session.return_value = session

    def apply_mutation(_program, db, consumer, mutation, bubble_parents=True):
        assert db is session
        assert consumer is episode
        assert bubble_parents is False
        mutation(consumer, db)

    mock_apply_mutation.side_effect = apply_mutation

    program = MagicMock()
    vfs = MagicMock()
    program.riven_vfs = vfs

    with patch("routers.secure.items.di", {Program: program}):
        response = await blacklist_stream(item_id=episode.id, stream_id=stream.id)

    assert "Blacklisted active stream" in response.message
    assert season.blacklisted_streams == [stream]
    assert season.streams == []
    assert season.active_stream is stream
    assert episode.active_stream is None
    assert episode.filesystem_entries == []
    assert episode.subtitles == []
    episode.store_state.assert_called_once_with(States.Indexed)
    vfs.remove.assert_called_once_with(episode)
    program.em.add_event.assert_called_once()
    event = program.em.add_event.call_args.args[0]
    assert event.emitted_by == "RetryItem"
    assert event.item_id == episode.id


def test_unblacklist_resolves_parent_owned_blacklisted_stream():
    """An episode request can restore a stream moved to its season blacklist."""
    stream = FakeStream(7, "a" * 40)
    season = SimpleNamespace(
        id=10,
        log_string="Season 1",
        streams=[],
        blacklisted_streams=[stream],
        parent=None,
    )
    episode = SimpleNamespace(
        id=42,
        log_string="Episode 1",
        streams=[],
        blacklisted_streams=[],
        parent=season,
    )

    assert MediaItem.get_stream_owner(episode, stream_id=stream.id) is season

    MediaItem.unblacklist_stream(episode, stream)

    assert season.blacklisted_streams == []
    assert season.streams == [stream]
