# YouTube Downloader
Available on Unix (Linux & MacOS) and NT (Windows) systems.


## Requirements
- **Python**: 3.7+ (3.12.3 Recommended)
  - [Download Python 3.12.3](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe)
- **pip**:
  - `yt_dlp`
  - `argparse`
  - Install with: `pip install yt_dlp argparse`
- **ffmpeg**:
  - [Download ffmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)
  - Unzip the ffmpeg `.7z` file to a designated folder.

## Installation Instructions

1. **Install Python and pip**:
   - Download and install Python from the link above.
   - Make sure pip is included during the Python installation.

2. **Install ffmpeg**:
   - Download ffmpeg from the link above.
   - Unzip the file to a folder where you won’t accidentally delete it.

3. **Install Python Packages**:
   - Open CMD and run: `pip install yt_dlp argparse`

4. **Set up ffmpeg location**:
   - In the YouTube Downloader folder, create or edit `fflocation.txt`.
   - Add the directory path to ffmpeg, but **do not include** `ffmpeg.exe` in the path.
     - **Correct Format**: `path\to\your\ffmpeg\`
     - **Incorrect Format**: `path\to\your\ffmpeg\ffmpeg.exe`

## How to Use

1. **Edit `fflocation.txt`**:
   - Replace `YOUR_FFMPEG_DIRECTORY` with the path to your ffmpeg folder.

2. **Run the YouTube Downloader**:
   - Open CMD and navigate to the YouTube Downloader folder.
   - Run: `python YouTubeDownloader.py`

## Troubleshooting

### Script Errors
- **ModuleNotFoundError**: 
  - You haven't installed `yt_dlp` or `argparse`. 
  - Run: `pip install yt_dlp argparse`
- **ERROR: ffmpeg not found**:
  - Ensure the correct directory is set in `fflocation.txt`.

### Other Errors
- **Application won't open**:
  - Make sure Python is installed: [Download Python 3.12.3](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe)
- **Script issues**:
  - Update `yt_dlp` or `argparse`:
    - `pip install --upgrade yt_dlp`
    - `pip install --upgrade argparse`
