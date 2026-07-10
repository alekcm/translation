label school_class_normal_felix:
    $ rand_choice = WeightedChoice([
    ("school_class_normal_felix_1", 1),
    ("school_class_normal_felix_2", 1),
    ("school_class_normal_felix_3", 1),
    ("school_class_normal_felix_4", 1),

    ])
    jump expression rand_choice

label school_class_normal_felix_1:
    show felix at right1 with dissolve
    pc "Morning. Not used to seeing you this early."
    felix.name "Yeah..."
    pc "Problem?"
    felix.name "Ah no. My flatmate has \"company\" round so I am giving him space. No where else to be but here."
    pc "Ah."
    jump school_class_normal_end

label school_class_normal_felix_2:
    show felix at right1 with dissolve
    pc "Morning. What you doing here so early?"
    felix.name "Nothing really. I guess I should at least attend some classes."
    pc "Pobably."
    jump school_class_normal_end

label school_class_normal_felix_3:
    show felix at right1 with dissolve
    pc "Morning."
    felix.name "Morning [name]."
    pc "You sound energetic."
    felix.name "Not used to being up so early. Wanted to take some photos while the streets were empty and that means being up at the crack of dawn."
    pc "Ah."
    jump school_class_normal_end

label school_class_normal_felix_4:
    show felix at right1 with dissolve
    pc "Morning."
    felix.name "Hey. How's things."
    pc "Same old. What you doing here so early?"
    felix.name "Nothing really. Just happened to be awake so thought I would come here."
    pc "Ah."
    jump school_class_normal_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
