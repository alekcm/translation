image dance_behind_pc_body_base_layer:
    "dance_behind_pc_body_base"
    skin_base_colour_transform()
image dance_behind_pc_body_shad_layer:
    "dance_behind_pc_body_shad"
    skin_shad_colour_transform()

image dance_behind_pc_body_spank_layer:
    "dance_behind_pc_body_spank"
    opacity_transform(bruise.ass)
image dance_behind_pc_writing_ass_layer:
    "dance_behind_pc_writing_ass"
    writing_transform("ass")
image dance_behind_pc_writing_anus_layer:
    "dance_behind_pc_writing_anus"
    writing_transform("anus")

image dance_behind_pc_breasts_base_layer:
    get_skin_filename("dance_behind_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image dance_behind_pc_breasts_shad_layer:
    get_skin_filename("dance_behind_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image dance_behind_pc_breasts_nips_layer:
    get_skin_filename("dance_behind_pc_breasts_nips", breasts=True)
    nipple_colour_transform()

image dance_behind_pc_clothes_crop:
    get_skin_filename("dance_behind_pc_clothes_crop", breasts=True)

image dance_behind = LayeredImageProxy("dance_behind_layered", Transform(xalign = (0.7)))

layeredimage dance_behind_layered:

    if loc(loc_park):
        "dance_behind_bg_park"
    else:
        "dance_behind_bg_gym"

    if not c.top == 20:
        "dance_behind_breasts"

    always "dance_behind_pc_body_base_layer"
    always "dance_behind_pc_body_shad_layer"
    always "dance_behind_pc_body_col"
    always "dance_behind_pc_body_spank_layer"
    if writing.ass:
        "dance_behind_pc_writing_ass_layer"
    if writing.anus:
        "dance_behind_pc_writing_anus_layer"
    if tattoo.ass:
        "dance_behind_pc_tattoo_tramp"

    if c.pants and not c.thong:
        "dance_behind_pc_clothes_pants"
    if c.socks:
        "dance_behind_pc_clothes_tights"
    if c.bottom == 13:
        "dance_behind_pc_clothes_skirt"
    if c.top == 20:
        "dance_behind_pc_clothes_knot"
    elif c.top == 19:
        "dance_behind_pc_clothes_crop"

    always:
        "dance_behind_frame"

layeredimage dance_behind_breasts:
    always "dance_behind_pc_breasts_base_layer"
    always "dance_behind_pc_breasts_shad_layer"
    always "dance_behind_pc_breasts_nips_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
