import sys
import os

directory = "Directory URL"
test = os.listdir( directory )

for item in test:
    if item.endswith("Extension i.e (.jpg,.png)"):
        os.remove( os.path.join( directory, item ) )
