
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
driver.get("https://www.mtgmate.com.au/buylist/magic_sets/cmm") #this has to be where the cards you want to check are
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

#https://www.mtgmate.com.au/buylist/magic_sets/who
paradox_power = """Arcane Signet
Beast Within
Become the Pilot
Bigger on the Inside
Bill Potts
Carpet of Flowers
Chaos Warp
Cinder Glade
Clara Oswald
Command Tower
Confession Dial
Cultivate
Cursed Mirror
Dan Lewis
Danny Pink
Decaying Time Loop
Desolate Lighthouse
Dreamroot Cascade
Exotic Orchard
Farseek
Fiery Islet
Flaming Tyrannosaurus
Flatline
Frontier Bivouac
Frost Fair Lure Fish
Frostboil Snarl
Fugitive of the Judoon
Gallifrey Council Chamber
Game Trail
Graham O'Brien
Growth Spiral
Heaven Sent
Impending Flux
Into the Time Vortex
Iraxxa, Empress of Mars
Jenny Flint
Karvanista, Loyal Lupari
Last Night Together
Lunar Hatchling
Madame Vastra
Me, the Immortal
Memory Worm
Myriad Landscape
Nardole, Resourceful Cyborg
Ominous Cemetery
Osgood, Operation Double
Path of Ancestry
Ponder
Preordain
Psychic Paper
Quantum Misalignment
Reliquary Tower
Return the Past
River Song
River Song's Diary
Rockfall Vale
Rogue's Passage
Rootbound Crag
Ryan Sinclair
Search for Tomorrow
Sheltered Thicket
Sisterhood of Karn
Sol Ring
Sonic Screwdriver
Start the TARDIS
Stormcarved Coast
Strax, Sontaran Nurse
Surge of Brilliance
Talisman of Curiosity
Talisman of Impulse
TARDIS
Temple of Abandon
Temple of Epiphany
Temple of Mystery
Temple of the False God
The Flux
The Foretold Soldier
The Fugitive Doctor
The Twelfth Doctor
Thijarian Witness
Think Twice
Throes of Chaos
Truth or Consequences
Twice Upon a Time // Unlikely Meeting
Vineglimmer Snarl
Waterlogged Grove
Wreck and Rebuild
The Thirteenth Doctor · Foil
Yasmin Khan · Foil"""

deadly_disguise = """Ainok Survivalist
Akroma, Angel of Fury
Arcane Signet
Ashcloud Phoenix
Austere Command
Beast Whisperer
Boltbender
Boros Garrison
Branch of Vitu-Ghazi
Broodhatch Nantuko
Canopy Vista
Chaos Warp
Cinder Glade
Command Tower
Deathmist Raptor
Decimate
Den Protector
Dusk/Dawn
Duskana, the Rage Mother
Exalted Angel
Exotic Orchard
Experiment Twelve
Fell the Mighty
Fortified Village
Furycalm Snarl
Game Trail
Gruul Turf
Hidden Dragonslayer
Hooded Hydra
Imperial Hellkite
Jeska's Will
Jungle Shrine
Kessig Wolf Run
Krosan Cloudscraper
Krosan Colossus
Krosan Verge
Lifecrafter's Bestiary
Master of Pearls
Mastery of the Unseen
Mirror Entity
Mossfire Valley
Mosswort Bridge
Nantuko Vigilante
Nature's Lore
Neheb, the Eternal
Nervous Gardener
Obscuring Aether
Ohran Frostfang
Panoptic Projektor
Path to Exile
Printlifter Ooze
Ransom Note
Return of the Wildspeaker
Root Elemental
Sacred Peaks
Sakura-Tribe Elder
Salt Road Ambushers
Saryth, the Viper's Fang
Scattered Groves
Scourge of the Throne
Scroll of Fate
Seedborn Muse
Selesnya Sanctuary
Sheltered Thicket
Showstopping Surprise
Shrine of the Forsaken Gods
Sidar Kondo of Jamuraa
Sol Ring
Sungrass Prairie
Temple of Abandon
Temple of Plenty
Temple of the False God
Temple of Triumph
Temur War Shaman
Tesak, Judith's Hellhound
Thelonite Hermit
Three Visits
Toski, Bearer of Secrets
Trail of Mystery
True Identity
Ugin's Mastery
Unexplained Absence
Veiled Ascension
Welcoming Vampire
Whisperwood Elemental
Wild Growth
Yedora, Grave Gardener
Zoetic Cavern
Kaust, Eyes of the Glade · Foil"""

blame_game = """Access Tunnel
Agitator Ant
Ancient Stone Idol
Angel of the Ruins
Anya, Merciless Angel
Arcane Signet
Ash Barrens
Bloodthirsty Blade
Boros Garrison
Boros Reckoner
Brash Taunter
Castle Ardenvale
Comeuppance
Command Tower
Curse of Opulence
Darien, King of Kjeldor
Deflecting Palm
Disrupt Decorum
Duelist's Heritage
Elspeth, Sun's Champion
Escape Tunnel
Etali, Primal Storm
Exotic Orchard
Feather, Radiant Arbiter
Fellwar Stone
Fiendish Duo
Frontier Warmonger
Furycalm Snarl
Ghostly Prison
Gideon's Sacrifice
Gisela, Blade of Goldnight
Havoc Eater
Hot Pursuit
Immortal Obligation
Kazuul, Tyrant of the Cliffs
Keeper of the Accord
Kher Keep
Labyrinth of Skophos
Loran of the Third Path
Martial Impetus
Mind Stone
Mob Verdict
Myriad Landscape
Needle Spires
Orzhov Advokist
Otherworldly Escort
Prisoner's Dilemma
Promise of Loyalty
Ransom Note
Redemption Arc
Reliquary Tower
Rite of the Raging Storm
Rogue's Passage
Scavenger Grounds
Seal of Cleansing
Selfless Squire
Sevinne's Reclamation
Shiny Impetus
Slayers' Stronghold
Smuggler's Share
Sol Ring
Solemn Simulacrum
Soul Snare
Spectacular Showdown
Stalking Leonin
Steel Hellkite
Sun Titan
Sunhome, Fortress of the Legion
Take the Bait
Talisman of Conviction
Temple of the False God
Temple of Triumph
Thought Vessel
Throne of the High City
Tome of Legends
Trouble in Pairs
Vengeful Ancestor
Vow of Duty
Vow of Lightning
Wall of Omens
War Room
Windborn Muse
Winds of Rath
Nelly Borca, Impulsive Accuser · Foil"""

deep_clue_sea = """Academy Manufactor
Adrix and Nev, Twincasters
Aerial Extortionist
Alandra, Sky Dreamer
Arcane Signet
Armed with Proof
Azorius Chancery
Azorius Signet
Bennie Bracks, Zoologist
Canopy Vista
Chulane, Teller of Tales
Command Tower
Confirm Suspicions
Detective of the Month
Disorder in the Court
Erdwal Illuminator
Esix, Fractal Bloom
Ethereal Investigator
Exotic Orchard
Farewell
Finale of Revelation
Follow the Bodies
Fumigate
Graf Mole
Hornet Queen
Hydroid Krasis
Idol of Oblivion
Innocuous Researcher
Inspiring Statuary
Irrigated Farmland
Jolrael, Mwonvuli Recluse
Junk Winder
Kappa Cannoneer
Killer Service
Knowledge Is Power
Koma, Cosmos Serpent
Krosan Verge
Lonely Sandbar
Lonis, Cryptozoologist
Magnifying Glass
Mechanized Production
Merchant of Truth
Nadir Kraken
Nettlecyst
On the Trail
Ongoing Investigation
Organic Extinction
Path of Ancestry
Prairie Stream
Psychosis Crawler
Ransom Note
Reliquary Tower
Scattered Groves
Search the Premises
Seaside Citadel
Secluded Steppe
Selesnya Sanctuary
Selvala, Explorer Returned
Serene Sleuth
Shimmer Dragon
Simic Growth Chamber
Simic Signet
Skycloud Expanse
Sol Ring
Sophia, Dogged Detective
Spire of Industry
Sungrass Prairie
Swords to Plowshares
Talisman of Curiosity
Talisman of Progress
Talisman of Unity
Tangletrove Kelp
Teferi's Ageless Insight
Temple of Enlightenment
Temple of Mystery
Temple of Plenty
Temple of the False God
Tezzeret, Betrayer of Flesh
Thought Monitor
Tireless Tracker
Tranquil Thicket
Ulvenwald Mysteries
Wavesifter
Whirler Rogue
Wilderness Reclamation
Morska, Undersea Sleuth · Foil"""

revenant_recon = """Amphin Mutineer
Animate Dead
Arcane Signet
Ash Barrens
Baleful Strix
Black Sun's Zenith
Bojuka Bog
Brainstorm
Case of the Shifting Visage
Charnel Serenade
Choked Estuary
Command Tower
Connive/Concoct
Consider
Copy Catchers
Counterpoint
Curate
Darkwater Catacombs
Deep Analysis
Dimir Aqueduct
Dimir Signet
Dimir Spybug
Discovery/Dispersal
Disinformation Campaign
Dogged Detective
Doom Whisperer
Dream Eater
Drownyard Temple
Enhanced Surveillance
Ephara's Dispersal
Everflowing Chalice
Eye of Duskmantle
Fetid Pools
Final-Word Phantom
Foreboding Steamboat
Grave Titan
Hostile Desert
Lazav, the Multifarious
Marvo, Deep Operative
Massacre Wurm
Master of Death
Mind Stone
Mission Briefing
Mulldrifter
Myriad Landscape
Mystic Sanctuary
Necromancy
Nightveil Sprite
Notion Rain
Otherworldly Gaze
Overseer of the Damned
Phyrexian Arena
Phyrexian Metamorph
Pile On
Port of Karfell
Price of Fame
Ransom Note
Ravenous Chupacabra
Reanimate
Reliquary Tower
Rise of the Dark Realms
River of Tears
Rogue's Passage
Shriekmaw
Sinister Starfish
Sol Ring
Sphinx of the Second Sun
Sunken Hollow
Syr Konrad, the Grim
Tainted Isle
Talisman of Dominance
Temple of the False God
Thought Vessel
Thoughtbound Phantasm
Tocasia's Dig Site
Toxic Deluge
Twilight Prophet
Unshakable Tail
Vizier of Many Faces
Watcher of Hours
Whispering Snitch
Mirko, Obsessive Theorist · Foil"""

corrupting_influence = """Arcane Signet
Beast Within
Bilious Skulldweller
Blight Mamba
Blightbelly Rat
Bojuka Bog
Cankerbloom
Canopy Vista
Caress of Phyrexia
Carrion Call
Chromatic Lantern
Command Tower
Commander's Sphere
Contagion Clasp
Contaminant Grafter
Culling Ritual
Cultivate
Evolution Sage
Exotic Orchard
Expand the Sphere
Feed the Infection
Fellwar Stone
Fortified Village
Fumigate
Geth's Summons
Ghostly Prison
Glissa's Retriever
Glistening Sphere
Golgari Signet
Grafted Exoskeleton
Grateful Apparition
Ichor Rats
Ichorclaw Myr
Infectious Inquiry
Karn's Bastion
Krosan Verge
Merciless Eviction
Moldervine Reclamation
Mortify
Mycosynth Fiend
Myr Convert
Myriad Landscape
Necroblossom Snarl
Night's Whisper
Norn's Annex
Norn's Choirmaster
Norn's Decree
Noxious Assault
Noxious Revival
Painful Truths
Path of Ancestry
Pestilent Syphoner
Phyresis Outbreak
Phyrexian Atlas
Phyrexian Rebirth
Phyrexian Swarmlord
Plague Myr
Plague Stinger
Putrefy
Sandsteppe Citadel
Scavenging Ooze
Shineshadow Snarl
Sol Ring
Sungrass Prairie
Swords to Plowshares
Tainted Field
Tainted Wood
Temple of Malady
Temple of Plenty
Temple of Silence
Trailblazer's Boots
Unnatural Restoration
Vat Emergence
Venomous Brutalizer
Viridian Corrupter
Vishgraz, the Doomhive
Vraska's Fall
Windborn Muse
Wurmquake
Ixhel, Scion of Atraxa · Foil"""

quick_draw = """Arcane Bombardment
Arcane Denial
Arcane Signet
Archmage Emeritus
Baral's Expertise
Big Score
Bloodthirsty Adversary
Cascade Bluffs
Chaos Warp
Command Tower
Crackling Spellslinger
Curse of the Swine
Cursed Mirror
Deep Analysis
Dig Through Time
Electrostatic Field
Elemental Eruption
Epic Experiment
Eris, Roar of the Storm (Extended Art)
Exotic Orchard
Expressive Iteration
Faithless Looting
Ferrous Lake
Finale of Promise
Finale of Revelation
Forger's Foundry
Frostboil Snarl
Galvanic Iteration
Goblin Electromancer
Guttersnipe
Haughty Djinn
Izzet Boilerworks
Izzet Signet
Kaza, Roil Chaser
Leyline Dowser
Lock and Load
Midnight Clock
Mizzix's Mastery
Murmuring Mystic
Niv-Mizzet, Parun
Octavia, Living Thesis
Opt
Ponder
Pongify
Preordain
Propaganda
Pteramander
Pyretic Charge
Radical Idea
Reliquary Tower
Rousing Refrain
Serum Visions
Shark Typhoon
Shivan Reef
Smoldering Stagecoach
Sol Ring
Storm-Kiln Artist
Sulfur Falls
Talrand, Sky Summoner
Temple of Epiphany
Temple of the False God
Tezzeret's Gambit
Think Twice
Third Path Iconoclast
Thunderclap Drake
Treasure Cruise
Vandalblast
Veyran, Voice of Duality
Volcanic Torrent
Windfall
Winged Boots
Young Pyromancer
Stella Lee, Wild Card (Borderless) · Foil"""

grand_larceny = """Access Tunnel
Arcane Heist
Arcane Signet
Baleful Mastery
Baleful Strix
Bladegriff Prototype
Brainstealer Dragon
Cazur, Ruthless Stalker
Chaos Wand
Cold-Eyed Selkie
Command Tower
Culling Ritual
Cunning Rhetoric
Curse of the Swine
Darkslick Shores
Darksteel Ingot
Darkwater Catacombs
Dazzling Sphinx
Diluvian Primordial
Dimir Aqueduct
Doc Aurlock, Grizzled Genius
Dream-Thief's Bandana
Drowned Catacomb
Edric, Spymaster of Trest
Exotic Orchard
Extract Brain
Fallen Shinobi
Feed the Swarm
Felix Five-Boots (Extended Art)
Fellwar Stone
Fetid Pools
Flooded Grove
Ghostly Pilferer
Gonti, Lord of Luxury
Heartless Conscription
Hinterland Harbor
Hostage Taker
Kodama's Reach
Llanowar Wastes
Mind's Dilation
Nashi, Moon Sage's Scion
Oblivion Sower
Ohran Frostfang
Opulent Palace
Orochi Soul-Reaver
Overflowing Basin
Plasm Capture
Predators' Hour
Prismatic Lens
Putrefy
Rampant Growth
Reliquary Tower
Sage of the Beyond
Savvy Trader
Shadowmage Infiltrator
Silent-Blade Oni
Silhana Ledgewalker
Siphon Insight
Slither Blade
Smirking Spelljacker
Sol Ring
Stolen Goods
Sunken Hollow
Temple of Deceit
Temple of Malady
Temple of Mystery
The Mimeoplasm
Thief of Sanity
Thieving Amalgam
Thieving Skydiver
Thieving Varmint
Three Visits
Tower Winder
Triton Shorestalker
Trygon Predator
Twilight Mire
Ukkima, Stalking Shadow
Underground River
Villainous Wealth
Viridescent Bog
Void Attendant
Whirler Rogue
Woodland Cemetery
Yavimaya Coast
Gonti, Canny Acquisitor (Borderless) · Foil"""


most_wanted = """Academy Manufactor
Aetherborn Marauder
Angelic Sell-Sword
Angrath's Marauders
Arcane Signet
Back in Town
Bandit's Haul
Battlefield Forge
Blackcleave Cliffs
Bojuka Bog
Bonders' Enclave
Boros Charm
Bounty Board
Breena, the Demagogue
Canyon Slough
Captain Lannery Storm
Captivating Crew
Caves of Koilos
Changeling Outcast
Charred Graverobber
Clifftop Retreat
Command Beacon
Command Tower
Council's Judgment
Curtains' Call
Dead Before Sunrise
Deadly Dispute
Demolition Field
Desolate Mire
Dire Fleet Daredevil
Dire Fleet Ravager
Discreet Retreat
Dragonskull Summit
Exotic Orchard
Fain, the Broker
Feed the Swarm
Fetid Heath
Glittering Stockpile
Graywater's Fixer
Grenzo, Havoc Raiser
Heliod's Intervention
Hex
Humble Defector
Idol of Oblivion
Impulsive Pilferer
Isolated Chapel
Kamber, the Plunderer
Laurine, the Diversion
Life Insurance
Lightning Greaves
Mari, the Killing Quill
Marshland Bloodcaster
Mass Mutiny
Massacre Girl
Mirror Entity
Misfortune Teller
Mistmeadow Skulk
Morbid Opportunist
Nighthawk Scavenger
Nomad Outpost
Ogre Slumlord
Orzhov Signet
Painful Truths
Path of Ancestry
Queen Marchesa
Rain of Riches
Rakdos Signet
Rankle, Master of Pranks
Requisition Raid
Rogue's Passage
Rugged Prairie
Seize the Spotlight
Shadowblood Ridge
Shiny Impetus
Shoot the Sheriff
Smoldering Marsh
Sol Ring
Sulfurous Springs
Sunhome, Fortress of the Legion
Tainted Peak
Temple of Malice
Temple of Silence
Temple of the False God
Temple of Triumph
Tenured Inkcaster
Trailblazer's Boots
Vault of the Archangel
Veinwitch Coven
Vihaan, Goldwaker (Extended Art)
We Ride at Dawn
Witch of the Moors
Olivia, Opulent Outlaw (Borderless) · Foil"""

desert_bloom = """Abraded Bluffs
Ancient Greenwarden
Angel of Indemnity
Angel of the Ruins
Arcane Signet
Avenger of Zendikar
Bitter Reunion
Bovine Intervention
Bristling Backwoods
Cactus Preserve
Cataclysmic Prospecting
Chromatic Lantern
Command Tower
Conduit Pylons
Crawling Sensation
Creosote Heath
Decimate
Descend upon the Sinful
Desert of the Fervent
Desert of the Indomitable
Desert of the True
Dune Chanter
Dunes of the Dead
Eccentric Farmer
Electric Revelation
Elvish Rejuvenator
Embrace the Unknown
Escape to the Wilds
Evolving Wilds
Explore
Genesis Hydra
Harrow
Hashep Oasis
Hazezon, Shaper of Sand
Heaven // Earth
Hour of Promise
Jungle Shrine
Kirri, Talented Sprout (Extended Art)
Krosan Verge
Magmatic Insight
Map the Frontier
Marshal's Anthem
Mirage Mesa
Nantuko Cultivator
Nesting Dragon
Omnath, Locus of Rage
Oracle of Mul Daya
Painted Bluffs
Path to Exile
Perennial Behemoth
Perpetual Timepiece
Ramunap Excavator
Ramunap Ruins
Requisition Raid
Return of the Wildspeaker
Rumbleweed
Sand Scout
Satyr Wayfinder
Scaretiller
Scattered Groves
Scavenger Grounds
Scute Swarm
Sevinne's Reclamation
Shefet Dunes
Sheltered Thicket
Skullwinder
Sol Ring
Springbloom Druid
Sun Titan
Sunscorched Divide
Swiftfoot Boots
Terramorphic Expanse
The Mending of Dominaria
Thrilling Discovery
Titania, Protector of Argoth
Turntimber Sower
Unholy Heat
Valorous Stance
Vengeful Regrowth
Winding Way
World Shaper
Wreck and Rebuild
Yuma, Proud Protector (Borderless) · Foil"""

token_triumph = """Ajani, Caller of the Pride
Arcane Signet
Aura Mutation
Avacyn's Pilgrim
Blossoming Sands
Camaraderie
Canopy Vista
Champion of Lambholt
Citanul Hierophants
Citywide Bust
Collective Blessing
Collective Unconscious
Command Tower
Commander's Insignia
Commander's Sphere
Conclave Tribunal
Curse of Bounty
Dauntless Escort
Dawn of Hope
Devouring Light
Dictate of Heliod
Elfhame Palace
Eternal Witness
Farhaven Elf
Felidar Retreat
Fortified Village
Graypelt Refuge
Great Oak Guardian
Harmonize
Harvest Season
Holdout Settlement
Hornet Nest
Hornet Queen
Hour of Reckoning
Idol of Oblivion
Jade Mage
Jaspera Sentinel
Karametra's Favor
Leafkin Druid
Loyal Guardian
Maja, Bretagard Protector
March of the Multitudes
Mentor of the Meek
Nissa's Expedition
Nullmage Shepherd
Overrun
Overwhelming Instinct
Path to Exile
Presence of Gond
Reclamation Sage
Rishkar, Peema Renegade
Rootborn Defenses
Scatter the Seeds
Scavenging Ooze
Selesnya Evangel
Selesnya Guildmage
Slate of Ancestry
Sol Ring
Sporemound
Sylvan Reclamation
Talisman of Unity
Temple of Plenty
Thunderfoot Baloth
Tranquil Expanse
Trostani Discordant
Valor in Akros
Verdant Force
Vitu-Ghazi, the City-Tree
Voice of Many
White Sun's Zenith
Emmara, Soul of the Accord · Etched"""

#https://www.mtgmate.com.au/buylist/magic_sets/moc
growing_threat = """Ambition's Cost
Ancient Stone Idol
Angel of the Ruins
Arcane Signet
Bitterthorn, Nissa's Animus
Blade Splicer
Blight Titan
Bloodline Pretender
Bojuka Bog
Bone Shredder
Burnished Hart
Cataclysmic Gearhulk
Command Tower
Commander's Sphere
Compleated Huntmaster
Coveted Jewel
Darksteel Splicer
Despark
Duplicant
Evolving Wilds
Excise the Imperfect
Exotic Orchard
Fetid Heath
Filigree Vector
First-Sphere Gargantua
Fractured Powerstone
Go for the Throat
Goldmire Bridge
Graveshifter
Hedron Archive
Ichor Elixir
Karn's Bastion
Keskit, the Flesh Sculptor
Massacre Wurm
Master Splicer
Meteor Golem
Mind Stone
Moira and Teshar
Mortify
Myr Battlesphere
Nettlecyst
Night's Whisper
Noxious Gearhulk
Orzhov Locket
Orzhov Signet
Path of Ancestry
Path of the Schemer
Phyrexian Delver
Phyrexian Gargantua
Phyrexian Ghoul
Phyrexian Rager
Phyrexian Rebirth
Phyrexian Scriptures
Phyrexian Triniform
Psychosis Crawler
Scrap Trawler
Sculpting Steel
Scytheclaw
Shattered Angel
Shimmer Myr
Shineshadow Snarl
Silverquill Campus
Sol Ring
Soul of New Phyrexia
Spire of Industry
Swords to Plowshares
Tainted Field
Talisman of Hierarchy
Temple of Silence
Terramorphic Expanse
Utter End
Vault of the Archangel
Victimize
Vulpine Harvester
Wayfarer's Bauble
Yawgmoth's Vile Offering
Brimaz, Blight of Oreskos · Foil"""

#https://www.mtgmate.com.au/buylist/magic_sets/clb
mind_flayarrrs = """Aboleth Spawn
Arcane Signet
Ash Barrens
Black Market
Brainstealer Dragon
Chasm Skulker
Choked Estuary
Command Tower
Consuming Aberration
Creeping Tar Pit
Crippling Fear
Curtains' Call
Dark Hatchling
Darkwater Catacombs
Dauthi Horror
Dimir Aqueduct
Dimir Keyrune
Dimir Signet
Dross Harvester
Drown in the Loch
Drownyard Temple
Dusk Mangler
Endless Evil
Everflowing Chalice
Exotic Orchard
Extract from Darkness
Fact or Fiction
Feed the Swarm
Forgotten Creation
Fractured Sanity
From the Catacombs
Grazilaxx, Illithid Scholar
Grell Philosopher
Guiltfeeder
Haunted One
Herald's Horn
Hex
Hullbreaker Horror
Hunted Horror
In Garruk's Wake
Leyline of Anticipation
Lightning Greaves
Memory Plunder
Mind Flayer
Mind Stone
Mindcrank
Myriad Landscape
Nemesis of Reason
Nephalia Drownyard
Nighthowler
Nihilith
Overcharged Amalgam
Path of Ancestry
Phyrexian Rager
Phyrexian Revoker
Plague Spitter
Port of Karfell
Psionic Ritual
Psychosis Crawler
Pull from Tomorrow
Ravenous Chupacabra
Reflections of Littjara
River of Tears
Rogue's Passage
Sewer Nemesis
Sludge Monster
Sol Ring
Spellskite
Sunken Hollow
Syphon Mind
Tainted Isle
Talisman of Dominance
Temple of Deceit
Temple of the False God
Thought Vessel
Uchuulon
Wharf Infiltrator
Woe Strider
Zellix, Sanity Flayer
Captain N'ghathrod"""

#https://www.mtgmate.com.au/buylist/magic_sets/cmm
planeswalker_party = """Ajani Steadfast
Arcane Signet
Azorius Signet
Blasphemous Act
Boros Signet
Cartographer's Hawk
Cascade Bluffs
Chandra, Awakened Inferno
Chandra, Legacy of Fire
Chandra, Torch of Defiance
Command Tower
Deepglow Skate
Deploy the Gatewatch
Elspeth, Sun's Champion
Exotic Orchard
Fellwar Stone
Flux Channeler
Fog Bank
Forge of Heroes
Frostboil Snarl
Furycalm Snarl
Gatewatch Beacon
Gideon Jura
Grateful Apparition
Guff Rewrites History
Honor-Worn Shaku
Interplanar Beacon
Izzet Signet
Jace Beleren
Jace, Architect of Thought
Jace, Mirror Mage
Jaya's Phoenix
Karn's Bastion
Kazuul, Tyrant of the Cliffs
Leori, Sparktouched Hunter
Mangara, the Diplomat
Mobilized District
Myriad Landscape
Mystic Gate
Mystic Monastery
Nahiri, the Harbinger
Narset of the Ancient Way
Narset, Enlightened Master
Narset, Parter of Veils
Nevinyrral's Disk
Norn's Annex
Oath of Gideon
Oath of Jace
Oath of Teferi
Onakke Oathkeeper
Oreskos Explorer
Path to Exile
Port Town
Prairie Stream
Promise of Loyalty
Reliquary Tower
Repeated Reverberation
Rugged Prairie
Saheeli, Sublime Artificer
Sarkhan the Masterless
Semester's End
Silent Arbiter
Skycloud Expanse
Sol Ring
Spark Double
Sparkshaper Visionary
Swords to Plowshares
Talisman of Conviction
Talisman of Creativity
Talisman of Progress
Temple of Enlightenment
Temple of Epiphany
Temple of Triumph
Teyo, Geometric Tactician
The Chain Veil
The Wanderer
Thrummingbird
Urza's Ruinous Blast
Vronos, Masked Inquisitor
Wall of Denial
Wayfarer's Bauble
Commodore Guff · Foil"""

#require that all precons are in the same mtgmate link
thesePrecons = [planeswalker_party] #change it based on the variable name above (or add your own)
theyWouldPay = 0

for thisPrecon in thesePrecons:
    thisPreconList = thisPrecon.split("\n")

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


