# Changelog

## [1.2.1](https://github.com/S0lidByte/triven/compare/v1.5.0...v1.2.1) (2026-03-01)


### Features

* add aiostreams scraper and fix mediafusion scraper & update schemas ([#1340](https://github.com/S0lidByte/triven/issues/1340)) ([e221e50](https://github.com/S0lidByte/triven/commit/e221e5033e09355af6867f1f59cc0d39706d39f5))
* **backend:** implement comprehensive audit fixes for performance and stability ([ded391c](https://github.com/S0lidByte/triven/commit/ded391ca90a4ad623bb9e653497f624b8b54ef42))
* **calendar:** overhaul calendar api bounds, add deduplication guard and ui tweaks ([b5d95ac](https://github.com/S0lidByte/triven/commit/b5d95acea790c2aa51b5acfd1c4a40a925f32b7a))
* fix ffmpeg shell injection and bump starlette ([a89bc78](https://github.com/S0lidByte/triven/commit/a89bc7803662ad6b0985908c294796ccd677ac20))


### Bug Fixes

* **api:** properly return 404 instead of 500 when GET /items/{id} fails ([8fac650](https://github.com/S0lidByte/triven/commit/8fac650ee5d1070a84bed7473899604e183691ae))
* **backend:** resolve 5 post-audit regressions ([c81e642](https://github.com/S0lidByte/triven/commit/c81e642a38cdd81e9c446b74b50a4d2cbb048c11))
* **backend:** resolve 500 on /items endpoint and zilean fallback ([dcdb90b](https://github.com/S0lidByte/triven/commit/dcdb90b047fa43b8be19c9e5f915dbbbc722cc64))
* **calendar:** revert SQL JSON filter to Python — SeriesReleaseDecorator is not raw JSONB ([494d6b4](https://github.com/S0lidByte/triven/commit/494d6b4bf2b1cd8e46239784c4e7648519ed1c7e))
* **calendar:** strip timezone from iso parsed datetimes to prevent 500 comparison error ([8681692](https://github.com/S0lidByte/triven/commit/86816922c78f7d8ebb6380d0c53fd6e2620007d2))
* **core:** Handle Unknown state in transition and CI PLATFORM_PAIR access ([282176e](https://github.com/S0lidByte/triven/commit/282176e9160dd922d61234dac83f7a5bec49c0c3))
* **debug:** import time for trace logs ([4791e6a](https://github.com/S0lidByte/triven/commit/4791e6ab29718f33a48f081e7ec36372b3b663e7))
* **downloader:** fall back to Indexed when all streams exhausted ([9ab0b8a](https://github.com/S0lidByte/triven/commit/9ab0b8a107b2103722e23c8f248aeafffc956613))
* **items:** validate TVDB IDs before enqueuing, surface 404s to frontend ([a26547a](https://github.com/S0lidByte/triven/commit/a26547ad8931ac2247e1c2f7ca437d02a3fd7f5f))
* **memory:** free httpx decoder buffers and revert thread pool to 5 ([f378bf7](https://github.com/S0lidByte/triven/commit/f378bf70fbcb85f84a05acec7eff476242eb80d3))
* **queue:** correct priority order to prevent starvation ([9ab0b8a](https://github.com/S0lidByte/triven/commit/9ab0b8a107b2103722e23c8f248aeafffc956613))
* remove anime check from aiostreamms ([9bfdb89](https://github.com/S0lidByte/triven/commit/9bfdb8918ec803648731b56ad9a8c2cfa27843a0))
* resolve queue deadlock and stream fetch crash ([207e383](https://github.com/S0lidByte/triven/commit/207e3837f0c8e117bd198bbcbe398ab2b000044d))
* retry scraper trigger + PlexWatchlist memory leak ([078ab18](https://github.com/S0lidByte/triven/commit/078ab1803e1e181ba8b57d360f9aa355e6732bca))
* **retry:** recursively reset scraped_at/scraped_times on child seasons and episodes ([c968ed4](https://github.com/S0lidByte/triven/commit/c968ed4b55bdccfa6583a30b0f2fe1417f2a7f6d))
* **retry:** reset failed_attempts and Failed state on child episodes ([22902b7](https://github.com/S0lidByte/triven/commit/22902b7e718baeb2299fb886b8fbfd37259088e0))
* tidy error log for torrentio outages ([91bfd58](https://github.com/S0lidByte/triven/commit/91bfd582a4ebfe318fb1e58f4ba511d6b04798a1))
* **vfs:** resolve subtitle caching, dead-link retries, and TOCTOU races ([da8a025](https://github.com/S0lidByte/triven/commit/da8a025c8bf322d625cb2fa290a6374bb0ce5d07))


### Performance Improvements

* **calendar:** V6 optimizations — bounded JSON query, set-based dedup, tmdb_id fallback ([ccb529f](https://github.com/S0lidByte/triven/commit/ccb529f3c88814bf5376dc0f7d790947ec9f41f5))
* **downloader:** increase thread pool to 10 and limit to 1 stream per run ([94d9357](https://github.com/S0lidByte/triven/commit/94d935799757d35e7406f9853f755de440fbf9d3))


### Miscellaneous Chores

* release 1.2.1 ([94ef103](https://github.com/S0lidByte/triven/commit/94ef1031b7d0d908f5d957d387ee29d024b5f003))
