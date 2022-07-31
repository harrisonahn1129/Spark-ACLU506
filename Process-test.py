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

import requests

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

    # data_fields function takes the json returned from the query as an input. It will return the fields of the data in json with
# types and names.
def data_fields(rejson):
    return rejson['result']['fields']

# data_meta function takes the json returned from the query as an input. It will return the records of the data in json.
def data_meta(rejson):
    return rejson['result']['records']

    # Using sourceList() to get the list of names of sources in the dictionary.
srcList = sourceList()

# Printing each elements (names of sources) in the srcList.
for i in srcList:
    print(i)


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
