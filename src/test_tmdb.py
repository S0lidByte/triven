import asyncio
import os
import sys
sys.path.append(os.getcwd())
from program.apis.tmdb_api import TMDBApi
from program.settings.manager import settings_manager
async def test_fallout():
    settings = settings_manager.settings
    api_key = settings.apis.tmdb.key
    tmdb = TMDBApi(api_key)
    result = await tmdb.get_external_ids(108978, "tv")
    print("External IDs for Fallout (TMDB 108978):")
    print(result)

if __name__ == "__main__":
    asyncio.run(test_fallout())
