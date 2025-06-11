import feedparser
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# 1. Define your RSS feeds
RSS_FEEDS = {
    'BBC World':    'http://feeds.bbci.co.uk/news/world/rss.xml',
    'Reuters Top':  'http://feeds.reuters.com/reuters/topNews',
    'The Guardian': 'https://www.theguardian.com/world/rss',
}

# 2. Fetch and parse
def fetch_feeds():
    feed_data = {}
    for name, url in RSS_FEEDS.items():
        parsed = feedparser.parse(url)
        articles = []
        for entry in parsed.entries[:5]:
            articles.append({
                'title':   entry.title,
                'link':    entry.link,
                'summary': getattr(entry, 'summary', '')  # raw summary if present
            })
        feed_data[name] = articles
    return feed_data

# 3. Render with Jinja2
def render_html(feed_data):
    env = Environment(loader=FileSystemLoader('.'))
    tpl = env.get_template('template.html')
    html = tpl.render(
        date=datetime.now().strftime('%Y-%m-%d'),
        feed_data=feed_data
    )
    with open('news.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    data = fetch_feeds()
    render_html(data)
    print('✅ news.html generated.')
