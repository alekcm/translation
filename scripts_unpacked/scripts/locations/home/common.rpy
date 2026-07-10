label common_screen:

    call screen travel_screen


label common_arrival:
    $ walk(False, "common", 1)
    $ loc_home = True

    $ arrival()

    if player.mood <= 20:
        $ player.mouth = 3
        pc "Ah, the TV will surely cheer me up!"
        $ player.mouth = 1
        jump common_tv

    jump common_screen


label common_tv:
    if player.tired <= 15:
        $ randomnum = renpy.random.randint(1,5)
        if randomnum == 1:
            "I lay on the sofa and relax watching some TV"
            $ player.eye = 3
            $ time_sleep(numgen(30,120))
            "...zzzZZZzz..."
            $ player.eye = 1
            $ player.brow = 3
            $ player.mouth = 9
            pc "Ugh, I probably should have went to bed instead."

            $ player.face_normal()
            jump common_screen

    "I spend some time relaxing on the sofa watching the TV."
    $ relax(20)
    $ player.add_mood(2)



    jump common_screen

label common_sport:

    if player.tired < 15:
        $ player.face_sad()
        $ dialouge = renpy.random.choice([
        "I'm so tired. It's probably not a good idea to do any exercise now.",
        "I'm ready to fall asleep on my feet. Doing some exercise is not a good idea.",
        "Exercise while as tired as I am will just lead to me face planting. I had better just sleep",
        "Struggling to keep my eyes open so no chance am I exercising.",
        "I haven't managed to master sleep exercise just yet so I think I will pass on doing anything right now."
        ])
        pcm "[dialouge]"
        $ player.face_normal()
        jump travel
    elif player.fitness < 35 and player.mood < 10:
        $ player.face_sad()
        $ dialouge = renpy.random.choice([
        "I'm not in the mood to be exercising. I'd rather just watch TV.",
        "I don't feel like exercising right now. Would prefer to do something to lift my mood.",
        "Ugh no. Exercising now will just upset me even more than I am already",
        "I'm not in the mood for exercising.",
        "No, just no. I am not in the mood for exercising right now."
        ])
        pcm "[dialouge]"
        $ player.face_normal()
        jump travel
    if any(clothes in ["school", "home"] for clothes in tab_top):
        if home.inappropriate == False:
            "I quickly head off to change before working out."
            $ pc_dress_event("home", loc_bedroom, loc_common)
        elif sport.inappropriate == False:
            "I quickly head off to change before working out."
            $ pc_dress_event("sport", loc_bedroom, loc_common)
        else:
            pcm "I need to change into something I can exercise in first."
            jump common_screen
    if player.pregnancy >= 2:
        $ dialouge = renpy.random.choice([
        "Since I am pregnant, I should stick to light exercises.",
        "I should take it easy since I have this belly.",
        "Need to take it easy with this fat belly."
        ])
        pcm "[dialouge]"
    $ player.face_exercise()
    "I put the TV to recordings of old fitness channels and follow one of the routines."
    $ exercise(60)
    pc "Phew."
    $ player.face_normal()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
