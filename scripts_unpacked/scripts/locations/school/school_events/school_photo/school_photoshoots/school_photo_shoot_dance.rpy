label school_photo_quest_photoshoot_dance:
    $ school_photo_shoots_done += 1
    $ add_to_list(school_photo_quest.list,["dance", "dance_sexy","underboob","pants"])
    "This is the revealing version of the dance outfit."
    $ walk(loc_school_locker_girls)
    pause 0.5
    $ photo_clothes_dance_revealing()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    pause 0.5
    $ walk(loc_school_gym)
    show ps_dance with dissolve
    felix.name "Already doesn't leave much to the imagination..."
    $ c.top = 0
    show ps_dance pout worried with dissolve
    pc "But we can show off more."
    show ps_dance armup tounge cheeky with dissolve
    pc "Ner, can't see anything now!"
    $ c.bottom = 0
    show ps_dance pout worried with dissolve
    pc "Fuck!"
    $ c.pants = 0
    pc "Seriously? Everything?"
    show ps_dance armdown vhappy straight with dissolve
    pc "Whatever..."
    show ps_dance ag worried with dissolve
    pc "Ahhhhh!"
    hide ps_dance with dissolve
    $ pc_dress()
    $ walk(loc_school_darkroom)
    jump school_photo_quest_photoshoot_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
