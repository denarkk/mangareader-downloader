import sys
from cx_Freeze import setup, Executable

setup(
  name = "Mangareader Downloader",
  version = "1.0",
  description = "Download manga from MangaReader.net",
  executables = [Executable("manga.py", base = "Win32GUI")])