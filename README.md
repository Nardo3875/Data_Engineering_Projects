# Data-Engineering
My Portfolio (Data Engineering Projects)




# Data Mining for Exploration & Machine Learning Notebook

By Leonard M. Newbill
Sources, Content, Software:
Source Data: WIKIPEDIA - https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue
Software: VS Code 
Libraries: See Code Block1
Code Storage & repository: GitHub


## Web Scraping with BeautifulSoup in Python

We use Python's `requests` library to make a GET request to a Specified URL, 
and then use `BeautifulSoup` from the `bs4` (Beautiful Soup) 
Library to Parse the HTML Content of the Page.



## Extract Data from HTML Table and Create a Pandas DataFrame

Check Pandas DataFrame for the Sum of Null Values
Use the value_counts() Function to Get an Overall Picture of the DataFrame Values.
Use the info() Function to Get all Dataframe Information.



## Clarify the Exact Column Names for Machine Learning Process.

This code performs data preprocessing by converting relevant columns to strings, removing commas, and handling NaN values. After preprocessing, it divides the data into categories (e.g., top 10 companies, next 10 companies) and plots line graphs for each category to visualize revenue trends.



## Web Scraping to Extract Information about the Largest Companies in the United States by Revenue from a Wikipedia page.

This code creates a DataFrame (cd) to store the data and performs data cleaning and preprocessing. The preprocessed data is split into training and testing sets, and categorical variables are encoded using Label Encoding. The code trains a machine learning model (Random Forest Regressor) on the training set and evaluates its performance on the test set using Mean Absolute Error. Finally, it demonstrates making a revenue prediction on new data using the trained model.




## Data Preprocessing and Train a Random Forest Regression Model to Predict Revenue.



## Generate Two Plots to Assess the Performance of the Regression Model.

