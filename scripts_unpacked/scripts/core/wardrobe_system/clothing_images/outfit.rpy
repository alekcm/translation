init python:
    def get_outfit_displayable(st, at, name, **kwargs):
        
        return (get_outfit_filename(name, **kwargs), None)

image trans_normal:
    Solid("#fff")
    matrixcolor OpacityMatrix(0.97)
image trans_sheer:
    Solid("#fff")
    matrixcolor OpacityMatrix(0.90)
image trans_trans:
    Solid("#fff")
    matrixcolor OpacityMatrix(0.75)
image trans_opaque:
    Solid("#fff")

image outfit_pokenips:
    get_nips_filename()
    outfit_primary_colour_transform(get_nipple_poke_opacity())
image outfit_sec_pokenips:
    get_nips_filename()
    outfit_secondary_colour_transform(get_nipple_poke_opacity())





image hospitalgown_breasts:
    get_outfit_filename("hospitalgown", breasts=True)
    outfit_primary_colour_transform()

image hospitalgown_base:
    get_outfit_filename("hospitalgown", preg=True)
    outfit_primary_colour_transform()

layeredimage hospitalgown_layer:
    always "hospitalgown_base"
    always "hospitalgown_breasts"
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image backlessmini_body:
    get_outfit_filename("backlessmini", preg=True)

image backlessmini_breasts:
    get_outfit_filename("backlessmini", breasts=True)

layeredimage backlessmini_layer:
    always "backlessmini_body"
    always "backlessmini_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image backlessmini_flat:
    Flatten("backlessmini_layer")
    outfit_primary_colour_transform()

image backlessmini:
    clothing_alpha_transform("backlessmini_flat", "outfit", True)




image summerdress_body:
    get_outfit_filename("summerdress", preg=True)

image summerdress_breasts:
    get_outfit_filename("summerdress", breasts=True)

layeredimage summerdress_layer:
    always "summerdress_body"
    always "summerdress_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image summerdress:
    "summerdress_layer"
    outfit_primary_colour_transform()





image bimbodress_body:
    get_outfit_filename("bimbodress", preg=True)

image bimbodress_breasts:
    get_outfit_filename("bimbodress", breasts=True)

layeredimage bimbodress_layer:
    always "bimbodress_body"
    always "bimbodress_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image bimbodress_flat:
    Flatten("bimbodress_layer")
    outfit_primary_colour_transform()

image bimbodress:
    clothing_alpha_transform("bimbodress_flat", "outfit", True)





image bodycon_breasts_base:
    get_top_filename("croptop", breasts=True)

image bodycon_base:
    get_outfit_filename("bodycon", preg=True)

layeredimage bodycon_layer:
    always "bodycon_base"
    always "bodycon_breasts_base"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image bodycon_flat:
    Flatten("bodycon_layer")
    outfit_primary_colour_transform()

image bodycon:
    clothing_alpha_transform("bodycon_flat", "outfit")





image schswimsuit_body:
    get_outfit_filename("schswimsuit", preg=True)

image schswimsuit_breasts:
    get_outfit_filename("schswimsuit", breasts=True)

layeredimage schswimsuit_layer:
    always "schswimsuit_body"
    always "schswimsuit_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image schswimsuit_flat:
    Flatten("schswimsuit_layer")
    outfit_primary_colour_transform()

image schswimsuit:
    clothing_alpha_transform("schswimsuit_flat", "outfit", True)





image compswimsuit_body_base:
    get_outfit_filename("compswimsuit", preg=True)
    outfit_secondary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("compswimsuit", preg=True), "outfit", False)

image compswimsuit_body_trim:
    get_outfit_filename("compswimsuit", base=False, preg=True)
    outfit_primary_colour_transform()

image compswimsuit_breasts:
    get_outfit_filename("compswimsuit", breasts=True)
    outfit_primary_colour_transform()

layeredimage compswimsuit_layer:
    always "compswimsuit_body_base"
    always "compswimsuit_body_trim"
    always "compswimsuit_breasts"
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image halterdress_breasts:
    get_outfit_filename("halterdress", breasts=True)
    outfit_primary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("halterdress", breasts=True), "outfit")

image halterdress_band:
    get_outfit_filename("halterdress", preg=True)
    outfit_secondary_colour_transform()

image halterdress_breasts:
    get_outfit_filename("halterdress", breasts=True)

layeredimage halterdress_breasts_layer:
    always "halterdress_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image halterdress_breasts_flat:
    Flatten("halterdress_breasts_layer")

image halterdress_breasts_trans:
    outfit_primary_colour_transform()
    clothing_alpha_transform("haltertop_breasts_flat", "outfit")

image halterdress_skirt:
    get_outfit_filename("halterdress_skirt", preg=True)
    outfit_primary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("halterdress_skirt", preg=True), "outfit")

layeredimage halterdress_layer:
    always "halterdress_breasts_trans"
    always "halterdress_skirt"
    always "halterdress_band"





image sidestrapdress_body:
    get_outfit_filename("sidestrapdress", preg=True)
    outfit_primary_colour_transform()

image sidestrapdress_breasts:
    get_outfit_filename("sidestrapdress", breasts=True)
    outfit_primary_colour_transform()

image sidestrapdress_skirt:
    get_outfit_filename("sidestrapdress_skirt", preg=True)
    outfit_primary_colour_transform()

layeredimage sidestrapdress_layer:
    always "sidestrapdress_skirt"
    always "sidestrapdress_body"
    always "sidestrapdress_breasts"
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image patchdress_body_base:
    get_outfit_filename("patchdress", preg=True)

image patchdress_body_trim:
    get_outfit_filename("patchdress", preg=True, base=False)
    outfit_primary_colour_transform()

image patchdress_breasts_base:
    get_outfit_filename("patchdress", breasts=True)

image patchdress_breasts_trim:
    get_outfit_filename("patchdress", breasts=True, base=False)
    outfit_primary_colour_transform()

layeredimage patchdress_toflat:
    always "patchdress_body_base"
    always "patchdress_breasts_base"

image patchdress_flat:
    Flatten("patchdress_toflat")
    outfit_secondary_colour_transform()

image patchdress_trans:
    clothing_alpha_transform("patchdress_flat", "outfit", False)

layeredimage patchdress_layer:

    always "patchdress_trans"
    always "patchdress_body_trim"
    always "patchdress_breasts_trim"
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image shoulderwrap_body:
    get_outfit_filename("shoulderwrap", preg=True)
    outfit_primary_colour_transform()

image shoulderwrap_body_breasts:
    get_outfit_filename("shoulderwrap", breasts=True)
    outfit_primary_colour_transform()

image shoulderwrap_breasts:
    get_outfit_filename("shoulderwrap", breasts=True, base=False)
    outfit_secondary_colour_transform()

layeredimage shoulderwrap_layer:
    always "shoulderwrap_body"
    always "shoulderwrap_body_breasts"
    always "shoulderwrap_breasts"





image bodyconmaternal_breasts:
    get_outfit_filename("bodyconmaternal", breasts=True)

image bodyconmaternal_body_base:
    get_outfit_filename("bodyconmaternal", preg=True)

image bodyconmaternal_body_trim:
    get_outfit_filename("bodyconmaternal", preg=True, base=False)
    outfit_secondary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("bodyconmaternal", preg=True, base=False), "outfit", False)

layeredimage bodyconmaternal_toflat:
    always "bodyconmaternal_body_base"
    always "bodyconmaternal_breasts"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image bodyconmaternal_flat:
    Flatten("bodyconmaternal_toflat")
    outfit_primary_colour_transform()

image bodyconmaternal_trans:
    clothing_alpha_transform("bodyconmaternal_flat", "outfit", True)

layeredimage bodyconmaternal_layer:
    always "bodyconmaternal_body_trim"
    always "bodyconmaternal_trans"



image bargirl_breasts_base:
    get_outfit_filename("bargirl", breasts=True)
    outfit_primary_colour_transform()

image bargirl_breasts_trim:
    get_outfit_filename("bargirl", base=False, breasts=True)
    outfit_secondary_colour_transform()

image bargirl_base:
    get_outfit_filename("bargirl", preg=True)
    outfit_primary_colour_transform()

image bargirl_trim:
    get_outfit_filename("bargirl", base=False, preg=True)
    outfit_secondary_colour_transform()

layeredimage bargirl_layer:

    always "bargirl_base"
    always "bargirl_trim"
    always "bargirl_breasts_base"
    always "bargirl_breasts_trim"



image rags_outfit_breasts_base:
    get_outfit_filename("rags", breasts=True)

image rags_outfit_base:
    get_outfit_filename("rags", preg=True)

image rags_outfit_nips:
    AlphaMask("pokenips", "rags_outfit_breasts_base")

layeredimage rags_outfit_layerd:
    always "rags_outfit_base"
    always "rags_outfit_breasts_base"
    if c.pokenips:
        "rags_outfit_nips"
    if player.milky:
        "milkstain"

image rags_outfit_flat:
    Flatten("rags_outfit_layerd")

image rags_outfit_layer:
    outfit_primary_colour_transform()
    clothing_alpha_transform("rags_outfit_flat", "outfit")





image collardress_base_layer:
    "pc_outfit_dresscollar_base"
    outfit_primary_colour_transform()
image collardress_trim_layer:
    "pc_outfit_dresscollar_trim"
    outfit_secondary_colour_transform()

image collardress_breasts_layer:
    get_outfit_filename("dresscollar", breasts=True)
    outfit_primary_colour_transform()

image collardress_belly_base_layer:
    get_outfit_filename("dresscollar", preg=True)
    outfit_primary_colour_transform()
image collardress_belly_trim_layer:
    get_outfit_filename("dresscollar", preg=True, base=False)
    outfit_secondary_colour_transform()

layeredimage collardress_layer:
    always "collardress_base_layer"
    always "collardress_trim_layer"
    always "collardress_breasts_layer"
    if player.pregnancy:
        "collardress_belly_base_layer"
    if player.pregnancy:
        "collardress_belly_trim_layer"





image serverdress_breasts_base_layer:
    get_outfit_filename("server", breasts=True)
    outfit_primary_colour_transform()
image serverdress_breasts_trim_layer:
    get_outfit_filename("server", breasts=True, base=False)
    outfit_secondary_colour_transform()

image serverdress_belly_base_layer:
    get_outfit_filename("server", preg=True)
    outfit_primary_colour_transform()
image serverdress_belly_trim_layer:
    get_outfit_filename("server", preg=True, base=False)
    outfit_secondary_colour_transform()

layeredimage serverdress_layer:
    always "serverdress_belly_base_layer"
    always "serverdress_belly_trim_layer"
    always "serverdress_breasts_base_layer"
    always "serverdress_breasts_trim_layer"





image serverdress_breasts_base_layer:
    get_outfit_filename("server", breasts=True)
    outfit_primary_colour_transform()
image serverdress_breasts_trim_layer:
    get_outfit_filename("server", breasts=True, base=False)
    outfit_secondary_colour_transform()

image corset_belly_base_layer:
    get_outfit_filename("corset", preg=True, base=False)
    outfit_primary_colour_transform()
image corset_belly_trim_layer:
    get_outfit_filename("corset", preg=True)
    outfit_secondary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("corset", preg=True), "outfit", False)

layeredimage corsetdress_layer:
    always "corset_belly_trim_layer"
    always "corset_belly_base_layer"





image bunnyoutfit_breasts_base:
    get_outfit_filename("bunny", breasts=True)
    outfit_primary_colour_transform()
image bunnyoutfit_base:
    get_outfit_filename("bunny", preg=True)
    outfit_primary_colour_transform()

layeredimage bunnyoutfit_layer:
    always "bunnyoutfit_base"
    always "bunnyoutfit_breasts_base"
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image dungarees_breasts_base_layer:
    get_outfit_filename("dungarees", breasts=True)
    outfit_primary_colour_transform()
image dungarees_breasts_trim_layer:
    get_outfit_filename("dungarees", breasts=True, base=False)
    outfit_secondary_colour_transform()

image dungarees_belly_base_layer:
    get_outfit_filename("dungarees", preg=True, base=False)
    outfit_secondary_colour_transform()
image dungarees_belly_trim_layer:
    get_outfit_filename("dungarees", preg=True)
    outfit_primary_colour_transform()


layeredimage dungarees_layer:

    always "dungarees_belly_trim_layer"
    always "dungarees_belly_base_layer"
    always "dungarees_breasts_base_layer"
    always "dungarees_breasts_trim_layer"





image maid_breasts_base_layer:
    get_outfit_filename("maid", breasts=True)
    outfit_primary_colour_transform()
image maid_breasts_trim_layer:
    get_outfit_filename("maid", breasts=True, base=False)
    outfit_secondary_colour_transform()

image maid_belly_base_layer:
    get_outfit_filename("maid", preg=True)
    outfit_primary_colour_transform()
image maid_belly_trim_layer:
    get_outfit_filename("maid", preg=True, base=False)
    outfit_secondary_colour_transform()


layeredimage maid_outfit_layer:
    always "maid_belly_base_layer"
    always "maid_belly_trim_layer"
    always "maid_breasts_base_layer"
    always "maid_breasts_trim_layer"

    if c.pokenips:
        "outfit_sec_pokenips"
    if player.milky:
        "milkstain"





image puffdress_breasts_base_layer:
    get_outfit_filename("puffdress", breasts=True)
    outfit_primary_colour_transform()
image puffdress_breasts_trim_layer:
    get_outfit_filename("puffdress", breasts=True, base=False)
    outfit_secondary_colour_transform()

image puffdress_belly_base_layer:
    get_outfit_filename("puffdress", preg=True)
    outfit_primary_colour_transform()
image puffdress_belly_trim_layer:
    get_outfit_filename("puffdress", preg=True, base=False)
    outfit_secondary_colour_transform()


layeredimage puffdress_outfit_layer:
    always "puffdress_belly_base_layer"
    always "puffdress_belly_trim_layer"
    always "puffdress_breasts_base_layer"
    always "puffdress_breasts_trim_layer"

    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image paledress_breasts_base:
    get_outfit_filename("paledress", breasts=True)
    outfit_primary_colour_transform()
image paledress_base:
    get_outfit_filename("paledress", preg=True)
    outfit_primary_colour_transform()

layeredimage paledress_layer:
    always "paledress_base"
    always "paledress_breasts_base"
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image frillydress_breasts_base_layer:
    get_outfit_filename("frillydress", breasts=True)
    outfit_primary_colour_transform()
image frillydress_breasts_trim_layer:
    get_outfit_filename("frillydress", breasts=True, base=False)
    outfit_secondary_colour_transform()
image frillydress_breasts_trans_layer:
    "pc_outfit_frillydress_breasts_trans_" + str(player.breasts)
    get_outfit_filename("frillydress", breasts=True, base=False)
    outfit_secondary_colour_transform()
    clothing_alpha_transform("pc_outfit_frillydress_breasts_trans_" + str(player.breasts), "outfit", False)

image frillydress_belly_base_layer:
    get_outfit_filename("frillydress", preg=True)
    outfit_primary_colour_transform()
image frillydress_belly_trim_layer:
    get_outfit_filename("frillydress", preg=True, base=False)
image frillydress_belly_trans_layer:
    "pc_outfit_frillydress_trans"
    outfit_secondary_colour_transform()
    clothing_alpha_transform("pc_outfit_frillydress_trans", "outfit", False)


layeredimage frillydress_outfit_layer:
    always "frillydress_belly_base_layer"
    always "frillydress_belly_trans_layer"
    always "frillydress_belly_trim_layer"

    always "frillydress_breasts_base_layer"
    always "frillydress_breasts_trans_layer"
    always "frillydress_breasts_trim_layer"

    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image frontdress_breasts_base_layer:
    get_outfit_filename("frontdress", breasts=True)
image frontdress_breasts_trim_layer:
    get_outfit_filename("frontdress", breasts=True, base=False)
    outfit_secondary_colour_transform()

image frontdress_belly_base_layer:
    get_outfit_filename("frontdress", preg=True)
image frontdress_belly_trim_layer:
    get_outfit_filename("frontdress", preg=True, base=False)
    outfit_secondary_colour_transform()

layeredimage frontdress_outfit_layerd:
    always "frontdress_belly_base_layer"
    always "frontdress_breasts_base_layer"
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"
image frontdress_outfit_flat:
    Flatten("frontdress_outfit_layerd")

image frontdress_outfit_re:
    "frontdress_outfit_flat"
    outfit_primary_colour_transform()
    clothing_alpha_transform("frontdress_outfit_flat", "outfit")

layeredimage frontdress_outfit_layer:
    always "frontdress_outfit_re"
    always "frontdress_belly_trim_layer"
    always "frontdress_breasts_trim_layer"





image gothdress_breasts_base_layer:
    get_outfit_filename("gothdress", breasts=True)
    outfit_primary_colour_transform()
image gothdress_breasts_trim_layer:
    get_outfit_filename("gothdress", breasts=True, base=False)
    outfit_secondary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("gothdress", breasts=True, base=False), "outfit", False)
image gothdress_breasts_trans_layer:
    "pc_outfit_gothdress_breasts_trans_" + str(player.breasts)
    get_outfit_filename("gothdress", breasts=True, base=False)
    outfit_secondary_colour_transform()
    clothing_alpha_transform("pc_outfit_gothdress_breasts_trans_" + str(player.breasts), "outfit", False)

image gothdress_belly_base_layer:
    get_outfit_filename("gothdress", preg=True)
    outfit_primary_colour_transform()
image gothdress_belly_trim_layer:
    get_outfit_filename("gothdress", preg=True, base=False)
    outfit_secondary_colour_transform()
image gothdress_belly_trans_layer:
    "pc_outfit_gothdress_trans"
    outfit_secondary_colour_transform()
    clothing_alpha_transform("pc_outfit_gothdress_trans", "outfit", False)


layeredimage gothdress_outfit_layer:
    always "gothdress_belly_base_layer"
    always "gothdress_belly_trans_layer"
    always "gothdress_belly_trim_layer"



    always "gothdress_breasts_trim_layer"
    always "gothdress_breasts_base_layer"
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image highlegdress_breasts_base_layer:
    get_outfit_filename("highlegdress", breasts=True)

image highlegdress_belly_base_layer:
    get_outfit_filename("highlegdress", preg=True)

layeredimage highlegdress_layerd:
    always "highlegdress_belly_base_layer"
    always "highlegdress_breasts_base_layer"    
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image highlegdress_flat:
    Flatten("highlegdress_layerd")

image highlegdress_layer:
    outfit_primary_colour_transform()
    clothing_alpha_transform("highlegdress_flat", "outfit")





image cheongsam_breasts_base_layer:
    get_outfit_filename("cheongsam", breasts=True)
    outfit_primary_colour_transform()

image cheongsam_belly_base_layer:
    get_outfit_filename("cheongsam", preg=True)
    outfit_primary_colour_transform()
image cheongsam_belly_trim_layer:
    get_outfit_filename("cheongsam", preg=True, base=False)
    outfit_secondary_colour_transform()

layeredimage cheongsam_layer:
    always "cheongsam_belly_base_layer"
    always "cheongsam_belly_trim_layer"    
    always "cheongsam_breasts_base_layer"   
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image chinesedress_breasts_base_layer:
    get_outfit_filename("chinesedress", breasts=True)
    outfit_primary_colour_transform()
image chinesedress_breasts_trim_layer:
    get_outfit_filename("chinesedress", breasts=True, base=False)
    outfit_secondary_colour_transform()

image chinesedress_belly_base_layer:
    get_outfit_filename("chinesedress", preg=True)
    outfit_primary_colour_transform()
image chinesedress_belly_trim_layer:
    get_outfit_filename("chinesedress", preg=True, base=False)
    outfit_secondary_colour_transform()

layeredimage chinesedress_layerd: 
    always "chinesedress_belly_base_layer"
    always "chinesedress_breasts_base_layer" 
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"

image chinesedress_flat:
    Flatten("chinesedress_layerd")

image chinesedress_alpha:
    clothing_alpha_transform("chinesedress_flat", "outfit")

layeredimage chinesedress_layer:
    always "chinesedress_alpha"
    always "chinesedress_belly_trim_layer"    
    always "chinesedress_breasts_trim_layer"





image nicedress_breasts_base_layer:
    get_outfit_filename("nicedress", breasts=True)
    outfit_primary_colour_transform()
image nicedress_belly_base_layer:
    get_outfit_filename("nicedress", preg=True)
    outfit_primary_colour_transform()

layeredimage nicedress_layer:
    always "nicedress_belly_base_layer"
    always "nicedress_breasts_base_layer"  
    if player.milky:
        "milkstain"  





image deephalter_breasts_base_layer:
    get_outfit_filename("deephalter", breasts=True)


image deephalter_belly_base_layer:
    get_outfit_filename("deephalter", preg=True)



layeredimage deephalter_layerd:
    always "deephalter_belly_base_layer"
    always "deephalter_breasts_base_layer"    
    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image deephalter_flat:
    Flatten("deephalter_layerd")

image deephalter_layer:
    outfit_primary_colour_transform()
    clothing_alpha_transform("deephalter_flat", "outfit")





image waistband_breasts_base_layer:
    get_outfit_filename("waistband", breasts=True)
    outfit_primary_colour_transform()

image waistband_belly_base_layer:
    get_outfit_filename("waistband", preg=True)
    outfit_primary_colour_transform()
image waistband_belly_trim_layer:
    get_outfit_filename("waistband", preg=True, base=False)
    outfit_secondary_colour_transform()

layeredimage waistband_layerd:
    always "waistband_belly_base_layer"
    always "waistband_belly_trim_layer"  
    always "waistband_breasts_base_layer"  






image latexbody_breasts_base_layer:
    get_outfit_filename("bodysuit", breasts=True)
    outfit_primary_colour_transform()

image latexbody_belly_base_layer:
    get_outfit_filename("bodysuit", preg=True)
    outfit_primary_colour_transform()

image latexbody_larm_layer:
    DynamicDisplayable(get_outfit_displayable, "bodysuit", arm="larm")
    outfit_primary_colour_transform()
image latexbody_larm_above_layer:
    "pc_outfit_bodysuit_larm_coverabove_base"
    outfit_primary_colour_transform()

image latexbody_rarm_layer:
    DynamicDisplayable(get_outfit_displayable, "bodysuit", arm="rarm")
    outfit_primary_colour_transform()

layeredimage latexbody_layered:
    always "latexbody_belly_base_layer"
    always "latexbody_breasts_base_layer"    
    if c.pokenips:
        "outfit_pokenips"
    always "pc_outfit_bodysuit_shine"





image latexdress_breasts_base_layer:
    get_outfit_filename("latexdress", breasts=True)
    outfit_primary_colour_transform()

image latexdress_belly_base_layer:
    get_outfit_filename("latexdress", preg=True)
    outfit_primary_colour_transform()

layeredimage latexdress_layered:
    always "latexdress_belly_base_layer"
    always "latexdress_breasts_base_layer"    
    if c.pokenips:
        "outfit_pokenips"
    always "pc_outfit_latexdress_shine"





image latexwindow_breasts_base_layer:
    get_outfit_filename("latexwindow", breasts=True)
    outfit_primary_colour_transform()

image latexwindow_belly_base_layer:
    get_outfit_filename("latexwindow", preg=True)
    outfit_primary_colour_transform()

layeredimage latexwindow_layered:
    always "latexwindow_belly_base_layer"
    always "latexwindow_breasts_base_layer"    
    if c.pokenips:
        "outfit_pokenips"
    always "pc_outfit_latexwindow_shine"





image teestrap_breasts_base_layer:
    get_outfit_filename("teestrap", breasts=True)
    outfit_secondary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("teestrap", breasts=True), "outfit", is_primary=False)
image teestrap_breasts_trim_layer:
    get_outfit_filename("teestrap", base=False, breasts=True)
    outfit_primary_colour_transform()

image teestrap_belly_trim_layer:
    get_outfit_filename("teestrap", base=False, preg=True)
    outfit_primary_colour_transform()

layeredimage teestrapdress_layered:
    always "teestrap_belly_trim_layer"
    always "teestrap_breasts_base_layer"
    always "teestrap_breasts_trim_layer"    
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image highleggown_breasts_base_layer:
    get_outfit_filename("highleggown", breasts=True)
    outfit_primary_colour_transform()

image highleggown_belly_trim_layer:
    get_outfit_filename("highleggown", preg=True)
    outfit_primary_colour_transform()


image highleggown_larm_layerd:
    DynamicDisplayable(get_top_displayable, "perry", arm="larm")
    outfit_primary_colour_transform()
image highleggown_larm_above_layered:
    "pc_top_perry_larm_coverabove_base"
    outfit_primary_colour_transform()

image highleggown_rarm_layerd:
    DynamicDisplayable(get_top_displayable, "perry", arm="rarm")
    outfit_primary_colour_transform()

layeredimage highleggown_layered:
    always "highleggown_belly_trim_layer"
    always "highleggown_breasts_base_layer"    
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image crumpdress_base_layer:
    get_outfit_filename("crumpdress", preg=True)
    outfit_primary_colour_transform()

image crumpdress_breasts_base_layer:
    get_outfit_filename("crumpdress", breasts=True)
    outfit_primary_colour_transform()
image crumpdress_breasts_trim_layer:
    get_outfit_filename("crumpdress", breasts=True, base=False)
    outfit_secondary_colour_transform()
image crumpdress_nip_sec:
    AlphaMask("outfit_sec_pokenips", get_outfit_filename("crumpdress", breasts=True, base=False))

layeredimage crumpdress_layered:
    always "crumpdress_base_layer" 
    always "crumpdress_breasts_base_layer"
    if c.pokenips:
        "outfit_pokenips"
    always "crumpdress_breasts_trim_layer"   
    if c.pokenips:
        "crumpdress_nip_sec"
    if player.milky:
        "milkstain"





image romper_base_layer:
    get_outfit_filename("romper", preg=True)
    outfit_primary_colour_transform()
image romper_breasts_base_layer:
    get_outfit_filename("romper", breasts=True)
    outfit_primary_colour_transform()


layeredimage romper_layered:
    always "romper_base_layer" 
    always "romper_breasts_base_layer"
    if c.pokenips:
        "outfit_pokenips"
    if player.milky:
        "milkstain"





image ruffpj_breasts_base_layer:
    get_outfit_filename("ruffpj", breasts=True)
    outfit_secondary_colour_transform()
image ruffpj_breasts_trim_layer:
    get_outfit_filename("ruffpj", base=False, breasts=True)
    outfit_primary_colour_transform()

image pc_outfit_ruffpjskirt_base_1 = "pc_outfit_ruffpjskirt_base_0"
image pc_outfit_ruffpjskirt_trim_1 = "pc_outfit_ruffpjskirt_trim_0"

image ruffpj_skirt_base_layer:
    get_outfit_filename("ruffpjskirt", preg=True)
    outfit_secondary_colour_transform()
image ruffpj_skirt_trim_layer:
    get_outfit_filename("ruffpjskirt", base=False, preg=True)
    outfit_primary_colour_transform()

image ruffpj_body_layer:
    get_outfit_filename("ruffpj", preg=True)
    outfit_secondary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("ruffpj", preg=True), "outfit")

layeredimage ruffpj_layered:
    always "ruffpj_body_layer"
    always "ruffpj_skirt_base_layer"
    always "ruffpj_skirt_trim_layer"    
    always "ruffpj_breasts_base_layer"
    always "ruffpj_breasts_trim_layer"    





image rompersq_breasts_base_layer:
    get_outfit_filename("rompersq", breasts=True)
    outfit_primary_colour_transform()

image rompersq_skirt_base_layer:
    get_outfit_filename("rompersq", preg=True)
    outfit_primary_colour_transform()

image rompersq_larm_layer:
    DynamicDisplayable(get_outfit_displayable, "rompersq", arm="larm")
    outfit_primary_colour_transform()
image rompersq_larm_above_layer:
    "pc_outfit_rompersq_larm_coverabove_base"
    outfit_primary_colour_transform()
image rompersq_rarm_layer:
    DynamicDisplayable(get_outfit_displayable, "rompersq", arm="rarm")
    outfit_primary_colour_transform()

layeredimage rompersq_layered:
    always "rompersq_skirt_base_layer"
    always "rompersq_breasts_base_layer"
    if c.pokenips:
        "outfit_pokenips"  
    if player.milky:
        "milkstain"





image romperv_breasts_base_layer:
    get_outfit_filename("romperv", breasts=True)
    outfit_primary_colour_transform()
image romperv_breasts_trim_layer:
    get_outfit_filename("romperv", base=False, breasts=True)
    outfit_secondary_colour_transform()

image romperv_skirt_base_layer:
    get_outfit_filename("romperv", preg=True)
    outfit_primary_colour_transform()

layeredimage romperv_layered:
    always "romperv_skirt_base_layer"
    always "romperv_breasts_base_layer"
    always "romperv_breasts_trim_layer"





image knitdress_breasts_base_layer:
    get_outfit_filename("knitdress", breasts=True)
    outfit_primary_colour_transform()

image knitdress_skirt_base_layer:
    get_outfit_filename("knitdress", preg=True)
    outfit_primary_colour_transform()

layeredimage knitdress_layer:
    always "knitdress_skirt_base_layer"
    always "knitdress_breasts_base_layer"

    if c.pokenips:
        "pokenips"
    if player.milky:
        "milkstain"

image knitdress_flat:
    Flatten("knitdress_layer")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
