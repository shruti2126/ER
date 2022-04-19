"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014
Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:
1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.
Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub
import os

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file

        items_dat = open("Items.dat", "a")
        category_dat = open("Category.dat", "a")
        bid_dat = open("Bid.dat", "a")
        seller_dat = open("Seller.dat", "a")

        for item in items:
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            # TODO: How do we enforce primary keys? do we delete rows that don't follow the rules?
            # TODO: remove duplicates.
            # TODO: itemid and number of bids? rating?
            # NOTE: escape double quotes and null strings are NONE

            #QUESTION: We haven't used the transform dollar and dttm functions provided
            # if ("Buy_Price" in item.keys()):
        # Buy_Price = str(transformDollar(item['Buy_Price']))

            # Fill Items.dat
            item_id = item["ItemID"] if "ItemID" in item.keys() and item['ItemID'] else "-1"
            name = "\"" + item["Name"].replace("\"", "\"\"") + "\"" if "Name" in item.keys() and item["Name"] else "\"NONE\""
            currently = transformDollar(item['Currently']) if "Currently" in item.keys() and item['Currently'] else "-1"
            first_bid = transformDollar(item['First_Bid']) if "First_Bid" in item.keys() and item['First_Bid'] else "-1"
            seller_id = "\"" + item["Seller"]["UserID"].replace("\"", "\"\"") + "\"" if "Seller" in item.keys() and "UserID" in item["Seller"].keys() and item["Seller"]["UserID"] else "\"NONE\""
            buy_price = transformDollar(item['Buy_Price']) if "Buy_Price" in item.keys() and item['Buy_Price'] else "-1"
            started = transformDttm(item['Started']) if "Started" in item.keys() and item['Started'] else "0000-00-00 00:00:00"
            ends = transformDttm(item['Ends']) if "Ends" in item.keys() and item['Ends'] else "0000-00-00 00:00:00"
            description = "\"" + item["Description"].replace("\"", "\"\"") + "\"" if "Description" in item.keys() and item["Description"] else "\"NONE\""
            num_bids = item["Number_of_Bids"] if "Number_of_Bids" in item.keys() and item['Number_of_Bids'] else "-1"

            # create one row of Items dat file
            items_row = [item_id, name, currently, first_bid, buy_price, seller_id, num_bids, started, ends, description]
            items_row = map(str, items_row)
            items_row = "|".join(items_row) + "\n"
            # append to Items dat file
            items_dat.write(items_row)

            # Fill Category.dat
            if item["Category"]:
                for org_cat in item["Category"]:
                    cat = "\"" + org_cat.replace("\"", "\"\"") + "\""

                    cat_row = item_id + "|" + cat + "\n"
                    category_dat.write(cat_row)

            # Fill Sellers.dat
            seller_rating = item["Seller"]["Rating"] if "Seller" in item.keys() and "Rating" in item["Seller"].keys() and item["Seller"]["Rating"] else "-1"
            sell_row = seller_id + "|" + seller_rating + "\n"
            seller_dat.write(sell_row)

            # Fill Bid.dat
            if item["Number_of_Bids"] != "0":
                for bid_0 in item["Bids"]:
                    bid = bid_0["Bid"]
                    bidder = bid["Bidder"]

                    # print(item["Bids"])
                    # print(bid)
                    # print(bidder["Country"])
                    # exit()

                    amount = transformDollar(bid["Amount"]) if "Amount" in bid.keys() and bid["Amount"] else "-1"
                    bidder_id = "\"" + bidder["UserID"].replace("\"", "\"\"") + "\"" if "UserID" in bidder.keys() and bidder["UserID"] else "\"NONE\""
                    time = transformDttm(bid["Time"]) if "Time" in bid.keys() and bid["Time"] else "0000-00-00 00:00:00"
                    location = "\"" + bidder["Location"].replace("\"", "\"\"") + "\"" if "Location" in bidder.keys() and bidder["Location"] else "\"NONE\""
                    country = "\"" + bidder["Country"].replace("\"", "\"\"") + "\"" if "Country" in bidder.keys() and bidder["Country"] else "\"NONE\""
                    bidder_rating = bidder["Rating"] if "Rating" in bidder.keys() and bidder["Rating"] else "-1"
                    bid_row = [item_id, amount, time, bidder_id, bidder_rating, location, country]
                    bid_row = "|".join(bid_row) + "\n"
                    bid_dat.write(bid_row)
  
        items_dat.close()
        category_dat.close()
        bid_dat.close()
        seller_dat.close()

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print(sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>')
        sys.exit(1)

    if(os.path.exists("Items.dat")):
        os.remove("Items.dat")
    if(os.path.exists("Category.dat")):
        os.remove("Category.dat")
    if(os.path.exists("Bid.dat")):
        os.remove("Bid.dat")
    if(os.path.exists("Seller.dat")):
        os.remove("Seller.dat")
    
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print ("Success parsing " + f)

if __name__ == '__main__':
    main(sys.argv)