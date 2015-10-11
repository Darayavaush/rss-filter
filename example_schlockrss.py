from subprocess import call


call("""python rssfilter.py\
    -f "C:/wamp/www/schlock.xml"\
    -u "http://feeds.feedburner.com/SchlockRSS"\
    -t "'feed-first.png' in x.summary"\
""")
