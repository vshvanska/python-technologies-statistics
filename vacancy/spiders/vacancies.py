import scrapy
from scrapy.http import Response
from urllib.parse import urljoin


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["djinni.co"]
    home_url = "https://djinni.co"

    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response, **kwargs):
        for vacancy in response.css(".list-jobs__item"):
            yield {
                "company": vacancy.css("a.mr-2::text").get().replace("\n", "").strip(),
                "position": vacancy.css(".job-list-item__link::text")
                .get()
                .replace("\n", "")
                .strip(),
                "link": urljoin(
                    self.home_url, vacancy.css(".job-list-item__link::attr(href)").get()
                ),
                "location": vacancy.css(".location-text::text")
                .get()
                .replace("\n", "")
                .strip(),
                "experience": vacancy.css(".nobr:contains('досвіду')::text")
                .get()
                .replace("Без", "0")[0],
                "additional_info": ", ".join(
                    map(
                        str.strip,
                        vacancy.css(".job-list-item__job-info .nobr::text").getall(),
                    )
                ).replace(", ,", ""),
                "date": vacancy.css(".text-muted span::attr(title)").get(),
                "views": vacancy.css(
                    ".text-muted .nobr span[title$='переглядів']::attr(title)"
                )
                .get()
                .split()[0],
                "reviews": vacancy.css(
                    ".text-muted .nobr span[title$='відгуків']::attr(title)"
                )
                .get()
                .split()[0],
                "description": vacancy.css(
                    ".job-list-item__description span::attr(data-original-text)"
                ).get(),
            }
        next_page = response.css(
            "li.page-item.active + li.page-item a.page-link::attr(href)"
        ).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
