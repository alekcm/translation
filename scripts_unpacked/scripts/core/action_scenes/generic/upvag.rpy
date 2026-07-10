image sb_pose_upvag_bg_layer:
    "sb_pose_upvag_bg_" + loc_cur.loc_type

image sb_pose_upvag_pc_belly_base_1 = "sb_pose_upvag_pc_belly_base_0"
image sb_pose_upvag_pc_belly_shad_1 = "sb_pose_upvag_pc_belly_shad_0"
image sb_pose_upvag_pc_belly_base_2 = "sb_pose_upvag_pc_belly_base_3"
image sb_pose_upvag_pc_belly_shad_2 = "sb_pose_upvag_pc_belly_shad_3"

image sb_pose_upvag_pc_belly_base_layer:
    get_skin_filename("sb_pose_upvag_pc_belly_base", preg=True)
    skin_base_colour_transform()
image sb_pose_upvag_pc_belly_shad_layer:
    get_skin_filename("sb_pose_upvag_pc_belly_shad", preg=True)
    skin_shad_colour_transform()

image sb_pose_upvag_pc_body_base_layer:
    get_skin_filename("sb_pose_upvag_pc_body_base")
    skin_base_colour_transform()
image sb_pose_upvag_pc_body_shad_layer:
    get_skin_filename("sb_pose_upvag_pc_body_shad")
    skin_shad_colour_transform()

image sb_pose_upvag_pc_hand_mast_base_layer:
    get_skin_filename("sb_pose_upvag_pc_hand_mast_base")
    skin_base_colour_transform()
image sb_pose_upvag_pc_hand_mast_shad_layer:
    get_skin_filename("sb_pose_upvag_pc_hand_mast_shad")
    skin_shad_colour_transform()
image sb_pose_upvag_pc_hand_mast_nails_layer:
    get_skin_filename("sb_pose_upvag_pc_hand_mast_nails")
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_pose_upvag_pc_hand_spread_base_layer:
    get_skin_filename("sb_pose_upvag_pc_hand_spread_base")
    skin_base_colour_transform()
image sb_pose_upvag_pc_hand_spread_shad_layer:
    get_skin_filename("sb_pose_upvag_pc_hand_spread_shad")
    skin_shad_colour_transform()
image sb_pose_upvag_pc_hand_spread_nails_layer:
    get_skin_filename("sb_pose_upvag_pc_hand_spread_nails")
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image sb_pose_upvag_pc_hand_spread_vag_layer:
    get_skin_filename("sb_pose_upvag_pc_hand_spread_vag")
    vagina_colour_transform()

image sb_pose_upvag_pc_clothes_swimwear_2_layer:
    "sb_pose_upvag_pc_clothes_swimwear_2"
    bottom_primary_colour_transform()
image sb_pose_upvag_pc_clothes_swimwear_3_layer:
    "sb_pose_upvag_pc_clothes_swimwear_3"
    bottom_primary_colour_transform()
    clothing_alpha_transform("sb_pose_upvag_pc_clothes_swimwear_3", "bottom")
image sb_pose_upvag_pc_clothes_swimwear_sch_layer:
    "sb_pose_upvag_pc_clothes_swimwear_sch"
    outfit_primary_colour_transform()
    clothing_alpha_transform("sb_pose_upvag_pc_clothes_swimwear_sch", "outfit")
image sb_pose_upvag_pc_clothes_swimwear_comp_layer:
    "sb_pose_upvag_pc_clothes_swimwear_comp"
    outfit_primary_colour_transform()

image sb_pose_upvag_pc_clothes_swimwear_tri_base_layer:
    "sb_pose_upvag_pc_clothes_swimwear_tri_base"
    bottom_primary_colour_transform()
    clothing_alpha_transform("sb_pose_upvag_pc_clothes_swimwear_tri_base", "bottom")
image sb_pose_upvag_pc_clothes_swimwear_tri_trim_layer:
    "sb_pose_upvag_pc_clothes_swimwear_tri_trim"
    bottom_secondary_colour_transform()

image sb_pose_upvag_pc_spank_layer:
    "sb_pose_upvag_pc_spank"
    opacity_transform(bruise.ass)

image sb_pose_upvag_pc_writing_ass_layer:
    "sb_pose_upvag_pc_writing_ass"
    writing_transform("ass")
image sb_pose_upvag_pc_writing_anus_layer:
    "sb_pose_upvag_pc_writing_anus"
    writing_transform("anus")
image sb_pose_upvag_pc_writing_lleg_layer:
    "sb_pose_upvag_pc_writing_lleg"
    writing_transform("lleg")

image sb_pose_upvag_shower_rain:
    "sb_pose_upvag_shower_rain1"
    .03
    "sb_pose_upvag_shower_rain2"
    .03
    "sb_pose_upvag_shower_rain3"
    .03
    repeat

layeredimage sb_pose_upvag:

    always "sb_pose_upvag_bg_layer"

    always "sb_pose_upvag_pc_belly_base_layer"
    always "sb_pose_upvag_pc_belly_shad_layer"

    always "sb_pose_upvag_pc_body_base_layer"
    always "sb_pose_upvag_pc_body_shad_layer"

    always "sb_pose_upvag_pc_spank_layer"

    if acc.anus:
        "sb_pose_upvag_pc_plug" 
    if writing.ass:
        "sb_pose_upvag_pc_writing_ass_layer"
    if writing.anus:
        "sb_pose_upvag_pc_writing_anus_layer"
    if writing.lleg:
        "sb_pose_upvag_pc_writing_lleg_layer"
    if tattoo.ass:
        "sb_pose_upvag_pc_tat_tramp" 
    group hand:
        attribute nohand default:
            null

        attribute mast:
            "sb_pose_upvag_pc_hand_mast_base_layer"
        attribute mast:
            "sb_pose_upvag_pc_hand_mast_shad_layer"
        attribute mast:
            "sb_pose_upvag_pc_hand_mast_nails_layer"
        attribute mast:
            "sb_pose_upvag_pc_hand_mast_juice"

        attribute spread:
            "sb_pose_upvag_pc_hand_spread_base_layer"
        attribute spread:
            "sb_pose_upvag_pc_hand_spread_shad_layer"
        attribute spread:
            "sb_pose_upvag_pc_hand_spread_nails_layer"
        attribute spread:
            "sb_pose_upvag_pc_hand_spread_vag_layer"

    if player.cum_locations["cum_vagin"]:
        if_any "spread" "sb_pose_upvag_pc_cum_vagspread"
    if player.cum_locations["cum_vagin"]:
        if_any "nohand" "sb_pose_upvag_pc_cum_vagclosed"
    if player.cum_locations["cum_assin"]:
        "sb_pose_upvag_pc_cum_anus"

    if c.bottom == 1:
        "sb_pose_upvag_pc_clothes_swimwear_tri_base_layer"
    elif c.bottom == 2:
        "sb_pose_upvag_pc_clothes_swimwear_2_layer"
    elif c.bottom == 3:
        "sb_pose_upvag_pc_clothes_swimwear_3_layer"
    elif c.outfit == 2:
        "sb_pose_upvag_pc_clothes_swimwear_sch_layer"
    elif c.outfit == 5:
        "sb_pose_upvag_pc_clothes_swimwear_comp_layer"
    if c.bottom == 1:
        "sb_pose_upvag_pc_clothes_swimwear_tri_trim_layer"

    group water:
        attribute shower:
            "sb_pose_upvag_shower_rain"
        attribute shower:
            "sb_pose_upvag_shower_steam"

    always:
        "sb_pose_upvag_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
