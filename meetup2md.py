#!/usr/bin/python
# -*- coding: utf-8 -*-
"""meetup2md.py"""

import json
import requests
import sys
import re
import time

theAPIKey = ""

def main():

    # Building the request
    if len(sys.argv) == 2:
        args = sys.argv
        theEventURL = args[1]
        pattern = r'h?t?t?p?s?:?/*www.meetup.com/es-ES/([A-Za-z-]*)/events/(\d+)/'
        matchURL = re.match(pattern, theEventURL)
        if matchURL:
            theGroup = matchURL.group(1)
            theEvent = matchURL.group(2)
        else:
            print ("Asegúrate de que la URL está bien escrita")
            sys.exit()
    else:
        print ("Usa el método así: python meetup2md.py urldelevento")
        sys.exit()

    theURL = "https://api.meetup.com/"+theGroup+"/events/"+theEvent+"?&sign=true&photo-host=public&key="+theAPIKey

    # Obtaining the response in JSON
    theJSON = obtain_json(theURL)

    # Preparing the output file, a markdown post
    location = "_posts/"
    date = time.strftime("%Y-%m-%d")
    postName = re.sub(r"\s+", '-', theJSON['name'])
    postFilename = location+date+"-"+postName+".markdown"

    # Writing the post
    post = open(postFilename, 'w')
    # Head
    post.write("---\nlayout: post\ntitle: \""+theJSON['name']+"\"\nsubtitle:\"Evento\"\ndate: "+time.strftime("%Y-%m-%d %H:%M:%S")+"::00 +0530"+"\ncategories: [\"eventos\"]\nauthor: \"Geek & Tech Girls\"\navatar: img/authors/geekandtechgirls.png\nimage: img/eventos.jpg\n---")
    # Post title
    post.write("\n\n## Evento: "+theJSON['name']+"\n\n")
    # Description
    post.write(theJSON['description'])
    # Link
    post.write("\n\nPuedes apuntarte [aquí]("+theEventURL+")")

    post.close()

def obtain_json(eventURL):
    request = requests.get(eventURL)
    data = request.json()

    return data

if __name__=="__main__":
        main()
