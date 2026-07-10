label action_exercise_run:
    if loc(loc_school_field) and not school_field_running_intro:
        $ school_field_running_intro = True
        pcm "Looks like there is a running track going around the soccer pitch. I could go for a run after school to get in better shape."
        jump travel




    $ player.can_sport(pregnant=True)

    if not "sport" in tab_top and not (loc_cur in dis_beach.locs):
        if not sport.inappropriate:
            pcm "I am not wearing my sports outfit. Should I try and change somewhere so I can go for a run?"
            menu:
                "Find somewhere to change":
                    "I look around for a secluded place to change. After finding somewhere I change into my sports clothes."
                    if loc(loc_school_field):
                        $ pc_dress_event("sport", If(loc_school_locker_old.unlocked, loc_school_locker_old, If(loc_school_locker_girls.open(), loc_school_locker_girls, loc_cur.isolate_loc)), loc_cur)
                    else:
                        $ pc_dress_event("sport", where2=loc_cur)
                    jump action_exercise_run
                "I had better not.":
                    jump travel
        else:
            pcm "I need to change into my sports outfit before I can do any running. I can't really wear the one I have picked out."
            jump travel
    else:
        $ player.face_exercise()
        if loc(loc_park):
            "I go for a run around the park."
        elif dis(dis_beach):
            "I go for a run along the beach."
        elif loc(loc_school_field):
            "I go for a run around the field."

        jump expression WeightedChoice([
        ("action_exercise_run_normal", 300),
        ("action_exercise_run_braless", If (c.braless and player.breasts > 1, 200,0)),
        ("action_exercise_run_male", If (player.has_perk(perk_male), (-player.body_conf), 0)),
        ("action_exercise_run_desire", player.check_horny()),
        
        ("action_exercise_run_allure", player.allure),
        ("action_exercise_run_fitness", If (player.fitness >= 30, player.fitness * 2,0)),
        ("action_exercise_run_unfit", If (player.fitness < 30, (100 - player.fitness * 2),0)),
        ("action_exercise_run_conf", (player.confidence / 2)),
        ("action_exercise_run_fat", If (player.isfat, 200,0)),
        ("action_exercise_run_dark", If (t.hour in dark and not dis(dis_school), 200,0)),
        ("action_exercise_run_soccerboys", If (loc(loc_school_field) and nate.love > 5 and school_soccer_hangingout(), 100,0)),
        ])


label action_exercise_run_end:
    $ player.face_exercise()
    $ exercise(60)
    $ show_activity_image("running")
    $ dialouge = renpy.random.choice([
    "I make my way back to where I started and have a bit of a rest to catch my breath.",
    "I stand around to catch my breath before moving on.",
    "I decide to rest a bit before moving on.",
    "After resting up to catch my breath, I decide to move on.",
    "I make my way back to where I started and have a bit of a rest before going about my day."
    ])
    "[dialouge]"
    $ player.face_normal()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
