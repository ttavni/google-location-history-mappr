from mappr import json_to_df, line, scatter,heatmap

if __name__ == "__main__":

	df = json_to_df('LocationHistory.json')
	line(df)
	scatter(df)
	heatmap(df)