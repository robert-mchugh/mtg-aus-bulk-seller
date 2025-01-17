
from selenium import webdriver
from selenium.webdriver.common.by import By  
import boto3
#import json
from datetime import datetime
import ast

def parse_price_results(rawTable):
   
    # takes raw results, returns an array of arrays. Each of the sub-arrays comprises of  items
    # One row is a key value pair, where the key is the card name and the value is an array
    # [Cardname, Quantity, Cash]

    splits = rawTable.split("\n")
    columns = int(4)
    output = {} #dict
    totalRows = int(len(splits) / columns)
    for i in range(totalRows):

        # Parse card name
        thisCardName = splits[i * columns]
        
        # Parse how many they want
        thisManyWantedRaw = splits[i * columns + 1]
        thisManyWanted = int(thisManyWantedRaw[:-2]) #Strip off the last two chars

        #Parse cash
        cashRaw = splits[i * columns + 2]
        cash = float(cashRaw[1:]) #strip the dollar sign

        #Structure the dict
        output[thisCardName] = {"quantityWanted": thisManyWanted,"price": cash}

    return output
        

def get_s3_file_content(bucket, filepath):
    s3 = boto3.resource("s3")
    obj = s3.Object(bucket,filepath)
    data=obj.get()['Body'].read()
    decoded = data.decode("utf-8")
    return decoded

def determine_if_authed_to_mtgmate(page_source):
    if "You are already signed in" in page_source:
        return True
    else:
        return False

def update_price_data(setname):
    #download sets.txt
    #get the URL
    s3bucket = "mtg-seller"
    
    raw_sets = get_s3_file_content(s3bucket,"sets.txt")
    master_sets = ast.literal_eval(raw_sets) #need this because in JSON, definitions are wrapped in "
    #master_sets = json.loads(parsed_json)
    thisSet = master_sets[setname]
    thisSetURL = thisSet["mtgmateurl"]
    driver = webdriver.Chrome()
    
    source = driver.get("https://www.mtgmate.com.au/users/sign_in") #this can be anything where the login page is presented
    page_source = driver.page_source
    authed = determine_if_authed_to_mtgmate(page_source)
    if not authed:
        input("log into mtg mate and press enter to continue...")
    driver.get(thisSetURL) #this has to be where the cards you want to check are
    

    priceData = {}

    found = False
    retryCount = 0
    while found == False:
        try:
            resultsTable = driver.find_element(By.CLASS_NAME,"MuiTableBody-root")
            found = True
        except:
            driver.implicitly_wait(1)
            retryCount = retryCount + 1
            print("Failed to get the data table. Retry " + str(retryCount))  

    thisResult = parse_price_results(resultsTable.text)
    priceData = thisResult

    while 1:
        try:
            nextPageButton = driver.find_element(By.XPATH, "//*[@id=\"pagination-next\"]")
            nextPageButton.click()
        except:
            print("finished trawling, ending gracefully")
            break
        resultsTable = driver.find_element(By.CLASS_NAME,"MuiTableBody-root")
        thisResult = parse_price_results(resultsTable.text)
        priceData.update(thisResult)
    
    noSpecials = remove_specials(setname)
    filePath = "prices/" + noSpecials + ".txt"
    success = write_or_update_file_to_s3(s3bucket,filePath,str(priceData))

    #Update the lastpricecheckdate
    today = datetime.today().strftime('%Y-%m-%d')
    master_sets[setname]["lastpricecheckdate"] = today
        
    #Update the sets.txt with a pathToPricesFile
    master_sets[setname]["pathToPricesFile"] = filePath

    #Write the metadata back to S3 in the sets file
    write_or_update_file_to_s3(s3bucket,"sets.txt",str(master_sets))
    
    print("done")


def remove_specials(inputStr):
    noSpecials = inputStr.translate ({ord(c): " " for c in " !@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    noSpecials = noSpecials.replace(" ","_")
    return noSpecials

def write_or_update_file_to_s3(bucket,filepath,body):
    s3 = boto3.client("s3")
    response = s3.put_object(Body=body,Bucket=bucket,Key=filepath)

def update_all_prices():
    s3bucket = "mtg-seller"
    raw_sets = get_s3_file_content(s3bucket,"sets.txt")
    master_sets = ast.literal_eval(raw_sets)
    for cardset in master_sets.keys():
        update_price_data(cardset)

def price_check(deckname):
    s3bucket = "mtg-seller"
    
    # Get msater data for decks and sets
    raw_decks = get_s3_file_content(s3bucket,"decks.txt")
    master_decks = ast.literal_eval(raw_decks)

    raw_sets = get_s3_file_content(s3bucket,"sets.txt")
    master_sets = ast.literal_eval(raw_sets)
        
    # Retrieve deck list
    pathToDeckList = master_decks[deckname]["pathToDeckList"]
    raw_decklist = get_s3_file_content(s3bucket,pathToDeckList)
    decklist = raw_decklist.split("\r\n")

    #Determine the set
    setName = master_decks[deckname]["setname"]

    #Determine path to pricing
    pathToPriceFile = master_sets[setName]["pathToPricesFile"]
    raw_prices = get_s3_file_content(s3bucket,pathToPriceFile)
    prices = ast.literal_eval(raw_prices)


    theyWouldPay = 0
    sellList = []
    keepList = []
    noMatchList = []
    for i in decklist:

        try :
            thisCard = prices[i]
            if thisCard["quantityWanted"] > 0:
                theyWouldPay = theyWouldPay + thisCard["price"]
                sellList.append([i,thisCard["price"]])
            else:
                keepList.append([i,thisCard["price"]])
        except KeyError:
            noMatchList.append(i)
    return theyWouldPay, sellList, keepList, noMatchList

#theyWouldPay, sellList, keepList, noMatchList = price_check("Squirreled Away")

def export_price_report():
    # Get msater data for decks and sets
    s3bucket = "mtg-seller"
    raw_decks = get_s3_file_content(s3bucket,"decks.txt")
    master_decks = ast.literal_eval(raw_decks)
    report_output = ""
    for deck in master_decks.keys():
        print("Working on: " + deck)
        if master_decks[deck]["pathToDeckList"] == 'decks/UNDEFINED':
            print ("No decklist, skipping: " + deck)
            continue
        theyWouldPay, sellList, keepList, noMatchList = price_check(deck)
        report_output = report_output + master_decks[deck]["setname"] + "\t" + deck + "\t" + str(theyWouldPay) + "\n"
    print("=======================================")
    print(report_output)
            
            
#theyWouldPay, sellList, keepList, noMatchList = price_check("Blood Rites")
    

#input_setname = "Bloomburrow Commander"
#lol = update_price_data(input_setname)



