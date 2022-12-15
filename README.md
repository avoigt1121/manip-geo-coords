# manip-geo-coords
Rob's assignment on practicing pandas manipulation and geocoordinates

This doesnt actually work yet lol
REQUIRED IMPORTS/INSTALLS:

from cmath import inf
import pandas as pd
import re
from datetime import datetime
from dateutil.parser import parse
import math
import sympy


The idea is to scrape a file for geocoordinates. The scraper can take DD, DDM, or DMS formats. 

Secondly, the code converts all formats to DD so they can be compared to each other.

Thirdly, the code runs calculations for time and distance based of off id type and timestamps

Fourth, the code will make a guess on what type of craft each id is

