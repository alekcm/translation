

image rachel_dancenude_grind_pc_base_layer:
    "rachel_dancenude_grind_pc_base"
    skin_base_colour_transform()
image rachel_dancenude_grind_pc_shad_layer:
    "rachel_dancenude_grind_pc_shad"
    skin_shad_colour_transform()

image rachel_dancenude_grind_pc_breasts_base_layer:
    get_skin_filename("rachel_dancenude_grind_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image rachel_dancenude_grind_pc_breasts_shad_layer:
    get_skin_filename("rachel_dancenude_grind_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image rachel_dancenude_grind_pc_breasts_nips_layer:
    get_skin_filename("rachel_dancenude_grind_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image rachel_dancenude_grind_pc_breasts_nipring_layer:
    get_skin_filename("rachel_dancenude_grind_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image rachel_dancenude_grind_pc_writing_ass_layer:
    "rachel_dancenude_grind_pc_writing_ass"
    writing_transform("ass")
image rachel_dancenude_grind_pc_writing_anus_layer:
    "rachel_dancenude_grind_pc_writing_anus"
    writing_transform("anus")

image rachel_dancenude_grind_pc_spank_layer:
    "rachel_dancenude_grind_pc_spank"
    opacity_transform(bruise.ass)

image rachel_dancenude_grind = LayeredImageProxy("rachel_dancenude_grind_layer", Transform(align=(0.8, 0.0)))

layeredimage rachel_dancenude_grind_layer:
    always "rachel_dancenude_grind_bg"

    always "rachel_dancenude_grind_pc_base_layer"
    always "rachel_dancenude_grind_pc_shad_layer"
    always "rachel_dancenude_grind_pc_spank_layer"

    if writing.ass:
        "rachel_dancenude_grind_pc_writing_ass_layer"
    if writing.anus:
        "rachel_dancenude_grind_pc_writing_anus_layer"
    if tattoo.ass:
        "rachel_dancenude_grind_pc_tattoo_tramp"

    always "rachel_dancenude_grind_pc_breasts_base_layer"
    always "rachel_dancenude_grind_pc_breasts_shad_layer"
    always "rachel_dancenude_grind_pc_breasts_nips_layer"
    if acc.nipring:
        "rachel_dancenude_grind_pc_breasts_nipring_layer"

    always "rachel_dancenude_grind_rachel"

    always "rachel_dancenude_grind_frame"




image rachel_dancenude_hug_pc_base_layer:
    "rachel_dancenude_hug_pc_base"
    skin_base_colour_transform()
image rachel_dancenude_hug_pc_shad_layer:
    "rachel_dancenude_hug_pc_shad"
    skin_shad_colour_transform()

image rachel_dancenude_hug_pc_breasts_base_layer:
    get_skin_filename("rachel_dancenude_hug_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image rachel_dancenude_hug_pc_breasts_shad_layer:
    get_skin_filename("rachel_dancenude_hug_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image rachel_dancenude_hug_pc_breasts_nips_layer:
    get_skin_filename("rachel_dancenude_hug_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image rachel_dancenude_hug_pc_breasts_nipring_layer:
    get_skin_filename("rachel_dancenude_hug_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image rachel_dancenude_hug_pc_writing_ass_layer:
    "rachel_dancenude_hug_pc_writing_ass"
    writing_transform("ass")
image rachel_dancenude_hug_pc_writing_anus_layer:
    "rachel_dancenude_hug_pc_writing_anus"
    writing_transform("anus")

image rachel_dancenude_hug_pc_spank_layer:
    "rachel_dancenude_hug_pc_spank"
    opacity_transform(bruise.ass)

image rachel_dancenude_hug = LayeredImageProxy("rachel_dancenude_hug_layer", Transform(align=(0.8, 0.0)))

layeredimage rachel_dancenude_hug_layer:
    always "rachel_dancenude_hug_bg"

    always "rachel_dancenude_hug_pc_base_layer"
    always "rachel_dancenude_hug_pc_shad_layer"
    always "rachel_dancenude_hug_pc_spank_layer"

    if writing.ass:
        "rachel_dancenude_hug_pc_writing_ass_layer"
    if writing.anus:
        "rachel_dancenude_hug_pc_writing_anus_layer"
    if tattoo.ass:
        "rachel_dancenude_hug_pc_tattoo_tramp"

    always "rachel_dancenude_hug_pc_breasts_base_layer"
    always "rachel_dancenude_hug_pc_breasts_shad_layer"
    always "rachel_dancenude_hug_pc_breasts_nips_layer"
    if acc.nipring:
        "rachel_dancenude_hug_pc_breasts_nipring_layer"

    always "rachel_dancenude_hug_frame"





image rachel_dancenude_hips_pc_base_layer:
    "rachel_dancenude_hips_pc_base"
    skin_base_colour_transform()
image rachel_dancenude_hips_pc_shad_layer:
    "rachel_dancenude_hips_pc_shad"
    skin_shad_colour_transform()

image rachel_dancenude_hips_pc_breasts_base_layer:
    get_skin_filename("rachel_dancenude_hips_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image rachel_dancenude_hips_pc_breasts_shad_layer:
    get_skin_filename("rachel_dancenude_hips_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image rachel_dancenude_hips_pc_writing_ass_layer:
    "rachel_dancenude_hips_pc_writing_ass"
    writing_transform("ass")
image rachel_dancenude_hips_pc_writing_anus_layer:
    "rachel_dancenude_hips_pc_writing_anus"
    writing_transform("anus")

image rachel_dancenude_hips_pc_spank_layer:
    "rachel_dancenude_hips_pc_spank"
    opacity_transform(bruise.ass)

image rachel_dancenude_hips = LayeredImageProxy("rachel_dancenude_hips_layer", Transform(align=(0.8, 0.0)))

layeredimage rachel_dancenude_hips_layer:
    always "rachel_dancenude_hips_bg"

    always "rachel_dancenude_hips_pc_breasts_base_layer"
    always "rachel_dancenude_hips_pc_breasts_shad_layer"

    always "rachel_dancenude_hips_pc_base_layer"
    always "rachel_dancenude_hips_pc_shad_layer"
    if acc.anus:
        "rachel_dancenude_hips_pc_plug"
    always "rachel_dancenude_hips_pc_spank_layer"

    if writing.ass:
        "rachel_dancenude_hips_pc_writing_ass_layer"
    if writing.anus:
        "rachel_dancenude_hips_pc_writing_anus_layer"
    if tattoo.ass:
        "rachel_dancenude_hips_pc_tattoo_tramp"

    always "rachel_dancenude_hips_rachel"

    always "rachel_dancenude_hips_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
