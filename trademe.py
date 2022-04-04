from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

class Place:

    # Saving house rental info
    def __init__(self, URL=None, info=None):

        self.URL = URL
        self.info = info

        # print(Place.split_text(info))

        self.address, \
        self.available, \
        self.bedroom_amount, \
        self.bathroom_amount, \
        self.parking, \
        self.rent = Place.split_text(info)
        

        self.rent_per_person = self.rent // self.bedroom_amount


    def __str__(self):

        result = """
address: {}
URL: {}
bedrooms: {}
price per person: ${}
""".format(self.address, self.URL, self.bedroom_amount, self.rent_per_person)

        return result

    # Splitting the HTML info of the trade me house
    def split_text(TEXT):

        information = TEXT.split("\n")

        remove_text = ["No Photo", "Private listing", "Video"]

        while information[0].split()[0] != "Listed":
            information.pop(0)


        
        address = information[1]
        available = information[2]

        if not information[3].isdigit():
            information = information[:3] + information[4:]
        
        bedrooms = int(information[3])
        bathrooms = int(information[4])
        parking = 0
        rent = 0
        if information[5][0] != "$":
            parking = int(information[5])
            rent = int(information[6].split()[0][1:])

        else:
            rent = int(information[5].split()[0][1:])



        return (address, available, bedrooms, bathrooms, parking, rent)
        
        



lowest_price = 300
highest_price = 500

minimum_bedrooms = 2

sort_order = "priceasc"
page_number = 1

# Setting up Selenium Browser simulation
options = Options()
options.headless = True
browser = Firefox(options=options)

# List of houses
all_houses = []



URL = "https://www.trademe.co.nz/a/property/residential/rent/auckland/auckland-city/city-centre/search?price_min={}&price_max={}&bedrooms_min={}&sort_order={}&page={}".format(
    lowest_price,
    highest_price,
    minimum_bedrooms,
    sort_order,
    page_number)

browser.get(URL)
results = browser.find_elements_by_class_name("tm-property-search-card__link")




while len(results) > 0 :
    print(page_number)
    
    for house in results:

        link = house.get_property("href")
        info = house.text

        all_houses.append(Place(link, info))

    page_number += 1

    URL = "https://www.trademe.co.nz/a/property/residential/rent/auckland/auckland-city/city-centre/search?price_min={}&price_max={}&bedrooms_min={}&sort_order={}&page={}".format(
        lowest_price,
        highest_price,
        minimum_bedrooms,
        sort_order,
        page_number)

    browser.get(URL)
    results = browser.find_elements_by_class_name("tm-property-search-card__link")


#for i in all_houses:
#    print(i)
#    print()
