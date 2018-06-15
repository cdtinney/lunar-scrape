# lunar-scrape
> A simple Python script to scrape NASA's Planetary Data System (PDS) website and download images of the Moon.

I found these images from [this article](http://www.worldofindie.co.uk/?p=682) ([HackerNews discussion](https://news.ycombinator.com/item?id=17311005)).

## Getting Started

### Requirements

* Python 2.7
* `urllib2`
* `pathlib2`
* `multiprocessing`

### Running

To download all images, run:
```
python lunar-scrape.py
```

This will download all images to the `/images` directory, preserving the original folder structure.
