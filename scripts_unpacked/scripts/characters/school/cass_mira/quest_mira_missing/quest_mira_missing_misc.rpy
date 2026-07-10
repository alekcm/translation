



label quest_mira_missing_cass_approach:
    show cass worried at right1 with dissolve
    cass.name "Hey [name], got a moment?"
    pc "Sure, what's up?"
    cass.name "You haven't seen [mira.name] around have you?"
    pc "Err, maybe? Err, not for a few days I think. Why?"
    cass.name "Well, she isn't coming to school. I thought she was sick so went to her house but she isn't there either."
    pc "Maybe you just missed her or something?"
    cass.name "No, her flatmates haven't seen her either. I'm a bit worried."
    pc "It's probably fine. She might just be staying with a friend or something."
    cass.name "Not sure about that. Could you ask around anyway and see if anyone has seen her?"
    pc "Err, I guess I can."
    cass.name "Thanks."
    hide cass with dissolve
    pcm "Hmm, I said she might be seeing a friend, but people don't just go missing like that."
    pcm "Hope everything is ok."
    $ log.assign("Find Mira")
    jump travel






label quest_mira_missing_robin_mira_ask:
    pc "You haven't seen [mira.name] around have you?"
    robin.name "Err, that's the short one isn't it?"
    pc "Yeah."
    robin.name "Not really. But I don't know her well so don't pay attention."
    pc "Mmmm."
    robin.name "Why? There a problem?"
    pc "Hopefully not."
    $ add_to_list(robin.list, "asked_about_mira")
    jump robin_talk_end



label quest_mira_missing_pc_knows:
    pcm "Hmmm, thinking about it, [mira.name] worked the highway..."
    pcm "If she's gone missing, it would probably have to do with something there."
    pcm "Ugh, but going to have to tell [cass.name] about it."
    $ log.markdone("mira_missing_01")
    jump travel



label quest_mira_missing_soccer_hangout_mira_ask:
    pc "You guys haven't seen [mira.name] around have you?"
    nate.name "No, something wrong?"
    pc "Not sure, [cass.name] is worried because [mira.name] hasnt been around for a while."
    nate.name "I'm sure she will turn up. Probably just sick or something."
    pc "Mmm, hope so."
    $ add_to_list(dan.list, "asked_about_mira")
    jump school_field_soccer_hangout_conv_end

label quest_mira_missing_dan_approach:
    show dan at right1 with dissolve

    dan.name "Hey."
    pc "Err, hey [dan.name]."
    dan.name "You find out anything more about [mira.name]?"
    if not log.interactive("mira_missing_01"):
        pc "Err, yeah..."
        pc "I managed to dig up some stuff."
        dan.name "Right, so you know where she worked?"
        pc "You knew?"
        dan.name "Yeah, was going to tell you but seems I don't need to."
        pc "Right."
        hide dan with dissolve
        pc "Err, bye?"
        pcm "Hmm, so he knew about what she did. Strange."
        pcm "Though [dan.name] does do some shady stuff with beers and whatever round that way. So maybe he bumped into her."
    else:
        pc "No, you seen her?"
        dan.name "No. But you are looking for so you should probably know..."
        pc "Know what?"
        dan.name "She worked the highway. If she's gone missing then it's probably there."
        pc "Wait what? Worked the highway? You cant mean what it sounds like."
        dan.name "It is. I go round that way for beers and stuff. Seen her a few times."
        pc "No. C'mon. Must have been someone else."
        dan.name "It wasn't. We spoke..."
        dan.name "We are friends."
        pc "Really? I've never seen you talking to her."
        dan.name "Yeah. On purpose. Easier to hide things."
        dan.name "If you need some help, tell me."
        pc "Err, right..."
        hide dan with dissolve
        pc "Bye?"
        pcm "They were friends?"
        pcm "Hmmm. Well [dan.name] does do some shady stuff round that way for beers and whatever else."
        pcm "So it might make sense he saw her..."
        pcm "Fuck, will have to speak to [cass.name] about this."
        $ log.markdone("mira_missing_01")
    $ add_to_list(dan.list, "told_about_mira")
    jump travel





label quest_mira_missing_return_to_cass:
    show cass at right1 with dissolve
    if "met_whore_mira_as_whore" in mira.list:
        $ add_to_list(quest_whore.list, "cass_knows")
        pc "So... There is probably something you should know."
        show cass laugh
        cass.name "Is it about [mira.name]?"
        pc "Yeah... I might know where to look for her."
        show cass neutral
        cass.name "Really?"
        pc "So not sure if you know. But to make some money I work up the highway sometimes."
        cass.name "Err, okay. Not seeing what that has to do with it."
        pc "I have seen [mira.name] working there as well."
        cass.name "Oh? You worked together? [mira.name] never told me."
        cass.name "The Motel? Hmm, the Diner is also round there."
        pc "We are whores."
        show cass worried
        cass.name "What?! Noooo..."
        pc "If she is missing, then it probably has something to do with that."
    elif "met_whore_mira" in mira.list:
        pc "So... There is probably something you should know."
        show cass laugh
        cass.name "Is it about [mira.name]?"
        pc "Yeah... I might know where to look for her."
        show cass neutral
        cass.name "Really?"
        pc "I was around the highway area some time ago and met [mira.name] there."
        cass.name "Err, okay. Not seeing what that has to do with it."
        pc "I have seen [mira.name] working the highway."
        cass.name "Working there? What kind of jobs are over there?"
        cass.name "The Motel? Hmm, the Diner is also round there."
        pc "She is a whore."
        show cass worried
        cass.name "Wha... No... What?! No way!"
        pc "It seems so. So if she is missing it might have something to do with that."
        cass.name "Are you sure about this?"
        pc "I met her there and talked to her about it."
    else:
        pc "So, err... I kinda found out some stuff about [mira.name]."
        show cass laugh
        cass.name "You know where she is?"
        pc "No. But I found out where she worked and that might have something to do with it."
        show cass neutral
        cass.name "She never mentioned anything about working to me. You sure?"
        pc "Yeah..."
        pc "Apparently she worked at the highway."
        cass.name "Hmmm... What is there? The motel, the Diner..."
        cass.name "Truck stop is there as well but not sure what she could do with those."
        pc "She worked the highway. Work worked the highway."
        cass.name "Err... What does that mean?"
        pc "..."
        show cass worried
        cass.name "What?"
        pc "She was a highway whore."
        cass.name "Wha... No... What?! No way!"
        pc "It seems so. So if she is missing it might have something to do with that."
        cass.name "Are you sure about this?"
        pc "It's what I have heard from people who knew she did this."
    cass.name "..."
    cass.name "Thanks..."
    cass.name "Err. I need a bit to think..."
    hide cass with dissolve
    pcm "Yeah, I would think so..."
    $ log.markdone("mira_missing_02")
    $ quest_mira_missing.dict["told_cass_mira_whore_date"] = t.day
    jump travel

label quest_mira_missing_cass_whore_idea:
    show cass at right1 with dissolve
    cass.name "Hey [name]. Can we talk?"
    pc "Sure."
    if "cass_knows" in quest_whore.list:
        cass.name "So, I've been thinking. Would it be possible for me to come with you one day and ask around?"
        pc "Err, you could. But I doubt they will talk to you. I can just ask around if you want."
        cass.name "I know you can. But I want to look for her myself as well."
        pc "Well, up to you. But doubt you will have any luck."
        cass.name "I want to try anyway."
        pc "Okay... When do you want to go?"

    elif quest_whore.sold:
        $ add_to_list(quest_whore.list, "cass_knows")
        cass.name "So, I've been thinking. If what you say is true. Maybe we can go to the highway and ask around."
        pc "Err... I have been to the highway before."
        cass.name "You have?"
        pc "I needed the money."
        cass.name "Oh? Err... that's good I think. You know how things work there."
        pc "I do. And they won't speak to you there but I can ask around."
        cass.name "They won't?"
        pc "No, you are a stranger. They will just tell you to go away."
        cass.name "I want to try anyway. I want to look for her myself as well."
        cass.name "I can't just leave it up to you."
        pc "Right..."
        pc "Okay... When do you want to go?"
    else:

        cass.name "So, I've been thinking. If what you say is true. Maybe we can go to the highway and ask around."
        pc "Seems like a good place to see. Maybe she has friends there."
        cass.name "But I don't want to go alone..."
        pc "Probably for the best. I guess you want me to come?"
        cass.name "Yeah... If you would."
        pc "Sure, when do you want to go?"
    cass.name "Well, today? But if you are busy..."
    cass.name "I guess just come after school when you are ready. We can go from there."
    pc "Okay."
    cass.name "Thanks."
    hide cass with dissolve
    pcm "Finding things out as soon as possible is best. Who knows what might have happened around the highway."
    pcm "Should speak to [cass.name] after classes when I am ready to head to the highway."
    $ log.markdone("mira_missing_03")
    jump travel





label quest_mira_missing_cass_only_whores:
    show cass at right1 with dissolve
    if "investigate_whore_route" in quest_mira_missing.list:
        cass.name "Can we meet later?"
        pc "Huh? Why?"
        cass.name "I have an idea."
        pc "About what? What are we talking about?"
        cass.name "I have been thinking about finding [mira.name], can you meet me later at night?"
        pc "I guess..."
        cass.name "At Revel street. I know a place that can help."
        hide cass with dissolve
        pcm "Okay..."
        $ log.markdone("mira_missing_06")
        jump travel
    pc "So, I asked about..."
    show cass laugh
    cass.name "About [mira.name]?"
    if "cass_knows" in quest_whore.list:
        pc "About how you might get info around the highway without me."
        show cass worried
        cass.name "Oh..."
        cass.name "Pretty sure I know what you are going to say."
        pc "Yeah... nothing good."
        cass.name "It's the only way?"
        pc "Other than leaving it to me, yes."
        cass.name "Right... I've also been thinking about it."
        pc "Yeah?"
        cass.name "Meet me later at night."
        pc "Err..."
        cass.name "At Revel street. I know a place that can help."
        pc "You sure?"
        hide cass with dissolve
        pcm "Okay..."
    elif quest_whore.sold:
        $ add_to_list(quest_whore.list, "cass_knows")
        pc "Err, sort of?"
        show cass neutral
        pc "I have been to the highway alone..."
        pc "And worked there..."
        show cass worried
        cass.name "What?"
        pc "The only way to get in with them is to be one of them."
        cass.name "Ugh! I know!"
        cass.name "*Sigh*"
        cass.name "Meet me later at night."
        pc "Err..."
        cass.name "At Revel street. I know a place that can help."
        pc "You sure?"
        hide cass with dissolve
        pcm "Okay..."
    else:
        pc "About how we might be able to get info from the highway."
        cass.name "Oh?"
        pc "Not good news really..."
        show cass worried
        pc "..."
        pc "The girls at the highway won't speak to anyone who isn't a whore."
        cass.name "Oh? Hmmm..."
        cass.name "So we can dress up and..."
        pc "Won't work. Security and other folk try it. Just dressing the part doesn't get any results."
        cass.name "But we can try..."
        pc "Unless you go the whole..."
        cass.name "Let's try like that."
        pc "But..."
        cass.name "I think I can do it."
        pc "..."
        cass.name "I know. Meet me later at night."
        pc "Err..."
        cass.name "At Revel street. I know a place that can help."
        hide cass with dissolve
        pcm "Pretty sure she understood perfectly what I meant..."
    pcm "Is she really willing to go that far?"
    pcm "Well, [mira.name] was her... Is her best friend. Not easy to come by those."
    pcm "Right, whatever. If I want to get roped into her plan, guess I'll meet her at night round Revel."
    $ log.markdone("mira_missing_06")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
