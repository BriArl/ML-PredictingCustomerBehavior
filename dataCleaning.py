#Set up import staments for libraries
import pandas as pd
import matplotlib.pyplot as pit
import seaborn as sns
import squarify as sq

#read in this online retail dataset excel file from datasets folder
#pandas DataFrame will provide data types for the different columns within the excel file
retail_dataset = pd.read_excel("./datasets/Online_Retail.xlsx")
retail_dataset.head(10);

#displays record count
retail_dataset.shape

#.info (Pandas) gives us the data types for diffrent columns
retail_dataset.info

#there are a few columns I will not need (even for exploratory data analysis)
# I dropped the columns for StockCode and CustomerID, this makes dataset easier to analyze
retail_dataset = retail_dataset.drop(["StockCode", "CustomerID"], axis =1)
retail_dataset.head

#invoked .strip function so all the leading a trailing white spaces get removed
retail_dataset["Description"] = retail_dataset["Description"].str.strip()
retail_dataset.head()

#checks for any null values in he dataset
retail_dataset.isnull().sum()

#drops any null values present in the data set
retail_dataset.dropna(inplace = True)
retail_dataset.shape

#My market analysis is looking for which products were purchased together(itemsets)
#Eliminating those invoices which contain the character C which are returns (getting ride of rules)
(retail_dataset["InvoiceNo"].str.contains("C")).value_counts()
retail_dataset=retail_dataset[-retail_dataset["InvoiceNo"].str.contains("C")]
retail_dataset.shape

#This data has a lot of duplicates. Im going to drop all the records which are duplicates of other records in the data
retail_dataset_duplicates = retail_dataset[retail_dataset.duplicated()]
retail_dataset_duplicates

#Getting  rid of unncessary info like if people paid postage on thier invoices helps clear up the data
postage = retail_dataset["Description"] == "POSTAGE"
postage.value_counts()
retail_dataset.shape

#For the purpose of my market basket analysis, I'm soley intrested in seeing goods sold in specific contries
# Focus: Germany, France, Spain, Netherlands, and Belgium
(retail_dataset["Country"]).value_counts()
#I filtered out all the records that dont belong to these contries specifically
conutry_list = ["Germany", "France", "Spain", "Netherlands", "Belgium"]
retail_dataset = [retail_dataset.loc["Country"].isin(conutry_list)]\
                                .rest_index().drop('index', axis=1)
retail_dataset.shape

#after execuing these data cleaning methods I am now left with 23,500 records..initially we started with over 500,000