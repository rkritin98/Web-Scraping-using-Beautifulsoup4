from bs4 import BeautifulSoup
import requests
import csv
source= requests.get('https://coreyms.com/').text

soup= BeautifulSoup(source, 'lxml') #lxml- parsing tool

#.prettify() indents the html code

csv_file = open("scrape_site.csv",'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Youtube_Link'])

for article in soup.find_all('article'): #soup.find() finds the first. soup.find_all() gives a list as an output

    headline= article.h2.a.text
    
    summary = article.find('div',class_='entry-content').p.text #div is a block, class_ is the specific class of the block on which the search happens
            
    try:
        vid_src = article.find('iframe', class_= 'youtube-player')['src'] #access values in a html block like a dictionary
        print(vid_src)
        vid_id = vid_src.split('/')[4].split('?')[0]

        yt_link= f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    
    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()
    