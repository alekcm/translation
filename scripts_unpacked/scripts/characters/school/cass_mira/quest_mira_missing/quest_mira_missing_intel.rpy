label quest_mira_missing_intel_cass:
    show cass at right1 with dissolve
    cass.name "I managed to get some info on [mira.name]."
    pc "Oh? What did you find out?"
    "We spend some time comparing notes and going over what each of us have learned."
    $ relax(10)
    $ inv.take(item_mira_intel)
    $ cass.inv.drop(item_mira_intel)
    $ log.find("mira_missing_08")
    if log.interactive("mira_missing_09"):
        jump quest_mira_missing_intel_complete
    pc "This is great, but still need to find out more."
    cass.name "Yeah..."
    hide cass with dissolve
    jump travel

label quest_mira_missing_intel_whore_customer_picker:
    "I strike up a conversation with the guy as we are walking to see if I can get any info about [mira.name]..."
    call expression WeightedChoice([
    
    ("quest_mira_missing_intel_whore_customer_fail_1", 1),
    ("quest_mira_missing_intel_whore_customer_intel_1", If(quest_mira_intel_weight(), 1000, 0)),

    ]) from _call_expression_17
    return

label quest_mira_missing_intel_whore_customer_fail_1:
    "But it doesn't seem like he knows anything."
    return

label quest_mira_missing_intel_whore_customer_intel_1:
    man "Oh? You mean her?"
    "He spends a bit of time talking to me as we walk."
    pcm "This is helpful."
    $ inv.take(item_mira_intel)
    $ log.find("mira_missing_08")
    return

label quest_mira_missing_intel_whore_whores_picker:
    "Instead of looking for customers, I have a chat with the girls around me about [mira.name]..."
    call expression WeightedChoice([
    
    ("quest_mira_missing_intel_whore_whores_fail_1", 1),
    ("quest_mira_missing_intel_whore_whores_intel_1", If(quest_mira_intel_weight(), 1000, 0)),

    ]) from _call_expression_20
    return

label quest_mira_missing_intel_whore_whores_fail_1:
    "But it doesn't seem like anyone has anything to say."
    return

label quest_mira_missing_intel_whore_whores_intel_1:
    $ quest_mira_whore_whore_name_picker()
    $ renpy.scene()
    if tempname == kitty:
        show kitty at right1
        with dissolve
        kitty.name "[mira.wname]? Yeah."
        "We chat a bit about [mira.name], or [mira.wname] as the girls know her by."
        pc "Oh? Like that?"
    elif tempname == pursy:
        show pursy at right1
        with dissolve
        pursy.name "[mira.wname]? You were her friend?"
        "We chat a bit about [mira.name], or [mira.wname] as the girls know her by."
        pc "Oh? Like that?"
    elif tempname == rose:
        show rose at right1
        with dissolve
        rose.name "Ah, you are friends with [mira.wname]?"
        "We chat a bit about [mira.name], or [mira.wname] as the girls know her by."
    elif tempname == charity:
        show charity at right1
        with dissolve
        charity.name "[mira.wname]? Shame she went missing. You were friends?"
        "We chat a bit about [mira.name], or [mira.wname] as the girls know her by."
    else:
        with dissolve
        tempname.name "Oh? [mira.wname]?"
        "We chat a bit about [mira.name], or [mira.wname] as the girls know her by."
    pc "Oh? Like that?"
    "She chats a bit about her and I try to remember every detail."
    pcm "This is helpful."
    $ inv.take(item_mira_intel)
    $ log.find("mira_missing_08")
    "Conversation eventually goes off to something else and I carry on looking around."
    $ renpy.scene()
    with dissolve
    $ tempname = punter
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
