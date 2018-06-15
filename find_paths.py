# Import libraries
import urllib2
from functools import reduce
import itertools
from bs4 import BeautifulSoup

root_url = 'https://pds-imaging.jpl.nasa.gov/data/lo/LO_1001/EXTRAS/BROWSE/'

def find_sub_dir_paths(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    subdirs = soup.find_all('td', class_='indexcolname')[1:]
    subdir_names = list(map(lambda subdir: subdir.find('a')['href'], subdirs))
    return subdir_names

def find_sub_dir_paths_and_add_prefix(url, prefix):
    return list(map(lambda sub_dir: prefix + sub_dir, find_sub_dir_paths(url)))

def find_rel_sub_dir_paths(url, paths):
    return list(map(lambda sub_dir: find_sub_dir_paths_and_add_prefix(url + '/' + sub_dir, sub_dir), paths))
    
def flatten(list_of_lists):
    return list(itertools.chain.from_iterable(list_of_lists))

print('Scraping paths...')

loc_dir_paths = find_sub_dir_paths(root_url)
frame_dir_paths = flatten(find_rel_sub_dir_paths(root_url, loc_dir_paths))
image_paths = flatten(find_rel_sub_dir_paths(root_url, frame_dir_paths))

image_path_file = open('image_paths.txt', 'w')
for path in image_paths:
    print >> image_path_file, path
image_path_file.close()
