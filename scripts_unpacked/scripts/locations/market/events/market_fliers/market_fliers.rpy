init python:
    def work_fliers(): 
        tamount = 60 
        
        baseallure = player.allure - 40 
        timeallure = tamount / 15 * baseallure / 20
        if timeallure < 0:
            randomnum = renpy.random.randint(1, 10)
            ttime = tamount + randomnum
        else:
            ttime = int(tamount - timeallure)
        
        hunger = tamount / 15
        allure = tamount / 15 * player.allure / 30
        
        if player.pregnancy == 2:
            tiredtotal = int(tamount / 15 * 2)
        elif player.pregnancy == 3:
            tiredtotal = int(tamount / 15 * 2.5)
        else:
            tiredtotal = int(tamount / 15 * 1.5)
        
        moodtotal = int(tamount / 8)
        
        t.minute = ttime
        
        player.inhib_degrade(tamount)
        player.add_hunger(hunger)
        player.add_tired(-tiredtotal)
        player.add_mood(-moodtotal)
        player.add_desire(allure)
        
        market_flyer.add_timesworked()



label park_local_market_flyer_intro:
    pc "Hey, so you asked me to speak to you for some work handing out flyers..."
    jaz "Yes of course. You ready to start now?"
    pc "Well, what do I need to do specifically?"
    jaz "Just walk around town handing these out to anyone you see. The more you give out the more I pay you."
    pc "Ok, sounds good."
    jaz "So, ready to start?"
    menu:
        "Yeah sure.":
            $ market_flyer.active = 1
            $ market_flyer.stage = 1
            jump park_local_market_flyer
        "Not right now.":

            jaz "Ok, well come see me when you are ready."
            pc "Will do."
            $ market_flyer.active = 1
            $ market_flyer.stage = 1
            jump travel

label park_local_market_flyer:
    "I take a bunch of flyers off the desk and prepare to head off to hand them out."
    pc "Hmm, where to today?"
    $ randomnum = renpy.random.randint(1, 5)
    $ walk(renpy.random.choice([loc_park, loc_revel, loc_residential, loc_revel_backstreet]))
    "I head off somewhere busy to hand out fliers"
    $ player.face_happy()
    $ dialouge = renpy.random.choice([
    "Shop at the market. Great prices and friendly service.",
    "Here you go. Support local businesses.",
    "The market has everything you need all in one location and all prices are negotiable.",
    "Why shop in the stuffy mall when you can get your good in the fresh air.",
    "Everything you need in one place and service with a smile.",
    "Special discounts today only at the market.",
    "Clothes, makeup and household goods all at great prices.",
    "The largest bookstore around at the market. New and second hand all at great prices.",
    "Free book exchange for all students at market."
    ])
    pc "[dialouge]"
    "I start handing out the last of my flyers."
    $ working(60)
    pc "Thats the last of them, I should head back."
    $ walk(loc_market)
    jaz "Good work [fname]. Here is your pay. Come back if you want to hand out more."
    $ player.add_money(market_flyer.reward)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
