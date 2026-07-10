label cass_talk_whore_tombola:
    jump expression WeightedChoice([

    ("cass_talk_whore_1", If(cass.iswhore and dis(dis_truckstop), 100, 0)),
    ("cass_talk_whore_2", If(cass.iswhore and dis(dis_truckstop) and quest_whore.sold >= 10, 100, 0)),
    ("cass_talk_whore_3", If(cass.iswhore and dis(dis_truckstop), 100, 0)),
    ("cass_talk_whore_4", If(cass.iswhore and dis(dis_truckstop) and quest_whore.sold >= 10, 100, 0)),
    ("cass_talk_whore_5", If(cass.iswhore and dis(dis_truckstop), 100, 0)),
    ("cass_talk_whore_6", If(cass.iswhore and dis(dis_truckstop) and t.month == "Winter", 100, 0)),
    ("cass_talk_whore_7", If(cass.iswhore and dis(dis_truckstop), 100, 0)),
    ("cass_talk_whore_8", If(cass.iswhore and dis(dis_truckstop), 100, 0)),

    ])

label cass_talk_whore_1:
    pc "Keeping safe I hope."
    cass.name "Safe as you can be round here."
    pc "I'm here if you need someone to watch your back."
    cass.name "Yeah, same here."
    jump cass_talk_end

label cass_talk_whore_2:
    cass.name "You get asked for weird stuff?"
    pc "I'm starting to think the weird stuff isn't as weird as I thought it should be."
    cass.name "Yeah. It's like they want it every way except normal."
    pc "Haha yeah."
    jump cass_talk_end

label cass_talk_whore_3:
    cass.name "Plus side of all this I guess is the money."
    pc "Well, yeah... Not sure."
    cass.name "No?"
    pc "Well, I think I would rather be sitting at a desk answering the phone or something."
    cass.name "Ah. Well yeah. No phones any more though. And if these guy's got hold of one they would probably ask me to put it up my arse."
    jump cass_talk_end

label cass_talk_whore_4:
    cass.name "People really expect to get freebies?"
    pc "Yeah. Had one guy follow me around just wanking like I am TV porn."
    cass.name "Haha yeah I have the same."
    jump cass_talk_end

label cass_talk_whore_5:
    cass.name "Kinda getting used to walking around near naked these days."
    pc "You still wearing underwear?"
    cass.name "Not really. It was getting expensive to replace."
    jump cass_talk_end

label cass_talk_whore_6:
    cass.name "Got to stand out freezing to death in this cold."
    pc "If you do die, I'll sell your corpse."
    cass.name "Thanks..."
    jump cass_talk_end

label cass_talk_whore_7:
    cass.name "You been into the slums? Someone there sells stuff that comes in handy."
    if havenvik.has_met:
        pc "Yeah I had a look. Expensive though."
        cass.name "Yeah... Might not be worth it in the end."
    else:
        pc "Not had a look. What do they sell?"
        cass.name "Pills and stuff so you don't end up pregnant."
        if cass.showing:
            pc "Errr..."
            cass.name "It's expensive..."
    jump cass_talk_end

label cass_talk_whore_8:
    cass.name "Sometimes it's easier to just get a blue room and crash there for the night."
    pc "Yeah?"
    cass.name "Room isn't that bad and it has a shower."
    jump cass_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
