image robin_lipstick_neutral_pink:
    "robin_lipstick_neutral"
    matrixcolor TintMatrix(Color(rgb=(0.8471, 0.2784, 0.7059)))
image robin_lipstick_worried_pink:
    "robin_lipstick_worried"
    matrixcolor TintMatrix(Color(rgb=(0.8471, 0.2784, 0.7059)))
image robin_lipstick_angry_pink:
    "robin_lipstick_angry"
    matrixcolor TintMatrix(Color(rgb=(0.8471, 0.2784, 0.7059)))
image robin_lipstick_happy_pink:
    "robin_lipstick_happy"
    matrixcolor TintMatrix(Color(rgb=(0.8471, 0.2784, 0.7059)))
image robin_lipstick_drunk_pink:
    "robin_lipstick_drunk"
    matrixcolor TintMatrix(Color(rgb=(0.8471, 0.2784, 0.7059)))


image robin_lipstick_neutral_red:
    "robin_lipstick_neutral"
    matrixcolor TintMatrix(Color(rgb=(0.8667, 0.1412, 0.1412)))
image robin_lipstick_worried_red:
    "robin_lipstick_worried"
    matrixcolor TintMatrix(Color(rgb=(0.8667, 0.1412, 0.1412)))
image robin_lipstick_angry_red:
    "robin_lipstick_angry"
    matrixcolor TintMatrix(Color(rgb=(0.8667, 0.1412, 0.1412)))
image robin_lipstick_happy_red:
    "robin_lipstick_happy"
    matrixcolor TintMatrix(Color(rgb=(0.8667, 0.1412, 0.1412)))
image robin_lipstick_drunk_red:
    "robin_lipstick_drunk"
    matrixcolor TintMatrix(Color(rgb=(0.8667, 0.1412, 0.1412)))


layeredimage robin_base_layer:
    always "robin_base"
    if robin.heavy_preg:
        "robin_base_2"
    elif robin.showing:
        "robin_base_1"
    if "can_bitch" in robin.list and robin_here(loc_park):
        "robin_bitchcollar"


layeredimage robin_base_cuffed_layer:
    always "robin_base_cuffed"
    if robin.heavy_preg:
        "robin_base_2"
    elif robin.showing:
        "robin_base_1"

layeredimage robin_outfit_nude_layer:
    always "robin_outfit_nude"
    always "robin_hair"

layeredimage robin_outfit_nude_makeup_layer:
    always "robin_outfit_nude"
    always "robin_hair_pink"

layeredimage robin_outfit_uni_layer:
    always "robin_outfit_uni"
    if robin.heavy_preg:
        "robin_outfit_uni_preg2"
    elif robin.showing:
        "robin_outfit_uni_preg1"
    always "robin_head_shad_hair"
    always "robin_hair"

layeredimage robin_outfit_sport_layer:
    always "robin_outfit_sport"
    if robin.heavy_preg:
        "robin_outfit_sport_preg2"
    elif robin.showing:
        "robin_outfit_sport_preg1"

    if loc_cur.outside and weather_var == 1:
        "robin_head_shad_hat"
    else:
        "robin_head_shad_hair"
    if loc_cur.outside and weather_var == 1:
        "robin_hat"
    else:
        "robin_hair"

layeredimage robin_outfit_baggy_winter_layer:
    if robin.heavy_preg:
        "robin_outfit_baggywinter_preg2"
    elif robin.showing:
        "robin_outfit_baggywinter_preg1"
    else:
        "robin_outfit_baggywinter"

layeredimage robin_outfit_baggy_layer:
    always "robin_outfit_baggy"
    if robin.heavy_preg:
        "robin_outfit_baggy_preg2"
    elif robin.showing:
        "robin_outfit_baggy_preg1"
    if t.month in ("Winter", "Autumn"):
        "robin_outfit_baggy_winter_layer"

    if loc_cur.outside and weather_var in (1,3,4):
        "robin_head_shad_hat"
    else:
        "robin_head_shad_hair"

    if loc_cur.outside and weather_var in (1,3,4):
        "robin_hat"
    else:
        "robin_hair"

layeredimage robin_outfit_hoodiebody_layer:
    if robin.heavy_preg:
        "robin_outfit_hoodiebody_preg2"
    elif robin.showing:
        "robin_outfit_hoodiebody_preg1"
    else:
        "robin_outfit_hoodiebody"

layeredimage robin_outfit_hoodie_layer:
    if t.month in ("Winter", "Autumn"):
        "robin_outfit_hoodieneck"
    if loc_cur.outside and weather_var in (3,4):
        "robin_outfit_hoodieup"
    else:
        "robin_outfit_hoodiedown"
    if robin.heavy_preg:
        "robin_outfit_hoodie_preg2"
    elif robin.showing:
        "robin_outfit_hoodie_preg1"
    if t.month in ("Winter", "Autumn"):
        "robin_outfit_hoodiebody_layer"
    if weather_var == 1 and loc_cur.outside:
        "robin_head_shad_hat"
    elif not (loc_cur.outside and weather_var in (3,4)):
        "robin_head_shad_hair"
    if weather_var == 1 and loc_cur.outside:
        "robin_hat"
    elif not (loc_cur.outside and weather_var in (3,4)):
        "robin_hair"

layeredimage robin_outfit_pyjamas_layer:
    always "robin_outfit_pyjamas"
    if robin.heavy_preg:
        "robin_outfit_pyjamas_preg2"
    elif robin.showing:
        "robin_outfit_pyjamas_preg1"
    always "robin_head_shad_hair"
    always "robin_hair"

layeredimage robin_outfit_swim_layer:
    always "robin_outfit_swim"
    if robin.heavy_preg:
        "robin_outfit_swim_preg2"
    elif robin.showing:
        "robin_outfit_swim_preg1"
    always "robin_head_shad_hair"
    always "robin_hair"

layeredimage robin_outfit_slut_layer:
    always "robin_outfit_nude"
    always "robin_outfit_thong_layer"
    if robin.heavy_preg:
        "robin_outfit_slut_preg2"
    elif robin.showing:
        "robin_outfit_slut_preg1"
    else:
        "robin_outfit_slut"
    always "robin_head_shad_hair"
    if not robin.isslut:
        "robin_hair_pink"
    else:
        "robin_hair"

layeredimage robin_outfit_bimbo_layer:
    always "robin_outfit_nude"
    always "robin_outfit_thong_layer"
    if robin.heavy_preg:
        "robin_outfit_bimbo_preg2"
    elif robin.showing:
        "robin_outfit_bimbo_preg1"
    else:
        "robin_outfit_bimbo"
    always "robin_head_shad_hair"
    if not robin.isslut:
        "robin_hair_pink"
    else:
        "robin_hair"

layeredimage robin_outfit_bimbo_nomakeup_layer:
    always "robin_outfit_nude"
    always "robin_outfit_thong_layer"
    always "robin_outfit_bimbo"
    if robin.heavy_preg:
        "robin_outfit_bimbo_preg2"
    elif robin.showing:
        "robin_outfit_bimbo_preg1"
    always "robin_head_shad_hair"
    always "robin_hair"

layeredimage robin_outfit_thong_layer:
    always "robin_outfit_nude"
    if robin.heavy_preg:
        "robin_outfit_thong_preg2"
    elif robin.showing:
        "robin_outfit_thong_preg1"
    else:
        "robin_outfit_thong"
    always "robin_head_shad_hair"
    always "robin_hair"


layeredimage robin_outfit_thongm_layer:
    always "robin_outfit_nude"
    if robin.heavy_preg:
        "robin_outfit_thong_preg2"
    elif robin.showing:
        "robin_outfit_thong_preg1"
    else:
        "robin_outfit_thong"
    always "robin_head_shad_hair"
    always "robin_hair_pink"

layeredimage robin_outfit_outing_layer:
    if robin.dict["robin_talk_sexobject_outing_clothes"] == "slut":
        "robin_outfit_slut_layer"
    else:
        "robin_outfit_bimbo_layer"

layeredimage robin_outfit_mess_layer:
    always "robin_outfit_nude"
    always "robin_head_shad_hairmess"
    always "robin_hair_mess" anchor (0.0, 0.025)
layeredimage robin_outfit_mess_hair_layer:
    always "robin_hair_mess" anchor (0.0, 0.025)

layeredimage robin_outfit_bunny_layer:
    always "robin_outfit_bunny"
    if robin.heavy_preg:
        "robin_outfit_bunny_preg2"
    elif robin.showing:
        "robin_outfit_bunny_preg1"
    always "robin_head_shad_hairc"
    always "robin_hair_combed"


layeredimage robin_outfit_standard:
    if "nude_vball" in loc_beach_hangout.list and t.hour in (21,22,23,0,1,2) and robin_here(loc_beach_gym):
        "robin_outfit_nude_layer"
    elif "slut_outing" in robin.list:
        "robin_outfit_outing_layer"
    elif (robin_here(loc_school_field_back) and not t.timeofday == "day" and "naked_for_boys" in robin.list):
        "robin_outfit_nude_layer"
    elif robin_here(loc_park):
        "robin_outfit_mess_layer"
    elif robin_here(dis_beach.locs):
        "robin_outfit_swim_layer"
    elif robin_here(loc_school_field):
        "robin_outfit_sport_layer"
    elif t.wkday in weekdays and t.hour in school_hours:
        "robin_outfit_uni_layer"
    elif robin_here(dis_home.locs) and (t.timeofday == "night" or t.hour in (6,7)) and dis(dis_home):
        "robin_outfit_pyjamas_layer" 
    elif (global_random_number % 2): 
        "robin_outfit_baggy_layer"
    else:
        "robin_outfit_hoodie_layer"

layeredimage robin_face_neutral_layered:
    if robin.drunk > 50:
        "robin_face_drunk"
    else:
        "robin_face_neutral"
layeredimage robin_face_neutral_pink_layered:
    if robin.drunk > 50:
        "robin_lipstick_drunk_pink"
    else:
        "robin_lipstick_neutral_pink"
layeredimage robin_face_neutral_red_layered:
    if robin.drunk > 50:
        "robin_lipstick_drunk_red"
    else:
        "robin_lipstick_neutral_red"

layeredimage robin_face_angry_layered:
    if robin.drunk > 50:
        "robin_face_drunk"
    else:
        "robin_face_angry"
layeredimage robin_face_angry_pink_layered:
    if robin.drunk > 50:
        "robin_lipstick_drunk_pink"
    else:
        "robin_lipstick_angry_pink"
layeredimage robin_face_angry_red_layered:
    if robin.drunk > 50:
        "robin_lipstick_drunk_red"
    else:
        "robin_lipstick_angry_red"

layeredimage robin_face_worried_layered:
    if robin.drunk > 50:
        "robin_face_drunk"
    else:
        "robin_face_worried"
layeredimage robin_face_worried_pink_layered:
    if robin.drunk > 50:
        "robin_lipstick_drunk_pink"
    else:
        "robin_lipstick_worried_pink"
layeredimage robin_face_worried_red_layered:
    if robin.drunk > 50:
        "robin_lipstick_drunk_red"
    else:
        "robin_lipstick_worried_red"

layeredimage robin_face_happy_layered:
    if robin.drunk > 50:
        "robin_face_drunk"
    else:
        "robin_face_happy"
layeredimage robin_face_happy_pink_layered:
    if robin.drunk > 50:
        "robin_lipstick_drunk_pink"
    else:
        "robin_lipstick_happy_pink"
layeredimage robin_face_happy_red_layered:
    if robin.drunk > 50:
        "robin_lipstick_drunk_red"
    else:
        "robin_lipstick_happy_red"

layeredimage robin:
    at sprite_highlight("robin") 

    group body:
        attribute arm_up "robin_base_layer" default
        attribute cuffed "robin_base_cuffed_layer"

    group collar:
        attribute no_collar null default
        attribute bitch "robin_bitchcollar"

    group cum:
        attribute no_cum null default
        attribute park_cum "robin_parkcum"
        attribute cum "robin_cum"

    group outfit:
        attribute standard default:
            "robin_outfit_standard"
        attribute uni:
            "robin_outfit_uni_layer"
        attribute hoodie:
            "robin_outfit_hoodie_layer"
        attribute baggy:
            "robin_outfit_baggy_layer"
        attribute sport:
            "robin_outfit_sport_layer"
        attribute swim:
            "robin_outfit_swim_layer"
        attribute pyjamas:
            "robin_outfit_pyjamas_layer"
        attribute bimbo:
            "robin_outfit_bimbo_layer"
        attribute bimbo_nomakeup:
            "robin_outfit_bimbo_nomakeup_layer"
        attribute slut:
            "robin_outfit_slut_layer"
        attribute outing:
            "robin_outfit_outing_layer"
        attribute thong:
            "robin_outfit_thong_layer"
        attribute thongm:
            "robin_outfit_thongm_layer"
        attribute bunny:
            "robin_outfit_bunny_layer"
        attribute nude:
            "robin_outfit_nude_layer"
        attribute mess:
            "robin_outfit_mess_layer"
        attribute nude_makeup:
            "robin_outfit_nude_makeup_layer"

    always:
        if_any ["bimbo", "slut", "thongm", "nude_makeup"] "robin_makeup"
    always:
        if_any ["bunny",] "robin_makeupcas"
    group face:
        attribute neutral if_any ["bimbo", "slut", "thongm", "nude_makeup"] "robin_face_neutral_pink_layered"
        attribute neutral if_any ["bunny"] "robin_face_neutral_red_layered"
        attribute neutral "robin_face_neutral_layered" default

        attribute happy if_any ["bimbo", "slut", "thongm", "nude_makeup"] "robin_face_happy_pink_layered"
        attribute happy if_any ["bunny"] "robin_face_happy_red_layered"
        attribute happy "robin_face_happy_layered"

        attribute angry if_any ["bimbo", "slut", "thongm", "nude_makeup"] "robin_face_angry_pink_layered"
        attribute angry if_any ["bunny"] "robin_face_angry_red_layered"
        attribute angry "robin_face_angry_layered"

        attribute worried if_any ["bimbo", "slut", "thongm", "nude_makeup"] "robin_face_worried_pink_layered"
        attribute worried if_any ["bunny"] "robin_face_worried_red_layered"
        attribute worried "robin_face_worried_layered"

        attribute gagged "robin_face_worried_layered"
        attribute gagged "robin_gag"

    group outfit:
        attribute mess:
            "robin_outfit_mess_hair_layer"

layeredimage robin_cuffed:
    at sprite_highlight("robin") 

    always "robin_base_cuffed_layer"
    always "robin_parkcum"

    group collar:
        attribute no_collar null default
        attribute bitch "robin_bitchcollar"
    group face:
        attribute neutral "robin_face_neutral" default
        attribute happy "robin_face_happy"
        attribute angry "robin_face_angry"
        attribute worried "robin_face_worried"

        attribute gagged "robin_face_worried"
        attribute gagged "robin_gag"

    always "robin_outfit_mess_hair_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
