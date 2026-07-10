



image stringsuit_body:
    get_bsuit_filename("string", preg=True)
    bsuit_primary_colour_transform()
image stringsuit_breasts:
    get_bsuit_filename("string", breasts=True)
    bsuit_primary_colour_transform()

layeredimage stringsuit_layer:
    always "stringsuit_body"
    always "stringsuit_breasts"





image uboob_base:
    get_bsuit_filename("underboob", preg=True)
image uboob_trim:
    get_bsuit_filename("underboob", base=False, preg=True)

image uboob_breasts_base:
    get_bsuit_filename("underboob", breasts=True)
image uboob_breasts_trim:
    get_bsuit_filename("underboob", base=False, breasts=True)

layeredimage underboob_suit_pre_layer:
    always "uboob_base"
    always "uboob_breasts_base"

image underboob_flat:
    Flatten("underboob_suit_pre_layer")

image uboob_body_trans:
    bsuit_primary_colour_transform()
    clothing_alpha_transform("underboob_flat", "bsuit")

layeredimage underboob_suit_layer:
    always "uboob_body_trans"
    always "uboob_trim"
    always "uboob_breasts_trim"





image frilly_suit_base:
    get_bsuit_filename("frilly", preg=True)
image frilly_suit_trim:
    get_bsuit_filename("frilly", base=False, preg=True)
image frilly_suit_lines:
    "pc_bsuit_frilly_lines_" + str(player.pregnancy)

image frilly_suit_breasts_base:
    get_bsuit_filename("frilly", breasts=True)
image frilly_suit_breasts_trim:
    get_bsuit_filename("frilly", base=False, breasts=True)
image frilly_suit_breasts_lines:
    "pc_bsuit_frilly_breasts_lines_" + str(player.breasts)

layeredimage frilly_suit_breasts_base_pre_layer:
    always "frilly_suit_base"
    always "frilly_suit_breasts_base"
image frilly_suit_base_flat:
    Flatten("frilly_suit_breasts_base_pre_layer")
image frilly_suit_base_trans:
    bsuit_primary_colour_transform()
    clothing_alpha_transform("frilly_suit_base_flat", "bsuit")

layeredimage frilly_suit_breasts_trim_pre_layer:
    always "frilly_suit_trim"
    always "frilly_suit_breasts_trim"
image frilly_suit_trim_flat:
    Flatten("frilly_suit_breasts_trim_pre_layer")
image frilly_suit_trim_trans:
    bsuit_secondary_colour_transform()
    clothing_alpha_transform("frilly_suit_trim_flat", "bsuit", False)

layeredimage frilly_suit_layer:
    always "frilly_suit_base_trans"
    always "frilly_suit_trim_trans"
    always "frilly_suit_lines"
    always "frilly_suit_breasts_lines"





image tleo_base:
    get_bsuit_filename("tleo", preg=True)

image tleo_breasts_base:
    get_bsuit_filename("tleo", breasts=True)

layeredimage tleo_pre_layer:
    always "tleo_base"
    always "tleo_breasts_base"

image tleo_flat:
    Flatten("tleo_pre_layer")

image tleo_body:
    bsuit_primary_colour_transform()
    clothing_alpha_transform("tleo_flat", "bsuit")





image open_base:
    get_bsuit_filename("open", preg=True)

image open_breasts_base:
    get_bsuit_filename("open", breasts=True)

layeredimage open_pre_layer:
    always "open_base"
    always "open_breasts_base"

image open_flat:
    Flatten("open_pre_layer")

image open_body:
    bsuit_primary_colour_transform()
    clothing_alpha_transform("open_flat", "bsuit")





image meshedsuit_base:
    get_bsuit_filename("meshed", preg=True)
image meshedsuit_trim:
    get_bsuit_filename("meshed", preg=True, base=False)
    bsuit_secondary_colour_transform()

image meshedsuit_breasts_base:
    get_bsuit_filename("meshed", breasts=True)
image meshedsuit_breasts_trim:
    get_bsuit_filename("meshed", breasts=True, base=False)
    bsuit_secondary_colour_transform()

layeredimage meshedsuit_pre_layer:
    always "meshedsuit_base"
    always "meshedsuit_breasts_base"

image meshedsuit_flat:
    Flatten("meshedsuit_pre_layer")

image meshedsuit_body:
    bsuit_primary_colour_transform()
    clothing_alpha_transform("meshedsuit_flat", "bsuit")

layeredimage meshedsuit_layer:
    always "meshedsuit_body"
    always "meshedsuit_trim"
    always "meshedsuit_breasts_trim"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
