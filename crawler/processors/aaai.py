import re

from .base import Processor


class AAAIProcessor(Processor):
    def get_title(self, s: str) -> str:
        return s

    def get_authors(self, s: str) -> str:
        return s

    def get_award(self, s: str) -> str:
        return s

    def get_year(self, s: str) -> str:
        year_short = int(re.search(r"\d{2}", s).group())

        return f"20{year_short}"
