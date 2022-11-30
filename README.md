# MTGCEDHDB
"Magic: The Gathering Competitive Elder Dragon Highlander Database" 

Released in 1993, Magic: The Gathering (MTG) was the first-ever trading card game. One popular way to play MTG is a format called Elder Dragon Highlander (EDH) where players battle each other using their own individual decks of exactly 100 cards out of a pool of over 20,000. In each deck all of the cards must have the same colors, no card may be repeated, and one card is assigned a special role of Commander with special rules that sets it apart from the others. 

Although mostly played at home on the kitchen table among friends, EDH is popular enough to draw interest in no-holds-barred tournament games with prizes on the line. Is there any information to be gleaned from tabulating the successes and losses of tournament-level gameplay? Which cards out of the 20,000 available rise to the top? 

The purpose of this project is to collect tournament gameplay results posted online, create a database of wins and losses, and investigate for trends. In short, I want to learn which cards win games.

# TECHNOLOGIES
BeautifulSoup was used to parse downloaded HTML files. I was pretty sure that my method of downloading the tournament data from online sources would be essentially identical to executing a malicious data breach, so I made every effort to precisely target only the data I needed and not trigger any suspicion until I had everything. I started at Page 1 of EDH tournament results, downloaded the source HTML, wrote a Python script that used BS4 to parse for links to the other Pages, and downloaded all of the Pages at once. Next, I wrote a Python script that used BS4 to parse those pages for links to each Tournament, and download all the Tournaments at once. Finally, I wrote a script to parse each tournament page, look for links to individual Decks, and download their source HTML all at once. Each individual Deck webpage has a list of 100 unique cards (with one specially desinated as the Commander), a list name, a player name, a tournament location, a tournament date, and a placement for that event. I would later discover that the website I pulled the data from did in fact treat my actions as a malicious data breach, and since increased site security such that it is no longer possible to obtain data the same way anymore. 

AWS was used to store the downloaded files in the cloud rather than locally. In retrospect, I wish I could have written the original script to dump the data in to an S3 bucket, but at the time I didn't know enough about AWS to make that happen. Nevertheless, the data is in an S3 bucket now, and I intend to use a Lambda script with a BeautifulSoup package installed to parse the source HTML files in the S3 bucket to build the database.


COMPLETE:
 - Tournament data has been collected and saved to an AWS S3 bucket.
 - Create dependencies deployment package for AWS Lambda (bs4)


TODO:
 - Write script to read contents of an html file stored in the bucket
