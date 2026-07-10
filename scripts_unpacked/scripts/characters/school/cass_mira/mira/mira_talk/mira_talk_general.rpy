label mira_talk_general_tombola:


    jump expression WeightedChoice([

    
    ("mira_talk_general_1", 100),
    ("mira_talk_general_2", 100),

    
    ("mira_talk_school_1", If(dis(dis_school) and not mira.active and not quest_mira_missing.active, 100, 0)),
    ("mira_talk_school_2", If(dis(dis_school), 100, 0)),
    ("mira_talk_school_3", If(dis(dis_school), 100, 0)),  
    ("mira_talk_school_4", If(dis(dis_school), 100, 0)),

    
    ("mira_talk_general_whore_1", If(not cass_here() and "pc_knows_whore" in mira.list and not player.has_perk(perk_whore), 100, 0)),
    ("mira_talk_general_whore_2", If(not cass_here() and "pc_knows_whore" in mira.list and not player.has_perk(perk_whore), 100, 0)),
    ("mira_talk_general_whore_3", If(not cass_here() and "pc_knows_whore" in mira.list and not player.has_perk(perk_whore), 100, 0)),
    ("mira_talk_general_whore_4", If(not cass_here() and "pc_knows_whore" in mira.list and not player.has_perk(perk_whore), 100, 0)),
    ("mira_talk_general_whore_5", If(not cass_here() and "pc_knows_whore" in mira.list and not player.has_perk(perk_whore), 100, 0)),

    ("mira_talk_general_whore_highway_1", If(dis(dis_truckstop), 100, 0)),
    ("mira_talk_general_whore_highway_2", If(dis(dis_truckstop), 100, 0)),
    ("mira_talk_general_whore_highway_3", If(dis(dis_truckstop), 100, 0)),
    ("mira_talk_general_whore_highway_4", If(dis(dis_truckstop), 100, 0)),

    ])

label mira_talk_general_1:
    mira.name "Hey [name]."
    pc "How you been keeping."
    mira.name "Same as usual."
    jump mira_talk_end

label mira_talk_general_2:
    mira.name "Hey [name]."
    pc "How you been keeping."
    mira.name "Same as usual."
    jump mira_talk_end





label mira_talk_school_1:
    pc "Don't see you going to gym classes too much."
    mira.name "Yeah, I can't be bothered to run around much. Still have the whole day to go."
    mira.name "Also don't trust the showers."
    jump mira_talk_end

label mira_talk_school_2:
    mira.name "I swear each so called teacher tells us totally different things to each other."
    pc "Wait until they start talking about sex, then it's all the same."
    mira.name "Take it in the bum..."
    jump mira_talk_end

label mira_talk_school_3:
    mira.name "Not sure how they manage to keep the water hot here."
    pc "Well, hot is generous."
    mira.name "Well, lukewarm is better than most other places."
    pc "Yeah."
    jump mira_talk_end

label mira_talk_school_4:
    mira.name "You ever seen anyone use the lockers here?"
    pc "Some. Risking all their stuff."
    mira.name "Doubt they keep anything valuable in there."
    pc "Everything's valuable these days."
    jump mira_talk_end





label mira_talk_general_whore_1:
    pc "Keeping safe at the highway?"
    mira.name "Safe as you can be there."
    pc "Scary place. Lot of weirdos."
    mira.name "Yeah..."
    jump mira_talk_end

label mira_talk_general_whore_2:
    pc "Not considered other jobs?"
    mira.name "Yeah, but they all end the same way so what's the point?"
    pc "Don't have to hang around the dangerous highway?"
    mira.name "It's about the only bonus. Less money though."
    jump mira_talk_end

label mira_talk_general_whore_3:
    mira.name "You ever considered earning at the highway?"
    pc "Not really. To be honest it's kind of new to me."
    mira.name "Whoring?"
    pc "Earning money using your body. Like all the jobs round here pretty much need it."
    jump mira_talk_end

label mira_talk_general_whore_4:
    mira.name "Well if you want, I can take you round to whore."
    pc "Going to take a cut of my money?"
    mira.name "Other girls would kill me if I did."
    pc "Really?"
    mira.name "Yeah, that sort of thing would literally get you put in the ground."
    jump mira_talk_end

label mira_talk_general_whore_5:
    mira.name "Keep this stuff quiet to [cass.nname]."
    pc "The highway stuff? Yeah. Not my business."
    pc "You sure she isn't round here somewhere already? Seems a lot of people make money this way."
    mira.name "I would have seen her if she was."
    jump mira_talk_end





label mira_talk_general_whore_highway_1:
    pc "Customers treating you well?"
    mira.name "As well as they ever do."
    pc "Well, keep safe."
    jump mira_talk_end

label mira_talk_general_whore_highway_2:
    pc "Not sure if the rain is more dangerous or the men while standing out here."
    mira.name "Rain doesn't try to lure you into an alleyway and rape you."
    pc "It might give you a cold though."
    mira.name "The horror!"
    jump mira_talk_end

label mira_talk_general_whore_highway_3:
    pc "I don't see you hanging much with the other whores."
    mira.name "No, I try to keep things quiet."
    mira.name "Plus most of them live in some run down homeless shelter and stick together."
    pc "Ah, you are not part of their group?"
    mira.name "Not really."
    jump mira_talk_end

label mira_talk_general_whore_highway_4:
    pc "Why don't you work the motel? I hear they do weird things there."
    mira.name "Because they do weird things there."
    pc "Okay..."
    mira.name "People pay for really extreme things in the rooms. Not my thing."
    pc "Right..."
    jump mira_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
