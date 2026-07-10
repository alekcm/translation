image showerf_body_phair_layer:
    get_skin_filename("showerf_body_phair")
    phair_colour_transform()

image showerf_body_breasts_nips_layer:
    get_skin_filename("showerf_body_breasts_nips", breasts=True)
    nipple_colour_transform()
image showerf_body_breasts_nipring_layer:
    get_skin_filename("showerf_body_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image showerf_body_breasts_base_layer:
    get_skin_filename("showerf_body_breasts_base", breasts=True)
    skin_base_colour_transform()
image showerf_body_breasts_shad_layer:
    get_skin_filename("showerf_body_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image showerf_body_breasts_tat_layer:
    get_skin_filename("showerf_body_breasts_tat", breasts=True)

image showerf_body_belly_base_layer:
    get_skin_filename("showerf_body_belly_base", preg=True)
    skin_base_colour_transform()
image showerf_body_belly_shad_layer:
    get_skin_filename("showerf_body_belly_shad", preg=True)
    skin_shad_colour_transform()
image showerf_body_navring_layer:
    get_skin_filename("showerf_body_navring", preg=True)
    accessories_secondary_colour_transform("navelring")

image showerf_body_base_layer:
    get_skin_filename("showerf_body_base")
    skin_base_colour_transform()
image showerf_body_shad_layer:
    get_skin_filename("showerf_body_shad")
    skin_shad_colour_transform()

image showerf_larm_wash_base_layer:
    get_skin_filename("showerf_larm_wash_base")
    skin_base_colour_transform()
image showerf_larm_wash_shad_layer:
    get_skin_filename("showerf_larm_wash_shad")
    skin_shad_colour_transform()
image showerf_larm_up_base_layer:
    get_skin_filename("showerf_larm_up_base")
    skin_base_colour_transform()
image showerf_larm_up_shad_layer:
    get_skin_filename("showerf_larm_up_shad")
    skin_shad_colour_transform()

image showerf_rarm_wash_base_layer:
    get_skin_filename("showerf_rarm_wash_base")
    skin_base_colour_transform()
image showerf_rarm_wash_shad_layer:
    get_skin_filename("showerf_rarm_wash_shad")
    skin_shad_colour_transform()
image showerf_rarm_up_base_layer:
    get_skin_filename("showerf_rarm_up_base")
    skin_base_colour_transform()
image showerf_rarm_up_shad_layer:
    get_skin_filename("showerf_rarm_up_shad")
    skin_shad_colour_transform()

image showerf_manbehind_grope_base_layer:
    get_skin_filename("showerf_manbehind_grope_base", True)
    npc_skin_base_colour_transform()
image showerf_manbehind_grope_shad_layer:
    get_skin_filename("showerf_manbehind_grope_shad", True)
    npc_skin_shad_colour_transform()

image showerf_manbehind_hold_base_layer:
    get_skin_filename("showerf_manbehind_hold_base")
    npc_skin_base_colour_transform()
image showerf_manbehind_hold_shad_layer:
    get_skin_filename("showerf_manbehind_hold_shad")
    npc_skin_shad_colour_transform()
image showerf_manbehind_holdhand_base_layer:
    get_skin_filename("showerf_manbehind_holdhand_base", True)
    npc_skin_base_colour_transform()
image showerf_manbehind_holdhand_shad_layer:
    get_skin_filename("showerf_manbehind_holdhand_shad", True)
    npc_skin_shad_colour_transform()



image showerf_manfront_base_layer:
    get_skin_filename("showerf_manfront_base")
    npc2_skin_base_colour_transform()
image showerf_manfront_shad_layer:
    get_skin_filename("showerf_manfront_shad")
    npc2_skin_shad_colour_transform()

image showerf_manfrontgrope_base_layer:
    get_skin_filename("showerf_manfrontgrope_base")
    npc2_skin_base_colour_transform()
image showerf_manfrontgrope_shad_layer:
    get_skin_filename("showerf_manfrontgrope_shad")
    npc2_skin_shad_colour_transform()

image showerf_manfront_arm_base_layer:
    get_skin_filename("showerf_manfront_arm_base")
    npc2_skin_base_colour_transform()
image showerf_manfront_arm_shad_layer:
    get_skin_filename("showerf_manfront_arm_shad")
    npc2_skin_shad_colour_transform()

image showerf_rain_loop:
    "showerf_rain_loop1"
    .03
    "showerf_rain_loop2"
    .03
    "showerf_rain_loop3"
    .03
    repeat

layeredimage shower:

    always:
        "showerf_bg"

    group rarm:
        attribute rarm_pos default if_not ["grope","finger","hold","stand"]:
            "showerf_rarm_wash_base_layer"
        attribute rarm_pos default if_not ["grope","finger","hold","stand"]:
            "showerf_rarm_wash_shad_layer"

        attribute rarm_pos default if_any ["grope","finger","hold","stand"]:
            "showerf_rarm_up_base_layer"
        attribute rarm_pos default if_any ["grope","finger","hold","stand"]:
            "showerf_rarm_up_shad_layer"



    group man_front:
        attribute stand:
            "showerf_manfront_arm_base_layer"
        attribute stand:
            "showerf_manfront_arm_shad_layer"

        attribute finger:
            "showerf_manfront_arm_base_layer"
        attribute finger:
            "showerf_manfront_arm_shad_layer"

    always:
        "showerf_body_base_layer"
    always:
        "showerf_body_shad_layer"

    always:
        "showerf_body_breasts_base_layer"
    always:
        "showerf_body_breasts_shad_layer"
    always:
        "showerf_body_breasts_nips_layer"
    if tattoo.chest == 1:
        "showerf_body_breasts_tat_layer"
    if acc.nipring == 1:
        "showerf_body_breasts_nipring_layer"

    always:
        "showerf_body_belly_base_layer"
    always:
        "showerf_body_belly_shad_layer"
    if acc.navelring == 1:
        "showerf_body_navring_layer"

    if player.phair:
        "showerf_body_phair_layer"

    group man_behind:
        attribute noman_behind default:
            null

        attribute grope:
            "showerf_manbehind_grope_base_layer"
        attribute grope:
            "showerf_manbehind_grope_shad_layer"

        attribute hold:
            "showerf_manbehind_hold_base_layer"
        attribute hold:
            "showerf_manbehind_hold_shad_layer"
        attribute hold:
            "showerf_manbehind_holdhand_base_layer"
        attribute hold:
            "showerf_manbehind_holdhand_shad_layer"

    group man_front:
        attribute noman_front default:
            null

        attribute stand:
            "showerf_manfront_base_layer"
        attribute stand:
            "showerf_manfront_shad_layer"

        attribute finger:
            "showerf_manfront_base_layer"
        attribute finger:
            "showerf_manfront_shad_layer"
        attribute finger:
            "showerf_manfrontgrope_base_layer"
        attribute finger:
            "showerf_manfrontgrope_shad_layer"

    group larm:
        attribute larm_pos default if_not ["grope","finger","hold","stand"]:
            "showerf_larm_wash_base_layer"
        attribute larm_pos default if_not ["grope","finger","hold","stand"]:
            "showerf_larm_wash_shad_layer"

        attribute larm_pos default if_any ["grope","finger","hold","stand"]:
            "showerf_larm_up_base_layer"
        attribute larm_pos default if_any ["grope","finger","hold","stand"]:
            "showerf_larm_up_shad_layer"




    always:
        "showerf_steam"
    always:
        "showerf_rain_loop"
    always:
        "showerf_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
