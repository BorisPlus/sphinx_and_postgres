# coding: utf-8
# This is api.py
from pprint import pprint
import sphinxsearch

client = sphinxsearch.SphinxClient()
client.SetServer('localhost', 9312)
result = client.Query(r'голова лучшая')

pprint(result)
