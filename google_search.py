from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

# Country Codes from https://support.google.com/business/answer/6270107?hl=en
country_to_code = {
    'Russia': 'ru',
    'Turkey': 'tr',
}


# Takes a search term and optionally a country code and number of results (max seems to be 100)
def query_search_term(search_term, country_code='', results_count=100):
    # FireFox should load geckodriver.exe (https://github.com/mozilla/geckodriver/releases).
    # Make sure to have it in the same directory
    # There are other drivers, if necessary (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
    browser = webdriver.Firefox()

    # Use Google Search, starting with google.com
    url = "https://www.google.com"
    # Check if a country code was input, adds to end of domain
    if country_code:
        url = url + "." + country_code

    # add number of results and search term
    search_url = url + "/search?num={}&q={}".format(results_count, search_term)

    # delay is the max time in seconds before timeout.
    # loaded_page_id is the id of the element that indicates Google search has loaded, and is ready to scrape.
    browser.get(search_url)
    delay = 3  # seconds
    loaded_page_id = "rso"

    list_of_links = []

    # Catches a TimeoutException, based on the time set by delay
    try:
        # Page may take a few seconds to load
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, loaded_page_id)))
        print("Page is ready!")
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        # Each Google result is defined with class "g"
        results = soup.find_all("div", {"class": "g"})

        # iterate over each item with class containing "g" and with "href", adding item to list_of_links
        for result in results:
            link = result.find('a', href=True)
            if link:
                list_of_links.append(link)
    except TimeoutException:
        print("Loading took too much time!")
    browser.close()

    return list_of_links


# Takes input of txt file, each row being one search term
def query_all_from_txt(input_file_name, country_code='', results_number=100):
    # encoding is utf8 to account for non-ascii characters
    with open(input_file_name, encoding="utf8") as text_file:
        # each line counts as a search term
        for line in text_file:
            # retrieve list
            link_list = query_search_term(line, country_code=country_code, results_count=results_number)

            # output txt file named after search term
            output_file_name = line.strip() + ".txt"

            # Will write over same named file
            # or a create a new txt in the same directory
            with open(output_file_name, 'w') as output_file:
                # retrieve each item from link_list
                for link in link_list:
                    # Extract text of url from each item, write it to one line.
                    output_file.write(link['href'] + '\n')


# Run search of all terms in test_terms.txt
query_all_from_txt('test_terms.txt')
