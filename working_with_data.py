from dataBaseConnector import Database
from getDataFormJson import teaList
from main import db
import random

i = 0

def insert_data_funcion(tea):
    existing_tea = Database.check_for_duplicates_tea(tea["name"])
    
    if existing_tea == 0:
        return Database.add_tea(name=tea["name"], tea_group=tea["type"], link=tea["link"])
    else:
        return -1

def insert_comment(tea_name, text):
    id = Database.get_id_for_tea_name(tea_name)
    userName = "Anonymous"
    location = "No whare"
    print(id, text, userName, location)
    Database.add_comment(tea_id=id, text=text, userName=userName, location=location)

def insert_comment_funcion(tea_id):
    
    if Database.get_comments_count_with_tea_id(tea_id) < 5:
        data=random_comments(tea_id)
        Database.add_comment(tea_id=data[3], text=data[0], userName=data[1], location=data[2])

def random_comments(tea_id):
    randomComment = ["A delicate green tea with a smooth flavor."
                    ,"Perfect for relaxation after a long day."
                    ,"An excellent tea for pairing with light snacks."
                    ,"An Ju Bai Cha has a sweet, mellow taste."
                    ,"Great for beginners in the world of green tea."

                    ,"Bancha is a classic Japanese green tea."
                    ,"Mild and refreshing with a light grassy taste."
                    ,"Perfect for sipping throughout the day."
                    ,"A traditional tea that pairs well with Japanese cuisine."
                    ,"A good tea for those who prefer a less grassy flavor."

                    ,"A fragrant tea with a fresh, floral aroma."
                    ,"Bi Luo Chun has a delicate and sweet taste."
                    ,"One of the top Chinese green teas, very popular."
                    ,"The tea leaves are beautifully curled, making it a visual treat."
                    ,"Great for those who enjoy a fresh, sweet green tea."

                    ,"Dragon Well is one of China's most famous green teas."
                    ,"A smooth and slightly nutty flavor."
                    ,"It has a wonderful vegetal taste with a sweet aftertaste."
                    ,"Dragon Well is perfect for daily tea drinkers."
                    ,"One of the best green teas you can find from China."

                    ,"A rare and high-quality green tea from En Shi."
                    ,"Has a refreshing, light taste with floral notes."
                    ,"En Shi Yu Lu is known for its delicate taste and smooth finish."
                    ,"A perfect tea for those who like mild green teas."
                    ,"Great for brewing multiple times, each infusion brings new flavors."

                    ,"Rich in antioxidants due to its high zinc and selenium content."
                    ,"A mild green tea with a unique, earthy taste."
                    ,"Known for its health benefits, especially for skin health."
                    ,"The taste is subtle but refreshing."
                    ,"A good choice for those who enjoy a soft, mineral flavor."

                    ,"A unique green tea combined with roasted rice."
                    ,"The roasted rice adds a toasty, nutty flavor."
                    ,"Genmaicha is soothing and perfect for cold weather."
                    ,"A comforting, balanced flavor that isn’t too strong."
                    ,"Great for pairing with a variety of meals."

                    ,"A high-quality Japanese green tea with an umami-rich taste."
                    ,"Gyokuro is sweet and has a deep, rich flavor."
                    ,"Great for tea connoisseurs looking for a unique experience."
                    ,"Perfect for those who enjoy a savory green tea."
                    ,"This tea offers a sweet and vegetal taste that's very distinct."

                    ,"A famous tea from the Huangshan region in China."
                    ,"A delicate and floral tea with a smooth finish."
                    ,"Has a mild, sweet flavor with a light grassy note."
                    ,"Great for those who enjoy a balanced green tea."
                    ,"Huang Shan Mao Feng is perfect for afternoon tea."

                    ,"A roasted green tea that has a warm, comforting flavor."
                    ,"Hōjicha has a rich, toasty flavor that is less grassy."
                    ,"A great tea for evening relaxation."
                    ,"Its roasted taste makes it unique compared to other green teas."
                    ,"Hōjicha has a calming, mellow taste that’s perfect after meals."

                    ,"Fragrant jasmine blossoms enhance the green tea’s flavor."
                    ,"A perfect blend of floral and grassy notes."
                    ,"Ideal for relaxing moments, with a sweet aroma."
                    ,"A classic, refreshing green tea."
                    ,"Great for anyone who loves floral tea blends."

                    ,"Made from the stems and leaves of the tea plant."
                    ,"Kukicha has a unique, light, and nutty flavor."
                    ,"A smooth, sweet taste that's great for beginners."
                    ,"A very soothing tea that's perfect for any time of day."
                    ,"Kukicha is a gentle green tea with a light taste."

                    ,"Also known as Dragon Well, it’s a highly revered green tea."
                    ,"Lung Ching has a deep, rich flavor with a slightly nutty aftertaste."
                    ,"A fragrant, fresh tea with a vegetal flavor."
                    ,"Great for people who prefer a clean, natural green tea."
                    ,"One of the best teas for both beginners and experts."

                    ,"The most famous powdered green tea from Japan."
                    ,"Matcha has a bold, rich flavor with a creamy finish."
                    ,"Perfect for traditional Japanese tea ceremonies."
                    ,"Great for adding to smoothies or desserts."
                    ,"Matcha has a unique, vibrant green color and a strong taste."

                    ,"A sweet, floral tea with a smooth and refreshing taste."
                    ,"Meng Ding Gan Lu is light and mellow, perfect for everyday drinking."
                    ,"A great tea for new green tea drinkers."
                    ,"Has a rich, sweet aftertaste that lingers."
                    ,"This tea is gentle, with a light, fresh flavor."

                    ,"A blend of strong black tea with fragrant jasmine."
                    ,"The floral jasmine aroma complements the boldness of black tea."
                    ,"Jasmine Black Tea is a great introduction to floral black teas."
                    ,"Rich in flavor and soothing with a delicate floral finish."
                    ,"Ideal for those who enjoy fragrant, flavorful teas."

                    ,"A lighter, more delicate version of jasmine tea."
                    ,"The subtle jasmine fragrance enhances the smooth white tea."
                    ,"A calming, refreshing drink that's perfect for tea lovers."
                    ,"Jasmine White Tea has a delicate and aromatic profile."
                    ,"Great for when you want something gentle and floral."

                    ,"A bold, malty black tea from India."
                    ,"Assam tea has a rich, full-bodied flavor."
                    ,"Great for breakfast or a strong afternoon tea."
                    ,"Pairs well with milk and sugar for a robust cup."
                    ,"Assam is a classic tea that is perfect for a strong brew."

                    ,"Ceylon tea is light and brisk with a citrusy flavor."
                    ,"A perfect afternoon tea with a smooth finish."
                    ,"It has a refreshing taste that’s great on its own or with milk."
                    ,"Ceylon is perfect for those who enjoy a crisp, clean black tea."
                    ,"A great tea for a revitalizing pick-me-up."

                    ,"Known as the 'Champagne of teas,' Darjeeling offers a delicate flavor."
                    ,"A light, floral tea with fruity notes."
                    ,"Darjeeling is perfect for tea connoisseurs who enjoy complex flavors."
                    ,"A sophisticated tea with a unique muscatel flavor."
                    ,"It has a floral aroma and a light, crisp finish."

                    ,"Dian Hong is a smooth, rich black tea from Yunnan, China."
                    ,"It has a sweet, malty flavor with hints of cocoa."
                    ,"Dian Hong offers a pleasant, mellow brew that's easy to drink."
                    ,"This tea has a beautifully rich color and flavor."
                    ,"A great black tea for those who enjoy a smoother brew."

                    ,"Ruby tea has a sweet, fruity flavor with a smooth finish."
                    ,"A rare tea from Taiwan with a distinct red color."
                    ,"Rich in flavor with subtle notes of honey and fruit."
                    ,"Great for those who prefer a smoother, less astringent black tea."
                    ,"Ruby tea is a special treat for tea lovers seeking something unique."

                    ,"A luxurious black tea with a sweet, malty flavor."
                    ,"Jin Jun Mei has a rich, full-bodied taste with hints of honey."
                    ,"A premium tea that's perfect for special occasions."
                    ,"It has a smooth, complex flavor profile."
                    ,"Jin Jun Mei offers a delicate, floral aroma."
                    ]
    randomNames = ["Dewdrop Emerald",
                    "Jade Blossom",
                    "Silver Springs",
                    "Mountain Mist",
                    "Morning Dew",
                    "Celestial Green",
                    "Whispering Bamboo",
                    "Golden Grove",
                    "Crystal Leaf",
                    "Frosted Willow",
                    "Verdant Bliss",
                    "Tranquil Leaf",
                    "Jade Dragon",
                    "Sunlit Meadow",
                    "Misty Hills",
                    "Moonlit Orchard",
                    "Pure Serenity",
                    "Lush Bamboo",
                    "Radiant Garden",
                    "Dewy Forest",
                    "Ancient Springs",
                    "Evergreen Delight",
                    "Zen Essence",
                    "Crystal Brook",
                    "Enchanted Meadow",
                    "Dragon’s Breath",
                    "Spring Veil",
                    "Peaceful Grove",
                    "Everlast Green",
                    "Twilight Green",
                    "Verdant Forest",
                    "Zen Garden",
                    "Lotus Leaf",
                    "Emerald Dew",
                    "Heavenly Green",
                    "Morning Breeze",
                    "Green Gold",
                    "Autumn Green",
                    "Sacred Dew",
                    "Whispering Pines",
                    "Crimson Majesty",
                    "Velvet Black",
                    "Dark Night",
                    "Royal Ceylon",
                    "Midnight Brew",
                    "Bold Essence",
                    "Sunset Brew",
                    "Dark Velvet",
                    "Imperial Gold",
                    "Golden Shadow",
                    "Majestic Assam",
                    "Black Thunder",
                    "Ruby Eclipse",
                    "Golden Amber",
                    "Royal Bliss",
                    "Dark Moon",
                    "Autumn Ember",
                    "Smoky Charm",
                    "Eclipse Delight",
                    "Dark Blossom",
                    "Midnight Ember",
                    "Ebony Dream",
                    "Wild Harvest",
                    "Shadow Rose",
                    "Steeped Essence",
                    "Velvet Night",
                    "Royal Harmony",
                    "Shadowed Gold",
                    "Spiced Essence",
                    "Silver Moon",
                    "Dark Mystique",
                    "Black Crest",
                    "Amber Kiss",
                    "Noble Earl",
                    "Royal Serenade",
                    "White Whisper",
                    "Silver Moonlight",
                    "Frosted Rose",
                    "Snow Blossom",
                    "Morning Dew White",
                    "Pure Serenity",
                    "Winter Bloom",
                    "Silver Frost",
                    "Crystal White",
                    "Vanilla Mist",
                    "White Velvet",
                    "Golden Orchid",
                    "Winter’s Kiss",
                    "Snowflake Essence",
                    "Bright Snow",
                    "Pearl Dew",
                    "Pure Blossom",
                    "Fresh Snowfall",
                    "Sweet Haze",
                    "White Diamond",
                    "Ice Blossom",
                    "Elegant Snow",
                    "Winter Breeze",
                    "Jasmine Snow",
                    "Silver Dawn",
                    "Crystal Veil",
                    "Radiant Snow",
                    "Glacial Essence",
                    "Snowy Embrace",
                    "Frosted Bliss",
                    "White Cloud",
                    "Snowfield White",
                    "Tranquil Pearl",
                    "Winter Jewel",
                    "White Moon",
                    "Ice Rose",
                    "Arctic Breeze",
                    "Frosted Pearl",
                    "Velvet Snow",
                    "Pure Horizon"]                   
    randomLocations = ["Silverstone", 
                    "Heights",
                    "Coral Bay City",
                    "Timberview Park",
                    "Crescent Harbor",
                    "Ambercliff",
                    "Solstice Harbor",
                    "Moonfall City",
                    "Riverstone Bay",
                    "Summit Ridge",
                    "Crystal Falls",
                    "Royal Grove",
                    "Sapphire Springs",
                    "Redwood Crossing",
                    "Windward City",
                    "Emerald Bay",
                    "Horizon Peaks",
                    "Ashfield Township",
                    "Starlight Quarter",
                    "Falcon's Reach",
                    "Maplewood",
                    "Beacon's Edge",
                    "Aurora Valley",
                    "Riverview Heights",
                    "Golden Gate District",
                    "Seabreeze Cove",
                    "Summit Gardens",
                    "Grandview Heights",
                    "Westbrook Plaza",
                    "Bayfield Heights",
                    "Morningstar City",
                    "Thunder Peak",
                    "Serpent’s Summit",
                    "Snowy Ridge",
                    "Silver Rock Mountain",
                    "Misty Hillside",
                    "Ravenstone Peak",
                    "Crystal Glacier",
                    "Northward Mountain",
                    "Suncrest Heights",
                    "Glacier’s Reach",
                    "Wintergate Summit",
                    "Pinecrest Peak",
                    "Storm Watch",
                    "Dark Hollow Ridge",
                    "Bearclaw Summit",
                    "Twilight Mountain",
                    "Frostfall Pass",
                    "Azure Summit",
                    "Dragon’s Wing Peak",
                    "Evergreen Spire",
                    "Highwind Bluff",
                    "Silverstone Crest",
                    "Cloudcrest Peak",
                    "Thundercliff Ridge",
                    "Eternal Snow Peak",
                    "Sandspire Dunes",
                    "Mirage Oasis",
                    "Sunblaze Desert",
                    "Golden Sands",
                    "Crimson Canyon",
                    "Oasis of Dreams",
                    "Dustfall Ridge",
                    "Shifting Sands",
                    "Starry Hollow",
                    "Solstice Sands",
                    "Sunfire Oasis",
                    "Silver Mirage",
                    "Cactus Grove",
                    "Windcarver Dunes",
                    "Ember Desert",
                    "Forgotten Canyon",
                    "Starlight Plateau",
                    "Heatwave Hollow",
                    "Serpent’s Mirage",
                    "Dunecrest Oasis",
                    "Crystal Mirage",
                    "Desert Sun Peaks",
                    "Sagebrush Flats",
                    "Desert Moon Bay",
                    "Canyon's End",
                    "Whispering Woods",
                    "Twilight Grove",
                    "Ravenwood Forest",
                    "Shadowleaf Glen",
                    "Moonlight Hollow",
                    "Sylvan Glade",
                    "Frostwind Forest",
                    "Deepwood Hollow",
                    "Ironbark Grove",
                    "Ashenwood Forest",
                    "Dreamweaver Grove",
                    "Fallenleaf Grove",
                    "Evergreen Hollow",
                    "Silverpine Forest",
                    "Mistwood Hollow",
                    "Wyrmwood Glade",
                    "Wildflower Forest",
                    "Hidden Glen",
                    "Redwood Realm",
                    "Thicketwood Hollow",
                    "Sagebrush Forest",
                    "Starlight Isle",
                    "Coral Shore",
                    "Crystal Isle",
                    "Moonrise Bay",
                    "Horizon Isle",
                    "Sapphire Lagoon",
                    "Emerald Archipelago",
                    "Solana Island",
                    "Driftwood Isle",
                    "Tempest Bay",
                    "Windward Isles",
                    "Mariner’s Island",
                    "Sunreef Isle",
                    "Seabound Isle"]
    
    i1= random.randrange(1,len(randomComment))
    i2= random.randrange(1,len(randomNames))
    i3= random.randrange(1,len(randomLocations))
    
    return [randomComment[i1], randomNames[i2], randomLocations[i3], tea_id]
    
def insert_data():
    
    # Database.drop_tea_table()
    # Database.drop_comment_table()
    # Database.drop_recipe_table()
    
    Green, Black, White=teaList()
    global i  
    for tea in Green:
        id=insert_data_funcion(tea)
        for value in range(5):
            insert_comment_funcion(id)
 
    for tea in Black:
        insert_data_funcion(tea)
        
    for tea in White:
        insert_data_funcion(tea)
        
def get_search_data():
    teaList=[]
    
    for teaName in Database.get_all_teas():
        teaName = {
            "tea_group": teaName.tea_group,
            "name": teaName.name
        }
        teaList.append(teaName)
        
    return teaList

def get_comments(tea_name):
    id = Database.get_id_for_tea_name(tea_name)
    comments_data = [
        {
            "id": comment.id,
            "text": comment.text,
            "location": comment.location,
            "userName": comment.userName,
            "tea_id": comment.tea_id
        }
        for comment in Database.get_comments_for_tea(id)
    ]
 
    return comments_data

def get_random_comment():
    # Get Comment count, how many commants thare is
    # Gen Random valid id
    # Get All Comments with id
    # Select random one
    
    count=Database.get_tea_count()
    rand_count=random.randint(1, count)
    data=Database.get_comments_with_tea_id(rand_count)
    rand_data_count=random.randint(1, len(data))-1
    comment=data[rand_data_count]
    
    comments_data = [
        {
            "id": comment.id,
            "teaName": Database.get_name_for_tea_id(comment.tea_id),
            "text": comment.text,
            "location": comment.location,
            "userName": comment.userName,
            "tea_id": comment.tea_id
        }
    ]
    return comments_data

def update_comment_with_tea_id(id,comment):
    Database.update_comment(id,comment)

# Makes a comment for tea
# adds comment to one sesific tea


#   BIG SPAGETI, SKANAUS SKAITYTOJUI
