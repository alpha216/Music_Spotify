import json, pickle
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging, logging.config
import asyncio
    
    
    
# async def addit(i):
#     sp.playlist_add_items("5GtIGGE8Nsu8ndMBCkn6ET", "spotify:track:" + i)
#     logger.debug("Added " + i)
    
# async def main():
#     global results, found
#     found = []
    
#     fts = [asyncio.ensure_future(addit(u)) for u in ids]
#     r = await asyncio.gather(*fts)
#     results = r

def main():
    print(sp.playlist("4lcZMcilWGBNp7RVpPvtRi"))
    # return 0
    for i in ids:
        print(i)
        sp.playlist_add_items("4lcZMcilWGBNp7RVpPvtRi", ["spotify:track:" + i])
        logger.debug("Added " + i)

if __name__ == '__main__':
    with open('logging.json', 'rt') as f: config = json.load(f)
    open("./info.log", 'w').close()
    logging.config.dictConfig(config)
    logger = logging.getLogger()
    
    info = json.load(open('info.json', 'r'))
    ids = pickle.load(open('src/ids.p', 'rb'))
    
    
    client = info['Client']
    secret = info['Secret']
    return_url = info['ReturnURL']
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client, client_secret=secret, redirect_uri=return_url, scope="playlist-modify-public playlist-modify-private"))

    # asyncio.run(main())
    main()

    
