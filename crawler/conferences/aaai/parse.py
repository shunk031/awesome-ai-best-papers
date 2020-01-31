import re
from typing import List
from urllib.request import urlopen

from bs4 import BeautifulSoup

from crawler.handler.base import Handler
from crawler.papers.base import Paper
from crawler.processors.base import Processor


class AAAIHander(Handler):
    def __init__(self, processor: Processor, base_url: str) -> None:
        super().__init__(processor, base_url)

    def get_best_papers(self) -> List[Paper]:

        html = urlopen(self._base_url)
        soup = BeautifulSoup(html, "lxml")

        content_class = soup.find("div", {"class": "content"})

        contents = content_class.get_text().split("\n")

        papers: List[Paper] = []
        for i, content in enumerate(contents):

            cond = re.search(r"AAAI-\d{2} Outstanding Paper Award", content)
            if cond:

                title = self._processor.get_title(contents[i + 1])
                authors = self._processor.get_authors(contents[i + 2])
                award = self._processor.get_award("Outstanding Paper Award")
                year = self._processor.get_year(content)

                papers.append(
                    Paper(title=title, authors=authors, award=award, year=year)
                )

                continue

            cond = re.search(r"AAAI-\d{2} Outstanding Student Paper Award", content)
            if cond:

                title = self._processor.get_title(contents[i + 1])
                authors = self._processor.get_authors(contents[i + 2])
                award = self._processor.get_award("Outstanding Student paper Award")
                year = self._processor.get_year(content)

                papers.append(
                    Paper(title=title, authors=authors, award=award, year=year)
                )
                continue

        return papers
