from src.scraper.scraper import Scraper


class Facade:

    def __init__(self):
        self.scraper = Scraper()

    def prepare(self):
        self.scraper.cnt_pages_to_scrape = 2
        return self.scraper.scrape_url_list()


def main():
    facade = Facade()
    facade.prepare()


if __name__ == '__main__':
    main()
