import re
from pprint import pprint
from typing import List

import requests
from bs4 import BeautifulSoup

from crawler.papers.base import Paper


def get_best_papers(year):

    URL = f"http://cvpr{year}.thecvf.com/program/main_conference"

    req = requests.get(URL)
    req.raise_for_status()

    soup = BeautifulSoup(req.text)

    content_class = soup.find_all("ul")[4]
    contents = content_class.get_text().split("\n")

    contents = [x for x in contents if x]

    papers: List[Paper] = []

    is_best_paper_award = False
    is_best_student_paper_award = False
    is_best_paper_honorable_mention = False

    for content in contents:
        cond = re.search("Best Paper Award", content)
        if cond:
            is_best_paper_award = True
            continue

        cond = re.search("Best Student Paper Award", content)
        if cond:
            is_best_paper_award = False
            is_best_student_paper_award = True
            continue

        cond = re.search("Best Paper Honorable Mention", content)
        if cond:
            is_best_student_paper_award = False
            is_best_paper_honorable_mention = True
            continue

        title = re.search(r'"(.*?)(?<!\\)"', content)
        if not title:
            break

        title = title.group().replace('"', "")
        authors = content.replace(title, "").replace("by", "")[2:]

        if is_best_paper_award:
            award = "Best Paper Award"
        elif is_best_student_paper_award:
            award = "Best Student Paper Award"
        elif is_best_paper_honorable_mention:
            award = "Best Paper Honorable Mention"
        else:
            raise ValueError()

        papers.append(Paper(title=title, authors=authors, award=award, year=year))

    return papers


for y in range(0, 100):
    print(2019 - y)
    pprint(get_best_papers(2019 - y))
