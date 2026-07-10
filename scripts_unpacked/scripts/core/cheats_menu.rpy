init python:

    def cheat_toggle_pregnancy():
        global cheat_pregnancy_enabled
        if cheat_pregnancy_enabled:
            cheat_pregnancy_enabled = False
        else:
            cheat_pregnancy_enabled = True

    def cheat_check_who(who, what):
        global cheat_name_who, speaking_char, test_what, name   
        cheat_name_who = who
        
        if who == name:
            test_what = what

    def get_display_name_for_character(who):
        global speaking_char_class
        if isinstance(speaking_char_class, Npc) and speaking_char_class.name.name == who:
            return speaking_char_class.setname
        elif who == name: 
            return get_display_name_for_pc_character()
        else:
            return who

    def get_display_name_for_pc_character():
        if dis(dis_truckstop) and quest_whore.isactive() and player.iswhore and wname:
            return wname
        else:
            return name

    def pass_time_day():
        for _ in range(24):
            t.hour = 1

    def pass_time_week():
        for _ in range(168):
            t.hour = 1

    def pregnancy_length_cheat():
        global global_pregnancy_length
        if global_pregnancy_length == 7:
            global_pregnancy_length = 21
        elif global_pregnancy_length == 21:
            global_pregnancy_length = 42
        elif global_pregnancy_length == 42:
            global_pregnancy_length = 90
        else:
            global_pregnancy_length = 7

    def cheat_meet_everyone():
        for i in npc_unique:
            i.last_spoke_to = t.day
            if i.has_met and i.bio_text:
                add_to_list(diary_people_list, i)

    def npc_pass_time(tamount=60):
        for _ in range(tamount):
            npc_girls_newday_tick(ignore_timer=True)


    def cheat_preg_all_npc():
        for i in npc_girls:
            i.preg_force(lover)

    def clean_screen():
        
        renpy.hide_screen("sex_action_flash")
        renpy.hide_screen("cum_action")
        renpy.hide_screen("punch")
        renpy.hide_screen("spank_bum")
        renpy.hide_screen("sex_action_flash", layer="fg_screen")
        renpy.hide_screen("sex_cum_action_image", layer="fg_screen")
        renpy.hide_screen('sex_action_image', layer="fg_screen")
        renpy.hide_screen('nosex_cum_action_image', layer="fg_screen")
        for i in irange(0,8):
            renpy.hide_screen("notif_popup_" + str(i))

define cheat_first_time_opening = False
define cheat_name_who = ""
define speaking_char_class = ""
label cheat_first_time_opening_desc:

    "*** IMPORTANT NOTE ***"
    $ cheat_first_time_opening = True
    "Using cheats does not mean more naughty scenes. And often has the opposite effect."
    "The game is not designed to have all your stats maxed out. So you can miss out on a lot of content because of it. Especially in places like Haven which specifically takes advantage of Sammy's lower stats."
    "If you still want to boost your stats anyway. Set them to about 40. This will allow you to trigger both high and low stat requirement events."

    return



screen cheats_screen():
    frame:
        yalign 0.25
        xalign 0.4
        has hbox
        vbox:
            textbutton "CLOSE CHEAT MENU":
                text_size 30
                action Hide("cheats_screen")

            hbox:

                vbox:
                    hbox:
                        text "Desire" size 20
                        textbutton "+10":
                            text_size 20
                            action Function(player.add_desire, 10)
                        textbutton "-10":
                            text_size 20
                            action Function(player.add_desire, -10)
                    hbox:
                        text "Tired" size 20
                        textbutton "+10":
                            text_size 20
                            action Function(player.cheat_add_tired)
                        textbutton "-10":
                            text_size 20
                            action Function(player.cheat_remove_tired)
                    hbox:
                        text "Mood" size 20
                        textbutton "+10":
                            text_size 20
                            action Function(player.cheat_add_mood)
                        textbutton "-10":
                            text_size 20
                            action Function(player.cheat_remove_mood)
                    hbox:
                        text "Confidence" size 20
                        textbutton "+10":
                            text_size 20
                            action Function(player.cheat_add_conf)
                        textbutton "-10":
                            text_size 20
                            action Function(player.cheat_remove_conf)
                    hbox:
                        text "Fitness" size 20
                        textbutton "+10":
                            text_size 20
                            action Function(player.cheat_add_fitness)
                        textbutton "-10":
                            text_size 20
                            action Function(player.cheat_remove_fitness)
                    hbox:
                        text "Intelligence" size 20
                        textbutton "+10":
                            text_size 20
                            action Function(player.cheat_add_int)
                        textbutton "-10":
                            text_size 20
                            action Function(player.cheat_remove_int)
                    hbox:
                        text "Money" size 20
                        textbutton "+1000":
                            text_size 20
                            action Function(player.cheat_add_money)
                        textbutton "-1000":
                            text_size 20
                            action Function(player.cheat_remove_money)

                    hbox:
                        text "Drunk" size 20
                        textbutton "+20":
                            text_size 20
                            action Function(player.add_drunk,20)
                        textbutton "-20":
                            text_size 20
                            action Function(player.add_drunk,-20)

                    hbox:
                        text "Hygiene" size 20
                        textbutton "+20":
                            text_size 20
                            action Function(player.add_hygiene,20)
                        textbutton "-20":
                            text_size 20
                            action Function(player.add_hygiene,-20)

                    hbox:
                        textbutton "Clean screen":
                            text_size 20
                            action Function(clean_screen)

                    hbox:
                        textbutton "Meet all":
                            text_size 20
                            action Function(cheat_meet_everyone)

                    hbox:
                        textbutton "NPC timeskip":
                            text_size 20
                            action Function(npc_pass_time)

                    hbox:
                        textbutton "player cycle":
                            text_size 20
                            action Function(player.cycle)





                    hbox:
                        textbutton "Pass hour":
                            text_size 20
                            action SetVariable("t.hour", 1)

                    hbox:
                        textbutton "Pass day":
                            text_size 20
                            action Function(pass_time_day)
                    hbox:
                        textbutton "Pass Week":
                            text_size 20
                            action Function(pass_time_week)
                    hbox:
                        textbutton "Perk menu":
                            text_size 20
                            action Hide("cheats_screen"), Show("perk_cheats_screen")








                vbox:
                    hbox:
                        textbutton "Customise":
                            text_size 20
                            action Jump("surgery_screen_cheat")
                    hbox:
                        textbutton "Impregnante":
                            text_size 20
                            action Function(player.preg, unknown)

                    hbox:
                        textbutton "Advance pregnancy":
                            text_size 20
                            action Function(player.cheat_preg_day)

                    hbox:
                        textbutton "Impregnante npc's":
                            text_size 20
                            action Function(cheat_preg_all_npc)

                    hbox:
                        textbutton "Toggle debug":
                            text_size 20
                            if cheats == 0:
                                action SetVariable("cheats", 1)
                            else:
                                action SetVariable("cheats", 0)
                    hbox:
                        textbutton "Toggle avatar":
                            text_size 20
                            if renpy.get_screen("pc_avatar", layer="pc_avatar"):
                                action Function(renpy.hide_screen, "pc_avatar", layer="pc_avatar")
                            else:
                                action Function(renpy.show_screen, "pc_avatar", _layer="pc_avatar")
                    hbox:
                        textbutton "Wardrobe restricted [wardrobe_restricted]":
                            text_size 20
                            action Function(cheat_unrestrict_wardrobe)
                    hbox:
                        textbutton "Add clothes":
                            text_size 20
                            action Function(cheat_clothes)

                    hbox:
                        textbutton "Add items":
                            text_size 20
                            action Function(item_add_all)

                    hbox:
                        textbutton "Bukake":
                            text_size 20
                            action Function(player.cheat_bukake)

                    hbox:
                        textbutton "Shower":
                            text_size 20
                            action Function(player.shower)

                    hbox:
                        textbutton "Toggle makeup":
                            text_size 20
                            if acc.makeup_on == True:
                                action SetVariable("acc.makeup_on", False)
                            else:
                                action SetVariable("acc.makeup_on", True)
                    hbox:
                        textbutton "Pregnancy enabled [cheat_pregnancy_enabled]":
                            text_size 20
                            action Function(cheat_toggle_pregnancy)

                    hbox:
                        textbutton "Danger days [danger_content]":
                            text_size 20
                            action SetVariable("danger_content", If(danger_content, False, True))
                    hbox:
                        textbutton "Danger limit [danger_day_limit]":
                            text_size 20
                            action SetVariable("danger_day_limit", If(danger_day_limit, False, True))

                    hbox:
                        textbutton "Pregnancy [global_pregnancy_length] days":
                            text_size 20
                            action Function(pregnancy_length_cheat)

                    hbox:
                        textbutton "Cumflation [cheat_fetish_cumflation]":
                            text_size 20
                            action SetVariable("cheat_fetish_cumflation", If(cheat_fetish_cumflation, False, True))

                    hbox:
                        textbutton "Preg fantasy [cheat_fetish_preg_fantasy]":
                            text_size 20
                            action SetVariable("cheat_fetish_preg_fantasy", If(cheat_fetish_preg_fantasy, False, True))

                    hbox:
                        textbutton "PUNCH":
                            text_size 20
                            action Function(player.punch, True)

                    hbox:
                        textbutton "SPANK":
                            text_size 20
                            action Function(player.spank)


                vbox:

                    hbox:
                        textbutton "Jump to Haven":
                            text_size 20
                            if not (loc_cur in district_haven or renpy.get_screen("say") or renpy.get_screen("choice") or renpy.get_screen("qlog") or _windows_hidden):
                                action Jump("main_quest_05_cheatjump")
                            else:
                                action Function(NullAction())
                    hbox:
                        text "Dance stage [school_dance_quest_show_count]" size 20
                        textbutton "+1":
                            text_size 20
                            action Function(school_dance_quest_show_count_cheat,1)
                        textbutton "-1":
                            text_size 20
                            action Function(school_dance_quest_show_count_cheat,-1)

                    hbox:
                        textbutton "Jump to Dance":
                            text_size 20
                            action Jump("school_dance_show_picker_cheat")
                    hbox:
                        textbutton "VIP party":
                            text_size 20
                            action Jump("dance_party_vip_cheat")
                    hbox:
                        textbutton "Robin sex object":
                            text_size 20
                            action Jump("robin_talk_sexobject_bought_intro")
                    hbox:
                        textbutton "Mira quest":
                            text_size 20
                            action Jump("quest_mira_missing_debug_picker")
                    hbox:
                        textbutton "Bully event":
                            text_size 20
                            action Jump("random_event_school_bully")

                    hbox:
                        textbutton "Soccer boys talk":
                            text_size 20
                            action Jump("school_field_soccer_hangout")

                    hbox:
                        textbutton "Photography quest":
                            text_size 20
                            action Jump("school_photo_intro_cheat")
                    hbox:
                        textbutton "Group shower":
                            text_size 20
                            action Jump("school_field_soccer_play_end_shower")
                    hbox:
                        textbutton "Soccer sex offer":
                            text_size 20
                            action Jump("school_field_soccer_sex_offer_cheat")
                    hbox:
                        textbutton "Bully sex scenes":
                            text_size 20
                            action Jump("school_bully_bully_event_force_cheat")
                    hbox:
                        textbutton "Pub rep sex":
                            text_size 20
                            action Jump("pub_waitress_work_sex_debug")
                    hbox:
                        textbutton "First mission":
                            text_size 20
                            action Jump("main_quest_01_reporter_start_cheat")
                    hbox:
                        textbutton "Gloryhole start":
                            text_size 20
                            action Jump("gloryhole_event_cheat")
                    hbox:
                        textbutton "Flatmates cheat":
                            text_size 20
                            action Jump("flatmate_cheat")
                    hbox:
                        textbutton "Landlord office sex":
                            text_size 20
                            action Jump("oskar_sex_debug")
                    hbox:
                        textbutton "Cleaner rep sex":
                            text_size 20
                            action Jump("action_clean_event_sex_debug")

                    hbox:
                        textbutton "Gangbang/group sex":
                            text_size 20
                            action Jump("whore_street_sex_group_start")
                vbox:

                    hbox:
                        textbutton "Park bitch":
                            text_size 20
                            action Jump("wolfgang_cheat")
                    hbox:
                        textbutton "Exhib start":
                            text_size 20
                            action Jump("rachel_talk_exhib_cheat")

screen perk_cheats_screen():
    frame:
        yalign 0.25
        xalign 0.4
        xysize (1500, 900)
        has hbox
        vbox:
            textbutton "CLOSE PERK MENU":
                text_size 30
                action Hide("perk_cheats_screen")

            hbox:


                vbox:
                    box_wrap True
                    for i in perk_list:
                        hbox:
                            text i.name size 20
                            textbutton "+":
                                text_size 20
                                action Function(player.add_perk, i)
                            textbutton "-":
                                text_size 20
                                action Function(player.remove_perk, i)

label new_sex_scenes:
    "Here I will show off any scenes that I have drawn but haven't made it into a story yet."

    show gh_blow_behind no_man_hole with dissolve
    "Empty..."
    show gh_blow_behind man_hole with dissolve
    "Ah, someone is there..."
    show gh_blow_behind suck with dissolve
    $ c.outfit = 6
    $ c.pants = 6
    "If you are in your pub gear, the image will reflect that"
    $ c.pants = 0
    "No pants."
    show gh_blow_behind dani_hump with dissolve
    "Dani can come and tease you a bit."
    "Or even Trixie"
    show gh_blow_behind trixie with dissolve
    "She can help one of you out..."
    show gh_blow_behind trixie_dani with dissolve
    pause 1.0
    show gh_blow_behind trixie_pc with dissolve
    "Or both"
    show gh_blow_behind trixie_both with dissolve
    "Oh no, some guy invited himself."
    show gh_blow_behind dani_poke trixie with dissolve
    "Trixie can also help him out as well..."
    show gh_blow_behind trixie_rub with dissolve
    "The guy can fuck sammy or dani."
    show gh_blow_behind dani_sex with dissolve
    pause 1.0
    show gh_blow_behind vagpoke with dissolve
    pause 1.0
    show gh_blow_behind vagsex with dissolve
    pause 1.0
    show gh_blow_behind asspoke with dissolve
    pause 1.0
    show gh_blow_behind asssex with dissolve
    pause 1.0
    show gh_blow_behind dani_poke with dissolve
    pause 1.0
    show gh_blow_behind dani_sex with dissolve
    "If dani is shit drunk and ends up getting fucked senseless, then the worst happens and he losing control of her faculties."
    show gh_blow_behind dani_pee with dissolve
    pause 1.0
    hide gh_blow_behind with dissolve
    show gh_blow_close no_man_hole with dissolve
    "No man"
    show gh_blow_close man_hole with dissolve
    "Man"
    show gh_blow_close lick with dissolve
    "Getting started."
    show gh_blow_close suck with dissolve
    "Going at it."
    show gh_blow_close cum with dissolve
    "Scene for when he cums"
    "But not yet, Sammy wants more..."
    show gh_blow_close no_pc with dissolve
    pause 0.5
    show gh_blow_close vagpoke with dissolve
    pause 1.0
    show gh_blow_close vagsex with dissolve
    pause 1.0
    show gh_blow_close asspoke with dissolve
    pause 1.0
    show gh_blow_close asssex with dissolve
    pause 1.0
    hide gh_blow_close with dissolve
    show gh_blow_behind man_hole with dissolve
    "This scene I am currently drawing sex variants. But they are not done yet."
    show gh_blow_behind dani_suck with dissolve
    "Catching dani."
    show gh_blow_behind idle with dissolve
    "Whats sammy gonna do?"
    show gh_blow_behind mast with dissolve
    "help her out of course"
    show gh_blow_behind man_mast with dissolve
    "Uh oh?"
    show gh_blow_behind no_man no_dani with dissolve
    "Did they leave together?"
    "Oh well, sammy all alone. The insertion images for this will be the more zoomed in version."
    show gh_blow_close vagpoke with dissolve
    "This one"
    hide gh_blow_close with dissolve
    "She can stand"
    show gh_blow_behind sex_stand with dissolve
    "Bend over"
    show gh_blow_behind sex_down with dissolve
    "Or something in between"
    show gh_blow_behind sex_up with dissolve
    "..."
    show gh_blow_behind sex_stand dani_stand with dissolve
    "Dani can also catch Sammy"
    show gh_blow_behind sex_stand dani_lick with dissolve
    "And of course help her out."
    "I will probably make at some point versions with Trixie, Rachel and whoever else might be fitting."
    hide gh_blow_behind with dissolve
    "These next scenes are huge dance questline spoilers. You might not want to see them."
    menu:
        "I want to see them.":
            $ NullAction()
        "Take me away, I do not want to see them.":

            jump travel
    "These scenes are for the party with the dance girls. Depending on what you get up to, you might see what some of the other girls are up to."
    show dance_dani_group with dissolve
    "Here we have Dani fully embracing becoming a whore. She needs the money and this party has become very lucrative for her."
    "Depending on Sammys stats, this may be the first time she realised what is going on. Of course it is heavily hinted at throughout the story so the player will already know at this point."
    hide dance_dani_group with dissolve
    show dance_anabel_behind with dissolve
    "Anabel seems to be having fun here. She is completely wasted and gets caught up in the naughty vibes from the other girls."
    "This is probably her first time having sex and is part of the reason she reacts like she does after this story event."
    hide dance_anabel_behind with dissolve
    show dance_svet_buk with dissolve
    "Svet being a prudent one and not having actual sex. But it doesn't seem like her friends are too bothered."
    hide dance_svet_buk with dissolve
    show dance_rachel_dp with dissolve
    "With Rachel, you are not even sure if she is doing it for the money or for the fun of it."
    show dance_rachel_dp look with dissolve
    rachel.name "Fun!!"
    $ renpy.scene()
    with dissolve
    jump travel

label new_polaroid_scenes:
    "This is a test showing the new polaroid images."
    $ show_activity_image("soccer")
    "Currently there are 3 variations here. Play the scene again to get a new one."
    "Sammy plays ball or something"
    $ renpy.scene()
    with dissolve
    "Then finishes up and goes about her day"
    "*NOTE* If I do end up adding these, they will be a collectable and once shown will be added to your photo collection."
    "If i do add it, it will probably be expanded to give a memorabilia photo for all major actions Sammy takes."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
