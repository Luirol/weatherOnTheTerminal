from urllib import response
import requests

list_params = {'TqnM':'', 'lang':'ru'}
areas = ['svo', 'London', 'Череповец']
for area in areas:
    url = 'HTTP://wttr.in/{}'
    url = url.format(area) # svo London Череповец
    response = requests.get(url, params = list_params)
    response.raise_for_status()
    print(response.text)