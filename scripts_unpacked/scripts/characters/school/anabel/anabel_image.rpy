layeredimage anabel_body_layer:
    always "anabel_base"
    if anabel.heavy_preg:
        "anabel_base_belly2"
    elif anabel.showing:
        "anabel_base_belly1"

layeredimage anabel_outfit_uni_layer:
    if anabel.heavy_preg:
        "anabel_outfit_uni_preg2"
    elif anabel.showing:
        "anabel_outfit_uni_preg1"
    else:
        "anabel_outfit_uni"

layeredimage anabel_outfit_casual_layer:
    if anabel.heavy_preg:
        "anabel_outfit_casual_preg2"
    elif anabel.showing:
        "anabel_outfit_casual_preg1"
    else:
        "anabel_outfit_casual"

layeredimage anabel_outfit_sport_layer:
    if anabel.heavy_preg:
        "anabel_outfit_sport_preg2"
    elif anabel.showing:
        "anabel_outfit_sport_preg1"
    else:
        "anabel_outfit_sport"



layeredimage anabel_outfit_dance_skirt_layer:
    if anabel.heavy_preg:
        "anabel_outfit_dance_skirt_preg2"
    elif anabel.showing:
        "anabel_outfit_dance_skirt_preg1"
    else:
        "anabel_outfit_dance_skirt"

layeredimage anabel_outfit_dance_knot_layer:
    if anabel.heavy_preg:
        "anabel_outfit_dance_knot_preg2"
    elif anabel.showing:
        "anabel_outfit_dance_knot_preg1"
    else:
        "anabel_outfit_dance_knot"

layeredimage anabel_outfit_dance_first_layer:
    always "anabel_outfit_dance_skirt_layer"
    always "anabel_outfit_dance_knot_layer"
    always "anabel_outfit_dance_underwear"
    always "anabel_outfit_dance_tights"

layeredimage anabel_outfit_dance_notights_layer:
    always "anabel_outfit_dance_skirt_layer"
    always "anabel_outfit_dance_knot_layer"
    always "anabel_outfit_dance_underwear"

layeredimage anabel_outfit_dance_crop_layer:
    always "anabel_outfit_dance_skirt_layer"
    always "anabel_outfit_dance_crop"

layeredimage anabel_outfit_dance_topless_layer:
    always "anabel_outfit_nude"
    always "anabel_outfit_dance_skirt_layer"
layeredimage anabel_outfit_dance_bottomless_layer:
    always "anabel_outfit_dance_crop"

layeredimage anabel_outfit_dance:
    if "nude" in anabel.list and "topless" in anabel.list:
        "anabel_outfit_nude"
    elif "nude" in anabel.list:
        "anabel_outfit_dance_bottomless_layer"
    elif "topless" in anabel.list:
        "anabel_outfit_dance_topless_layer"

    elif school_dance_quest_show_count >= 11:
        "anabel_outfit_dance_crop_layer"
    elif school_dance_quest_show_count >= 8:
        "anabel_outfit_dance_notights_layer"
    else:
        "anabel_outfit_dance_first_layer"

layeredimage anabel_outfit_standard:
    if school_dance_trope_present() and quest_dance.active and school_dance_quest_show_count >= 2 and anabel_here(loc_school_gym):
        "anabel_outfit_dance"
    elif anabel_here(location=dis_partyhouse):
        "anabel_outfit_dance"
    elif school_dance_trope_present() and anabel_here(loc_school_gym):
        "anabel_outfit_sport_layer"
    elif (t.wkday in weekdays and t.hour in irange(8,13)) or anabel_here([loc_school_cafe, loc_school_classroom]):
        "anabel_outfit_uni_layer"
    else:
        "anabel_outfit_casual_layer"

layeredimage anabel_face_neutral_layered:
    if anabel.drunk > 50:
        "anabel_face_drunk"
    else:
        "anabel_face_neutral"
layeredimage anabel_face_happy_layered:
    if anabel.drunk > 50:
        "anabel_face_drunk"
    else:
        "anabel_face_happy"
layeredimage anabel_face_angry_layered:
    if anabel.drunk > 50:
        "anabel_face_drunk"
    else:
        "anabel_face_angry"
layeredimage anabel_face_worried_layered:
    if anabel.is_tipsy:
        "anabel_face_drunk"
    else:
        "anabel_face_worried"

layeredimage anabel:
    at sprite_highlight("anabel")

    always "anabel_body_layer"
    group face auto:
        attribute neutral default "anabel_face_neutral_layered"
        attribute happy "anabel_face_happy_layered"
        attribute angry "anabel_face_angry_layered"
        attribute worried "anabel_face_worried_layered"
        attribute drunk "anabel_face_drunk"


    group outfit auto:
        attribute standard default "anabel_outfit_standard"
        attribute casual "anabel_outfit_casual_layer"
        attribute sport "anabel_outfit_sport_layer"
        attribute uni "anabel_outfit_uni_layer"
        attribute nude "anabel_outfit_nude"
        attribute dance "anabel_outfit_dance"
        attribute dance1 "anabel_outfit_dance_first_layer"
        attribute dance2 "anabel_outfit_dance_notights_layer"
        attribute dance3 "anabel_outfit_dance_crop_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
