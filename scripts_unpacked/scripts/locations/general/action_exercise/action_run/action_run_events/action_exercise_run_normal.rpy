label action_exercise_run_normal:
    jump expression WeightedChoice([
    ("action_exercise_run_normal_1", 100),
    ("action_exercise_run_normal_2", If (weather_var == 1, 100, 0)),
    ("action_exercise_run_normal_3", 100),
    ("action_exercise_run_normal_4", If (not dis(dis_school), 100, 0)),
    ("action_exercise_run_normal_5", 100),
    ("action_exercise_run_normal_6", If (not dis(dis_school), 100, 0)),
    ("action_exercise_run_normal_7", If (not dis(dis_school), 100, 0)),
    ("action_exercise_run_normal_8", 100),
    ("action_exercise_run_normal_9", 100),
    ("action_exercise_run_normal_10", If (loc(loc_park), 100, 0)),
    ("action_exercise_run_normal_11", 100),
    ("action_exercise_run_normal_12", If (loc(loc_park) and t.hour in workhours, 100, 0)),
    ("action_exercise_run_normal_13", 100),
    ("action_exercise_run_normal_14", 100),
    ("action_exercise_run_normal_15", If (not dis(dis_school), 100, 0)),
    ("action_exercise_run_normal_16", 100),
    ("action_exercise_run_normal_17", 100),
    ])

label action_exercise_run_normal_1:
    $ player.face_happy()
    pc "This is nice."
    $ player.add_mood(5)
    jump action_exercise_run_end

label action_exercise_run_normal_2:
    $ player.face_happy()
    pc "Uff, such lovely weather."
    $ player.add_mood(4)
    jump action_exercise_run_end

label action_exercise_run_normal_3:
    "There is a lovely breeze keeping me cool as I run"
    $ player.add_mood(4)
    jump action_exercise_run_end

label action_exercise_run_normal_4:
    "As I am running I pass a cute couple walking hand in hand."
    pcm "Awww."
    if player.has_perk([perk_gamine, perk_whore]):
        pcm "Hope they are together and she's not being paid to be there."
    $ player.add_mood(4)
    jump action_exercise_run_end

label action_exercise_run_normal_5:
    pcm "One two one two one two..."
    pcm "Would be a lot nicer if I was able to listen to music."
    $ player.add_mood(2)
    jump action_exercise_run_end

label action_exercise_run_normal_6:
    "As I am running, I have to slow down and make a detour because of people blocking my path."
    pcm "Damn, move out the way!"
    $ player.add_mood(-3)
    jump action_exercise_run_end

label action_exercise_run_normal_7:
    "As I am running, a cute guy running the opposite way smiles at me."
    $ player.face_happy()
    $ player.add_mood(4)
    $ player.add_desire(2)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_normal_8:
    "As I am running a fly gets in my eye and I have to stop and try and get it out."
    $ player.eye = 3
    pc "Ugh!"
    $ player.add_mood(-3)
    jump action_exercise_run_end

label action_exercise_run_normal_9:
    "As I am running, I step into some type of hole I couldn't see and almost fall over."
    with vpunch
    $ player.face_angry()
    pc "Ugh!"
    $ player.add_mood(-3)
    jump action_exercise_run_end

label action_exercise_run_normal_10:
    "As I am running I almost stomp all over some drunk who decided to just sleep on the floor."
    $ player.face_angry()
    pcm "Stupid idiot!"
    $ player.add_mood(-3)
    jump action_exercise_run_end

label action_exercise_run_normal_11:
    "As I am running my shoe almost falls off and I have to stop and tie my laces."
    pcm "Uff, annoying"
    $ player.add_mood(-3)
    jump action_exercise_run_end

label action_exercise_run_normal_12:
    "There are so few people in the park right now and I manage to have an uneventful run."
    pcm "So much nicer when there is no one to get in my way."
    $ player.add_mood(4)
    jump action_exercise_run_end

label action_exercise_run_normal_13:
    "As I am running I end up running alongside a group of joggers and exchanging small talk."
    pcm "That was nice. I wonder if I should join a club or something."
    pcm "Are there such clubs for this these days?"
    $ player.add_mood(6)
    jump action_exercise_run_end

label action_exercise_run_normal_14:
    "As I am running I notice other people are running in small groups."
    pcm "Hmm... I wonder if [emile.name] will join me?"
    $ player.add_mood(6)
    jump action_exercise_run_end

label action_exercise_run_normal_15:
    "As I am running I look around at others who are going about their lives."
    pcm "The world has changed but people still go about their lives. Not much else to do."
    $ player.add_mood(5)
    jump action_exercise_run_end

label action_exercise_run_normal_16:
    "As I am running, I almost run straight into some staggering drunk."
    pc "Uff."
    $ player.add_mood(-4)
    jump action_exercise_run_end

label action_exercise_run_normal_17:
    "As I am running, I pass a man who hands a flower out to me."
    $ player.face_happy()
    pc "Thanks!"
    $ player.face_normal()
    pcm "Probably just something he picked out of the bushes. Well, nice anyway."
    $ player.add_mood(5)
    jump action_exercise_run_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
