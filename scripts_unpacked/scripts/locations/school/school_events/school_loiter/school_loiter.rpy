label loc_school_field_loiter:
    $ walk(loc_school_field)
    jump school_field_soccer_watch
label loc_school_field_back_loiter:
    $ walk(loc_school_field_back)
    jump school_field_soccer_hangout
label loc_school_library_loiter:
    $ walk(loc_school_library)
    jump school_library_relax


label dis_school_loiter_tombola:


    $ rand_choice = WeightedChoice([
    ("loc_school_field_loiter", If (can_loiter(loc_school_field) and drake.has_met and school_soccer_playing(), 100, 0)),
    ("loc_school_field_back_loiter", If (can_loiter(loc_school_field_back) and school_soccer_hangingout() and school_soccer_quest_hangout_prompt, 100, 0)),
    ("loc_school_library_loiter", If (can_loiter(loc_school_library), 25, 0)),
    ("loc_school_classroom_loiter", If (can_loiter(loc_school_classroom), 25, 0)),
    ("loc_school_cafe_loiter", If (can_loiter(loc_school_cafe), 25, 0)),
    ("loc_school_loiter", If (can_loiter(loc_school), 1, 0)),
    ("loc_school_robin_chat", If (robin_here(loc_school_hallway), 100, 0)),
    ("loc_school_cass_chat", If (cass_here([loc_school_classroom, loc_school]), 100, 0)),
    ("loc_school_dani_chat", If (dani_here([loc_school_cafe, loc_school]) and not t.hour == 12, 100, 0)),
    ("loc_school_sas_chat", If ((saskia_here(loc_school_sewroom) or frida_here(loc_school_sewroom)) and can_loiter(loc_school_sewroom), 100, 0)),
    ])
    jump expression rand_choice

label loc_school_loiter:
    $ walk(loc_school)
    "School is closed so I hang out by the entrance with not much to do."
    $ loiter()
    jump travel

label loc_school_classroom_loiter:
    $ walk(loc_school_classroom)
    "Hang out in the classroom."
    $ loiter()
    jump travel

label loc_school_cafe_loiter:
    $ walk(loc_school_cafe)
    "Hang out in the cafe."
    $ loiter()
    jump travel

label loc_school_robin_chat:
    $ walk(robin_here(class_loc=True))
    jump robin_talk_picker

label loc_school_cass_chat:
    $ walk(cass_here(class_loc=True))
    if mira_here():
        jump cass_mira_talk_picker
    else:
        jump cass_talk_subject

label loc_school_dani_chat:
    $ walk(dani_here(class_loc=True))
    jump dani_talk_subject

label loc_school_sas_chat:
    $ walk(loc_school_sewroom)
    jump saskia_frida_talk_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
