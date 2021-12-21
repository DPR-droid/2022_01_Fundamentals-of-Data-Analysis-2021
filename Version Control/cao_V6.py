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
# DF2019 = 1391 rows × 4 columns
########################################################################
# Read csvs into 2019 pandas dataframe
# https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# https://www.kite.com/python/answers/how-to-make-a-single-pandas-dataframe-from-multiple-%60.csv%60-files-in-python
########################################################################

csvfiles = ['lvl8_19.csv', 'lvl76_19.csv']

dflist = []

colname = ['Code', 'Title', '19_EOS', '19_Mid']

for filename in csvfiles:
    dflist.append(pd.read_csv(filename, sep=',' , skiprows = 1,header = None, names = colname ))
    
DF2019 = pd.concat(dflist)

DF2019

########################################################################
# Parse 2018 Data
# CAO2018_8 = 'http://www2.cao.ie/points/lvl8_18.pdf' - 914 rows × 4 columns
# CAO2018_76 = 'http://www2.cao.ie/points/lvl76_18.pdf' - 471 rows × 4 columns
# DF2018 = 1385 rows × 4 columns
########################################################################
# Read csvs into 2018 pandas dataframe
########################################################################

csvfiles = ['lvl8_18.csv', 'lvl76_18.csv']

dflist = []

colname = ['Code', 'Title', '18_EOS', '18_Mid']

for filename in csvfiles:
    dflist.append(pd.read_csv(filename, sep=',' , skiprows = 1,header = None, names = colname ))
    
DF2018 = pd.concat(dflist)

DF2018

########################################################################
# Pandas Join Data
########################################################################
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# Estimate = 1874 indiviual courses codes
# Merge all Dataframes
# Drop all dupicates on Code only
########################################################################

lvl_21 = DF2021[['Code', 'Title']]
lvl_20 = DF2020[['Code', 'Title']]
lvl_19 = DF2019[['Code', 'Title']]
lvl_18 = DF2018[['Code' , 'Title']]

frames = [lvl_21, lvl_20, lvl_19, lvl_18]

Codes = pd.concat(frames)

AllCourses = Codes.drop_duplicates('Code').reset_index(drop=True)


########################################################################
# Add College Code
########################################################################
# Add College Code
# https://www.datasciencemadesimple.com/return-first-n-character-from-left-of-column-in-pandas-python/
AllCourses['College Code'] = AllCourses['Code'].str[:2]

AllCourses

########################################################################
# Check to see if any missing College code
# https://datatofish.com/rows-with-nan-pandas-dataframe/
########################################################################
AllCourses[AllCourses['College Code'].isna()]


########################################################################
# Set indexes of Code for df in AllCourses
########################################################################
AllCourses.set_index('Code', inplace=True)
########################################################################
# Add Columns to Dataframe
########################################################################
DF2021.set_index('Code', inplace=True)

AllCourses = AllCourses.join(DF2021[['Category', '21_R1 Points', '21_R2 Points','21_EOS', '21_Mid']])

DF2020.set_index('Code', inplace=True)

AllCourses = AllCourses.join(DF2020[['20_R1 Points', '20_R2 Points','20_EOS', '20_Mid']])

DF2019.set_index('Code', inplace=True)

AllCourses = AllCourses.join(DF2019[['19_Mid']])

DF2018.set_index('Code', inplace=True)

AllCourses = AllCourses.join(DF2018[['18_Mid']])

AllCourses

########################################################################
# Replace Cells with data
########################################################################
# Replace all AQA with 100
# Replace all # with NAN
# Replace all +matric with NAN
# Replace all blank/empty cells with NAN
# https://stackoverflow.com/questions/38277928/remove-special-characters-in-pandas-dataframe
########################################################################

AllCourses=AllCourses.replace('AQA','100',regex=True)
AllCourses=AllCourses.replace('\#','',regex=True)
AllCourses=AllCourses.replace('\+matric',np.nan,regex=True)
AllCourses=AllCourses.replace('',np.nan)

AllCourses

########################################################################
# Set all data to_numeric
########################################################################
# https://devenum.com/pandas-convert-multiple-columns-to-float/
########################################################################

AllCourses[['21_R1 Points', '21_R2 Points','21_EOS', '21_Mid','20_R1 Points', '20_R2 Points','20_EOS', '20_Mid', '19_Mid', '18_Mid']]= AllCourses[['21_R1 Points', 
        '21_R2 Points','21_EOS', '21_Mid','20_R1 Points', '20_R2 Points','20_EOS', '20_Mid', '19_Mid', '18_Mid']].apply(pd.to_numeric)



########################################################################
# Review Data
########################################################################
# https://cmdlinetips.com/2019/03/how-to-select-top-n-rows-with-the-largest-values-in-a-columns-in-pandas/
########################################################################
# Select to top colleges by courses 
TOP5Colleges = AllCourses.groupby('College Code').head(5)
sns.boxplot(x='College Code', y='21_R1 Points', data=TOP5Colleges)

# Top 10 points by College Code for 2021
TOPpoints21 = AllCourses.nlargest(10,['21_R1 Points'])
sns.boxplot(x='College Code', y='21_R1 Points', data=TOPpoints21)

# Top 10 points by College Code for 2020
TOPpoints20 = AllCourses.nlargest(10,['20_R1 Points'])
sns.boxplot(x='College Code', y='20_R1 Points', data=TOPpoints20)

# Bottom 10 points by College Code for 2021
BOTpoints21 = AllCourses.nsmallest(10,['21_R1 Points',])
sns.boxplot(x='College Code', y='21_R1 Points', data=BOTpoints21)