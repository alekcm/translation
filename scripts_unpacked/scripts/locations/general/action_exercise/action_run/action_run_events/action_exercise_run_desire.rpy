label action_exercise_run_desire:
    jump expression WeightedChoice([
    ("action_exercise_run_desire_1", 100),
    ("action_exercise_run_desire_2", 100),
    ("action_exercise_run_desire_3", 100),
    ("action_exercise_run_desire_4", If (player.has_perk(perk_exhibitionist), 100, 0)),
    ("action_exercise_run_desire_5", 100),
    ])

label action_exercise_run_desire_1:
    pc "Hmmmm, running around like this is kinda making me feel a bit hot..."
    $ player.add_desire(3)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_desire_2:
    "During my run, I decide to stop near a group of guys and bend over while pretending to tighten my laces."
    $ player.face_happy()
    pc "Heh."
    if c.skirt and c.pantsless:
        if player.has_perk(perk_exhibitionist):
            pcm "No knickers on either. They can probably see everything."
        else:
            pcm "Oh shit, I forgot what I am wearing. They can probably see everything..."
            pcm "Not that I really care~~"
        $ player.add_desire(8)
        $ player.add_conf(1)
    $ player.add_desire(5)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_desire_3:
    if c.skirt:
        "During my run, I decide to slow my pace and make sure to rock my hips in a rhythm, making sure my skirt rocks with my hips."
        pcm "I wonder if anyone will get a peek?"
        if c.pantsless:
            pcm "Although maybe I should be a bit more careful. They might get to see everything."
    elif c.ass:
        "During my run, I decide to slow my pace and add some more bounce to my steps."
        pcm "Getting a good view?"
    else:
        "During my run, I decide to slow my pace and run in a more seductive way."
        pcm "Nothing wrong with a little tease is there~?"
    $ player.add_desire(5)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_desire_4:
    $ player.face_worried()
    pc "Anyone around...?"
    pc "Doesn't look like it..."
    $ c.top = 0
    $ player.mouth = 4
    pc "Whoo."
    $ c.bra = 0
    pc "Fresh air~~~~~"
    $ player.face_happy()
    pc "Hehehe."
    $ pc_dress()
    $ player.add_desire(5)
    $ player.add_conf(1)
    jump action_exercise_run_end

label action_exercise_run_desire_5:
    if c.skirt:
        pcm "Running around with this skirt flapping around is kinda making me feel a bit hot..."
        pcm "And pretty cool come to think of it, the breeze coming up my legs is lovely and refreshing."
        $ player.add_mood(4)
    elif c.clevage:
        pcm "Running around with my chest so open is kinda making me feel a bit hot..."
        pcm "And pretty cool come to think of it, the breeze is lovely."
        $ player.add_mood(3)
    elif c.belly:
        pcm "Running around with belly so open is kinda making me feel a bit hot..."
        pcm "And pretty cool come to think of it, the breeze is lovely."
        $ player.add_mood(2)
    elif c.ass:
        pcm "Running around with these bottoms showing off my ass is kinda making me feel a bit hot..."
    else:
        pcm "Running around being all sweaty is kinda making me feel a little bit hot..."
        pcm "Although maybe it's just the clothes. These things cover everything."
        $ player.add_mood(-2)
    $ player.add_desire(3)
    $ player.add_conf(1)
    jump action_exercise_run_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
