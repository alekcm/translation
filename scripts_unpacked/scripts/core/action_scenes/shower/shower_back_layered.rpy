image showerback_body_base_layer:
    get_skin_filename("showerback_body_base", preg=True)
    skin_base_colour_transform()
image showerback_body_shad_layer:
    get_skin_filename("showerback_body_shad", preg=True)
    skin_shad_colour_transform()

image showerback_breasts_base_layer:
    get_skin_filename("showerback_breasts_base", breasts=True)
    skin_base_colour_transform()
image showerback_breasts_shad_layer:
    get_skin_filename("showerback_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image showerback_breasts_nips_layer:
    get_skin_filename("showerback_breasts_nips", breasts=True)
    nipple_colour_transform()
image showerback_breasts_nipring_layer:
    get_skin_filename("showerback_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image showerback_main_base_layer:
    get_skin_filename("showerback_main_base")
    skin_base_colour_transform()
image showerback_main_shad_layer:
    get_skin_filename("showerback_main_shad")
    skin_shad_colour_transform()

image showerback_larm_wash_base_layer:
    get_skin_filename("showerback_larm_wash_base")
    skin_base_colour_transform()
image showerback_larm_wash_shad_layer:
    get_skin_filename("showerback_larm_wash_shad")
    skin_shad_colour_transform()
image showerback_larm_washman_base_layer:
    get_skin_filename("showerback_larm_washman_base")
    skin_base_colour_transform()
image showerback_larm_washman_shad_layer:
    get_skin_filename("showerback_larm_washman_shad")
    skin_shad_colour_transform()

image showerback_rarm_wash_base_layer:
    get_skin_filename("showerback_rarm_wash_base")
    skin_base_colour_transform()
image showerback_rarm_wash_shad_layer:
    get_skin_filename("showerback_rarm_wash_shad")
    skin_shad_colour_transform()
image showerback_rarm_washman_base_layer:
    get_skin_filename("showerback_rarm_washman_base")
    skin_base_colour_transform()
image showerback_rarm_washman_shad_layer:
    get_skin_filename("showerback_rarm_washman_shad")
    skin_shad_colour_transform()
image showerback_rarm_down_base_layer:
    get_skin_filename("showerback_rarm_down_base")
    skin_base_colour_transform()
image showerback_rarm_down_shad_layer:
    get_skin_filename("showerback_rarm_down_shad")
    skin_shad_colour_transform()


image showerback_manbehind_body_base_layer:
    "showerback_manbehind_body_base"
    npc_skin_base_colour_transform()
image showerback_manbehind_body_shad_layer:
    "showerback_manbehind_body_shad"
    npc_skin_shad_colour_transform()

image showerback_manbehind_grope_base_1 = "showerback_manbehind_grope_base_0"
image showerback_manbehind_grope_shad_1 = "showerback_manbehind_grope_shad_0"
image showerback_manbehind_grope_base_layer:
    get_skin_filename("showerback_manbehind_grope_base", preg=True)
    npc_skin_base_colour_transform()
image showerback_manbehind_grope_shad_layer:
    get_skin_filename("showerback_manbehind_grope_shad", preg=True)
    npc_skin_shad_colour_transform()

image showerback_manbehind_hold_base_layer:
    get_skin_filename("showerback_manbehind_hold_base")
    npc_skin_base_colour_transform()
image showerback_manbehind_hold_shad_layer:
    get_skin_filename("showerback_manbehind_hold_shad")
    npc_skin_shad_colour_transform()

image showerback_manbehind_penis_base_layer:
    get_skin_filename("showerback_manbehind_penis_base")
    npc_skin_base_colour_transform()
image showerback_manbehind_penis_shad_layer:
    get_skin_filename("showerback_manbehind_penis_shad")
    npc_skin_shad_colour_transform()

image showerback_manfront_body_base_layer:
    get_skin_filename("showerback_manfront_body_base")
    npc2_skin_base_colour_transform()
image showerback_manfront_body_shad_layer:
    get_skin_filename("showerback_manfront_body_shad")
    npc2_skin_shad_colour_transform()
image showerback_manfront_hand_base_layer:
    get_skin_filename("showerback_manfront_hand_base")
    npc2_skin_base_colour_transform()
image showerback_manfront_hand_shad_layer:
    get_skin_filename("showerback_manfront_hand_shad")
    npc2_skin_shad_colour_transform()

image showerback_rain_loop:
    "showerback_rain_loop1"
    .03
    "showerback_rain_loop2"
    .03
    "showerback_rain_loop3"
    .03
    repeat

layeredimage shower_back:

    always:
        "showerback_bg"

    group man_front_group:
        attribute noman_front default:
            null

        attribute man_front:
            "showerback_manfront_body_base_layer"
        attribute man_front:
            "showerback_manfront_body_shad_layer"

    group larm:
        attribute washman_left default if_any ["grope", "hold", "man_front"]:
            "showerback_larm_washman_base_layer"
        attribute washman_left default if_any ["grope", "hold", "man_front"]:
            "showerback_larm_washman_shad_layer"



    always:
        "showerback_breasts_base_layer"
    always:
        "showerback_breasts_shad_layer"

    always:
        "showerback_body_base_layer"
    always:
        "showerback_body_shad_layer"

    always:
        "showerback_main_base_layer"
    always:
        "showerback_main_shad_layer"


    always:
        "showerback_breasts_nips_layer"
    if acc.nipring == 1:
        "showerback_breasts_nipring_layer"
    if tattoo.ass == 1:
        "showerback_tat_ass"

    group man_front_group:
        attribute man_front:
            "showerback_manfront_hand_base_layer"
        attribute man_front:
            "showerback_manfront_hand_shad_layer"

    group larm:
        attribute washself_left default if_not ["grope", "hold", "man_front"]:
            "showerback_larm_wash_base_layer"
        attribute washself_left default if_not ["grope", "hold", "man_front"]:
            "showerback_larm_wash_shad_layer"

    group man_behind_penis:
        attribute nopenis default:
            null
        attribute noman_behind:
            null

        attribute penis:
            "showerback_manbehind_penis_base_layer"
        attribute penis:
            "showerback_manbehind_penis_shad_layer"

    group man_behind:
        attribute noman_behind default:
            null

        attribute grope:
            "showerback_manbehind_body_base_layer"
        attribute grope:
            "showerback_manbehind_body_shad_layer"
        attribute grope:
            "showerback_manbehind_grope_base_layer"
        attribute grope:
            "showerback_manbehind_grope_shad_layer"

        attribute hold:
            "showerback_manbehind_body_base_layer"
        attribute hold:
            "showerback_manbehind_body_shad_layer"
        attribute hold:
            "showerback_manbehind_hold_base_layer"
        attribute hold:
            "showerback_manbehind_hold_shad_layer"





    group rarm:
        attribute rarm_pos default if_all ["noman_behind","noman_front"]:
            "showerback_rarm_wash_base_layer"
        attribute rarm_pos default if_all ["noman_behind","noman_front"]:
            "showerback_rarm_wash_shad_layer"

        attribute rarm_pos default if_any ["grope","hold"]:
            "showerback_rarm_down_base_layer"
        attribute rarm_pos default if_any ["grope","hold"]:
            "showerback_rarm_down_shad_layer"

        attribute rarm_pos default if_any "man_front":
            "showerback_rarm_washman_base_layer"
        attribute rarm_pos default if_any "man_front":
            "showerback_rarm_washman_shad_layer"


    always:
        "showerback_steam"
    always:
        "showerback_rain_loop"
    always:
        "showerback_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
