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
import urllib.parse as urlpar
# Import tabula to read table in pdf
import tabula as tb
# Import mathplotlib
import matplotlib.pyplot as plt
# Import time
import time
# import pandas
import pandas as pd 
# import seaborn
import seaborn as sns
# import warnings
import warnings
warnings.filterwarnings("ignore")

########################################################################
# Set Datetime
########################################################################
# Get the current date and time
now = dt.datetime.now()

# format as a string
nowstr = now.strftime('%Y%m%d_%H%M%S')

print(nowstr)

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
		resp = rq.get(url)
		# if the request succeeds
		if resp.status_code == 404:
			print(f"{url}: is not reachable")
		else:
			print(f"{url}: is reachable")
			

	#Exception
	except rq.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(print(f"{url}: is Not reachable \nErr: {e}"))


########################################################################
# Web and files saves functions
########################################################################
########################################################################
# Function to save CAO Webpages 
########################################################################

def htmlcopy(url):
    # Fetch the CAO points URL
    resp = rq.get(url)
    # Check connection '<Response [200]>' means OK
    if resp.status_code == 200:
        print(f"{url}: is reachable")

        path = 'data/' + nowstr + '_CAO_Webpage_' + url[-4:] + '.html'
        print(str(path))

        # Save the original html file.
        with open(path, 'w') as f:
            f.write(resp.text)
    else:
        print(f"{url}: is not reachable")


########################################################################
# Function to save files
########################################################################

def caosavefile(url):
    split = urlpar.urlsplit(url)
    path = 'data/' + nowstr + '_CAO_file_' + split.path.split("/")[-1]
    print(str(path))
    urlrq.urlretrieve(url, path)


########################################################################
# Web and files links
########################################################################
########################################################################
# CAO web pages
# https://www.cao.ie/index.php?page=points&p=2018
# https://www.cao.ie/index.php?page=points&p=2019
# https://www.cao.ie/index.php?page=points&p=2020
# https://www.cao.ie/index.php?page=points&p=2021
########################################################################

html2018 = 'https://www.cao.ie/index.php?page=points&p=2018'
html2019 = 'https://www.cao.ie/index.php?page=points&p=2019'
html2020 = 'https://www.cao.ie/index.php?page=points&p=2020'
html2021 = 'https://www.cao.ie/index.php?page=points&p=2021'

caopointshtml = [html2018,html2019,html2020,html2021]

for url in caopointshtml:
    htmlcopy(url)



########################################################################
# CAO points files
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
########################################################################
caopointslist = [CAO2021,CAO2020,CAO2019_8, CAO2019_76,CAO2018_8, CAO2018_76]

for url in caopointslist:
    url_checker(url)
    caosavefile(url)

########################################################################
# Parse 2021 Data
# CAO2021 = 'http://www2.cao.ie/points/CAOPointsCharts2021.xlsx' - 1451 rows × 15 columns
########################################################################

# Download and parse the excel spreadsheet.
# 1451 rows × 15 columns
# Skip first 10 Rows
# # https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
df = pd.read_excel(CAO2021, skiprows=11)

DF2021 = df[['Course Code','Course Title','R1 Points','R2 Points ','EOS Points','EOS Midpoints', 'CATEGORY (ISCED Description)', 'HEI']] 

DF2021 = DF2021.rename(columns={'Course Code': 'Code', 'Course Title': 'Title', 'R1 Points': 'R1 Points', 'R2 Points ': 'R2 Points', 'EOS Points': 'EOS',
        'EOS Midpoints': 'Mid', 'CATEGORY (ISCED Description)': 'Category', 'HEI': 'College'})

DF2021

########################################################################
# Parse 2020 Data
# CAO2020 = 'http://www2.cao.ie/points/CAOPointsCharts2020.xlsx' - 1464 rows × 23 columns
########################################################################

# Download and parse the excel spreadsheet.
# 1464 rows × 23 columns
# Skip first 10 Rows
df = pd.read_excel(CAO2020, skiprows=10)

DF2020 = df[['COURSE CODE2','COURSE TITLE','R1 POINTS','R2 POINTS','EOS','EOS Mid-point','CATEGORY (i.e.ISCED description)', 'HEI']] 

DF2020 = DF2020.rename(columns={'COURSE CODE2': 'Code', 'COURSE TITLE': 'Title', 'R1 POINTS': 'R1 Points', 'R2 POINTS': 'R2 Points', 'EOS Mid-point': 'Mid',
            'CATEGORY (i.e.ISCED description)': 'Category', 'HEI': 'College'})

DF2020




########################################################################
# Parse 2019 Data
# CAO2019_8 = 'http://www2.cao.ie/points/lvl8_19.pdf' - 930 rows × 4 columns
# CAO2019_76 = 'http://www2.cao.ie/points/lvl76_19.pdf' - 461 rows × 4 columns
########################################################################

# Read csv as a pandas dataframe
df2019lvl8 = pd.read_csv('lvl8_19.csv', sep=',')

df2019lvl8

# Read csv as a pandas dataframe
df2019lvl76 = pd.read_csv('lvl76_19.csv', sep=',')

df2019lvl76




########################################################################
# Parse 2018 Data
# CAO2018_8 = 'http://www2.cao.ie/points/lvl8_18.pdf' - 914 rows × 4 columns
# CAO2018_76 = 'http://www2.cao.ie/points/lvl76_18.pdf' - 471 rows × 4 columns
########################################################################

# Read csv as a pandas dataframe
df2018lvl8 = pd.read_csv('lvl8_18.csv', sep=',')

df2018lvl8

# Read csv as a pandas dataframe
df2018lvl76 = pd.read_csv('lvl76_18.csv', sep=',')

df2018lvl76




########################################################################
# Pandas Join Data
########################################################################

lvl76_18 = df2018lvl76[['Code', 'Title' ]]
lvl8_18  = df2018lvl8[['Code', 'Title']]
lvl76_19  = df2019lvl76[['Code', 'Title']]
lvl8_19 = df2019lvl8[['Code', 'Title']]
lvl_20 = DF2020[['Code', 'Title' ]]
lvl_21 = DF2021[['Code' , 'Title']]


########################################################################
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# Estimate = 1874 indiviual courses codes
########################################################################

frames = [lvl76_18, lvl8_18, lvl76_19, lvl8_19, lvl_20, lvl_21 ]
Codes = pd.concat(frames)
Codes

AllCourses = Codes.drop_duplicates('Code').reset_index(drop=True)
AllCourses

########################################################################
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html
# Remove Duplicates
########################################################################

AllCourses = Codes.drop_duplicates('Code').reset_index(drop=True)

# Set indexes of Code for df
AllCourses.set_index('Code', inplace=True)

DF2021.set_index('Code', inplace=True)

AllCourses

AllCourses = AllCourses.join(DF2021[['R1 Points', 'R2 Points', 'EOS', 'Mid']])

AllCourses
