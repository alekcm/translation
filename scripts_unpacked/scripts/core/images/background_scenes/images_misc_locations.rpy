image bg_bushes:
    get_background_noshad_filename("bushes")
    bg_tint_transform()
image bg_alley:
    get_background_noshad_filename("alley")
    bg_tint_transform()
image bg_shop_corner:
    get_background_filename("shop_corner")
    bg_tint_transform()

layeredimage bg_gloryhole_scene:
    if dis(dis_beach) or dis(dis_lake):
        "bg_gloryole_stall_lake"
    elif loc(loc_park_toilet_girls_stall):
        "bg_gloryole_stall_brick"
    else:
        "bg_gloryole_stall_toilet"
    if loc_cur.has_gloryhole:
        "bg_gloryole_hole"

image bg_beach_locker_girls_stall = "bg_gloryhole_scene"
image bg_school_toilet_girls_stall = "bg_gloryhole_scene"
image bg_pub_toilet_girls_stall = "bg_gloryhole_scene"
image bg_park_toilet_girls_stall = "bg_gloryhole_scene"
image bg_changingroom = "bg_commercial_area_mall_fitting"

image bg_flat1:
    "bg_party_bedroom4"
    xzoom -1
image bg_flat2:
    "bg_party_bedroom3"
    xzoom -1
image bg_flat3:
    "bg_party_bedroom2"
    xzoom -1
image bg_flat4:
    "bg_party_bedroom1"
    xzoom -1
image bg_flat5:
    "bg_party_bedroom4"
    xzoom -1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
