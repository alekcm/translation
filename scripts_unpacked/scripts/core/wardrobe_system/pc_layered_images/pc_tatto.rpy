
image tattoo_chest_c_layer:
    ("tattoo_chest_c_" + str(tattoo.chest))
image tattoo_chest_n_layer:
    ("tattoo_chest_n_" + str(tattoo.chest))

layeredimage pc_tattoo_chest:

    if tattoo.chest > 0 and (c.top or c.outfit or c.bra):
        "tattoo_chest_c_layer"
    elif tattoo.chest > 0:
        "tattoo_chest_n_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
