# Fundamentals-of-Data-Analysis-2021

## Introduction
The purpose of this assessment is to demonstrate the learning outcomes of the fundamentals of data analysis module.

**README Table of Contents**

1. GitHub Repository
2. Pyplot Notebook
3. CAO Points Notebook
4. Review the Assignment

# 1. GitHub Repository
GitHub repository containing two Jupyter notebooks

## 1.1 README.md 
This README.md file explains why the repository exists, what is in it, and how to run the notebooks

## 1.2 requirements.txt
A requirements.txt file is included to enable someone to quickly run this notebooks with minimal configuration.

## 1.3 pyplot_V3.ipynb
Jupyter notebook for Pyplot Notebook

## 1.4 cao_V7.ipynb
Jupyter notebook for CAO Points Notebook

## 1.5 Version Control
A Version control to keep track of changes made to the Jupyter notebooks and learning outcomes.

## 1.6 data
Pictures for notebooks
cao_V7.ipynb also uses the data folder to read 2018 and 2019 data and save files HTML, pdf and xlsx.  

## 1.7 Coursework
Samples of coursework

# 2. Pyplot Notebook - pyplot_V3.ipynb

***pyplot_V3.ipynb Table of Contents***

    1. Overview
    2. Pyplot the first demonstration
    3. What is a figure?
    4. What is the Matplotlib library (Matplotlib, pyplot and pylab)?
    5. Plots from the matplotlib.pyplot
        - 5.1 Scatterplot
        - 5.2 Exponential 
        - 5.3 Stackplot Plot
    6. References
    7. End

## 2.1 About the Pyplot Notebook
The challenge with the Pyplot Notebook was to create an overview pitched at the class for the matplotlib.pyplot python package. 

The outcomes from this part of the assessment first showed how easy it is to implement plots using the matplotlib.pyplot module. A couple of lines of code can generate plots, and then add new functions to visually see the representation of the relationships and derive an understanding which may not have come from a list of values.

![my_first_pyplot.png](data\my_first_pyplot.png)

![subplots.png](data\subplots.png)

This is further demonstrated by using real-world energy consumption in India and India and Bangladesh 1972 - 2012

![Electricity_Power_Consumption](data\Electricity_Power_Consumption.png)

The assessment gave me an understanding of data analysis terms 

What is a:

    - Plot
    - Figure
    - Matplotlib history
    - Explicit Code
    - Implicit Code

When and how to use different plots:
    
    - Scatterplot
    - Exponential
    - Stackedplot

What makes this Pyplot Notebook different is the use of real-world examples to show how matplotlib.pyplot can be used. 

### ***Scatterplot*** primary uses are to observe and show relationships between two numeric variables. 

![scatterplot.png](data\scatterplot.png)

This is demonstrated with a link to my project work on the [iris dataset](https://github.com/DPR-droid/pands-project). This shows with some practise and scatterplots show the distinct groups among three different species of iris.

![Iris Dataset scatterplot](data\Pairwise-Scatterplots.png)

### ***An exponential plot*** to model the growth of a virus.

![exponential](data\exponential.png)

### ***Stackplot*** track changes over time illustrated using categories of sleeping, eating, college and family time over five days Monday to Friday.

![stackedplot](data\stackedplot.png)

The biggest challenge was understanding 
Matplotlib library is extensive and has over 70,000 lines of code, 
Functionality and the 
Issues with pyplot API?  
Explicit Code
Implicit Code
All References are in the Jupyter notebook


# 3. CAO Points Notebook - cao_V7.ipynb
This repository includes a Jupyter notebook called cao_V7.ipynb 

***cao_V7.ipynb Table of Contents***

    1. Setup
        - 1.1 Imports
        - 1.2 Set Time
        - 1.3 CAO URL Availability Function
        - 1.4 CAO HTML Save functions
        - 1.5 CAO file save function
        - 1.6 CAO Webpage links
        - 1.7 CAO Points URL
    2. Import CAO Points into pandas
        - 2.1 Load 2021 Points
        - 2.2 Load 2020 Points
        - 2.3 Load 2019 Points
        - 2.4 Load 2018 Points
        - 2.5 Merge all DataFrames
        - 2.6 Replace and convert values
    3. CAO Points comparison comparison, plots and other visualisations
        - 3.1 Pandas Describe with Observation
        - 3.2 Matplotlib Histogram with Observation
        - 3.3 Top N results with Pandas
        - 3.4 Final Dataframe with Observations using Seaborn mobule
    4. Reference
    5. End of file analysis
    6. Other Learning outcomes
        - 6.1 Pandas import on HTML Data
        - 6.2 Pandas import on PDF Data
        - 6.3 Zip files

## 3.1 About the CAO Points Notebook.

The challenge with the CAO Points Notebook was to create an overview pitched at the class of how to load data from different online sources (HMTL, Excel, PDF, CSV), compare that data loaded and output plot and visualisations to enhance the notebook for viewers.

## 3.2 What does the Setup at the beginning do?

- Imports to run the notebook
- A global timestamp of when the files are extracted and saved. 
- Test functions.
    - Check availability of the CAO website
    - Save the webpage and track changes
    - Save all files to a folder
- CAO Webpage links used for the assessment
    - Using the saved webpage the HTML could be inspected to extract the links with required data 
- CAO Points URL
    - After inspecting the URLs a list of all links to the files used in the project are set here.

## 2.3 What does the Import CAO Points into pandas do?
This demonstrates how a data analyst should use the extract, transform, load (ETL) process. 

    1. ***Extract*** the data from sources
    2. ***Transform*** a series of rules or functions applied to the extracted data in order to prepare it for loading into the end target including data cleansing
    3. ***Load*** the data into the end target, a pandas frame [1]

### 2021 and 2020 CAO Data ETL
Inspect the Excel files to detect any anomalies
- Preamble
- Extra columns
- Header names
- Correct file

Extract data using the pandas.read_excel function 

Transforming the data for 2021 and 2020 
- Skip top N rows to remove the preamble
- Header names to extract data
- The pandas Dataframe columns are renamed
- isna().sum() function is used to identify missing values in a column.
- This information gathered here will later inform how all the Dataframes will be merged

Load the data 2021 and 2020 into the end target, a pandas frame with the following results:
- DF2021 - 1451 rows × 8 columns
- DF2020 - 1464 rows × 8 columns

### 2019 and 2018 CAO Data ETL
Extract data for 2019 and 2018 the following step 
1. Download original pdf files.
2. Check data in the files
3. Copy Data into Libre Office
4. Delete preamble on page 1.
5. Delete headers and footers.
6. Remove all whitespaces
7. Save the data as a CSV file
8. Extract data using the pandas.read_csv function

Transforming the data for 2019 and 2018
- Set header names
- Concatenate level 6 7 data with level 8 data 
- isna().sum() function is used to identify missing values in a column.
- This information gathered here will later inform how all the Dataframes will be merged

Load the data 2019 and 2018 into the end target, a pandas frame with the following results:
- DF2019= 1391 rows × 4 columns
- DF2018= 1385 rows × 4 columns

To analyse the 2018 to 2021 Data from the CAO a single Dataframe is created. The isna().sum() function informed that the College Code (Code) and College Title (Title) had no missing data and these are used as our indexes to join all the data frames together. Merging the Dataframes to create a single Dataframe the following step:
1. New Dataframe is created with only Code and Title
2. Dropping all duplicated in Code creating unique values
3. Create a College code column on the New Dataframe
4. Check for missing values
5. Set the index of Code on the New Dataframe
6. Set the index of Code on the corresponding DF2021, DF2020, DF2019, DF2018 Dataframes
7. Use the Pandas join function with all the required Data in the New Dataframe
8. Check for Missing values
9. Replace and convert values to numeric
    - This step was required and only discovered during the Analyse Data stage.  
10. Check Data types



# 4. Review the Assignment

How to run or review the Jupyter notebook.      

## 4.1 Github
Review the assessment [Click here cao_V7.ipynb](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/cao_V7.ipynb) or [here for pyplot_V3.ipynb](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/pyplot_V3.ipynb)

## 4.2 NBViewer
NBViewer is another way to share Jupyter Notebook.

To view the cao_V7.ipynb click this badge →→  [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](http://nbviewer.org/github/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/cao_V7.ipynb)

To view the pyplot_V3.ipynb click the badge →→ [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](http://nbviewer.org/github/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/pyplot_V3.ipynb)

## 4.3 Try at home

To try this on your own PC you require the following:
- Install Anaconda https://www.anaconda.com/products/individual this ditribution includes Python and serveral packages used in this Assignment including the numpy package. 
- 'requirments.txt' for other modules required. 
- Install Jupyter https://jupyter.org/ to run cao_V7.ipynb and pyplot_V3.ipynb
- Install Github
- git clone git@github.com:DPR-droid/Fundamentals-of-Data-Analysis-2021.git


## 4.4 Binder
Binder will not have a link in this project as the online virtual executable environment had several issue with loading imports from the requirments.txt file, see below:

    - urllib
    - re
    - warnings
    - time
    - zipfile

When removed from the requirments.txt file the online virtual executable environment would run but was unable to execute segments of the jupyter notebooks


***

# References

[1] https://en.wikipedia.org/wiki/Extract,_transform,_load