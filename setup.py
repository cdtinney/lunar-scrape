from setuptools import setup

setup(name='lunar-scrape',
      version='0.1',
      url='http://github.com/cdtinney/lunar-scrape',
      author='Colin Tinney',
      author_email='me@colintinney.com',
      license='MIT',
      packages=['lunar-scrape'],
      install_requires=[
        'pathlib2',
        'multiprocessing',
      ],
      zip_safe=False)
