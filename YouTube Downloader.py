try:
   import yt_dlp as youtube_dl
   import requests
   import os
   import random as r
   import argparse
except:
   print("You do not have yt_dlp, please run requirements.bat to install it.")

version = "V0.135"

def read_github_file(raw_url):
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file: {e}")
        return None

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
    else:
        print("Failed to download file. Status code:", response.status_code)

tips = [
   "\nDidn't download properly? Run 'pip install --upgrade yt-dlp' in your command line!\n",
   "\nHaving issues with download? Try updating Youtube Downloader or run 'pip install --upgrade yt_dlp'"
]

tipchance = 20

currentVersion = ""
changelog = ""

try:
   exec(read_github_file("https://raw.githubusercontent.com/GDTMG232/YouTube-Downloader/main/updates.py"))
   if currentVersion != version:
      if input(f"You have to update from {version} to {currentVersion}!\n{changelog}\n\nWould you like to update?\nY/N: ").lower() == "y":
         os.rename(__file__, "outdatedYTDNLDR.py")
         download_file("https://raw.githubusercontent.com/GDTMG232/YouTube-Downloader/main/YouTube%20Downloader.py", "Youtube Downloader.py")
         input("Downloaded! Run Youtube Downloader.py for the newest version!\nPress Enter to quit.")
         os.remove("outdatedYTDNLDR.py")
         exit()
      else:
         print("\nOkay!\n")
except:
   pass

def download_audio(url, output_path = ""):
    global fflocation
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '/%(title)s',
        'ffmpeg_location': fflocation
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
    print("Audio downloaded successfully.")

def download_video(url, output_path = ""):
    global fflocation
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path + '/%(title)s' + ".mp4",
        'ffmpeg_location': fflocation
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Video downloaded successfully.")

runs = 0

try:
    with open("fflocation.txt", "r") as f:
       fflocation = f.read().split(" -- ")[0]
    parser = argparse.ArgumentParser(description="YT DNLDR")
    parser.add_argument("type", nargs='?', help="av/va/v/a")
    parser.add_argument("url", nargs='?', help="YT URL")
    args = parser.parse_args()
    if args.type and args.url:
        Type = args.type
        url = args.url
        if Type.lower() == "v":
           download_video(url, os.getcwd())
        elif Type.lower() == "a":
           download_audio(url, os.getcwd())
        elif Type.lower() == "an" or Type.lower() == "na":
           download_video(url, os.getcwd())
           download_audio(url, os.getcwd())
    else:
       while True:
         try:
           if runs != 0:
              if r.randint(1, tipchance) == 1:
                 print(tips[r.randint(0, len(tips)-1)])
           x = input("\nv or a\n\nv = video download, a = audio download\nor do va/av for both\nor \"exit\" to quit.\n\n")
           if x.lower() == "a":
             download_audio(input("url: "), "\\Audio\\")
           elif x.lower() == "v":
             download_video(input("url: "), "\\Video\\")
           elif x.lower() == "av" or x.lower() == "va":
               url = input("url: ")
               download_audio(url, "\\Audio\\")
               download_video(url, "\\Video\\")
           elif x.lower() == "exit":
              print("ok bye")
              exit()
           else:
             print("wrong")
         except Exception as e:
           print(e)
           pass
except KeyboardInterrupt:
    print("ok bye")
    exit()
