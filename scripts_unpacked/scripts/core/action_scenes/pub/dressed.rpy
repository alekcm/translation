image pc_pub_dressed_base:
    get_skin_filename("pc_pub_dressed_skin_base", False)
    skin_base_colour_transform()
image pc_pub_dressed_shad:
    get_skin_filename("pc_pub_dressed_skin_shad", False)
    skin_shad_colour_transform()

layeredimage pub_dressed:

    always:
        "pc_pub_dressed_bg" anchor (0.2, 0.0)
    if player.race > 0:
        "pc_pub_dressed_base"
    if player.race > 0:
        "pc_pub_dressed_shad"



    if c.pants > 0:
        "pc_pub_dressed_pants"
    if c.socks > 0:
        "pc_pub_dressed_socks"
    always:
        "pc_pub_dressed_dress"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
