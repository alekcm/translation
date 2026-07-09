



image trousers:
    get_bottom_filename("trousers", preg=True)
    bottom_primary_colour_transform()





image skirtpleat:
    get_bottom_filename("skirtpleat", preg=True)
    bottom_primary_colour_transform()





image skirtstraight:
    get_bottom_filename("skirtstraight", preg=True)
    bottom_primary_colour_transform()





image skirtflared:
    get_bottom_filename("skirtflared", preg=True)
    bottom_primary_colour_transform()





image yoga_base:
    get_bottom_filename("yoga", preg=True)
    bottom_secondary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("yoga", preg=True), "bottom", False)

image yoga_trim:
    get_bottom_filename("yoga", preg=True, base=False)
    bottom_primary_colour_transform()

layeredimage yoga_layer:
    always:
        "yoga_base"
    always:
        "yoga_trim"





image pc_bottom_vball_trim_1 = "pc_bottom_vball_trim_0"
image pc_bottom_vball_trim_3 = "pc_bottom_vball_trim_2"
image pc_bottom_vball_base_1 = "pc_bottom_vball_base_0"

image vballshorts_base:
    get_bottom_filename("vball", preg=True)
    bottom_primary_colour_transform()

image vballshorts_trim:
    get_bottom_filename("vball", preg=True, base=False)
    bottom_secondary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("vball", preg=True, base=False), "bottom", False)

layeredimage vballshorts_layer:
    always:
        "vballshorts_trim"
    always:
        "vballshorts_base"





image pc_bottom_haven_base_1 = "pc_bottom_haven_base_0"
image pc_bottom_haven_trim_1 = "pc_bottom_haven_trim_0"

image havenshorts_base:
    get_bottom_filename("haven", preg=True)
    bottom_primary_colour_transform()

image havenshorts_trim:
    get_bottom_filename("haven", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage havenshorts_layer:
    always:
        "havenshorts_base"
    always:
        "havenshorts_trim"






image pc_bottom_microbikini_base_1 = "pc_bottom_microbikini_base_0"
image pc_bottom_microbikini_trim_1 = "pc_bottom_microbikini_trim_0"

image microbikini_base:
    get_bottom_filename("microbikini", preg=True)
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("microbikini", preg=True), "bottom")

image microbikini_trim:
    get_bottom_filename("microbikini", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage microbikini_bottom_layer:

    always:
        "microbikini_base"
    always:
        "microbikini_trim"





image knotbikini_bottom:
    get_bottom_filename("knotbikini")
    bottom_primary_colour_transform()





image stringbikini_base:
    get_bottom_filename("stringbikini")
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("stringbikini"), "bottom", True)

image stringbikini_trim:
    get_bottom_filename("stringbikini", base=False)

layeredimage stringbikini_bottom_layer:

    always:
        "stringbikini_base"
    always:
        "stringbikini_trim"





image micromini_layer:
    get_bottom_filename("micromini", preg=True)
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("micromini", preg=True), "bottom", True)





image straptrousers_layer:
    get_bottom_filename("straptrousers", preg=True)
    bottom_primary_colour_transform()





image dancemini_layer:
    get_bottom_filename("danceskirt", preg=True)
    bottom_primary_colour_transform()





image rags_bottom:
    get_bottom_filename("rags")
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("rags"), "bottom")




image pleatmini_base:
    get_bottom_filename("rmini", preg=True)
    bottom_primary_colour_transform()

image pleatmini_trim:
    get_bottom_filename("rmini", preg=True, base=False)
    bottom_secondary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("rmini", preg=True, base=False), "bottom", False)

layeredimage pleatmini_layer:
    always "pleatmini_trim"
    always "pleatmini_base"





image pc_bottom_shortshorts_base_1 = "pc_bottom_shortshorts_base_0"

image shortshorts_layer:
    get_bottom_filename("shortshorts", preg=True)
    bottom_primary_colour_transform()





image flaredshorts_layer:
    get_bottom_filename("flaredshorts", preg=True)
    bottom_primary_colour_transform()





image pc_bottom_jeanshorts_base_1 = "pc_bottom_jeanshorts_base_0"
image pc_bottom_jeanshorts_trim_1 = "pc_bottom_jeanshorts_trim_0"
image jeantorn_base:
    get_bottom_filename("jeanshorts", preg=True)
    bottom_primary_colour_transform()

image jeantorn_trim:
    get_bottom_filename("jeanshorts", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage jeantorn_layer:
    always "jeantorn_base"
    always "jeantorn_trim"





image frillskirt_base:
    get_bottom_filename("frillskirt", preg=True)
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("frillskirt", preg=True), "bottom")
image frillskirt_trim:
    get_bottom_filename("frillskirt", preg=True, base=False)
    bottom_secondary_colour_transform()
image frillskirt_frill:
    "pc_bottom_frillskirt_frill"
    bottom_secondary_colour_transform()
    clothing_alpha_transform("pc_bottom_frillskirt_frill", "bottom", False)

layeredimage frillskirt_layer:
    always "frillskirt_frill"
    always "frillskirt_base"
    always "frillskirt_trim"





image highskirt_base:
    get_bottom_filename("highskirt", preg=True)
    bottom_primary_colour_transform()





image heartpatch_bottom_base:
    get_bottom_filename("heartpatch", preg=True)
    bottom_primary_colour_transform()

image heartpatch_bottom_trim:
    get_bottom_filename("heartpatch", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage heartpatch_layer:
    always "heartpatch_bottom_base"
    always "heartpatch_bottom_trim"





image harlequin_bottom_base:
    get_bottom_filename("harlequin", preg=True)
    bottom_primary_colour_transform()

image harlequin_bottom_trim:
    get_bottom_filename("harlequin", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage harlequin_bottom_layer:
    always "harlequin_bottom_base"
    always "harlequin_bottom_trim"





image pc_bottom_hipjeans_base_1 = "pc_bottom_hipjeans_base_0"
image pc_bottom_hipjeans_trim_1 = "pc_bottom_hipjeans_trim_0"

image hipjeans_base:
    get_bottom_filename("hipjeans", preg=True)
    bottom_primary_colour_transform()

image hipjeans_trim:
    get_bottom_filename("hipjeans", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage hipjeans_layer:
    always "hipjeans_base"
    always "hipjeans_trim"





image pc_bottom_rippedhipjeans_base_1 = "pc_bottom_rippedhipjeans_base_0"
image pc_bottom_rippedhipjeans_trim_1 = "pc_bottom_rippedhipjeans_trim_0"

image rippedhipjeans_base:
    get_bottom_filename("rippedhipjeans", preg=True)
    bottom_primary_colour_transform()

image rippedhipjeans_trim:
    get_bottom_filename("rippedhipjeans", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage rippedhipjeans_layer:
    always "rippedhipjeans_base"
    always "rippedhipjeans_trim"





image rippedskirt_layer:
    get_bottom_filename("rippedskirt")
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("rippedskirt"), "bottom")




image pc_bottom_sweatpants_base_1 = "pc_bottom_sweatpants_base_0"
image pc_bottom_sweatpants_trim_1 = "pc_bottom_sweatpants_trim_0"

image sweatpants_base:
    get_bottom_filename("sweatpants", preg=True)
    bottom_primary_colour_transform()

image sweatpants_trim:
    get_bottom_filename("sweatpants", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage sweatpants_layer:
    always "sweatpants_base"
    always "sweatpants_trim"





image sweatshorts_base:
    get_bottom_filename("sweatshorts", preg=True)
    bottom_primary_colour_transform()

image sweatshorts_trim:
    get_bottom_filename("sweatshorts", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage sweatshorts_layer:
    always "sweatshorts_base"
    always "sweatshorts_trim"





image pc_bottom_micromini2_base_1 = "pc_bottom_micromini2_base_0"
image pc_bottom_micromini2_base_2 = "pc_bottom_micromini2_base_0"

image micromini2_layer:
    get_bottom_filename("micromini2", preg=True)
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("micromini2", preg=True), "bottom")





image sweatpantsband_base:
    get_bottom_filename("sweatpantsband", preg=True)
    bottom_primary_colour_transform()


image sweatpantsband_trim:
    get_bottom_filename("sweatpantsband", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage sweatpantsband_layer:
    always "sweatpantsband_base"
    always "sweatpantsband_trim"





image minitight_base:
    get_bottom_filename("minitight", preg=True)
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("minitight", preg=True), "bottom")

image minitight_trim:
    get_bottom_filename("minitight", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage minitight_layer:
    always "minitight_base"
    always "minitight_trim"





image pc_bottom_latextrou_base_1 = "pc_bottom_latextrou_base_0"
image latextrou_base:
    get_bottom_filename("latextrou", preg=True)
    bottom_primary_colour_transform()


layeredimage latextrou_layered:
    always "latextrou_base"
    always "pc_bottom_latextrou_shine"





image jayshorts_base:
    get_bottom_filename("jayshorts", preg=True)
    bottom_primary_colour_transform()


image jayshorts_trim:
    get_bottom_filename("jayshorts", preg=True, base=False)
    bottom_secondary_colour_transform()

layeredimage jayshorts_layer:
    always "jayshorts_base"
    always "jayshorts_trim"





image knot_base:
    get_bottom_filename("knot", preg=True)
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_bottom_filename("knot", preg=True), "bottom")
image knot_trim:
    get_bottom_filename("knot", preg=True, base=False)
    bottom_primary_colour_transform()

image pc_bottom_knot_base_1 = "pc_bottom_knot_base_0"
image pc_bottom_knot_trim_1 = "pc_bottom_knot_trim_0"

layeredimage knotskirt_layer:
    always "knot_base"
    always "knot_trim"





image ruffskirt_base:
    get_outfit_filename("ruffpjskirt", preg=True)
    bottom_primary_colour_transform()
    clothing_alpha_transform(get_outfit_filename("ruffpjskirt", preg=True), "bottom")
image ruffskirt_trim:
    get_outfit_filename("ruffpjskirt", base=False, preg=True)
    bottom_secondary_colour_transform()

layeredimage ruffskirt_layer:
    always "ruffskirt_base"
    always "ruffskirt_trim"





image santa_skirt_base:
    get_bottom_filename("santa", preg=True)
    bottom_primary_colour_transform()
image santa_skirt_trim:
    get_bottom_filename("santa", base=False, preg=True)
    bottom_secondary_colour_transform()

layeredimage santa_skirt_layer:
    always "santa_skirt_base"
    always "santa_skirt_trim"






image bloomers_base:
    get_bottom_filename("bloomers", preg=True)
    bottom_primary_colour_transform()





image trousers_stripe_base:
    get_bottom_filename("trousers_stripe", preg=True)
    bottom_primary_colour_transform()





image yogashorts_base:
    get_bottom_filename("yogashorts", preg=True)
    bottom_primary_colour_transform()
image yogashorts_trim:
    get_bottom_filename("yogashorts", base=False, preg=True)
    bottom_secondary_colour_transform()

layeredimage yogashorts_layer:
    always "yogashorts_base"
    always "yogashorts_trim"





image shortscut_base:
    get_bottom_filename("shortscut", preg=True)
    bottom_primary_colour_transform()
image shortscut_trim:
    get_bottom_filename("shortscut", base=False, preg=True)
    bottom_secondary_colour_transform()

layeredimage shortscut_layer:
    always "shortscut_base"
    always "shortscut_trim"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
