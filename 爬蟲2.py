import requests

URL="https://www.majortests.com/word-lists/"

def generate_urls(url,start_page,end_page):
    url=[]
    for page in range(start_page,end_page):
        urls.append(url.format(page))
        return urls
def get_resource(url):
    headers={
        "user-agent":"Mozill/5.0(Windows NT 10.0; Win64; x64) ApplWebKit/537.36 (KHTML,like Gecko) Chorme/63.0.3239.132 Safari/537.36"}
    return request.get(url,headers=headers)


if __name__=="__main__":
    urlx=generate_urls(url,1,10)
    for url in urlx:
        file=url.split("/")[-1]
        print("catching:",file,"web data...")
        r= get_resource(url)
        if r.status_code==requests.code.ok:
            print(r.text)
            print("------------\n\n")
        else:
            print("HTTP request error")

