Requirments:<br>
  Python - 3.7 Minimum - 3.12.3 Recommended
  pip:<br>
    yt_dlp<br>
    argparse<br>
    command: pip install yt_dlp argparse<br>
  other:<br>
    ffmpeg<br>
    link: https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z<br>

<h1>How to use</h1><br>
In <b>fflocation.txt</b> replace <b>YOUR_FFMPEG_DIRECTORY</b> with the directory where ffmpeg.exe is located.<br>
With cmd, run the command <b>pip install yt_dlp argparse</b> in order to install required modules.<br>
<br>
Then run YouTube Downloader.py and it should work.<br>
<h2>If it doesn't work</h2><br>
<h5>Script Errors</h5>
<i>ModuleNotFoundError</i> - You haven't installed either yt_dlp or argparse - Run <b>pip install yt_dlp argparse</b><br>
<i>ERROR: ffmpeg not found. Please install or provide the path using --ffmpeg-location</i> - Have you set the correct directory in <b>fflocation.txt</b>?

<h5>Other errors</h5>
If it doesn't open properly - You more than likely haven't got Python installed. https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe<br>
If something doesn't work in the script itself - Try updating yt-dlp or argparse <b>pip install --upgrade yt-dlp</b> <b>pip install --upgrade argparse</b>
