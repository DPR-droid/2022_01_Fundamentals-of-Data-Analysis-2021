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

## 1.3 cao_V7.ipynb
Jupyter notebook for Pyplot Notebook

## 1.4 pyplot_V3.ipynb
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

## 2.1 About the CAO Points Notebook.

1. 2021
- CAO2021 = 'http://www2.cao.ie/points/CAOPointsCharts2021.xlsx' - 1451 rows × 15 columns


2. 2020
- CAO2020 = 'http://www2.cao.ie/points/CAOPointsCharts2020.xlsx' - 1464 rows × 23 columns

3. 2019
- CAO2019_8 = 'http://www2.cao.ie/points/lvl8_19.pdf' - 930 rows × 4 columns
- CAO2019_76 = 'http://www2.cao.ie/points/lvl76_19.pdf' - 461 rows × 4 columns

4. 2018
- CAO2018_8 = 'http://www2.cao.ie/points/lvl8_18.pdf' - 914 rows × 4 columns
- CAO2018_76 = 'http://www2.cao.ie/points/lvl76_18.pdf' - 471 rows × 4 columns




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