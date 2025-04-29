# 🗞️ Khabre - News Reader in Termux

**Khabre** is a simple Python script that fetches the latest business news headlines from the US using the [NewsAPI](https://newsapi.org/) and reads them aloud using [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/). This script is specifically designed to run inside [Termux](https://termux.dev/) on Android.

## 📦 Features

- Fetches top 10 US business news headlines from NewsAPI.
- Converts the headlines to speech using gTTS.
- Plays the generated audio using `mpv`.
- Automatically deletes the audio file after playback.


## 📲 Installation (in Termux)

```bash
pkg update && pkg upgrade
pkg install python mpv
pip install gtts requests
```

## 🔑 Setup

1. Get a free API key from [NewsAPI](https://newsapi.org/).
2. Replace `'API KEY'` in the code with your actual API key:
   ```python
   NEWS_API_KEY = 'your_actual_api_key'
   ```

## ▶️ Usage

Simply run the script:

```bash
python khabre.py
```

The script will:
- Print today's date and the top 10 US business headlines.
- Convert the headlines to speech.
- Play the audio using `mpv`.
- Delete the audio file afterward.

## 📁 File Structure

```
khabre/
├── khabre.py          # Main script
├── todays_news.mp3   # Temporary audio file (auto-deleted)
├── README.md
├── requirements.txt 
```

## 🛑 Notes

- Ensure your Termux has access to storage and audio playback capabilities.
- The script uses hardcoded Termux paths:
  ```
  /data/data/com.termux/files/home/khabre/
  ```
  Modify the path if you're running it elsewhere.

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

Made by Ro706 and 📱 for Termux users.

---

Let me know if you want me to generate a `LICENSE` file or package this into a `setup.py` or `requirements.txt` for easier distribution.
