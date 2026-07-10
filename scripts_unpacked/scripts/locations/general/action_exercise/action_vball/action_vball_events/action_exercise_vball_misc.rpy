



label action_exercise_vball_nude:
    jump expression WeightedChoice([
    ("action_exercise_vball_nude_1", 100),
    ("action_exercise_vball_nude_2", 100),
    ("action_exercise_vball_nude_3", 100),
    ("action_exercise_vball_nude_4", 100),
    ])

label action_exercise_vball_nude_1:
    pc "Kinda fun playing naked, but damn sand is getting everywhere."
    jump action_exercise_vball_end

label action_exercise_vball_nude_2:
    pcm "Tits are bouncing all over the place playing like this."
    pcm "Kind of the point I guess."
    jump action_exercise_vball_end

label action_exercise_vball_nude_3:
    guy "Nice tits! Bounce them around some more for us will ya?"
    if player.has_perk([perk_exhibitionist, perk_bimbo, perk_slut], notif=True):
        $ player.face_happy()
        pc "Like them do you?"
        guy "Love em!"
        pc "Heh."
    else:
        $ player.face_worried()
        pc "Whaaa!"
    jump action_exercise_vball_end

label action_exercise_vball_nude_4:
    $ player.face_worried()
    pc "Feels like there are a lot more people watching me play more than usual..."
    jump action_exercise_vball_end





label action_exercise_vball_male:
    jump expression WeightedChoice([
    ("action_exercise_vball_male_1", 100),
    ("action_exercise_vball_male_2", If (player.breasts == 3, 100, 0)),
    ("action_exercise_vball_male_3", 100),
    ("action_exercise_vball_male_4", 100),
    ])

label action_exercise_vball_male_1:
    pcm "This is much harder than I thought it would be. This body gets tired a lot quicker."
    jump action_exercise_vball_end

label action_exercise_vball_male_2:
    pcm "These huge tits make it pretty hard to play. They bounce around like they have a life of their own."
    jump action_exercise_vball_end

label action_exercise_vball_male_3:
    pcm "Nothing between my legs any more. Wonder if that makes it easier or harder to play?"
    jump action_exercise_vball_end

label action_exercise_vball_male_4:
    pcm "No one paid any attention to me when I was a guy. But running around the beach like this I seem to get all sorts of looks."
    jump action_exercise_vball_end





label action_exercise_vball_fitness:
    jump expression WeightedChoice([
    ("action_exercise_vball_fitness_1", 100),
    ("action_exercise_vball_fitness_2", 100),
    ("action_exercise_vball_fitness_3", 100),
    ("action_exercise_vball_fitness_4", 100),
    ("action_exercise_vball_fitness_5", 100),
    ])

label action_exercise_vball_fitness_1:
    pcm "Feels good to play and let off some stress."
    jump action_exercise_vball_end

label action_exercise_vball_fitness_2:
    pcm "Ahh, was horrible in the beginning but now that I've managed to build some stamina, playing like this is really fun."
    jump action_exercise_vball_end

label action_exercise_vball_fitness_3:
    pcm "Feel good to get the blood pumping like this."
    jump action_exercise_vball_end

label action_exercise_vball_fitness_4:
    if player.has_perk(perk_male):
        pcm "Feels good to have decent fitness like I had in my old life. Starting out fat in this body was a bit of a chore."
        pcm "What was that quote I read? \"Take care of your body, It's your only home you have\" or some such. Not quite true In my case, but I shouldn't let my second chance go to waste."
    else:
        pcm "Feel good to get the blood pumping like this. Don't really remember how fit or slim I was before."
        pcm "What was that quote I read? \"Take care of your body, It's your only home you have\" or some such. Not quite true In my case, but I shouldn't let my second chance go to waste."
    jump action_exercise_vball_end

label action_exercise_vball_fitness_5:
    if player.has_perk(perk_male):
        pcm "Starting out as a woman, and a bit fat a that, was hard. But I feel so much better now that I am stronger and fitter than before."
    else:
        pcm "Feel good to get the blood pumping like this."





label action_exercise_vball_unfit:
    jump expression WeightedChoice([
    ("action_exercise_vball_unfit_1", 100),
    ("action_exercise_vball_unfit_2", 100),
    ("action_exercise_vball_unfit_3", 100),
    ("action_exercise_vball_unfit_4", 100),
    ])

label action_exercise_vball_unfit_1:
    pcm "Uff... Uff... I'm really not cut out for this..."
    jump action_exercise_vball_end

label action_exercise_vball_unfit_2:
    pcm "Ugh, this is horrible..."
    jump action_exercise_vball_end

label action_exercise_vball_unfit_3:
    pc "Ufff... Ufff... Ufffff..."
    guy "Keep it up girl!"
    $ player.face_happy()
    pc "Ufff... Thanks..."
    jump action_exercise_vball_end

label action_exercise_vball_unfit_4:
    pc "Ufff... Ufff...."
    pcm "I'm gonna take a rest..."
    $ player.face_exercise()
    "I end up spending most of my time relaxing and not actually playing."
    $ player.face_normal()
    $ relax(60)
    jump travel





label action_exercise_vball_fat:
    jump expression WeightedChoice([
    ("action_exercise_vball_fat_1", 100),
    ("action_exercise_vball_fat_2", 100),
    ("action_exercise_vball_fat_3", 100),
    ("action_exercise_vball_fat_4", 100),
    ("action_exercise_vball_fat_5", 100),
    ])

label action_exercise_vball_fat_1:
    guy "Keep going you gutlord! You need it!"
    $ player.face_annoyed()
    pcm "Arsehole!"
    jump action_exercise_vball_end

label action_exercise_vball_fat_2:
    pc "Uff... Uff... Ufffff... "
    jump action_exercise_vball_end

label action_exercise_vball_fat_3:
    pc "Uff... People actually... Ufff... Do this for fun...?"
    jump action_exercise_vball_end

label action_exercise_vball_fat_4:
    guy "Keep going fatty! Don't let up! I believe in you."
    $ player.face_shy()
    pc "Err... Thanks...?"
    $ player.face_annoyed()
    pc "Arsehole."
    jump action_exercise_vball_end

label action_exercise_vball_fat_5:
    guy "Ohhh jigglebum! Go go go!"
    $ player.face_sus()
    pc "Fucker."
    jump action_exercise_vball_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
