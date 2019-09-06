from urllib.request import urlopen

data = urlopen("https://data.nasa.gov/api/views/gquh-watm/rows.csv?accessType=DOWNLOAD").read().decode()

print({"nasa_patents.csv":data})
