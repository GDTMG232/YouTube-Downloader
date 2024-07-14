try:
   import yt_dlp as youtube_dl
   import requests
   import os
   import random
   import argparse
   from getpass import getuser as getUsername
except:
   print("You don't have all required modules, use Requirements.bat to install the modules needed.")
   input("")
   exit()

version = "V0.18"

quality = True # Set this to False if you would like videos to be downloaded faster | Does degrade quality

def read_github_file(raw_url):
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file: {e}")
        return None

def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
    except requests.RequestException as e:
        print(f"Failed to download file: {e}")

tips = [
    "\nDidn't download properly? Run 'pip install --upgrade yt-dlp' in your command line!\n",
    "\nHaving issues with download? Try updating Youtube Downloader or run 'pip install --upgrade yt_dlp'\n"
]

tip_chance = 20

current_version = ""
changelog = ""

def check_for_update():
    global current_version, changelog
    script_content = read_github_file("https://raw.githubusercontent.com/GDTMG232/YouTube-Downloader/main/updates.py")
    if script_content:
        for line in script_content.split('\n'):
            if line.startswith("currentVersion"):
                current_version = line.split('=')[1].strip().strip('"')
            elif line.startswith("changelog"):
                changelog = line.split('=')[1].strip().strip('"')

        if current_version and current_version != version:
            update = input(f"You need to update from {version} to {current_version}!\n{changelog}\n\nWould you like to update? (Y/N) or no and don't ask again (A): ").strip().lower()
            if update == "y":
                os.rename(__file__, "old_YT_Downloader.py")
                download_file("https://raw.githubusercontent.com/GDTMG232/YouTube-Downloader/main/YouTube%20Downloader.py", "Youtube Downloader.py")
                input("Downloaded! Run 'Youtube Downloader.py' for the newest version!\nPress Enter to quit.")
                os.remove("old_YT_Downloader.py")
                exit()
            else:
                if update == "a":
                   with open(f"{directory}\\Do Update Remind.txt", "w") as f:
                     f.write("N")
                   print("Won't ask again.")
                else:
                   print("Okay!")
                   

def download_audio(url, output_path=""):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': fflocation
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
    print("Audio downloaded successfully.")

def download_video(url, output_path=""):
    options = {
        'format': 'bestvideo+bestaudio/best' if quality else 'best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': fflocation
    }

    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
    print("Video downloaded successfully.")

def main():
    global fflocation

    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fflocation.txt"), "r") as f:
            fflocation = f.read().strip().split(" -- ")[0]
    except FileNotFoundError:
        print("fflocation.txt not found. Please ensure the file exists.")
        exit()

    parser = argparse.ArgumentParser(description="YT DNLDR")
    parser.add_argument("type", nargs='?', help="av/va/v/a")
    parser.add_argument("url", nargs='?', help="YouTube URL")
    args = parser.parse_args()

    if args.type and args.url:
        if args.type.lower() == "v":
            download_video(args.url)
        elif args.type.lower() == "a":
            download_audio(args.url)
        elif args.type.lower() in ["av", "va"]:
            download_audio(args.url)
            download_video(args.url)
    else:
        interactive_mode()

def interactive_mode():
    runs = 0

    while True:
        try:
            if runs > 0 and random.randint(1, tip_chance) == 1:
                print(random.choice(tips))

            choice = input("\nv or a\n\nv = video download, a = audio download\nor do va/av for both\nor 'exit' to quit.\n\n").strip().lower()
            if choice == "a":
                url = input("URL(s) or playlist(s): ").strip()
                for link in url.split(","):
                   download_audio(link.strip(), "Audio")
            elif choice == "v":
                url = input("URL(s) or playlist(s): ").strip()
                for link in url.split(","):
                   download_video(link.strip(), "Video")
            elif choice in ["av", "va"]:
                url = input("URL(s) or playlist(s): ").strip()
                for link in url.split(","):
                   download_audio(link.strip(), "Audio")
                   download_video(link.strip(), "Video")
            elif choice == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 'v', 'a', 'av', 'va', or 'exit'.")
            runs += 1
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
   directory = f"C:\\Users\\{getUsername()}\\AppData\\Local\\TMG\\YT Downloader"
   if not os.path.exists(f"C:\\Users\\{getUsername()}\\AppData\\Local\\TMG\\YT Downloader\\Do Update Remind.txt"):
      os.makedirs(directory, exist_ok=True)
      with open(f"{directory}\\Do Update Remind.txt", "x") as f:
         pass
      with open(f"{directory}\\Do Update Remind.txt", "a") as f:
         f.write("Y -- Set to N if you don't want updates.")
   with open(f"{directory}\\Do Update Remind.txt", "r") as f:
      if f.read().startswith("Y"):
         check_for_update()
   main()
