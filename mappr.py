import gmplot
import pandas as pd
from pandas.io.json import json_normalize

api_key = 'ENTER API KEY'

def json_to_df(filepath):

	json_data = pd.read_json(filepath)['locations']
	location_data = json_normalize(data=json_data.values.tolist())
	location_data.loc[:, ['latitudeE7', 'longitudeE7']] = location_data[['latitudeE7', 'longitudeE7']] / 1e7
	location_data['timestampMs'] = pd.to_datetime(location_data['timestampMs'], unit='ms')
	location_data = location_data.rename({'timestampMs': 'time'}, axis='columns')
	location_data = location_data.set_index('time')
	location_data = location_data[['latitudeE7', 'longitudeE7']]

	return location_data

def minmax(df):

	min_lat, max_lat = min(df['latitudeE7']), max(df['latitudeE7'])
	min_lon, max_lon = min(df['longitudeE7']), max(df['longitudeE7'])

	return min_lat, max_lat, min_lon, max_lon

def line(df, filename='line.html',colour='blue',edge_width=1):

	min_lat, max_lat, min_lon, max_lon = minmax(df)
	mymap = gmplot.GoogleMapPlotter((max_lat + min_lat) / 2, (max_lon + min_lon) / 2, 7,apikey=api_key)
	mymap.plot(df.latitudeE7, df.longitudeE7, colour, edge_width=edge_width)
	mymap.draw(filename)

def scatter(df, filename='scatter.html',colour='red',size=15,marker=False):

	min_lat, max_lat, min_lon, max_lon = minmax(df)
	mymap = gmplot.GoogleMapPlotter((max_lat + min_lat) / 2, (max_lon + min_lon) / 2, 7,apikey=api_key)
	mymap.scatter(tuple(df.latitudeE7), tuple(df.longitudeE7), colour, size=size, marker=marker)
	mymap.draw(filename)


def heatmap(df, filename='heatmap.html',threshold=1,radius=500):

	min_lat, max_lat, min_lon, max_lon = minmax(df)
	mymap = gmplot.GoogleMapPlotter((max_lat + min_lat) / 2, (max_lon + min_lon) / 2, 7,apikey=api_key)
	mymap.heatmap(tuple(df.latitudeE7), tuple(df.longitudeE7), threshold=threshold, radius=radius)
	mymap.draw(filename)