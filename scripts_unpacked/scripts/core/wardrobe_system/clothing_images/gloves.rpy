init python:
    def get_gloves_displayable(st, at, name, **kwargs):
        
        return (get_gloves_filename(name, **kwargs), None)

image fingerless_gloves_r_base:
    DynamicDisplayable(get_gloves_displayable, "fingerless", arm="rarm",)
    gloves_primary_colour_transform()

image fingerless_gloves_r_trim:
    DynamicDisplayable(get_gloves_displayable, "fingerless", arm="rarm", base=False)
    gloves_secondary_colour_transform()

image fingerless_gloves_l_base:
    DynamicDisplayable(get_gloves_displayable, "fingerless", arm="larm",)
    gloves_primary_colour_transform()

image fingerless_gloves_l_trim:
    DynamicDisplayable(get_gloves_displayable, "fingerless", arm="larm", base=False)
    gloves_secondary_colour_transform()

image fingerless_gloves_l_above_base:
    DynamicDisplayable(get_gloves_displayable, "fingerless", arm="larm", gloves=True)

    gloves_primary_colour_transform()

image fingerless_gloves_l_above_trim:
    DynamicDisplayable(get_gloves_displayable, "fingerless", arm="larm", gloves=True, base=False)

    gloves_secondary_colour_transform()

layeredimage fingerless_gloves_r_layer:
    always "fingerless_gloves_r_base"
    always "fingerless_gloves_r_trim"

layeredimage fingerless_gloves_l_layer:
    always "fingerless_gloves_l_base"
    always "fingerless_gloves_l_trim"

layeredimage fingerless_gloves_l_above_layer:
    always "fingerless_gloves_l_above_base"
    always "fingerless_gloves_l_above_trim"


image sleeve_gloves_r_base:
    DynamicDisplayable(get_gloves_displayable, "sleeve", arm="rarm")
    gloves_primary_colour_transform()

image sleeve_gloves_r_trim:
    DynamicDisplayable(get_gloves_displayable, "sleeve", arm="rarm", base=False)
    gloves_secondary_colour_transform()

image sleeve_gloves_l_base:
    DynamicDisplayable(get_gloves_displayable, "sleeve", arm="larm")
    gloves_primary_colour_transform()

image sleeve_gloves_l_trim:
    DynamicDisplayable(get_gloves_displayable, "sleeve", arm="larm", base=False)
    gloves_secondary_colour_transform()

image sleeve_gloves_l_above_base:
    DynamicDisplayable(get_gloves_displayable, "sleeve", arm="larm", gloves=True)
    gloves_primary_colour_transform()

image sleeve_gloves_l_above_trim:
    DynamicDisplayable(get_gloves_displayable, "sleeve", arm="larm", base=False, gloves=True)
    gloves_secondary_colour_transform()

layeredimage sleeve_gloves_r_layer:
    always "sleeve_gloves_r_base"
    always "sleeve_gloves_r_trim"

layeredimage sleeve_gloves_l_layer:
    always "sleeve_gloves_l_base"
    always "sleeve_gloves_l_trim"

layeredimage sleeve_gloves_l_above_layer:
    always "sleeve_gloves_l_above_base"
    always "sleeve_gloves_l_above_trim"

image server_gloves_r_base:
    DynamicDisplayable(get_gloves_displayable, "server", arm="rarm")
    gloves_primary_colour_transform()

image server_gloves_r_trim:
    DynamicDisplayable(get_gloves_displayable, "server", arm="rarm", base=False)
    gloves_secondary_colour_transform()

image server_gloves_l_base:
    DynamicDisplayable(get_gloves_displayable, "server", arm="larm")
    gloves_primary_colour_transform()

image server_gloves_l_trim:
    DynamicDisplayable(get_gloves_displayable, "server", arm="larm", base=False)
    gloves_secondary_colour_transform()

image server_gloves_l_above_base:
    DynamicDisplayable(get_gloves_displayable, "server", arm="larm")
    gloves_primary_colour_transform()

image server_gloves_l_above_trim:
    DynamicDisplayable(get_gloves_displayable, "server", arm="larm", base=False)
    gloves_secondary_colour_transform()

layeredimage server_gloves_r_layer:
    always "server_gloves_r_base"
    always "server_gloves_r_trim"

layeredimage server_gloves_l_layer:
    always "server_gloves_l_base"
    always "server_gloves_l_trim"

layeredimage server_gloves_l_above_layer:
    always "server_gloves_l_above_base"
    always "server_gloves_l_above_trim"





image rubber_gloves_r:
    DynamicDisplayable(get_gloves_displayable, "rubber", arm="rarm")
    gloves_primary_colour_transform()

image rubber_gloves_l:
    DynamicDisplayable(get_gloves_displayable, "rubber", arm="larm")
    gloves_primary_colour_transform()

image rubber_gloves_l_above:
    DynamicDisplayable(get_gloves_displayable, "rubber", arm="larm", gloves=True)
    gloves_primary_colour_transform()






image pads_gloves_r_base:
    DynamicDisplayable(get_gloves_displayable, "pads", arm="rarm")
    gloves_primary_colour_transform()

image pads_gloves_r_trim:
    DynamicDisplayable(get_gloves_displayable, "pads", arm="rarm", base=False)
    gloves_secondary_colour_transform()

image pads_gloves_l_base:
    DynamicDisplayable(get_gloves_displayable, "pads", arm="larm")
    gloves_primary_colour_transform()

image pads_gloves_l_trim:
    DynamicDisplayable(get_gloves_displayable, "pads", arm="larm", base=False)
    gloves_secondary_colour_transform()

image pads_gloves_l_above_base:
    DynamicDisplayable(get_gloves_displayable, "pads", arm="larm")
    gloves_primary_colour_transform()
image pads_gloves_l_above_trim:
    DynamicDisplayable(get_gloves_displayable, "pads", arm="larm", base=False)
    gloves_secondary_colour_transform()

layeredimage pads_gloves_l_above_layer:
    always "pads_gloves_l_above_base"
    always "pads_gloves_l_above_trim"

layeredimage pads_gloves_r_layer:
    always "pads_gloves_r_base"
    always "pads_gloves_r_trim"

layeredimage pads_gloves_l_layer:
    always "pads_gloves_l_base"
    always "pads_gloves_l_trim"






image cow_gloves_r_base:
    DynamicDisplayable(get_gloves_displayable, "cow", arm="rarm")
    gloves_primary_colour_transform()

image cow_gloves_r_trim:
    DynamicDisplayable(get_gloves_displayable, "cow", arm="rarm", base=False)
    gloves_secondary_colour_transform()

image cow_gloves_l_base:
    DynamicDisplayable(get_gloves_displayable, "cow", arm="larm")
    gloves_primary_colour_transform()

image cow_gloves_l_trim:
    DynamicDisplayable(get_gloves_displayable, "cow", arm="larm", base=False)
    gloves_secondary_colour_transform()

image cow_gloves_l_above_base:
    DynamicDisplayable(get_gloves_displayable, "cow", arm="larm", gloves=True)
    gloves_primary_colour_transform()

image cow_gloves_l_above_trim:
    DynamicDisplayable(get_gloves_displayable, "cow", arm="larm", gloves=True, base=False)
    gloves_secondary_colour_transform()

layeredimage cow_gloves_r_layer:
    always "cow_gloves_r_base"
    always "cow_gloves_r_trim"

layeredimage cow_gloves_l_layer:
    always "cow_gloves_l_base"
    always "cow_gloves_l_trim"
layeredimage cow_gloves_l_above_layer:
    always "cow_gloves_l_above_base"
    always "cow_gloves_l_above_trim"





image santa_gloves_r_base:
    DynamicDisplayable(get_gloves_displayable, "santa", arm="rarm")
    gloves_primary_colour_transform()

image santa_gloves_r_trim:
    DynamicDisplayable(get_gloves_displayable, "santa", arm="rarm", base=False)
    gloves_secondary_colour_transform()

image santa_gloves_l_base:
    DynamicDisplayable(get_gloves_displayable, "santa", arm="larm")
    gloves_primary_colour_transform()

image santa_gloves_l_trim:
    DynamicDisplayable(get_gloves_displayable, "santa", arm="larm", base=False)
    gloves_secondary_colour_transform()

image santa_gloves_l_above_base:
    DynamicDisplayable(get_gloves_displayable, "santa", arm="larm")
    gloves_primary_colour_transform()
image santa_gloves_l_above_trim:
    DynamicDisplayable(get_gloves_displayable, "santa", arm="larm", base=False)
    gloves_secondary_colour_transform()

layeredimage santa_gloves_r_layer:
    always "santa_gloves_r_base"
    always "santa_gloves_r_trim"

layeredimage santa_gloves_l_layer:
    always "santa_gloves_l_base"
    always "santa_gloves_l_trim"

layeredimage santa_gloves_l_above_layer:
    always "santa_gloves_l_above_base"
    always "santa_gloves_l_above_trim"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
