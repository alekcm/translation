layeredimage svet_body_layer:
    always "svet_base"
    if svet.heavy_preg:
        "svet_base_preg2"
    elif svet.showing:
        "svet_base_preg1"

layeredimage svet_outfit_uni_layer:
    if svet.heavy_preg:
        "svet_outfit_uni_preg2"
    elif svet.showing:
        "svet_outfit_uni_preg1"
    else:
        "svet_outfit_uni"

layeredimage svet_outfit_casual_layer:
    if svet.heavy_preg:
        "svet_outfit_casual_preg2"
    elif svet.showing:
        "svet_outfit_casual_preg1"
    else:
        "svet_outfit_casual"

layeredimage svet_outfit_sport_layer:
    if svet.heavy_preg:
        "svet_outfit_sport_preg2"
    elif svet.showing:
        "svet_outfit_sport_preg1"
    else:
        "svet_outfit_sport"



layeredimage svet_outfit_dance_skirt_layer:
    if svet.heavy_preg:
        "svet_outfit_dance_skirt_preg2"
    elif svet.showing:
        "svet_outfit_dance_skirt_preg1"
    else:
        "svet_outfit_dance_skirt"

layeredimage svet_outfit_dance_knot_layer:
    if svet.heavy_preg:
        "svet_outfit_dance_knot_preg2"
    elif svet.showing:
        "svet_outfit_dance_knot_preg1"
    else:
        "svet_outfit_dance_knot"

layeredimage svet_outfit_dance_first_layer:
    always "svet_outfit_dance_underwear"
    always "svet_outfit_dance_skirt_layer"
    always "svet_outfit_dance_knot_layer"
    always "svet_outfit_dance_tights"

layeredimage svet_outfit_dance_notights_layer:
    always "svet_outfit_dance_underwear"
    always "svet_outfit_dance_skirt_layer"
    always "svet_outfit_dance_knot_layer"


layeredimage svet_outfit_dance_crop_layer:
    always "svet_outfit_dance_skirt_layer"
    always "svet_outfit_dance_crop"

layeredimage svet_outfit_dance_topless_layer:
    always "svet_outfit_dance_skirt_layer"
    always "svet_outfit_nude"
layeredimage svet_outfit_dance_bottomless_layer:
    always "svet_outfit_dance_crop"

layeredimage svet_outfit_dance:
    if "nude" in svet.list and "topless" in svet.list:
        "svet_outfit_nude"
    elif "nude" in svet.list:
        "svet_outfit_dance_bottomless_layer"
    elif "topless" in svet.list:
        "svet_outfit_dance_topless_layer"
    elif school_dance_quest_show_count >= 11:
        "svet_outfit_dance_crop_layer"
    elif school_dance_quest_show_count >= 8:
        "svet_outfit_dance_notights_layer"
    else:
        "svet_outfit_dance_first_layer"



layeredimage svet_outfit_standard:
    if school_dance_trope_present() and quest_dance.active and school_dance_quest_show_count >= 2 and svet_here(loc_school_gym):
        "svet_outfit_dance"
    elif svet_here(location=dis_partyhouse):
        "svet_outfit_dance"
    elif school_dance_trope_present() and svet_here(loc_school_gym):
        "svet_outfit_sport_layer"
    elif t.wkday in weekdays and t.hour in irange(7,13):
        "svet_outfit_uni_layer"
    else:
        "svet_outfit_casual_layer"

layeredimage svet_face_neutral_layered:
    if svet.drunk > 50:
        "svet_face_drunk"
    else:
        "svet_face_neutral"
layeredimage svet_face_happy_layered:
    if svet.drunk > 50:
        "svet_face_drunk"
    else:
        "svet_face_happy"
layeredimage svet_face_angry_layered:
    if svet.drunk > 50:
        "svet_face_drunk"
    else:
        "svet_face_angry"
layeredimage svet_face_worried_layered:
    if svet.drunk > 50:
        "svet_face_drunk"
    else:
        "svet_face_worried"

image svet = LayeredImageProxy("svet_layer", Transform(xoffset =(75)))

layeredimage svet_layer:
    at sprite_highlight("svet")

    always "svet_body_layer"
    group face auto:
        attribute neutral default "svet_face_neutral_layered"
        attribute happy "svet_face_happy_layered"
        attribute angry "svet_face_angry_layered"
        attribute worried "svet_face_worried_layered"
        attribute drunk "svet_face_drunk"


    group outfit auto:
        attribute standard default "svet_outfit_standard"
        attribute casual "svet_outfit_casual_layer"
        attribute sport "svet_outfit_sport_layer"
        attribute uni "svet_outfit_uni_layer"
        attribute nude "svet_outfit_nude"
        attribute dance "svet_outfit_dance"
        attribute dance1 "svet_outfit_dance_first_layer"
        attribute dance2 "svet_outfit_dance_notights_layer"
        attribute dance3 "svet_outfit_dance_crop_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
