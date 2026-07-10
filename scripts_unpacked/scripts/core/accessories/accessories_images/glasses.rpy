image topframe_f_layered:
    get_accessories_filename("topframe_f", "glasses")
    accessories_primary_colour_transform("glasses")
image topframe_b_layered:
    get_accessories_filename("topframe_b", "glasses")
    accessories_primary_colour_transform("glasses")

image avi_f_layered:
    get_accessories_filename("avi_f", "glasses")
    accessories_primary_colour_transform("glasses")
image avi_b_layered:
    get_accessories_filename("avi_b", "glasses")
    accessories_primary_colour_transform("glasses")

image horned_f_layered:
    get_accessories_filename("horned_f", "glasses")
    accessories_primary_colour_transform("glasses")
image horned_b_layered:
    get_accessories_filename("horned_b", "glasses")
    accessories_primary_colour_transform("glasses")

image nerd_f_layered:
    get_accessories_filename("nerd_f", "glasses")
    accessories_primary_colour_transform("glasses")
image nerd_b_layered:
    get_accessories_filename("nerd_b", "glasses")
    accessories_primary_colour_transform("glasses")

image round_f_layered:
    get_accessories_filename("round_f", "glasses")
    accessories_primary_colour_transform("glasses")
image round_b_layered:
    get_accessories_filename("round_b", "glasses")
    accessories_primary_colour_transform("glasses")

image mask_server_layer:
    "pc_glasses_eyemask_base"
    accessories_primary_colour_transform("glasses")

layeredimage pc_glasses_front:
    if acc.glasses == 1:
        "topframe_f_layered"

    if acc.glasses == 2:
        "pc_glasses_avi_g"
    if acc.glasses == 2:
        "avi_f_layered"


    if acc.glasses == 3:
        "pc_glasses_horned_g"
    if acc.glasses == 3:
        "horned_f_layered"

    if acc.glasses == 4:
        "pc_glasses_nerd_g"
    if acc.glasses == 4:
        "nerd_f_layered"


    if acc.glasses == 5:
        "round_f_layered"



layeredimage pc_glasses_back:
    if acc.glasses == 1:
        "topframe_b_layered"
    if acc.glasses == 2:
        "avi_b_layered"
    if acc.glasses == 3:
        "horned_b_layered"
    if acc.glasses == 4:
        "nerd_b_layered"
    if acc.glasses == 5:
        "round_b_layered"
    if acc.glasses == 6:
        "mask_server_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
