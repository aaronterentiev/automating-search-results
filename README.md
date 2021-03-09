# automating-search-results
Scripts for retrieving URLs from search engines

# Google Search
google_search.py uses Selenium to automate gathering of URLs from Google searches. Selenium is mainly used for automating browser interaction, such as for debugging a website. It can also be used for scraping, in this case with the help of BeautifulSoup. More information on using Selenium in Python can be found here: https://selenium-python.readthedocs.io/

This current script takes an input of the input file name, which is a text file, where each line represents one term to be queried in Google. Each term will generate a txt file, containing one URL for each search result. By default, that URL count is set at 100, though that can be decreased (and I believe increased, though I'm not sure what Google's limit).

Each search term will open a new browser window, which means this script can be resource intensive. It currently uses Firefox, and requires users to download the geckodriver.exe for use (https://github.com/mozilla/geckodriver/releases). I believe it can be adapted for other browsers compatible with Selenium (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).

This is the appearance of my directory before running the script.
![Windows directory window, showing 3 files: geckodriver.exe, google_search.py, and test_terms.txt](/images/directory_pre_running.jpg)

And the appearance of my directory after running it.
![Windows directory window, showing 5 additional files from the last image. 4 new files for each of the search terms, and 1 file for the gecko driver logs.](/images/directory_post_running.jpg)

Each generated txt file contains a list of URLs, such as this result for search term from the test_terms.txt file (Âşık Veysel was a 20th century Turkish poet and musician).
![URLs from each search result for Turkish poet Âşık Veysel.](/images/Veysel_URL_results.jpg)
