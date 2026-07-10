image sb_beach_lay_bg_layer:
    "sb_beach_lay_bg_" + loc_cur.loc_type

image sb_beach_lay_pc_body_base_layer:
    "sb_beach_lay_pc_body_base"
    skin_base_colour_transform()
image sb_beach_lay_pc_body_shad_layer:
    "sb_beach_lay_pc_body_shad"
    skin_shad_colour_transform()
image sb_beach_lay_pc_body_vag_layer:
    "sb_beach_lay_pc_body_vag"
    vagina_colour_transform()

image sb_beach_lay_pc_writing_ass_layer:
    "sb_beach_lay_pc_writing_ass"
    writing_transform("ass")
image sb_beach_lay_pc_writing_anus_layer:
    "sb_beach_lay_pc_writing_anus"
    writing_transform("anus")
image sb_beach_lay_pc_spank_layer:
    "sb_beach_lay_pc_spank"
    opacity_transform(bruise.ass)

image sb_beach_lay_pc_clothing_top_knot_layer:
    "sb_beach_lay_pc_clothing_top_knot"
    top_primary_colour_transform()
image sb_beach_lay_pc_clothing_top_tri_layer:
    "sb_beach_lay_pc_clothing_top_tri"
    top_secondary_colour_transform()

image sb_beach_lay_pc_clothing_bottom_knot_layer:
    "sb_beach_lay_pc_clothing_bottom_knot"
    bottom_primary_colour_transform()
image sb_beach_lay_pc_clothing_bottom_tri_base_layer:
    "sb_beach_lay_pc_clothing_bottom_tri_base"
    bottom_primary_colour_transform()
    clothing_alpha_transform("sb_beach_lay_pc_clothing_bottom_tri_base", "bottom")
image sb_beach_lay_pc_clothing_bottom_tri_trim_layer:
    "sb_beach_lay_pc_clothing_bottom_tri_trim"
    bottom_secondary_colour_transform()

image sb_beach_lay_pc_clothing_outfit_sch_layer:
    "sb_beach_lay_pc_clothing_outfit_sch"
    outfit_primary_colour_transform()
    clothing_alpha_transform("sb_beach_lay_pc_clothing_outfit_sch", "outfit")
image sb_beach_lay_pc_clothing_outfit_comp_layer:
    "sb_beach_lay_pc_clothing_outfit_comp"
    outfit_primary_colour_transform()

image sb_beach_lay_pc_hair_back_pony_2 = "sb_beach_lay_pc_hair_back_bun"
image sb_beach_lay_pc_hair_back_pony_3 = "sb_beach_lay_pc_hair_back_bun"
image sb_beach_lay_pc_hair_back_pony_4 = "sb_beach_lay_pc_hair_back_bun"
image sb_beach_lay_pc_hair_back_bun_2 = "sb_beach_lay_pc_hair_back_bun"
image sb_beach_lay_pc_hair_back_bun_3 = "sb_beach_lay_pc_hair_back_bun"
image sb_beach_lay_pc_hair_back_bun_4 = "sb_beach_lay_pc_hair_back_bun"

image sb_beach_lay_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_beach_lay_pc_hair_back")
    hair_colour_transform()
image sb_beach_lay_pc_hair_front_layer:
    "sb_beach_lay_pc_hair_front"
    hair_colour_transform()

image activity_beach_lay = LayeredImageProxy("activity_beach_lay_layer", Transform(align=(0.7, 0.0)))

layeredimage activity_beach_lay_layer:

    always "sb_beach_lay_bg_layer"

    group people:
        attribute alone default null
        attribute emile "sb_beach_lay_person_emile"
        attribute emile "sb_beach_lay_person_emile_swim"

        attribute emile_nude "sb_beach_lay_person_emile"

        attribute kaan "sb_beach_lay_person_kaan"

    always "sb_beach_lay_pc_body_base_layer"
    always "sb_beach_lay_pc_body_shad_layer"
    always "sb_beach_lay_pc_body_vag_layer"
    always "sb_beach_lay_pc_spank_layer"
    if writing.ass:
        "sb_beach_lay_pc_writing_ass_layer"
    if writing.anus:
        "sb_beach_lay_pc_writing_anus_layer"
    if acc.anus:
        "sb_beach_lay_pc_plug"
    if c.top == 1:
        "sb_beach_lay_pc_clothing_top_tri_layer"
    elif c.top == 2:
        "sb_beach_lay_pc_clothing_top_knot_layer"
    elif c.top == 3:
        "sb_beach_lay_pc_clothing_top_string"

    if c.bottom == 1:
        "sb_beach_lay_pc_clothing_bottom_tri_base_layer"
    elif c.bottom == 2:
        "sb_beach_lay_pc_clothing_bottom_knot_layer"
    elif c.bottom == 3:
        "sb_beach_lay_pc_clothing_bottom_string"
    if c.bottom == 1:
        "sb_beach_lay_pc_clothing_bottom_tri_trim_layer"

    if c.outfit == 2:
        "sb_beach_lay_pc_clothing_outfit_sch_layer"
    elif c.outfit == 5:
        "sb_beach_lay_pc_clothing_outfit_comp_layer"

    always "sb_beach_lay_pc_hair_front_layer"
    always "sb_beach_lay_pc_hair_back_layer"

    always "sb_beach_lay_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
