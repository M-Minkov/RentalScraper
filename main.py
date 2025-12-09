from RentalBrowser import RentalBrowser
from RentalProperty import RentalProperty
import os

def get_int_input(prompt, default):
    val = input(f"{prompt} [{default}]: ")
    return int(val) if val.strip() else default

def get_str_input(prompt, default):
    val = input(f"{prompt} [{default}]: ")
    return val.strip() if val.strip() else default

print("Enter filter values (press Enter to use default):")
lowest_price = get_int_input("Lowest price", 300)
highest_price = get_int_input("Highest price", 500)
minimum_bedrooms = get_int_input("Minimum bedrooms", 2)
sort_order = get_str_input("Sort order (e.g. priceasc)", "priceasc")
property_limit = get_int_input("How many properties to collect data on? (Warning: large numbers can take a while)", 10)
headless_input = get_str_input("Run browser in headless mode? (yes/no)", "yes")
headless = headless_input.lower() in ['yes', 'y', 'true', '1']

property_filter = [lowest_price, highest_price, minimum_bedrooms, sort_order]

browser = RentalBrowser(headless=headless)

all_houses = browser.find_all_rentals(property_filter)

os.makedirs("output_folder", exist_ok=True)
out_path = os.path.join("output_folder", "output.csv")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(RentalProperty.CSV_HEADER + "\n")
    for i in all_houses[:property_limit]:
        f.write(i.get_csv_format() + "\n")

browser.end()