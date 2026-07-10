layeredimage bg_commercial: 
    if t.hour in light:
        "bg_commercial_area_day"
    elif t.hour == 21:
        "bg_commercial_area_night_open"
    elif t.hour in dark:
        "bg_commercial_area_night"
    else:
        "bg_commercial_area_dawn"

image bg_park_local_market_layer:
    get_background_filename("park_local_market")
    bg_tint_transform()
image bg_park_local_market_people1_layer:
    "bg_park_local_market_people1"
    bg_tint_transform()
image bg_park_local_market_people2_layer:
    "bg_park_local_market_people2"
    bg_tint_transform()

image bg_mall = "bg_commercial_area_mall"











image bg_mall_changingroom = "bg_commercial_area_mall_fitting"
image bg_mall_shop_clothing = "bg_commercial_area_mall_clothing"
image bg_mall_shop_cosmetics = "bg_commercial_area_mall_cosmetics"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
