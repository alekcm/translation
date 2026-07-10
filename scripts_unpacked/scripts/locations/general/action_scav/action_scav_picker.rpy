label scav_jump:
    if not loc_cur.can_scavenge:
        pcm "Nothing to be found round here."
        jump travel



    elif player.tired < 20:
        pcm "I am exhausted. Probably end up passing out on my feet if I keep looking around."
        jump travel
    elif loc_cur.scav_recent:
        pcm "I already looked around here recently. I should check elsewhere."
        jump travel
    elif loc_cur.home_location:
        pcm "No point in scavving my own stuff."
        jump travel
    elif renpy.has_label(loc_cur.name + "_scavenge"):
        jump expression loc_cur.name + "_scavenge"
    elif renpy.has_label(loc_cur.get_district().name + "_scavenge"):
        jump expression loc_cur.get_district().name + "_scavenge"
    else:
        jump loc_generic_scavenge

label dis_hospital_scavenge:
    $ dialouge = renpy.random.choice([
    "Digging around the hospital is just theft.",
    "Doubt they will be pleased if I start rifling through their cabinets.",
    "They aren't going to let me wander the hospital searching through their drawers.",
    ])
    pcm "[dialouge]"
    jump travel
label dis_pub_scavenge:
    $ dialouge = renpy.random.choice([
    "Can't just walk around stealing stuff from the pub.",
    "Can't just go taking stuff from the pub.",
    ])
    pcm "[dialouge]"
    jump travel

label dis_home_scavenge:
    pcm "No point searching around my own home."
    jump travel

label loc_junk_trailer_scavenge:
    if not robin.love > 80:
        pcm "I don't think [jaylee.name] would like me rummaging around her trailer."
    else:
        $ temp_var_1 = [item_bottom_32, item_top_40, item_pants_10]
        python:
            for i in temp_var_1:
                if not wardrobe.qty(i):
                    temp_var_2 = i
                else:
                    temp_var_2 = False
        if temp_var_2:
            pcm "Hopefully [jaylee.name] doesn't mind me borrowing something..."
            "I take a look around for a bit and find something nice to wear."
            $ working(10)
            $ wardrobe.take(temp_var_2, all_notif=True)
            if temp_var_2.type == "pants":
                pcm "I just stole a girls knickers from her bedroom..."
                pcm "Hope she doesn't get the wrong idea."
                pcm "Better wash them first."
        else:
            pcm "I don't think she has any clothes that I don't already have."
    jump travel

label loc_junk_trailer_bathroom_scavenge:
    pcm "No point in looking around [jaylee.name]'s shower..."
    jump travel

label loc_bedroom_robin_scavenge:
    if not robin.love > 80:
        pcm "I don't think [robin.name] would like me rummaging around her room."
    else:
        $ temp_var_1 = [item_bottom_16, item_top_23, item_coat_10]
        python:
            for i in temp_var_1:
                if not wardrobe.qty(i):
                    temp_var_2 = i
                else:
                    temp_var_2 = False
        if temp_var_2:
            pcm "Hopefully [robin.name] doesn't mind me borrowing something..."
            "I take a look around for a bit and find something nice to wear."
            $ working(10)
            $ wardrobe.take(temp_var_2, all_notif=True)
        else:

            pcm "I don't think she has any clothes that I don't already have."
    jump travel

label loc_bedroom_dani_scavenge:
    if not robin.love > 80:
        pcm "I don't think [dani.name] would like me rummaging around her room."
    else:
        $ temp_var_1 = [item_bottom_6, item_top_5, item_pants_2]
        python:
            for i in temp_var_1:
                if not wardrobe.qty(i):
                    temp_var_2 = i
                else:
                    temp_var_2 = False
        if temp_var_2:
            pcm "Hopefully [robin.name] doesn't mind me borrowing something..."
            "I take a look around for a bit and find something nice to wear."
            $ working(10)
            $ wardrobe.take(temp_var_2, all_notif=True)
            if temp_var_2.type == "pants":
                pcm "I just stole a girls knickers from her bedroom..."
                pcm "Hope she doesn't get the wrong idea."
                pcm "Better wash them first."
        else:
            pcm "I don't think she has any clothes that I don't already have."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
