image dance_girls_anabel = LayeredImageProxy("dance_girls_anabel_layered", Transform(xalign = (0.7)))

layeredimage dance_girls_anabel_layered:

    if loc(loc_school_gym):
        "dance_girls_anabel_bg_gym"
    else:
        "dance_girls_anabel_bg_grass"

    always "dance_girls_anabel_body"

    if school_dance_quest_show_count >= 11:
        "dance_girls_anabel_clothes_crop"
    else:
        "dance_girls_anabel_clothes_knot"

    if school_dance_quest_show_count < 11:
        "dance_girls_anabel_clothes_bra"

    always "dance_girls_anabel_clothes_skirt"
    always "dance_girls_anabel_frame"

image dance_girls_dani = LayeredImageProxy("dance_girls_dani_layered", Transform(xalign = (0.7)))

layeredimage dance_girls_dani_layered:

    if loc(loc_school_gym):
        "dance_girls_dani_bg_gym"
    else:
        "dance_girls_dani_bg_grass"

    always "dance_girls_dani_body"

    if "topless" in dani.list:
        "dance_girls_dani_nude"
    elif school_dance_quest_show_count >= 11:
        "dance_girls_dani_crop"
    else:
        "dance_girls_dani_knot"

image dance_girls_rachel = LayeredImageProxy("dance_girls_rachel_layered", Transform(xalign = (0.7)))

layeredimage dance_girls_rachel_layered:

    if loc(loc_school_gym):
        "dance_girls_rachel_bg_gym"
    else:
        "dance_girls_rachel_bg_grass"

    always "dance_girls_rachel_body"


    if school_dance_quest_show_count >= 11 and not rachel_exhib_stripping_show():
        "dance_girls_rachel_clothes_pink"

    if not rachel_exhib_stripping_show():
        "dance_girls_rachel_clothes_skirt"

    if school_dance_quest_show_count >= 11 and not rachel_exhib_stripping_show():
        "dance_girls_rachel_clothes_crop"
    elif not rachel_exhib_stripping_show():
        "dance_girls_rachel_clothes_knot"

    if school_dance_quest_show_count < 11 and not rachel_exhib_stripping_show():
        "dance_girls_rachel_clothes_bra"
    if school_dance_quest_show_count < 11 and not rachel_exhib_stripping_show():
        "dance_girls_rachel_clothes_pants"


    if school_dance_quest_show_count <= 7 and not rachel_exhib_stripping_show():
        "dance_girls_rachel_clothes_tights"

image dance_girls_svet = LayeredImageProxy("dance_girls_svet_layered", Transform(xalign = (0.7)))

layeredimage dance_girls_svet_layered:

    if loc(loc_school_gym):
        "dance_girls_svet_bg_gym"
    else:
        "dance_girls_svet_bg_grass"

    always "dance_girls_svet_body"

    if school_dance_quest_show_count >= 11 and not "topless" in svet.list:
        "dance_girls_svet_crop"
    elif not "topless" in svet.list:
        "dance_girls_svet_knot"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
