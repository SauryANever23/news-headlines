import re
import requests
from bs4 import BeautifulSoup

url2 = 'https://www.nytimes.com/international/' # For New York Times

res2 = requests.get(url2)

soup2 = BeautifulSoup(res2.text, 'html.parser')

def get_headlines(q):
    try:
        a = 0
        for item in q.select(".css-xdandi"):
            if len(item.text) > 20:
                a += 1
                print("\n")
                print(item.text)
                if a >= 20:
                    break

    except Exception as e:

        print(e)
    finally:
        return a

num = 20

def get_link(w):
    
    n = int(input("want to print or want in file?:(1/2) "))
    
    if n == 2:
        for link in w.find_all("a", href=True):
            with open('links.txt', 'w') as f:
                f.write(link['href'])
    elif n == 1:
        for link in w.find_all('a', href=True):
            print(link['href'])
    else:
        print('Invalid input')

# get_headlines(soup1, soup2)

def wrd_len(x) -> int:
    """
    This function gives the number of words in a sentence
    """
    if len(x) == 0:
        a = 0
    else:
        a = 1 

    for i in x:
        if i == " ":
            a += 1 

    return a

def adv_cmp(l: list, y: str) -> bool:
    """
    This function returns True even if a single element of list l matches with y
    this function requires regex, 

    pre-requisites:
    import re
    """

    for i in l:
        match = re.search(i, y)
        if match:
            val = True
        else:
            val = False
    return val
        

def get_details(a) -> dict:
    """
    This Function gets the URL's and the summary text from each article
    returns a dict
    """

    details = {
        'urls': [],
        'summary': []
    }
    
    for l in a.find_all("a", class_="css-9mylee", href=True):
        details['urls'].append(l['href'])

    pattern = r"summary"
    
    paragraphs = a.find_all("p")
    
    for para in paragraphs:
        b = str(para.get('class'))
        match = re.search(pattern, b)

        if match:
            details['summary'].append(para.text)
    test = []
    t1 = 0
    for i in details['summary']:
        if wrd_len(i) > 12:
            t1 += 1
            test.append(i)
            if t1 >= num:
                break
        
    details['summary'] = test
    
    k_wrd = [r"crosswords", r"spelling-bee", r"connections", r"strands", r"wordle"]
    new_test = []
    t2 = 0
    for j in details['urls']:
        if "game" in j:   
            pass
        elif "puzzles" in j:
            pass
        elif "crosswords" in j:
            pass
        else:
            t2 += 1
            new_test.append(j)
            if t2 >= num:
                break
    

    details['urls'] = new_test

    return details

def organized_form():
    
    detail = get_details(soup2)
    url = detail['urls']
    summary = detail['summary']

    try:
        b = 0
        i = 0
        for item in soup2.select(".css-xdandi"):
            if len(item.text) > 20:
                b += 1
                print("\n")
                print(f"{item.text}\n\n{summary[i]}\n{url[i]}")
                i += 1
                if b >= num:
                    break

    except Exception as e:
        pass
  

def main():
    organized_form()


if __name__ == '__main__':
    main()


    
    

    
