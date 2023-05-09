import pandas as pd
from pykml.factory import KML_ElementMaker as KML
from lxml import etree
import simplekml
from bng_latlon import OSGB36toWGS84

filepath = '/home/tuf-learning/Documents/Code/ARWAC_row_generation/data/laughton_row_23.csv'

df = pd.read_csv(filepath)

# print(df)

points_list = []

for index, row in df.iterrows():
    lat_long = OSGB36toWGS84(row['X'], row['Y'])
    points_list.append((lat_long[1],lat_long[0], 0))

kml = simplekml.Kml()

folder1 = kml.newfolder(name='Boundaries')
folder2 = kml.newfolder(name='AB_Lines')
folder3 = kml.newfolder(name='Curve_Lines')


ls = folder3.newlinestring(tessellate=1)

ls.style.linestyle.color = "ff6699ff"
ls.style.linestyle.width = 2

ls.coords = points_list



kml.save("laughton.kml")
