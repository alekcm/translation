layeredimage bg_party_kitchen_people_men_layered:
    if t.hour in (22,23,0,1,3) and not anabel_here():
        "bg_party_kitchen_people_men_3"
    if t.hour in (21,22,23,0,1,2,3,4):
        "bg_party_kitchen_people_men_2"
    always "bg_party_kitchen_people_men_1"


layeredimage bg_party_kitchen_people_dani_layered:
    always "bg_party_kitchen_people_dani_base"
    if dani.showing:
        "bg_party_kitchen_people_dani_preg"
    if not "topless" in dani.list:
        "bg_party_kitchen_people_dani_top"
    if not "nude" in dani.list:
        "bg_party_kitchen_people_dani_skirt"

layeredimage bg_party_kitchen_people_anabel_layered:
    always "bg_party_kitchen_people_anabel_base"
    if anabel.showing:
        "bg_party_kitchen_people_anabel_preg"
    if not "topless" in anabel.list:
        "bg_party_kitchen_people_anabel_top"
    if anabel.showing and not "nude" in anabel.list:
        "bg_party_kitchen_people_anabel_skirt_preg"
    elif not "nude" in anabel.list:
        "bg_party_kitchen_people_anabel_skirt"

layeredimage bg_party_kitchen_people_rachel_layered:
    always "bg_party_kitchen_people_rachel_base"
    if rachel.showing:
        "bg_party_kitchen_people_rachel_preg"
    if not "topless" in rachel.list:
        "bg_party_kitchen_people_rachel_top"
    if rachel.showing and not "nude" in rachel.list:
        "bg_party_kitchen_people_rachel_skirt_preg"
    elif not "nude" in rachel.list:
        "bg_party_kitchen_people_rachel_skirt"

layeredimage bg_party_kitchen_people_svet_layered:
    always "bg_party_kitchen_people_svet_base"
    if svet.showing:
        "bg_party_kitchen_people_svet_preg"
    if not "topless" in svet.list:
        "bg_party_kitchen_people_svet_top"
    if svet.showing and not "nude" in svet.list:
        "bg_party_kitchen_people_svet_skirt_preg"
    elif not "nude" in svet.list:
        "bg_party_kitchen_people_svet_skirt"

layeredimage bg_party_kitchen_layered:
    always "bg_party_kitchen_scene"
    if anabel_here() and not renpy.showing("anabel") and not "party_sex" in anabel.list:
        "bg_party_kitchen_people_anabel_layered"
    if svet_here() and not renpy.showing("svet") and not "party_sex" in svet.list:
        "bg_party_kitchen_people_svet_layered"
    if (t.wkday == "Saturday" and t.hour in (20,21,22,23)) or (t.wkday == "Sunday" and t.hour in (0,1,2,3,4)):
        "bg_party_kitchen_people_men_layered"
    if dani_here() and not renpy.showing("dani") and not "party_sex" in dani.list:
        "bg_party_kitchen_people_dani_layered"
    if rachel_here() and not renpy.showing("rachel") and not "party_sex" in rachel.list:
        "bg_party_kitchen_people_rachel_layered"

image bg_party_kitchen:
    "bg_party_kitchen_layered"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
