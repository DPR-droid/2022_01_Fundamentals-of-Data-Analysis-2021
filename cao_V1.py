########################################################################
# GMIT Project for Fundamentals for Data Analysis
# Programming-for-Data-Analysis-Project-2021
# Due: last commit on or before 03/01/2021
# Fundamentals-for-Data-Analysis-Project-2021.py
# Author David
# The project submitted is in a Jupyter notebook
# This python script is a reference and testing 
########################################################################
# Global settings
# Importing all the modules required for the juypter Notbook
# All imports are listed in the requirments.txt
########################################################################

# Regular expressions 
import re
# Convenient HTTP requests
import requests as rq
# Dates and times
import datetime as dt
# Import numpy module
import numpy as np
# For downloading.
import urllib.request as urlrq
# Import tabula to read table in pdf
import tabula as tb
# Import mathplotlib
import matplotlib.pyplot as plt
# Import time
import time
# import seaborn
import seaborn as sns
# import warnings
import warnings
warnings.filterwarnings("ignore")


########################################################################
# Error Checks
########################################################################

########################################################################
# Function to test URLs
# https://pytutorial.com/check-url-is-reachable
########################################################################

def url_checker(url):
	try:
		#Get Url
		get = rq.get(url)
		# if the request succeeds 
		if get.status_code == 200:
			return(print(f"{url}: is reachable"))
		else:
			return(print(f"{url}: is Not reachable, status_code: {get.status_code}"))

	#Exception
	except rq.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(print(f"{url}: is Not reachable \nErr: {e}"))



########################################################################
# Function to save orginal files
########################################################################

# Get the current date and time
now = dt.datetime.now()

# format as a string
nowstr = now.strftime('%Y%m%d_%H%M%S')

print(nowstr)
# Create a file path for the original data.
path = 'data/' + + nowstr + '.html'

# Save the original html file.
with open(path, 'w') as f:
    f.write(resp.text)






########################################################################
# URL for CAO points
# http://www2.cao.ie/points/lvl8_18.pdf
# http://www2.cao.ie/points/lvl76_18.pdf
# http://www2.cao.ie/points/lvl8_19.pdf
# http://www2.cao.ie/points/lvl76_19.pdf
# http://www2.cao.ie/points/CAOPointsCharts2020.xlsx
# http://www2.cao.ie/points/CAOPointsCharts2021.xlsx
########################################################################
CAO2021 = 'http://www2.cao.ie/points/CAOPointsCharts2021.xlsx'
CAO2020 = 'http://www2.cao.ie/points/CAOPointsCharts2020.xlsx'
CAO2019_8 = 'http://www2.cao.ie/points/lvl8_19.pdf'
CAO2019_76 = 'http://www2.cao.ie/points/lvl76_19.pdf'
CAO2018_8 = 'http://www2.cao.ie/points/lvl8_18.pdf'
CAO2018_76 = 'http://www2.cao.ie/points/lvl76_18.pdf'

########################################################################
# List of URL 
# Use function to test if available
# https://pytutorial.com/check-url-is-reachable
########################################################################
caopointslist = [CAO2021,CAO2020,CAO2019_8, CAO2019_76,CAO2018_8, CAO2018_76]

for url in caopointslist:
    url_checker(url)





# Check text
# resp.text







########################################################################
# 
########################################################################