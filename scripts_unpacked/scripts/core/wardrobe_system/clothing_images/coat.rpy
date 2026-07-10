init python:
    def get_coat_displayable(st, at, name, **kwargs):
        
        return (get_coat_filename(name, **kwargs), None)





image teehood_coat_body_base_layer:
    get_coat_filename("teehood", preg=True)
    coat_primary_colour_transform()

image teehood_coat_breasts_base_layer:
    get_coat_filename("teehood", breasts=True)
    coat_primary_colour_transform()

layeredimage teehood_coat_layerd:
    always "teehood_coat_body_base_layer"
    always "teehood_coat_breasts_base_layer"





image cropjump_coat_body_base_layer:
    get_coat_filename("cropjump", preg=True)
    coat_primary_colour_transform()
image cropjump_coat_body_trim_layer:
    get_coat_filename("cropjump", preg=True, base=False)
    coat_secondary_colour_transform()

image cropjump_coat_breasts_base_layer:
    get_coat_filename("cropjump", breasts=True)
    coat_primary_colour_transform()

image cropjump_coat_rarm_base:
    DynamicDisplayable(get_coat_displayable, "cropjump", arm="rarm")
    coat_primary_colour_transform()
image cropjump_coat_rarm_trim:
    DynamicDisplayable(get_coat_displayable, "cropjump", arm="rarm", base=False)
    coat_secondary_colour_transform()

image cropjump_coat_larm_base:
    DynamicDisplayable(get_coat_displayable, "cropjump", arm="larm")
    coat_primary_colour_transform()
image cropjump_coat_larm_trim:
    DynamicDisplayable(get_coat_displayable, "cropjump", arm="larm", base=False)
    coat_secondary_colour_transform()
image cropjump_coat_larm_above_base:
    "pc_coat_cropjump_larm_coverabove_base"
    coat_primary_colour_transform()
image cropjump_coat_larm_above_trim:
    "pc_coat_cropjump_larm_coverabove_trim"
    coat_secondary_colour_transform()

layeredimage cropjump_coat_layerd:
    always "cropjump_coat_body_base_layer"
    always "cropjump_coat_body_trim_layer"
    always "cropjump_coat_breasts_base_layer"

layeredimage cropjump_coat_rarm_layerd:
    always "cropjump_coat_rarm_base"
    always "cropjump_coat_rarm_trim"
layeredimage cropjump_coat_larm_layerd:
    always "cropjump_coat_larm_base"
    always "cropjump_coat_larm_trim"
layeredimage cropjump_coat_larm_above_layered:
    always "cropjump_coat_larm_above_base"
    always "cropjump_coat_larm_above_trim"





image sleevelesscoat_coat_body_layer:
    get_top_filename("sleevelesscoat", preg=True)
    coat_secondary_colour_transform()
image sleevelesscoat_coat_breasts_layer:
    get_top_filename("sleevelesscoat", breasts=True)
    coat_secondary_colour_transform()

layeredimage sleevelesscoat_coat_layerd:
    always "sleevelesscoat_coat_body_layer"
    always "sleevelesscoat_coat_breasts_layer"




image pc_coat_long_base_1 = "pc_coat_long_base_0"
image pc_coat_long_trim_1 = "pc_coat_long_trim_0"
image longcoat_base:
    get_coat_filename("long", preg=True)
    coat_primary_colour_transform()
image longcoat_trim:
    get_coat_filename("long", preg=True, base=False)
    coat_secondary_colour_transform()
image longcoat_breasts_base:
    get_coat_filename("long", breasts=True)
    coat_primary_colour_transform()
image longcoat_breasts_trim:
    get_coat_filename("long", breasts=True, base=False)
    coat_secondary_colour_transform()

image longcoat_rarm_base:
    DynamicDisplayable(get_coat_displayable, "long", arm="rarm")
    coat_primary_colour_transform()
image longcoat_rarm_trim:
    DynamicDisplayable(get_coat_displayable, "long", arm="rarm", base=False)
    coat_secondary_colour_transform()

image longcoat_larm_base:
    DynamicDisplayable(get_coat_displayable, "long", arm="larm")
    coat_primary_colour_transform()
image longcoat_larm_trim:
    DynamicDisplayable(get_coat_displayable, "long", arm="larm", base=False)
    coat_secondary_colour_transform()
image longcoat_larm_above_base:
    "pc_coat_long_larm_coverabove_base"
    coat_primary_colour_transform()
image longcoat_larm_above_trim:
    "pc_coat_long_larm_coverabove_trim"
    coat_secondary_colour_transform()

layeredimage longcoat_body_layer:
    always "longcoat_base"
    always "longcoat_trim"
    always "longcoat_breasts_base"
    always "longcoat_breasts_trim"
layeredimage longcoat_larm_layer:
    always "longcoat_larm_base"
    always "longcoat_larm_trim"
layeredimage longcoat_larm_above_layer:
    always "longcoat_larm_above_base"
    always "longcoat_larm_above_trim"
layeredimage longcoat_rarm_layer:
    always "longcoat_rarm_base"
    always "longcoat_rarm_trim"





image coat_server_base:
    "pc_coat_server"
    coat_primary_colour_transform()
image coat_server_collar_base:
    "pc_top_server"
    coat_secondary_colour_transform()

layeredimage coat_server_body_layer:
    always "coat_server_base"
    always "coat_server_collar_base"





image waistcoat_coat_body_layer:
    get_coat_filename("waistcoat", preg=True)
    coat_primary_colour_transform()
image waistcoat_coat_breasts_layer:
    get_coat_filename("waistcoat", breasts=True)
    coat_primary_colour_transform()

layeredimage waistcoat_coat_layerd:
    always "waistcoat_coat_body_layer"
    always "waistcoat_coat_breasts_layer"





image pc_coat_puff_base_1 = "pc_coat_puff_base_0"
image pc_coat_puff_trim_1 = "pc_coat_puff_trim_0"

image puff_coat_body_base_layer:
    get_coat_filename("puff", preg=True)
    coat_primary_colour_transform()
image puff_coat_body_trim_layer:
    get_coat_filename("puff", preg=True, base=False)
    coat_secondary_colour_transform()

image puff_coat_breasts_base_layer:
    get_coat_filename("puff", breasts=True)
    coat_primary_colour_transform()

image puff_coat_rarm_base:
    DynamicDisplayable(get_coat_displayable, "puff", arm="rarm")
    coat_primary_colour_transform()
image puff_coat_rarm_trim:
    DynamicDisplayable(get_coat_displayable, "puff", arm="rarm", base=False)
    coat_secondary_colour_transform()

image puff_coat_larm_base:
    DynamicDisplayable(get_coat_displayable, "puff", arm="larm")
    coat_primary_colour_transform()
image puff_coat_larm_trim:
    DynamicDisplayable(get_coat_displayable, "puff", arm="larm", base=False)
    coat_secondary_colour_transform()
image puff_coat_larm_above_base:
    "pc_coat_puff_larm_coverabove_base"
    coat_primary_colour_transform()
image puff_coat_larm_above_trim:
    "pc_coat_puff_larm_coverabove_trim"
    coat_secondary_colour_transform()

layeredimage puff_coat_layerd:
    always "puff_coat_body_base_layer"
    always "puff_coat_body_trim_layer"
    always "puff_coat_breasts_base_layer"

layeredimage puff_coat_rarm_layerd:
    always "puff_coat_rarm_base"
    always "puff_coat_rarm_trim"
layeredimage puff_coat_larm_above_layerd:
    always "puff_coat_larm_above_base"
    always "puff_coat_larm_above_trim"
layeredimage puff_coat_larm_layerd:
    always "puff_coat_larm_base"
    always "puff_coat_larm_trim"




image sleevelesshoodie_coat_body_layer:
    get_coat_filename("lesshood", preg=True)
    coat_primary_colour_transform()
image sleevelesshoodie_coat_body_trim_layer:
    get_coat_filename("lesshood", preg=True, base=False)
    coat_secondary_colour_transform()

image sleevelesshoodie_coat_breasts_layer:
    get_coat_filename("lesshood", breasts=True)
    coat_primary_colour_transform()

layeredimage sleevelesshoodie_coat_layerd:
    always "sleevelesshoodie_coat_body_layer"
    always "sleevelesshoodie_coat_body_trim_layer"
    always "sleevelesshoodie_coat_breasts_layer"






image ziphoodie_coat_body_base_layer:
    get_coat_filename("ziphoodie", preg=True)
    coat_primary_colour_transform()
image ziphoodie_coat_body_trim_layer:
    get_coat_filename("ziphoodie", preg=True, base=False)
    coat_secondary_colour_transform()

image ziphoodie_coat_breasts_base_layer:
    get_coat_filename("ziphoodie", breasts=True)
    coat_primary_colour_transform()
image ziphoodie_coat_breasts_trim_layer:
    get_coat_filename("ziphoodie", breasts=True, base=False)
    coat_secondary_colour_transform()

image ziphoodie_coat_rarm_base:
    DynamicDisplayable(get_coat_displayable, "ziphoodie", arm="rarm")
    coat_primary_colour_transform()
image ziphoodie_coat_rarm_trim:
    DynamicDisplayable(get_coat_displayable, "ziphoodie", arm="rarm", base=False)
    coat_secondary_colour_transform()

image ziphoodie_coat_larm_base:
    DynamicDisplayable(get_coat_displayable, "ziphoodie", arm="larm")
    coat_primary_colour_transform()
image ziphoodie_coat_larm_trim:
    DynamicDisplayable(get_coat_displayable, "ziphoodie", arm="larm", base=False)
    coat_secondary_colour_transform()
image ziphoodie_coat_larm_above_base:
    "pc_coat_ziphoodie_larm_coverabove_base"
    coat_primary_colour_transform()
image ziphoodie_coat_larm_above_trim:
    "pc_coat_ziphoodie_larm_coverabove_trim"
    coat_secondary_colour_transform()

layeredimage ziphoodie_coat_layerd:
    always "ziphoodie_coat_body_base_layer"
    always "ziphoodie_coat_body_trim_layer"
    always "ziphoodie_coat_breasts_base_layer"
    always "ziphoodie_coat_breasts_trim_layer"

layeredimage ziphoodie_coat_rarm_layerd:
    always "ziphoodie_coat_rarm_base"
    always "ziphoodie_coat_rarm_trim"
layeredimage ziphoodie_coat_larm_layerd:
    always "ziphoodie_coat_larm_base"
    always "ziphoodie_coat_larm_trim"
layeredimage ziphoodie_coat_larm_above_layerd:
    always "ziphoodie_coat_larm_above_base"
    always "ziphoodie_coat_larm_above_trim"





image crophoodie_base_breasts:
    get_top_filename("crophoodie", breasts=True)
    coat_primary_colour_transform()
image crophoodie_trim_breasts:
    get_top_filename("crophoodie", breasts=True, base=False)
    coat_secondary_colour_transform()

image crophoodie_base_larm_layer:
    DynamicDisplayable(get_top_displayable, "crophoodie", arm="larm")
    coat_primary_colour_transform()
image crophoodie_trim_larm_layer:
    DynamicDisplayable(get_top_displayable, "crophoodie", arm="larm", base=False)
    coat_secondary_colour_transform()
image crophoodie_base_larm_above_layer:
    "pc_top_crophoodie_larm_coverabove_base"
    coat_primary_colour_transform()
image crophoodie_trim_larm_above_layer:
    "pc_top_crophoodie_larm_coverabove_trim"
    coat_secondary_colour_transform()

image crophoodie_base_rarm_layer:
    DynamicDisplayable(get_top_displayable, "crophoodie", arm="rarm")
    coat_primary_colour_transform()
image crophoodie_trim_rarm_layer:
    DynamicDisplayable(get_top_displayable, "crophoodie", arm="rarm", base=False)
    coat_secondary_colour_transform()

layeredimage crophoodie_layerd:
    always "crophoodie_base_breasts"
    always "crophoodie_trim_breasts"

layeredimage crophoodie_larm_layerd:
    always "crophoodie_base_larm_layer"
    always "crophoodie_trim_larm_layer"
layeredimage crophoodie_larm_above_layerd:
    always "crophoodie_base_larm_above_layer"
    always "crophoodie_trim_larm_above_layer"

layeredimage crophoodie_rarm_layerd:
    always "crophoodie_base_rarm_layer"
    always "crophoodie_trim_rarm_layer"





image bftee_base_breasts:
    get_coat_filename("bftee", breasts=True)
    coat_primary_colour_transform()
image bftee_base_body:
    get_coat_filename("bftee", preg=True)
    coat_primary_colour_transform()

layeredimage bftee_layerd:
    always "bftee_base_body"
    always "bftee_base_breasts"




image pc_coat_onesee_base_1 = "pc_coat_onesee_base_0"
image pc_coat_onesee_trim_1 = "pc_coat_onesee_trim_0"

image onesee_base_breasts:
    get_coat_filename("onesee", breasts=True)
    coat_primary_colour_transform()
image onesee_trim_breasts:
    get_coat_filename("onesee", breasts=True, base=False)
    coat_secondary_colour_transform()

image onesee_base_body:
    get_coat_filename("onesee", preg=True)
    coat_primary_colour_transform()
image onesee_trim_body:
    get_coat_filename("onesee", preg=True, base=False)
    coat_secondary_colour_transform()

image onesee_larm_layerd:
    DynamicDisplayable(get_coat_displayable, "onesee", arm="larm")
    coat_primary_colour_transform()
image onesee_larm_above_layerd:
    "pc_coat_onesee_larm_coverabove_base"
    coat_primary_colour_transform()

image onesee_rarm_layerd:
    DynamicDisplayable(get_coat_displayable, "onesee", arm="rarm")
    coat_primary_colour_transform()

layeredimage onesee_layerd:
    always "onesee_base_body"
    always "onesee_trim_body"
    always "onesee_base_breasts"
    always "onesee_trim_breasts"





image knithoodie_base_body:
    "pc_coat_knithoodie_base"
    coat_primary_colour_transform()

image knithoodie_larm_layerd:
    get_coat_filename("knithoodie", arm="larm")
    coat_primary_colour_transform()

image knithoodie_rarm_layerd:
    get_coat_filename("knithoodie", arm="rarm")
    coat_primary_colour_transform()

image knithoodie_larm_coverabove_layerd:
    "pc_coat_knithoodie_larm_coverabove_base"
    coat_primary_colour_transform()

layeredimage knithoodie_layerd:
    always "knithoodie_base_body"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
