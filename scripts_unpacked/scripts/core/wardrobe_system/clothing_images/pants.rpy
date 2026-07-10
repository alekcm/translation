image pc_pants_briefs1_base_1 = "pc_pants_briefs1_base_0"
image pc_pants_briefs1_trim_1 = "pc_pants_briefs1_trim_0"
image pc_pants_briefs2_trim_1 = "pc_pants_briefs2_trim_0"

image briefs1_base:
    get_clothing_filename("briefs1", "pants", preg=True)
    pants_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("briefs1", "pants", preg=True), "pants", True)
image briefs1_trim:
    get_clothing_filename("briefs1", "pants", is_base=False, preg=True)
    pants_secondary_colour_transform()
image briefs2_trim:
    get_clothing_filename("briefs2", "pants", is_base=False, preg=True)
    pants_secondary_colour_transform()

image pc_pants_briefs3_base_1 = "pc_pants_briefs3_base_0"
image pc_pants_briefs3_trim_1 = "pc_pants_briefs3_trim_0"
image briefs3_base:
    get_clothing_filename("briefs3", "pants", preg=True)
    pants_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("briefs3", "pants", preg=True), "pants", True)

image briefs3_trim:
    get_clothing_filename("briefs3", "pants", is_base=False, preg=True)
    pants_secondary_colour_transform()

layeredimage briefs1_layer:

    always:
        "briefs1_base"
    always:
        "briefs1_trim"
layeredimage briefs2_layer:

    always:
        "briefs1_base"
    always:
        "briefs2_trim"
layeredimage briefs3_layer:

    always:
        "briefs3_base"
    always:
        "briefs3_trim"

image french_base:
    get_clothing_filename("french", "pants", preg=True)
    pants_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("french", "pants", preg=True), "pants", True)
image french_trim:
    get_clothing_filename("french", "pants", is_base=False, preg=True)
    pants_secondary_colour_transform()

layeredimage french_layer:

    always:
        "french_base"
    always:
        "french_trim"

image pc_pants_thong1_base_1 = "pc_pants_thong1_base_0"
image pc_pants_thong1_base_2 = "pc_pants_thong1_base_0"
image pc_pants_thong1_trim_1 = "pc_pants_thong1_trim_0"
image pc_pants_thong1_trim_2 = "pc_pants_thong1_trim_0"

image thong1_base:
    get_clothing_filename("thong1", "pants", preg=True)
    pants_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("thong1", "pants", preg=True), "pants", True)
image thong1_trim:
    get_clothing_filename("thong1", "pants", is_base=False, preg=True)
    pants_secondary_colour_transform()

layeredimage thong1_layer:

    always:
        "thong1_base"
    always:
        "thong1_trim"





image pc_pants_bargirl_base_1 = "pc_pants_bargirl_base_0"

image bargirl_pants_layer:
    get_clothing_filename("bargirl", "pants", preg=True)
    pants_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("bargirl", "pants", preg=True), "pants", True)




image pc_pants_rthong_trim_3 = "pc_pants_rthong_trim_2"
image stripthong_base:
    get_clothing_filename("rthong", "pants", preg=True)
    pants_primary_colour_transform()
image stripthong_trim:
    get_clothing_filename("rthong", "pants", is_base=False, preg=True)
    pants_secondary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("rthong", "pants", is_base=False, preg=True), "pants", False)

layeredimage stripthong_layer:
    always "stripthong_base"
    always "stripthong_trim"





image pc_pants_highleg_base_1 = "pc_pants_highleg_base_0"
image pc_pants_highleg_trim_1 = "pc_pants_highleg_trim_0"

image highleg_base:
    get_clothing_filename("highleg", "pants", preg=True)
    pants_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("highleg", "pants", preg=True), "pants")
image highleg_trim:
    get_clothing_filename("highleg", "pants", is_base=False, preg=True)
    pants_secondary_colour_transform()


layeredimage highleg_layer:
    always "highleg_base"
    always "highleg_trim"





image pc_pants_open_trim_1 = "pc_pants_open_trim_0"
image pc_pants_open_base_1 = "pc_pants_open_base_0"
image open_pants_base:
    get_clothing_filename("open", "pants", preg=True)
    pants_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("open", "pants", preg=True), "pants")
image open_pants_trim:
    get_clothing_filename("open", "pants", preg=True, is_base=False)
    pants_secondary_colour_transform()


layeredimage open_pants_layer:
    always "open_pants_base"
    always "open_pants_trim"





image lowride_pants_base:
    "pc_pants_lowride_base"
    pants_primary_colour_transform()
    clothing_alpha_transform("pc_pants_lowride_base", "pants")
image lowride_pants_trim:
    "pc_pants_lowride_trim"
    pants_secondary_colour_transform()

layeredimage lowride_pants_layer:
    always "lowride_pants_base"
    always "lowride_pants_trim"





image cstring_layer:
    get_clothing_filename("cstring", "pants", preg=False)
    pants_primary_colour_transform()




image pc_pants_crossstring_base_1 = "pc_pants_crossstring_base_0"
image crossstring_layer:
    get_clothing_filename("crossstring", "pants", preg=True)
    pants_primary_colour_transform()




image pc_pants_maid_base_1 = "pc_pants_maid_base_0"
image pc_pants_maid_base_2 = "pc_pants_maid_base_0"
image pc_pants_maid_trim_1 = "pc_pants_maid_trim_0"
image pc_pants_maid_trim_2 = "pc_pants_maid_trim_0"
image pc_pants_maid_trans_1 = "pc_pants_maid_trans_0"
image pc_pants_maid_trans_2 = "pc_pants_maid_trans_0"

image maid_pants_base:
    get_clothing_filename("maid", "pants", preg=True)
    pants_secondary_colour_transform()
image maid_pants_trim:
    get_clothing_filename("maid", "pants", is_base=False, preg=True)
    pants_primary_colour_transform()
image maid_pants_trans:
    get_clothing_filename("maid", "pants", is_base="trans", preg=True)
    pants_primary_colour_transform()
    clothing_alpha_transform(get_clothing_filename("maid", "pants", is_base="trans", preg=True), "pants")

layeredimage maid_pants_layer:
    always "maid_pants_trans"
    always "maid_pants_base"
    always "maid_pants_trim"





image wrap_pants_base:
    get_clothing_filename("wrap", "pants", preg=True)
    pants_primary_colour_transform()
image wrap_pants_trim:
    get_clothing_filename("wrap", "pants", preg=True, is_base=False)
    pants_secondary_colour_transform()

layeredimage wrap_pants_layer:
    always "wrap_pants_base"
    always "wrap_pants_trim"




image pc_pants_strappy_base_1 = "pc_pants_strappy_base_0"
image pc_pants_strappy_trim_1 = "pc_pants_strappy_trim_0"
image strappy_pants_base:
    get_clothing_filename("strappy", "pants", preg=True)
    pants_primary_colour_transform()
image strappy_pants_trim:
    get_clothing_filename("strappy", "pants", preg=True, is_base=False)
    pants_secondary_colour_transform()

layeredimage strappy_pants_layer:
    always "strappy_pants_base"
    always "strappy_pants_trim"





image cow_pants_base:
    get_clothing_filename("cow", "pants")
    pants_primary_colour_transform()
image cow_pants_trim:
    get_clothing_filename("cow", "pants", is_base=False)
    pants_secondary_colour_transform()

layeredimage cow_pants_layer:
    always "cow_pants_base"
    always "cow_pants_trim"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
