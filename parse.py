# Name:         Alexandru Galetus
# email:        fibre@montai.me
# file:         parse.py
# Description:  This Python script is used for shiptaime, an automated system for Montaime's shipping and handing
#               operations. The functions allow a user to specify a path to a spreadsheet, parsed by a Pandas dataframe
#               and is sent out to a neatly formatted .txt file. This script is used for tracking updates to customers.

import pandas as pd
from config import *

# sheet_parse()
# parses .xls/.xlsx spreadsheet, given user path
# inputs:       path: string provided by user with path to spreadsheet
# outputs:      arr: 2D array parsed by pandas dataframe
def sheet_parse(path):
    # initializing array
    arr = []
    try:
        # reads from imported .xlsx spreadsheet
        workbook = pd.read_excel(path)
        # checks valid columns (service may be used for Bandcamp API at later time)
        s_fmt = workbook[['Recipient', 'Email', 'Tracking Number', 'Service']]

        # list comprehension to pull customer/email/tracking #s from s_fmt -> 2D array [arr[i][0-3])
        arr = [[x, y, z] for x, y, z in zip(s_fmt['Recipient'], s_fmt['Email'], s_fmt['Tracking Number'])]
    except:
        print("Invalid sheet!")
    return arr

# track_loop()
# Loops through tracking array data provided by sheetParse()
# inputs:       arr: 2D array providing customer name, email, tracking #
# outputs:      none
def track_loop(arr):
    for i in range(len(arr)):
        # arr[i][2] = tracking no
        track_no = arr[i][2]
        # ahoy_b & num_b are bools checking if tracking # is Asendia, USPS Domestic or USPS Intl
        ahoy_b, num_b = AHOY_check(track_no)
        # 2D indices passed to be written to text file alongside bool values above
        write_file(arr[i], ahoy_b, num_b)

# write_file()
# writes parsed customer info to .txt file
# inputs:       cust_info: 1D array passed per each customer including cust name, email & tracking #
#               ahoy_b: bool, checks whether tracking # starts with "AHOY"- if so, true
#               num_b: bool, checks whether a tracking number is entirely numerical (no alphabetical chars / symbols)
# outputs:      none
def write_file(cust_info, ahoy_b, num_b):
    # cust_info array indices:
    # [0] = customer name
    # [1] = customer email
    # [2] = tracking number

    track = cust_info[2]

    # "text.txt" is a placeholder
    # if it already exists, it'll keep appending to that file
    # to be implemented: asking the user to create new file, or give option to append to an existing file

    file = open("test.txt", "a")
    # temp method of fancily printing out customer name & email into .txt file
    file.write(cust_info[0] + " | " + cust_info[1] + " | ")

    # Asendia / Simple Export Rate = ahoy_b
    if ahoy_b:
        # write shipping msg
        file.write(f"{msg_start} {intl_time} {msg_fin} {msg_asendia} {ASENDIA_URL + track} \n")

    # USPS Domestic = not ahoy_b & num_b
    elif not ahoy_b and num_b:
        # write shipping msg
        file.write(f"{msg_start} {dom_time} {msg_fin} {msg_usps} {track} \n")

    # USPS Intl = not ahoy_b & not num_b
    else:
        file.write(f"{msg_start} {intl_time} {msg_fin} {msg_usps} {track} \n")

# AHOY_check()
# checks whether a tracking # starts with the letters "AHOY" and checks whether a tracking number is entirely numeric
# inputs:       track_no: tracking number provided by 2D array at index [i][2]
# outputs:      ahoy_check, num_check
def AHOY_check(track_no):
    ahoy_check = False
    num_check = False

    # If tracking number starts w/ AHOY, ahoy_check = true
    if track_no[0:4] == "AHOY":
        ahoy_check = True

    # if entirely numeric, (9....),  has to be USPS Domestic (Media Mail or First Class), num_check = true
    # check for edge cases...
    elif track_no.isnumeric():
        num_check = True

    # o/w, it's treated as a USPS Intl tracking #
    # some simple export packages going to Canada just use USPS Intl tracking #s -> treat it like a reg USPS intl pkg
    return ahoy_check, num_check

if __name__ == "__main__":
    # user provides spreadsheet path
    usr_path = input("Select a path for the Excel document you'd like to parse: ")

    # check whether the path provided is actually a valid spreadsheet
    arr = sheet_parse(usr_path)
    track_loop(arr)
