label action_clean_event_general_1:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    jump action_clean_event_picker

label action_clean_event_public_1:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pervert "Hey [rlist.name_deg]. Come show your arse off in my flat when you're done there."
    pcm "Ugh..."
    pervert "I got lotsa stuff fer you ta clean."
    jump action_clean_event_picker

label action_clean_event_public_2:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    $ player.spank()
    pc "Ah!"
    pervert "Keep at it [rlist.name_deg]. I'm enjoying the show."
    pcm "Ugh..."
    jump action_clean_event_picker

label action_clean_event_public_3:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    guy "Someone actually cleanin' up 'round 'ere? Thought I'd never see the day."
    jump action_clean_event_picker

label action_clean_event_public_4:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    guy "Ya missed a spot there [rlist.name_cute]."
    pcm "Always got to make a comment..."
    jump action_clean_event_picker

label action_clean_event_public_5:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pervert "Come to my place [rlist.name_deg] so I can 'ave a closer look at those [rlist.name_breasts]."
    pcm "Ugh..."
    jump action_clean_event_picker

label action_clean_event_secluded_1:
    $ show_cleaning_image()

    "[rlist.clean_area_dialogue]"
    $ player.face_shock()
    if renpy.showing("sb_onfours"):
        show sb_onfours grope up with dissolve
    else:
        $ player.spank()

    pc "Aii!"
    if c.skirt and not c.pants:
        pervert "Damn you dirty [rlist.name_deg]. You looking to get fucked like this?"
    else:
        pervert "Nice one [rlist.name_deg]."
    if not player.has_perk(perk_freeuse):
        with hpunch
        pc "Go away!"
    else:
        pc "..."
    $ if_showing("sb_onfours", "noman")
    if not player.has_perk(perk_freeuse):
        pc "Idiot."

    if any(renpy.showing(i) for i in ("sb_doggy1","sb_doggy2","sb_onfours")):
        if (c.skirt and not c.pants and not numgen(0,10)) or not numgen(0,30):
            $ if_showing("sb_doggy1", "poke", "sb_doggy2", "pokevag", "sb_onfours", "poke")
            if not player.has_perk(perk_freeuse):
                pc "Ah! What are you doing!?"
                pervert "Clean this up [rlist.name_deg]."
                "He drops some money on the floor in front of me."
                pcm "Cunt!"
                if player.check_whore():
                    menu:
                        "Pick up the money":
                            $ tempname = streetpervert
                            $ player.set_whore_price(2)
                            if c.pants:
                                "I lean over and pick up the money from the floor while he lowers my knickers."
                                $ c.pants = 0
                            else:
                                "I lean over and pick up the money from the floor."
                            $ player.add_money(player.soldprice)
                            pervert "Thought so."
                            jump whore_street_sex_floor_vag_picker
                        "Get rid of him":

                            $ NullAction()
                pc "No, get off!"
                if danger_gen(50,1):
                    $ player.sex_forced(rapist)
                    pervert "Fuck you!"
                    pervert "C'mere bitch!"
                    hide sb_onfours with hpunch
                    $ player.grope_breasts()
                    pc "Ah!"
                    if player.check_fight(2):
                        $ player.sex_end()
                        $ player.grope_end()
                        $ player.face_angry()
                        with hpunch
                        "I manage to kick at the guy and get away from him. Instead of carrying on he runs off with his trousers round his legs."
                        pcm "Fucking hell. Just trying to clean and got cunts like him around..."
                        pc "Ugh..."
                        jump action_clean_event_picker
                    else:
                        jump random_event_generic_sex_force_bendover

                pervert "*Tsk* Bitch!"
                $ if_showing("sb_doggy1", "noman", "sb_doggy2", "noman" "sb_onfours", "noman")
            else:

                pc "Oh? Poking me?"
                $ renpy.scene()
                show sb_assup back poke
                with dissolve
                "I lean down and present my ass to the guy so he can easier fuck me."
                pervert "Wow, you really are looking to get fucked?"
                pc "I was going to get fucked anyway. Might as well have some fun if it's going to happen."
                pervert "Oh?"
                if not numgen(0,10):
                    show sb_assup noman
                    pcm "Huh? Did he just leave?"
                    pcm "..."
                    pcm "Seems so..."
                    hide sb_assup with dissolve
                    pcm "Wonder why?"
                    jump action_clean_event_picker
                show sb_assup back poke

        elif numgen(0,10):
            jump action_clean_event_sex_cumrun
    elif numgen(0,5):
        $ renpy.scene()
        show sb_standbehind
        with vpunch
        pc "Ah! What are you doing?"

    $ player.face_annoyed()
    $ renpy.scene()
    with dissolve
    if not player.has_perk(perk_freeuse):
        "I stand up and watch the man walk away making sure he doesn't try anything else."
        pc "Ugh..."
    else:
        pcm "Did he leave?"
    jump action_clean_event_picker

label action_clean_event_secluded_2:
    show sb_onfours with dissolve
    "[rlist.clean_area_dialogue]"
    jump action_clean_event_sex_cumrun
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
