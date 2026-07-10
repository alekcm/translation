label school_dance_show_8:
    pause 0.5
    $ school_dance_quest_show_count += 1
    $ walk(loc_school_gym, trans=False)
    show svet dance at right1 with dissolve
    svet.name "Okay [dancet], gather round."
    show rachel dance at left3 with dissolve
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "Last time went quite well on the money front. We up for it again?"
    show dani happy
    dani.name "Sure. We earned quite a lot last time."
    show rachel happy
    rachel.name "Whoo!"
    $ add_to_list(rachel.list, "no_location")
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(anabel.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    hide rachel with dissolve
    anabel.name "Errr..."
    hide dani with dissolve
    pc "Err, okay then..."
    hide anabel
    hide svet
    $ walk(loc_school, trans=False)
    hide anabel
    hide svet
    with dissolve
    pause 0.2
    $ walk(loc_busstop_school)
    $ remove_from_list(rachel.list, "no_location")
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(anabel.list, "no_location")
    $ remove_from_list(svet.list, "no_location")
    show dani dance at right1 with dissolve
    dani.name "Come on [anabel.nname]! Bus is already here."
    hide dani with dissolve
    $ walk(loc_bus_interior)
    $ player.face_worried()
    with dissolve
    pc "Ung!"
    show rachel dance at left1 with hpunch:
        xzoom -1
    rachel.name "Hup!"
    rachel.name "Tight squeeze as usual."
    $ player.face_neutral()
    pc "Mmm."
    rachel.name "This is all more fun than I expected."
    pc "Really? You're having fun?"
    rachel.name "Sure, you're not?"
    if player.check_sex_agree(3, exhibitionist=True):
        pc "Well, sure. I guess it's pretty fun."
    else:
        pc "Eh, still feel a bit awkward."
    $ player.grope_poke()
    $ player.face_shock()
    with vpunch
    if player.check_sex_agree(5):
        $ player.face_surprised()
        pc "Uwaaaa!"
        rachel.name "Errr..."
        rachel.name "Having fun?"
        pc "Ung..."
        if player.isslut:
            $ player.face_happy()
            pc "Some guy is jamming his cock into me."
            pc "If I didn't have knickers on he'd probably already be fucking me."
            show rachel happy
            rachel.name "I can take 'em off for you if you want."
        else:
            rachel.name "Ha! Okay then."
    else:
        $ player.face_shock()
        pc "Ugn!"
        pc "Wha..."
        rachel.name "Err, having fun?"
        $ player.face_annoyed()
        pc "Wouldn't call it that."
        with hpunch
        pc "Shoo!"
    $ player.sex_cum(nosex, "ass")
    $ player.face_confused()
    pc "Ah no..."
    if player.isslut:
        pc "Too late..."
    else:
        pc "Shit..."
    $ player.grope_end()
    $ player.face_annoyed()
    pc "..."
    rachel.name "Well, he left quick."
    pc "Ugh. Not before ruining my pants."
    rachel.name "Don't worry, I have some stuff in [svet.nname]'s bag. I can give you a new pair."
    pc "..."
    pc "Thanks."
    rachel.name "We're here. Come on cummy pants."
    pc "Ugh!"
    hide rachel with vpunch
    pause 0.5
    $ walk(loc_busstop_residential, trans=hpunch)
    pcm "Ugh. My pants are all wet."
    pcm "Idiot!"
    $ walk(loc_park, trans=False)
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    with dissolve
    svet.name "We got everyone?"
    show dani dance at left2
    with dissolve
    dani.name "Yup."
    svet.name "Ok, like before, [rachel.name], you are on hat duty."
    show rachel happy
    rachel.name "Right!"
    show rachel with dissolve:
        xzoom 1
    rachel.name "[name] will join me. Come on."
    pc "I will? Ok."
    $ walk(loc_bushes, trans=False)
    hide dani
    hide anabel
    hide svet
    with dissolve
    rachel.name "Here you go. Swap into these."
    if player.has_perk(perk_commando, notif=True):
        $ add_to_list(quest_dance.list, "messy_wore_commando")
        pc "Err, actually I think I will go without."
        rachel.name "Really? Going to have a lot of fun like that."
        if player.has_perk(perk_exhibitionist, notif=True):
            pc "Hope so."
        else:
            pc "Mmm, might end badly but we will see."
        rachel.name "Haha!"
        show sb_pose_upskirt with dissolve
        pc "Already doesn't hide much. But here goes..."
        $ c.pants = 0
        $ work.pants = 0
        rachel.name "Let's go you pervert."
        pc "You're one to talk."
        hide sb_pose_upskirt with dissolve
    else:
        $ wardrobe.take(item_pants_5, all_notif=True)
        $ add_to_list(quest_dance.list, "messy_wore_thong")
        $ player.face_worried()
        pc "Err, already showing off enough of my arse and you want me to wear those? They are tiny."
        rachel.name "Yeah, you will get all the fun."
        hide rachel with dissolve
        pcm "Ugh. Tiny little skirt and now a pink thong..."
        pcm "Well, no choice unless I just go home."
        $ work.pants = 5
        $ work.pants_primary_colour = "pink"
        $ work.pants_secondary_colour = "pink"
        $ c.pants = 5
        $ c.pants_primary_colour = "pink"
        $ c.pants_secondary_colour = "pink"
        show sb_pose_upskirt with dissolve
        if player.check_sex_agree(5):
            $ player.face_normal()
            pcm "Well, shake my arse in front of a crowd..."
            $ player.face_happy()
            pcm "Might be fun."
        else:
            pcm "This is going to end badly..."
            pcm "Ugh, no choice."
        hide sb_pose_upskirt with dissolve
    $ walk(loc_park)
    show dani dance at right1 with dissolve
    dani.name "Everything ok? We are almost ready."
    if not c.pants:
        pc "Yeah, just had an issue with my knickers thanks to the bus."
    else:
        pc "Yeah, just had to swap out my knickers thanks to the bus."
    dani.name "Ah... Right."
    hide dani
    hide rachel
    with dissolve
    $ show_dance_image()
    "Me and the girls do our routine like we have done many times before. We are much more practised now both in the dance and in entertaining the crowd. Today seems especially lively."
    $ renpy.scene()
    show dance_behind
    with dissolve
    if c.pants:
        "I am fairly conscious of the fact I am wearing not only a tiny pair of pants, but a bright pink pair that really attracts attention from the watching men."
    else:
        "I am fairly conscious of the fact I have nothing under my skirt. It's clear the men have noticed as well as I seem to be getting way more comments than usual."
    "But I fall into rhythm and keep on dancing."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_18
    if c.pants:
        "When working the crowd and getting tips though, it's clear I am the popular choice. My pants have definitely brought me more attention than the rest of the girls."
    else:
        "When working the crowd and getting tips though, it's clear I am the popular choice. My lack of pants have definitely brought me more attention than the rest of the girls."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_19
    "While it is making my hat a lot more heavy than usual, there is hardly a moment when someone isn't pressing their arm against my chest or just blatantly putting their hand up my skirt."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_20

    "Things eventually start getting a lot more gropey than I would like, so I squeeze through the crowd and try to find the other girls."
    $ renpy.scene()
    with dissolve
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    show rachel with dissolve:
        xzoom 1
    rachel.name "Ah, finally got back."
    pc "Yeah... Just about."
    show dani happy with dissolve:
        xzoom 1
    dani.name "Thought we would have to send a search party."
    pc "Did pretty well today. This thing is so full with coins it's almost weighing me down."
    show rachel happy
    if c.pants:
        rachel.name "Seems a flash of pink is just what the wallet needed."
    else:
        rachel.name "Seems [name]'s show is just what the wallet needed."
    show dani happy
    dani.name "Ha, maybe."
    anabel.name "Huh? What do you mean?"
    svet.name "Well let's see how much we got then..."
    show dani:
        xzoom -1
    show rachel:
        xzoom -1
    with dissolve
    svet.name "Wow, [name] did pretty well today. Got almost double what anyone else did."
    $ player.add_money(65)
    show dani with dissolve:
        xzoom 1
    dani.name "Oooh, good for you."
    show anabel with dissolve:
        xzoom 1
    anabel.name "How did you manage that?"
    show rachel with dissolve:
        xzoom 1
    if c.pants:
        rachel.name "Pink power!"
    else:
        rachel.name "Pussy power!"
    dani.name "See you guys. Got to go."
    hide svet
    hide dani
    with dissolve
    anabel.name "Huh?"
    pc "She's making fun of my underwear."
    show rachel at right1
    show anabel at right2
    with dissolve
    anabel.name "Oh? What's so funny about them?"
    if c.pants:
        pc "They are pink."
        anabel.name "Ok... Ah! Right... That brought in more money?"
        pc "So [rachel.name] thinks."
        rachel.name "Of course they did!"
    else:
        pc "They got soiled on the bus so I kinda had to get rid of them."
        anabel.name "So?"
        pc "I didn't have any replacements."
        anabel.name "What? So you are..."
        rachel.name "Totally showing off her gash!"
        anabel.name "I... Err... Wha..."
    rachel.name "Anyway, I'm going home."
    anabel.name "Erm... Where did [dani.nname] get to?"
    rachel.name "Ah, some guy took a liking to her so asked [svet.name] to introduce them."
    anabel.name "Ah... Ok... Wonder if I should wait."
    rachel.name "Probably not. Anyway, see you guys."
    pc "Mm. See you."
    hide rachel with dissolve
    anabel.name "Well, I don't want to hang around alone with this skirt on so I'll be going too. See you [name]."
    pc "Right. Be safe."
    hide anabel with dissolve
    if player.has_perk([perk_gamine, perk_whore, perk_slut, perk_bimbo]) or player.check_sex_agree(4, notif=False) or player.check_speech(4, notif=False):
        pcm "Hmmm, asked to introduce them?"
        pcm "Maybe [dani.nname] will get home with more money than she thought."
    $ add_to_list(dani.conversation_topics, "dance_went_alone")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
