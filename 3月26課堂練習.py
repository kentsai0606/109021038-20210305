import requests


def get_webpage(url):
    html_page=requests.get(url)

    if html_page.status_code !=200:
        print("invalid url",html_page.status_code)
        return None
    else:
        return html_page.text


site="http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm"
html=get_webpage(site)
print(html)
