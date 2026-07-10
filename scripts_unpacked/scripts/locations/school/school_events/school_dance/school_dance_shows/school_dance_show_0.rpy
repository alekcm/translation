label school_dance_show_0:
    $ school_dance_quest.activate()
    $ school_dance_quest_show_count += 1
    $ walk(loc_school_gym)
    show svet sport at right1 with dissolve
    svet.name "[name]. Over here."
    svet.name "Have you met the other girls yet?"
    if any([rachel.has_met, dani.has_met]):
        pc "I think so. Not sure who is on the team."
    else:
        pc "I've seen them around but never met."
        svet.name "Ok, I'll introduce them."

    show svet at left1 with dissolve
    svet.name "Girls! Come and say hello to our new member."
    show anabel sport happy at right1 with dissolve
    if dani.has_met:
        anabel.name "Hey [name], glad to see you here."
        pc "Hi [anabel.name]."
        show anabel neutral
        show dani sport at right2 with dissolve
        dani.name "Hi [name]."
        pc "Hey [dani.nname]."
    else:
        anabel.name "Hi, I'm [anabel.name]."
        pc "Hi."
        show anabel neutral
        show dani sport at right2 with dissolve
        svet.name "This is [dani.name]. She joined just before you did."
        show dani happy
        dani.name "Hi."
        pc "Nice to meet you."

    show dani neutral
    show rachel sport at right3 with dissolve
    if rachel.has_met:
        show rachel happy
        rachel.name "Ah [name]! You are joining us?"
        pc "Yeah."
        svet.name "Me and [rachel.name] started the club together."
    else:
        svet.name "And here we have [rachel.name]. We started the club together so she has been around as long as me."
        show rachel happy
        rachel.name "Ah, a new face. Hi."
        pc "Hello."
        show rachel neutral
        svet.name "This is our newest member [fname]."
        $ player.face_happy()
        pc "[name]. Nice to meet you all."

    $ player.face_neutral()
    svet.name "And since I have all you girls gathered. As you know I have been trying to get some shows so we can try and earn a bit of money."
    pc "Shows?"
    svet.name "Ah you don't know. Yeah like you used to have before, dancing on stage at some event or wearing branded clothes to promote some company. Whatever people will pay for."
    dani.name "Any luck?"
    svet.name "Some. I am speaking to someone from a clothing stall and seeing if we can arrange something. But he's dragging his feet so don't hold your breath."
    show dani worried
    dani.name "Oh, ok..."
    svet.name "For now all we can do is practice so when shows do come up, we are prepared. So let's get to it!"
    show rachel happy
    rachel.name "Right. Let's dance! I got a tape with some new stuff so we can listen to that."
    hide rachel with dissolve
    pcm "A tape?"
    hide svet
    hide dani
    hide anabel
    with dissolve
    show activity_dance with dissolve
    $ player.face_exercise()
    "I spend the next few hours practising a some dance routines with the girls. We go over the same routine again and again trying to nail it down properly."
    "At the beginning we are all fairly uncoordinated. But the more we practice the more me and the girls get into a rhythm and are able to manage being somewhat coordinated."
    "It is hard work and by the end me and the girls are totally drained."
    $ exercise(180)
    $ player.add_mood(20)
    if player.tired <= 21:
        $ player.add_tired(21 - player.tired)
    $ player.face_neutral()
    hide activity_dance with dissolve
    show svet sport at right1 with dissolve
    svet.name "Okay girls, that's enough for today. We will pick this back up next time."
    $ player.face_exercise()
    pc "Phew!"
    svet.name "And good work [name]. Nice to see you taking it seriously."
    $ player.face_happy()
    pc "Thanks."
    hide svet with dissolve
    $ walk(loc_school_locker_girls, trans=False)
    show anabel sport at right1
    show dani sport at right3
    with dissolve
    pc "Phew, I'm exhausted."
    dani.name "Tell me about it..."
    hide anabel with dissolve
    pc "So you are also new here?"
    $ pc_strip_tops()
    dani.name "Yeah, but I have known [anabel.name] for a while so it's a bit less scary joining a new group."
    show dani nooutfit with dissolve
    pc "Yeah guess that makes things easier."
    dani.name "Mmm."
    hide dani with dissolve
    $ pc_strip()
    $ acc_shower()
    $ player.set_hair("loose")
    pause 0.5
    $ walk(loc_school_locker_shower)
    $ shower_scene_wash()
    $ walk(loc_school_locker_girls, trans=False)
    show dani underwear at left3
    show anabel at right1
    with dissolve
    dani.name "...front of other people? You're not embarrassed?"
    $ pc_set_outfit("party")
    $ pc_dress_under()
    anabel.name "Yeah. Not sure about the shows..."
    $ pc_dress()
    $ acc_shower_dress()
    $ player.set_hair()
    dani.name "Think we are good enough?"
    show dani casual with dissolve
    anabel.name "Not sure. What would people expect anyway? Doubt they expect some professional dance show and just something more interesting than doing nothing."
    dani.name "Thats... Good I guess. What about the paid ones?"
    anabel.name "Those..."
    dani.name "What?"
    anabel.name "I don't know what they would expect."
    dani.name "Hmmm. Ok..."
    anabel.name "Anyway, I'm going home. See you next time [name]."
    show dani happy with dissolve:
        xzoom 1
    dani.name "Me too. See you."
    pc "Bye."
    hide dani
    hide anabel
    with dissolve
    call makeup_apply_call from _call_makeup_apply_call
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
