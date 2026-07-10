label cass_talk_broken_tombola:
    show cass at right1 with dissolve
    call expression WeightedChoice([

    ("cass_talk_broken_1", 100),
    ("cass_talk_broken_2", 100),
    ("cass_talk_broken_3", 100),
    ("cass_talk_broken_4", 100),
    ("cass_talk_broken_5", 100),
    ("cass_talk_broken_6", 100),
    ("cass_talk_broken_7", 100),
    ("cass_talk_broken_8", 100),

    ]) from _call_expression_21

    hide cass with dissolve
    jump travel

label cass_talk_broken_1:
    pc "Hi. How are you?"
    cass.name "Fine."
    return

label cass_talk_broken_2:
    pc "Hi [cass.nname]."
    cass.name "..."
    return

label cass_talk_broken_3:
    pc "[cass.name]... [mira.name] is gone..."
    cass.name "No she isn't!"
    return

label cass_talk_broken_4:
    pc "[cass.name]. Let's talk."
    cass.name "I need to find [mira.name]."
    return

label cass_talk_broken_5:
    pc "[cass.name]. I'm sorry."
    cass.name "..."
    return

label cass_talk_broken_6:
    pc "[cass.name]. Can we talk?"
    cass.name "No time. I need to find [mira.name]."
    return

label cass_talk_broken_7:
    pc "..."
    cass.name "... ..."
    return

label cass_talk_broken_8:
    pc "[cass.name]..."
    cass.name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
