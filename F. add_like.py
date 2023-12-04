import json, pickle
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging, logging.config
import asyncio
    
def main():
    for i in ids:
        print(i)
        sp.current_user_saved_tracks_add(["spotify:track:" + i])
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
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client, client_secret=secret, redirect_uri=return_url, scope="user-library-modify"))

    main()