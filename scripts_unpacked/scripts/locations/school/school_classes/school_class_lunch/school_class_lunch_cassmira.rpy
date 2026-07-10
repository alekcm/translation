label school_class_lunch_cassmira:
    jump expression renpy.random.choice([
    "school_class_lunch_cassmira_1",
    "school_class_lunch_cassmira_2",
    "school_class_lunch_cassmira_3",
    "school_class_lunch_cassmira_4",
    
    "school_class_lunch_cassmira_6",
    "school_class_lunch_cassmira_7",
    "school_class_lunch_cassmira_8",
    "school_class_lunch_cassmira_9",
    "school_class_lunch_cassmira_10"
    ])

label school_class_lunch_cassmira_1:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "What did you get?"
    mira.name "Just a sandwich and some fruit."
    cass.name "You on a diet or something."
    mira.name "No, but fish? I'm not eating fish cooked here. Who knows how old it is."
    jump school_class_lunch_end

label school_class_lunch_cassmira_2:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "How's your dance classes going [name]?"
    if player.isfat == True:
        pc "Hard work. I am far too unfit to really do anything."
    elif school_dance_quest_on_team == True:
        pc "It's great actually. Training with the team is much more fun than the normal class."
    else:
        pc "Going ok, just trying to learn the routines and not fall on my arse."
    cass.name "How is the club leader? She seems a bit of a bitch."
    pc "Hmm, she's just harsh. She means well."
    jump school_class_lunch_end

label school_class_lunch_cassmira_3:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "Mira~~"
    mira.name "Huh?"
    cass.name "I saw you earlier."
    mira.name "Err. Okay... Saw me doing what?"
    cass.name "Don't be coy, the boy on the football team."
    mira.name "Ah."
    cass.name "Well...?"
    mira.name "Well what?"
    cass.name "Okay be that way. Keep your secrets."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        $ player.eye = 4
        $ player.mouth = 6
        pc "FRODO!!!!"
        $ player.face_normal()
        cass.name "Whaaaa...?"
        pc "Nothing."
    jump school_class_lunch_end

label school_class_lunch_cassmira_4:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "Here she is. So [name]. How's life living in a house full of boys?"
    pc "It has it's ups and downs."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        cass.name "I'm sure it's you that's making the \"ups\""
        pc "Huh?"
        mira.name "[cass.nname]! Pervert!"
        cass.name "What?"
    else:
        pc "Mostly they stay in their rooms. Don't really speak much with them."
    jump school_class_lunch_end

label school_class_lunch_cassmira_5:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "You done any more handing out flyers in the market [mira.name]?"
    mira.name "Don't want to, but have no choice."
    cass.name "Why not? At least they don't screw you on the pay."
    mira.name "Because I can't count how many people think it's okay to put their hands on me."
    cass.name "Ah yeah. Part of the job unfortunately."
    mira.name "How can you accept such a thing?"
    cass.name "I don't accept it. But if I want to get paid I have no choice."
    mira.name "Wouldn't it bring more money if you just walked the highway with that attitude?"
    cass.name "Well I don't want to be hit over the head and bundled into the back of a car. That won't happen in the market."
    jump school_class_lunch_end

label school_class_lunch_cassmira_6:
    show mira at right2
    show cass at right1
    with dissolve
    mira.name "She tried to pull my swimsuit down in swimming class."
    cass.name "She did?"
    mira.name "Yeah, bitch."
    cass.name "Maybe she wanted a look at the goods?"
    mira.name "What? You think so?"
    cass.name "Na, she's probably just a cunt."
    jump school_class_lunch_end

label school_class_lunch_cassmira_7:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "I saw you [name]. In dance class."
    pc "You did. What was I doing?"
    cass.name "♪ Want you to make me feel... like the only girl in the wooooorld... ♪"
    $ player.eye = 2
    $ player.mouth = 8
    pc "Tell anyone and they will never find your body."
    cass.name "♪ Like I'm the only one that you'll ever love... ♪"
    pc "It will be a brutal murder with your tongue cut out."
    mira.name "Hahahaha!"
    $ player.face_normal()
    jump school_class_lunch_end

label school_class_lunch_cassmira_8:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "What is that [name]?"
    pc "Haven't a clue, I was late and this is all they had."
    cass.name "Looks like puke."
    pc "Doesn't taste much better either."
    jump school_class_lunch_end

label school_class_lunch_cassmira_9:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "What do you think [mira.name]? At what point is a slice of pizza just bread?"
    mira.name "What?"
    cass.name "Look, it's bread instead of pizza dough and there is so little tomato that you can't even see it. The bread absorbed it all."
    cass.name "And I don't see any cheese on this thing. It's basically a slice of warm, mushy bread."
    jump school_class_lunch_end

label school_class_lunch_cassmira_10:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "That... Thing you are eating looks tasty."
    pc "Tell me about it. It is somehow both slimy and crumbly."
    cass.name "They must have some kind of genius chef working here to create such a monstrosity."
    jump school_class_lunch_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
