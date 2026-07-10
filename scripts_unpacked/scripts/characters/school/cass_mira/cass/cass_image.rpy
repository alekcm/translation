layeredimage cass_body_layer:
    always "cass_base"
    if cass.heavy_preg:
        "cass_base_preg2"
    elif cass.showing:
        "cass_base_preg1"

layeredimage cass_outfit_uni_layer:
    always "cass_outfit_uni_base"
    if cass.heavy_preg:
        "cass_outfit_uni_preg2"
    elif cass.showing:
        "cass_outfit_uni_preg1"

layeredimage cass_outfit_swim_layer:
    always "cass_outfit_swim_base"
    if cass.heavy_preg:
        "cass_outfit_swim_preg2"
    elif cass.showing:
        "cass_outfit_swim_preg1"

layeredimage cass_outfit_casual_layer:
    always "cass_outfit_casual_base"
    if cass.heavy_preg:
        "cass_outfit_casual_preg2"
    elif cass.showing:
        "cass_outfit_casual_preg1"

layeredimage cass_outfit_slut_layer:
    always "cass_outfit_slut_base"
    if cass.heavy_preg:
        "cass_outfit_slut_preg2"
    elif cass.showing:
        "cass_outfit_slut_preg1"

layeredimage cass_outfit_bimbo_layer:
    always "cass_outfit_nude"
    if cass.heavy_preg:
        "cass_outfit_bimbo_preg2"
    elif cass.showing:
        "cass_outfit_bimbo_preg1"
    else:
        "cass_outfit_bimbo_base"

layeredimage cass_underwear1_layer:
    if cass.heavy_preg:
        "cass_underwear1_preg2"
    elif cass.showing:
        "cass_underwear1_preg1"
    else:
        "cass_underwear1_base"

layeredimage cass_underwear2_layer:
    always "cass_outfit_nude"
    if cass.heavy_preg:
        "cass_underwear2_preg2"
    else:
        "cass_underwear2_base"

layeredimage cass_outfit_standard:
    if cass_here(dis_beach.locs):  
        "cass_outfit_swim_layer"
    elif t.wkday in weekdays and (t.hour in school_hours or t.hour == 7) :
        "cass_outfit_uni_layer"
    elif cass_here(dis_truckstop.locs) and cass.iswhore and (cass.noon_number % 2):
        "cass_outfit_slut_layer"
    elif cass_here(dis_truckstop.locs) and cass.iswhore:
        "cass_outfit_bimbo_layer"
    else:
        "cass_outfit_casual_layer"

layeredimage cass_face_neutral_layer:
    if "broken" in cass.list:
        "cass_face_dull"
    if cass.iswhore and dis(dis_truckstop) and not "broken" in cass.list:
        "cass_face_neutral_lipstick"
    if not "broken" in cass.list:
        "cass_face_neutral"
layeredimage cass_face_laugh_layer:
    if cass.iswhore and dis(dis_truckstop):
        "cass_face_laugh_lipstick"
    always "cass_face_laugh"
layeredimage cass_face_cry_layer:
    if cass.iswhore and dis(dis_truckstop):
        "cass_face_cry_lipstick"
    always "cass_face_cry"
layeredimage cass_face_angry_layer:
    if cass.iswhore and dis(dis_truckstop):
        "cass_face_angry_lipstick"
    always "cass_face_angry"
layeredimage cass_face_worried_layer:
    if cass.iswhore and dis(dis_truckstop):
        "cass_face_angry_lipstick"
    always "cass_face_worried"


layeredimage cass:
    at sprite_highlight("cass") 
    always "cass_body_layer"

    if cass.iswhore and dis(dis_truckstop):
        "cass_face_eyeshadow"

    group face:
        attribute neutral default "cass_face_neutral_layer"
        attribute angry "cass_face_angry_layer"
        attribute cry "cass_face_cry_layer"
        attribute laugh "cass_face_laugh_layer"
        attribute happy "cass_face_laugh_layer" 
        attribute worried "cass_face_worried_layer"
        attribute dull "cass_face_dull"

    group outfit:
        attribute nude:
            "cass_outfit_nude"
        attribute no_outfit:
            "cass_outfit_nude"
        attribute standard default:
            "cass_outfit_standard"
        attribute uni:
            "cass_outfit_uni_layer"
        attribute swim:
            "cass_outfit_swim_layer"
        attribute casual:
            "cass_outfit_casual_layer"
        attribute slut:
            "cass_outfit_slut_layer"
        attribute bimbo:
            "cass_outfit_bimbo_layer"
        attribute underwear1: 
            "cass_underwear1_layer"
        attribute underwear2:
            "cass_underwear2_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
