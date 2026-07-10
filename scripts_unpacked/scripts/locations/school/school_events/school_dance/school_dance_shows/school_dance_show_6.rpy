label school_dance_show_6:
    $ school_dance_quest_show_count += 1
    $ walk(loc_school_gym)
    show svet dance at right1
    svet.name "Okay [dancet] let's have a chat."
    show rachel dance at left3 with dissolve
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "So last time we managed to practice dance while also earning a bit of cash out of it. The money wasn't too bad either considering we expected to earn nothing."
    svet.name "So, we up for it again tonight?"
    rachel.name "Yeah let's go!"
    svet.name "[anabel.name]?"
    anabel.name "..."
    if player.has_perk([perk_whore, perk_slut, perk_broken, perk_bimbo, perk_sucu, perk_exhibitionist]):
        anabel.name "I guess... [rachel.name] and [name] offered to do the hat stuff so I guess it's ok."
    else:
        anabel.name "I guess... [rachel.name] offered to do the hat stuff so I guess it's ok."
    svet.name "Really? I thought you would be against."
    anabel.name "I am. But..."
    anabel.name "I enjoy dancing and this is what the group wants."
    svet.name "Ok. Well, great. So to the park it is."
    rachel.name "Great. Let's go!"
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(anabel.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    $ add_to_list(rachel.list, "no_location")
    hide rachel with dissolve
    hide svet with dissolve
    show dani with dissolve:
        xzoom 1
    dani.name "I thought for sure you would refuse."
    anabel.name "I just don't like the look on those perverts' faces. To dance for them makes me feel dirty."
    anabel.name "But I enjoy being with you guys so I'll go along with it."
    hide anabel with dissolve
    dani.name "Didn't expect that..."
    hide dani with dissolve
    pcm "..."
    pcm "Why does everyone keep leaving without me?"
    $ walk(loc_school)
    $ walk(loc_school, trans=False)
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(anabel.list, "no_location")
    $ remove_from_list(svet.list, "no_location")
    $ remove_from_list(rachel.list, "no_location")
    $ walk(loc_busstop_school, trans=False)
    show anabel dance at left1
    show dani dance at left2
    show rachel dance at left3
    show svet dance happy at right1
    with dissolve
    svet.name "Right, so same as last time. Dance, smile and entertain the people that come to watch."
    rachel.name "Yup!"

    hide dani
    hide anabel
    hide rachel
    hide svet
    $ walk(loc_bus_interior)
    pcm "Dance and smile..."
    pcm "Entertain the crowd..."
    show dani dance at left1 with hpunch:
        xzoom -1
    dani.name "Ung!"
    pc "You ok."
    dani.name "Yeah just trying to squeeze by these perverts that want to rub up on you."
    pc "Ah. Fun times..."
    dani.name "Yeah. Hope we can make something nice today as well. And looks like [anabel.name] is coming round."
    pc "Just barely. I'm quite surpri..."
    show dani angry with hpunch
    pc "..."
    pc "Groper?"
    dani.name "Yeah."
    show dani neutral
    pc "I'm quite surprised she agreed."
    dani.name "She likes dancing. More than most of us here probably. But she has her issues with men..."
    pc "Yeah can see that."
    show dani happy
    dani.name "How she manages to ride the bus without murdering someone I don't know."
    $ player.face_happy()
    pc "Ha, pretty sure the day will come."
    $ player.face_neutral()
    dani.name "Here we go."
    show dani angry with hpunch
    dani.name "Move!"
    hide dani with dissolve
    $ walk(loc_busstop_residential)
    $ walk(loc_park)
    show svet dance at right1 with dissolve
    svet.name "Okay girls. Gather round."
    show anabel dance at left1
    show dani dance at left2
    show rachel dance at left3
    with dissolve
    svet.name "So same as last time. Dance, smile and entertain. Give these people something worth giving their money for."
    if player.has_perk([perk_whore, perk_slut, perk_broken, perk_bimbo, perk_sucu, perk_exhibitionist]):
        svet.name "[rachel.name], [name], you are on hat duty so try to keep them happy."
    else:
        svet.name "[rachel.name], you are on hat duty so try to keep them happy."
    svet.name "Let's go!"
    hide svet
    hide dani
    hide anabel
    hide rachel
    with dissolve
    $ show_dance_image()
    "Me and the girls put on another show. After the last one we are all feeling a lot more confident in ourselves and put on a much more pleasant performance."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_3
    if player.has_perk([perk_whore, perk_slut, perk_broken, perk_bimbo, perk_sucu, perk_exhibitionist]):
        "As before, after each routine, me and [rachel.name] head around the crowd trying to tempt viewers into putting some money in our hats. The comments we get are mostly perverted and offers to give us more money if we go off alone with them."
    else:
        "As before, after each routine, [rachel.name] heads around the crowd trying to tempt viewers into putting some money in our hats. She seems to not be too bothered by the comments and groping she receives and keeps a positive attitude."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_4
    "[anabel.name] and [dani.nname] also seem a lot more relaxed and confident in what they are doing. While this is to be expected of [dani.nname], I am surprised to see [anabel.name] smiling and being seemingly happy."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_5
    "Eventually we are all exhausted and [svet.name] decides to call it a day."

    $ player.add_mood(20)
    if player.tired <= 21:
        $ player.add_tired(21 - player.tired)
    $ player.face_neutral()
    $ renpy.scene()
    with dissolve

    pcm "Ufff. Ufff."
    show svet dance at right1 with dissolve
    svet.name "Okay [dancet], let's have a chat."
    show anabel dance at left1
    show dani dance at left2
    show rachel dance at left3
    with dissolve
    dani.name "Uff. I am knackered!"
    anabel.name "Same."
    dani.name "So? How was it?"
    svet.name "Just checking..."
    svet.name "Oh, looks like we got more this time round."
    show dani happy
    dani.name "Ah really?"
    svet.name "Here you all go."
    $ player.add_money(30)
    dani.name "Ahh nice!"
    show dani with dissolve:
        xzoom 1
    dani.name "Look [anabel.name]. We made more this time."
    anabel.name "Yeah. Looks that way."
    svet.name "Good job girls. Guess this means we will be doing the same next time."
    show dani with dissolve:
        xzoom -1
    dani.name "Yeah!"
    rachel.name "Yay!"
    svet.name "Ok, see you next time."
    hide svet with dissolve
    show rachel with dissolve:
        xzoom 1
    rachel.name "See you next time."
    hide rachel with dissolve
    show dani at right2
    show anabel at right1
    with dissolve
    dani.name "Well that's good news. Wonder if we could do more to bring in the tips."
    anabel.name "Already showing my arse off to everyone."
    show dani happy
    dani.name "Showing off your giant shorts more like."
    anabel.name "Anyway, I'm heading off. Cya."
    hide anabel with dissolve
    dani.name "I'm gonna head off as well. Think of ways we can earn more money [name]."
    pc "Yeah, cya."
    hide dani with dissolve
    show sb_pose_upskirt with dissolve
    pcm "..."
    pcm "Leaving me here with my arse out is becoming a habit."
    pcm "..."
    pcm "Ah well, whatever."
    hide sb_pose_upskirt with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
