import sys
import os
import urllib2
import pathlib2
import argparse
from multiprocessing.dummy import Pool

def safe_print(content):
  sys.stdout.write(content)

parser = argparse.ArgumentParser(description='Scrape lunar images from NASA.')
parser.add_argument('--preserve-dir', dest='preserve_dir', action='store_true',
                    help='Preserve directory')
args = parser.parse_args()

root_url = 'https://pds-imaging.jpl.nasa.gov/data/lo/LO_1001/EXTRAS/BROWSE/'
default_base_dir = 'images'

image_paths_file = open('image_paths.txt', 'r')
image_paths = [line.rstrip('\n') for line in image_paths_file.readlines()]
image_paths_file.close()

def download_image(url, image_path):
  full_url = url + '/' + image_path
  return urllib2.urlopen(full_url).read()

def get_save_path(base_dir, preserve_dir, image_path):
  if preserve_dir:
    return base_dir + '/' + image_path
  else:
    return base_dir + '/' + image_path.replace('/', '_')

def save_image(base_dir, preserve_dir, image_path, image):
    save_path = get_save_path(base_dir, preserve_dir, image_path)
    save_path_parent_dir = os.path.dirname(save_path)
    pathlib2.Path(save_path_parent_dir).mkdir(parents=True, exist_ok=True)
    safe_print('  {}\n'.format(save_path))
    image_file = open(save_path, 'wb')
    image_file.write(image)
    image_file.close()

def download_and_save_image(image_path):
    save_image(default_base_dir, args.preserve_dir, image_path, download_image(root_url, image_path))

def lunar_scrape():
    print('Downloading {} images...'.format(len(image_paths)))
    Pool(4).map(download_and_save_image, image_paths)

lunar_scrape()
