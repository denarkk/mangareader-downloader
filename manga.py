import requests as req
from helpers import *
from bs4 import BeautifulSoup as bs
import sys

globalpath = "C:/Manga/"

def get_manga(series, episode):
  page = 1 # Initial page
  download_path = globalpath + series + "/" + episode + "/"

  # Check to see if the episode exists
  if is_not_released(series, episode):
    print("Episode not released")
    return None

  while True:
    dst = url(series, episode, page)
    r   = req.get(dst) # Request to page
    src = r.text # Source code of the page

    # If the page doesn't exist...
    if r.status_code != 200:
      break # Exit the loop

    # Crawl the page to download manga image
    source = bs(src, "html.parser")
    for imglink in source.findAll("img", {"id": "img"}):
      img = imglink.get("src")
      get_img(img, download_path, page)

    # Go to the next page
    page = page + 1

  print("Finished downloading " + series + " " + episode)

get_manga(sys.argv[1], sys.argv[2])