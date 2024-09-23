# YouTube Downloader
Available on Unix (Linux & MacOS) and NT (Windows) systems.

Current Version - V0.21 ([Release Notes](#v021-release-notes))

[Releases](https://github.com/GDTMG232/YouTube-Downloader/releases)

## Requirements
- **Python**: 3.7+ (3.12.4 Recommended)
  - [Download Python 3.12.4 - Windows EXE](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe)
- **pip**:
  - `yt_dlp`
  - `argparse`
  - NT: Install with: `pip install yt_dlp argparse`
  - UNIX: Install with: `pip3 install yt_dlp argparse --break-system-packages`
- **ffmpeg**:
  - [Download ffmpeg - Windows](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)
  - Unzip the ffmpeg `.7z` file to a designated folder.
  - [Download ffmpeg - Linux Ubuntu](https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/ffmpeg/7:6.1.1-5ubuntu8/ffmpeg_6.1.1.orig.tar.xz)
  - Unzip the ffmpeg `.tar.xz` file to a designated folder.

## Installation Instructions

1. **Install Python and pip**:
   - Download and install Python from the link above.
   - Make sure pip is included during the Python installation.

2. **Install ffmpeg**:
   - Download ffmpeg from the link above.
   - Unzip the file to a folder where you won’t accidentally delete it.

3. **Install Python Packages**:
   - For NT - Open CMD and run: `pip install yt_dlp argparse`
   - For UNIX - Open Terminal and run: `pip3 install yt_dlp argparse --break-system-packages`

4. **Set up ffmpeg location**:
   - In the YouTube Downloader folder, create or edit `fflocation.txt`.
   - For NT - Add the directory path to ffmpeg, but **do not include** `ffmpeg.exe` in the path.
     - **Correct Format**: `path\to\your\ffmpeg\`
     - **Incorrect Format**: `path\to\your\ffmpeg\ffmpeg.exe`

## How to Use

1. **Edit `fflocation.txt`**:
   - Replace `YOUR_FFMPEG_DIRECTORY` with the path to your ffmpeg folder.

2. **Run the YouTube Downloader**:
   - Open CMD and navigate to the YouTube Downloader folder.
   - For NT: Run: `python "YouTube Downloader.py"`
   - For UNIX: Run: `python3 "YouTube Downloader.py"`
  
3. **If you want to have higher quality downloads**
   - Open DownloadSettings.json, using a text editor of some sort
   - Set "enabled" to "true"
   - This will increase quality, but will slow down downloads of playlists and whatnot.

## Troubleshooting

### Script Errors
- **ModuleNotFoundError**: 
  - You haven't installed `yt_dlp` or `argparse`. 
  - Run: `pip install yt_dlp argparse`
- **ERROR: ffmpeg not found**:
  - Ensure the correct directory is set in `fflocation.txt`.

### Other Errors
- **Application won't open**:
  - Make sure Python is installed: [Download Python 3.12.4 Windows](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe)
- **Script issues**:
  - Update `yt_dlp` or `argparse`:
    - `pip install --upgrade yt_dlp` | `pip3 install --upgrade yt_dlp --break-system-packages`
    - `pip install --upgrade argparse` | `pip3 install --upgrade argparse --break-system-packages`

<hr>
# V0.21 Release Notes
Added internet checking and made HQ downloads actually work

Get V0.21 [here](https://github.com/GDTMG232/YouTube-Downloader/releases/tag/V0.21)!
