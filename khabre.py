import os
import requests
import datetime
from dotenv import load_dotenv
from gtts import gTTS

# Load environment variables
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

class Speak:
    def __init__(self, news):
        self.language = 'en'
        self.news = news

    def speak(self):
        output = gTTS(text=self.news, lang=self.language)
        file_path = 'todays_news.mp3'
        output.save(file_path)
        os.system(f'mpv "{file_path}"')  # Play with mpv
        os.remove(file_path)

class News:
    def __init__(self):
        if not NEWS_API_KEY:
            raise ValueError("NEWS_API_KEY is missing! Please set it in your .env file.")
        self.url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWS_API_KEY}"

    def get_news(self):
        try:
            response = requests.get(self.url)
            print("Status Code:", response.status_code)
            print("Raw Response:", response.text[:500])  # Limit output for readability
            response.raise_for_status()
            news_data = response.json()
            articles = news_data.get("articles", [])
            news_titles = [article["title"] for article in articles if "title" in article]

            print("\nDate:", datetime.datetime.now().strftime("%d-%m-%Y"))
            print("News Report:")
            for i, title in enumerate(news_titles[:10]):
                print(f"{i + 1}. {title}")

            if news_titles:
                all_titles = ". ".join([f"{i + 1}. {title}" for i, title in enumerate(news_titles[:10])])
                speaker = Speak(all_titles)
                speaker.speak()
            else:
                print("No news headlines found.")

        except requests.RequestException as e:
            print("Error fetching news:", e)

def news_report():
    news = News()
    news.get_news()

if __name__ == "__main__":
    news_report()
                         
