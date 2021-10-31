import pandas as pd

if __name__ == "__main__":
    s = True
    usr_path = input("Select a path for the Excel document you'd like to parse: ")
    try:
        workbook = pd.read_excel(usr_path)
        s_fmt = workbook[['Recipient', 'Email', 'Tracking Number', 'Service']]
        # progress, shoutout list comp!
        result = [[x,y] for x, y in zip(s_fmt['Recipient'], s_fmt['Tracking Number'])]
        print(result)
    except FileNotFoundError:
        print("Invalid sheet!")