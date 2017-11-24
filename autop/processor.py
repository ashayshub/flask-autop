import logging
import time
import datetime
import requests
from bs4 import BeautifulSoup
from autop.models import db_insert


def get_yearwise_urllist(soup):
    url_list = list()
    now = datetime.datetime.now()
    f = soup.find_all('ul', {'class': 'dropdown-menu'})
    for a in f[0].find_all('a', href=True):
        if str(now.year) in a['href']:
            continue
        url_list.append(f'{a["href"]}')
    return url_list


def format_list(data_type, soup):
    data_list = list()
    p = soup.find_all('div', {'class': 'rtww'})
    for div_tag in p:
        for tag in div_tag.find_all('a'):
            data_list.append({
                'title': tag.h3.text,
                'year': tag.h3.text.split()[0],
                'car_make': tag.h3.text.split()[1],
                'car_model': ' '.join(tag.h3.text.split()[2:]),
                'summary': tag.p.text,
                'car_type': data_type,
                'image': tag.img.text
            })
    return data_list


class Crawler(object):
    """
    Class to crawl through set of URLs
    """

    def __init__(self):
        pass

    def populate(self, urls):

        car_list = list()
        url_prefix = 'http://www.nydailynews.com'

        for car_type, url in urls.items():
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            car_list.extend(format_list(car_type, soup))

            # Process all available years
            # except already processed current year

            for year_url in get_yearwise_urllist(soup):

                # Throttle 1 sec for crawling
                # optional for low intensity crawling
                time.sleep(1)

                r = requests.get(url_prefix + year_url)
                soup = BeautifulSoup(r.text, 'html.parser')
                car_list.extend(format_list(car_type, soup))

            if not car_list:
                return None

        if not db_insert(car_list):
            return False

        return True

