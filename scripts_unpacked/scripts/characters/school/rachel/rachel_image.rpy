layeredimage rachel_body_layer:
    always "rachel_base"
    if rachel.heavy_preg:
        "rachel_base_preg2"
    elif rachel.showing:
        "rachel_base_preg1"
    if "can_bitch" in rachel.list:
        "rachel_extra_bitchcollar"

layeredimage rachel_outfit_uni_layer:
    if rachel.heavy_preg:
        "rachel_outfit_uni_preg2"
    elif rachel.showing: 
        "rachel_outfit_uni_preg1"
    else:
        "rachel_outfit_uni"

layeredimage rachel_outfit_casual_layer:
    if rachel.heavy_preg:
        "rachel_outfit_casual_preg2"
    elif rachel.showing:
        "rachel_outfit_casual_preg1"
    else:
        "rachel_outfit_casual"

layeredimage rachel_outfit_sport_layer:
    if rachel.heavy_preg:
        "rachel_outfit_sport_preg2"
    elif rachel.showing:
        "rachel_outfit_sport_preg1"
    else:
        "rachel_outfit_sport"


layeredimage rachel_outfit_dance_skirt_layer:
    if rachel.heavy_preg:
        "rachel_outfit_dance_skirt_preg2"
    elif rachel.showing:
        "rachel_outfit_dance_skirt_preg1"
    else:
        "rachel_outfit_dance_skirt"

layeredimage rachel_outfit_dance_knot_layer:
    if rachel.heavy_preg:
        "rachel_outfit_dance_knot_preg2"
    elif rachel.showing:
        "rachel_outfit_dance_knot_preg1"
    else:
        "rachel_outfit_dance_knot"

layeredimage rachel_outfit_nude_layer:
    always "rachel_outfit_nude"

layeredimage rachel_outfit_dance_first_layer:
    always "rachel_outfit_dance_skirt_layer"
    always "rachel_outfit_dance_knot_layer"
    always "rachel_outfit_dance_underwear"
    always "rachel_outfit_dance_tights"

layeredimage rachel_outfit_dance_notights_layer:
    always "rachel_outfit_dance_skirt_layer"
    always "rachel_outfit_dance_knot_layer"
    always "rachel_outfit_dance_underwear"

layeredimage rachel_outfit_dance_crop_layer:
    always "rachel_outfit_dance_skirt_layer"
    always "rachel_outfit_dance_crop"

layeredimage rachel_outfit_dance_topless_layer:
    always "rachel_outfit_dance_skirt_layer"
    always "rachel_outfit_nude"

layeredimage rachel_outfit_dance:
    if "nude" in rachel.list:
        "rachel_outfit_nude"
    elif "topless" in rachel.list:
        "rachel_outfit_dance_topless_layer"
    elif school_dance_quest_show_count >= 11:
        "rachel_outfit_dance_crop_layer"
    elif school_dance_quest_show_count >= 8:
        "rachel_outfit_dance_notights_layer"
    else:
        "rachel_outfit_dance_first_layer"

layeredimage rachel_outfit_standard:
    if school_dance_trope_present() and quest_dance.active and school_dance_quest_show_count >= 2 and rachel_here(loc_school_gym):
        "rachel_outfit_dance"
    elif rachel_here(location=dis_partyhouse):
        "rachel_outfit_dance"
    elif school_dance_trope_present() and rachel_here(loc_school_gym):
        "rachel_outfit_sport_layer"
    elif (rachel_exhib_stripping_show() or "streaking" in rachel.list) or rachel_here([loc_beach_gym, dis_park, loc_school_field_back]):
        "rachel_outfit_nude_layer"
    elif t.wkday in weekdays and t.hour in irange(7,13):
        "rachel_outfit_uni_layer"
    else:
        "rachel_outfit_casual_layer"

layeredimage rachel_face_neutral_layered:
    if rachel.drunk > 50:
        "rachel_face_drunk"
    else:
        "rachel_face_neutral"
layeredimage rachel_face_happy_layered:
    if rachel.drunk > 50:
        "rachel_face_drunk"
    else:
        "rachel_face_happy"
layeredimage rachel_face_angry_layered:
    if rachel.drunk > 50:
        "rachel_face_drunk"
    else:
        "rachel_face_angry"
layeredimage rachel_face_worried_layered:
    if rachel.drunk > 50:
        "rachel_face_drunk"
    else:
        "rachel_face_worried"

layeredimage rachel:
    at sprite_highlight("rachel")

    always "rachel_body_layer"

    group bitch: 
        attribute no_bitch_effects null default
        attribute bitch_effects "rachel_extra_bitcheffects"

    group face auto:
        attribute neutral default "rachel_face_neutral_layered"
        attribute happy "rachel_face_happy_layered"
        attribute angry "rachel_face_angry_layered"
        attribute worried "rachel_face_worried_layered"
        attribute drunk "rachel_face_drunk"


    group outfit auto:
        attribute standard default "rachel_outfit_standard"
        attribute casual "rachel_outfit_casual_layer"
        attribute sport "rachel_outfit_sport_layer"
        attribute uni "rachel_outfit_uni_layer"
        attribute nude "rachel_outfit_nude"
        attribute dance "rachel_outfit_dance"
        attribute dance1 "rachel_outfit_dance_first_layer"
        attribute dance2 "rachel_outfit_dance_notights_layer"
        attribute dance3 "rachel_outfit_dance_crop_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
