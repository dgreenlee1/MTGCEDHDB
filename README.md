# MTGCEDHDB
"Magic: The Gathering Competitive Elder Dragon Highlander Database" 

Released in 1993, Magic: The Gathering (MTG) was the first-ever trading card game. One popular way to play MTG is a format called Elder Dragon Highlander (EDH) where players battle each other using their own individual decks of exactly 100 cards out of a pool of over 20,000. In each deck all of the cards must have the same colors, no card may be repeated, and one card is assigned a special role of Commander with special rules that sets it apart from the others. 

Although mostly played at home on the kitchen table among friends, EDH is popular enough to draw interest in no-holds-barred tournament games with prizes on the line. Is there any information to be gleaned from tabulating the successes and losses of tournament-level gameplay? Which cards out of the 20,000 available rise to the top? 

The purpose of this project is to collect tournament gameplay results posted online, create a database of wins and losses, and investigate for trends. In short, I want to learn which cards win games.

# TECHNOLOGIES
**BeautifulSoup** was used to parse downloaded HTML files. I knew that the website I was pulling from had a lot of data available, and I didn't want to waste bandwith downloading everything and sorting it out later. So I started with Page 1 of the results I wanted, and wrote a script to download each other Page as source HTML. On each Page were links recent Tournament events, so I wrote a script to download each Tournament as source html, and from there download each Deck that was at that tournament. 


COMPLETE:
 - Tournament data has been collected and saved to an AWS S3 bucket.
 - Create dependencies deployment package for AWS Lambda (bs4)


TODO:
 - Write script to read contents of an html file stored in the bucket
