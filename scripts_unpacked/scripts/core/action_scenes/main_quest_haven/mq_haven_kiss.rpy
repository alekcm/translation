layeredimage haven_kiss:

    always:
        "haven_kiss_base"

    group havman:
        attribute hav default:
            "haven_kiss_man_hav"
        attribute hav_off:
            null

    group vest:
        attribute veston:
            "haven_kiss_man_vest"
        attribute vestoff default:
            null
    group trou:
        attribute trouon:
            "haven_kiss_man_trou"
        attribute trouoff default:
            null

    if c.top:
        "haven_kiss_pc_top"
    if c.bottom:
        "haven_kiss_pc_shorts"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
