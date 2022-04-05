class RentalProperty:

    # Saving house rental info
    def __init__(self, new_url=None, raw_data=None):

        self.URL = new_url
        self.info = raw_data

        # print(Place.split_text(info))

        self.address, \
            self.available, \
            self.bedroom_amount, \
            self.bathroom_amount, \
            self.parking, \
            self.rent = RentalProperty.split_text(self.info)

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
    @staticmethod
    def split_text(text):

        information = text.split("\n")

        # remove_text = ["No Photo", "Private listing", "Video"]

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

        return address, available, bedrooms, bathrooms, parking, rent
