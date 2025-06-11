# Personal News Digest

This is my personal, Python-based news digest script. It fetches the top 5 headlines from each news source and generates a standalone `news.html` page.

## Features

- Fetches headlines from BBC World, Reuters Top News, and The Guardian via RSS.
- Renders a clean HTML file with titles, links, and summaries.
- Easy to customise sources and styling.
- No external credits or API keys required.

## Getting Started

1. Clone this repo:
   ```bash
   git clone https://github.com/<YourUser>/news-digest.git
   cd news-digest
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python news_digest.py
   ```
5. Open `news.html` in your browser to see the latest digest.

## Customisation

- Modify `RSS_FEEDS` in `news_digest.py` to add or remove sources.
- Edit `template.html` to change the layout or styling.

---

*Built by me to keep up with the headlines every morning.*
