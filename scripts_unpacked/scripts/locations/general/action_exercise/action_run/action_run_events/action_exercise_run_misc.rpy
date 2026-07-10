



label action_exercise_run_braless:
    jump expression WeightedChoice([
    ("action_exercise_run_braless_1", 100),
    ("action_exercise_run_braless_2", 100),
    ("action_exercise_run_braless_3", 100),
    ("action_exercise_run_braless_4", 100),
    ])

label action_exercise_run_braless_1:
    pc "This is harder than I thought it would be. I really should wear a bra."
    $ player.add_desire(10)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_braless_2:
    pc "This is harder than I thought it would be. I really should wear a bra."
    $ player.add_desire(10)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_braless_3:
    guy "Nice tits! Bounce them around some more for us will ya?"
    if player.has_perk([perk_exhibitionist, perk_bimbo], notif=True):
        $ player.face_happy()
        pc "Like them do you?"
        guy "Love em!"
        pc "Heh."
    else:
        $ player.face_worried()
        pc "Whaaa!"
    $ player.add_desire(10)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_braless_4:
    $ player.face_worried()
    pc "Feels like there are a lot more people watching me run than usual..."
    $ player.add_conf(1)
    $ player.add_desire(5)
    jump action_exercise_run_end





label action_exercise_run_soccerboys:
    jump expression WeightedChoice([
    ("action_exercise_run_soccerboys_1", 100),
    ("action_exercise_run_soccerboys_2", 100),
    ("action_exercise_run_soccerboys_3", 100),
    ("action_exercise_run_soccerboys_4", 100),
    ])

label action_exercise_run_soccerboys_1:
    pcm "Bet those perverts are drinking beer and watching me run."
    $ player.add_desire(5)
    jump action_exercise_run_end

label action_exercise_run_soccerboys_2:
    nate.name "Run [name]. Keep it up!"
    pcm "..."
    $ player.add_desire(5)
    jump action_exercise_run_end

label action_exercise_run_soccerboys_3:
    pc "You lazy not should be out here running with me!"
    nate.name "No thanks. Better drinking and watching you go!"
    pcm "..."
    $ player.add_desire(5)
    jump action_exercise_run_end

label action_exercise_run_soccerboys_4:
    pc "Stop watching me and stick to your beer!"
    nate.name "Can do both!"
    pcm "..."
    $ player.add_desire(5)
    jump action_exercise_run_end





label action_exercise_run_male:
    jump expression WeightedChoice([
    ("action_exercise_run_male_1", 100),
    ("action_exercise_run_male_2", If (player.breasts == 3, 100, 0)),
    ("action_exercise_run_male_3", 100),
    ("action_exercise_run_male_4", 100),
    ])

label action_exercise_run_male_1:
    pcm "This is much harder than I thought it would be. This body gets tired a lot quicker."
    jump action_exercise_run_end

label action_exercise_run_male_2:
    pcm "These huge tits make it pretty hard to run. They bounce around like they have a life of their own."
    jump action_exercise_run_end

label action_exercise_run_male_3:
    pcm "Nothing between my legs any more. Wonder if that makes it easier or harder to run?"
    jump action_exercise_run_end

label action_exercise_run_male_4:
    pcm "No one paid any attention to me when I was a guy. But running around I seem to get all sorts of looks."
    jump action_exercise_run_end





label action_exercise_run_fitness:
    jump expression WeightedChoice([
    ("action_exercise_run_fitness_1", 100),
    ("action_exercise_run_fitness_2", 100),
    ("action_exercise_run_fitness_3", 100),
    ("action_exercise_run_fitness_4", 100),
    ("action_exercise_run_fitness_5", 100),
    ])

label action_exercise_run_fitness_1:
    pcm "Feels good to go for a run and let off some stress."
    $ player.add_mood(2)
    jump action_exercise_run_end

label action_exercise_run_fitness_2:
    pcm "Ahh, was horrible in the beginning but now that I've managed to build some stamina a run like this is so invigorating."
    $ player.add_mood(2)
    jump action_exercise_run_end

label action_exercise_run_fitness_3:
    pcm "Feel good to get the blood pumping like this."
    $ player.add_mood(2)
    jump action_exercise_run_end

label action_exercise_run_fitness_4:
    if player.has_perk(perk_male):
        pcm "Feels good to have decent fitness like I had in my old life. Starting out fat in this body was a bit of a chore."
        pcm "What was that quote I read? \"Take care of your body, It's your only home you have\" or some such. Not quite true In my case, but I shouldn't let my second chance go to waste."
    else:
        pcm "Feel good to get the blood pumping like this. Don't really remember how fit or slim I was before."
        pcm "What was that quote I read? \"Take care of your body, It's your only home you have\" or some such. Not quite true In my case, but I shouldn't let my second chance go to waste."
    $ player.add_mood(4)
    jump action_exercise_run_end

label action_exercise_run_fitness_5:
    if player.has_perk(perk_male):
        pcm "Starting out as a woman, and a bit fat a that, was hard. But I feel so much better now that I am stronger and fitter than before."
    else:
        pcm "Feel good to get the blood pumping like this."





label action_exercise_run_unfit:
    jump expression WeightedChoice([
    ("action_exercise_run_unfit_1", 100),
    ("action_exercise_run_unfit_2", 100),
    ("action_exercise_run_unfit_3", 100),
    ("action_exercise_run_unfit_4", 100),
    ])

label action_exercise_run_unfit_1:
    pcm "Uff... Uff... I'm really not cut out for this..."
    jump action_exercise_run_end

label action_exercise_run_unfit_2:
    pcm "Ugh, this is horrible..."
    jump action_exercise_run_end

label action_exercise_run_unfit_3:
    pc "Ufff... Ufff... Ufffff..."
    guy "Keep it up girl!"
    $ player.face_happy()
    pc "Ufff... Thanks..."
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_unfit_4:
    pc "Ufff... Ufff...."
    pcm "I'm gonna take a rest..."
    $ player.face_exercise()
    "I end up spending most of my time relaxing and not actually running."
    $ player.face_normal()
    $ relax(60)
    jump travel





label action_exercise_run_fat:
    jump expression WeightedChoice([
    ("action_exercise_run_fat_1", 100),
    ("action_exercise_run_fat_2", 100),
    ("action_exercise_run_fat_3", 100),
    ("action_exercise_run_fat_4", 100),
    ("action_exercise_run_fat_5", 100),
    ])

label action_exercise_run_fat_1:
    guy "Keep running you gutlord! You need it!"
    $ player.face_annoyed()
    pcm "Arsehole!"
    jump action_exercise_run_end

label action_exercise_run_fat_2:
    pc "Uff... Uff... Ufffff... "
    jump action_exercise_run_end

label action_exercise_run_fat_3:
    pc "Uff... People actually... Ufff... Do this for fun...?"
    jump action_exercise_run_end

label action_exercise_run_fat_4:
    guy "Keep going fatty! Don't let up! I believe in you."
    $ player.face_shy()
    pc "Err... Thanks...?"
    $ player.face_annoyed()
    pc "Arsehole."
    jump action_exercise_run_end

label action_exercise_run_fat_5:
    guy "Ohhh jigglebum! Go go go!"
    $ player.face_sus()
    pc "Fucker."
    jump action_exercise_run_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
