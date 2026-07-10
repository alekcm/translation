label school_dance_show_12:
    $ school_dance_quest_show_count += 1
    $ add_to_list(rachel.list, "no_location")
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(anabel.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    $ walk(loc_school_gym)
    show svet dance at right1 with dissolve
    svet.name "Looks like everyone is here now. Gather round girls."
    show rachel dance at left3
    show anabel dance at left1
    with dissolve
    show dani dance neutral at left2
    with dissolve
    svet.name "So, it looks like our dancing in the park attracted some attention and we now have a proper gig to do."
    anabel.name "What? Tonight?"
    svet.name "No, today we will do like we have been doing and dance for tips in the park."
    svet.name "But next time we will have this private gig."
    rachel.name "Oh? What are we supposed to do?"
    svet.name "Still getting the details, but it looks like it's some kind of private party and we have been hired as entertainment."
    anabel.name "So turn up and dance for the people paying?"
    svet.name "Not entirely. The party will go on until the early hours so this will be a full day's work for us all."
    svet.name "In between sets, we are to act as servers and deliver food and drink to the guests."
    anabel.name "Like waitresses?"
    svet.name "I guess so. I am still speaking with the organiser to figure out how many people will be there, but so far it seems like it will be a smallish party."
    rachel.name "Rich twats with more money than sense sounds like."
    svet.name "Pretty much."
    dani.name "And how much are they paying?"
    svet.name "A lot."
    svet.name "We will all get a fixed fee for the dancing and serving. But the organiser claims there will be more to be made in tips."
    rachel.name "How'd you meet the fool in the first place?"
    if "dance_waited_interrupt" in dani.conversation_topics:
        svet.name "He claimed to know [dani.nname] and [name]. Never met him before myself."
        rachel.name "You know who it is?"
        pc "Have a good idea who, yeah."
    else:
        svet.name "He claimed to know [dani.nname]. Never met him before myself."
        rachel.name "You know who it is?"
        dani.name "Yeah I think so."
    svet.name "Well anyway, the pay is good and dancing is what we are here for. So on Saturday, be ready for a big one since it will go on a lot longer than we usually spend in the park."
    dani.name "Saturday?"
    svet.name "Yeah, not our usual time. Meet at Revel at 9ish and we will head up there."
    $ log.assign("Dance VIP show")
    rachel.name "Right. So to the park for now?"
    svet.name "Yup, usual routine today."
    if "dance_waited_interrupt" in dani.conversation_topics:
        svet.name "[dani.nname], [name]. Let's have a chat about your friend."
        pc "Ok."
        hide anabel
        hide rachel
        with dissolve
        svet.name "I'm assuming he's someone who has been paying for extra dances?"
        if player.has_perk(perk_whore):
            pc "Yeah pretty much. He took a liking to [dani.nname]."
        else:
            pc "Err... I suppose so?"
        svet.name "He ever try to get stingy with the money?"
        dani.name "..."
        dani.name "I don't know..."
        svet.name "You don't?"
        if player.has_perk(perk_whore):
            pc "It was her first dance."
        else:
            dani.name "I... Never did this before..."
            dani.name "I don't know if it's good or not."
        svet.name "Oh?"
        if player.has_perk(perk_whore):
            svet.name "What did you make of him [name]?"
            if "dance_waited_interrupt_toilet" in dani.conversation_topics:
                pc "He seemed decent enough. We spent some time alone with him and he wasn't pushy or demanding."
                pc "Didn't seem like the usual degenerate and just someone wanting a little excitement."
            else:
                pc "Well, I didn't spend alone time with him but he wasn't your usual degenerate. Didn't seem so anyway."
            svet.name "You think it's safe to go ahead with it all?"
            pc "Depends on what you mean by safe."
            pc "Considering how we know him, he is probably expecting us to \"earn\" our tips and keep his guests company."
        else:
            svet.name "He ever do anything you didn't want him to?"
            dani.name "No. Actually he hasn't even asked... To do \"that\"."
            svet.name "He hasn't?"
            dani.name "No."
        svet.name "Hmmm."
        svet.name "Thanks."
        svet.name "I'll have another chat with him and see if it all seems ok. But looks like we will probably go there next time round."
        dani.name "Mmm."
        svet.name "Right, let's head out."
        hide svet with dissolve
        hide dani with dissolve
    else:
        svet.name "[dani.nname]. Let's have a chat about your friend."
        dani.name "Right."
        hide svet
        hide dani
        with dissolve

    $ walk(loc_school)
    $ remove_from_list(rachel.list, "no_location")
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(anabel.list, "no_location")
    $ remove_from_list(svet.list, "no_location")
    pause 0.2
    $ walk(loc_busstop_school)
    if "dance_waited_interrupt" in dani.conversation_topics:
        show rachel dance at right1
        show anabel dance at right2
        with dissolve
        rachel.name "Hurry up! The bus is arriving."
        hide anabel with dissolve
        hide rachel with dissolve
    else:

        show rachel dance at right1
        show anabel dance at right2
        with dissolve
        rachel.name "Oooh, an actual job. Sounds nice."
        anabel.name "Not done something proper since the market thing."
        rachel.name "Oh yeah, I forgot about that."
        anabel.name "How'd you forget? It was our first job."
        rachel.name "Feels like forever ago."
        anabel.name "Well, yeah."
        anabel.name "We at least worse tights then."
        show rachel happy
        rachel.name "Aw don't worry. People love your arse."
        show anabel worried
        anabel.name "Wha!?"
        rachel.name "All juicy. The guys love it."
        anabel.name "Hey! I don't..."
        show dani dance at right3 with dissolve
        dani.name "Still waiting on the bus?"
        rachel.name "Yeah, though I can see it coming now."
        rachel.name "Come on you exhibitionist."
        anabel.name "Me?"
        rachel.name "Who else?"
        hide rachel with dissolve
        anabel.name "Exhibitionist?"
        show dani happy
        dani.name "Well, you are spilling out everywhere."
        hide dani with dissolve
        anabel.name "Not like I chose to wear this..."
        hide anabel


    $ walk(loc_bus_interior)
    pcm "This place is as stinky as always..."
    show anabel dance at left1 with vpunch:
        xzoom -1
    anabel.name "Ung!"
    anabel.name "Always packed like sardines at this time."
    pc "Yeah."
    anabel.name "Didn't know [dani.nname] was making friends."
    pc "It's some guy that chats with her during the show. Just some idiot who took a liking to her I guess."
    anabel.name "From the shows?"
    pc "Yeah, how else would he know we are dancers?"
    anabel.name "Hmmm..."
    anabel.name "Think he is a pervert?"
    pc "He's a man. So of course he is."
    anabel.name "Hrmf."
    show dani dance at left2 with hpunch:
        xzoom -1
    dani.name "Ug!"
    dani.name "Perverts."
    if player.check_sex_agree(4):
        pc "Been having fun?"
    else:
        pc "Come here for an escape?"
    dani.name "These skirts just invite them don't they?"
    pc "Pretty much."
    show anabel angry with vpunch
    anabel.name "Ai!"
    dani.name "Sorry. That was me."
    show anabel worried
    anabel.name "Err... I don't think so..."
    anabel.name "Ung!"
    dani.name "Oh?"
    pc "Good job on getting us a new gig."
    dani.name "Oh? Didn't even know about it until [svet.nname] mentioned it just now."
    pc "Well, sounds like he is paying a lot, so good for us anyway."
    dani.name "Yeah. Though she didn't say how much."
    pc "Never heard her say \"a lot\" before, so guess it will be worth it."
    anabel.name "Ha!"
    anabel.name "I gotta go!"
    hide anabel with hpunch
    pc "Errr..."
    dani.name "It's our stop soon anyway. Let's go."
    hide dani with dissolve
    pc "Mmm."
    $ walk(loc_busstop_residential)
    show anabel worried dance at right1
    show dani dance at right2
    with dissolve
    anabel.name "...his finger in my arse!"
    dani.name "Oh? That makes a change. Normally they see those pillows you have and go for them."
    show anabel worried
    anabel.name "Very funny."
    hide anabel with dissolve
    dani.name "Wasn't making a joke..."
    dani.name "Let's go [name]."
    hide dani with dissolve
    $ walk(loc_park)
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "Right. You all know the drill by now. So let's get to it."
    rachel.name "Right!"
    $ renpy.scene()
    with dissolve
    "We spend a bit of time clearing away some space to dance under the watchful eye of the gathering crowd. People were here even before we arrived so they definitely expected us today."
    $ show_dance_image()
    "Our routine is much more impromptu this time round. Someone is pretty much always working the crowd and getting them more excited."
    "Even [anabel.nname] tries her hand at working the crowd this time. Though she usually makes a run for it back to the group when someone gets too handy with her."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_10
    "[rachel.name] seems to spend more time in the crowd than with the group. This ends up leaving me and [dani.nname] having to rescue her on a few occasions when it looks like she is getting in too deep."
    "[rachel.name] doesn't seem to mind though. She seems to enjoy the attention and probably wouldn't complain no matter what the unruly crowd did to her."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_11
    "As expected, the hands don't stop at [rachel.name]. Any one of us that winds up in the crowd is lucky to make it out fully clothed."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_12
    "But it's the price I have to pay to get all the tips flowing. We are earning more and more each time and it's all down to working the crowd."
    call school_dance_show_busk_start_call from _call_school_dance_show_busk_start_call_13
    "But time goes on and we are all pretty tired so call an end to the show. One last round in the crowd to gather up all the money in the hat before heading off."
    $ player.grope()
    "Of course knowing we are close to leaving, they get a lot more bold."
    $ player.grope()
    pcm "Damn perverts."
    $ player.grope()
    pcm "At least pay more if you're going to do this..."
    $ player.grope_end()
    $ renpy.scene()
    with dissolve
    show svet dance at right1
    show rachel dance at left3
    show anabel dance at left1
    show dani dance at left2
    with dissolve
    svet.name "Good job girls. Gather round."
    svet.name "Let's see... We have [dani.nname]'s... [anabel.nname]..."
    svet.name "There we go."
    $ player.add_money(120)
    svet.name "We did pretty well today."
    dani.name "Oooh."
    anabel.name "That's quite a lot..."
    rachel.name "Mmmm. Good job guys!"
    svet.name "Right. Well I'm off to meet this new client. You coming [dani.name]?"
    dani.name "Yeah, See you."
    hide dani
    with dissolve
    svet.name "Don't forget. Saturday, 9ish at Revel."
    hide svet
    with dissolve
    show rachel with dissolve:
        xzoom 1
    rachel.name "So, a big one next time. Make sure to get a lot of sleep. Can't have you all passing out."
    anabel.name "Right."
    rachel.name "See you smelly lot next time."
    hide rachel with dissolve
    show anabel with dissolve:
        xzoom 1
    anabel.name "Big one next time. Uff..."
    pc "Pay should be good."
    anabel.name "I guess."
    pc "Not to worry. It should be fun. Dancing is what we are here for after all. Maybe the party will be less touchy feely than these park deviants."
    anabel.name "Yeah, we'll see."
    anabel.name "Anyway, I'm off. Don't want to stand round here with these perverts still around."
    pc "Right. See you."
    hide anabel with dissolve


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
