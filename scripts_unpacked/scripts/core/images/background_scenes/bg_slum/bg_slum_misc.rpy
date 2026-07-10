image bg_walk_slum_pipe:
    "bg_slum_pipe"

image bg_highway_slum_street_image:
    get_background_filename("highway_slum_street", True, False)

layeredimage bg_highway_slum_street_layer:
    always "bg_highway_slum_street_image"
    if t.hour in irange(10, 19):
        "bg_highway_slum_street_people_girlleft"
    if t.hour in irange(13, 22):
        "bg_highway_slum_street_people_girlright"
    if neighbour_here():
        "bg_highway_slum_street_people_neigh"

image bg_highway_slum_street:
    "bg_highway_slum_street_layer"
    bg_tint_transform()

layeredimage bg_highway_slum_still:
    always "bg_slum_still_image"
    if loc_highway_slum_still.open() and not renpy.showing("haven_viktor"):
        "bg_slum_still_people_viktor"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
