import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

    
def main():
    client = info['Client']
    secret = info['Secret']
    return_url = info['ReturnURL']
    token = info['Token']
        
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client, client_secret=secret, redirect_uri=return_url, scope="user-library-read"))

    cond = True
    num = 0
    saved_list = []
    while(cond):
        results = sp.current_user_saved_tracks(limit=50, offset=num, market="US")
        for i in results['items']:
            i = i['track']
            name = i['name']
            artist = i['artists'][0]['name']
            album = i['album']['name']
            saved_list.append([name, artist, album])
        num += 50
        print("plus 50 - total " + str(num))
        if results['next'] == None:
            cond = False

    json.dump({"items": saved_list}, open('src/saved_list.json', 'w'), indent=4, ensure_ascii=False)


if __name__ == '__main__':
    info = json.load(open('info.json', 'r'))
    main()
