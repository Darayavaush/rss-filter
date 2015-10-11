from subprocess import call


call("""python rssfilter.py\
    -f "C:/wamp/www/jig.xml"\
    -u "http://jayisgames.com/index.xml"\
    -t "\
        'tag/interactiveart' not in x.summary\
         and 'tag/pointandclick' not in x.summary\
         and 'tag/weekday-escape' not in x.summary\
         and 'tag/launch' not in x.summary\
         and 'tag/narrative' not in x.summary\
         and 'Platform: iOS &#8212; ' not in x.summary\
    "\
""")
