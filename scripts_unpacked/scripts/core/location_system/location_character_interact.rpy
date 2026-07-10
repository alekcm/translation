screen action_button_npc_TEMPLATE():




    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + simon.setname, "simon_talk_subject")
        showif expand_button:
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("work", "Ask about work", "simon_work_picker")
            if log.interactive("mira_missing_05"):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("quest", "Ask about " + mira.setname, "quest_mira_missing_whore_investigation_simon")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_expand():
    frame padding (0,0) xysize (61,25) pos (0,-20) background None:
        add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
            action [SetVariable("action_npc_var", If(action_npc_var, False, loc_cur.name))]
            hovered Show("travel_but_text", text="More actions")
            unhovered Hide("travel_but_text")

screen action_button_npc_robin():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + robin.setname, "robin_talk_picker")
        showif expand_button:




            if robin.love > 40:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("gift", "Give gift", "robin_gift_picker")


            if robin.isslut and quest_wolfgang.sex > 5 and not robin_can_bitch():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("howl", "Introduce to bitching", "robin_action_park_adventure_picker")



            if sum([robin_can_bus(), robin_can_bitch(), robin_can_slut()]) > 1:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("whore", "Do something fun", "robin_action_fun_picker")


            elif robin_can_bus():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("bus", "Go on bus ride", "robin_action_bus_adventure_invite")
            elif robin_can_bitch():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("howl", "Go bitching", "robin_action_park_adventure_picker")
            elif robin_can_slut():
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("whore", "Offer to go out", "robin_talk_sexobject_offer_outing_start")



        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_jaylee():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + jaylee.setname, "jaylee_talk_picker")
        showif expand_button:
            if loc_cur == loc_junk_2:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("shop", "Sell junk", "jaylee_shop_sell")
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("shop", "Buy jewelery", "jaylee_shop_buy")
            elif loc_cur == loc_junk_trailer:
                if jaylee.can_sex:
                    frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                        $ amount_total += amount
                        use action_button("heart", "Offer fun", "robin_sex_picker")
                if jaylee.love > 40:
                    frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                        $ amount_total += amount
                        use action_button("gift", "Give gift", "jaylee_gift_picker")
        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_oskar():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + oskar.setname, "oskar_talk_picker")
        showif expand_button:
            if loc_cur == loc_office_ll:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("buy", "Pay rent", "oskar_talk_pay_rent")

                if not log.interactive("quest_rent_b"):
                    frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                        $ amount_total += amount
                        use action_button("work", "Ask about work", "oskar_talk_ask_work")
                if oskar.can_sex:
                    frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                        $ amount_total += amount
                        use action_button("whore", "Reduce rent", "oskar_talk_pay_rent_sex_offer")
                if log.interactive("quest_rent_b") and not oskar.can_sex and not oskar.rape and rent_total_owed() and player.has_perk([perk_whore, perk_sucu]):
                    frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                        $ amount_total += amount
                        use action_button("whore", "Negotiate rent", "oskar_talk_pay_rent_sex_offer_pc_ask")
        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_cass():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + cass.setname, "cass_talk_subject")
        showif expand_button:
            if cass.love > 40 and not "broken" in cass.list:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("gift", "Give gift", "cass_gift_picker")
        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_mira():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + mira.setname, "mira_talk_subject")
        showif expand_button:
            if mira.love > 40:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("gift", "Give gift", "mira_gift_picker")

            if "offered_whore_training" in mira.list and not quest_whore.active:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("whore", "Become a whore", "mira_whore_train_start")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_cass_mira():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + cass.setname + " and " + mira.setname, "cass_mira_talk_picker")
        showif expand_button:
            if mira.love > 40:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("gift", "Give gift to " + mira.setname, "mira_gift_picker")
            if cass.love > 40 and not "broken" in cass.list:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("gift", "Give gift to " + cass.setname, "cass_gift_picker")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_felix():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + felix.setname, "felix_talk_test")
        showif expand_button:
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("buy", "Sell photos", "felix_sell_photos")
            if log.interactive("photo_02"):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("work", "Ask about work", "school_photo_work_picker")
            if felix.can_gift:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("gift", "Give gift", "felix_gift_picker")
            if felix.can_sex and loc(loc_school_darkroom):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("heart", "Flirt", "felix_sex_picker")
        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_dani():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + dani.setname, "dani_talk_picker")
        showif expand_button:
            if dani.love > 40:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("gift", "Give gift", "dani_gift_picker")
            if dani.sex_les > 3 and loc(loc_bedroom_dani):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("heart", "Have some fun", "dani_sex_bedroom_picker")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_anabel():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + anabel.setname, "anabel_talk_picker")
        showif expand_button:
            if anabel.love > 40:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("gift", "Give gift", "anabel_gift_picker")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_simon():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + simon.setname, "simon_talk_subject")
        showif expand_button:
            frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                $ amount_total += amount
                use action_button("work", "Ask about work", "simon_work_picker")
            if log.interactive("mira_missing_05"):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("quest", "Ask about " + mira.setname, "quest_mira_missing_whore_investigation_simon")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_lake_dealer():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("shop", "Buy sweets", "lake_dealer_shop")
        showif expand_button:
            if lake_dealer.osex or lake_dealer.sex and player.has_perk([perk_slut, perk_whore, perk_sucu, perk_bimbo, perk_broken]):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("buy", "Ask for a discount", "lake_dealer_shop_discount_ask")
            if lake_dealer.can_sex and player.has_perk([perk_slut, perk_whore, perk_sucu, perk_bimbo, perk_broken]):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("whore", "Have sex", "lake_dealer_sex_ask")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_kitty():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + kitty.setname, "kitty_talk_picker")
        showif expand_button:
            if "whore_offer" in kitty.list and not log.interactive("quest_whore_01"):
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("whore", "Ask about whoring", "kitty_whore_quest_start")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")

screen action_button_npc_rachel():
    default expand_button = False
    $ amount_total = -65
    $ amount = -65
    frame padding (0,0) xysize (61,61) background None:
        use action_button("talk", "Talk to " + rachel.setname, "rachel_talk_picker")
        showif expand_button:
            if "can_play_games" in rachel.list:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("streak", "Streaking games", "rachel_talk_exhib_game_picker")
            if "rachel_talk_exhib_games_chain" in rachel.dict and rachel.dict["rachel_talk_exhib_games_chain"] >= 5 and quest_wolfgang.active and not "can_bitch" in rachel.list and quest_wolfgang.sex > 5:
                frame padding (0,0) xysize (61,61) pos (0, amount_total) background None:
                    $ amount_total += amount
                    use action_button("howl", "Talk about bitching", "rachel_talk_exhib_bitching_start")

        showif not expand_button and amount_total != amount:
            frame padding (0,0) xysize (61,25) pos (0,-20) background None:
                add "action_arrow" anchor (0.5,0.5) align (0.5,0.5)
                imagebutton auto "action_button_arrow_%s" anchor (0.5,0.5) align (0.5,0.5):
                    action [Hide("travel_but_text"), SetLocalVariable("expand_button", True)]
                    hovered Show("travel_but_text", text="More actions")
                    unhovered Hide("travel_but_text")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
