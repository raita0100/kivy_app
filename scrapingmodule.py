import requests
from bs4 import BeautifulSoup as BS
from time import sleep

def scrape_data(query):
    query = query.replace(" ", "+")

    url = f"https://en.wikipedia.org/wiki/Special:Search?search={query}&go=Go"
    ret_text = []

    try:

        resp = requests.get(url)
        sleep(4)

        soup = BS(resp.text, 'html.parser')
        x = soup.find("div", {"id": "bodyContent"}).find("div", {"id": "mw-content-text"}).find("ul", {
        "class": "mw-search-results"}).find("li").find("a", href=True)

        domain = "https://en.wikipedia.org"
        data_url = domain + x['href']

        resp = requests.get(data_url)

        soup2 = BS(resp.text, 'html.parser')

        res = soup2.find("div", {"id": "mw-content-text"}).find("div", {"class", "mw-parser-output"}).find_all("p")
        sleep(4)

        #ret_text = []
        for i in range(len(res)):
            data = res[i].text
            if len(data) > 10:
                ret_text.append(data)
    except Exception as e:
        print(e)
        ret_text.append("OOps! sorry I din't catch that.")

    return ret_text
