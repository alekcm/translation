label school_class_lunch_mira:
    $ rand_choice = WeightedChoice([
    ("school_class_lunch_mira_1", If(not cass.isactive,1,0)),
    ("school_class_lunch_mira_2", If(not cass.isactive,1,0)),
    ("school_class_lunch_mira_3", If(not cass.isactive,1,0)),
    ("school_class_lunch_mira_4", If(cass.isactive and school_bully_quest_bully_cass_target,1,0)),
    ("school_class_lunch_mira_5", If(not cass.isactive,1,0)),
    ("school_class_lunch_mira_6", If(not cass.isactive,1,0)),
    ("school_class_lunch_mira_7", If(cass.isactive,1,0)),
    ])
    jump expression rand_choice

label school_class_lunch_mira_1:
    show mira at right1
    pc "You're alone today?"
    mira.name "Looks like it. Not seen [cass.nname] today."
    pc "Hmmm."
    jump school_class_lunch_end

label school_class_lunch_mira_2:
    show mira at right1
    pc "You ok?"
    mira.name "Yeah, just a bit worried about [cass.nname]."
    mira.name "She isn't here as much as she used to be since... Well, I think you have seen it."
    pc "Oh? Them?"
    mira.name "Mmmm."
    jump school_class_lunch_end

label school_class_lunch_mira_3:
    show mira at right1
    pc "No [cass.nname] today?"
    mira.name "No. Wel yes, but she decided to leave early."
    pc "Ah, she sick or something?"
    mira.name "No, I think she just doesn't want to be here any more."
    pc "Really? Why?"
    mira.name "You not noticed what's been happening?"
    pc "..."
    jump school_class_lunch_end

label school_class_lunch_mira_4:
    show mira at right1
    show cass at right2:
        xzoom -1
    pc "Hey."
    hide cass with dissolve
    pc "Err, bye?"
    pc "..."
    pc "She going home for the day?"
    mira.name "Yeah."
    pc "To avoid them?"
    mira.name "Yeah..."
    $ cass.active = False
    jump school_class_lunch_end

label school_class_lunch_mira_5:
    show mira at right1
    pc "Hmm, seeing a lot less of [cass.nname] these days."
    mira.name "Yeah..."
    pc "..."
    jump school_class_lunch_end

label school_class_lunch_mira_6:
    show mira at right1
    pcm "Hmm, still no [cass.nname]..."
    pcm "Maybe I shouldn't have got the boys to scare those arseholes away. Now it's her that is having to deal with them."
    mira.name "Yes? No? Hello?"
    pc "Huh? Ah sorry, my mind was wandering."
    jump school_class_lunch_end

label school_class_lunch_mira_7:
    show mira at right2
    show cass at right1
    mira.name "Looks tasty as always."
    pc "Yeah tell me about it."
    pcm "[cass.nname] looks all sullen..."
    pcm "Those idiots been messing with her again today?"
    mira.name "...even if I tried."
    pc "Mmmm."
    jump school_class_lunch_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
