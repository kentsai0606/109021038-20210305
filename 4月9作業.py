URL="https://www.majortests.com/word-lists/"
import requests
import time
from bs4 import BeautifulSoup

def generate_urls(url,start_page,end_page):
    url=[]
    for page in range(start_page,end_page):
        urls.append(url.format(page))
        return urls
def get_resource(url):
    headers={
        "user-agent":"Mozill/5.0(Windows NT 10.0; Win64; x64) ApplWebKit/537.36 (KHTML,like Gecko) Chorme/63.0.3239.132 Safari/537.36"}
    return request.get(url,headers=headers)
def parse_html(html_str):
    return BeautifulSoup(html_str,"lxml")

if __name__=="__main__":
    urlx=generate_urls(URL,1,3)
    for url in urlx:
        file=url.split("/")[-1]
        print("catching",file,"web data...")
        r=get_resource(url)
        if r.status_code==requests.code.ok:
            soup=parse_html(r.text)
            word=[]
            count=0
            for wordlist_table in soup.find_all(class_="wordlist"):
                count+=1
                for word_entry in wordlist_table.find_all("tr"):
                    new_word=[]
                    new_word.append(file)
                    new_word.append(str(count))
                    new_word.append(word_entry.th.text)
                    new_word.append(word_entry.td.text)
                    words.append(new_word)
            print(words)
            print("------------\n\n")
        else:
            print("HTTP request error")
        print("sleep 5 seconds")
        time.sleep(5)


