define pub_open_hours = (11,12,13,14,15,16,17,18,19,20,21,22,23,0,1,2)
define pub_work_hours = (17,18,19,20,21,22,23,0,1,2)

label loc_pub_toilet_girls_stall_closed:
label loc_pub_toilet_girls_closed:
label loc_pub_toilet_boys_closed:
label loc_pub_changingroom_closed:
label loc_pub_closed:
    if t.timeofday == "night":
        pcm "The pub is closed for the night. Will have to come back tomorrow."
    else:
        pcm "The pub is closed. It opens back up at 11."
    if dis(dis_pub):
        $ walk(loc_revel)
    jump travel

label pub_waitress_work_pants_picker:
    if pub_waitress.dict["wear_pants"]:
        pcm "Going commando out there will probably earn me more money..."
        $ pub_waitress.pants = 0
    else:
        pcm "Safer to wear underwear while out there."
        $ pub_waitress.pants = 6
    $ pub_waitress.dict["wear_pants"] = not pub_waitress.dict["wear_pants"]
    jump travel

label pub_waitress_work_socks_picker:
    if pub_waitress.dict["wear_socks"]:
        pcm "Going with my legs bare should earn more tips."
        $ pub_waitress.socks = 0
    else:
        pcm "I should probably wear my socks out there."
        $ pub_waitress.socks = 7
    $ pub_waitress.dict["wear_socks"] = not pub_waitress.dict["wear_socks"]
    jump travel

label pub_waitress_work:
    if not wardrobe.qty(item_outfit_6):
        pcm "I need to buy a new dress before I can work the bar."
        call screen inventory_itemshop_screen(shop_pub)  
        if not wardrobe.qty(item_outfit_6):
            pcm "I can't go out there naked."
            jump travel
    $ pub_waitress.workcycle = 0
    if not ("work" in tab_top and c.outfit == 6):
        $ pc_striptease()
        pause 0.5  
        $ pub_waitress.work_dress(slow=True)






    if bool(c.pants) != pub_waitress.dict["wear_pants"] or bool(c.socks) != pub_waitress.dict["wear_socks"]:
        show sb_pose_upskirt with dissolve
        if pub_waitress.missionvar8 == 0:
            $ pub_waitress.missionvar8 = 1
            show sb_pose_upskirt with dissolve
            if (pub_waitress.socks == 0 and pub_waitress.dict["wear_socks"] == True) and (pub_waitress.pants == 0 and pub_waitress.dict["wear_pants"] == True):
                pc "Hmm, what should I do about my missing pants and socks?"
            elif pub_waitress.socks == 0 and pub_waitress.dict["wear_socks"] == True:
                pc "Hmm, what should I do about my missing socks?"
            elif pub_waitress.pants == 0 and pub_waitress.dict["wear_pants"] == True:
                pc "Hmm, what should I do about my missing pants?"
            show trixie at right1 with dissolve
            trixie.name "Lost parts of your uniform have you?"
            if player.has_perk(perk_commando) and not c.pants and not c.socks:
                pc "My knickers? No, I got rid of those. Socks kind of went missing though."
                trixie.name "Oh? You are going to make the men really happy round here then."
                trixie.name "Well, if you ever want to replace something you can get new ones from the locker over there. They go missing a lot though so need to pay."
            else:
                $ player.face_shame()
                pc "Errr..."
                trixie.name "Haha. Don't worry. It \"happens\" to all of us. There are spare ones in the staff lockers but since these things seem to \"get lost\" all the time you have to pay to replace them."
            trixie.name "Just be sure that no matter how you lose them, to make up more than they cost."
            $ player.mouth = 1
            pc "I'll keep that in mind."
            trixie.name "You do that hon, have fun out there."
            $ player.face_normal()
            hide trixie with dissolve

        pcm "Hmm, I finished my last shift with bits of my uniform missing."
        menu:
            "Buy replacements":
                call screen inventory_itemshop_screen(shop_pub, show_locked=True)
                $ pub_waitress.work_dress()
            "Just work as I am":

                $ NullAction()

        pc "Ok, off we go then."
    if renpy.showing("sb_pose_upskirt"):
        hide sb_pose_upskirt with dissolve
    if "pub_started_working" in dani.dict and "willwork_pub" in dani.list and not "asked_about_dani" in trixie.list and dani.dict["pub_started_working"] > (t.day - 2):
        $ add_to_list(trixie.list, "asked_about_dani")
        show trixie at right1 with dissolve
        trixie.name "By the way [name]. A girl came asking for work saying she knew you."
        pc "Ah [dani.nname] finally came by?"
        trixie.name "Yeah, just checking if you did actually know her."
        pc "She get the job?"
        trixie.name "Of course. I would have given her it even if she didn't know you. But it's better that you sent her here."
        pc "Ah good. Hopefully she can deal with it."
        trixie.name "We'll see."
        hide trixie with dissolve
    if dani_here(loc_pub) and not "pub_first_talk" in dani.list:
        show dani happy at right1 with dissolve
        $ add_to_list(dani.list, "pub_first_talk")
        dani.name "Hey [name]!"
        if dani.dict["pub_started_working"] == t.day:
            pc "Oh hey [dani.nname]. Your first day?"
            dani.name "Yeah."
        else:
            pc "Oh hey [dani.nname]. Good to see you are still here after your first day."
            dani.name "Yeah, it's not so bad and need the money."
        pc "Well, good luck out there. Don't kick too many drunks."
        dani.name "Ha! I will try not to."
        hide dani with dissolve
    jump pub_waitress_work_picker

label pub_waitress_work_picker:
    if not loc_cur == loc_pub:
        $ walk(loc_pub)
    $ male_npc_create_all()
    $ tempname = pubpatron


    $ quest_temp = pub_waitress
    $ player.soldprice = 0
    $ pub_waitress.missionvar1 = False
    $ player.reset_sex_status(True)
    $ player.face_normal()
    if pub_waitress.workcycle >= 4 or not pub_waitress.can_work():
        $ pub_waitress.work()
        if not pub_waitress.can_work():
            pcm "The pub will be closing soon so I had better get ready to head home."
            jump pub_waitress_work_home
        else:
            if player.tired < 20:
                pcm "My shift is over but I am too tired to be working any more..."
                if inv.qty(item_wakeup):
                    menu:
                        "Take some Wakeup":
                            call item_wakeup_action from _call_item_wakeup_action
                            jump pub_waitress_work_picker
                        "Don't bother":
                            $ NullAction()

                pcm "Best I call it a night."
                jump pub_waitress_work_home
            elif player.mood < 20:
                pcm "My shift is over and I am in no mood to do any more work. Should I stay?"
                menu:
                    "Take a Joy" if (player.mood < 20 and inv.qty(item_joy)):
                        call item_joy_action from _call_item_joy_action
                        jump pub_waitress_work_picker
                    "Have a beer before working another shift" if (player.mood < 20):
                        jump pub_waitress_work_picker_beer
                    "Call it a night":
                        jump pub_waitress_work_home
            else:
                pcm "That's my shift over but the pub is still open. Should I work some more?"
                menu:
                    "Work another bar shift":
                        jump pub_waitress_work_picker
                    "Work at the gloryhole" if loc_pub_toilet_girls.has_gloryhole:
                        jump pub_waitress_work_gloryhole
                    "Call it a night":
                        jump pub_waitress_work_home
    else:

        if not pub_waitress.workcycle:
            $ player.left_hand = "beer"
            $ player.right_hand = "beer"
            $ dialouge = renpy.random.choice([
            "I head to the bar and grab the drinks that are up for order.",
            "I take the drinks that are up for order then head off to the people who ordered them.",
            "I grab the drinks up for order and head into the crowd.",
            "I grab the drinks from the bar and make my way to whoever ordered them."
            ])
            "[dialouge]"
        elif not numgen(0,10):
            $ pub_waitress.workcycle += 1
            jump pub_waitress_work_cleaner
        else:
            $ dialouge = renpy.random.choice([
            "I start making my way back to the bar, picking up orders as I head through the crowd then grab some more beers to take to a table.",
            "I get a few orders from waiting patrons before heading back to the bar to see if there are any more orders.",
            "There are more orders at the bar so I head there to deal with them while picking up more orders on my way.",
            "I head back to the bar to get some more orders."
            ])
            "[dialouge]"
            $ player.left_hand = "beer"
            $ player.right_hand = "beer"



        $ pub_waitress.workcycle += 1
        $ rand_choice = WeightedChoice([
        ("pub_waitress_work_normal", 500),
        ("pub_waitress_work_clevage", If (pub_waitress.timesworked >= 2, 100,0)),
        ("pub_waitress_work_ass", If (pub_waitress.timesworked >= 2, 100,0)),
        ("pub_waitress_work_harass", If (pub_waitress.timesworked >= 6, 100,0)),
        ("pub_waitress_work_others_picker", If (pub_waitress.timesworked >= 6, 100,0)),
        ])
        jump expression rand_choice

label pub_waitress_work_picker_beer:
    "I head over to the bar and have a sit down while taking one of the drinks that is ready for a customer."
    $ player.left_hand = "beer"
    pcm "Phew... This could do the job."
    $ relax(10)
    $ player.beer()
    if player.mood < 20:
        pcm "Hmmm, another I think."
        $ player.left_hand = "beer"
        pc "..."
        $ relax(10)
        $ player.beer()
    pcm "Well, better get back to it..."
    jump pub_waitress_work_picker

label pub_waitress_work_home:

    $ walk(loc_pub_changingroom)
    $ player.face_normal()
    "I head back to the changing rooms to get changed and count up the tips I collected."

    if pub_waitress.reward_counter <= 20:
        pc "Didn't really earn much today, only £[pub_waitress.reward_counter]. Wonder if I should be more friendly to the drunks."
    elif pub_waitress.reward_counter >= 50:
        pc "Did quite well for tips out there tonight. Managed to get £[pub_waitress.reward_counter]."
    else:
        pc "Hmm, tips I suppose are alright tonight. Got £[pub_waitress.reward_counter] for tonights work."
    $ player.add_money(pub_waitress.reward_counter)

    if pub_waitress.missionvar2 > 0 and pub_waitress.missionvar3 > 0:
        $ pub_waitress.missionvar2 += pub_waitress.missionvar3
        pc "And I made £[pub_waitress.missionvar2] selling my pants and socks. Perverts will buy anything a woman touches it seems."
        $ player.add_money(pub_waitress.missionvar2)
    elif pub_waitress.missionvar2 > 0:
        pc "And I made £[pub_waitress.missionvar2] selling my socks to some pervert."
        $ player.add_money(pub_waitress.missionvar2)
    elif pub_waitress.missionvar3 > 0:
        pc "And I made £[pub_waitress.missionvar3] selling my pants to some pervert."
        $ player.add_money(pub_waitress.missionvar3)
    $ pub_reset_vars()
    $ pub_waitress.work()
    pc "Ok, time to get dressed and leave this place."
    $ pc_striptease()
    pause 1
    $ pc_dress_slow(outfit="party")
    $ walk(loc_pub)
    if robin_here():
        show robin at right1 with dissolve
        robin.name "Ah, you heading home?"
        pc "Yeah. I'm done for now."
        if t.hour >= 2:
            robin.name "Want to catch the bus together?"
            menu:
                "Sure, lets go":
                    jump robin_goto_home
                "No, I have other things to do":
                    robin.name "Okay, be safe."
                    hide robin with dissolve
        else:
            robin.name "Okay. I'll hang around for a bit more."
            pc "Don't get in too much trouble."
            robin.name "Sure."
            hide robin with dissolve
    if loc_cur.closed():
        $ walk(loc_revel)
    jump travel_arrival

label pub_waitress_work_home_drunk:
    $ walk(loc_pub_changingroom)
    $ player.face_normal()
    "I stagger back to the changing rooms to get changed."
    pc "Fuck, I drank way too much..."
    if pub_waitress.missionvar2 > 0 or pub_waitress.missionvar3 > 0:
        "I scoop my tip money into my purse, It comes to £[pub_waitress.reward_counter] plus whatever I made from selling my clothes."
    else:
        "I scoop my tip money into my purse, It comes to £[pub_waitress.reward_counter]."
    $ player.add_money(pub_waitress.reward_counter)
    $ player.add_money(pub_waitress.missionvar2)
    $ player.add_money(pub_waitress.missionvar3)
    $ pub_reset_vars()
    $ pub_waitress.work()
    pc "Better get changed."
    $ pc_striptease()
    pause 1
    $ pc_dress_slow(outfit="party")
    $ walk(loc_pub)
    if robin_here():
        show robin at right1 with dissolve
        robin.name "Ah, you heading home?"
        pc "Yeah. I'm done for now."
        if t.hour == 2:
            robin.name "Want to catch the bus together?"
            menu:
                "Sure, lets go":
                    jump robin_goto_home
                "No, I have other things to do":
                    robin.name "Okay, be safe."
                    hide robin with dissolve
        else:
            robin.name "Okay. I'll hang around for a bit more."
            pc "Don't get in too much trouble."
            robin.name "Sure."
            hide robin with dissolve
    if loc_cur.closed():
        $ walk(loc_revel)
    jump travel_arrival






label pub_waitress_work_cycle1:

    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_cycleend", 200),
    ("pub_waitress_work_clean_harass", If (pub_waitress.timesworked >= 5 and renpy.showing("sb_table"), 100, 0)),
    ("pub_waitress_work_talk", If (pub_waitress.timesworked >= 5, 70, 0)),
    ("pub_waitress_work_talk", If (pub_waitress.timesworked >= 5 and player.mood < 40, 100, 0)),
    ("pub_waitress_work_talk", If (pub_waitress.timesworked >= 5 and player.mood < 20, 200, 0))
    ])
    jump expression rand_choice

label pub_waitress_work_cycle2:
    if renpy.showing("pub_serve_talking"):
        hide pub_serve_talking with dissolve

    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_cycleend", 500),
    ("pub_waitress_work_lap", If (pub_waitress.timesworked >= 10, player.desire + player.drunk,0))
    ])
    jump expression rand_choice

label pub_waitress_work_cycle3:
    if renpy.showing("pub_serve_lap"):
        hide pub_serve_lap with dissolve

    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_cycleend", 500),
    ("pub_waitress_work_table", If (pub_waitress.timesworked >= 15, player.desire + player.drunk, 0))
    ])
    jump expression rand_choice

label pub_waitress_work_cycleend:
    $ working(15)
    $ player.soldprice = 0
    $ pub_waitress.missionvar1 = 0
    $ renpy.scene()
    $ player.reset_sex_status(True)
    with dissolve
    $ walk(loc_pub)

    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_picker", If(not pub_waitress.can_work(), 10000, 0)),
    ("pub_waitress_work_picker", 500),
    ("pub_waitress_work_cycleend_cleantoilet", 30),
    ("pub_waitress_work_cycleend_harass", If (pub_waitress.timesworked >= 6, 100,0)),
    ("pub_waitress_work_cycleend_cumleak", If (player.cum_locations["cum_vagin"] == True, 50,0)),
    ("pub_waitress_work_cycleend_wash", If (player.hygiene <= 20, 1000, 0)),
    
    ("pub_waitress_work_cycleend_malestart", If (player.has_perk(perk_male), ((-player.body_conf) / 2), 0)),
    ("pub_waitress_work_cycleend_newstart", If (pub_waitress.timesworked < 20, 50, 0)),
    ("pub_waitress_work_others_picker", If (pub_waitress.timesworked >= 6, 100,0)),
    ])
    jump expression rand_choice

label pub_waitress_work_ogleend:
    $ player.soldprice = 0
    $ player.face_normal()

    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_normal", 500),
    ])
    jump expression rand_choice

label pub_waitress_work_cycleend_cumleak:
    pc "Fuck, I can feel cum leaking out of me..."
    $ walk(loc_pub_toilet_girls)
    "I head to the toilets to clean myself up a bit."
    if player.has_perk(perk_preg_want):
        pc "It's annoying, but a price I have to pay to get what I want."
    else:
        pc "Uff, this is annoying. Probably shouldn't have let him cum in me."
    jump pub_waitress_work_picker

label pub_waitress_work_cycleend_cleantoilet:
    patron "Hey, I just came from the toilet and it's a mess. Someone puked up all over the place."
    $ player.face_annoyed()
    pc "Ugh, thanks..."
    pc "Suppose I had better clean it... *Sigh*"
    $ randomnum = renpy.random.randint(0, 1)
    if randomnum == 0:
        $ walk(loc_pub_toilet_girls)
    else:
        $ walk(loc_pub_toilet_boys)
    $ player.face_puke()
    pc "Ubb. Fucking disgusting!"
    jump action_clean_event_picker_tombola

    $ show_cleaning_image()
    $ player.face_normal()
    "I spend the next few minutes cleaning up the mess."
    $ player.add_mood(-10)
    $ player.add_desire(-10)
    pcm "There we go..."
    $ renpy.scene()
    with dissolve
    jump pub_waitress_work_picker

label pub_waitress_work_cycleend_wash:
    pc "I am starting to smell a bit. I should probably clean myself up."
    $ walk(loc_pub_toilet_girls)
    $ player.face_worried
    pc "Hmm, not much privacy. Hope no one is in here..."
    $ c.outfit = 0
    $ player.add_desire(10)
    $ player.add_mood(-5)
    $ player.wash()
    "I quickly wash my body down with some warm water and hand soap and use some paper towels to pat myself dry."
    $ player.face_normal()
    if danger_gen(300, 1):
        pc "That should do until I can have a show..."
        jump pub_waitress_work_ko
    pc "That should do until I can have a shower."
    $ pub_waitress.work_dress()
    pc "Ok, better head back to it."
    jump pub_waitress_work_picker

label pub_waitress_work_cycleend_newstart:
    $ dialouge = WeightedChoice([
    ("Do these perverts think I can't hear what they are saying about me?", 100),
    ("I know this dress is small. But do they need to be so open about trying to look up it?", 100),
    ("Ugh, can't count how many times I overheard someone commenting about my tits.", If (player.breasts > 1, 100,0)),
    ("These perverts don't even pretend they aren't looking at my tits.", If (player.breasts > 1, 100,0)),
    ("At least pretend you are looking somewhere else. These fuckers just stare at me drooling.", 100),
    ])
    pcm "[dialouge]"
    jump pub_waitress_work_picker

label pub_waitress_work_cycleend_malestart:
    $ dialouge = WeightedChoice([
    ("So this is what it felt like for the girls before. Or are these guys even worse. The comments are endless.", 100),
    ("Never thought I would be flashing my arse to a bunch of men. Ugh...", 100),
    ("I'm not even used to having tits myself and these fuckers are looking at them like a lion looking at prey.", If (player.breasts > 1, 100,0)),
    ("Not even used to being in this body myself. Having these guys drooling over me is weird.", If (player.breasts > 1, 100,0)),
    ("Come on guys. At least show some respect. Was it always like this for serving girls in the past?", 100),
    ])
    pcm "[dialouge]"
    jump pub_waitress_work_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
