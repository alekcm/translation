label school_dance_show_7:
    $ school_dance_quest_show_count += 1
    $ walk(loc_school_gym)
    show svet dance1 at right1 with dissolve
    svet.name "Okay [dancet], gather round."
    show rachel dance1 at left3 with dissolve
    show anabel dance1 at left1
    show dani dance1 at left2
    with dissolve
    svet.name "So off to the park again?"
    show dani with dissolve:
        xzoom 1
    dani.name "You thought of anything to make more tips [name]?"
    pc "Huh, actually I didn't think much about it."
    show rachel with dissolve:
        xzoom 1
    rachel.name "You want to get more tips out of them? That's easy."
    show dani happy with dissolve:
        xzoom -1
    dani.name "What? How?"
    rachel.name "Silly, they give tips for you."
    dani.name "What?"
    rachel.name "Ok, wait."
    $ add_to_list(rachel.list, "no_location")
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(anabel.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    hide rachel with dissolve
    anabel.name "What's she up to?"
    dani.name "No idea..."
    show rachel dance happy at right3 with vpunch
    rachel.name "TADAAA!"
    show dani worried
    show anabel worried
    anabel.name "Err, wow..."
    dani.name "Ummm..."
    rachel.name "I guarantee more tips this way."
    dani.name "Thats... Too much isn't it?"
    anabel.name "It... Is..."
    anabel.name "It will show off everything."
    rachel.name "Well, not for you and me. We are modest. But this lot are a bit more naughty."
    rachel.name "Come on! More tips ahoy!"
    hide rachel with dissolve
    svet.name "Wai..."
    svet.name "*Sigh* At least wait for us to discuss it..."
    anabel.name "Are you fine with this [svet.name]?"
    svet.name "Me? Danced before in clothes that didn't hide anything. It's what you think that matters."
    dani.name "Really?"
    svet.name "Of course. Dancers are expected to. But this isn't a professional troupe and we aren't dancing on a stage full of ticket holders. So things are a bit different."
    anabel.name "We are dancing for..."
    svet.name "Mmm. So up to you lot."
    dani.name "Think it will improve tips?"
    svet.name "Definitely."
    show dani neutral with dissolve:
        xzoom 1
    dani.name "What do you think?"
    if player.has_perk([perk_slut, perk_whore, perk_broken, perk_exhibitionist, perk_bimbo, perk_sucu]):
        pc "I'm okay with it. People will tip more if we show off more so I'm fine with it."
    else:
        anabel.name "This is going too far isn't it? Showing off to attract more money?"
    svet.name "That's pretty much what we are doing no matter what we wear."
    anabel.name "You think so?"
    svet.name "Long flowing gowns or tiny hotpants. Either way all eyes are on us and it's our job to entertain the crowd."
    anabel.name "..."
    show dani angry
    dani.name "Ugh!"
    hide dani with dissolve
    anabel.name "Where is she off to?"
    $ walk(loc_school_locker_girls, trans=False)
    hide svet
    show dani dance worried at right1
    show anabel dance1 at left1
    with dissolve
    dani.name "..."
    show dani neutral
    dani.name "Let's go."
    hide dani with dissolve
    pc "Err, okay then..."
    show sb_pose_upskirt with dissolve

    pause 0.5
    $ c.socks = 0
    show sb_pose_upskirt
    with dissolve
    pause 0.5
    hide sb_pose_upskirt with dissolve
    pause 0.5
    $ walk(loc_school_gym, trans=False)
    hide anabel with dissolve
    pause 0.2
    $ walk(loc_school)
    pause 0.2
    $ walk(loc_busstop_school, trans=False)
    $ remove_from_list(rachel.list, "no_location")
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(anabel.list, "no_location")
    $ remove_from_list(svet.list, "no_location")
    show dani dance at right1 with dissolve
    dani.name "..."
    show rachel dance at right3 with dissolve
    rachel.name "Great, we ready to go?"
    pc "Just waiting on [anabel.name]."
    rachel.name "Ok, bus is almost here so hope she..."
    show anabel dance at left2 with dissolve
    anabel.name "I'm here."
    rachel.name "Great, let's get on."
    hide anabel
    hide dani
    with dissolve
    hide rachel
    with dissolve
    $ walk(loc_bus_interior, trans=hpunch)
    $ player.face_angry()
    pc "Excuse me."
    $ player.face_neutral()
    pcm "..."
    show anabel dance at left1 with hpunch

    anabel.name "Ugn!"
    pc "Hey."
    show anabel with dissolve:
        xzoom 1
    anabel.name "Hey."
    anabel.name "Feels like I am exposing myself to everyone on the bus..."
    pc "Probably are in these tiny skirts."
    show anabel angry with hpunch
    anabel.name "Ah!"
    show rachel dance happy at left2 with hpunch:
        xzoom -1
    rachel.name "Just me."
    show anabel neutral
    rachel.name "You look good without the tights [anabel.name]!"
    anabel.name "..."
    anabel.name "Thanks..."
    rachel.name "We are gonna knock their socks off."
    pc "Let's see."
    rachel.name "Ok, here we go. Move!"
    hide rachel with hpunch
    show anabel angry
    anabel.name "Ugn!"
    hide anabel with hpunch
    pcm "..."
    with hpunch
    pause 0.5
    $ walk(loc_busstop_residential, trans=hpunch)
    pc "Ugh."
    $ walk(loc_park, trans=False)
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "Ok, we all know what we are doing. Make a space to dance and [rachel.name], you are on hat duty."
    if player.has_perk([perk_whore, perk_slut, perk_broken, perk_bimbo, perk_sucu, perk_exhibitionist]):
        pc "I'll do hat stuff as well."
    if "pub_first_talk" in dani.list:
        dani.name "I don't mind doing hat stuff as well."
    show rachel happy
    rachel.name "Great!"
    hide dani
    hide rachel
    hide svet
    hide anabel
    with dissolve
    $ show_dance_image()
    "Like we have all done before, we dance our routines and at the end of each one, [rachel.name] goes around the crowd with a hat to gather people's tips."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_14
    "Towards the end it has become clear to us all that there is much greater interest in the show than the times before and it even requires all five of us to circle around doing hat duty."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_15
    "It starts getting to the point where we are all spending more time working the crowd gathering tips than actually dancing."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_16
    "Even though we are all doing hat duty, we will somehow manage to get in some dance routines."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_17
    "Eventually though we start to get tired and [svet.name] calls us all over."
    $ player.face_normal()
    $ renpy.scene()
    with dissolve
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    rachel.name "Ahhh that was tiring..."
    svet.name "Ok, let's gather all the money together and see what we got out of it."
    rachel.name "Don't know about the rest of you but my hat was getting heavy."
    anabel.name "Yeah... Was a lot more than usual..."
    svet.name "Looks like it. Almost double what we got last time."
    $ player.add_money(55)
    show dani happy
    dani.name "Ah that's amazing!"
    show anabel happy
    anabel.name "Yeah..."
    show rachel happy with dissolve:
        xzoom 1
    rachel.name "Told ya."
    show svet worried
    dani.name "Double? That's quite a big increase."
    show anabel angry
    anabel.name "Ugh. The crowd was horrible."
    hide svet
    show dani:
        xzoom 1
    with dissolve
    dani.name "They touch you as well?"
    anabel.name "Yeah..."
    show anabel neutral
    rachel.name "They tend to do that."
    show rachel angry
    rachel.name "Some of them don't even tip after. Greedy!"
    anabel.name "Err..."
    show rachel neutral
    rachel.name "Anyway, I am going. Where has [svet.nname] gone to?"
    show rachel with dissolve:
        xzoom -1
    rachel.name "Ah, who's that she's talking to?"
    show dani neutral with dissolve:
        xzoom -1
    dani.name "No idea."
    rachel.name "Anyway, see you guys."
    pc "Bye."
    hide rachel with dissolve
    show anabel at right1
    show dani at right2
    with dissolve
    dani.name "Gonna head off as well. See you [name]."
    show anabel angry
    anabel.name "Yeah, gonna have to wash the stink of those perverts off me for the next few hours."
    pc "Cya."
    hide dani
    hide anabel
    with dissolve
    pcm "Why does no one walk home together?"
    show sb_pose_upskirt with dissolve
    if player.has_perk(perk_exhibitionist):
        pcm "Well, I can show my ass off without them saying something while walking home I suppose."
    else:
        pcm "Even worse now I'm showing off more of my ass while going home."
        pcm "Ah well, getting used to it at this point."
    hide sb_pose_upskirt with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
