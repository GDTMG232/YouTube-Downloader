try:
    import yt_dlp as youtube_dl
    import requests
    import time
    import os
    import random
    import argparse
    from getpass import getuser as getUsername
except ImportError:
    print("You don't have all required modules.")
    if input("Would you like to install them? (Y/N)\n").lower() == "y":
        import os
        os.system("python -m pip install argparse yt_dlp")
        os.system("cls" if os.name == "nt" else "clear")
        import yt_dlp as youtube_dl
        import requests
        import random
        import argparse
        from getpass import getuser as getUsername
    else:
        exit()

os.system("title YouTube Downloader" if os.name == "nt" else 'echo -ne "\033]0;YouTube Downloader\007"')

version = "V0.19"

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

# Use the user's home directory to construct paths
home_dir = os.path.expanduser("~")
directory = os.path.join(home_dir, "AppData", "Local", "TMG", "YT Downloader")

# For cross-platform compatibility, ensure it works on non-Windows systems
if os.name != 'nt':
    directory = os.path.join(home_dir, "YT_Downloader")  # Modify this as needed for non-Windows systems

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

        if current_version and current_version != version and (float(current_version.replace("V", "")) > float(version.replace("V", ""))):
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

def parse_arguments():
    parser = argparse.ArgumentParser(description="Download YouTube Videos without sketchy websites!")
    parser.add_argument("type", nargs='?', choices=['v', 'a', 'av', 'va'], 
                        help="Type of download: 'v' for video, 'a' for audio, 'av' for audio and video, 'va' for video and audio")
    parser.add_argument("url", nargs='?', help="YouTube URL or playlist URL")
    return parser.parse_args()

def main():
    global fflocation

    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fflocation.txt"), "r") as f:
            fflocation = f.read().strip().split(" -- ")[0]
    except FileNotFoundError:
        print("fflocation.txt not found. Please ensure the file exists.")
        exit()

    args = parse_arguments()

    if args.type and args.url:
        if args.type == "v":
            if "youtube" in args.url.lower():
                download_video(args.url)
            else:
                print("This is not a YouTube URL.")
        elif args.type == "a":
            if "youtube" in args.url.lower():
                download_audio(args.url)
            else:
                print("This is not a YouTube URL.")
        elif args.type in ["av", "va"]:
            if "youtube" in args.url.lower():
                download_video(args.url)
                download_audio(args.url)
            else:
                print("This is not a YouTube URL.")
    else:
        directory = os.path.join(home_dir, "AppData", "Local", "TMG", "YT Downloader") if os.name == 'nt' else os.path.join(home_dir, "YT_Downloader")
        if not os.path.exists(directory):
            os.makedirs(directory)
        remind_file = os.path.join(directory, "Do Update Remind.txt")
        if not os.path.exists(remind_file):
            with open(remind_file, "w") as f:
                f.write("Y -- Set to N if you don't want updates.")
            print("This is your first time using YouTube Downloader.")
        with open(remind_file, "r") as f:
            if f.read().startswith("Y"):
                check_for_update()
        interactive_mode()

def interactive_mode():
    runs = 0

    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            doDownload = True
            if runs > 0 and random.randint(1, tip_chance) == 1:
                print(random.choice(tips))

            choice = input("\nv or a\n\nv = video download, a = audio download\nor do va/av for both\nor 'exit' to quit.\n\n").strip().lower()
            if choice == "a":
                url = input("URL(s) or playlist(s) (split with \",\": ").strip()
                if not "youtube" in url:
                    print("This is not a YouTube URL!")
                    doDownload = False
                if doDownload:
                    for link in url.split(","):
                        download_audio(link.strip(), "Audio")
            elif choice == "v":
                url = input("URL(s) or playlist(s) (split with \",\": ").strip()
                if not "youtube" in url:
                    print("This is not a YouTube URL!")
                    doDownload = False
                if doDownload:
                    for link in url.split(","):
                        download_video(link.strip(), "Video")
            elif choice in ["av", "va"]:
                url = input("URL(s) or playlist(s) (split with \",\": ").strip()
                if not "youtube" in url:
                    print("This is not a YouTube URL!")
                    doDownload = False
                if doDownload:
                    for link in url.split(","):
                        download_audio(link.strip(), "Audio")
                        download_video(link.strip(), "Video")
            elif choice == "exit":
                print("Goodbye!")
                return
            else:
                print("Invalid choice. Please enter 'v', 'a', 'av', 'va', or 'exit'.")
            runs += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
   
   main()
