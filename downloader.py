import subprocess
import os
import json
import requests

class SCDownloader():

    def download(self, url):
        
        filename = self.__get_track_name(url)
        self.__download_json_file(url)
        json_files = self.__open_json_file()
        url, thumb, title = self.__read_json_file(json_files)
        
        with open(f'{title}.mp3', 'wb') as fp:
            fp.write(requests.get(url, stream=True).content)
            
        #self.__remove_json_from_dir(filename)
    
    def __get_track_name(self,url):
        filename = subprocess.check_output(
            ['youtube-dl' , '--get-filename', url] 
        ).decode('UTF-8').rstrip('\n')
        print(filename)       
    
    def __download_json_file(self, url):
        subprocess.call(
    ['youtube-dl', '--write-info-json', '--skip-download' , url])

    def __open_json_file(self):
        json_files = [pos_json for pos_json in os.listdir(os.path.dirname(os.path.realpath('__file__'))) if pos_json.endswith('.json')]
        print(json_files)
        return json_files       

    def __read_json_file(self, json_files):   
        with open(json_files[0], 'r') as fp:
            data = json.load(fp)
        #Extract data from json
        url = data['url']
        thumb = data['thumbnail']
        title = data['fulltitle']
        print(f"Download url: {url} Thumb url: {thumb}\n Title: {title}")
        return url,thumb,title
        
    def __remove_json_from_dir(self, filename):
        path = f'{os.path.dirname(os.path.realpath("__file"))}/{filename.replace(".mp3",".info.json")}'
        try:
            if os.path.isfile(path):
                os.remove(path)
        except Exception as e:
            print(f"Error: {e}")
            
# Run
scd = SCDownloader()
scd.download('https://soundcloud.com/abdulla-mohammed-59851950/losing-focus-playlist-m4a')