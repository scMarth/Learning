import os, sys, json, shutil, datetime

date_string = "{}-{}-{}".format(datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().year)

workspace = os.path.dirname(os.path.abspath(__file__))

chrome_bookmarks_dir = r'C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default'.format(os.environ['COMPUTER_USER'])

shutil.copy(chrome_bookmarks_dir + r'\Bookmarks', workspace + r'\{}_Bookmarks'.format(date_string))
shutil.copy(chrome_bookmarks_dir + r'\Bookmarks.bak', workspace + r'\{}_Bookmarks.bak'.format(date_string))
