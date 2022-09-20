# Remnants of the web scraper used to download the data.
# The data to be scraped was presented as a simple navigable list of 84 pages Tournament hyperlinks.
# Each of those links went to a page containing hyperlinks to individual Participant files.
# The scraper opened the pages in order, picked out all the Tournament hyperlinks, and downloaded those pages in html form.
# Then each of those pages was opened up one-by-one, and each of the Participant files were downloaded in html form.

# About 10k Participant files were downloaded this way, comprising about 1 GB of data
# Participant files contain usernames, dates, locations, and other identifying information


import os
from os import walk
import bs4
import requests
import re
from bs4 import BeautifulSoup
dum_url = ' '                                                # Dummy base URL
page_url = ' '                                               # Another dummy URL

# Go through each page and look for links.
for i in range(1,84):
    new_url = page_url + str(i)
    print(page_url+str(i))
    page = requests.get(new_url)
    myfile = open('page_temp.txt','w+') # open the saved PAGE file for reading text
    contents = myfile.read()         # read the entire file to string
    myfile.close()                   # close the file
    os.remove('page_temp.txt')            # delete the file
    soup = BeautifulSoup(contents, 'html.parser')
    print(soup)
    
# Create list of tournaments by unique ID
tumlist = []                                                 # List of tournaments by unique ID
for file in os.listdir("/file_path/"):                       # Look through files in this folder
    if file.endswith(".txt"):                                # Check the ones saved as .txt
        tumlist.append(os.path.join("/mydir", file)[-9:-4])  # add the 5-digit ID to the list

# Open the files corresponding to the items in the list
for tum in tumlist:
    myfile = open('tournament_'+tum+'.txt', 'rt')            # open the saved PAGE file for reading text
    contents = myfile.read()                                 # read the entire file to string
    myfile.close()                                           # close the file
    soup = BeautifulSoup(contents, 'html.parser')

    for tr in soup.find_all("a"):                            # Look for any <a> tags
        numlist = []                                         # Start with an empty list
        dumlist = []
        try:
            href_generator = tr['href']                      # Get the ones that have an href, those go to individual Decks
        except:
            continue
        if bool(re.search(r'\d{5}', href_generator)) == True: # REGEX Check to see if the href has a 4-digit number
            numlist.append(href_generator)                    # If it does, add it to the list of deck numbers to check
        # Extract the last 5 digits of each ID
        for i in range(len(numlist)):
            test_string = numlist[i]
            res = ''.join(filter(lambda i: i.isdigit(), test_string))
            dumlist.append(res[-5:])                          # Take all of the Deck unique ID's into a list
        
        for d in range(len(dumlist)):
            new_url = dum_url + dumlist[d]                    # Go to each of those Deck pages and download it
            print("Now downloading tournament_"+dumlist[d])
            page = requests.get(new_url)
            f = open('tournament_'+dumlist[d]+'.txt', 'wb')
            f.write(page.content)
            f.close
