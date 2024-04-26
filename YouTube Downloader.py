try:
   import yt_dlp as youtube_dl
   import requests
except:
   print("You do not have yt_dlp, please run InstallYTDLP.bat to install it.")

version = "V0.01"

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
        print("File downloaded successfully!")
    else:
        print("Failed to download file. Status code:", response.status_code)

currentVersion = ""
changelog = ""

exec(read_github_file("https://raw.githubusercontent.com/GDTMG232/YouTube-Downloader/main/updates.py"))
if currentVersion != version:
   if input(f"You have to update to {currentVersion}!\n{changelog}\n\nWould you like to update?\nY/N: ").lower() == "y":
      download_file("https://raw.githubusercontent.com/GDTMG232/YouTube-Downloader/main/YouTube%20Downloader.py", "NewVersionYTDNLDR.py")
      input("Downloaded! Run NewVersionYTDNLDR.py for the newest version!\nPress Enter to quit.")
      exit()
   else:
      print("\nOkay!\n")

def download_audio(url, output_path = ""):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '/%(title)s',
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
    print("Audio downloaded successfully.")

def download_video(url, output_path = ""):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path + '/%(title)s' + ".mp4",
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Video downloaded successfully.")
    
try:
    while True:
      try:
        x = input("v or a\n\nv = video download, a = audio download\nor do na/an for both\nor \"exit\" to quit.\n\n")
        if x.lower() == "a":
          download_audio(input("url: "), "\\Audio\\")
        elif x.lower() == "v":
          download_video(input("url: "), "\\Video\\")
        elif x.lower() == "an" or x.lower() == "na":
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
