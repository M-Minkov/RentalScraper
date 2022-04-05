from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from RentalBrowser import RentalBrowser
from RentalProperty import RentalProperty


browser = RentalBrowser()

# List of houses
lowest_price = 300
highest_price = 500
minimum_bedrooms = 2
sort_order = "priceasc"

property_filter = [lowest_price, highest_price, minimum_bedrooms, sort_order]

all_houses = browser.find_all_rentals(property_filter)
browser.end_session()


# for i in all_houses:
#    print(i)
#    print()
