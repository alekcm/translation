image bg_revel_layer:
    get_background_filename("revel", winter=False, night=True)
    bg_tint_transform()

layeredimage bg_revel:

    always:
        "bg_revel_layer"

layeredimage bg_shop_funwear_assistant:
    always "bg_shop_funwear_people_owner_base"
    if fun_girl.heavy_preg:
        "bg_shop_funwear_people_owner_preg2"
    elif fun_girl.showing:
        "bg_shop_funwear_people_owner_preg1"

layeredimage bg_shop_funwear:
    always "bg_shop_funwear_scene"
    if not renpy.showing("fun_girl"):
        "bg_shop_funwear_assistant"
    if girl_dummy_4.hour_number > 4:
        "bg_shop_funwear_people_ass"
    if girl_dummy_2.hour_number < 7:
        "bg_shop_funwear_people_look"

layeredimage bg_shop_tattoo:
    always "bg_shop_tattoo_scene"
    if girl_dummy_4.hour_number < 4 and not renpy.showing("salongirl"):
        "bg_shop_tattoo_people_cut_ass"
    elif girl_dummy_4.hour_number == 5 and not renpy.showing("salongirl"):
        "bg_shop_tattoo_people_tat_ass"
    elif not renpy.showing("salongirl"):
        "bg_shop_tattoo_people_ass_stand"

    if girl_dummy_4.hour_number < 4:
        "bg_shop_tattoo_people_cut_cust" 
    elif girl_dummy_4.hour_number == 5:
        "bg_shop_tattoo_people_tat_cust"



image bg_pub_toilet_girls = "bg_trainstation_local_pub_toilet_girls"
image bg_pub_toilet_boys = "bg_trainstation_local_pub_toilet_boys"

image bg_hospital_entrance:
    get_background_filename("hospital_exterior")
    bg_tint_transform()

image bg_hospital_lobby = "bg_hospital_waiting"
image bg_hospital_office = "bg_hospital_meetingroom"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
