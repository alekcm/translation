layeredimage bg_party_stage_people_men_layered:
    if t.hour in (22,23,0,2,3):
        "bg_party_stage_people_man_2"
    always "bg_party_stage_people_man_1"
    if t.hour in (22,0,1,3):
        "bg_party_stage_people_man_3"
    if t.hour in (21,23,2):
        "bg_party_stage_people_man_4"
    if t.hour in (23,0,1):
        "bg_party_stage_people_man_5"
    if t.hour in (23,0,1,2):
        "bg_party_stage_people_man_6"
layeredimage bg_party_stage_people_men_full_layered:
    always "bg_party_stage_people_man_2"
    always "bg_party_stage_people_man_1"
    always "bg_party_stage_people_man_3"
    always "bg_party_stage_people_man_4"
    always "bg_party_stage_people_man_5"
    always "bg_party_stage_people_man_6"

layeredimage bg_party_stage_people_dani_layered:
    always "bg_party_stage_people_dani_base"
    if dani.showing:
        "bg_party_stage_people_dani_preg"
    if not "topless" in dani.list:
        "bg_party_stage_people_dani_top"
    if dani.showing and not "nude" in dani.list:
        "bg_party_stage_people_dani_skirt_preg"
    elif not "nude" in dani.list:
        "bg_party_stage_people_dani_skirt"
layeredimage bg_party_stage_people_dance_dani_layered:
    always "bg_party_stage_people_dance_dani_base"
    if dani.showing:
        "bg_party_stage_people_dance_dani_preg"
    if not "topless" in dani.list:
        "bg_party_stage_people_dance_dani_top"
    if dani.showing and not "nude" in dani.list:
        "bg_party_stage_people_dance_dani_skirt_preg"
    elif not "nude" in dani.list:
        "bg_party_stage_people_dance_dani_skirt"

layeredimage bg_party_stage_people_anabel_layered:
    always "bg_party_stage_people_anabel_base"
    if anabel.showing:
        "bg_party_stage_people_anabel_preg"
    if not "topless" in anabel.list:
        "bg_party_stage_people_anabel_top"
    if anabel.showing and not "nude" in anabel.list:
        "bg_party_stage_people_anabel_skirt_preg"
    elif not "nude" in anabel.list:
        "bg_party_stage_people_anabel_skirt"
layeredimage bg_party_stage_people_dance_anabel_layered:
    always "bg_party_stage_people_dance_anabel_base"
    if anabel.showing:
        "bg_party_stage_people_dance_anabel_preg"
    if not "topless" in anabel.list:
        "bg_party_stage_people_dance_anabel_top"
    if anabel.showing and not "nude" in anabel.list:
        "bg_party_stage_people_dance_anabel_skirt_preg"
    elif not "nude" in anabel.list:
        "bg_party_stage_people_dance_anabel_skirt"

layeredimage bg_party_stage_people_rachel_layered:
    always "bg_party_stage_people_rachel_base"
    if rachel.showing:
        "bg_party_stage_people_rachel_preg"
    if not "topless" in rachel.list:
        "bg_party_stage_people_rachel_top"
    if not "nude" in rachel.list:
        "bg_party_stage_people_rachel_skirt"
layeredimage bg_party_stage_people_dance_rachel_layered:
    always "bg_party_stage_people_dance_rachel_base"
    if rachel.showing:
        "bg_party_stage_people_dance_rachel_preg"
    if not "topless" in rachel.list:
        "bg_party_stage_people_dance_rachel_top"
    if not "nude" in rachel.list:
        "bg_party_stage_people_dance_rachel_skirt"

layeredimage bg_party_stage_people_svet_layered:
    always "bg_party_stage_people_svet_base"
    if svet.showing:
        "bg_party_stage_people_svet_preg"
    if not "topless" in svet.list:
        "bg_party_stage_people_svet_top"
    if svet.showing and not "nude" in svet.list:
        "bg_party_stage_people_svet_skirt_preg"
    elif not "nude" in svet.list:
        "bg_party_stage_people_svet_skirt"
layeredimage bg_party_stage_people_dance_svet_layered:
    always "bg_party_stage_people_dance_svet_base"
    if svet.showing:
        "bg_party_stage_people_dance_svet_preg"
    if not "topless" in svet.list:
        "bg_party_stage_people_dance_svet_top"
    if not "nude" in svet.list:
        "bg_party_stage_people_dance_svet_skirt"

layeredimage bg_party_stage_people_girls_stand_layered:
    if dani_here() and not renpy.showing("dani") and not "party_sex" in dani.list:
        "bg_party_stage_people_dani_layered"
    if rachel_here() and not renpy.showing("rachel") and not "party_sex" in rachel.list:
        "bg_party_stage_people_rachel_layered"
    if anabel_here() and not renpy.showing("anabel") and not "party_sex" in anabel.list:
        "bg_party_stage_people_anabel_layered"
    if svet_here() and not renpy.showing("svet") and not "party_sex" in svet.list:
        "bg_party_stage_people_svet_layered"

layeredimage bg_party_stage_people_girls_dance_layered:
    if dani_here() and not renpy.showing("dani") and not "party_sex" in dani.list:
        "bg_party_stage_people_dance_dani_layered"
    if rachel_here() and not renpy.showing("rachel") and not "party_sex" in rachel.list:
        "bg_party_stage_people_dance_rachel_layered"
    if anabel_here() and not renpy.showing("anabel") and not "party_sex" in anabel.list:
        "bg_party_stage_people_dance_anabel_layered"
    if svet_here() and not renpy.showing("svet") and not "party_sex" in svet.list:
        "bg_party_stage_people_dance_svet_layered"

layeredimage bg_party_stage_people_girls_layered:
    if dance_is_dancing():
        "bg_party_stage_people_girls_dance_layered"
    else:
        "bg_party_stage_people_girls_stand_layered"

layeredimage bg_party_stage_layered:
    always "bg_party_stage_scene"

    always "bg_party_stage_people_girls_layered"

    if dance_is_dancing():
        "bg_party_stage_people_men_full_layered"
    if (t.wkday == "Saturday" and t.hour in (20,21,22,23)) or (t.wkday == "Sunday" and t.hour in (0,1,2,3,4)):
        "bg_party_stage_people_men_layered"


image bg_party_stage:
    "bg_party_stage_layered"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
