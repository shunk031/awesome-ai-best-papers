from dataclasses import dataclass


@dataclass
class Paper(object):
    title: str
    authors: str
    year: int
    award: str
