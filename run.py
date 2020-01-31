from crawler.conferences.aaai.parse import AAAIHander
from crawler.processors.aaai import AAAIProcessor


def main():

    handler = AAAIHander(
        processor=AAAIProcessor(), base_url="https://aaai.org/Awards/paper.php"
    )
    papers = handler.get_best_papers()

    import ipdb

    ipdb.set_trace()


if __name__ == "__main__":
    main()
