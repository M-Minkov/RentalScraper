from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from RentalProperty import RentalProperty


class RentalBrowser:

    def __init__(self, headless=False):
        self.options = Options()
        if headless:
            self.options.add_argument('--headless=new')
        self.browser = Firefox(options=self.options)

    # Wrapper for going to URL
    def go_to_page(self, url):
        self.browser.get(url)

    # Starts the web driver engine
    def start(self):
        self.browser = Firefox(options=self.options)

    # Closes the web driver engine
    def end(self):
        self.browser.quit()

    # Grabs all the property tags from the HTML file
    # Returns list of HTML classes
    def grab_properties(self):
        houses = self.grab_small_cards() + self.grab_big_cards()
        return houses

    # Grabs properties that are given a small card CSS class
    def grab_small_cards(self):
        small_cards = self.browser.find_elements(By.CLASS_NAME, "tm-property-search-card__link")
        return small_cards

    # Grabs properties that are given a big card CSS class
    # There is no difference between the 2 properties, other than
    # how they are displayed (big or small) on the html page.
    def grab_big_cards(self):
        big_cards = []
        return big_cards


    # Grabs all rentals off of Trade Me, that match the filter, and saves them into a list with the RentalProperty class
    # Returns list of RentalProperty class types.
    def find_all_rentals(self, property_filter):
        # self.start()
        lowest_price, \
        highest_price, \
        minimum_bedrooms, \
        sort_order = property_filter

        page_number = 1

        all_houses = []

        # while len(results) > 0:
        while page_number < 2:
            print(page_number)
            url = "https://www.trademe.co.nz/a/property/residential/rent/auckland/" + \
                  "auckland-city/city-centre/search?price_min={}&price_max={}&bedrooms_min={}&sort_order={}&page={}". \
                      format(
                      lowest_price,
                      highest_price,
                      minimum_bedrooms,
                      sort_order,
                      page_number)
            self.go_to_page(url)

            results = self.grab_properties()

            for house in results:
                link = house.get_property("href")
                info = house.text

                all_houses.append(RentalProperty(link, info))

            page_number += 1

        # self.end()
        return all_houses
