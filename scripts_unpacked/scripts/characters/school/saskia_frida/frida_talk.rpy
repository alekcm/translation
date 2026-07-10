label frida_talk_subject:
    show frida at right1 with dissolve
    jump expression WeightedChoice([

    ("frida_talk_general_1", 100),

    ])

label frida_talk_general_1:
    "General talk with [frida.name] alone."
    jump saskia_frida_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
