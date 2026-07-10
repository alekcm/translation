image sb_pose_checkvag_bg_layer:
    "sb_pose_checkvag_bg"
    desire_colour_transform()

image sb_pose_checkvag_body_base_layer:
    get_skin_filename("sb_pose_checkvag_body_base", False)
    skin_base_colour_transform()
image sb_pose_checkvag_body_shad_layer:
    get_skin_filename("sb_pose_checkvag_body_shad", False)
    skin_shad_colour_transform()
image sb_pose_checkvag_body_vag_layer:
    get_skin_filename("sb_pose_checkvag_body_vag", False)
    vagina_colour_transform()
image sb_pose_checkvag_body_phair_layer:
    get_cg_filename("sb_pose_checkvag_body_phair", False)
    phair_colour_transform()

image sb_pose_checkvag_belly_base_layer:
    get_skin_filename("sb_pose_checkvag_belly_base", True)
    skin_base_colour_transform()
image sb_pose_checkvag_belly_shad_layer:
    get_skin_filename("sb_pose_checkvag_belly_shad", True)
    skin_shad_colour_transform()
image sb_pose_checkvag_belly_nip_layer:
    get_skin_filename("sb_pose_checkvag_belly_nip", True)
    nipple_colour_transform()
image sb_pose_checkvag_belly_tat_breast_layer:
    get_skin_filename("sb_pose_checkvag_belly_tat_breast", True)
image sb_pose_checkvag_belly_nipring_layer:
    get_skin_filename("sb_pose_checkvag_belly_nipring", True)
    accessories_secondary_colour_transform("nipring")
image sb_pose_checkvag_belly_navring_layer:
    get_skin_filename("sb_pose_checkvag_belly_navring", True)
    accessories_secondary_colour_transform("navelring")

image sb_pose_checkvag_writing_belly_layer:
    get_skin_filename("sb_pose_checkvag_writing_belly", True)

image sb_pose_checkvag_shower_rain_loop:
    "sb_pose_checkvag_shower_rain1"
    .03
    "sb_pose_checkvag_shower_rain2"
    .03
    "sb_pose_checkvag_shower_rain3"
    .03
    repeat

layeredimage sb_pose_checkvag:

    group bg:
        attribute nobg default:
            "sb_pose_checkvag_bg_layer"
        attribute shower:
            "sb_pose_checkvag_bg_shower"

    always:
        "sb_pose_checkvag_body_base_layer"
    always:
        "sb_pose_checkvag_body_shad_layer"
    always:
        "sb_pose_checkvag_body_vag_layer"


    always:
        "sb_pose_checkvag_belly_base_layer"
    always:
        "sb_pose_checkvag_belly_shad_layer"
    always:
        "sb_pose_checkvag_belly_nip_layer"
    if acc.nipring:
        "sb_pose_checkvag_belly_nipring_layer"
    if acc.navelring:
        "sb_pose_checkvag_belly_navring_layer"
    if tattoo.chest == 1:
        "sb_pose_checkvag_belly_tat_breast_layer"
    if player.phair == 1:
        "sb_pose_checkvag_body_phair_layer"
    if player.cum_locations["cum_vagin"] or player.cum_locations["cum_vagout"]:
        "sb_pose_checkvag_cum_vag"
    if writing.belly:
        "sb_pose_checkvag_writing_belly_layer"
    if writing.pubic:
        "sb_pose_checkvag_writing_pubic"

    group bg:
        attribute no_shower default:
            null
        attribute shower:
            "sb_pose_checkvag_shower_rain_loop"
        attribute shower:
            "sb_pose_checkvag_shower_steam"
    always:
        "sb_pose_checkvag_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
