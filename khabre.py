import os
import requests
import datetime
from gtts import gTTS  # Ensure gTTS is installed via pip
NEWS_API_KEY = 'API KEY'

class Speak:
    def __init__(self, news):
        self.language = 'en'
        self.news = news

    def speak(self):
        output = gTTS(text=self.news, lang=self.language)
        output.save('todays_news.mp3')
        os.system('mpv /data/data/com.termux/files/home/khabre/todays_news.mp3')
        os.system('rm -r /data/data/com.termux/files/home/khabre/todays_news.mp3')

class News:
    def __init__(self):
        if not NEWS_API_KEY:
            raise ValueError("NEWS_API_KEY is missing! Please set it.")
        self.url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWS_API_KEY}"

    def get_news(self):
        news_data = requests.get(self.url).json()
        articles = news_data.get("articles", [])
        news_titles = [article["title"] for article in articles if "title" in article]

        print("Date:", datetime.datetime.now().strftime("%d-%m-%Y"))
        print("News Report:")

        for i, title in enumerate(news_titles[:10]):  # limiting to 10 headlines for brevity
            print(f"{i + 1}. {title}")

        # Optionally, speak the news headlines
        if news_titles:
            all_titles = "\n".join([f"{i + 1}. {title}" for i, title in enumerate(news_titles[:10])])
            speaker = Speak(all_titles)
            speaker.speak()

def news_report():
    obj = News()
    obj.get_news()

if __name__ == "__main__":
    news_report()
