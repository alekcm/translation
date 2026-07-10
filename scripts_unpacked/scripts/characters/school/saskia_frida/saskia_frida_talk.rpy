label saskia_frida_talk_subject:
    show saskia at right1
    show frida at right2
    with dissolve
    jump expression WeightedChoice([
    ("saskia_frida_talk_general_1", 100),
    ("saskia_frida_talk_general_2", If(player.slutty, 100, 0)),
    ])

label saskia_frida_talk_general_1:
    "General talk with [saskia.name] and [frida.name] together."
    jump saskia_frida_talk_end

label saskia_frida_talk_general_2:
    saskia.name "All dressed for finding a new boyfriend?"
    frida.name "Looks like it. So where you off to [name]?"
    pc "Huh? Iam just here. No boyfriends around this place."
    saskia.name "True, you need to look better."
    jump saskia_frida_talk_end

label saskia_frida_talk_end:
    if all([saskia_here(), frida_here()]):
        $ relax(20, [saskia, frida])
        $ dialouge = renpy.random.choice([
        "I hang out chatting with the girls about random stuff.",
        "I hang out for a while chatting and joking around about random topics.",
        "We hang out chatting and laughing about whatever comes up.",
        "We chat and have a bit of a laugh about random stuff."
        ])
    elif saskia_here():
        $ relax(20, saskia)
        $ dialouge = renpy.random.choice([
        "Me and " + saskia.setname + " hang out chatting away for a while.",
        "I hang out for a while chatting and joking around about random topics.",
        "We hang out chatting and laughing about whatever comes up.",
        "We chat and have a bit of a laugh about random stuff."
        ])
    else:
        $ relax(20, frida)
        $ dialouge = renpy.random.choice([
        "Me and " + frida.setname + " hang out chatting away for a while.",
        "I hang out for a while chatting and joking around about random topics.",
        "We hang out chatting and laughing about whatever comes up.",
        "We chat and have a bit of a laugh about random stuff."
        ])
    "[dialouge]"
    hide saskia
    hide frida
    with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
