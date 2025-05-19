Web scraper

So this is not that cliche of a project but expected and this is my take on it.

First off, Web scraping is basically teaching Python to “read” a website and extract useful data from it — like harvesting chocolate chips from a massive cookie (the internet). It’s NOT hacking or stealing hidden data or messing with private backends. You’re just reading the stuff that’s already there in your browser — but doing it smarter.

Humans can’t scroll through 1,000 pages and manually copy data. Scrapers can. Scraping allows to Build datasets from online stores (e.g., prices, product names, ratings), Monitor flight prices / hotel rates, Gather articles or blog posts, Collect stock prices, weather info, job listings, Feed data into ML models or dashboards.

requests is a third-party Python library to send HTTP requests (GET, POST, etc.) what it does is - Connects to a URL, fetches the response (HTML, status codes, headers).it matters because it lets Python talk to websites and APIs like a browser. once we import requests and beautifulSoup -oh beautifulSoup? it's a parsing library from the bs4 package that organizes raw HTML into a searchable structure. What it does is - Converts messy HTML into Python objects (tags, text, attributes), enabling surgical data extraction. It matters because it lets you extract exactly what you need from HTML — headlines, links, product names, anything.

the backend is you choose a target url and download html content of the page. parse the html with beautifulSoup and add code accordingly if you want to get specific elements from that website. and final code for extracting and printing the content you require.

The core program or code is over.

- requests Fetches HTML from a webpage {.get(), .status_code, .text}
- bs4 Parses HTML into a tree structure	{.find(), .text, .select()}

Output i got, 
XD> python web_scraper.py
Quote  : “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
Author : Albert Einstein
Tags   : change, deep-thoughts, thinking, world
--------------------------------------------------------------------------------
Quote  : “It is our choices, Harry, that show what we truly are, far more than our abilities.”
Author : J.K. Rowling
Tags   : abilities, choices
--------------------------------------------------------------------------------
Quote  : “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
Author : Albert Einstein
Tags   : inspirational, life, live, miracle, miracles
--------------------------------------------------------------------------------
Quote  : “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
Author : Jane Austen
Tags   : aliteracy, books, classic, humor
--------------------------------------------------------------------------------
Quote  : “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
Author : Marilyn Monroe
Tags   : be-yourself, inspirational
--------------------------------------------------------------------------------
Quote  : “Try not to become a man of success. Rather become a man of value.”
Author : Albert Einstein
Tags   : adulthood, success, value
--------------------------------------------------------------------------------
Quote  : “It is better to be hated for what you are than to be loved for what you are not.”
Author : André Gide
Tags   : life, love
--------------------------------------------------------------------------------
Quote  : “I have not failed. I've just found 10,000 ways that won't work.”
Author : Thomas A. Edison
Tags   : edison, failure, inspirational, paraphrased
--------------------------------------------------------------------------------
Quote  : “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
Author : Eleanor Roosevelt
Tags   : misattributed-eleanor-roosevelt
--------------------------------------------------------------------------------
Quote  : “A day without sunshine is like, you know, night.”
Author : Steve Martin
Tags   : humor, obvious, simile
--------------------------------------------------------------------------------

if you want to add some additions go for adding Pagination Support, Extract More Fields, Save Output, Formatted CLI Output, Category Scraping, Per-Category Pagination, CLI Support, Modular Structure. I will add these features later in advanced_web_scraper folder - wait a bit!

Also i used this URL: https://quotes.toscrape.com/ because it is a sandbox site made for web scraping learners. Where you get: Quotes, authors, tags, author bios (if you go deeper).

2 libraries were needed here - requests, beautifulsoup4

It used these Python concepts - import, requests.get(), BeautifulSoup, for loop, List comprehension, f-strings.

challenges faced : Targeting correct HTML tags, Handling missing elements, Understanding site structure, Encoding issues.

� how do you run it? open VS code go to terminal after you saved the entire code, just run this command - 'python palindrome_checker.py' (dont forget to install the dependencies i.e, pip install requests beautifulsoup4)

See you in the next one.