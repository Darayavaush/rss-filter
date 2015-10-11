import PyRSS2Gen
import feedparser
import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name')
parser.add_argument('-l', '--link')
parser.add_argument('-f', '--file', required=True)
parser.add_argument('-u', '--url', required=True)
parser.add_argument('-t', '--filter', required=True)
parser.add_argument('-c', '--content', action="store_true")
parser.add_argument('-d', '--debug', action="store_true")
args = parser.parse_args()

feed = feedparser.parse(args.url)

if args.debug:
    # import pprint
    # debug = open('temp.txt', 'w')
    # pprint.pprint(feed.entries, debug)

    # print(feed.entries[0].content)
    for x in feed.entries:
        print(x.title)
    exit()

items = [
    PyRSS2Gen.RSSItem(
        title=x.title,
        link=x.link,
        description=x.content[0]['value'] if args.content else x.summary,
    )
    for x in feed.entries if (eval(args.filter))
]

rss = PyRSS2Gen.RSS2(
    title=args.name if args.name else feed.feed.title,
    link=args.link if args.link else feed.feed.link,
    description="RSS filter made by Dariush.",
    language='en-us',
    lastBuildDate=datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT"),
    docs='http://blogs.law.harvard.edu/tech/rss',
    items=items[-100:],
)
f = open(args.file, encoding="utf-8", mode="w")
f.write(rss.to_xml("utf-8").replace('><', '>\n<'))
