# -*- coding: utf-8 -*-
# #!/usr/bin/env python3

import os
import sys
from datetime import date

from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt

def main(areapath, outfolder, start_date, end_date):
    # connect to the API
    api = SentinelAPI('javy', 'Javy9289', 'https://scihub.copernicus.eu/dhus')

    # search by polygon, time, and Hub query keywords
    # footprint = geojson_to_wkt(read_geojson('map.geojson'))
    # products = api.query(footprint,
    #                      date = ('20151219', date(2015, 12, 29)),
    #                      platformname = 'Sentinel-2',
                         # cloudcoverpercentage = (0, 30))

    footprint = geojson_to_wkt(read_geojson(areapath))
    products = api.query(footprint,
                         date = (start_date, end_date),
                         platformname = 'Sentinel-2')

    # download all results from the search
    api.download_all(products, outfolder, , checksum=False)

    # GeoJSON FeatureCollection containing footprints and metadata of the scenes
    # api.to_geojson(products)

    # GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
    # api.to_geodataframe(products)

    # Get basic information about the product: its title, file size, MD5 sum, date, footprint and
    # its download url
    # api.get_product_odata(<product_id>)

    # Get the product's full metadata available on the server
    # api.get_product_odata(<product_id>, full=True)

if __name__ == '__main__':
    areapath = './china.geojson'
    outfolder = '/data/sentinel_data/sendata/data'
    start_date = '20180101'
    end_date = '20180131'
    main(areapath, outfolder, start_date, end_date)
