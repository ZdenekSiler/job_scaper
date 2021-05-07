import requests
from bs4 import BeautifulSoup


class Scraper:
    # class variables
    base_url = "https://www.jobs.cz/prace/"
    segments = ['is-it-konzultace-analyzy-a-projektove-rizeni', 'is-it-sprava-systemu-a-hw', 'is-it-vyvoj-aplikaci-a'
                                                                                             '-systemu']
    city = 'praha'
    cnt_pages_to_scrape = 3

    def get_url(self):
        url_dict = []
        pg_nm = 1
        while pg_nm < self.cnt_pages_to_scrape:
            for segment in self.segments:
                url = self.base_url + self.city + "/" + segment + "?page=" + str(pg_nm)
                url_dict.append(url)
            pg_nm = pg_nm + 1
        return url_dict

    def scrape_url_list(self):
        for url in self.get_url():
            try:
                response = requests.get(url)
                url_content = BeautifulSoup(response.content, 'html.parser')
                # print(self.get_main_content(url_content))
                job_title, address, company = self.get_main_content(url_content)
                job_link = [title_link.find("a").attrs['href'] for title_link in job_title]
                job_text = [title_link.find("a").text for title_link in job_title]
                # salary = url_content.find_all('div', {"class": "search-list__salary"})
                job_company = [co.text.strip() for co in company]
                print(f"job_link:{job_link},job_text:{job_text},job_company:{job_company}")

            except Exception as e:
                print(e)

    @staticmethod
    def get_main_content(url_content):
        for job in url_content.find_all('div', {"class": "search-list__main-info"}):
            job_title = job.find_all('h3', {"class": "search-list__main-info__title"})
            address = job.find_all('div', {"class": "search-list__main-info__address"})
            company = job.find_all('div', {"class": "search-list__main-info__company"})
            return job_title, address, company
