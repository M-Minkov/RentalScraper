from RentalBrowser import RentalBrowser
from RentalProperty import RentalProperty

browser = RentalBrowser(headless=False)

# List of houses
lowest_price = 300
highest_price = 500
minimum_bedrooms = 2
sort_order = "priceasc"

property_filter = [lowest_price, highest_price, minimum_bedrooms, sort_order]

all_houses = browser.find_all_rentals(property_filter)


f=open("stuff.csv", "w+")

f.write(RentalProperty.CSV_HEADER + "\n")
for i in all_houses[:10]:
    f.write(i.get_csv_format() + "\n")

f.close()

# browser.end()