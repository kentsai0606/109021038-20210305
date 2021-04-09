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
            
