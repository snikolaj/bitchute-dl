import subprocess
import requests
import re
import sys
import argparse
from bs4 import BeautifulSoup


if __name__ == "__main__":

    URL = sys.argv[1]

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="video-title").string
    title += ".mp4"

    video = soup.find(id="player").source['src']
    print(video)

    subprocess.run(["curl", video, "-o", title])
