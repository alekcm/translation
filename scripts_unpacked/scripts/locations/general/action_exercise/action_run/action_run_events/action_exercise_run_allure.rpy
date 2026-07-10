label action_exercise_run_allure:
    jump expression WeightedChoice([
    ("action_exercise_run_allure_1", 100),
    ("action_exercise_run_allure_2", 100),
    ("action_exercise_run_allure_3", 100),
    ("action_exercise_run_allure_4", 100),
    ("action_exercise_run_allure_5", 100),
    ("action_exercise_run_allure_6", If (c.ass, 100, 0)),
    ])

label action_exercise_run_allure_1:
    if c.ass:
        guy "Nice ass babe, come back round here so I can get a better look."
    elif c.skirt and (c.thong or c.pantsless):
        guy "Nice ass babe. Lift that skirt higher so I can get a better look!"
    else:
        guy "Keep shaking those hips baby!"
    $ player.face_shy()
    pc "..."
    $ player.add_desire(10)
    jump action_exercise_run_end

label action_exercise_run_allure_2:
    if c.clevage and c.braless:
        guy "Damn sugar tits. Bounce your way over here and I will free them for you!"
    elif c.clevage:
        guy "Hey sexy. Let me put my face between those sweaty tits of yours!"
    elif c.braless:
        guy "Hey sugar tits! Take your top off and let us see how much they really bounce!"
    else:
        guy "Keep bouncing those tits baby!"
    $ player.face_shy()
    pc "..."
    $ player.add_desire(10)
    jump action_exercise_run_end

label action_exercise_run_allure_3:
    "I am feeling quite confident in myself while running. The time spent to look good is paying off."
    $ player.add_desire(10)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_allure_4:
    "I am feeling quite confident in myself while running so I decide to go at a slower pace and shake my hips a bit more than usual"
    $ player.add_desire(10)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_allure_5:
    guy "Hey baby, show us your tits!"
    if player.has_perk([perk_exhibitionist, perk_bimbo, perk_slut], notif=True) or player.check_sex_agree(3):
        pcm "He is a crude arse, but he is pretty good looking..."
        menu:
            "Flash him":
                $ player.face_happy()
                $ pc_strip_tops()
                pc "You like?"
                guy "Oooh sexy baby!"
                $ player.mouth = 1
                guy "Come over and give is a closer look."
                if player.check_sex_agree(4):
                    menu:
                        "Give him a closer look.":
                            pc "Ok, but take it easy."
                            show sb_pose_showbreasts with dissolve
                            guy "Damn girl, they are hot, why not give 'em a shake?"
                            pc "You dirty boy..."
                            guy "You know it!"
                            show sb_pose_showbreasts happy
                            pc "You like?"
                            guy "Ohh baby. Such a sexy girl."
                            show sb_pose_showbreasts tounge
                            pc "Thats all you are getting today handsome."
                            hide sb_pose_showbreasts with dissolve
                            $ pc_dress()
                            guy "Awwww."
                            $ player.add_desire(20)
                            $ player.add_conf(2)
                            jump action_exercise_run_end
                        "Keep jogging":

                            $ NullAction()

                pc "Thats all you are getting today handsome."
                $ pc_dress()
                guy "Awwww."
                $ player.add_desire(20)
                $ player.add_conf(2)
                jump action_exercise_run_end
            "Ignore him":

                $ NullAction()

    pcm "Idiot!"
    pcm "Kinda nice to be desired though..."
    $ player.add_desire(10)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_allure_6:
    guy "Hey sexy. Nice arse!"
    $ player.face_shy()
    $ player.add_desire(10)
    $ player.add_conf(1)
    jump action_exercise_run_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
