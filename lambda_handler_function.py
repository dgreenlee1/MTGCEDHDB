import json
import boto3
from bs4 import BeautifulSoup


s3_client = boto3.client("s3")
S3_BUCKET = 'pythontestbucket2022'


def lambda_handler(event, context):
    
    session = boto3.Session()
    bucket_arn = "s3://pythontestbucket2022"
    s3 = session.resource("s3")
    bucket = s3.Bucket("pythontestbucket2022")
    index = 0
    

    for my_bucket_object in bucket.objects.all():
        color_identity = []
        card_list = []
        commander_list = []
        print(my_bucket_object.key)
        file_content = s3_client.get_object(
            Bucket=S3_BUCKET, Key=my_bucket_object.key)["Body"].read()
        print(file_content[0:20])
        soup = BeautifulSoup(file_content, "html.parser") # Make soup
        # Get color identity
        if soup.find_all('span',class_="ms ms-cost ms-w ms-shadow"):
            color_identity.append('W')
        if soup.find_all('span',class_="ms ms-cost ms-u ms-shadow"):
            color_identity.append('U')
        if soup.find_all('span',class_="ms ms-cost ms-b ms-shadow"):
            color_identity.append('B')
        if soup.find_all('span',class_="ms ms-cost ms-r ms-shadow"):
            color_identity.append('R')
        if soup.find_all('span',class_="ms ms-cost ms-g ms-shadow"):
            color_identity.append('G')
        if not color_identity:
            color_identity.append('C')
        color_id = str("".join(color_identity))
        print("- Color Identity:", color_id)
        # Get card info (card list, commander list)
        # enough_cards = True                                       # Sanity check for 100-card decks only.
        for dek in soup.find_all('a'):                              # Get the card list. 
            try:
                dek.get('href')
                if 'prices/' in dek.get('href'):                    # Anything that looks up a price is a card.
                    for x in range (0,int(dek.previous)):
                        card_list.append(dek.get('href')[8:])       # Card names area attached to hrefs, list them.
                        #deck_data['card_list'] = card_list          # Get KEY card_list?
                        # deck_data['deck_size'] = (len(card_list))   # Get KEY deck_size?
            except:
                pass 
        #deck_size = '- Deck Size: '+str(len(card_list))
        #deck_data['deck_size'] = str(len(card_list)
        for com in soup.find_all('th', class_="type Sideboard"):    # Get the Commander list from the Sideboard
            for num in com.find_all('span', class_='small'):
                sb = num.text
                s = int(sb[2])
                for zum in range(0,s):                              # Last 1-2 cards in the card list are commanders
                    kommand = str(card_list[(zum+1)*-1])
                    commander_list.append(kommand)
                    # deck_data['commander_list'] = commander_list  # Dunno why it doesn't like this line
                    
        for gli in (commander_list): # Remove Commanders from the mainboard
            card_list.remove(gli)
        print('- Commanders: '+str(commander_list))
        print('- Card List: '+str(card_list))
        index += 1
        if index == 1:          # It takes a really long time to make the soup, one at a time only
            break
    

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
