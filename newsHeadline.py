from bs4 import BeautifulSoup
import requests
import datetime

#URL link of The Hindu website
url = "https://www.thehindu.com/news/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#title is the class name where all main heading is written
headlines = soup.find_all(class_='title')

file = open("news.txt", "w", encoding="utf-8") 

#we use datetime libaray to show the current date 
date = f"Date : {datetime.datetime.now().strftime('%Y-%m-%d')}\n"
file.write(date)
file.write("\t\tToday's News Headlines:\n\n")
file.write(f"\t\tHere are the top {len(headlines)} news headlines from The Hindu:\n")
file.write("----------------------------------------------------------\n\n")
for i, headline in enumerate(headlines, start=1):
    news = f"{i}.    {headline.get_text(strip=True)}\n" #single headline fetching by usnig loop
    file.write(news)

file.close()