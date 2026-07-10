init python:
    def get_top_displayable(st, at, name, **kwargs):
        
        return (get_top_filename(name, **kwargs), None)

image top_pokenips:
    get_nips_filename()
    top_primary_colour_transform(get_nipple_poke_opacity())
image top_sec_pokenips:
    get_nips_filename()
    top_secondary_colour_transform(get_nipple_poke_opacity())

image pokenips:
    get_nips_filename()
    matrixcolor OpacityMatrix(get_nipple_poke_opacity())

image top_milkstain:
    get_milkstain_filename()
    top_primary_colour_transform()
image top_sec_milkstain:
    get_milkstain_filename()
    top_secondary_colour_transform()

image milkstain:
    get_milkstain_filename()





image shirt_breasts_base:
    get_top_filename("shirt", breasts=True)
    top_primary_colour_transform()

image shirt_base:
    get_top_filename("shirt", preg=True)
    top_primary_colour_transform()


layeredimage shirt_layer:
    always "shirt_base"
    always "shirt_breasts_base"


    if c.pokenips:
        "top_pokenips"  
    if player.milky:
        "milkstain"






image loosetee_breasts_base:
    get_top_filename("loosetee", breasts=True)

layeredimage loosetee_breasts:
    always "loosetee_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image loosetee_flat:
    Flatten("loosetee_breasts")
    top_primary_colour_transform()

image loosetee_trans:
    clothing_alpha_transform("loosetee_flat", "top", True)

image loosetee_breasts_trim:
    get_top_filename("loosetee", breasts=True, base=False)
    top_secondary_colour_transform()
    clothing_alpha_transform(get_top_filename("loosetee", breasts=True, base=False), "top", False)

layeredimage loosetee_layer:
    always "loosetee_trans"
    always "loosetee_breasts_trim"






image croptop_breasts_base:
    get_top_filename("croptop", breasts=True)

image croptop_base:
    get_top_filename("croptop", preg=True)

layeredimage croptop_layer:
    always "croptop_base"
    always "croptop_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"


image croptop_flat:
    Flatten("croptop_layer")
    top_primary_colour_transform()

image croptop:
    clothing_alpha_transform("croptop_flat", "top")





image vestskin_breasts_base:
    get_top_filename("vestskin", breasts=True)

layeredimage vestskin_base_layer:
    always "teeskin_base"
    always "vestskin_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image vestskin_flat:
    Flatten("vestskin_base_layer")

image vestskin_trans:
    top_primary_colour_transform()
    clothing_alpha_transform("vestskin_flat", "top")

image vestskin_breasts_trim:
    get_top_filename("vestskin", breasts=True, base=False)
    top_secondary_colour_transform()

layeredimage vestskin_layer:
    always "vestskin_trans"
    always "teeskin_trim"
    always "vestskin_breasts_trim"





image teeskin_base:
    get_top_filename("teeskin", preg=True)
image teeskin_breasts_base:
    get_top_filename("teeskin", breasts=True)

layeredimage teeskin_base_layer:
    always "teeskin_base"
    always "teeskin_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image teeskin_flat:
    Flatten("teeskin_base_layer")

image teeskin_trans:
    top_primary_colour_transform()
    clothing_alpha_transform("teeskin_flat", "top")

image teeskin_trim:
    get_top_filename("teeskin", preg=True, base=False)
    top_secondary_colour_transform()
image teeskin_breasts_trim:
    get_top_filename("teeskin", breasts=True, base=False)
    top_secondary_colour_transform()

layeredimage teeskin_layer:
    always "teeskin_trans"
    always "teeskin_trim"
    always "teeskin_breasts_trim"





image pc_top_vball_breasts_trim_1 = "pc_top_vball_breasts_trim"
image pc_top_vball_breasts_trim_2 = "pc_top_vball_breasts_trim"
image pc_top_vball_breasts_trim_3 = "pc_top_vball_breasts_trim"

image pc_top_vball_trim_1 = "pc_top_vball_trim_0"

image vballtop_breasts_base:
    get_top_filename("vball", breasts=True)
    top_primary_colour_transform()
image vballtop_breasts_trim:
    get_top_filename("vball", breasts=True, base=False)
    top_secondary_colour_transform()
    clothing_alpha_transform(get_top_filename("vball", breasts=True, base=False), "top", is_primary=False)

image vballtop_base:
    get_top_filename("vball", preg=True)
    top_primary_colour_transform()
image vballtop_trim:
    get_top_filename("vball", preg=True, base=False)
    top_secondary_colour_transform()
    clothing_alpha_transform(get_top_filename("vball", preg=True, base=False), "top", is_primary=False)

layeredimage vballtop_layer:   
    always "vballtop_breasts_trim"
    always "vballtop_trim"
    always "vballtop_base"
    always "vballtop_breasts_base"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image croptee_breasts_base:
    get_top_filename("croptee", breasts=True)
    top_secondary_colour_transform()
image croptee_breasts_trim:
    get_top_filename("croptee", breasts=True, base=False)
    top_primary_colour_transform()

image croptee_base:
    get_top_filename("croptee", preg=True)
    top_secondary_colour_transform()
image croptee_trim:
    get_top_filename("croptee", preg=True, base=False)
    top_primary_colour_transform()

layeredimage croptee_combine:
    always "croptee_trim"
    always "croptee_breasts_trim"

layeredimage croptee_layer:
    always "croptee_breasts_base"
    always "croptee_base"
    always "croptee_trim"
    always "croptee_breasts_trim"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image strappy_breasts_base:
    get_top_filename("strappy", breasts=True)
    top_secondary_colour_transform()
image strappy_breasts_trim:
    get_top_filename("strappy", breasts=True, base=False)
    top_primary_colour_transform()

image strappy_base:
    get_top_filename("strappy", preg=True)
    top_secondary_colour_transform()
    clothing_alpha_transform(get_top_filename("strappy", preg=True), "top", is_primary=False)
image strappy_trim:
    get_top_filename("strappy", preg=True, base=False)
    top_primary_colour_transform()

layeredimage strappy_layer:
    always "strappy_base"
    always "strappy_trim"
    always "strappy_breasts_base"
    always "strappy_breasts_trim"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image pc_top_haven_belly_base_1_1 = "pc_top_haven_belly_base_1_0"
image pc_top_haven_belly_base_2_1 = "pc_top_haven_belly_base_2_0"
image pc_top_haven_belly_base_3_1 = "pc_top_haven_belly_base_3_0"
image pc_top_haven_belly_base_3_2 = "pc_top_haven_belly_base_3_0"

image haventop_breasts_base:
    get_top_filename("haven", breasts=True)
    top_primary_colour_transform()

image haventop_base:
    get_top_filename("haven", breasts=True, preg=True, base=False)
    top_secondary_colour_transform()
    clothing_alpha_transform(get_top_filename("haven", breasts=True, preg=True), "top", False)

layeredimage haventop_layer:
    always "haventop_base"
    always "haventop_breasts_base"





image microbikini_breasts_base:
    get_top_filename("microbikini", breasts=True)

layeredimage microbikini_breasts_layer:
    always "microbikini_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image microbikini_breasts_flat:
    Flatten("microbikini_breasts_layer")

image microbikini_breasts_trans:
    top_primary_colour_transform()
    clothing_alpha_transform("microbikini_breasts_flat", "top")

image microbikini_breasts_trim:
    get_top_filename("microbikini", breasts=True, base=False)
    top_secondary_colour_transform()

layeredimage microbikini_top_layer:
    always "microbikini_breasts_trans"
    always "microbikini_breasts_trim"





image knotbikini_top_base:
    get_top_filename("knotbikini", breasts=True)
    top_primary_colour_transform()

layeredimage knotbikini_top:
    always "knotbikini_top_base"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image stringbikini_breasts_base:
    get_top_filename("stringbikini", breasts=True)

layeredimage stringbikini_breasts_layer:
    always "stringbikini_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image stringbikini_breasts_flat:
    Flatten("stringbikini_breasts_layer")

image stringbikini_breasts_trans:
    top_primary_colour_transform()
    clothing_alpha_transform("stringbikini_breasts_flat", "top")

image stringbikini_breasts_trim:
    get_top_filename("stringbikini", breasts=True, base=False)

layeredimage stringbikini_top_layer:
    always "stringbikini_breasts_trans"
    always "stringbikini_breasts_trim"





image haltertop_band:
    get_outfit_filename("halterdress", preg=True)
    top_secondary_colour_transform()

image haltertop_breasts:
    get_outfit_filename("halterdress", breasts=True)

layeredimage haltertop_breasts_layer:
    always "haltertop_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image haltertop_breasts_flat:
    Flatten("haltertop_breasts_layer")

image haltertop_breasts_trans:
    top_primary_colour_transform()
    clothing_alpha_transform("haltertop_breasts_flat", "top")

layeredimage haltertop_layer:

    always "haltertop_breasts_trans"
    always "haltertop_band"





image knotfront_base:
    get_top_filename("knotfront", breasts=True)

layeredimage knotfront_base_layer:
    always "knotfront_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image knotfront_base_flat:
    Flatten("knotfront_base_layer")

image knotfront_base_trans:
    top_primary_colour_transform()
    clothing_alpha_transform("knotfront_base_flat", "top")

image knotfront_trim:
    get_top_filename("knotfront", breasts=True, base=False)
    top_primary_colour_transform()

layeredimage knotfront_layer:
    always "knotfront_base_trans"
    always "knotfront_trim"





image shoulderless_breasts:
    get_top_filename("shoulderless", breasts=True)

image shoulderless_belly:
    get_top_filename("shoulderless", preg=True)

layeredimage shoulderless_toflat:
    always "shoulderless_belly"
    always "shoulderless_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image shoulderless_colour:
    Flatten("shoulderless_toflat")
    top_primary_colour_transform()

image shoulderless_layer:
    clothing_alpha_transform("shoulderless_colour", "top")





image shoulderlessruff_breasts:
    get_top_filename("shoulderlessruff", breasts=True)
    top_primary_colour_transform()

image shoulderlessruff_belly:
    get_top_filename("shoulderlessruff", preg=True)
    top_primary_colour_transform()

image shoulderlessruff_larm_layer:
    DynamicDisplayable(get_top_displayable, "shoulderlessruff", arm="larm")
    top_primary_colour_transform()
image shoulderlessruff_larm_above_layer:
    "pc_top_shoulderlessruff_larm_coverabove_base"
    top_primary_colour_transform()

image shoulderlessruff_rarm_layer:
    DynamicDisplayable(get_top_displayable, "shoulderlessruff", arm="rarm")
    top_primary_colour_transform()

layeredimage shoulderlessruff_layer:

    always "shoulderlessruff_belly"
    always "shoulderlessruff_breasts"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image sleevelessneck_body:
    get_outfit_filename("sidestrapdress", preg=True)
    top_primary_colour_transform()

image sleevelessneck_breasts:
    get_outfit_filename("sidestrapdress", breasts=True)
    top_primary_colour_transform()

layeredimage sleevelessneck_layer:

    always "sleevelessneck_body"
    always "sleevelessneck_breasts"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image vestloose_base:
    get_top_filename("vestloose", breasts=True)

layeredimage vestloose_base_layer:
    always "vestloose_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image vestloose_base_flat:
    Flatten("vestloose_base_layer")

image vestloose_layer:
    top_primary_colour_transform()
    clothing_alpha_transform("vestloose_base_flat", "top")





image undercrop_base:
    get_top_filename("undercrop", breasts=True)

layeredimage undercrop_base_layer:
    always "undercrop_base"

    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image undercrop_base_flat:
    Flatten("undercrop_base_layer")

image undercrop_layer:
    top_primary_colour_transform()
    clothing_alpha_transform("undercrop_base_flat", "top")





image knotted_body:
    get_top_filename("knotted", preg=True)
    top_primary_colour_transform()

image knotted_breasts:
    get_top_filename("knotted", breasts=True)
    top_primary_colour_transform()

layeredimage knotted_layer:
    always "knotted_body"
    always "knotted_breasts"

    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image rags_top:
    get_top_filename("rags", breasts=True)

layeredimage rags_top_layerd:
    always "rags_top"

    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image rags_top_flat:
    Flatten("rags_top_layerd")

image rags_top_layer:
    top_primary_colour_transform()
    clothing_alpha_transform("rags_top_flat", "top")






image pc_top_sheerdrop_belly_base_1_1 = "pc_top_sheerdrop_belly_base_1_0"
image pc_top_sheerdrop_belly_base_2_1 = "pc_top_sheerdrop_belly_base_2_0"
image pc_top_sheerdrop_belly_base_3_1 = "pc_top_sheerdrop_belly_base_3_0"
image pc_top_sheerdrop_belly_base_3_2 = "pc_top_sheerdrop_belly_base_3_0"
image pc_top_sheerdrop_belly_base_3_3 = "pc_top_sheerdrop_belly_base_3_0"

image sheerdrop_body:
    get_top_filename("sheerdrop", breasts=True, preg=True)

image sheerdrop_larm_layer:
    DynamicDisplayable(get_top_displayable, "sheerdrop", arm="larm")
    clothing_alpha_transform(DynamicDisplayable(get_top_displayable, "sheerdrop", arm="larm"), "top")
    top_primary_colour_transform()

image sheerdrop_larm_above_layer:
    "pc_top_sheerdrop_larm_coverabove_base"
    clothing_alpha_transform("pc_top_sheerdrop_larm_coverabove_base", "top")
    top_primary_colour_transform()

image sheerdrop_rarm_layer:
    DynamicDisplayable(get_top_displayable, "sheerdrop", arm="rarm")
    clothing_alpha_transform(DynamicDisplayable(get_top_displayable, "sheerdrop", arm="rarm"), "top")
    top_primary_colour_transform()

layeredimage sheerdrop_layered:
    always "sheerdrop_body"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image sheerdrop_base_flat:
    Flatten("sheerdrop_layered")

image sheerdrop_layer:
    top_primary_colour_transform()
    clothing_alpha_transform("sheerdrop_base_flat", "top")





image pc_top_sportloose_belly_base_1_1 = "pc_top_sportloose_belly_base_1_0"
image pc_top_sportloose_belly_base_2_1 = "pc_top_sportloose_belly_base_2_0"
image pc_top_sportloose_belly_base_3_1 = "pc_top_sportloose_belly_base_3_0"
image pc_top_sportloose_belly_base_3_2 = "pc_top_sportloose_belly_base_3_0"

image sportloose_body:
    get_top_filename("sportloose", breasts=True, preg=True)

layeredimage sportloose_layerd:
    always "sportloose_body"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image sportloose_flat:
    Flatten("sportloose_layerd")

image sportloose_layer:
    top_primary_colour_transform()
    clothing_alpha_transform("sportloose_flat", "top")





image sweater_body_base:
    get_top_filename("sweater", preg=True)
    top_primary_colour_transform()
image sweater_body_trim:
    get_top_filename("sweater", preg=True, base=False)
    top_secondary_colour_transform()
image sweater_boob:
    get_top_filename("sweater", breasts=True)
    top_primary_colour_transform()

layeredimage sweater_layerd:
    always "sweater_body_base"

    always "sweater_body_trim"
    always "sweater_boob"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"

image sweater_larm:
    DynamicDisplayable(get_top_displayable, "sweater", arm="larm")
    top_secondary_colour_transform()
image sweater_above_larm:
    "pc_top_sweater_larm_coverabove_base"
    top_secondary_colour_transform()
image sweater_rarm:
    DynamicDisplayable(get_top_displayable, "sweater", arm="rarm")
    top_secondary_colour_transform()





image vestlong_body_layer:
    get_top_filename("vestlong", preg=True)
image vestlong_breasts_layer:
    get_top_filename("vestlong", breasts=True)

layeredimage vestlong_layerd:
    always "vestlong_body_layer"
    always "vestlong_breasts_layer"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image vestlong_flat:
    Flatten("vestlong_layerd")
image vestlong_layer:
    "vestlong_flat"
    top_primary_colour_transform()
    clothing_alpha_transform("vestlong_flat", "top")





image sleevelesscoat_body_layer:
    get_top_filename("sleevelesscoat", preg=True)
    top_secondary_colour_transform()
image sleevelesscoat_breasts_layer:
    get_top_filename("sleevelesscoat", breasts=True)
    top_secondary_colour_transform()

layeredimage sleevelesscoat_layerd:
    always "vestlong_layer"
    always "sleevelesscoat_body_layer"
    always "sleevelesscoat_breasts_layer"





image shirt_sleeveless_body_base:
    get_top_filename("shirtsleeveless", preg=True)
image shirt_sleeveless_body_trim:
    get_top_filename("shirtsleeveless", preg=True, base=False)
    top_secondary_colour_transform()

image shirt_sleeveless_breasts_base:
    get_top_filename("shirtsleeveless", breasts=True)
image shirt_sleeveless_breasts_trim:
    get_top_filename("shirtsleeveless", breasts=True, base=False)
    top_secondary_colour_transform()

layeredimage shirt_sleeveless_toflat:
    always "shirt_sleeveless_body_base"
    always "shirt_sleeveless_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image shirt_sleeveless_flat:
    Flatten("shirt_sleeveless_toflat")
image shirt_sleeveless_base:
    "shirt_sleeveless_flat"
    top_primary_colour_transform()
    clothing_alpha_transform("shirt_sleeveless_flat", "top")

layeredimage shirt_sleeveless_layer:
    always "shirt_sleeveless_base"

    always "shirt_sleeveless_body_trim"
    always "shirt_sleeveless_breasts_trim"





image heartpatch_top_base_body:
    get_top_filename("heartpatch", preg=True)
    top_primary_colour_transform()
image heartpatch_top_trim_body:
    get_top_filename("heartpatch", preg=True, base=False)
    top_secondary_colour_transform()

image heartpatch_top_base_breasts:
    get_top_filename("heartpatch", breasts=True)
    top_primary_colour_transform()
image heartpatch_top_trim_breasts:
    get_top_filename("heartpatch", breasts=True, base=False)
    top_secondary_colour_transform()

image heartpatch_top_nip_sec:
    AlphaMask("top_sec_pokenips", get_top_filename("heartpatch", breasts=True, base=False))

layeredimage heartpatch_top_layerd:
    always "heartpatch_top_base_body"
    always "heartpatch_top_trim_body"
    always "heartpatch_top_base_breasts"
    if c.pokenips:
        "top_pokenips"
    always "heartpatch_top_trim_breasts"
    if c.pokenips:
        "heartpatch_top_nip_sec"
    if player.milky:
        "milkstain"





image harlequin_top_base_body:
    get_top_filename("harlequin", preg=True)
    top_primary_colour_transform()
image harlequin_top_trim_body:
    get_top_filename("harlequin", preg=True, base=False)
    top_secondary_colour_transform()

image harlequin_top_base_breasts:
    get_top_filename("harlequin", breasts=True)
    top_primary_colour_transform()
image harlequin_top_trim_breasts:
    get_top_filename("harlequin", breasts=True, base=False)
    top_secondary_colour_transform()

image harlequin_top_nip_sec:
    AlphaMask("top_sec_pokenips", get_top_filename("harlequin", breasts=True, base=False))

layeredimage harlequin_top_layerd:
    always "harlequin_top_base_body"
    always "harlequin_top_trim_body"
    always "harlequin_top_base_breasts"
    if c.pokenips:
        "top_pokenips"
    always "harlequin_top_trim_breasts"
    if c.pokenips:
        "harlequin_top_nip_sec"
    if player.milky:
        "milkstain"





image rippedtee_base_body:
    get_top_filename("rippedtee", preg=True)
    top_primary_colour_transform()

image rippedtee_base_breasts:
    get_top_filename("rippedtee", breasts=True)
    top_primary_colour_transform()


layeredimage rippedtee_layer:
    always "rippedtee_base_body"
    always "rippedtee_base_breasts"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"

image rippedtee_layerd:
    Flatten("rippedtee_layer")
    clothing_alpha_transform("rippedtee_layer", "top")






image boobwindow_base_breasts:
    get_top_filename("boobwindow", breasts=True)
    top_primary_colour_transform()
image boobwindow_trim_breasts:
    get_top_filename("boobwindow", breasts=True, base=False)
    top_secondary_colour_transform()

image boobwindow_base:
    get_top_filename("boobwindow", preg=True)
    top_primary_colour_transform()
image boobwindow_trim:
    get_top_filename("boobwindow", preg=True, base=False)
    top_secondary_colour_transform()

layeredimage boobwindow_layerd:
    always "boobwindow_base"
    always "boobwindow_trim"
    always "boobwindow_base_breasts"
    always "boobwindow_trim_breasts"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"






image meshtop_base_breasts:
    get_top_filename("meshtop", breasts=True)
    top_primary_colour_transform()
image meshtop_trim_breasts:
    get_top_filename("meshtop", breasts=True, base=False)
    top_secondary_colour_transform()
    clothing_alpha_transform(get_top_filename("meshtop", breasts=True, base=False), "top", False)

layeredimage meshtop_layerd:
    always "meshtop_trim_breasts"
    always "meshtop_base_breasts"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image strappycross_base_breasts:
    get_top_filename("strappycross", breasts=True)
image strappycross_trim_breasts:
    get_top_filename("strappycross", breasts=True, base=False)
    top_secondary_colour_transform()


layeredimage strappycross_layerd:
    always "strappycross_base_breasts"

    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"

image strappycross_flat:
    Flatten("strappycross_layerd")
    top_primary_colour_transform()
    clothing_alpha_transform("strappycross_layerd", "top")

layeredimage strappycross_layer:
    always "strappycross_flat"
    always "strappycross_trim_breasts"





image only_base_breasts:
    get_top_filename("only", breasts=True)
image only_base_body:
    get_top_filename("only", preg=True)

layeredimage only_layerd:
    always "only_base_body"
    always "only_base_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image only_flat:
    Flatten("only_layerd")
image only_layer:
    top_primary_colour_transform()
    clothing_alpha_transform("only_flat", "top")




image chiwindow_base_breasts:
    get_top_filename("chiwindow", breasts=True)
image chiwindow_trim_breasts:
    get_top_filename("chiwindow", breasts=True, base=False)
    top_secondary_colour_transform()


layeredimage chiwindow_layerd:
    always "chiwindow_base_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image chiwindow_flat:
    Flatten("chiwindow_layerd")
    top_primary_colour_transform()
    clothing_alpha_transform("chiwindow_layerd", "top")

layeredimage chiwindow_layer:
    always "chiwindow_flat"
    always "chiwindow_trim_breasts"





image boobtube_breasts:
    get_top_filename("boobtube", breasts=True)


layeredimage boobtube_layerd:
    always "boobtube_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image boobtube_layer:
    Flatten("boobtube_layerd")
    top_primary_colour_transform()
    clothing_alpha_transform("boobtube_layerd", "top")





image deepv_body_base:
    get_top_filename("deepv", preg=True)
image deepv_breasts_base:
    get_top_filename("deepv", breasts=True)

layeredimage deepv_layerd:
    always "deepv_body_base"
    always "deepv_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image deepv_layer:
    Flatten("deepv_layerd")
    top_primary_colour_transform()
    clothing_alpha_transform("deepv_layerd", "top")





image pc_top_perry_base_3 = "pc_top_perry_base_2"
image perry_breasts:
    get_top_filename("perry", breasts=True)
    top_primary_colour_transform()
image perry_body:
    get_top_filename("perry", preg=True)
    top_primary_colour_transform()

image perry_larm_layerd:
    DynamicDisplayable(get_top_displayable, "perry", arm="larm")
    top_primary_colour_transform()
image perry_larm_above_layerd:
    "pc_top_perry_larm_coverabove_base"
    top_primary_colour_transform()

image perry_rarm_layerd:
    DynamicDisplayable(get_top_displayable, "perry", arm="rarm")
    top_primary_colour_transform()


layeredimage perry_layerd:
    always "perry_body"
    always "perry_breasts"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image latextop_breasts_base_layer:
    get_top_filename("latextop", breasts=True)
    top_primary_colour_transform()

image latextop_larm_layer:
    DynamicDisplayable(get_outfit_displayable, "bodysuit", arm="larm")
    top_primary_colour_transform()
image latextop_larm_above_layer:
    "pc_outfit_bodysuit_larm_coverabove_base"
    top_primary_colour_transform()

image latextop_rarm_layer:
    DynamicDisplayable(get_outfit_displayable, "bodysuit", arm="rarm")
    top_primary_colour_transform()

layeredimage latextop_layered:
    always "latextop_breasts_base_layer"  
    if c.pokenips:
        "top_pokenips"
    always "pc_top_latextop_shine"





image jaytee_breasts_base_layer:
    get_top_filename("jaytee", breasts=True)
    top_primary_colour_transform()
image jaytee_body_base_layer:
    get_top_filename("jaytee", preg=True)
    top_primary_colour_transform()
image jaytee_body_trim_layer:
    get_top_filename("jaytee", preg=True, base=False)
    top_secondary_colour_transform()

layeredimage jaytee_layered:
    always "jaytee_body_base_layer"  
    always "jaytee_body_trim_layer"  
    always "jaytee_breasts_base_layer"  
    if player.milky:
        "milkstain"





image drape_base_layer:
    get_top_filename("drape", breasts=True)
image drape_trim_layer:
    get_top_filename("drape", base=False, breasts=True)
    top_secondary_colour_transform()

layeredimage drapetop_base_layered:
    always "drape_base_layer"  
    if c.pokenips:
        "pokenips"

image drapetop_base_flat:
    Flatten("drapetop_base_layered")
image drapetop_base_trans:
    top_primary_colour_transform()
    clothing_alpha_transform("drapetop_base_flat", "top")

layeredimage drapetop_layered:
    always "drapetop_base_trans"  
    always "drape_trim_layer"





image rufftop_base_layer:
    get_outfit_filename("ruffpj", breasts=True)
    top_primary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("ruffpj", breasts=True), "top")
image rufftop_trim_layer:
    get_outfit_filename("ruffpj", base=False, breasts=True)
    top_secondary_colour_transform()

layeredimage rufftop_layered:
    always "rufftop_base_layer"  
    always "rufftop_trim_layer"






image santa_base_layer:
    get_top_filename("santa", preg=True)
    top_primary_colour_transform()
image santa_trim_layer:
    get_top_filename("santa", base=False, preg=True)
    top_secondary_colour_transform()

image santa_breasts_base_layer:
    get_top_filename("santa", breasts=True)
    top_primary_colour_transform()
image santa_breasts_trim_layer:
    get_top_filename("santa", base=False, breasts=True)
    top_secondary_colour_transform()

layeredimage santa_top_layered:
    always "santa_base_layer"  
    always "santa_trim_layer"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"
    always "santa_breasts_base_layer"  
    always "santa_breasts_trim_layer"





image sleevelessmuff_base_layer:
    get_top_filename("sleevelessmuff", breasts=True)
    top_secondary_colour_transform()
image sleevelessmuff_trim_layer:
    get_top_filename("sleevelessmuff", base=False, breasts=True)
    top_primary_colour_transform()

layeredimage sleevelessmuff_layered:
    always "sleevelessmuff_base_layer"  
    always "sleevelessmuff_trim_layer"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image shirtbaggy_base_layer:
    get_top_filename("shirtbaggy", preg=True)
    top_primary_colour_transform()
image shirtbaggy_breasts_layer:
    get_top_filename("shirtbaggy", breasts=True)
    top_primary_colour_transform()

layeredimage shirtbaggy_layered:
    always "shirtbaggy_base_layer"  
    always "shirtbaggy_breasts_layer"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"





image shoulderlesstee_base_layer:
    get_top_filename("shoulderlesstee", preg=True)
    top_primary_colour_transform()
image shoulderlesstee_breasts_layer:
    get_top_filename("shoulderlesstee", breasts=True)
    top_primary_colour_transform()

layeredimage shoulderlesstee_layered:
    always "shoulderlesstee_base_layer"  
    always "shoulderlesstee_breasts_layer"
    if c.pokenips:
        "top_pokenips"
    if player.milky:
        "milkstain"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
