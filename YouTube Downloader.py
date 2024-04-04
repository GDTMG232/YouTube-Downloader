try:
   import yt_dlp as youtube_dl
except:
   print("You do not have yt_dlp, please run InstallYTDLP.bat to install it.")

def download_audio(url, output_path = ""):
    """
    Download audio from YouTube given a URL and save it to the specified path.
    
    Parameters:
        url (str): The URL of the YouTube video.
        output_path (str): The path where the downloaded audio will be saved.
    """
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
    """
    Download video from YouTube given a URL and save it to the specified path.
    
    Parameters:
        url (str): The URL of the YouTube video.
        output_path (str): The path where the downloaded video will be saved.
    """
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path + '/%(title)s' + ".mp4",
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Video downloaded successfully.")

# Example usage:
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
