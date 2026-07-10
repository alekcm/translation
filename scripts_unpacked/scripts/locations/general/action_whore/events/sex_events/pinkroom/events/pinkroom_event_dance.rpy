init python:
    def pinkroom_customer_event_dance_clothes_checker():
        if (wardrobe.qty(item_top_19) or wardrobe.qty(item_top_20)) and wardrobe.qty(item_bottom_13):
            return True
        else:
            return False

    def pinkroom_customer_event_dance_clothes_setter():
        work.reset_clothes()
        if wardrobe.qty(item_top_19):
            work.top = 19
        else:
            work.top = 20
        
        work.bottom = 13
        
        if player.has_perk(perk_commando):
            work.pants = 0
        elif wardrobe.qty(item_pants_5):
            work.pants = 5
        elif wardrobe.qty(item_pants_6):
            work.pants = 6
        else:
            work.pants = 0
        
        work.top_primary_colour = "white"
        work.bottom_primary_colour = "black"
        work.pants_primary_colour = "pink"
        work.pants_secondary_colour = "pink"
        work.socks_primary_colour = "black"
        work.socks_secondary_colour = "black"
        for i in clothes_wardrobe_list:
            setattr(work, i + "primary_trans", "trans_normal")
            setattr(work, i + "secondary_trans", "trans_normal")



label pinkroom_customer_event_dance:
    tempname.name "Hey [rlist.name_cute], how about you entertain me a bit."
    pc "Oh? How so?"
    tempname.name "A little dance, striptease, singing? Something like that."
    pc "Sure, I can do that."
    $ inv.take(item_pinkticket)
    if school_dance_quest_show_count >= 4 and pinkroom_customer_event_dance_clothes_checker():
        pc "I have some clothes I sometimes dance in for work, want me to dress up in them?"
        if not numgen(0,2):
            tempname.name "No thanks [rlist.name_cute], better with nothing on."
            pc "Okay."
        else:
            tempname.name "Sure, that sounds like fun."
            $ pinkroom_customer_event_dance_clothes_setter()
            $ pc_dress_slow("work")
            pc "How's this?"
            tempname.name "Looks good to me."
    pc "Sit down then."
    "He heads over to the bed and sits down, no doubt eager to see what I will do."
    hide male_generic with dissolve
    $ temp_var_1 = "solo"
    call pinkroom_customer_event_dance_dancecall from _call_pinkroom_customer_event_dance_dancecall
    pc "Thank you, I am here all week!"
    $ renpy.scene()
    show male_generic at right1
    with dissolve
    if numgen():
        tempname.name "Whoo, go again!"
        pc "Want some more? Okay."
        call pinkroom_customer_event_dance_dancecall from _call_pinkroom_customer_event_dance_dancecall_1
        pc "Thank you! Thank you!"
    if numgen():
        if numgen():
            tempname.name "How about we do something more exciting?"
            pc "Sounds good to me."
            jump whore_street_sex_start_picker
        else:
            $ renpy.scene()
            show sb_standbehind happy
            with dissolve
            pc "Oh? Got you all excited have I?"
            "His hands are all over me and it's pretty clear what he wants."
            $ renpy.scene()
            $ renpy.show(renpy.random.choice(["sb_againstwall2 pokevag wink worried", "sb_againstwall3 poke wink"]))
            with dissolve
            jump whore_street_sex_standing_vag_picker
    else:
        tempname.name "Cheers [rlist.name_cute]."
        pc "No problem."
        jump whore_street_sex_end

label pinkroom_customer_event_dance_group:
    show male2_generic at right2
    show male3_generic at right3
    with dissolve
    tempname.name "Hey [rlist.name_cute], how about you entertain us a bit."
    pc "All of you? What do you want to do?"
    tempname.name "A little dance, striptease, singing? Something like that."
    $ inv.take(item_pinkticket, 3)
    if school_dance_quest_show_count >= 4 and pinkroom_customer_event_dance_clothes_checker():
        pc "I have some clothes I sometimes dance in for work, want me to dress up in them?"
        if not numgen(0,2):
            tempname.name "No thanks [rlist.name_cute], better with nothing on."
            pc "Okay."
        else:
            tempname.name "Sure, that sounds like fun."
            $ pinkroom_customer_event_dance_clothes_setter()
            $ pc_dress_slow("work")
            pc "How's this?"
            tempname.name "Looks good to me."
    pc "Okay, find some space you guys."
    "The boys find empty space to sit around and watch me."
    $ temp_var_1 = "group"
    call pinkroom_customer_event_dance_dancecall from _call_pinkroom_customer_event_dance_dancecall_2
    pc "Thank you, I am here all week!"
    $ renpy.scene()
    show male_generic at right1
    with dissolve
    if numgen():
        tempname.name "Whoo, go again!"
        pc "Want some more? Okay."
        call pinkroom_customer_event_dance_dancecall from _call_pinkroom_customer_event_dance_dancecall_3
        pc "Thank you! Thank you!"
    if numgen():
        $ player.sex_man_amount = numgen(3,5)
        if numgen():
            $ renpy.scene()
            show male_generic at right1
            with dissolve
            tempname.name "How about we do something more exciting with us?"
            pc "All of you?"
            show male2_generic nude at right2 with dissolve
            tempname2.name "Let's see if you can handle us."
            pc "Okay."
            $ renpy.scene()
            with dissolve
            jump whore_street_sex_group_start_picker
        else:
            $ renpy.scene()
            show sb_standbehind happy
            with dissolve
            pc "Oh? Got you all excited have I?"
            "His hands are all over me and it's pretty clear what he wants."
            pc "We aren't alone here?"
            tempname.name "That's fine, we will all have a go."
            pc "Uh oh..."
            hide sb_standbehind with dissolve
            jump whore_street_sex_group_start_picker
    else:
        $ renpy.scene()
        show male2_generic at right2
        show male3_generic at right3
        with dissolve
        tempname2.name "Cheers [rlist.name_cute]."
        pc "You heading off?"
        tempname2.name "We are, he isn't. Have fun."
        hide male2_generic
        hide male3_generic
        with dissolve
        pc "Oh? Staying for some alone fun?"
        show male_generic nude with dissolve
        tempname.name "Yeah."
        jump whore_street_sex_start_picker

label pinkroom_customer_event_dance_dancecall:
    $ renpy.scene()
    show ps_dance
    with dissolve
    if temp_var_1 == "solo":
        "I start dancing for the guy sitting and watching. But it's a bit quiet so I decide to sing."
    else:
        "I start dancing for the boys who are eagerly watching me. But it's a bit quiet so I decide to sing."
    pc "[rlist.singing_dialogue_1]"
    tempname.name "Whoo!"
    if temp_var_1 == "group":
        $ player.spank()
        pc "Ohh!"
        tempname2.name "Keep going girl!"
    pc "[rlist.singing_dialogue_2]"
    if c.top:
        "I slip my hands under my top and over my head giving a bit of a striptease."
        $ c.top = 0
        if temp_var_1 == "group":
            tempname2.name "Yeah take it off!"

    pc "[rlist.singing_dialogue_3]"
    $ renpy.scene()
    show dance_behind
    with dissolve
    if temp_var_1 == "group":
        tempname2.name "Nice ass!"
        $ player.spank()
    if c.bottom:
        "I hook my fingers under my skirt and strip them off."
        $ c.bottom = 0
    "I dance around the room making sure to give a good view of everything I have to offer."
    if c.pants:
        $ renpy.scene()
        show dance_behind
        with dissolve
        "With just my pants left, as an encore I strip them off and throw them onto the bed."
        $ c.pants = 0
    pc "[rlist.singing_dialogue_4]"
    tempname.name "Yeah! Shake it!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
