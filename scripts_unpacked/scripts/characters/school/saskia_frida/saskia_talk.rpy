label saskia_talk_subject:
    show saskia at right1 with dissolve
    jump expression WeightedChoice([

    ("saskia_talk_general_1", 100),

    ])

label saskia_talk_general_1:
    "General talk with [saskia.name] alone."
    jump saskia_frida_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
