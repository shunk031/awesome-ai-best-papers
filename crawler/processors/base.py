class Processor(object):
    def get_title(self, s: str) -> str:
        raise NotImplementedError

    def get_authors(self, s: str) -> str:
        raise NotImplementedError

    def get_year(self, s: str) -> str:
        raise NotImplementedError

    def get_award(self, s: str) -> str:
        raise NotImplementedError
