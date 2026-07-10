layeredimage pc_sch_shirt_cut:
    if c.shirt_body == 1:
        "shirt_body_ruff_cut_layer"
    elif c.shirt_body == 2:
        "shirt_body_short_cut_layer"

layeredimage pc_sch_shirt_body:
    if c.shirt_body == 1:
        "shirt_body_ruff_base_layer"
    elif c.shirt_body == 2:
        "shirt_body_short_base_layer"

    if c.shirt_body == 1:
        "shirt_body_ruff_trim_layer"

layeredimage pc_sch_shirt:

    if c.jacket == 1:
        "pc_sch_shirt_cut"
    else:
        "pc_sch_shirt_body"



    if c.shirt_collar == 1:
        "shirt_collar_ruff_base_layer"
    elif c.shirt_collar == 2:
        "shirt_collar_standard_base_layer"
    elif c.shirt_collar == 3:
        "shirt_collar_lace_base_layer"
    elif c.shirt_collar == 4:
        "shirt_collar_large_base_layer"


    if c.shirt_collar == 1:
        "shirt_collar_ruff_trim_layer"
    elif c.shirt_collar == 3:
        "shirt_collar_lace_trim_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
