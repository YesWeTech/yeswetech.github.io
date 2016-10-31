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
    pattern = r'h?t?t?p?s?:?/*www.meetup.com/es-ES/([A-Za-z-]*)/events/(\d+)/'
    matchURL = re.match(pattern, theEventURL)
    if matchURL:
        theGroup = matchURL.group(1)
        theEvent = matchURL.group(2)
else:
    print "Usa el método así: python meetup2md.py urldelevento"
    sys.exit()

theURL = "https://api.meetup.com/"+theGroup+"/events/"+theEvent+"?&sign=true&photo-host=public&key="+theAPIKey
