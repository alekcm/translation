



image tights_base:
    get_clothing_filename("tights", "socks", preg=True)
    socks_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("tights", "socks", preg=True), "socks", True)
image tights_trim:
    get_clothing_filename("tights", "socks", preg=True, is_base=False)
    socks_secondary_colour_transform()

layeredimage tights_layer:

    always:
        "tights_base"
    always:
        "tights_trim"

layeredimage high_stocking_layer:

    always:
        "tights_base"
    always:
        "pc_socks_tights_shine"
    always:
        "tights_trim"





image stocking_base:
    "pc_socks_base"
    socks_primary_colour_transform()
    clothing_alpha_transform("pc_socks_base", "socks", True)
image stocking_trim:
    "pc_socks_stocking"
    socks_secondary_colour_transform()

layeredimage stocking_layer:

    always:
        "stocking_base"
    always:
        "pc_socks_thigh_shine"
    always:
        "stocking_trim"





layeredimage schsocks_layer:

    always:
        "stocking_base"
    always:
        "stocking_trim"






image thinstripesocks_trim:
    "pc_socks_stripe_thin"
    socks_secondary_colour_transform()

layeredimage thinstripesocks_layer:

    always:
        "stocking_base"
    always:
        "thinstripesocks_trim"





image thickstripesocks_trim:
    "pc_socks_stripe_thick"
    socks_secondary_colour_transform()

layeredimage thickstripesocks_layer:

    always:
        "stocking_base"
    always:
        "thickstripesocks_trim"





image bargirl_sock_base:
    "pc_socks_bargirl_base"
    socks_primary_colour_transform()

image bargirl_sock_trim:
    "pc_socks_bargirl_trim"
    socks_secondary_colour_transform()

layeredimage bargirl_socks_layer:

    always:
        "bargirl_sock_base"
    always:
        "bargirl_sock_trim"





image garter_sock_base_layer:
    get_high_socks_filename("garter")
    socks_primary_colour_transform()
    clothing_alpha_transform(get_high_socks_filename("garter"), "socks", True)

image garter_sock_trim_layer:
    get_high_socks_filename("garter", is_base=False)
    socks_secondary_colour_transform()

layeredimage garter_socks_layer:

    always "garter_sock_base_layer"
    always "garter_sock_trim_layer"




image socks_bumhigh_base:
    "pc_socks_bumhigh_base"
    socks_primary_colour_transform()
    clothing_alpha_transform("pc_socks_bumhigh_base", "socks")
image socks_bumhigh_trim:
    "pc_socks_bumhigh_trim"
    socks_secondary_colour_transform()

layeredimage bumhigh_layer:
    always "socks_bumhigh_base"
    always "socks_bumhigh_trim"




image socks_pointed_base:
    "pc_socks_pointed_base"
    socks_primary_colour_transform()
    clothing_alpha_transform("pc_socks_pointed_base", "socks")
image socks_pointed_trim:
    "pc_socks_pointed_trim"
    socks_secondary_colour_transform()

layeredimage pointed_layer:
    always "socks_pointed_base"
    always "socks_pointed_trim"




image socks_diamond_base:
    "pc_socks_diamond_base"
    socks_primary_colour_transform()
    clothing_alpha_transform("pc_socks_diamond_base", "socks")
image socks_diamond_trim:
    "pc_socks_diamond_trim"
    socks_secondary_colour_transform()

layeredimage diamond_layer:
    always "socks_diamond_base"
    always "socks_diamond_trim"





image socks_server_base:
    "pc_socks_server_base"
    socks_primary_colour_transform()
    clothing_alpha_transform("pc_socks_server_base", "socks")
image socks_server_trim:
    "pc_socks_server_trim"
    socks_secondary_colour_transform()

layeredimage socks_server_layer:
    always "socks_server_base"
    always "socks_server_trim"





image leggings_base:
    get_clothing_filename("leggings", "socks", preg=True)
    socks_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("leggings", "socks", preg=True), "socks", True)
image leggings_trim:
    get_clothing_filename("leggings", "socks", preg=True, is_base=False)
    socks_secondary_colour_transform()

layeredimage leggings_layer:
    always "leggings_base"
    always "leggings_trim"





image maid_socks_base:
    get_clothing_filename("maid", "socks")
    socks_primary_colour_transform()
image maid_socks_trim:
    get_clothing_filename("maid", "socks", is_base=False)
    socks_secondary_colour_transform()

layeredimage maid_socks_layer:
    always "maid_socks_base"
    always "maid_socks_trim"





image polkasocks_trim:
    "pc_socks_polka"
    socks_secondary_colour_transform()

layeredimage polkadotsocks_layer:

    always:
        "stocking_base"
    always:
        "polkasocks_trim"





image polkastripesocks_trim:
    "pc_socks_polkastripe"
    socks_secondary_colour_transform()

layeredimage polkastripesocks_layer:

    always:
        "stocking_base"
    always:
        "polkastripesocks_trim"





image kneepads_base:
    "pc_socks_pads_base"
    socks_primary_colour_transform()
image kneepads_trim:
    "pc_socks_pads_trim"
    socks_secondary_colour_transform()

layeredimage kneepads_layer:
    always "kneepads_base"
    always "kneepads_trim"





image catsocks_base:
    "pc_socks_cat_base"
    socks_primary_colour_transform()
image catsocks_trim:
    "pc_socks_cat_trim"
    socks_secondary_colour_transform()

layeredimage catsocks_layer:
    always "catsocks_base"
    always "catsocks_trim"





image latexboots_base:
    "pc_socks_thighboots_base"
    socks_primary_colour_transform()


layeredimage latexboots_layer:
    always "latexboots_base"
    always "pc_socks_thighboots_shine"





image cowsocks_base:
    "pc_socks_base"
    socks_primary_colour_transform()
image cowsocks_trim:
    "pc_socks_cow"
    socks_secondary_colour_transform()

layeredimage cowsocks_layer:

    always:
        "cowsocks_base"
    always:
        "cowsocks_trim"





image santa_socks_base:
    "pc_socks_santa_base"
    socks_primary_colour_transform()
image santa_socks_trim:
    "pc_socks_santa_trim"
    socks_secondary_colour_transform()

layeredimage santa_socks_layer:
    always "santa_socks_base"
    always "santa_socks_trim"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
