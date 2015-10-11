from subprocess import call


call("""python rssfilter.py\
    -f "C:/wamp/www/rps.xml"\
    -u "http://feeds.feedburner.com/RockPaperShotgun"\
    -t "\
        'The Witcher 3' not in x.title \
        and 'League Of Legends' not in x.title \
        and 'Heroes Of The Storm' not in x.title \
        and 'MGSV' not in x.title \
        and 'ARK: Survival' not in x.title \
        and 'What Are We All Playing This Weekend?' != x.title \
    "
    -c \
    """)
