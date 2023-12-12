#wget clone
import requests
import os
import sys
from tqdm import tqdm

def download_file(url):
    filename = url.split('/')[-1]
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as bar:
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
    print(f"Downloaded {url} to {filename}")
        
    

def download_from_list(file_path):
    with open(file_path, "r") as file:
        for line in file:
            url = line.strip()
            if url:
                download_file(url)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        for line in sys.stdin: #this is for piping read from stdin
            url = line.strip()
            if url:
                download_file(url)
    if len(sys.argv) == 2:
        download_file(sys.argv[1])
    elif len(sys.argv) == 3 and sys.argv[1] == "-b":
        download_from_list(sys.argv[2])
    else:
        print("Usage: python wget.py <url>")
        print("   or: python wget.py -b <file_path>")
