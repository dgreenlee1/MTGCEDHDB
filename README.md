# MTGCEDHDB
"Magic: The Gathering Competitive Elder Dragon Highlander Database" 

Released in 1993, Magic: The Gathering (MTG) was the first-ever trading card game. One popular way to play MTG is a format called Elder Dragon Highlander (EDH) where players battle each other using their own individual decks of exactly 100 cards out of a pool of over 20,000. In each deck all of the cards must share the same colors, no card may be repeated (with few exceptions), and one card is assigned the role of "Commander" with special rules that sets it apart from the others. 

Although mostly played at home on the kitchen table among friends, EDH is popular enough to draw interest in tournament games with prizes on the line. Is there any information to be gleaned from tabulating the successes and losses of tournament-level gameplay? Which cards out of the 20,000 available rise to the top? 

The purpose of this project is to collect tournament gameplay results posted online, create a database of wins and losses, and investigate for trends. In short, I want to learn which cards win games.

# TECHNOLOGIES
**BeautifulSoup** was used to parse downloaded HTML files. I knew that the website I was pulling from had a lot of data available, and I didn't want to waste bandwith downloading everything and sorting it out later. Instead, I used a query string as the base URL, which let me use the site's own search tools to filter the results for me. 

**AWS** is where the main action is. I would have liked to have build the scraper to save results directly to an S3 bucket, but I didn't know enough about the technology at the time. Instead I simply saved the data locally and uploaded it to S3 afterwards. 

COMPLETE:
 - Tournament data has been collected and saved to an AWS S3 bucket.
 - Create dependencies deployment package for AWS Lambda (bs4)


TODO:
 - Write script to read contents of an html file stored in the bucket
