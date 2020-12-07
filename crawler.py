from urllib.request import urlopen
import re

products_dict = {
    "richer": { 
        "yamaha": 0,
    },
    "audiovisual" : {
        "yamaha": 0,
    }

}

data = urlopen("https://www.richersounds.com/yamaha-network-stereo-amplifier.html")
output = data.read()
html = output.decode("utf-8")
#pattern = "<title.*?>.*?</title.*?>"
pattern= "<span class=\"price\">.*?</span>"
match_results = re.search(pattern, html, re.IGNORECASE)

title = match_results.group()
price = re.sub("<.*?>", "", title)

products_dict["richer"]["yamaha"] = price



data = urlopen("https://www.audiovisualonline.co.uk/product/27105/yamaha-wxa-50-musiccast-stereo-streaming-amplifier/")
output = data.read()
html = output.decode("utf-8")
pattern = "<span class=\"js-product-single-price\" itemprop=\"price\">.*?/span>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
price = re.sub("<.*?>", "", title)


products_dict["audiovisual"]["yamaha"] = price



print(products_dict)