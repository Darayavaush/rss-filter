from subprocess import call
import requests
import bs4


html = requests.get('https://www.mangaupdates.com/mylist.html?id=450989&list=user2')
soup = bs4.BeautifulSoup(html.content).find(id='ptable')
links = [x['href'].replace('https', 'http') for x in soup('a')]

call("""python rssfilter.py\
    -f "C:/wamp/www/baka.xml"\
    -u "https://www.mangaupdates.com/rss.php"\
    -t "\
        x.link in """ + str(links) + """\
    " """)
