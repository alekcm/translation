label rachel_talk_exhib_strip:
    rachel.name "Why are you dressed?"
    pc "Err..."
    $ pc_striptease(temp=True)
    pc "Better?"
    rachel.name "Yup!"
    hide rachel with dissolve
    jump travel

label rachel_talk_exhib_strip_enter_school:
    $ walk(loc_school_hallway)
    if not c.nude:
        if not "should_strip_warning" in loc_school_hallway.list:
            $ add_to_list(loc_school_hallway.list, "should_strip_warning")
            pcm "I should undress while in here or [rachel.name] will be upset."
        $ pc_striptease(temp=True)
        jump travel
    else:
        jump travel_arrival

label rachel_talk_exhib_subject:
    jump expression WeightedChoice([

    ("rachel_talk_exhib_talk_1", 100),
    ("rachel_talk_exhib_talk_2", 100),
    ("rachel_talk_exhib_talk_3", 100),

    ("rachel_talk_exhib_chain_start_" + str(rachel.dict["rachel_talk_exhib_chain"]), If(renpy.has_label("rachel_talk_exhib_chain_start_" + str(rachel.dict["rachel_talk_exhib_chain"])) and loc(loc_school_gym) and rachel_exhib_stripping_show(), 1000, 0)),
    ("rachel_talk_exhib_talk_perk_offer", If(loc(loc_school_gym) and rachel_exhib_stripping_show() and not "asked_exhib_perk" in quest_exhib.list and log.completed("A place to be alone"), 1000, 0)), 

    ])

label rachel_talk_exhib_chain_start_0:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    pc "So, what is this all about anyway?"
    rachel.name "All what about?"
    pc "Being naked..."
    rachel.name "Trying out some fun things."
    pc "That doesn't explain much."
    rachel.name "Yes it does!"
    jump rachel_talk_end

label rachel_talk_exhib_chain_start_1:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    pc "Okay, so why do you want to be naked?"
    rachel.name "I told you. Fun!"
    pc "Err, yeah. But what made you think of doing this?"
    pc "You asked me to sneak you in here and everything, so sounds like you planned this."
    rachel.name "Yeah, I saw some girl running through the park naked. I looked fun."
    jump rachel_talk_end

label rachel_talk_exhib_chain_start_2:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    pc "Through the park naked?"
    rachel.name "Yeah."
    pc "What? She came up to you and showed off or what?"
    rachel.name "Na. She came out the bushes all naked and ran off somewhere."
    pc "Err, out the bushes?"
    rachel.name "Yup."
    jump rachel_talk_end

label rachel_talk_exhib_chain_start_3:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    rachel.name "I think she was teasing some boys or something."
    pc "Why?"
    rachel.name "When she ran out the bushes, a bunch of naked guys chased after her."
    pc "What?"
    rachel.name "Yeah, looked like they were playing a game or something."
    pc "You sure it was a game?"
    jump rachel_talk_end

label rachel_talk_exhib_chain_start_4:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    rachel.name "Of course it was a game. Why else would you run naked through the park?"
    pc "Err... To get away from the guys?"
    rachel.name "Yeah. And they chased her. She was making loads of noise so she was having loads of fun."
    pc "..."
    pc "Did they catch her?"
    rachel.name "Yeah, they grabbed her and picked her up into the bushes again."
    pc "..."
    jump rachel_talk_end

label rachel_talk_exhib_chain_start_5:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    rachel.name "Thought it might be fun to jump out of some guys in the park like her. But I was too scared."
    pc "I'm not sure you want to do that."
    rachel.name "I do! I just thought I might practice a bit first."
    pc "Okay... If you say so..."
    jump rachel_talk_end

label rachel_talk_exhib_chain_start_6:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    rachel.name "How about you help me practice?"
    pc "Err... How?"
    rachel.name "Let's play some games an jump out on people."
    pc "What? Are you serious?"
    rachel.name "Yeah, it'll be fun!"
    jump rachel_talk_end

label rachel_talk_exhib_chain_start_7:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    rachel.name "C'mon. Let's do some funny things."
    pc "Naked funny things?"
    rachel.name "Of course!"
    pc "Ugh..."
    jump rachel_talk_end

label rachel_talk_exhib_chain_start_8:
    $ rachel.dict["rachel_talk_exhib_chain"] += 1
    pc "Okay. What crazy things you got in mind?"
    rachel.name "Not sure. I thought you might have something."
    pc "Hmmm..."
    $ log.markdone("quest_exhib_03")
    $ add_to_list(rachel.list, "can_play_games")
    jump rachel_talk_end

label rachel_talk_exhib_talk_1:
    pc "You feeling okay being naked?"
    rachel.name "Yeah, it's fun. Would be nice if I could go everywhere like this."
    pc "You probably could."
    rachel.name "Sure. And I'll end up locked in some perverts basement until I get fat with a baby."
    pc "Yup."
    jump rachel_talk_end

label rachel_talk_exhib_talk_2:
    pc "Going around the highway naked is probably okay."
    rachel.name "Why there?"
    pc "Whores and other girls having fun. Naked girls are probably a normal thing."
    rachel.name "Might have to try it."
    jump rachel_talk_end

label rachel_talk_exhib_talk_3:
    rachel.name "Running around the park is also fun."
    pc "Yeah?"
    rachel.name "Soft floor and no poop any more in the grass."
    jump rachel_talk_end

label rachel_talk_exhib_talk_perk_offer:
    $ add_to_list(quest_exhib.list, "asked_exhib_perk")
    rachel.name "You having fun running around all naked?"
    pc "Yeah, it's kind of exciting."
    rachel.name "You should go everywhere naked."
    pc "Sure, I bet the men will have a lot of fun."
    rachel.name "Yeah. I try to go naked, but people end up jumping on me."
    pc "Thought you would like that."
    rachel.name "When they are gentle it's fun. Too many beat me up though."
    pc "Ah."
    rachel.name "You should try it."
    menu:
        "Yeah, it would be fun even with the risk"(badge="perk_exhibitionist"):
            rachel.name "I knew you would enjoy it."
            $ player.add_perk(perk_exhibitionist, notif=True)
        "No, I think I would rather be a bit safer":
            rachel.name "That's no fun!"
    jump rachel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
