import pandas as pd
from config import *

# parses .xls/.xlsx spreadsheet, given user path
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

# Loops through tracking array data provided by sheetParse()
def track_loop(arr):
    for i in range(len(arr)):
        # arr[i][2] = tracking no
        track_no = arr[i][2]
        # AHOYcheck returns True if track # = simple export rate / asendia tracking, else false
        ahoy_b, num_b = AHOY_check(track_no)
        # 2D indecies individually passed to be written to text file alongside bool value given by AHOYcheck
        write_file(arr[i], ahoy_b, num_b)


def write_file(cust_info, ahoy_b, num_b):
    # [0] = customer name
    # [1] = customer email
    # [2] = tracking number

    track = cust_info[2]

    # create new file and set to append
    # this solution is an issue - it'll keep appending to the same file.
    # need to find a way to make a new file and continue appending, or give the user an option.

    # need a method to provide a new file / overwrite a previous file.
    file = open("test.txt", "a")
    # temp method of fancily printing out customer name & email into .txt file (for now)
    file.write(cust_info[0] + " | " + cust_info[1] + " | ")

    # if tracking is equal = "AHOYXXXXXX", Simple Export Rate is used
    if ahoy_b:
        # there's gotta be a better way to do this other than string concatenation
        file.write(msg_start + intl_time + msg_fin + msg_asendia + ASENDIA_URL + track + "\n")

    # if tracking is entirely numerical (no alphabet/symbols), USPS Domestic used
    elif not ahoy_b and num_b:
        # write shipping msg
        file.write(msg_start + dom_time + msg_fin + msg_usps + track + "\n")

    # else, must be USPS intl shipment
    else:
        # same as above
        file.write(msg_start + intl_time + msg_fin + msg_usps + track + "\n")

# checks whether  a value
def AHOY_check(track_no):
    ahoy_check = False
    num_check = False

    # simple export rate tracking nums start with "AHOY" almost always
    if track_no[0:4] == "AHOY":
        ahoy_check = True

    # if entirely numeric, (9....),  has to be USPS media mail / first class (domestic)
    # check for edge cases...
    elif track_no.isnumeric():
        num_check = True

    # o/w it's simple export (some still use USPS intl #'s if going to Canada) & can be processed as
    # regular USPS tracking #
    return ahoy_check, num_check

if __name__ == "__main__":
    file_exists = False
    usr_path = input("Select a path for the Excel document you'd like to parse: ")

    # check whether the path provided is actually a valid spreadsheet, o/w this breaks

    arr = sheet_parse(usr_path)
    track_loop(arr)
