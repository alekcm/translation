image navelheart_layer:
    get_accessories_filename("heart", "navelring", preg=True)
    accessories_secondary_colour_transform("navelring")


image nipring_layer:
    "nipring_layered"
    accessories_secondary_colour_transform("nipring")

layeredimage nipring_layered:


    if player.breasts == 1 and player.breasts_free:
        "pc_nipring_ring_1"
    elif player.breasts == 2 and player.breasts_free:
        "pc_nipring_ring_2"
    elif player.breasts == 3 and player.breasts_free:
        "pc_nipring_ring_3"



    if player.breasts == 1 and player.breasts_lifted:
        "pc_nipring_ring_c_1"
    elif player.breasts == 2 and player.breasts_lifted:
        "pc_nipring_ring_c_2"
    elif player.breasts == 3 and player.breasts_lifted:
        "pc_nipring_ring_c_3" 

image nipheart_layer:
    "nipheart_layered"
    accessories_primary_colour_transform("nipring")

image nipheart_bra_layer:
    "nipheart_layered"
    bra_primary_colour_transform()

layeredimage nipheart_layered:


    if player.breasts == 1 and player.breasts_free:
        "pc_nipring_heart_1"
    elif player.breasts == 2 and player.breasts_free:
        "pc_nipring_heart_2"
    elif player.breasts == 3 and player.breasts_free:
        "pc_nipring_heart_3"



    if player.breasts == 1 and player.breasts_lifted:
        "pc_nipring_heart_c_1"
    elif player.breasts == 2 and player.breasts_lifted:
        "pc_nipring_heart_c_2"
    elif player.breasts == 3 and player.breasts_lifted:
        "pc_nipring_heart_c_3"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
