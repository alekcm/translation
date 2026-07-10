image sb_pose_upskirt_bg_room = "sb_pose_upskirt_bg_plaster"
image sb_pose_upskirt_bg_layer:
    "sb_pose_upskirt_bg_" + loc_cur.loc_type

image sb_pose_upskirt_pc_body_base_layer:
    get_skin_filename("sb_pose_upskirt_pc_body_base")
    skin_base_colour_transform()
image sb_pose_upskirt_pc_body_shad_layer:
    get_skin_filename("sb_pose_upskirt_pc_body_shad")
    skin_shad_colour_transform()
image sb_pose_upskirt_pc_body_skirtshad_layer:
    get_skin_filename("sb_pose_upskirt_pc_body_skirtshad")
    skin_shad_colour_transform()
image sb_pose_upskirt_pc_breasts_base_layer:
    get_skin_filename("sb_pose_upskirt_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_pose_upskirt_pc_breasts_shad_layer:
    get_skin_filename("sb_pose_upskirt_pc_breasts_shad", breasts=True)
    skin_base_colour_transform()
image sb_pose_upskirt_pc_belly_layer:
    get_skin_filename("sb_pose_upskirt_pc_belly")
    skin_base_colour_transform()


image sb_pose_upskirt_pc_bar_dress_breasts_layer:
    get_skin_filename("sb_pose_upskirt_pc_bar_dress_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_pose_upskirt_pc_bar_dress_breasts_col_layer:
    get_skin_filename("sb_pose_upskirt_pc_bar_dress_breasts_shad", breasts=True)


image sb_pose_upskirt_pc_dance_knot_breasts_layer:
    get_skin_filename("sb_pose_upskirt_pc_dance_knot_breasts", breasts=True)
image sb_pose_upskirt_pc_dance_crop_breasts_layer:
    get_skin_filename("sb_pose_upskirt_pc_dance_crop_breasts", breasts=True)

image sb_pose_upskirt_spank_layer:
    "sb_pose_upskirt_spank"
    opacity_transform(bruise.ass)

image sb_pose_upskirt_writing_ass_layer:
    "sb_pose_upskirt_writing_ass"
    writing_transform("ass")
image sb_pose_upskirt_writing_anus_layer:
    "sb_pose_upskirt_writing_anus"
    writing_transform("anus")

layeredimage sb_pose_upskirt:

    always "sb_pose_upskirt_bg_layer"

    always "sb_pose_upskirt_pc_body_base_layer"
    if c.skirt:
        "sb_pose_upskirt_pc_body_skirtshad_layer"
    always "sb_pose_upskirt_pc_body_shad_layer"
    if player.pregnancy >= 2:
        "sb_pose_upskirt_pc_belly_layer"
    always "sb_pose_upskirt_spank_layer"
    always "sb_pose_upskirt_pc_breasts_base_layer"
    always "sb_pose_upskirt_pc_breasts_shad_layer"

    if acc.anus:
        "sb_pose_upskirt_pc_plug"

    if c.pants == 3:
        "sb_pose_upskirt_pc_dance_pants"
    if c.pants == 5:
        "sb_pose_upskirt_pc_dance_thong"
    if c.pants == 6:
        "sb_pose_upskirt_pc_bar_pants"

    if c.socks == 1:
        "sb_pose_upskirt_pc_dance_socks"
    if c.socks == 7:
        "sb_pose_upskirt_pc_bar_socks"


    if writing.ass:
        "sb_pose_upskirt_writing_ass_layer"
    if writing.anus:
        "sb_pose_upskirt_writing_anus_layer"


    if c.outfit == 6:
        "sb_pose_upskirt_pc_pub_dress_layered"
    if c.top == 19:
        "sb_pose_upskirt_pc_dance_crop_breasts_layer"
    if c.top == 20:
        "sb_pose_upskirt_pc_dance_knot_layered"
    if c.bottom == 13:
        "sb_pose_upskirt_pc_dance_skirt"
    always "sb_pose_upskirt_frame"

layeredimage sb_pose_upskirt_pc_pub_dress_layered:
    always "sb_pose_upskirt_pc_bar_dress_base"
    always "sb_pose_upskirt_pc_bar_dress_breasts_col_layer"
    if player.pregnancy >= 2:
        "sb_pose_upskirt_pc_bar_dress_belly"
layeredimage sb_pose_upskirt_pc_dance_knot_layered:
    always "sb_pose_upskirt_pc_dance_knot_breasts_layer"
    if player.pregnancy >= 2:
        "sb_pose_upskirt_pc_dance_knot_2"
    else:
        "sb_pose_upskirt_pc_dance_knot_0"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
