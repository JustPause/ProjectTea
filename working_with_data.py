from dataBaseConnector import Database
from getDataFormJson import teaList
from main import db

def insert_data_funcion(tea):
    existing_tea = Database.check_for_duplicates_tea(tea["name"])
    
    if existing_tea == 0:
        Database.add_tea(name=tea["name"], tea_group=tea["type"], link=tea["link"])

def insert_data():

    # Database.drop_tea_table()
    # Database.drop_comment_table()
    # Database.drop_recipe_table()
    
    Green, Black, White=teaList()
        
    for tea in Green:
        insert_data_funcion(tea)
        
    for tea in Black:
        insert_data_funcion(tea)
        
    for tea in White:
        insert_data_funcion(tea)
    
    # tea1 = Database.add_tea(name="Earl Grey2", tea_group=1, link="http://example.com/earlgrey2")
    # tea2 = Database.add_tea(name="Matcha", tea_group=2, link="http://example.com/matcha")
    # tea3 = Database.add_tea(name="Chamomile", tea_group=3, link="http://example.com/chamomile")
    # tea4 = Database.add_tea(name="Oolong", tea_group=1, link="http://example.com/oolong")
    # tea5 = Database.add_tea(name="Jasmine Green", tea_group=2, link="http://example.com/jasminegreen")
    # tea6 = Database.add_tea(name="Peach Iced Tea", tea_group=1, link="http://example.com/peachicedtea")
    # tea7 = Database.add_tea(name="Sencha", tea_group=2, link="http://example.com/sencha")
    # tea8 = Database.add_tea(name="Peppermint", tea_group=3, link="http://example.com/peppermint")
    # tea9 = Database.add_tea(name="Blackberry Tea", tea_group=1, link="http://example.com/blackberrytea")
    # tea10 = Database.add_tea(name="Lemon Balm", tea_group=3, link="http://example.com/lemonbalm")
    
    # comment1 = Database.add_comment(tea_id=tea1.id, text="Great taste, very aromatic!")
    # comment2 = Database.add_comment(tea_id=tea2.id, text="I love the earthy notes in Matcha.")
    # comment3 = Database.add_comment(tea_id=tea3.id, text="Chamomile is so calming and relaxing.")
    # comment4 = Database.add_comment(tea_id=tea4.id, text="Oolong is perfect for afternoon tea!")
    # comment5 = Database.add_comment(tea_id=tea5.id, text="Jasmine Green Tea is my favorite!")
    # comment6 = Database.add_comment(tea_id=tea6.id, text="Peach Iced Tea is refreshing during summer.")
    # comment7 = Database.add_comment(tea_id=tea7.id, text="Sencha has a nice grassy flavor.")
    # comment8 = Database.add_comment(tea_id=tea8.id, text="Peppermint tea is soothing for my stomach.")
    # comment9 = Database.add_comment(tea_id=tea9.id, text="Blackberry Tea tastes sweet and fruity.")
    # comment10 = Database.add_comment(tea_id=tea10.id, text="Lemon Balm tea is great before bed.")
    
    # recipe1 = Database.add_recipe(tea_id=tea1.id, instructions="Steep in hot water at 90°C for 3-5 minutes.")
    # recipe2 = Database.add_recipe(tea_id=tea2.id, instructions="Whisk in hot water at 70°C for 1-2 minutes.")
    # recipe3 = Database.add_recipe(tea_id=tea3.id, instructions="Steep in hot water at 95°C for 4-6 minutes.")
    # recipe4 = Database.add_recipe(tea_id=tea4.id, instructions="Steep in hot water at 90°C for 5 minutes.")
    # recipe5 = Database.add_recipe(tea_id=tea5.id, instructions="Steep in hot water at 85°C for 3-4 minutes.")
    # recipe6 = Database.add_recipe(tea_id=tea6.id, instructions="Steep in cold water for 5-6 hours for a refreshing iced tea.")
    # recipe7 = Database.add_recipe(tea_id=tea7.id, instructions="Steep in hot water at 80°C for 2-3 minutes.")
    # recipe8 = Database.add_recipe(tea_id=tea8.id, instructions="Steep in hot water at 100°C for 3-5 minutes.")
    # recipe9 = Database.add_recipe(tea_id=tea9.id, instructions="Steep in hot water at 90°C for 4-5 minutes.")
    # recipe10 = Database.add_recipe(tea_id=tea10.id, instructions="Steep in hot water at 95°C for 3-5 minutes.")
    
def get_search_data():
    teaList=[]
    for row in Database.get_all_teas():
        teaList.append(row.name)

    return teaList