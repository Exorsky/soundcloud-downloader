import json
from datetime import datetime
from os import path

class Statistics():
    def write(self, song_name, song_url, download_url, genre):
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        songs_list = []
        filename = "downloaded_songs.json"
        data = {
            "song_name": song_name,
            "song_url": song_url,
            "genre": genre,
            "download_url": download_url,
            "download_date": dt
        }
        
        # Check if file exists
        if path.isfile(filename) is False:
            raise Exception("File not found")
        
        # Read JSON file
        with open(filename) as fp:
            songs_list = json.load(fp)
            
        songs_list["downloaded_songs"].append(data)
        
        with open(filename, 'w') as json_file:
            json.dump(songs_list, json_file, 
                                indent=4,  
                                separators=(',',': '))