label school_class_meet_friend:
    call school_class_morning_arrive from _call_school_class_morning_arrive

    $ walk(loc_school_classroom)
    pause 0.5
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "Hey, [fname] isn't it?"
    pc "Yeah, [name]."
    cass.name "Hey, I'm Cassidy, but call me Cass. This is Mira."
    mira.name "Hi."
    if "pc_knows_whore" in mira.list:
        pc "Err... Hi."
        if "saw_at_academy" in mira.list:
            pcm "Seeing her close, it is who I thought it was..."
        else:
            pcm "Is that who I think it is?"
        pcm "Better not say anything while here..."
    cass.name "You are new to this area as well aren't you?"
    pc "Yeah, arrived a week or so ago. And you?"
    cass.name "About a month ago. Came here after my parents died from the Plague. After things calmed down I was enrolled here by my uncle."
    pc "Ah, that's good I suppose."
    cass.name "Not really, he just wanted rid of me. I live in the school dorms now. Uncle probably didn't want to have to pay for looking after me so set this up instead."
    $ player.face_worried()
    pc "..."
    cass.name "Not to worry, it's nicer here. How about you [name]?"
    pc "Err."
    if quest_homeless_start.active:
        pcm "Hmm, I suppose I shouldn't keep it hidden..."
        $ player.face_neutral()
        pc "Me and my sister were running from one of the cities during the riots. Heard about this place being somewhat safe."
        pc "On the way here we ended up crashing the car and ended up chased by crazies. Sort of stumbled into town while security were confused."
        pc "Lost my sister on the way though. She ended up in another direction or something."
        cass.name "Did you manage to find her?"
        pc "Yeah we met up again recently. Nothing to worry about."
    else:
        pcm "Hmm, I should stick to the truth as much as possible, but I can't tell them the whole story."
        $ player.face_neutral()
        pc "Me and my sister were running from one of the cities during the riots but I ended up seriously hurt. Ended up here in hospital until I healed up."
        cass.name "Ah, sorry to hear that. Are you okay now?"
        pc "Yeah good as new. Nothing to worry about."
    cass.name "Well, good to meet you [name]. Hard to make friends round here. Everyone is so on guard."
    pc "Really?"
    cass.name "You haven't noticed? Everyone acts like you want something from them."
    pc "Hmm, maybe I am too used to the city where that was normal even before all the chaos."
    cass.name "Haha could be."
    hide mira
    hide cass
    with dissolve
    $ school_met_friend = True
    if t.hour == 8:
        jump school_class_normal_end
    else:
        $ renpy.scene()
        with dissolve
        pcm "Looks like class is starting."
        jump school_class_lesson_picker

    $ walk(loc_school_hallway)
    jump travel_arrival

label school_class_meet_friend_lunch:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "Hey [name], join us for lunch."
    pc "Sure."
    cass.name "Did you have that intro to women's history as well [mira.name]? So morbid."
    mira.name "Yeah I had it. Kinda scary."
    "I eat lunch while chatting away with [cass.nname] and [mira.name]."
    hide mira
    hide cass
    with dissolve
    jump school_class_lunch_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
