label school_photo_quest_photoshoot_witch:
    $ school_photo_shoots_done += 1
    $ add_to_list(school_photo_quest.list,["witch", "pants"])
    "This is a Halloween witch outfit."
    $ walk(loc_school_locker_girls)
    pause 0.5
    $ photo_clothes_witch()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    $ player.set_hair()
    pause 0.5
    $ walk(loc_school_gym)
    show ps_witch with dissolve
    felix.name "Base photo."
    $ c.outfit = 0
    show ps_witch with dissolve
    pc "Ah! Better cover up."
    show ps_witch cover with dissolve
    pc "Better"
    $ c.pants = 0
    pc "Uh oh!"
    pc "Well, whatever, no point in hiding now."
    show ps_witch open with dissolve
    pc "What are you looking at?"
    hide ps_witch with dissolve
    $ pc_dress()
    $ walk(loc_school_darkroom)
    jump school_photo_quest_photoshoot_picker

label school_photo_quest_photoshoot_catgirl:
    $ school_photo_shoots_done += 1
    $ add_to_list(school_photo_quest.list,"catgirl")
    "This is a Halloween catgirl outfit."
    $ walk(loc_school_locker_girls)
    pause 0.5
    $ photo_clothes_catgirl()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    pause 0.5
    $ walk(loc_school_gym)
    show ps_catgirl with dissolve
    felix.name "Base photo."
    $ c.top = 0
    show ps_catgirl oh worried with dissolve
    pc "Ah! How did that vanish?"
    show ps_catgirl oh worried closed with dissolve
    pc "Better"
    $ c.bottom = 0
    pc "Fuck!"
    pc "Well, whatever, no point in hiding now."
    show ps_catgirl open happy straight with dissolve
    pc "What are you looking at?"
    show ps_catgirl tounge cheeky with dissolve
    pc "Pffffft"
    hide ps_catgirl with dissolve
    $ pc_dress()
    $ walk(loc_school_darkroom)
    jump school_photo_quest_photoshoot_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
