from typing import List

from crawler.papers.base import Paper
from crawler.processors.base import Processor


class Handler(object):
    def __init__(self, processor: Processor, base_url: str) -> None:
        self._processor = processor
        self._base_url = base_url

    def get_best_papers(self) -> List[Paper]:
        raise NotImplementedError
