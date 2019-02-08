# Google Location History

Map your Google Map Location history into either line, scatter or heatmap

```python

from mappr import json_to_df, line, scatter,heatmap

df = json_to_df('LocationHistory.json')
line(df) OR scatter(df) OR heatmap(df)

```

![scatter](https://i.imgur.com/oTzaTs5.jpg)

![line](https://i.imgur.com/fcFZrbd.jpg)