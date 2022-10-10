from urllib import response
import requests

getParams = {'TqnM':'', 'lang':'ru'}
areas = ['svo', 'London', 'Череповец']
for area in areas:
    url = 'HTTP://wttr.in/{}'
    url = url.format(area)
    response = requests.get(url, params = getParams)
    response.raise_for_status()
    print(response.text)