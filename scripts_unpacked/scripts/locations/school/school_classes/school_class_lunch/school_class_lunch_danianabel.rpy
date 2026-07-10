label school_class_lunch_danianabel:
    $ rand_choice = WeightedChoice([
    ("school_class_lunch_danianabel_1", 1),
    ("school_class_lunch_danianabel_2", If (pub_waitress.timesworked >= 8, 1, 0)),
    ("school_class_lunch_danianabel_3", 1),
    ("school_class_lunch_danianabel_4", 1),
    ("school_class_lunch_danianabel_5", 1),
    ("school_class_lunch_danianabel_6", 1),
    ("school_class_lunch_danianabel_7", 1),
    ("school_class_lunch_danianabel_8", 1),
    ("school_class_lunch_danianabel_9", 1),
    ("school_class_lunch_danianabel_10", 1),
    ])
    jump expression rand_choice

label school_class_lunch_danianabel_1:
    show anabel at right1
    show dani at right2
    with dissolve
    dani.name "Have you been to the lake before?"
    anabel.name "No chance."
    dani.name "Huh? Why not?"
    anabel.name "Me in a bikini? No thanks."
    dani.name "C'mon, you could do with some sun."
    anabel.name "Maybe, but not getting naked on the beach to get it."
    jump school_class_lunch_end

label school_class_lunch_danianabel_2:
    show anabel at right1
    show dani at right2
    with dissolve
    anabel.name "Still working at the pub?"
    pc "When I get the chance, yeah."
    anabel.name "What's it like there?"
    pc "..."
    pc "Not something you should consider doing."
    anabel.name "Why not?"
    if "working_pub" in dani.list:
        show dani happy
        dani.name "You can't even get on the bus properly. Can't imagine how some pub drunks would react to those things you got there squeezing into the tiny dress."
        dani.name "Can you imagine her in one?"
        pc "She would earn double what everyone else does combined!"
        dani.name "Right!?"
    else:
        show dani happy
        dani.name "You working with a bunch of drunks around?"
        pc "You would end up fired in half an hour."
        dani.name "I don't think she would last that long."
    jump school_class_lunch_end

label school_class_lunch_danianabel_3:
    show anabel at right1
    show dani at right2
    with dissolve
    anabel.name "...he at least offer to pay you?"
    dani.name "He implied if I did a good enough job he would."
    anabel.name "Do people really fall for that?"
    dani.name "Maybe. Why else would scummy shits like that feel so confident in offering if it didn't work?"
    jump school_class_lunch_end

label school_class_lunch_danianabel_4:
    show anabel at right1
    show dani at right2
    with dissolve
    anabel.name "You ever been to the station to look for work?"
    dani.name "Couple of times. Scary there."
    anabel.name "I know! You have the gangs of urchins eyeing you up?"
    dani.name "No, for me it was the gamines that looked like they were ready to rip my throat out if someone offered me work before them."
    anabel.name "*Sigh* They probably would as well."
    dani.name "I don't doubt it."
    jump school_class_lunch_end

label school_class_lunch_danianabel_5:
    show anabel at right1
    show dani at right2
    with dissolve
    anabel.name "Had a run in with a group of gamines last night."
    dani.name "Oh? Anything happen?"
    anabel.name "Well, no. I saw the bus coming and jumped on it to avoid them."
    dani.name "Wow, you choosing the bus over a run in with them?"
    anabel.name "I know..."
    jump school_class_lunch_end

label school_class_lunch_danianabel_6:
    show anabel at right1
    show dani at right2
    with dissolve
    dani.name "Did you ever go to that place near the truck stop?"
    anabel.name "Yeah, spoke with the guy that runs the place."
    dani.name "Oh? That's good isn't it? He give you the job?"
    anabel.name "Well, yeah he offered. Then I saw the uniform."
    dani.name "And?"
    anabel.name "I think the local whores cover more than it did."
    dani.name "Hmmm. Well, pretty typical of most jobs these days..."
    if pub_waitress.timesworked > 5:
        pc "My pub uniform is pretty much the same. Doesn't hide much."
    jump school_class_lunch_end

label school_class_lunch_danianabel_7:
    show anabel at right1
    show dani at right2
    with dissolve
    dani.name "...nice to relax there but not a good idea to be there when it gets dark."
    pc "The lake?"
    dani.name "No, park."
    anabel.name "Well, that goes for anywhere outside your house."
    dani.name "And inside your house..."
    anabel.name "..."
    pc "... ..."
    jump school_class_lunch_end

label school_class_lunch_danianabel_8:
    show anabel at right1
    show dani at right2
    with dissolve
    anabel.name "... just sitting on the bench and noticed him on the grass."
    pc "Ohh, [anabel.nname] find a boyfriend?"
    anabel.name "Ugh, he was sitting there wanking looking at the girls."
    pc "Ah..."
    $ player.face_happy()
    pc "Well, still sounds better than most boyfriends I can imagine from round here."
    show dani happy
    dani.name "Right?"
    anabel.name "..."
    jump school_class_lunch_end

label school_class_lunch_danianabel_9:
    show anabel at right1
    show dani at right2
    with dissolve
    anabel.name "... rushed up covered in blood and was asking for help."
    dani.name "Did you?"
    anabel.name "Of course not! Not falling for their tricks."
    dani.name "Hmmm."
    anabel.name "What? You would have helped?"
    dani.name "No chance! Just a shame I guess. So many people out to screw you over that you don't help anyone. Ever."
    jump school_class_lunch_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
