# lunar-scrape
> A simple Python script to scrape NASA's Planetary Data System (PDS) website and download images of the Moon.

I found these images from [this article](http://www.worldofindie.co.uk/?p=682) ([HackerNews discussion](https://news.ycombinator.com/item?id=17311005)). Direct link to images is [here](https://pds-imaging.jpl.nasa.gov/data/lo/LO_1001/EXTRAS/BROWSE/).

Image paths are scraped via `scrape_paths.py` script and saved to `images.txt`.

## Getting Started

### Requirements

For all scripts:

* Python 2.7
* `urllib2`

To run `lunar_scrape.py` (the main script), you'll need:

* `pathlib2`
* `multiprocessing`

To run `find_paths.py`, you'll need:

* `functools`
* `itertools`
* `bs4` (BeautifulSoup)

### Running

To download all images, run:
```
python lunar_scrape.py
```

This will download all images to the `/images` directory, flattening them into a single directory.

To preserve the original directory, run:
```
python lunar_scrape.py --preserve-dir
```
