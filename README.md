# Google Location History

Map your Google Map Location history into either line, scatter or heatmap

```python

from mappr import json_to_df, line, scatter,heatmap

df = json_to_df('LocationHistory.json')
line(df) OR scatter(df) OR heatmap(df)

```

![scatter](https://i.imgur.com/oTzaTs5.jpg)

NEW UPDATE - use index.html to create animated HTML page

![html_gif](https://i.imgur.com/7qypWXN.gif)
