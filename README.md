# Fundamentals-of-Data-Analysis-2021

## Introduction
The purpose of this assessment is to demonstrate the learning outcomes of the fundamentals of the data analysis module.

**README Table of Contents**

1. GitHub Repository
2. Pyplot Notebook
    - 2.1 About the Pyplot Notebook
    - 2.2 First plot
    - 2.3 What did I learn?
    - 2.4 Biggest challenge
3. CAO Points Notebook
    - 3.1 About the CAO Points Notebook
    - 3.2 What does the Setup at the beginning do?
    - 3.3 The ETL Process
    - 3.4 Analyses of CAO data
    - 3.5 What did I learn?
    - 3.6 Biggest challenge
    - 3.7 Future challenges
4. How to Use the Project
    - 4.1 Github
    - 4.2 NBViewer
    - 4.3 Try at home
    - 4.4 Binder
5. Acknowledgement
6. References

***

# 1. GitHub Repository
GitHub repository contains the following

- 1.1 README.md 
    - This README.md file explains why the repository exists, what is in it, and how to run the notebooks
- 1.2 requirements.txt
    - A requirements.txt file is included to enable someone to quickly run these notebooks with minimal configuration.
- 1.3 pyplot_V3.ipynb
    - Jupyter notebook for Pyplot Notebook
- 1.4 cao_V7.ipynb
    - Jupyter notebook for CAO Points Notebook
- 1.5 Version Control
    - A version control to keep track of changes made to the Jupyter notebooks and learning outcomes.
- 1.6 data
    - Pictures for notebooks
    - cao_V7.ipynb also uses the data folder to read 2018 and 2019 data and save files HTML, pdf and xlsx.  
- 1.7 Coursework
    - Samples of coursework

# 2. Pyplot Notebook - pyplot_V3.ipynb
This README contains an overview of the Pyplot Notebook. The Jupyter notebook contains the main body of work and lists all references used in the assignment.

- 2.1 About the Pyplot Notebook
- 2.2 First plot
- 2.3 What did I learn?
- 2.4 Biggest challenge

### 2.1 About the Pyplot Notebook
The challenge with the Pyplot Notebook was to create an overview pitched at the class for the matplotlib.pyplot python package. 

### 2.2 First plot
The outcomes from this part of the assessment first showed how easy it is to implement plots using the matplotlib.pyplot module. A couple of lines of code can generate plots, and then add new functions to visually see the representation of the relationships and derive an understanding which may not have come from a list of values.

![my_first_pyplot.png](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/data/my_first_pyplot.png)

![subplots.png](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/data/subplots.png)

This is further demonstrated by using real-world energy consumption in India and India and Bangladesh 1972 - 2012

![Electricity_Power_Consumption](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/data/Electricity_Power_Consumption.png)

### 2.3 What did I learn?
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

***Scatterplot*** primary uses are to observe and show relationships between two numeric variables. 

![scatterplot.png](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/data/scatterplot.png)

 Scatterplots have the ability to show distinct groups. This is demonstrated with a link to my project work on the [iris dataset](https://github.com/DPR-droid/pands-project).

![Iris Dataset scatterplot](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/data/Pairwise-Scatterplots.png)

***An exponential plot*** to model the growth of a virus.

![exponential](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/data/exponential.png)

***Stackplot*** track changes over time illustrated using categories of sleeping, eating, college and family time over five days Monday to Friday.

![stackedplot](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/data/stackedplot.png)

### 2.4 Biggest challenge
- Matplotlib library is extensive and has over 70,000 lines of code, 
- Functionality 
- Understanding the issues with pyplot API?  
    - Explicit Code
    - Implicit Code

***

# 3. CAO Points Notebook - cao_V7.ipynb
This README contains an overview of the CAO Points Notebook. The Jupyter notebook contains the main body of work and list all references used in the assignment.

- 3.1 About the CAO Points Notebook
- 3.2 What does the Setup at the beginning do?
- 3.3 The ETL Process
- 3.4 Analyses of CAO data
- 3.5 What did I learn?
- 3.6 Biggest challenge
- 3.7 Future challenges

### 3.1 About the CAO Points Notebook.

The challenge with the CAO Points Notebook was to create an overview pitched at the class of how to load data from different online sources (HMTL, Excel, PDF, CSV), compare that data loaded and output plot and visualisations to enhance the notebook for viewers.

### 3.2 What does the Setup at the beginning do?

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

### 2.3 The ETL Process?
This demonstrates how a data analyst should use the extract, transform, load (ETL) process. 

    1. Extract the data from sources
    2. Transform a series of rules or functions applied to the extracted data in order to prepare it for loading into the end target including data cleansing
    3. Load the data into the end target, a pandas frame [1]

#### 2021 and 2020 CAO Data ETL
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

#### 2019 and 2018 CAO Data ETL
Extract data for 2019 and 2018 the following step 
1. Download original pdf files.
2. Check data in the files
3. Copy Data into Libre Office
4. Delete the preamble on page 1.
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
11. New Dataframe created 
    - AllCourses - 1885 rows × 14 columns

### 3.4 Analyses of CAO data
To complete the CAO points Notebook requires analyses of the data the following steps are completed:
1. Get the summary statistics on the new Dataframe (AllCourses)
2. Get summary statistics of the Mid point, as this is a common column over the 4 years
3. Create a histogram with observations on 
    - The differences between Mid-point from 2018 - 2020
    - The differences between Round 1 in 2020 and 2021
4. Create a new Dataframe with the Top N results to investigate the skewed data in the histograms for points required between 400 to 600
    - Top 10 Colleges providers
    - Top 5 Courses Categories
    - Points required between 400 to 600
5. Use the seaborn module to create a
    - Boxplots for Course Categories for round 1 in 2020 and 2021
    - Pair plot Mid point 2018 - 2020 Final Dataframe

### 3.5 What did I learn?
1. The ETL process
2. Pandas is a multifunctional tool with the ability 
    - Loading and saving data
    - Merges and joins
    - Data inspection
    - Data cleansing
    - Data fill
    - Data normalization
    - Data visualization
    - Statistical analysis

### 3.6 Biggest challenge

Please see the cao_V7.ipynb section 6 other learning outcomes

- How to extract data from HTML and fix errors
    - Sample HTML code is at the end of the notebook to illustrate other learning outcomes
- How to extract data from a PDF file
    - Sample PDF code is at the end of the notebook to illustrate other learning outcomes
- How to zip files 

### 3.7 Future challenges
- Fix reading data from the PDF files
- Automate reading of files
- Create a file check to compare files for changes
- Zip files in Data folder for archive purposes
- Investigate HTML reading data using beautifulsoup4 module.

***

# 4. How to Install and Run the Assessment

- 4.1 Github
- 4.2 NBViewer
- 4.3 Try at home
- 4.4 Binder
     

### 4.1 Github
Review the assessment [Click here cao_V7.ipynb](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/cao_V7.ipynb) or [here for pyplot_V3.ipynb](https://github.com/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/pyplot_V3.ipynb)

### 4.2 NBViewer
NBViewer is another way to share Jupyter Notebook.

To view the cao_V7.ipynb click this badge →→  [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](http://nbviewer.org/github/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/cao_V7.ipynb)

To view the pyplot_V3.ipynb click the badge →→ [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](http://nbviewer.org/github/DPR-droid/Fundamentals-of-Data-Analysis-2021/blob/master/pyplot_V3.ipynb)

### 4.3 Try at home

To try this on your PC you require the following:
- Install Anaconda https://www.anaconda.com/products/individual this distribution includes Python and several packages used in this Assignment including the NumPy package. 
- 'requirments.txt' for other modules required. 
- Install Jupyter https://jupyter.org/ to run cao_V7.ipynb and pyplot_V3.ipynb
- Install Github
- git clone git@github.com:DPR-droid/Fundamentals-of-Data-Analysis-2021.git


### 4.4 Binder
Binder will not have a link in this project as the online virtual executable environment had several issues with loading imports from the requirments.txt file, see below:

    - urllib
    - re
    - warnings
    - time
    - zipfile

When removed from the requirments.txt file the online virtual executable environment would run but was unable to execute segments of the jupyter notebooks

***

# 5. Acknowledgement
Lecturer Ian McLoughlin Fundamentals of Data Analysis GMIT

Family and friends for their support

# 6. References

[1] https://en.wikipedia.org/wiki/Extract,_transform,_load

[1] https://pytutorial.com/check-url-is-reachable

[2] https://en.wikipedia.org/wiki/HTTP_404

[3] https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

[4] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

[5] https://towardsdatascience.com/handling-missing-values-with-pandas-b876bf6f008f

[6] https://stackoverflow.com/questions/37826926/how-to-trim-starting-spaces-of-entire-column-in-libreoffice-or-google-sheets

[7] https://www.kite.com/python/answers/how-to-make-a-single-pandas-DataFrame-from-multiple-%60.csv%60-files-in-python

[8] https://pandas.pydata.org/pandas-docs/version/0.17.0/merging.html

[9] https://www.datasciencemadesimple.com/return-first-n-character-from-left-of-column-in-pandas-python/

[10] https://www.independent.ie/life/family/learning/understanding-your-cao-course-guide-26505318.html

[11] https://stackoverflow.com/questions/38277928/remove-special-characters-in-pandas-DataFrame

[12] http://www2.cao.ie/downloads/documents/Guidelines-EU-EFTA.pdf

[13] https://devenum.com/pandas-convert-multiple-columns-to-float/

[14] https://www.sharpsightlabs.com/blog/pandas-describe/

[15] https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/

[16] https://seaborn.pydata.org/

[17] https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics/cc-6th/v/calculating-interquartile-range-iqr

[18] https://medium.com/@jaimejcheng/data-exploration-and-visualization-with-seaborn-pair-plots-40e6d3450f6d