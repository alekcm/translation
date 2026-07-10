image jaylee_asslick_base_base_layer:
    "jaylee_asslick_base_base"
    skin_base_colour_transform()
image jaylee_asslick_base_shad_layer:
    "jaylee_asslick_base_shad"
    skin_shad_colour_transform()

image jaylee_asslick_base_spank_layer:
    "jaylee_asslick_base_spank"
    opacity_transform(bruise.ass)

image jaylee_asslick = LayeredImageProxy("jaylee_asslick_layered", Transform(align=(0.8, 0.0)))

layeredimage jaylee_asslick_layered:
    always "jaylee_asslick_bg"

    always "jaylee_asslick_base_base_layer"
    always "jaylee_asslick_base_shad_layer"
    always "jaylee_asslick_base_spank_layer"
    if tattoo.ass:
        "jaylee_asslick_base_tattoo"
    always "jaylee_asslick_base_col"

    group lick:
        attribute lick default "jaylee_asslick_head_down"

        attribute tongue "jaylee_asslick_head_up"
        attribute tongue "jaylee_asslick_head_up_tongue"

        attribute happy "jaylee_asslick_head_up"
        attribute happy "jaylee_asslick_head_up_smile"


    always "jaylee_asslick_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
