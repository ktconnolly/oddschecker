from collections import defaultdict, namedtuple
from operator import attrgetter

import requests
from bs4 import BeautifulSoup


class Oddschecker:
    def __init__(self, url):
        self.url = url
        self._soup = None

    def get_books(self):
        self._get_soup()

        books = []
        for row in self._get_table_head():
            elem = row.find("a")
            if elem and elem.has_attr("title"):
                books.append(elem["title"])
        return books

    def get_prices(self, target_books=None):
        all_books = self.get_books()

        if not target_books:
            target_books = all_books

        Book = namedtuple("Book", "name price")
        prices = defaultdict(list)

        for row in self._get_table_body():
            col = 0
            for elem in row:
                if not self._is_price(elem):
                    continue

                price = self._get_decimal_odds(elem)
                book_name = all_books[col]
                selection = row["data-bname"]

                if self._price_open(elem) and book_name in target_books:
                    prices[selection].append(Book(book_name, price))

                col += 1

        return self._sorted(prices)

    def _get_soup(self):
        r = requests.get(
            self.url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/72.0.3626.121 Safari/537.36"
            },
        )
        self._soup = BeautifulSoup(r.text, "html.parser")

    def _get_table_head(self):
        return self._soup.find("tr", {"class": "eventTableHeader"})

    def _get_table_body(self):
        return self._soup.find("tbody", id="t1")

    @staticmethod
    def _get_decimal_odds(elem):
        return float(elem["data-odig"])

    @staticmethod
    def _is_price(elem):
        return "data-odig" in elem.attrs

    @staticmethod
    def _price_open(elem):
        return elem.findChild()

    @staticmethod
    def _sorted(prices):
        for market in prices:
            prices[market] = sorted(
                prices[market], key=attrgetter("price"), reverse=True
            )
        return prices
