label school_class_lunch_soccerboys:
    $ rand_choice = WeightedChoice([
    ("school_class_lunch_soccerboys_1", 100),
    ("school_class_lunch_soccerboys_2", 100 - player.mood),
    ("school_class_lunch_soccerboys_3", nate.lust),
    ("school_class_lunch_soccerboys_4", 1),
    ("school_class_lunch_soccerboys_5", 1),
    ("school_class_lunch_soccerboys_6", If (mira.active,1,0)),
    ("school_class_lunch_soccerboys_7", 1),
    
    
    
    ])
    jump expression rand_choice

label school_class_lunch_soccerboys_1:
    show nate at right1 with dissolve
    nate.name "Ooh, looks tasty."
    pc "Yeah. Like everything here."
    nate.name "Good we have [dan.name]'s beer to wash this shit down."
    pc "Mmmm."
    jump school_class_lunch_end

label school_class_lunch_soccerboys_2:
    show dan at right1 with dissolve
    pc "Hey."
    dan.name "Mmm."
    dan.name "Looks like you could do with something to wash the food down."
    pc "Wouldn't say no..."
    dan.name "Here."
    $ player.beer()
    pc "Thanks."
    jump school_class_lunch_end

label school_class_lunch_soccerboys_3:
    show nate at right1 with dissolve
    nate.name "Hey. Look what you got."
    pc "It's... Something..."
    nate.name "Mmmm."
    nate.name "How about I take you somewhere for dessert?"
    pc "Ugh, pervert."
    if player.check_sex_agree(5):
        menu:
            "Come on then":
                pc "I feel dirty even agreeing with such a shitty pick up line."
                nate.name "But you are agreeing?"
                pc "Better than eating this. Let's go."
                nate.name "Nice."
                $ walk(loc_school_hallway)
                pause 0.5
                $ walk(loc_school_toilet)
                pause 0.5
                hide nate with dissolve
                pcm "Hmmm..."
                show nate at right1 with dissolve
                nate.name "It's empty. Come on."
                hide nate with dissolve
                pcm "Hopefully no one sees me..."
                $ walk(loc_school_toilet_boys)
                $ tempname = nate
                $ npc_race_picker(nate)
                jump school_field_soccer_sex_alone_start
            "Don't bother":
                $ NullAction()
    pc "You need some better pick up lines [nate.name]."
    jump school_class_lunch_end

label school_class_lunch_soccerboys_4:
    show drake at right1
    show dan at right2
    with dissolve
    drake.name "...the idiot."
    dan.name "Mmm."
    pc "Idiot? Talking about [nate.name]?"
    drake.name "Who else?"
    pc "What's he done now?"
    drake.name "You know what he's like. Have a guess."
    pc "Said something perverted and got kicked in the balls?"
    drake.name "..."
    dan.name "... ..."
    pc "What? Am I right?"
    drake.name "Pretty much..."
    dan.name "She got a good kick in and he puked..."
    $ player.face_laugh()
    pc "Haha!"
    jump school_class_lunch_end

label school_class_lunch_soccerboys_5:
    show nate at right1
    show dan at right2
    with dissolve
    nate.name "Doesn't your beer contact do food as well?"
    dan.name "If only. Would be better than this stuff."
    pc "You think so?"
    nate.name "Well, it would be pretty hard to get worse than whatever this slop is."
    pc "..."
    pc "Yeah... [dan.name]'s stuff probably would be better."
    pcm "Wonder if I should try and catch some birds in the park..."
    jump school_class_lunch_end

label school_class_lunch_soccerboys_6:
    show dan at right1
    show mira at right2:
        xzoom -1
        pause 0.5
    with dissolve
    hide mira with dissolve
    pc "Err... See you?"
    pc "You know [mira.name]?"
    dan.name "Yeah, a bit."
    pc "Why did she run away as soon as I came?"
    dan.name "Dunno."
    $ player.face_happy()
    pc "Oh? Secret lovers?"
    dan.name "Dunno."
    $ player.face_neutral()
    pc "Huh? What do you mean \"dunno\"? I'm asking if you are secret lovers with her."
    dan.name "Dunno."
    $ player.face_annoyed()
    pc "Ugh!"
    jump school_class_lunch_end

label school_class_lunch_soccerboys_7:
    show drake at right1
    show dan at right2
    with dissolve
    drake.name "...low on beer."
    $ player.face_shock()
    pc "What!?"
    dan.name "Calm down booze hound."
    dan.name "I'll just go and pick more up."
    pc "Need help?"
    dan.name "Err..."
    dan.name "Sure. I could pay with you instead of with money I suppose."
    $ player.face_annoyed()
    pc "..."
    drake.name "Think her ass would get us lot's of beer?"
    dan.name "It would set us up for a long time."
    drake.name "Well, was nice knowing you [name]."
    dan.name "You will be missed."
    pc "Ugh..."
    jump school_class_lunch_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
