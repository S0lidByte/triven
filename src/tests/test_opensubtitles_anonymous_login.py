"""Tests for OpenSubtitles anonymous login and authentication initialization."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from program.services.post_processing.subtitles.providers.opensubtitles import (
    OpenSubtitlesProvider,
)


def test_opensubtitles_anonymous_login_success():
    """Verify OpenSubtitles anonymous login initializes correctly when allow_anonymous=True."""
    provider = OpenSubtitlesProvider(
        username="",
        password="",
        user_agent="VLSub 0.11.1",
        allow_anonymous=True,
    )

    mock_server = MagicMock()
    mock_server.LogIn.return_value = {
        "status": "200 OK",
        "token": "anon-token-12345",
    }
    provider.server = mock_server

    provider.initialize()

    assert provider.token == "anon-token-12345"
    assert provider.login_time is not None
    mock_server.LogIn.assert_called_once_with("", "", "eng", "VLSub 0.11.1")


def test_opensubtitles_authenticated_login_success():
    """Verify OpenSubtitles authenticated login passes provided credentials."""
    provider = OpenSubtitlesProvider(
        username="testuser",
        password="secretpassword",
        user_agent="CustomAgent 1.0",
        allow_anonymous=False,
    )

    mock_server = MagicMock()
    mock_server.LogIn.return_value = {
        "status": "200 OK",
        "token": "auth-token-67890",
    }
    provider.server = mock_server

    provider.initialize()

    assert provider.token == "auth-token-67890"
    assert provider.login_time is not None
    mock_server.LogIn.assert_called_once_with(
        "testuser", "secretpassword", "eng", "CustomAgent 1.0"
    )


def test_opensubtitles_incomplete_credentials_raises():
    """Verify having only username or only password raises an explicit Exception."""
    provider_user_only = OpenSubtitlesProvider(
        username="useronly",
        password="",
    )
    with pytest.raises(Exception, match="credentials are incomplete"):
        provider_user_only.initialize()

    provider_pass_only = OpenSubtitlesProvider(
        username="",
        password="passwordonly",
    )
    with pytest.raises(Exception, match="credentials are incomplete"):
        provider_pass_only.initialize()


def test_opensubtitles_no_credentials_disallowed_anonymous_raises():
    """Verify empty credentials when allow_anonymous=False raises an authentication error."""
    provider = OpenSubtitlesProvider(
        username="",
        password="",
        allow_anonymous=False,
    )
    with pytest.raises(
        Exception,
        match="No OpenSubtitles credentials configured and anonymous login is disabled.",
    ):
        provider.initialize()
