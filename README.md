# RentalScraper
Collect rental listings from Trade Me and save them to a CSV file.

This repository contains a small command-line scraper that opens a browser, applies filters, and writes the results to `stuff.csv` for later analysis.

**Prerequisites**
- Python 3.11 or newer
- A supported browser and corresponding WebDriver on your PATH (Chrome/Chromium + `chromedriver`, Firefox + `geckodriver`, Edge + `msedgedriver`)
- Project dependencies listed in `requirements.txt`

**Setup (Windows PowerShell)**
1. Install dependencies:

```powershell
pip install -r requirements.txt
```

**Run**
1. Start the scraper:

```powershell
python main.py
```

2. Follow the prompt questions. Press Enter to accept the default value shown in brackets.

Typical prompts and defaults used by `main.py`:
- Lowest price: `300`
- Highest price: `500`
- Minimum bedrooms: `2`
- Sort order: `priceasc`
- Number of properties to collect: `10` (large numbers take longer)
- Run browser in headless mode: `yes`

Example session

```
$ python main.py
Enter filter values (press Enter to use default):
Lowest price [300]: 350
Highest price [500]:
Minimum bedrooms [2]:
Sort order (e.g. priceasc) [priceasc]:
How many properties to collect data on? (Warning: large numbers can take a while) [10]: 5
Run browser in headless mode? (yes/no) [yes]: y
```

**Output**
- A CSV file named `stuff.csv` is written in the repository root. Column headers come from `RentalProperty.CSV_HEADER` in `RentalProperty.py`.
- Scraping logic runs from `RentalBrowser.find_all_rentals` and is invoked by `main.py`.

**Troubleshooting**
- If the browser doesn't start, verify the correct WebDriver is installed and available on your PATH.
- If you get empty results, check filter values or try running without headless mode to watch the browser.
- Increase the property limit cautiously — scraping more pages takes more time and memory.

example.csv and example.txt are just there for example outputs.