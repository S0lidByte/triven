# Changelog

## [1.2.0](https://github.com/S0lidByte/triven/compare/v1.1.5...v1.2.0) (2026-02-28)


### Features

* **calendar:** overhaul calendar api bounds, add deduplication guard and ui tweaks ([b5d95ac](https://github.com/S0lidByte/triven/commit/b5d95acea790c2aa51b5acfd1c4a40a925f32b7a))


### Bug Fixes

* **calendar:** revert SQL JSON filter to Python — SeriesReleaseDecorator is not raw JSONB ([494d6b4](https://github.com/S0lidByte/triven/commit/494d6b4bf2b1cd8e46239784c4e7648519ed1c7e))
* **calendar:** strip timezone from iso parsed datetimes to prevent 500 comparison error ([8681692](https://github.com/S0lidByte/triven/commit/86816922c78f7d8ebb6380d0c53fd6e2620007d2))
* **core:** Handle Unknown state in transition and CI PLATFORM_PAIR access ([282176e](https://github.com/S0lidByte/triven/commit/282176e9160dd922d61234dac83f7a5bec49c0c3))
* retry scraper trigger + PlexWatchlist memory leak ([078ab18](https://github.com/S0lidByte/triven/commit/078ab1803e1e181ba8b57d360f9aa355e6732bca))
* **vfs:** resolve subtitle caching, dead-link retries, and TOCTOU races ([da8a025](https://github.com/S0lidByte/triven/commit/da8a025c8bf322d625cb2fa290a6374bb0ce5d07))


### Performance Improvements

* **calendar:** V6 optimizations — bounded JSON query, set-based dedup, tmdb_id fallback ([ccb529f](https://github.com/S0lidByte/triven/commit/ccb529f3c88814bf5376dc0f7d790947ec9f41f5))
