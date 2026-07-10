label action_exercise_vball:
    if not "beach_vball_asked" in loc_beach_gym.list:
        jump loc_beach_vball_ask_join
    if not "beach_vball_nude_asked" in loc_beach_gym.list and people_nude_beach_vball():
        jump loc_beach_vball_nude_join

    $ player.can_sport(pregnant=True, drunk=If(people_nude_beach_vball(), True, False))

    if people_nude_beach_vball():
        if not c.nude:
            pcm "I should undress..."
            $ pc_strip(temp=True)

    elif not ("swim" in tab_top or c.nude):
        if not c.nude:
            pcm "I should change into something better before playing."
            jump travel

    $ player.face_exercise()
    $ vball_image()
    "I join the girls to play some volleyball."

    jump expression WeightedChoice([
    ("action_exercise_vball_normal", 300),
    ("action_exercise_vball_people", If(npc_any_here(exclude=mason), 300, 0)),
    ("action_exercise_vball_nude", If (c.nude, 200,0)),
    ("action_exercise_vball_male", If (player.has_perk(perk_male), (-player.body_conf), 0)),
    
    
    ("action_exercise_vball_allure", (player.allure / 4)),
    ("action_exercise_vball_fitness", If (player.fitness >= 30, player.fitness * 2,0)),
    ("action_exercise_vball_unfit", If (player.fitness < 30, (100 - player.fitness * 2),0)),
    
    ("action_exercise_vball_fat", If (player.isfat, 200,0)),
    
    
    ])

label action_exercise_vball_end:
    $ player.face_exercise()
    $ exercise(60)
    $ dialouge = renpy.random.choice([
    "Thanks, I'm gonna sit for a bit.",
    "*Phew* I'm gonna take a rest.",
    "Hah, that was fun.",
    "*Phew*",
    "Better take a sit down."
    ])
    pc "[dialouge]"
    $ renpy.scene()
    with dissolve
    $ player.face_normal()
    if mason_here() and t.hour in [2,3] and not "walked_home" in mason.list:
        jump loc_beach_vball_nude_walkhome
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
