### Description
Downloads any track or playlists from soundcloud without using SoundCloud API.
Just put URL and enjoy with downloaded track :)

### Requirements
Requires only installation of **youtube-dl**
**apt install youtube-dl**

## How to use

**sc_downloader.py** just put soundcloud track URL:

```
# Run
if __name__ == "__main__":
    scd = SCDownloader()
    track_url = "Put url here"
    scd.download(track_url)
```

**sc_downloader_input.py** could be executed throught command line
You could just execute script and then input soundcloud track URL or just pass through command line:
```
python3 sc_downloader.py https://soundcloud.com/myabandonedhome/snowfall-w-oneheart  
```
or
```
python3 sc_downloader_input.py                                                                                        INT 08:56:21
Please provide the SoundCloud track URL: https://soundcloud.com/myabandonedhome/snowfall-w-oneheart
```
