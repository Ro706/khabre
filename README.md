# 🗞️ Khabre - News Reader for Termux

**Khabre** is a simple Python script that fetches the latest US business news headlines using the [NewsAPI](https://newsapi.org/) and reads them aloud using [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/). Built for use in [Termux](https://termux.dev/) on Android, it's a hands-free way to stay updated on business news.

---

## 📦 Features

- ✅ Fetches top 10 business headlines from the US using NewsAPI.
- 🗣️ Converts news headlines to speech using gTTS.
- 🔊 Plays audio via `mpv`.
- 🧹 Automatically deletes the temporary audio file after playback.
- 🔐 Loads the NewsAPI key securely using a `.env` file.
- ⚠️ Handles API errors and missing keys gracefully.

---

## 📲 Installation (in Termux)

```bash
pkg update && pkg upgrade
pkg install python mpv
pip install gtts requests python-dotenv
```

---

## 🔑 Setup

1. Create a free API key at [NewsAPI](https://newsapi.org/).
2. In the root folder of your project, create a `.env` file:
   ```
   NEWS_API_KEY=your_actual_api_key
   ```

---

## ▶️ Usage

Run the script with:

```bash
python khabre.py
```

It will:

- Print today’s date and the top 10 business headlines.
- Convert the headlines to an audio summary.
- Play the audio using `mpv`.
- Delete the generated audio file after playback.

---

## 📁 File Structure

```
khabre/
├── khabre.py          # Main script
├── .env               # Your API key (not committed to Git)
├── todays_news.mp3    # Temporary audio file (auto-deleted)
├── README.md
├── requirements.txt
```

---

## 📄 requirements.txt

```
gtts
requests
python-dotenv
```

---

## 🛑 Notes

- Ensure Termux has permission to access storage and audio.
- If you're not using the default Termux environment, adjust paths if necessary.
- Do **not** commit your `.env` file if uploading to GitHub or sharing the repo.

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for full details.

---

Made by Ro706 — for the Termux power users 📱

---

Let me know if you want a `.gitignore`, `LICENSE`, or `setup.py` file added.
