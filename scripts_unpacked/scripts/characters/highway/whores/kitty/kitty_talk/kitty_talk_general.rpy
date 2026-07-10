label kitty_talk_subject:
    jump expression WeightedChoice([

    ("kitty_talk_general_1", 100),
    ("kitty_talk_general_2", 100),
    ])

label kitty_talk_general_1:
    kitty.name "Don't do girls."
    pc "No? Money is money."
    kitty.name "Shoo!"
    jump kitty_talk_end

label kitty_talk_general_2:
    kitty.name "Why you not off selling yourself instead of speaking to me?"
    pc "More fun to annoy you."
    kitty.name "Ugh..."
    jump kitty_talk_end

label kitty_talk_end:
    $ relax(20, kitty)
    $ dialouge = renpy.random.choice([
    "We chat for a bit, and while she is a bit terse, we means well.",
    "We chat for a bit, even if it's just her pretending to be all grumpy.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide kitty with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
