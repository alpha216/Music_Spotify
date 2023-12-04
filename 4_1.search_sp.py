import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import asyncio
    
def main():
    client = info['Client']
    secret = info['Secret']
    return_url = info['ReturnURL']
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client, client_secret=secret, redirect_uri=return_url, scope="user-library-read"))

    results = ''
    found = []
    count = len(tosearch)
    for i in tosearch:
        query = i[0] + " " + i[1]
        res = sp.search(q=query, limit=3, type='track', market='US')
        
        for j in res["tracks"]["items"]:
            name = j['name']
            artist = j['artists'][0]['name']
            album = j['album']['name']
            id = j['id']
            results += f"Original is {i[0]} by {i[1]} | Name: {name} | Artist: {artist} | Album: {album} | ID: {id}"
            found.append([i[0], i[1], i[2].replace(' - EP', '').replace(' - Single', ''), name, artist, album, id])
        count -= 1
        print(f"Searched {i[0]} by {i[1]} - {count} left")
    
    json.dump(found, open('src/found.json', 'w'), ensure_ascii=False)
    # w = open("src/results.txt", "w")
    # w.write(results)
    # w.close()


if __name__ == '__main__':
    info = json.load(open('info.json', 'r'))
    tosearch = json.load(open('src/not_same.json', 'r'))
    main()
