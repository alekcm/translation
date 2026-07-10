label whore_street_sex_group_watch_robin_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_watch_robin_doubleblow", 100),
    ("whore_street_sex_group_watch_robin_spitroast", 100),
    ("whore_street_sex_group_watch_robin_prone", 100),
    ("whore_street_sex_group_watch_robin_onback", 100),
    ("whore_street_sex_group_watch_robin_doggy", 100),
    ])

label whore_street_sex_group_watch_robin_doubleblow:
    show robin_doubleblow with dissolve
    "I manage to take a look over and notice [robin.name] sucking off a couple of the guys."
    if not "mouth" in player.sex_holes or player.gagged:
        pc "Two cocks are better than one is it [robin.name]?"
        robin.name "[rlist.blowjob_muffle]"
        pc "You better swallow up what they give you."
        robin.name "[rlist.blowjob_muffle]"
    else:
        pc "[rlist.blowjob_muffle]"
        pcm "Both of us with some guys cock in our mouth."
    hide robin_doubleblow with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_watch_robin_spitroast:
    show robin_spitroast with dissolve
    "While entertaining my guys, I manage to look over and see [robin.name] taking it from both ends."
    if not "mouth" in player.sex_holes or player.gagged:
        pc "You are such a slut [robin.name]."
        robin.name "[rlist.blowjob_muffle]"
        pc "Two guys sticking you like a fat pig and you are loving it."
        robin.name "[rlist.blowjob_muffle]"
    else:
        pc "[rlist.blowjob_muffle]"
        pcm "I can't even trase the dirty girl with this cock in my mouth."
    hide robin_spitroast with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_watch_robin_prone:
    show robin_prone front with dissolve
    "I manage to look over to [robin.name] who looks like she has some guy riding her like a horse."
    if not "mouth" in player.sex_holes or player.gagged:
        robin.name "Like what you see?"
        pc "Mmmm, you laying there watching me?"
        robin.name "Of course. Fuck to watch you get fucked for once."
        pc "Well, enjoy it while the guys last."
    else:
        robin.name "Like what you see?"
        pc "[rlist.blowjob_muffle]"
        robin.name "Thats right, take it down your mouth. Just shit up and get fucked!"
        pc "[rlist.blowjob_muffle]"
    hide robin_prone with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_watch_robin_onback:
    show robin_onback with dissolve
    "At the corner of my eye, I notice [robin.name]'s legs flailing in the air and wonder what she is doing."
    if not "mouth" in player.sex_holes or player.gagged:
        if not robin.showing:
            pc "Oh? I hear if you take a guy like that they will knock you up."
            robin.name "Haa fuck!"
            pc "Make sure you cum in her fella."
            tempname.name "Don't worry, I'll try and knock this slut up."
            pc "Good."
        else:
            pc "On your back, legs in the air and a baby in your belly. Sign of a true slut."
            robin.name "Haa fuck!"
    else:
        pc "[rlist.blowjob_muffle]"
        pcm "Get fucked you dirty girl!"
    hide robin_onback with dissolve
    jump whore_street_sex_group_picker

label whore_street_sex_group_watch_robin_doggy:
    show robin_doggy with dissolve
    "I look over and see [robin.name] bent over and taking it hard from behind."
    if not "mouth" in player.sex_holes or player.gagged:
        pc "Taking it like a good bitch?"
        robin.name "Uh huh..."
        pc "Good girl."
    else:
        pc "[rlist.blowjob_muffle]"
        pcm "Yeah good little bitch."
    hide robin_doggy with dissolve
    jump whore_street_sex_group_picker



label whore_street_sex_group_robin_matingpress_facesit:
    $ add_to_list(player.sex_holes, "robin_facesit")
    $ add_to_list(player.sex_holes, "mouth")
    "Without warning, I notice [robin.name] starting to climb over me."
    show sb_matingpress up frown with dissolve
    pc "What are you..."
    show sb_matingpress robin_sit with dissolve
    pc "Mmmmfff..."
    tempname.name "You dirty girl."
    if "vag" in player.sex_holes or "ass" in player.sex_holes:
        robin.name "Keep fucking her."
        tempname.name "No problem there."
        jump whore_street_sex_group_picker
    else:
        jump whore_street_sex_group_robin_matingpress_facesit_sexoffer


label whore_street_sex_group_robin_matingpress_facesit_sexoffer:
    if renpy.showing("sb_matingpress robin_69"):
        show sb_matingpress robin_sit with dissolve
        $ remove_from_list(player.sex_holes, "robin_vaglick")
    if player.sex_man_amount:
        robin.name "Which one of you perverts want to fill this bitch with more cum?"
        jump whore_street_sex_group_matingpress_vag
    else:
        robin.name "Looks like you wore all the boys out."
        pc "Mmmfff!"
        jump whore_street_sex_group_robin_matingpress_facesit_lick

label whore_street_sex_group_robin_matingpress_facesit_lick:
    $ add_to_list(player.sex_holes, "robin_vaglick")
    show sb_matingpress robin_69 with dissolve
    "I can't see anything that is going on, but I suddenly feel [robin.name] licking me."
    robin.name "So much cum in you."
    pc "Mmmmfff."
    robin.name "You are such a dirty whore letting so many men fill you up."
    "With no other choice, I lay back and let [robin.name] lick me up."
    "She licks me all over, cleaning the cum from me and even puts her tongue inside me."
    robin.name "Mmm, you are so dirty."
    pc "Mmmmff..."

    jump expression WeightedChoice([
    ("whore_street_sex_group_robin_matingpress_facesit_sexoffer", If(player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_robin_matingpress_facesit_leave", 100),
    ("whore_street_sex_group_robin_matingpress_facesit_robinsex", 200),
    ])

label whore_street_sex_group_robin_matingpress_facesit_leave:
    show sb_matingpress robin_sit oh with dissolve
    robin.name "There you go you slut. I have cleaned you up."
    show sb_matingpress no_robin oh with dissolve
    "She starts to ciimb off me and I can finally breathe properly."
    pc "Phew!"
    $ remove_from_list(player.sex_holes, ["robin_facesit", "robin_vaglick", "mouth"])
    jump whore_street_sex_group_picker

label whore_street_sex_group_robin_matingpress_facesit_robinsex:
    hide sb_matingpress
    show robin_facesit
    with dissolve
    "While [robin.name] is licking between my legs, I notice a guy coming up from behind her."
    pcm "Ha, yes, get her!"
    if not numgen(0,3):
        show robin_facesit anal with dissolve
    else:
        show robin_facesit vag with dissolve
    robin.name "Ha fuck!"
    "I watch as the guy lines himself up with [robin.name] then starts to enter her."
    pcm "Wait, now I just have his balls swinging in my face..."
    pc "Mmmfff..."
    "Not able to do anything, I lay back trying to breathe as the guys dick fucks [robin.name]."
    "She keeps pushing back on the guys cock, making it even harder to breathe. I have to start hitting her leg to let up a bit."
    robin.name "Ahh fuck yes."
    pcm "Thank fuck he seems like he is about to cum."
    "I watch as he speeds up and I can hear him grunting, until finally he starts to unload inside her."
    $ player.sex_cum(tempname, "face", quest_temp)
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    show robin_facesit cum
    "[robin.name] starts to calm down a bit and I can finally breathe a bit more."
    show robin_facesit noman with dissolve
    "With the guy gone, cum leaks out of [robin.name] and I am forced to eat it all up."
    robin.name "Yeah [name], drink it all up!"
    pc "Mmmffff!"
    show sb_matingpress robin_sit
    hide robin_facesit
    with dissolve
    robin.name "Make sure to get it all."
    "She wiggles her hips while sitting on my face and I have no choice but to swallow what is leaking out of her."
    show sb_matingpress no_robin oh with dissolve
    "She starts to ciimb off me and I can finally breathe properly."
    pc "Phew!"
    $ player.sex_holes = []
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
