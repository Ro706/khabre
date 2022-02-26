import os
import requests
from gtts import gTTS
from pyfiglet import Figlet
f = Figlet(font='slant')
print (f.renderText('KHABRE'))
def speack(a):
    language ='en'
    output=gTTS(text=a,lang=language)
    output.save('todays_news.mp3')
    os.system('mpv /data/data/com.termux/files/home/code/todays_news.mp3')
    os.system('rm -r /data/data/com.termux/files/home/code/todays_news.mp3')
api_key='a8c42b827a044f0b90d1d1fb314ef182'
def news():
    main_url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key
    news=requests.get(main_url).json()
    article=news["articles"]
    news_article=[]
    for arti in article:
        news_article.append(arti["title"])
    for i in range(len(news_article)):
        a=i+1,news_article[i]
        print (i+1,news_article[i])
        speack(news_article[i])
news()

