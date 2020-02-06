# import requests
# import urllib.request
# import time
# from bs4 import BeautifulSoup
# from requests_html import HTMLSession



# source = "source"

# def get_oracle(url):
#     session = HTMLSession()
#     r = session.get(url)
#     time.sleep(2)
#     r.html.render(sleep=1, keep_page=True)
#     return (r.html.page.content())

# print(help(get_oracle("http://ilearning.oracle.com/ilearn/en/learner/jsp/player.jsp?rco_id=2345781686&classroom_id=2374678804&scorm_attempt=1580633557854&sessionId=-19520474731580633557870&home_url=http%3A%2F%2Filearning.oracle.com%2Filearn%2Fen%2Flearner%2Fjsp%2Foffering_details_home.jsp%3Faction%3Dexpand%26item%3D2345781676%26current_rco_id%3D2345781900%26classid%3D2374678804")))
my_url = "http://ilearning.oracle.com/ilearn/en/learner/jsp/player.jsp?rco_id=2345781686&classroom_id=2374678804&scorm_attempt=1580638598740&sessionId=-14053428951580638598783&home_url=http%3A%2F%2Filearning.oracle.com%2Filearn%2Fen%2Flearner%2Fjsp%2Foffering_details_home.jsp%3Fclassid%3D2374678804"

from requests_html import HTMLSession

false = "false"
true = "true"
null = "null"
cookies =     {
        "name": "ORA_UCM_INFO",
        "value": "3~902F51F34032CF1AE050E60AD17F45B4~Kevin~Agusto~kevinagusto28@gmail.com",
        "domain": ".oracle.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "sameSite": "no_restriction",
        "session": false,
        "firstPartyDomain": "",
        "expirationDate": "1587338935",
        "storeId": null
    }
session = HTMLSession()
r = session.get(my_url, cookies=cookies)
r.html.render(sleep=1, keep_page=True)
print((r.html.full_text))