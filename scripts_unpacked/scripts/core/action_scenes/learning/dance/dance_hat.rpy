layeredimage anabel_hat_front:
    always "anabel_hat_front_bg"
    if t.minute % 2 == 0:
        "anabel_hat_front_bg_man1"
    if t.minute % 3 != 0:
        "anabel_hat_front_bg_man2"

    always "anabel_hat_front_body" 

    if school_dance_quest_show_count >= 11:
        "anabel_hat_front_clothes_top_crop"
    else:
        "anabel_hat_front_clothes_top_knot"

    if school_dance_quest_show_count <= 7:
        "anabel_hat_front_clothes_tights"

    always "anabel_hat_front_clothes_skirt"

    always "anabel_hat_front_frame"

layeredimage anabel_hat_lower:
    always "anabel_hat_lower_bg"


    if school_dance_quest_show_count >= 11:
        "anabel_hat_lower_crop"
    else:
        "anabel_hat_lower_knot"

    always "anabel_hat_lower_frame"

layeredimage dani_hat_front:
    always "dani_hat_front_bg"
    if t.minute % 2 == 0:
        "dani_hat_front_bg_man1"


    always "dani_hat_front_body_base" 
    if dani.heavy_preg:
        "dani_hat_front_body_belly_2"
    elif dani.showing:
        "dani_hat_front_body_belly_1"

    if school_dance_quest_show_count >= 11:
        "dani_hat_front_crop"
    elif dani.heavy_preg:
        "dani_hat_front_knot_2"
    elif dani.showing:
        "dani_hat_front_knot_1"
    else:
        "dani_hat_front_knot_0"

    if dani.heavy_preg:
        "dani_hat_front_skirt_2"
    elif dani.showing:
        "dani_hat_front_skirt_1"
    else:
        "dani_hat_front_skirt_0"

    if t.minute % 2 != 0:
        "dani_hat_front_fg_man2"
    if t.minute % 3 != 0:
        "dani_hat_front_fg_man1"

    always "dani_hat_front_frame"

layeredimage dani_hat_ass:
    always "dani_hat_ass_bg"

    always "dani_hat_ass_body_main" 

    if school_dance_quest_show_count < 11:
        "dani_hat_ass_knot"



    if school_dance_quest_show_count < 11:
        "dani_hat_ass_body_pants"
    else:
        "dani_hat_ass_thong"

    if school_dance_quest_show_count <= 7:
        "dani_hat_ass_tights"

    always "dani_hat_ass_body_skirt"
    always "dani_hat_ass_frame"

layeredimage rachel_hat_front:
    always "rachel_hat_front_bg"
    if t.minute % 2 == 0:
        "rachel_hat_front_bg_man2"
    if t.minute % 3 != 0:
        "rachel_hat_front_bg_man1"

    always "rachel_hat_front_body"
    if rachel.showing:
        "rachel_hat_front_body_belly"

    if school_dance_quest_show_count >= 11:
        "rachel_hat_front_outfit_top_crop"
    else:
        "rachel_hat_front_outfit_top_knot"

    if school_dance_quest_show_count <= 7:
        "rachel_hat_front_outfit_tights"

    if rachel.showing:
        "rachel_hat_front_outfit_skirt_preg"
    else:
        "rachel_hat_front_outfit_skirt"

    if t.minute % 3 == 0 or t.minute % 3 == 1:
        "rachel_hat_front_fg_man1"

    always "rachel_hat_front_frame"

layeredimage rachel_hat_back:
    always "rachel_hat_back_bg"





    always "rachel_hat_back_body"


    if school_dance_quest_show_count >= 11:
        "rachel_hat_back_outfit_top_crop"
    else:
        "rachel_hat_back_outfit_top_knot"

    always "rachel_hat_back_outfit_skirt"

    if school_dance_quest_show_count <= 7:
        "rachel_hat_back_outfit_tights"
    if school_dance_quest_show_count < 11:
        "rachel_hat_back_outfit_pants"




    always "rachel_hat_back_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
