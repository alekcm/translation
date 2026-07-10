init python:
    def dani_yan_value():
        dani_yan_settings()  
        
        if "freakout_blocked" in dani.list:
            
            return 0
        
        elif dani.dict["yan_value"] >= dani.dict["yan_max"]:
            total_amount = dani.dict["yan_max"]
        
        else:
            total_amount = int(dani.dict["yan_value"])
        if total_amount >= 100:
            dani._lust_multi = 6
        elif total_amount >= 50:
            dani._lust_multi = 2
        else:
            dani._lust_multi = 0
        return total_amount

    def dani_yan_add(amount):
        
        dani_yan_settings()
        
        force_multi = float(dani.rape) / 5 
        
        total_multi = force_multi + dani.dict["yan_multi"]
        
        amount = amount * total_multi
        
        dani.dict["yan_value"] += amount
        
        if dani.dict["yan_value"] >= dani.dict["yan_max"]:
            dani.dict["yan_value"] = dani.dict["yan_max"]


    def dani_yan_remove(amount):
        dani_yan_settings()
        
        dani.dict["yan_value"] -= amount
        
        if dani.dict["yan_value"] < 0:
            dani.dict["yan_value"] = 0

    def dani_yan_max_add(amount):
        dani_yan_face_pick()
        
        dani.dict["yan_max"] += amount
        
        if dani.dict["yan_max"] <= 0:
            dani.dict["yan_max"] = 0
        if dani.dict["yan_max"] >= 250:
            
            dani.dict["yan_max"] = 250

    def dani_yan_settings():
        
        if not "yan_value" in dani.dict:
            dani.dict["yan_value"] = 0
        if not "yan_max" in dani.dict:
            dani.dict["yan_max"] = 0
        if not "yan_multi" in dani.dict:
            dani.dict["yan_multi"] = 1


    def dani_yan_face_pick():
        
        return weightgen(dani_yan_value(), 100 - dani_yan_value())

layeredimage dani_base_layer:
    always "dani_base"  
    if dani.heavy_preg:
        "dani_base_preg2"
    elif dani.showing:
        "dani_base_preg1"
    if dani_yan_value() >= 20:
        "dani_yan_cuts"

layeredimage dani_outfit_casual_layer:
    if dani.heavy_preg:
        "dani_outfit_casual_preg2"
    elif dani.showing:
        "dani_outfit_casual_preg1"
    else:
        "dani_outfit_casual"

layeredimage dani_outfit_sleep_layer:
    if dani.heavy_preg:
        "dani_outfit_sleep_preg2"
    elif dani.showing:
        "dani_outfit_sleep_preg1"
    else:
        "dani_outfit_sleep"

layeredimage dani_outfit_underwear_layer:
    if dani.heavy_preg:
        "dani_outfit_underwear_preg2"
    elif dani.showing:
        "dani_outfit_underwear_preg1"
    else:
        "dani_outfit_underwear"

layeredimage dani_outfit_swim_layer:
    always "dani_outfit_swim"
    if dani.heavy_preg:
        "dani_outfit_swim_preg2"
    elif dani.showing:
        "dani_outfit_swim_preg1"

layeredimage dani_outfit_uni_layer:
    always "dani_outfit_school"
    if dani.heavy_preg:
        "dani_outfit_school_preg2"
    elif dani.showing:
        "dani_outfit_school_preg1"

layeredimage dani_outfit_sport_layer:
    if dani.heavy_preg:
        "dani_outfit_sport_preg2"
    elif dani.showing:
        "dani_outfit_sport_preg1"
    else:
        "dani_outfit_sport"

layeredimage dani_outfit_pub_layer:
    always "dani_outfit_pub"
    if dani.heavy_preg:
        "dani_outfit_pub_preg2"
    elif dani.showing:
        "dani_outfit_pub_preg1"

layeredimage dani_outfit_strapon_layer:
    if dani.heavy_preg:
        "dani_outfit_strapon_preg2"
    elif dani.showing:
        "dani_outfit_strapon_preg1"
    else:
        "dani_outfit_strapon"

layeredimage dani_outfit_dance_skirt_layer:
    if dani.heavy_preg:
        "dani_outfit_dance_skirt_preg2"
    elif dani.showing:
        "dani_outfit_dance_skirt_preg1"
    else:
        "dani_outfit_dance_skirt"

layeredimage dani_outfit_dance_knot_layer:
    if dani.heavy_preg:
        "dani_outfit_dance_knot_preg2"
    elif dani.showing:
        "dani_outfit_dance_knot_preg1"
    else:
        "dani_outfit_dance_knot"

layeredimage dani_outfit_nude_layer:
    if junk_var:
        "dani_base"

layeredimage dani_outfit_dance_first_layer:
    always "dani_outfit_dance_tights"
    always "dani_outfit_dance_skirt_layer"
    always "dani_outfit_dance_knot_layer"
    always "dani_outfit_dance_underwear"


layeredimage dani_outfit_dance_notights_layer:
    always "dani_outfit_dance_skirt_layer"
    always "dani_outfit_dance_knot_layer"
    always "dani_outfit_dance_underwear"

layeredimage dani_outfit_dance_crop_layer:
    always "dani_outfit_dance_skirt_layer"
    always "dani_outfit_dance_crop"

layeredimage dani_outfit_dance_topless_layer:
    always "dani_outfit_dance_skirt_layer"
    always "dani_outfit_nude_layer"

layeredimage dani_outfit_dance_bottomless_layer:
    always "dani_outfit_dance_crop"

layeredimage dani_outfit_dance:
    if "nude" in dani.list and "topless" in dani.list:
        "dani_outfit_nude_layer"
    elif "nude" in dani.list:
        "dani_outfit_dance_bottomless_layer"
    elif "topless" in dani.list:
        "dani_outfit_dance_topless_layer"
    elif school_dance_quest_show_count >= 11:
        "dani_outfit_dance_crop_layer"
    elif school_dance_quest_show_count >= 8:
        "dani_outfit_dance_notights_layer"
    else:
        "dani_outfit_dance_first_layer"

layeredimage dani_outfit_standard:
    if school_dance_trope_present() and quest_dance.active and school_dance_quest_show_count >= 2 and dani_here(loc_school_gym):
        "dani_outfit_dance"
    elif dani_here(location=dis_partyhouse):
        "dani_outfit_dance"
    elif school_dance_trope_present() and dani_here(loc_school_gym):
        "dani_outfit_sport_layer"
    elif dani_here(dis_pub.locs):
        "dani_outfit_pub_layer"
    elif t.hour in (21,22,23,0,1,2,3,4,5,6,7,8,9) and dani_here(loc_bedroom_dani):
        "dani_outfit_sleep_layer"
    elif t.wkday in weekdays and t.hour in irange(8,13):
        "dani_outfit_uni_layer"
    else:
        "dani_outfit_casual_layer"

layeredimage dani_face_neutral_layer:
    if dani.drunk > 50:
        "dani_face_drunk"
    elif dani_yan_face_pick():
        "dani_face_yneutral"
    else:
        "dani_face_neutral"

layeredimage dani_face_happy_layer:
    if dani.drunk > 50:
        "dani_face_drunk"
    elif dani_yan_face_pick():
        "dani_face_yhappy"
    else:
        "dani_face_happy"

layeredimage dani_face_worried_layer:
    if dani.drunk > 50:
        "dani_face_drunk"
    elif dani_yan_face_pick():
        "dani_face_yworried"
    else:
        "dani_face_worried"

layeredimage dani_face_angry_layer:
    if dani.drunk > 50:
        "dani_face_drunk"
    elif dani_yan_face_pick():
        "dani_face_yangry"
    else:
        "dani_face_angry"


layeredimage dani:
    at sprite_highlight("dani")
    always "dani_base_layer"

    group face auto:
        attribute neutral default "dani_face_neutral_layer"
        attribute worried "dani_face_worried_layer"
        attribute angry "dani_face_angry_layer"
        attribute happy "dani_face_happy_layer"
        attribute crazy "dani_face_ycrazy"
        attribute derp "dani_face_yderp"


    group outfit auto:
        attribute standard default "dani_outfit_standard"
        attribute casual "dani_outfit_casual_layer"
        attribute sport "dani_outfit_sport_layer"
        attribute uni "dani_outfit_uni_layer"
        attribute pub "dani_outfit_pub_layer"
        attribute sleep "dani_outfit_sleep_layer"
        attribute dance "dani_outfit_dance"
        attribute dance1 "dani_outfit_dance_first_layer"
        attribute dance2 "dani_outfit_dance_notights_layer"
        attribute dance3 "dani_outfit_dance_crop_layer"
        attribute underwear "dani_outfit_underwear_layer"
        attribute nude "dani_outfit_nude_layer"
        attribute nooutfit "dani_outfit_nude_layer"
        attribute strapon "dani_outfit_strapon_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
