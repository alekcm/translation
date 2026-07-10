



image bra_fcup_trim:
    get_bra_filename("fcup", breasts=True, base=False)
    bra_secondary_colour_transform()


image bra_fcup_base:
    get_bra_filename("fcup", breasts=True)
    bra_primary_colour_transform()
    clothing_alpha_transform(get_bra_filename("fcup", breasts=True), "bra")

layeredimage fcup_layer:

    always "bra_fcup_base"
    always "bra_fcup_trim"
    if player.milky:
        "milkstain"





image bra_sport1_trim:
    get_bra_filename("sport1", breasts=True, base=False)
    bra_secondary_colour_transform()

image bra_sport1_base:
    get_bra_filename("sport1", breasts=True)
    bra_primary_colour_transform()

image bra_sport1_trans:
    get_bra_filename("sport1", breasts=True, base="trans")
    bra_primary_colour_transform()
    clothing_alpha_transform(get_bra_filename("sport1", breasts=True, base="trans"), "bra")

layeredimage sport1_layer:
    always "bra_sport1_trans"
    always "bra_sport1_base"
    always "bra_sport1_trim"
    if player.milky:
        "milkstain"





image bra_sport2_trim:
    get_bra_filename("sport2", breasts=True, base=False)
    bra_secondary_colour_transform()

image bra_sport2_base:
    get_bra_filename("sport2", breasts=True)
    bra_primary_colour_transform()

layeredimage sport2_layer:

    always "bra_sport2_base"
    always "bra_sport2_trim"
    if player.milky:
        "milkstain"





image bra_strapless_trim:
    get_bra_filename("strapless", breasts=True, base=False)
    bra_secondary_colour_transform()

image bra_strapless_base:
    get_bra_filename("strapless", breasts=True)
    bra_primary_colour_transform()

layeredimage strapless_layer:

    always "bra_strapless_base"
    always "bra_strapless_trim"
    if player.milky:
        "milkstain"





image bra_shelf_trim:
    get_bra_filename("shelf", breasts=True, base=False)
    bra_secondary_colour_transform()

image bra_shelf_base:
    get_bra_filename("shelf", breasts=True)
    bra_primary_colour_transform()
    clothing_alpha_transform(get_bra_filename("shelf", breasts=True), "bra")

layeredimage shelf_layer:

    always "bra_shelf_base"
    always "bra_shelf_trim"






image open_bra_base:
    get_bra_filename("open", breasts=True)
    bra_primary_colour_transform()
    clothing_alpha_transform(get_bra_filename("open", breasts=True), "bra")
image open_bra_trim:
    get_bra_filename("open", breasts=True, base=False)
    bra_secondary_colour_transform()


layeredimage open_bra_layer:
    always "open_bra_base"
    always "open_bra_trim"






image stringfront_layer_image:
    get_bra_filename("stringfront", breasts=True)
    bra_primary_colour_transform()
    clothing_alpha_transform(get_bra_filename("stringfront", breasts=True), "bra")

layeredimage stringfront_layer:
    always "stringfront_layer_image"
    if player.milky:
        "milkstain"





image wrap_bra_image:
    get_bra_filename("wrap", breasts=True)
    bra_primary_colour_transform()

layeredimage wrap_bra_layer:
    always "wrap_bra_image"
    if player.milky:
        "milkstain"




image frilly_bra_base:
    get_bra_filename("frilly", breasts=True)
    bra_primary_colour_transform()
image frilly_bra_trim:
    get_bra_filename("frilly", breasts=True, base=False)
    bra_secondary_colour_transform()


layeredimage frilly_bra_layer:
    always "frilly_bra_base"
    if player.milky:
        "milkstain"
    always "frilly_bra_trim"






image triangle_bra_base:
    get_bra_filename("triangle", breasts=True)
    bra_primary_colour_transform()
    clothing_alpha_transform(get_bra_filename("triangle", breasts=True), "bra")
image triangle_bra_trim:
    get_bra_filename("triangle", breasts=True, base=False)
    bra_secondary_colour_transform()


layeredimage triangle_bra_layer:
    always "triangle_bra_base"
    always "triangle_bra_trim"
    if player.milky:
        "milkstain"





image simple_bra_base:
    get_bra_filename("simple", breasts=True)
    bra_primary_colour_transform()
    clothing_alpha_transform(get_bra_filename("simple", breasts=True), "bra")
image simple_bra_trim:
    get_bra_filename("simple", breasts=True, base=False)
    bra_secondary_colour_transform()


layeredimage simple_bra_layer:
    always "simple_bra_base"
    always "simple_bra_trim"
    if player.milky:
        "milkstain"





image half_bra_base:
    get_bra_filename("half", breasts=True)
    bra_primary_colour_transform()
    clothing_alpha_transform(get_bra_filename("half", breasts=True), "bra")
image half_bra_trim:
    get_bra_filename("half", breasts=True, base=False)
    bra_secondary_colour_transform()


layeredimage half_bra_layer:
    always "half_bra_base"
    always "half_bra_trim"
    if player.milky:
        "milkstain"





image cow_bra_base:
    get_bra_filename("cow", breasts=True)
    bra_primary_colour_transform()
image cow_bra_trim:
    get_bra_filename("cow", breasts=True, base=False)
    bra_secondary_colour_transform()


layeredimage cow_bra_layer:
    always "cow_bra_base"
    always "cow_bra_trim"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
