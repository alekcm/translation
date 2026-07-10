label school_dance_show_10:
    $ school_dance_quest_show_count += 1
    $ add_to_list(rachel.list, "no_location")
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(anabel.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    $ walk(loc_school_gym)
    show svet dance1 at right1
    show rachel dance at left3
    with dissolve
    svet.name "Err, changed your outfit?"
    if c.pants:
        rachel.name "Yeah, we got a lot less last time than pink [name] got. So thought we should spice things up."
    else:
        rachel.name "Yeah, can't let [name] do all the work so I thought we should spice things up."
    show anabel dance1 at left1
    with dissolve
    anabel.name "Err, showing a lot more than before..."
    anabel.name "And before didn't hide much at all."
    show dani dance at left2
    with dissolve
    dani.name "Like this?"
    show rachel with dissolve:
        xzoom 1
    rachel.name "Watch out [name], won't be just you raking it in."
    pc "Err, no problem?"
    anabel.name "You're okay with this [dani.nname]?"
    show dani with dissolve:
        xzoom 1
    dani.name "[name] made almost double than the rest of us. If we all do the same and get double then the total will be double."
    anabel.name "Yeah, but dressed like this?"
    dani.name "Not like the stuff we were wearing before hid much. Why not just go all out and earn a fortune?"
    pc "Where did you even get the top from?"
    rachel.name "Ah, I got ones for everyone. Come on [name], I'll show you."
    pc "Err..."
    hide anabel
    hide dani
    hide svet
    $ walk(loc_school_locker_girls)
    rachel.name "Hmmm, what one for you... Ah, here we go!"
    $ wardrobe.take(item_pants_5, all_notif=True)
    $ wardrobe.take(item_top_19, all_notif=True)
    if c.pants:
        rachel.name "Put it on and change your knickers while you're at it."
    else:
        rachel.name "Put it on. With this and your bare arse, it should do the job."
    hide rachel with dissolve
    pcm "..."
    if player.check_sex_agree(3, exhibitionist=True):
        pcm "Well, no doubt this will earn a fair bit more money..."
    else:
        pcm "Err... Kinda small..."
    $ pc_striptease()
    $ work.bra = 0
    if player.has_perk(perk_commando):
        $ work.pants = 0
    else:
        $ work.pants = 5
    $ work.top = 19
    $ work.pants_primary_colour = "pink"
    $ work.pants_secondary_colour = "pink"
    pcm "Hmm, pink pants... Didn't see them wearing a bra either..."
    if player.has_perk(perk_commando):
        pcm "Guess they don't want to go commando like I have. Thought [rachel.name] at least would have been up for that."
    $ pc_dress_slow()
    pcm "Some serious underboob with this top. Going to be showing everything off when I lift my arms up."
    if player.check_sex_agree(4, exhibitionist=True):
        pcm "Probably earn more than double showing my tits off as well."
    else:
        pcm "Will be showing off a lot more than just the pink knickers..."
    show anabel dance1 at right1 with dissolve
    anabel.name "..."
    anabel.name "The top is tiny..."
    pc "Yeah, kind of shows a lot of what's under."
    anabel.name "Not sure I would even fit in it..."
    show dani dance at right2 with dissolve:
        xzoom -1
    dani.name "Come on [anabel.nname]! Squeeze your ass in those knickers and let's go!"
    anabel.name "Err, I am not..."
    hide dani with dissolve
    anabel.name "...sure I will fit..."
    anabel.name "She isn't listening."
    pc "Only hearing the money clinking in a hat by the look of things."
    anabel.name "Seems like it..."
    $ walk(loc_school_gym, trans=False)
    hide anabel
    show rachel dance at right1
    show dani dance at right2
    with dissolve
    rachel.name "Looking good."
    if player.has_perk([perk_exhibitionist, perk_bimbo, perk_slut], notif=True):
        pc "Thanks. Though you sure wearing this isn't going to wind up with us all arrested?"
    else:
        pc "Looking almost naked."
        rachel.name "Almost. Not sure I could remove any more without us getting arrested."
        pc "Not sure we won't be getting arrested wearing this."
    rachel.name "Only one way to find out."
    hide rachel with dissolve
    pc "[anabel.nname] is taking a while."
    if player.breasts == 3:
        dani.name "Getting those melons in her top is probably taking a while. You managed to squeeze yours in pretty quick [name]."
    else:
        dani.name "Getting those melons in her top is probably taking a while."
    hide dani with dissolve
    pc "Yeah..."
    $ walk(loc_school)
    pause 0.2
    $ walk(loc_busstop_school, trans=False)
    show dani dance at right1
    with dissolve
    pc "You seemed pretty eager to switch clothes."
    dani.name "Well, not really."
    pc "Money?"
    dani.name "Always..."
    pc "Mmmm."
    show anabel dance at right2 with dissolve
    show dani happy
    dani.name "Ah. Managed it?"
    anabel.name "Just about. Why did you all rush off? We didn't even talk about if this is ok?"
    dani.name "It's fine. I'm sure we won't get told off for wearing this stuff."
    anabel.name "That's not..."
    dani.name "Ah, bus is here. C'mon."
    anabel.name "..."
    $ walk(loc_bus_interior, trans=False)
    $ player.face_worried()
    hide dani
    hide anabel
    with dissolve
    pcm "Ugh, this place stinks..."
    $ remove_from_list(rachel.list, "no_location")
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(anabel.list, "no_location")
    $ remove_from_list(svet.list, "no_location")

    if player.has_perk([perk_slut, perk_exhibitionist, perk_bimbo, perk_bambi, perk_broken]):
        show rachel dance at left1 with dissolve:
            xzoom -1
        rachel.name "Squeezing in here is becoming a chore."
        pc "Mmm."
        rachel.name "Wanna have some fun?"
        $ player.face_conf()
        pc "What?"
        rachel.name "Hmmm, I wonder with who..."
        pc "What are you up to?"
        rachel.name "Hmm, I think him..."
        $ player.face_shock()
        with hpunch
        pc "Ah."
        with vpunch
        pc "What are you up to? Why are you pushing me?"
        rachel.name "Not so loud or they will know."
        pc "Know what? I don't even know..."
        $ player.grope_hips()
        pc "Ai!"
        rachel.name "Calm down."
        rachel.name "Have some fun."
        pc "What are you talking..."
        $ player.grope_poke()
        pc "Fuck! This your plan?"
        rachel.name "He take the bait?"
        pc "If you mean is he poking me, yes."
        $ player.face_normal()
        pc "Ugh, you are worse than me..."
        if c.pants:
            rachel.name "Yeah yeah, let me help you."
            $ player.face_worried()
            pc "Huh?"
            rachel.name "C'mere."
            pc "Why are you putting your hands up..."
            $ c.pants = 0
            $ player.face_shock()
            with vpunch
            pc "Oh shit."
        rachel.name "Haha!"
        $ player.face_worried()
        pc "You serious?"
        rachel.name "Perk you up before the dance."
        pc "He's going to do a lot more than that."
        $ player.grope()
        rachel.name "Good for you."
        $ player.face_shock()
        with hpunch
        pc "Hey."
        with hpunch
        pc "You trying to get me impaled?"
        $ player.face_worried()
        rachel.name "Of course."
        $ player.grope()
        pc "Oh shit! He's poking..."
        rachel.name "Mmm?"
        $ player.face_shock()
        with vpunch
        pc "Aie!"
        pcm "I'm getting fucked at this rate..."
        $ player.face_normal()
        menu:
            "Resist":
                pcm "Can't let this get too far..."
                with vpunch
                pc "I'm out of here before it goes too far."
                rachel.name "Ah? Shame."
                hide rachel
                $ player.grope_end()
                with vpunch
                pc "Ung!"
                pcm "That crazy idiot. Pushing me on some guy..."
                pcm "..."
                pcm "Was kind of fun though..."
                if work.pants:
                    pcm "Ah shit!"
                    pcm "I don't have my knickers..."
                show dani dance at left2 with dissolve:
                    xzoom -1
                dani.name "Ugh!"
                dani.name "Not sure I could count the hands that grabbed me. Looks like you are having it easier so I'll hang out with you."
                pc "Not sure it was easier. Had to escape here myself."
                dani.name "Oh?"
                dani.name "Well, it's our stop anyway."
                hide dani with hpunch
                pause 0.5
                $ walk(loc_busstop_residential)
                $ renpy.scene()
                show rachel dance at right1
                show anabel dance at right2
                with dissolve
            "Go along with it" if player.check_sex_agree(4):
                pc "He's going to poke in me..."
                rachel.name "Good. Next time I'll let him poke me."
                pc "Ugh, you slut."
                $ player.grope_insert()
                $ player.sex_vag(busgroper, quest_dance)
                pc "Unnng."
                rachel.name "Oooh, it go in?"
                pc "Fuck."
                rachel.name "Oh, so yes."
                $ player.face_mmm()
                pc "Mmmmm..."
                "I am not sure what [rachel.name] is saying to me any more and I just close my eyes and enjoy the feeling."
                "The guy behind me knows I am a slut who came here for this, so he doesn't really try to hide what he is doing so puts his hands on my hips."
                "With him pulling me towards him and the jumping and rocking of the bus, I am gently fucking him without making any movements of my own."
                "Although it's not a vigorous pace, the whole naughtiness of the situation has me horny as all hell and I am pretty close... I can feel it..."
                pc "Ahhhhh..."
                $ player.sex_cum(nosex,"self")
                pc "Unnnnng!"
                pc "Haaaa fuuuuck..."
                $ player.face_normal()
                pc "Fuuuuuu..."
                rachel.name "Good going. Our stop is close so you better hurry it up or you'll be left behind."
                pc "I got what I wanted, so it's him that needs to hurry if he..."
                show dani dance at left2 with dissolve:
                    xzoom -1
                dani.name "Ugh!"
                rachel.name "Hey."
                dani.name "Not sure I could count the hands that grabbed me. Looks like you are having it easier so I'll hang out with you."
                rachel.name "Yup, no perverts here."
                dani.name "Well, it's our stop anyway."
                hide dani with hpunch
                rachel.name "No perverts at all."
                hide rachel with vpunch
                pcm "Sorry fella."
                $ player.sex_end()
                $ player.grope_end()
                $ walk(loc_busstop_residential, trans=False)
                $ renpy.scene()
                with dissolve
                "I don't even give the guy a look and just walk away with his cock slipping out of me. He is just a bus deviant anyway so no need to care he didn't finish his fun."
                show rachel dance at right1
                show anabel dance at right2
                with dissolve


    elif "dance_waited_during_date" in dani.conversation_topics:
        show dani dance at left1 with dissolve:
            xzoom -1
        dani.name "Even worse now wearing this stuff."
        pc "Yeah?"
        pc "So you meeting your friend again tonight?"
        if "dance_waited_police" in dani.conversation_topics:
            dani.name "Yeah, sorry about getting you into trouble with security last time."
            if "dance_waited_police_blowjob" in dani.conversation_topics:
                pc "Yeah, next time I'll make sure it's you sucking his cock to get us out of trouble."
                show dani worried
                dani.name "What? You had to do that? I thought you bribed him?"
                pc "Yeah, you think I have cash to give to him?"
                dani.name "Shit... Sorry..."
                dani.name "I didn't realise."
                show dani neutral
            else:
                pc "Ah no worries. He was just being an arse."
                dani.name "Yeah?"
                pc "Thought I was whoring in the park and probably wanted a freebie."
                dani.name "Oh? That happens?"
                pc "Obviously. Security are full of cunts."
                pc "Be careful with them if you continue to do this kind of work."
                dani.name "Yeah..."
        else:


            dani.name "Yeah, though no need for you to hide in any more bushes. I'll be fine on my own."
            if "dance_waited_interrupt" in dani.conversation_topics:
                dani.name "Unless you want to be jumped on by some weirdo again."
                pc "No thanks. Getting harassed in the bushes once is enough for me."
                pc "Can't hide anywhere practically naked these days without someone jumping out on you."
                dani.name "Haha!"
            else:


                dani.name "Unless you want a repeat performance from some weirdo."
                pc "I'll think about it."
                dani.name "Haha."
                dani.name "I started to look for a rock to hit him over the head with."
                pc "Oh?"
                dani.name "Took me a while to realise it wasn't what I thought it was."
                pc "Ah well. I got a bit carried away."
                dani.name "I saw."
                pc "Spying on us were you. You peeping tom!"
                pc "I didn't realise that was your thing."
                dani.name "Ow shush or I'll hit you with the rock next time."

        if "dance_waited_interrupt_left" in dani.conversation_topics:
            dani.name "Is that why you left early?"
            pc "Ah, no. Not really."
            pc "Left early because it's you getting paid so no need for me in there with you. He seemed decent enough."
            pc "It all end ok?"
            dani.name "Yeah was fine. He just..."
            pc "Got what he paid for."
            dani.name "Ah no it wasn't like that."
            pc "I don't need to know. As long as he paid up it's all good."
            dani.name "Mmm. I suppose."
        else:
            dani.name "Well, thanks for hanging around after that."
            pc "Mmm, no problem."
            pc "You know he's going to want more from you right?"
            dani.name "Yeah I know..."
            dani.name "As long as he keeps paying then everything is okay right?"
            pc "I guess."
            pc "Not like there is any other reason to do it."
            dani.name "Mmm."


        dani.name "Anyway, looks like our stop is coming up."
        dani.name "Ung!"
        hide dani with vpunch
        pause 0.5
        $ walk(loc_busstop_residential)
        $ renpy.scene()
        show rachel dance at right1
        show anabel dance at right2
        with dissolve
    else:
        show anabel dance at left1 with dissolve:
            xzoom -1
        anabel.name "Feels like everyone is looking at me."
        pc "They probably are."
        anabel.name "Ugh. Really doesn't hide much does it?"
        pc "Err..."
        anabel.name "Yeah yeah. Big arse. Very funny."
        pc "I wasn't going to say anything."
        anabel.name "Thinking it though."
        pc "Maybe..."
        pc "Hey, at least everyone in the bus is happier because of it."
        anabel.name "Wonderful."
        $ player.face_happy()
        pc "Who knows. You might pied piper half the bus to our show and get us more tips."
        anabel.name "Let's see. Our stop is coming up."
        $ player.face_neutral()
        anabel.name "Move!"
        hide anabel with hpunch
        pcm "Would think someone like her would be used to the attention by now..."

    rachel.name "Everyone off?"
    show dani dance at right3 with dissolve
    dani.name "Ugh."
    rachel.name "Made it this time?"
    dani.name "Yeah, don't remind me."
    hide dani with dissolve
    hide rachel
    hide anabel
    with dissolve
    $ walk(loc_park)
    $ renpy.scene()
    with dissolve
    show svet dance at right1 with dissolve
    svet.name "Everyone here?"
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    show rachel happy
    rachel.name "Yup!"
    svet.name "Ok, you all know what to do so let's get to it."
    rachel.name "Right!"
    $ renpy.scene()
    with dissolve
    "We spend a bit of time clearing away some space to dance. It looks like people have come to expect us around here because people have already started gathering and watching us."
    $ show_dance_image()
    "We do our usual routine as we have practised and the crowd is extremely lively. There is a lot of hollering and whistling while we dance."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_25
    "[dani.nname] is playing the crowd quite well this time round and of course [rachel.name] is being as good as she always is. [anabel.nname] on the other hand seems a lot more withdrawn."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_26
    if c.pants:
        "I try to get with the stride [dani.nname] and [rachel.name] are setting and keep up with them. Although I feel quite self conscious about the new top I am wearing. I am sure it is showing off a lot more than I would like."
    else:
        "I try to get with the stride [dani.nname] and [rachel.name] are setting and keep up with them. But with the lack of underwear and our new top, I am sure I am giving people a show that is just short of a striptease."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_27
    "But I push it out of my mind and go along with it. It's clear the sexier the clothes, the more money people donates. So I just accept it is part of the show and go along with it."
    "All of us but [anabel.nname] work the crowd and try to tempt tips out of people. As expected, the men get very close and many of them grope and touch us."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_28
    "The show comes to an end and we all make some final rounds with hat in hand to get as much money as we can."
    $ player.grope()
    if not c.pants:
        "My lack of underwear makes intrusions much easier and it looks like most of the perverts have noticed I am not wearing anything because many seem to target me specifically."
    "I suffer the invading hands as best I can until it looks like the only people left are those who have no intention of tipping. So I make my way over to the rest of the girls."
    $ player.grope_end()
    $ renpy.scene()
    with dissolve
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "Good job girls. Let's see what we have here..."
    svet.name "...[rachel.name]'s... [name]'s..."
    svet.name "There we go."
    if not c.pants:
        svet.name "Hmm, how did you manage to earn far more than the rest again [name]?"
        rachel.name "Secret!"
        pc "Ugh."
    if not c.pants:
        $ player.add_money(100)
    else:
        $ player.add_money(70)
    dani.name "Fucking hell!"
    rachel.name "Wow!"
    anabel.name "So the clothes do make such a difference?"
    rachel.name "Told ya! This is a fortune!"
    dani.name "It is. Thanks [rachel.name]."
    rachel.name "Mmmm. I'm gonna go have a shower then get shit faced. See you."
    dani.name "Bye."
    hide rachel with dissolve
    svet.name "Good job girls. At this rate we can make this a regular thing."
    dani.name "Yeah, seems all the trouble was worth it."
    anabel.name "I'm heading home. See you next time."
    dani.name "Bye [anabel.nname]."
    hide anabel with dissolve
    svet.name "See you."
    hide svet with dissolve
    show dani with dissolve:
        xzoom 1
    if "dance_waited_during_date" in dani.conversation_topics:
        pc "Meeting your friend here?"
        dani.name "Yeah, I'd better go to the bathroom and clean up a bit."
        pc "Right, be safe."
        dani.name "You too."
    else:
        pc "You heading home?"
        dani.name "No, I'm meeting someone so won't be heading back just yet."
        pc "Ok, well, have fun."
        dani.name "You too."
    hide dani with dissolve
    $ player.face_worried()
    pcm "Ah fuck!"
    show sb_pose_upskirt with dissolve
    pcm "Always left alone here with my arse hanging out..."
    if c.pants:
        pcm "And this time I am wearing tiny pink undies that everyone will notice..."
    else:
        pcm "And literally hanging out. Not even the pink pants to cover some modesty."
        pcm "Damn [rachel.name]!"
    hide sb_pose_upskirt with dissolve
    if not c.pants:
        $ male_npc_create_all()
        $ tempname = punter
        $ quest_temp = quest_dance
        show male_generic at right1 with dissolve
        man "Hey darling, you up for some after dance fun?"
        pc "Err, you mean what I think?"
        $ player.set_whore_price(3)
        man "Some fun alone in the toilets for £[player.soldprice]?"
        if player.check_whore_agree_choice():
            man "Lead the way."
            pc "Okay."
            show male_generic at left1 with dissolve
            $ walk(loc_park_toilet)
            pc "Should be fine in here."
            $ walk(loc_park_toilet_girls)
            show dani dance at right1 with dissolve
            pc "Ah, [dani.nname]."
            if "dance_waited_during_date" in dani.conversation_topics:
                dani.name "Ooh, have fun."
                pc "Sure, you too."
            else:
                dani.name "Hey, just washing up before heading home."
                pc "Right."
            hide dani with dissolve
            show male_generic at right6 with dissolve
            jump whore_sex_start
        else:
            pc "Sorry mate, might look like a whore but not up for that."
            man "Right, I'll ask one of your friends."
            pc "Sure, have fun."
            hide male_generic with dissolve
            pc "..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
