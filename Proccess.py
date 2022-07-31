#!/usr/bin/env python
# coding: utf-8

# # Project Descriptions

# ## Data from Analyze Boston
#
# Each dataset in Analyze Boston has its own resourceID and is in a pattern of "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx."
# Thus, we will first make a disctionary that takes necessary resourceID's as elements and the string of description of each resourceID's as keys.

# We will be using dataset of:
# - CRIMEINCIDENTREPORTS_2022
# - CRIMEINCIDENTREPORTS_2021
# - CRIMEINCIDENTREPORTS_2020
# - CRIMEINCIDENTREPORTS_2019
# - CRIMEINCIDENTREPORTS_2018
# - SHOOTINGS
# - SHOTFIRED
# - FIELDINTERROGATION_2020
# - FIELDINTERROGATION_2019
# - FIELDINTERROGATION_2016
# - FIREARM_RECOVERY
# - EARNINGS_2021
# - EARNINGS_2020
# - EARNINGS_2019
# - EARNINGS_2018
# - EARNINGS_2017
# - EARNINGS_2016
# - EARNINGS_2015
# - EARNINGS_2014
# - EARNINGS_2013
# - EARNINGS_2012
# - EARNINGS_2011
# - CHECKBOOK_2022
# - CHECKBOOK_2021

# In[2]:


# This is the function that forms the dictionary of resourceID's with keys that describes which resourceID connects to which dataset.
def getSourceDict():
    source = {
        "CRIMEINCIDENTREPORTS_2022": "313e56df-6d77-49d2-9c49-ee411f10cf58",
        "CRIMEINCIDENTREPORTS_2021": "f4495ee9-c42c-4019-82c1-d067f07e45d2",
        "CRIMEINCIDENTREPORTS_2020": "be047094-85fe-4104-a480-4fa3d03f9623",
        "CRIMEINCIDENTREPORTS_2019": "34e0ae6b-8c94-4998-ae9e-1b51551fe9ba",
        "CRIMEINCIDENTREPORTS_2018": "e86f8e38-a23c-4c1a-8455-c8f94210a8f1",
        "SHOOTINGS": "313e56df-6d77-49d2-9c49-ee411f10cf58",
        "SHOTSFIRED": "e16705ca-49ce-4803-84c1-c9848aa63024",
        "FIELDINTERROGATION_2020": "64dd32d9-26f9-4275-9265-97fa3de7e22b",
        "FIELDINTERROGATION_2019": "03f33240-47c1-46f2-87ae-bcdabec092ad",
        "FIELDINTERROGATION_2016": "35f3fb8f-4a01-4242-9758-f664e7ead125",
        "FIREARM_RECOVERY": "a3d2260f-8a41-4e95-9134-d14711b0f954",
        "EARNINGS_2021": "ec5aaf93-1509-4641-9310-28e62e028457",
        "EARNINGS_2020": "e2e2c23a-6fc7-4456-8751-5321d8aa869b",
        "EARNINGS_2019": "3bdfe6dc-3a81-49ce-accc-22161e2f7e74",
        "EARNINGS_2018": "31358fd1-849a-48e0-8285-e813f6efbdf1",
        "EARNINGS_2017": "70129b87-bd4e-49bb-aa09-77644da73503",
        "EARNINGS_2016": "8368bd3d-3633-4927-8355-2a2f9811ab4f",
        "EARNINGS_2015": "2ff6343f-850d-46e7-98d1-aca79b619fd6",
        "EARNINGS_2014": "941c9de4-fb91-41bb-ad5a-43a35f5dc80f",
        "EARNINGS_2013": "fac6a421-72fb-4f85-b4ac-4aca1e32d94e",
        "EARNINGS_2012": "d96dd8ad-9396-484a-87af-4d15e9e2ccb2",
        "EARNINGS_2011": "a861eff8-facc-4372-9b2d-262c2887b19e",
        "CHECKBOOK_2022": "0a261d4e-3eec-4bac-bf72-b9a7aa77b033",
        "CHECKBOOK_2021": "32897eeb-d9ca-494f-93b1-991c50bcd6a6"
    }
    return source


# **Requests library**
#
# Instead of manually add query, we will use requests (HTTP) library to directly access to the dataset.

# In[3]:


import requests


# Example queries using requests:
#
# r = requests.get('--url address of the source page from Analyze Boston--')

# **Helping functions**
#
# As a helping function, we will make a function to convert from the name of the source to resourceID, and a function to create a list of srouces we are using in the dictionary.

# In[4]:


# fromNametoID function takes a string of name of the source as input. It searches the key in the source dictionary that is the same
# as the input. It will return the resourceID of the found key.
def fromNametoID(sourceName):
    ID = getSourceDict()[sourceName]

    return ID

# sourceList function takes no input. It will iterate through the keys in the source dictionary and return the list of keys (strings)
# in the dictionary (names of sources).
def sourceList():
    srcList = []
    dic = getSourceDict()
    for key in dic:
        srcList.append(key)

    return srcList


# **Use of Query**
#
# Analyze Boston has a specific form of url query form that returns the data in a form that we want (ex. first 5 data from the dataset,
# data with specific name from the dataset, etc.). The general form of the query is:
#
# **first # results**
# https://data.boston.gov/api/3/action/datastore_search?resource_id=(--resourceID of the source we want the data)&limit=#
# (# is an integer, which indicates first # results we want to get)
#
# **results containing 'jones'**
# https://data.boston.gov/api/3/action/datastore_search?resource_id=(--resourceID of the source we want the data)&q=jones
# ('jones' can be replaced with any string we want to include in the results)
#
# From the query, we are returning data in json format.
#
# Other examples of queries can be found from "Analyze Boston -> DATASETS (on the top right) -> search name of dataset -> scroll down for DATA AND RESOURCES -> preview the dataset we want to use -> in the url, there are resourceID and DATA API will include more explanation.

# In[5]:


# function for first # results. It will take the resourceID (string) and n (intger) as inputs. It will return the first n data from
# the dataset within the input resourceID in json.
def first_n_result(ID, n):
    result = requests.get("https://data.boston.gov/api/3/action/datastore_search?resource_id="+ID+"&limit="+str(n))

    return result.json()

# function for results containing 'jones'. It will take the resourceID (string) and contained (string) as inputs. It will return
# the data that contains the contained strings from the dataset within the input resourceID in json.
def contained_result(ID, contained):
    result = requests.get("https://data.boston.gov/api/3/action/datastore_search?resource_id="+ID+"&q="+contained)

    return result.json()


# **Parsing the returned jason**
#
# We will create two parsing functions:
# - A function that takes the json from the query as an input. It will return the fields of the data in json with types and names.
# - A function that takes the json from the query as an input. It will return the metadata of the data in json.

# If we search the url in the query form on google, we can see the format of the dataset in json. From this format, we can see that the data is stored in a form of dictionary. Since what we want from the data is the fields and records from the result part of the data, we will only take [result][fields] for the data fields and [result][records] for the actual data values.

# In[6]:


# data_fields function takes the json returned from the query as an input. It will return the fields of the data in json with
# types and names.
def data_fields(rejson):
    return rejson['result']['fields']

# data_meta function takes the json returned from the query as an input. It will return the records of the data in json.
def data_meta(rejson):
    return rejson['result']['records']


# ## Example run with EARNINGS_2021 Data
#
# we will try to run the functions to demonstrate how they can be used to display the imformation we want from the dataset.

# **Listing out the data srouces we have in the source dictionary**
#
# WE will first check which data sources we have in our source dictionary. Make sure to go on the Analyze Boston website, and add all the data sources we need in the source dictionary.

# In[7]:


# Using sourceList() to get the list of names of sources in the dictionary.
srcList = sourceList()

# Printing each elements (names of sources) in the srcList.
for i in srcList:
    print(i)


# **Get resourceID from the source name, testing query, and checking fields of the data**
#
# Since we decided to use EARNINGS_2021 dataset for the example, we will use its source name to obtain the corresponding resourceID. Then we will test one of the query (in this example, we will make a query on getting the first 5 data from the dataset). From the data we get from the query, we will check the fields of the data (this should be the same as the heading of the data from the excel file we can visualize by downloading the actual data from Analyze Boston).

# In[8]:


# We will use EARNINGS_2021 data for this example.
use = "EARNINGS_2021"

# Using fromNametoID(), we are getting the resourceID of the EARNINGS_2021 dataset from Analyze Boston
resourceID = fromNametoID(use)

# Checking the resourceID of the "EARNINGS_2021": ec5aaf93-1509-4641-9310-28e62e028457
print(resourceID)

# For this example, we will use the query of first 5 results of the data
data_5 = first_n_result(resourceID, 5)

# to check the fields in the dataset, we will use data_fields() with the input of the data result we got from the query.
fields = data_fields(data_5)

# Checking the fields of the dataset
for i in range(0,len(fields)):
    print(fields[i])


# ## Formatting and sorting data

# **Using numpy**
#
# For the example of formatting and sorting using numpy, we will continue to use EARNINGS_2021 dataset. You can use the other datasets and follow the same process to format and sort the data.

# We will first set the n (variable to indicate the number of data) as huge enough number to ensure that we retrieve all the data from the dataset.

# In[9]:


# It is okay for n to exceed the number of data, since we just want to ensure that we iterate all the data in the dataset.
n = 1000000


# Then as we have done in the previous example, we will take the fields of the data, and store the types and ids of it in separate arrays. To get the fields and types of the data, we only need to analyze one set of data since every data will have the same fields and types. Thus for this part, we will be using the query of getting the first one data from the dataset (first_n_result(resourceID, 1)).

# In[10]:


# Create arrays to store ids and types
data_type = []
data_id = []

dataset = "EARNINGS_2021"

# Convert the dataset name to resourceID
resourceID = fromNametoID(dataset)

# Get data fields
data = data_fields(first_n_result(resourceID,1))

# Iterate through the fields and store the ids and types
for i in range(len(data)):
    data_type.append(data[i]['type'])
    data_id.append(data[i]['id'])


# With the arrays of data fields and ids, we will start reformatting the records of the data. To start with it, we will first get the metadata. For this part, since we want to work with every data in the dataset, we will use previously assigned n in the query (retrieveing first n data).

# In[11]:


# Getting the metadata of the first n data from the dataset
metadata = data_meta(first_n_result(resourceID, n))


# If we analyze the fields of the data from above example, we see that in json format of the data, the numeric values of the data is stored in string format (type = text). In the following process, we will convert the string (text) format of the numeric value data into float (int) format.

# In[ ]:
