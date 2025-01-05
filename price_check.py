
from selenium import webdriver
from selenium.webdriver.common.by import By  



def parse_results(rawTable):
   
    # takes raw results, returns an array of arrays. Each of the sub-arrays comprises of  items
    # One row is a key value pair, where the key is the card name and the value is an array
    # [Cardname, Quantity, Cash]

    splits = rawTable.split("\n")
    columns = int(4)
    output = [] #array
    totalRows = int(len(splits) / columns)
    for i in range(totalRows):
        thisCardArray = []

        # Parse card name
        thisCardName = splits[i * columns]
        thisCardArray.append(thisCardName)
        
        # Parse how many they want
        thisManyWantedRaw = splits[i * columns + 1]
        thisManyWanted = int(thisManyWantedRaw[:-2]) #Strip off the last two chars
        thisCardArray.append(thisManyWanted)

        #Parse cash
        cashRaw = splits[i * columns + 2]
        cash = float(cashRaw[1:]) #strip the dollar sign      
        thisCardArray.append(cash)

        output.append(thisCardArray)
    return output
        
        
driver = webdriver.Chrome()
driver.get("https://www.mtgmate.com.au/buylist/magic_sets/onc") #this can be anything where the login page is presented
input("log into mtg mate and press enter to continue...")
driver.get("https://www.mtgmate.com.au/buylist/magic_sets/dsc") #this has to be where the cards you want to check are
page_source = driver.page_source

masterData = []

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

thisResult = parse_results(resultsTable.text)
masterData = thisResult

while 1:
    try:
        nextPageButton = driver.find_element(By.XPATH, "//*[@id=\"pagination-next\"]")
        nextPageButton.click()
    except:
        print("finished trawling, ending gracefully")
        break
    resultsTable = driver.find_element(By.CLASS_NAME,"MuiTableBody-root")
    thisResult = parse_results(resultsTable.text)
    masterData = masterData + thisResult

#https://www.mtgmate.com.au/buylist/magic_sets/dsc
miracle_worker = """Adarkar Wastes
Aminatou's Augury
Ancient Cellarspawn
Arcane Denial
Arcane Sanctum
Arcane Signet
Archetype of Imagination
Arvinox, the Mind Flail
Ash Barrens
Athreos, Shroud-Veiled
Auramancer
Azorius Chancery
Azorius Signet
Bojuka Bog
Bottomless Pool/Locker Room
Brainstone
Brainstorm
Burnished Hart
Cast Out
Caves of Koilos
Command Tower
Commander's Sphere
Cramped Vents/Access Maze
Demon of Fate's Design
Diabolic Vision
Dimir Aqueduct
Doomwake Giant
Dream Eater
Entreat the Angels
Evolving Wilds
Extravagant Replication
Fear of Sleep Paralysis
Halimar Depths
Hall of Heliod's Generosity
Inkshield
Life Insurance
Mesa Enchantress
Metamorphosis Fanatic
Mind Stone
Mirrormade
Monologue Tax
Moon-Blessed Cleric
Nightmare Shepherd
Obscura Storefront
Ondu Spiritdancer
One with the Multiverse
Orzhov Basilica
Orzhov Signet
Otherworldly Gaze
Phenomenon Investigators
Ponder
Portent
Prognostic Sphinx
Read the Bones
Redress Fate
Return to Dust
Secret Arcade/Dusty Parlor
Shark Typhoon
Sigil of the Empty Throne
Soaring Lightbringer
Sol Ring
Solemn Simulacrum
Sphere of Safety
Spirit-Sister's Call
Starfield Mystic
Swords to Plowshares
Tainted Field
Tainted Isle
Telling Time
Temple of Deceit
Temple of Enlightenment
Temple of Silence
Terminus
Terramorphic Expanse
The Eldest Reborn
The Master of Keys
Thirst for Meaning
Thriving Heath
Thriving Isle
Thriving Moor
Time Wipe
Timely Ward
Underground River
Utter End
Verge Rangers
Aminatou, Veil Piercer (Borderless)"""

rebellion_rising = """Adriana, Captain of the Guard
Arcane Signet
Assemble the Legion
Battle Screech
Boros Charm
Boros Garrison
Boros Signet
Buried Ruin
Call the Coppercoats
Castle Ardenvale
Castle Embereth
Chain Reaction
Clever Concealment
Collective Effort
Command Tower
Commander's Sphere
Court of Grace
Cut a Deal
Dragonmaster Outcast
Elspeth Tirel
Emeria Angel
Exotic Orchard
Felidar Retreat
Fellwar Stone
Finale of Glory
Flawless Maneuver
Forgotten Cave
Furycalm Snarl
Generous Gift
Glimmer Lens
Goldnight Commander
Goldwardens' Gambit
Harmonious Archon
Hate Mirage
Heroic Reinforcements
Hexplate Wallbreaker
Hordeling Outburst
Hour of Reckoning
Idol of Oblivion
Increasing Devotion
Intangible Virtue
Jor Kadeen, the Prevailer
Kemba's Banner
Kher Keep
Legion Warboss
Loxodon Warhammer
Loyal Apprentice
Mace of the Valiant
Martial Coup
Mask of Memory
Maul of the Skyclaves
Mentor of the Meek
Midnight Haunting
Mind Stone
Myr Battlesphere
Myriad Landscape
Otharri, Suns' Glory
Path of Ancestry
Path to Exile
Phantom General
Prava of the Steel Legion
Rip Apart
Roar of Resistance
Secluded Steppe
Siege-Gang Commander
Silverwing Squadron
Slayers' Stronghold
Sol Ring
Solemn Simulacrum
Soul-Guide Lantern
Staff of the Storyteller
Talisman of Conviction
Temple of the False God
Temple of Triumph
Vulshok Factory
White Sun's Zenith
Windbrisk Heights
Neyali, Suns' Vanguard"""

squirreled_away = """Academy Manufactor
Arasta of the Endless Web
Arcane Signet
Barren Moor
Bastion of Remembrance
Beastmaster Ascension
Beledros Witherbloom
Binding the Old Gods
Bojuka Bog
Cache Grab
Casualties of War
Chatterfang, Squirrel General
Chatterstorm
Chittering Witch
Chitterspitter
Command Tower
Deadly Dispute
Decree of Pain
Deep Forest Hermit
End-Raze Forerunners
Evolving Wilds
Exotic Orchard
Garruk, Cursed Huntsman
Gilded Goose
Golgari Rot Farm
Golgari Signet
Gourmand's Talent
Grim Backwoods
Haunted Mire
Haywire Mite
Hazel's Brewmaster
Honored Dreyleader
Idol of Oblivion
Insatiable Frugivore
Jungle Hollow
Llanowar Wastes
Maelstrom Pulse
Maskwood Nexus
Moldervine Reclamation
Moonstone Eulogist
Morbid Opportunist
Nadier's Nightblade
Necroblossom Snarl
Nested Shambler
Ogre Slumlord
Oran-Rief, the Vastwood
Path of Ancestry
Plaguecrafter
Plumb the Forbidden
Poison-Tip Archer
Prosperous Innkeeper
Putrefy
Ravenous Squirrel
Rootcast Apprenticeship
Saw in Half
Scurry of Squirrels
Second Harvest
Shamanic Revelation
Skullclamp
Skyfisher Spider
Sol Ring
Squirrel Nest
Squirrel Sovereign
Swarmyard
Swarmyard Massacre
Sword of the Squeak
Tainted Wood
Talisman of Resilience
Tear Asunder
Temple of Malady
Terramorphic Expanse
The Odd Acorn Gang
Tireless Provisioner
Toski, Bearer of Secrets
Tranquil Thicket
Twilight Mire
Viridescent Bog
Windgrace's Judgment
Woe Strider
Wolfwillow Haven
Woodland Cemetery
Zulaport Cutthroat
Hazel of the Rootbloom (Borderless)"""

# https://www.mtgmate.com.au/buylist/magic_sets/m3c
creative_energy = """Adarkar Wastes
Aether Hub
Aether Refinery
Aethergeode Miner
Aethersphere Harvester
Aethersquall Ancient
Aetherstorm Roc
Aethertide Whale
Aetherworks Marvel
Akroma's Will
Amped Raptor
Angel of Invention
Arcane Signet
Aurora Shifter
Austere Command
Azorius Chancery
Battlefield Forge
Bespoke Battlewagon
Bident of Thassa
Blaster Hulk
Brudiclad, Telchor Engineer
Burnished Hart
Castle Vantress
Cayth, Famed Mechanist
Coalition Relic
Combustible Gearhulk
Command Tower
Confiscation Coup
Conversion Apparatus
Coveted Jewel
Decoction Module
Demolition Field
Era of Innovation
Farewell
Filigree Racer
Frostboil Snarl
Furycalm Snarl
Glimmer of Genius
Goldspan Dragon
Gonti's Aether Heart
Grenzo, Havoc Raiser
Hourglass of the Lost
Izzet Boilerworks
Izzet Generatorium
Jolted Awake
Legion Loyalty
Lightning Runner
Localized Destruction
Midnight Clock
Myr Battlesphere
Mystic Gate
Mystic Monastery
Overclocked Electromancer
Port Town
Prairie Stream
Professional Face-Breaker
Razorfield Ripper
Roil Cartographer
Salvation Colossus
Scurry of Gremlins
Shivan Reef
Silverquill Lecturer
Skyclave Apparition
Sol Ring
Solar Transformer
Solemn Simulacrum
Sphinx of the Revelation
Stone Idol Generator
Swords to Plowshares
Talisman of Conviction
Talisman of Creativity
Talisman of Progress
Temple of Enlightenment
Temple of Epiphany
Temple of Triumph
Tezzeret's Gambit
Unstable Amulet
Wayfarer's Bauble
Whirler Virtuoso
Satya, Aetherflux Genius"""

thisPrecon = miracle_worker #change it based on the variable name above (or add your own)

thisPreconList = thisPrecon.split("\n")
theyWouldPay = 0
for i in thisPreconList:
    match = False
    for j in masterData:
        
        if i == j[0]: #if the line in the list matches a name of a card on mtgmate
            if j[1] > 0: #they'll buy it
                theyWouldPay = theyWouldPay + j[2]
                print("SELL",j)
                match = True
            else:
                print("NO SELL", j)
                match = True
    if match == False:
        print("NO MATCH", i)
print("If you sold all of the cards marked as SELL, you'd receive: " + str(theyWouldPay))


