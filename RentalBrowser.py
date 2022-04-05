from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

import tkinter

from RentalProperty import RentalProperty


class RentalBrowser:

    def __init__(self, headless=False):
        self.options = Options()
        self.options.headless = headless
        self.browser = Firefox(options=self.options)
        # browser.get("https://www.trademe.co.nz/a/property/residential/rent/auckland/auckland-city/city-centre/search?price_min=325&price_max=700&bedrooms_min=2")

        self.top = tkinter.Tk()
        self.B = tkinter.Button(self.top, text="Close Selenium", command=self.end_session)
        self.B.pack()
        self.top.mainloop()

    def go_to_page(self, url):
        self.browser.get(url)

    def find_all_rentals(self, property_filter):
        lowest_price, \
        highest_price, \
        minimum_bedrooms, \
        sort_order = property_filter

        page_number = 1

        all_houses = []
        url = "https://www.trademe.co.nz/a/property/residential/rent/auckland/" + \
              "auckland-city/city-centre/search?price_min={}&price_max={}&bedrooms_min={}&sort_order={}&page={}".format(
                  lowest_price,
                  highest_price,
                  minimum_bedrooms,
                  sort_order,
                  page_number)

        self.browser.get(url)
        results = self.browser.find_elements_by_class_name("tm-property-search-card__link")

        while len(results) > 0:
            print(page_number)

            for house in results:
                link = house.get_property("href")
                info = house.text

                all_houses.append(RentalProperty(link, info))

            page_number += 1

            url = "https://www.trademe.co.nz/a/property/residential/rent/auckland/" + \
                  "auckland-city/city-centre/search?price_min={}&price_max={}&bedrooms_min={}&sort_order={}&page={}". \
                      format(
                      lowest_price,
                      highest_price,
                      minimum_bedrooms,
                      sort_order,
                      page_number)

            self.browser.get(url)
            results = self.browser.find_elements_by_class_name("tm-property-search-card__link")
        return all_houses

    def end_session(self):
        self.browser.quit()
        self.top.destroy()


new_browser = RentalBrowser()
