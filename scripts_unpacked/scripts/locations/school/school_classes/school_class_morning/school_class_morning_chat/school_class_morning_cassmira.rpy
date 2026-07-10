label school_class_normal_cassmira:
    $ rand_choice = WeightedChoice([
    ("school_class_normal_cassmira_1", 1),
    ("school_class_normal_cassmira_2", 1),
    ("school_class_normal_cassmira_3", If(not cass.iswhore, 1, 0)),
    ("school_class_normal_cassmira_4", 1),
    ("school_class_normal_cassmira_5", 1),
    ("school_class_normal_cassmira_6", If (school_bully_quest_bully_cass_target and not shane.dead,1,0)),
    ("school_class_normal_cassmira_7", 1),
    ("school_class_normal_cassmira_8", If (player.has_perk(perk_slutty),1,0)),
    ("school_class_normal_cassmira_9", 1),
    ("school_class_normal_cassmira_10", If (weather_var > 2,1,0)),
    ("school_class_normal_cassmira_11", If ("rape" in cass.conversation_topics,1,0)),
    ("school_class_normal_cassmira_12", If ("lover" in cass.conversation_topics,1,0)),
    ("school_class_normal_cassmira_13", If ("pregnant" in cass.conversation_topics,1,0)),
    ])
    jump expression rand_choice

label school_class_normal_cassmira_1:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "...while I was just sitting there, he was constantly looking over at me."
    mira.name "Creep."
    cass.name "Tell me about it. Morning [name]."
    pc "Morning."
    mira.name "So what did you do?"
    cass.name "Nothing. Just waited for my stop and got off the bus."
    jump school_class_normal_end

label school_class_normal_cassmira_2:
    show mira at right2
    show cass at right1
    with dissolve
    mira.name "I wanted to go to the cosmetics shop this morning but I woke up late and didn't have time."
    cass.name "What did you want to buy?"
    mira.name "Nothing. As if I could afford anything from there. I just wanted to go to the makeup shop and put on something nice."
    pc "Without buying anything? You can do that?"
    mira.name "Sure why not? You just say you are trying it out. The staff usually don't care anyway."
    pc "Hmmm"
    jump school_class_normal_end

label school_class_normal_cassmira_3:
    show mira at right2
    show cass at right1
    with dissolve
    mira.name "...the pay isn't very good but not like there are many options while trying to go to school at the same time."
    cass.name "Yeah tell me about it. I tried to get a job in the motel but they wanted me to work the night shift."
    mira.name "Ugh, the place that the truckers take the street girls? Asking for trouble having a girl work there at night."
    cass.name "Yeah... *Sigh*"
    cass.name "What about you [name]? How are you managing to earn some money?"
    pc "Huh? However I can. Jobs are hard to come by."
    cass.name "Yeah. If this keeps up it won't be long before I have to walk the highway."
    mira.name "Cass no!"
    jump school_class_normal_end

label school_class_normal_cassmira_4:
    show mira at right2
    show cass at right1
    with dissolve
    pc "Morni..."
    mira.name "Don't be silly, of course not. You tell her [name]."
    pc "Err, sure I'll tell her."
    pc "...What should I tell her?"
    mira.name "Uggh!"
    jump school_class_normal_end

label school_class_normal_cassmira_5:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "... like you're ready to pass out on your feet."
    pc "Morning."
    mira.name "Ugh. Morning."
    pc "Partying all night?"
    mira.name "I wish."
    jump school_class_normal_end

label school_class_normal_cassmira_6:
    show mira at right2
    show cass worried at right1
    with dissolve
    mira.name "Maybe you should tell someone about it."
    cass.name "What good will that do?"
    mira.name "Not sure, but worst that can happen is nothing changes."
    cass.name "..."
    hide cass with dissolve
    pc "Those two shits?"
    mira.name "Yeah..."
    jump school_class_normal_end

label school_class_normal_cassmira_7:
    show cass at right1 with dissolve
    pc "Morning."
    cass.name "Shhh..."
    pc "What's going on?"
    cass.name "I am trying to hear what [mira.name] is saying to that boy."
    pc "Oh?"
    if school_soccer_quest.active:
        pc "Ah, that's [dan.name]."
        cass.name "You know him?"
        pc "Yeah, we play football together."
        cass.name "Oh? Think they have something going on together?"
        if dan.preg_current and player.preg_knows:
            pcm "Hope not. He already gave me his baby and don't need [mira.name] carrying another."
        elif dan.vsex or dan.asex:
            pcm "Well, considering he's been fucking me, I hope not."
        elif dan.osex:
            pcm "Hope not considering I sucked his dick."
        pc "Dunno. Let's keep spying..."
    else:
        pc "Who is it?"
        cass.name "One of the boys who hangs out on the pitch."
        pc "Hmmm..."
        pc "Her boyfriend?"
        cass.name "That's what I'm trying to find out."
    jump school_class_normal_end

label school_class_normal_cassmira_8:
    show mira at right2
    show cass at right1
    with dissolve
    pc "Morning."
    cass.name "Morning [name]. You trying to find yourself a boyfriend?"
    pc "Huh?"
    cass.name "You're looking very inviting."
    $ player.face_shy()
    pc "Ah..."
    cass.name "Good luck."
    pc "Thanks...?"
    jump school_class_normal_end

label school_class_normal_cassmira_9:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "Are you serious?"
    mira.name "Yeah, why not?"
    cass.name "What about you [name]? Been to the lake before?"
    pc "Err..."
    cass.name "Perverts everywhere."
    mira.name "Yeah. But that's no different to anywhere else."
    cass.name "Except I will be in a bikini."
    pc "The perverts would love to see that."
    cass.name "See [mira.name]!"
    jump school_class_normal_end

label school_class_normal_cassmira_10:
    show mira at right2
    show cass worried at right1
    with dissolve
    cass.name "... the weather so I got the bus."
    mira.name "Oh? Playing with fire there. What happened?"
    cass.name "Had to get off a bit early or I wasn't going to make it with my underwear still on."
    mira.name "Ah. So not bad then."
    show cass angry
    cass.name "Ugh!"
    jump school_class_normal_end

label school_class_normal_cassmira_11:
    show mira at right2
    show cass cry at right1
    with dissolve
    cass.name "Was horrible. I didn't even do anything."
    cass.name "*SOB*"
    mira.name "..."
    cass.name "He didn't even..."
    cass.name "*SOB*"
    pcm "Fuck... Seen that look before..."
    $ remove_from_list(cass.conversation_topics,"rape")
    jump school_class_normal_end

label school_class_normal_cassmira_12:
    show mira at right2
    show cass laugh at right1
    with dissolve
    cass.name "... and we... Y'know..."
    mira.name "Oh? Good for you. Will you see him again?"
    cass.name "Dunno. Probably not. But it was nice anyway."
    mira.name "Mmmm."
    pc "Ooooh. This what I think it is?"
    cass.name "Yup!"
    $ remove_from_list(cass.conversation_topics,"lover")
    jump school_class_normal_end

label school_class_normal_cassmira_13:
    show mira at right2
    show cass worried at right1
    with dissolve
    cass.name "...been more careful!"
    pc "Morning."
    show cass angry
    cass.name "Fuck this morning!"
    hide cass with dissolve
    pc "Something I said?"
    mira.name "Something her pregnancy test said."
    pc "Oh? Fuck..."
    mira.name "Yeah..."
    $ remove_from_list(cass.conversation_topics,"pregnant")
    jump school_class_normal_end





label school_class_normal_nomira:
    $ rand_choice = WeightedChoice([
    ("school_class_normal_nomira_1", 1),
    
    

    ])
    jump expression rand_choice

label school_class_normal_nomira_1:
    "Placeholder event for when mira goes missing."
    jump school_class_normal_end





label school_class_normal_nocass:
    $ rand_choice = WeightedChoice([
    ("school_class_normal_nocass_1", 1),
    ("school_class_normal_nocass_2", 1),
    ("school_class_normal_nocass_3", 1),
    ])
    jump expression rand_choice

label school_class_normal_nocass_1:
    show mira at right1 with dissolve
    pc "[cass.name] off flirting with the boys?"
    mira.name "Heh, that wouldn't be too bad."
    pc "Mmm. She's been a bit down recently."
    mira.name "Well, yeah I suppose so."
    pcm "Hmmm..."
    jump school_class_normal_end

label school_class_normal_nocass_2:
    show mira at right1 with dissolve
    pc "On your own?"
    mira.name "Yeah, [cass.name] wasn't waiting for me this morning."
    pc "Oh? Hope she's ok."
    mira.name "Probably trying to avoid any troubles round here?"
    pcm "Hmmm..."
    jump school_class_normal_end

label school_class_normal_nocass_3:
    show mira at right1 with dissolve
    pc "Morning."
    mira.name "Oh? Morning."
    pc "Everything ok?"
    mira.name "Yeah, just thinking about [cass.name]."
    pc "Oh? Not sure you could handle her."
    mira.name "Pfft. No way could I handle her. Just wondering why she didn't come today."
    pc "Ah..."
    jump school_class_normal_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
