import subprocess
import os
import json
import requests

class SCDownloader():
    
    def __get_track_name(self,url):
        filename = subprocess.check_output(
            ['youtube-dl' , '--get-filename', url] 
        ).decode('UTF-8').rstrip('\n')
        return filename 
    
    def __download_json_file(self, url):
        subprocess.call(
    ['youtube-dl', '--write-info-json', '--skip-download' , url])

    def __open_json_file(self):
        json_files = [pos_json for pos_json in os.listdir(os.path.dirname(os.path.realpath('__file__'))) if pos_json.endswith('.json')]
        return json_files

    def __read_json_file(self, json_files):   
        with open(json_files, 'r') as fp:
            data = json.load(fp)
        #Extract data from json
        url = data['url']
        title = data['fulltitle']
        return url,title
        
    def __remove_json_files_from_dir(self):
        directory = os.path.dirname(os.path.realpath('__file__'))
        for file in os.listdir(directory):
            if file.endswith('.info.json'):
                try:
                    path = os.path.join(directory, file)
                    os.remove(path)
                except Exception as e:
                    print(f"Error deleting file: {path}\n{e}")
    
    def download(self, url):
        self.__download_json_file(url)
        json_files = self.__open_json_file()
        for json_file in json_files:
            url, title = self.__read_json_file(json_file)
            title = title.replace('/', '_')
            with open(f'{title}.mp3', 'wb') as fp:
                fp.write(requests.get(url, stream=True).content)
                print(f"[Downloaded] - {title}.mp3")
                
        self.__remove_json_files_from_dir()
            
# Run
if __name__ == "__main__":
    scd = SCDownloader()
    track_url = "Put url here"
    scd.download(track_url)