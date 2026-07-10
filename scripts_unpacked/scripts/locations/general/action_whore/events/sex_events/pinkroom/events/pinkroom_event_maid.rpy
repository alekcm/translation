init python:
    def pinkroom_work_dress_pick():
        pinkroom_clothes_list = []
        if wardrobe.qty(item_outfit_6):
            pinkroom_clothes_list.append("pub")
        
        
        if wardrobe.qty(item_outfit_20):
            pinkroom_clothes_list.append("maid")
        pinkroom_clothes_pick = renpy.random.choice(pinkroom_clothes_list)
        pc_striptease()
        renpy.pause(0.5) 
        if pinkroom_clothes_pick == "pub":
            pub_waitress.work_dress(slow=True)  
        
        
        elif pinkroom_clothes_pick == "maid":
            maid_outfit_set()
            pc_dress_slow(outfit="work")

label pinkroom_customer_event_maid:
    $ player.face_happy()
    pc "[rlist.pinkroom_welcome_group]"
    tempname.name "Hey darling, we got some booze and looking for a good time. Mind serving for us?"
    pc "Sure, no problem."
    $ inv.take(item_pinkticket, 3)
    tempname.name "Dress up in something nice would ya?"
    pc "Sure."
    $ pinkroom_work_dress_pick()
    pc "How's this?"
    tempname.name "Perfect!"
    pc "So what we drinking?"
    $ player.left_hand  = "beer"
    $ player.right_hand = "beer"
    "I take some beers out of the box they brought, pour them into glasses and start serving them to the guys."
    $ player.hands_reset()
    pc "Here ya go lads."
    "The guys hang around in my room drinking and talking amongst themselves. Seems doing this is a common thing for them."
    $ relax(5)
    "Sometimes they include me in the conversation and offer me drinks, but mostly I just top up their glasses while being groped or spanked."
    $ player.beer()
    $ player.grope(strip=True)
    "Of course as time passes, I am starting to lose my clothes..."
    $ relax(10)
    $ player.grope_end()
    "That doesn't stop me though, I still serve them drinks."
    $ player.left_hand  = "beer"
    $ player.right_hand = "beer"
    pc "Here you go."
    $ player.hands_reset()
    $ player.add_perk(perk_drinking_beer_2)
    $ relax(5)
    $ player.spank()
    "They carry on talking among themselves, they are drinking pretty quickly and it's clear they are looking to get pretty drunk."
    $ player.grope(strip=True)
    "It's not even been that long and they are already pretty drunk. They are drinking a lot faster than I would expect people to."
    $ player.grope_end()
    $ relax(10)
    $ player.left_hand  = "beer"
    $ player.right_hand = "beer"
    $ player.face_happy()
    pc "More drinks?"
    $ player.hands_reset()
    $ player.add_perk(perk_drinking_beer_2)
    $ player.grope(strip=True)
    tempname.name "Cheers love."
    $ player.grope_end()
    tempname.name "Keep 'em coming."
    $ player.spank()
    $ relax(15)
    $ player.add_perk(perk_drinking_beer_2)
    "I keep serving them and I keep getting groped. But as far as customers go, this is more enjoyable than most."
    $ player.grope(strip=True)
    "They are getting a bit rowdy and looks like they are all having a good time."
    $ player.grope(strip=True)
    $ relax(15)
    "Drinks keep flowing and the guys talk all manner of silliness with each other."
    $ player.add_perk(perk_drinking_beer_2)
    $ player.grope_end()
    "Looks like things are starting to calm down now. They are talking about what they should do next."
    if t.hour in (18,19,20,21,22):
        tempname.name "Cheers love. Thanks for the service."
        pc "Heading off now?"
        tempname.name "Yeah, going to see if some other party is going on."
        pc "Have fun."
        "I see the guys out the door."
        $ pc_set_temp_outfit()
        $ player.drink_finish()
        jump travel
    elif t.hour in (17, 23, 0, 1):
        pc "Heading off now?"
        tempname.name "This lot are, I think I'll stay and have some fun."
        pc "Okay, see you guys."
        tempname.name "Looking at you all this time serving us was making me excited."
        pc "Mmm."
        $ player.drink_finish()
        jump whore_bed_sex_start
    else:
        tempname.name "So, how about we get this party really started?"
        pc "Oh? What did you have in mind?"
        tempname.name "Plenty of us, and one of you. I think you can imagine."
        pc "Oh? Okay. You got the tickets for that?"
        $ player.sex_man_amount = numgen(3,6)
        $ inv.take(item_pinkticket, player.sex_man_amount)
        tempname.name "Sure, here you go."
        pc "Okay."
        $ player.drink_finish()
        hide male_generic
        jump whore_street_sex_group_start_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
