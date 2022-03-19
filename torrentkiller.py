import sys
import os

directory = "/Users/komun/downloads/"
test = os.listdir( directory )

for item in test:
    if item.endswith(".torrent"):
        os.remove( os.path.join( directory, item ) )
