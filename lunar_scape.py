import os
import urllib2
import pathlib2
from multiprocessing.dummy import Pool

root_url = 'https://pds-imaging.jpl.nasa.gov/data/lo/LO_1001/EXTRAS/BROWSE/'
default_base_dir = 'images'

image_paths_file = open('image_paths.txt', 'r')
image_paths = [line.rstrip('\n') for line in image_paths_file.readlines()]
image_paths_file.close()

def download_image(url, image_path):
    return urllib2.urlopen(url + '/' + image_path).read()

def save_image(base_dir, image_path, image):
    full_image_path = base_dir + '/' + image_path
    save_path = os.path.dirname(full_image_path)
    pathlib2.Path(save_path).mkdir(parents=True, exist_ok=True)
    image_file = open(full_image_path, 'wb')
    image_file.write(image)
    image_file.close()

def download_and_save_image(image_path):
    save_image(default_base_dir, image_path, download_image(root_url, image_path))

def lunar_scrape():
    Pool(4).map(download_and_save_image, image_paths)

lunar_scrape()
