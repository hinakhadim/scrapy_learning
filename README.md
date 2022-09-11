# HumorQuotes

HumorQuotes is a python project, in which I have learned Scrapy and its workflow. There are two spider files; humor_quotes.py and python_spider.py. `humor_quotes` crawls the quotes website while `python_spider` crawls the reddit website. 

## Installation

```bash
pip install Scrapy
cd humorquotes
scrapy genspider example example.com - to generate a spider
```

## Run

```bash
# scrapy crawl quotes - to crawl quotes website

# to crawl the reddit website of python tag
scrapy crawl python_posts
```

## Output

It runs the spider and then output the result in the `reddit_python.csv` file