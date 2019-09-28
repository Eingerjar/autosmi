import feedparser

urls=("https://rss.blog.naver.com/bluewater91.xml","https://rss.blog.naver.com/ych622.xml")


def crawl_rss(url):
    d = feedparser.parse(url)
    print("\n"+url)
    print(d.entries)
    for e in d.entries :
        print("title = ",e.title)
        print("link = ",e.link)


for url in urls:
    crawl_rss(url)
