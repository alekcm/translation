label cass_mira_talk_picker:
    if cass_here() and mira_here():
        jump expression WeightedChoice([
        ("cass_mira_talk_subject", 100),
        ("cass_talk_subject", 50),
        ("mira_talk_subject", 50),
        ])
    elif cass_here():
        jump cass_talk_subject
    else:
        jump mira_talk_subject

label cass_mira_talk_subject:

    if not "whore_post_rescue_talk" in mira.dict:
        $ mira.dict["whore_post_rescue_talk"] = 0
    if not "whore_post_kidnap_talk" in mira.dict:
        $ mira.dict["whore_post_kidnap_talk"] = 0
    if not "whore_post_havenslave_talk" in mira.dict:
        $ mira.dict["whore_post_havenslave_talk"] = 0
    if not "photos_talk" in mira.dict:
        $ mira.dict["photos_talk"] = 0

    show cass at right1
    show mira at right2
    with dissolve
    jump expression WeightedChoice([

    ("cass_mira_talk_general_tombola", 100),

    
    ("cass_mira_talk_photos_chain_" + str(mira.dict["photos_talk"]), If(renpy.has_label("cass_mira_talk_photos_chain_" + str(mira.dict["photos_talk"])) and log.completed("Starting the magazine"), 100, 0)),
   
    
    ("cass_mira_talk_postwhore_" + str(mira.dict["whore_post_rescue_talk"]), If(renpy.has_label("cass_mira_talk_postwhore_" + str(mira.dict["whore_post_rescue_talk"])) and "rescued" in mira.list and cass_here() and dis(dis_truckstop), 100, 0)),
    
    
    ("cass_mira_talk_kidnap_explain_" + str(mira.dict["whore_post_kidnap_talk"]), If(renpy.has_label("cass_mira_talk_kidnap_explain_" + str(mira.dict["whore_post_kidnap_talk"])) and "rescued" in mira.list and cass_here() and dis(dis_truckstop), 500, 0)),
    ("cass_mira_talk_havenslave_explain_" + str(mira.dict["whore_post_havenslave_talk"]), If(renpy.has_label("cass_mira_talk_havenslave_explain_" + str(mira.dict["whore_post_havenslave_talk"])) and "rescued" in mira.list and cass_here() and dis(dis_truckstop) and not renpy.has_label("cass_mira_talk_postwhore_" + str(mira.dict["whore_post_rescue_talk"])) and "haven_slave" in mira.list, 500, 0)),

    ])

label cass_mira_talk_general_tombola:
    jump expression WeightedChoice([
    
    
    ("cass_mira_talk_general_1", 100),
    ("cass_mira_talk_general_2", 100),
    ("cass_mira_talk_general_3", If(not cass.iswhore, 100, 0)),
    ("cass_mira_talk_general_4", 100),

    
    ("cass_mira_talk_photos_1", If(not renpy.has_label("cass_mira_talk_photos_chain_" + str(mira.dict["photos_talk"])), 100, 0)),
    ("cass_mira_talk_photos_2", If(not renpy.has_label("cass_mira_talk_photos_chain_" + str(mira.dict["photos_talk"])), 100, 0)),
    ("cass_mira_talk_photos_3", If(not renpy.has_label("cass_mira_talk_photos_chain_" + str(mira.dict["photos_talk"])), 100, 0)),
    ("cass_mira_talk_photos_4", If(not renpy.has_label("cass_mira_talk_photos_chain_" + str(mira.dict["photos_talk"])), 100, 0)),

    
    ("cass_mira_talk_school_1", If(dis(dis_school), 100, 0)),
    ("cass_mira_talk_school_2", If(dis(dis_school), 100, 0)),
    ("cass_mira_talk_school_3", If(dis(dis_school), 100, 0)),
    ("cass_mira_talk_school_4", If(dis(dis_school), 100, 0)),

    ])





label cass_mira_talk_general_1:
    cass.name "How's your dance classes going [name]?"
    if player.isfat == True:
        pc "Hard work. I am far too unfit to really do anything."
    elif school_dance_quest_on_team == True:
        pc "It's great actually. Training with the team is much more fun than the normal class."
    else:
        pc "Going ok, just trying to learn the routines and not fall on my arse."
    cass.name "How is the club leader? She seems a bit of a bitch."
    pc "Hmm, she's just harsh. She means well."
    jump cass_mira_talk_end

label cass_mira_talk_general_2:
    cass.name "Mira~~"
    mira.name "Huh?"
    cass.name "I saw you earlier."
    mira.name "Err. Okay... Saw me doing what?"
    cass.name "Don't be coy, the boy on the football team."
    mira.name "Ah."
    cass.name "Well...?"
    mira.name "Well what?"
    cass.name "Okay be that way. Keep your secrets."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        $ player.eye = 4
        $ player.mouth = 6
        pc "FRODO!!!!"
        $ player.face_normal()
        cass.name "Whaaaa...?"
        pc "Nothing."
    jump cass_mira_talk_end

label cass_mira_talk_general_3:
    show mira at right2
    show cass at right1
    with dissolve
    cass.name "You done any more handing out flyers in the market [mira.name]?"
    mira.name "Don't want to, but have no choice."
    cass.name "Why not? At least they don't screw you on the pay."
    mira.name "Because I can't count how many people think it's okay to put their hands on me."
    cass.name "Ah yeah. Part of the job unfortunately."
    mira.name "How can you accept such a thing?"
    cass.name "I don't accept it. But if I want to get paid I have no choice."
    mira.name "Wouldn't it bring more money if you just walked the highway with that attitude?"
    cass.name "Well I don't want to be hit over the head and bundled into the back of a car. That won't happen in the market."
    jump cass_mira_talk_end

label cass_mira_talk_general_4:
    cass.name "I don't think it's a good idea."
    mira.name "Sure it is. Relax in the sun. They have volleyball there as well."
    if loc_beach_hangout.visited:
        pc "Water is also nice."
        mira.name "Yeah."
    jump cass_mira_talk_end





label cass_mira_talk_school_1:
    mira.name "Can get in the library upstairs."
    cass.name "Yeah, but don't those strange guys hang out in there?"
    mira.name "Them? Yeah, but they are harmless."
    jump cass_mira_talk_end

label cass_mira_talk_school_2:
    mira.name "Buy some bits off the girls upstairs."
    cass.name "I spoke to them. They are... Strange..."
    if saskia.has_met:
        pc "Yeah. I think they have been drinking too many chemicals or something."
    else:
        pc "Who's that?"
        mira.name "The girls that occupied the sewing room upstairs. They fix clothes and sell some stuff."
    jump cass_mira_talk_end

label cass_mira_talk_school_3:
    mira.name "I hear there are locked off parts to this place."
    cass.name "The school?"
    mira.name "Yeah, some parts used to be open but got locked off for some reason."
    pc "You are talking as if we are in a horror movie. Some monster is going to come out the abandoned parts."
    jump cass_mira_talk_end

label cass_mira_talk_school_4:
    mira.name "You ever check out the forest past the field?"
    cass.name "No. Why would I wander through a forest?"
    mira.name "Just wondering what might be in there."
    cass.name "Trees."
    if loc_walk_park_forest.visited:
        pc "I've been through there. You can get to the park that way."
        mira.name "Oh?"
    elif not numgen(0,5):
        pc "Probably rapists as well."
    jump cass_mira_talk_end





label cass_mira_talk_photos_1:
    cass.name "But don't you attract weirdos doing the photos?"
    pc "Err... We spoke about this before. Attract the weirdos no matter what I do."
    cass.name "Yeah..."
    jump cass_mira_talk_end

label cass_mira_talk_photos_2:
    cass.name "What about [felix.name]?"
    pc "What about him?"
    cass.name "He a pervert?"
    pc "Probably. But we do a job."
    cass.name "Hmmm..."
    jump cass_mira_talk_end

label cass_mira_talk_photos_3:
    mira.name "You don't mind the photos all being out there?"
    pc "Should I? All jobs around here that I can do would have people looking at my arse."
    pc "At least I don't need to whore for this job or something."
    mira.name "Yeah I suppose."
    jump cass_mira_talk_end

label cass_mira_talk_photos_4:
    mira.name "[name] superstar!"
    pc "In the flesh."
    mira.name "Can I have an autograph?"
    pc "Sure. Don't go selling it on the black market though."
    jump cass_mira_talk_end

label cass_mira_talk_test:

    mira.name "You are talking to both of us."
    cass.name "Yup, we should both be here"
    jump cass_mira_talk_end

label cass_mira_talk_end:
    $ relax(20, [cass, mira])
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide cass
    hide mira
    with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
