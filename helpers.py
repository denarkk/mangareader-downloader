import re # Regular Expressions
import os # Operating System
import requests
import shutil

provider = "http://www.mangareader.net/"

def is_not_released(series, episode):
  dst = url(series, episode)
  r   = requests.get(dst) # Request to page
  src = r.text # Source code of the page

  return "not released" in src

def dashes(manga):
  return re.sub("\s+", "-", manga)

def url(manga, episode, page = 1):
  return provider + dashes(manga) + "/" + str(episode) + "/" + str(page)

def get_img(url, path, page):
  if not os.path.exists(path):
    os.makedirs(path)

  img_name = str(page) + ".jpg"

  r = requests.get(url, stream = True)
  with open(path + img_name, 'wb') as f:
    r.raw.decode_content = True
    shutil.copyfileobj(r.raw, f)

  print("Downloading page " + str(page))