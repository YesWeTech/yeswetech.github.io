#!/usr/bin/python
# -*- coding: utf-8 -*-
"""meetup2md.py"""

import json
import sys
import re

theAPIKey = ""
theEvent = "234640453"

if len(sys.argv) == 2:
    args = sys.argv
    theEventURL = args[1]
    pattern = r'https?://www.meetup.com/es-ES/Granada-Geek/events/(\d+)/'
    matchURL = re.match(pattern, theEventURL)
    if matchURL:
        print "El evento es: ", matchURL.group(1)
else:
    print "Usa el método así: python meetup2md.py urldelevento"
    sys.exit()

theURL = "https://api.meetup.com/Granada-Geek/events/"+theEvent+"?&sign=true&photo-host=public&key="+theAPIKey
