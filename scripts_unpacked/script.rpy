label start:


    call location_call from _call_location_call_1
    $ inv = Inventory()
    $ inv_backup = Inventory()
    $ buy_inv = Inventory()
    $ wardrobe = Inventory()

    call inventory_items from _call_inventory_items
    call clothes from _call_clothes_1

    call perks_call from _call_perks_call

    call npc_call from _call_npc_call
    call shops_call from _call_shops_call
    call polaroids_call from _call_polaroids_call

    $ shop_milk.open = False
    $ shop_needle.open = False
    $ shop_motel.open = False



    $ game_version = config.version
    $ game_version_start = config.version



    $ rlist = Random_list_generator()
    $ weather_var = 1

    $ tattoo = BodyPaint()
    $ scar = BodyPaint()
    $ bruise = BodyPaint()
    $ blood = BodyPaint()
    $ writing = BodyPaint()
    $ skin_effect = BodyPaint()


    $ player = PlayerStats()
    $ t = Time(0, 24, 60, 7)





    $ acc = Accessories()
    $ accbak = Accessories()
    $ accchangebak = Accessories()




    $ c = Clothes(outfit=1)
    $ school = Clothes()
    $ daily = Clothes(top=1, bottom=1, bra=2, pants=3)
    $ party = Clothes()
    $ sport = Clothes()
    $ swim = Clothes()
    $ home = Clothes()
    $ work = Clothes()
    $ shop = Clothes()
    $ temp_outfit = Clothes()

    $ school2 = Clothes()
    $ daily2 = Clothes()
    $ party2 = Clothes()
    $ sport2 = Clothes()
    $ swim2 = Clothes()
    $ home2 = Clothes()

    $ school.outfit_colours("custom6","custom6","custom6","custom3","custom3","custom11","custom6","custom1","custom3","custom3","custom3","custom3","custom3","custom3")
    $ daily.outfit_colours("custom6","custom1","custom6","custom6","custom6","custom1","custom6","custom1","custom3","custom3","custom3","custom3","custom3","custom3")
    $ party.outfit_colours("custom6","custom1","custom6","custom6","custom6","custom1","custom6","custom1","custom3","custom3","custom3","custom3","custom3","custom3")
    $ sport.outfit_colours("custom6","custom11","custom6","custom6","custom6","custom11","custom6","custom11","custom3","custom3","custom3","custom3","custom3","custom3")
    $ swim.outfit_colours("custom6","custom11","custom6","custom6","custom6","custom11","custom6","custom11","custom3","custom3","custom3","custom3","custom3","custom3")
    $ home.outfit_colours("custom6","custom6","custom6","custom6","custom6","custom6","custom6","custom3","custom3","custom3","custom3","custom3","custom3","custom3")
    $ work.outfit_colours("custom6","custom6","custom6","custom6","custom6","custom6","custom6","custom3","custom3","custom3","custom3","custom3","custom3","custom3")
    $ shop.outfit_colours("custom6","custom11","custom6","custom11","custom6","custom11","custom6","custom11","custom6","custom11","custom6","custom11","custom11","custom6")





    $ player.race = 1
    $ player.hair_colour = 2
    $ player.eye_colour = 1
    $ player._hair_length = 1
    $ player.hair_fringe = 1






    call quests_call from _call_quests_call






    default emile_tutorial_info = 0






    $ school_dance_intro = False
    $ school_dance_quest_on_team = False
    $ school_dance_quest_preg = False
    $ school_gym_preg = False



    $ school_day = 0

    $ school_met_friend = False

    $ school_class_first_assignment_given = False





    $ new_day()



    $ log.keyon()






    scene main_menu


    $ npc_pass_time(40)

    "This game contains adult and mature themes not suitable for minors. Are you over 18 or of legal age according to your country's laws?"
    menu:
        "Yes":
            $ NullAction()
        "No":

            "Then by the laws of your country, you are unable to play this game."
            return

    if renpy.variant("web"):
        "Note, you are playing the web/browser version of The Fixer. This version does not use autosaves to be sure to manually save regularly. For the best experience, download the standalone version."

    "Are you a returning player who wants to skip the prologue?"
    menu:
        "Play from the start (Recommended for new players)":
            $ diary_list = []
            $ t.hour = 7
            $ player.add_conf(-100)
            jump start_hospital_intro
        "Skip (Not recommended for new players.)":

            $ diary_list = []
            $ t.hour = 7
            menu:
                "Female start":
                    $ player.male_origin = False
                "Male start":
                    $ player.male_origin = True


            menu:
                "Rename character":
                    $ fname = renpy.input("What do you want your new first name to be?", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=12)
                    $ fname = fname.strip()

                    if fname == "":
                        $ fname = "Samantha"

                    $ name = renpy.input("[fname]. Okay got it, a bit formal though isn't it? What do you want people to normally call you? Something short and cute.", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=12)
                    $ name = name.strip()

                    if name == "" and fname == "Samantha":
                        $ name = "Sammy"
                    elif name == "":
                        $ name = fname
                "Keep it as Samantha/Sammy":

                    $ NullAction()

            if not player.male_origin:
                "Pick an origin perk"
                call screen perk_choice(perk_origin_list)


            scene blank
            show screen background_scene(_layer="bg_screen")
            show screen pc_avatar(_layer="pc_avatar")
            show screen foreground_scene(_layer="fg_bg_screen")
            show screen right_menu

            $ player.hair_fringe = numgen(1, 6)
            $ player._hair_length = numgen(1,35)
            $ player.hair_colour = random(hair_colours_custom_list)
            $ player.eye_colour = random(eye_colours_custom_list)
            $ player.breasts = numgen(1, 3)
            $ acc.eyeliner = numgen(1, 4)

            $ wardrobe.take(item_bra_1, notif=True)
            $ wardrobe.take(item_outfit_3, notif=True)
            $ wardrobe.take(item_pants_1, notif=True)

            $ wardrobe.take(item_bottom_8, notif=True)
            $ wardrobe.take(item_top_8, notif=True)

            $ wardrobe.take(item_bottom_5, notif=True)
            $ wardrobe.take(item_top_12, notif=True)
            $ wardrobe.take(item_socks_3, notif=True)



            $ daily.outfit = 3
            $ daily.pants = 1
            $ daily.bra = 1
            $ tab_top = "daily"
            $ pc_dress()

            $ player.add_money(200)


            $ school.top = 12
            $ school.bottom = 5
            $ school.socks = 3
            $ sport.top = 8
            $ sport.bottom = 8
            $ swim.outfit = 0

            $ school.bra = daily.bra
            $ school.pants = daily.pants
            $ sport.bra = daily.bra
            $ sport.pants = daily.pants

            $ school.inappropriate_check()
            $ daily.inappropriate_check()
            $ party.inappropriate_check()
            $ swim.inappropriate_check()
            $ home.inappropriate_check()

            $ player.add_perk(perk_virgin)
            $ player.add_perk(perk_fresh, days=14)

            $ weather_var = 1

            if player.male_origin:
                $ player.origin_perk = perk_male
                $ player.add_perk(perk_male)
                $ player.add_preg_desire(-200)
                $ player.body_conf = -200


            $ player.update_stats()
            if player.origin_perk == perk_bimbo:
                $ player.hair_colour = "hair1"
                $ player.breasts = 3
            if player.origin_perk == perk_gamine:
                $ player.add_preg_desire(-200)
            if player.has_perk(perk_broodmother):
                $ player.add_preg_desire(200)

            $ player.cycle_gamestart_randomiser()

            $ player.face_normal()
            $ log.assign("Introduction to The Institute")

            $ diary_list = []
            $ diary_first_day = Diary_Class("Alive again", "Today was a weird day. Woke up in the hospital, told I died then rushed out onto the streets. Ugh. I have no idea what is going on. At least my sister seems to have somewhat of a clue.")


            $ rent_ledger.append(0)
            $ rent_ledger.append(0)

            $ talk_counter = 0


            jump travel
        "Alternate start: Homeless (Experimental)":

            menu:
                "Normal start":
                    $ temp_var_1 = True
                "Virgin start":
                    $ temp_var_1 = False
            $ player.add_conf(-100)
            jump start_homeless_intro
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
