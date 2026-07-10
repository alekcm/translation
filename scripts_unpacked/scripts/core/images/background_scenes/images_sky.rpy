init python:
    def bg_sky_trans():
        if t.timeofday == "day" and t.hour in (t.timeofday_check()[0], t.timeofday_check()[-1]):
            return If(t.hour == t.timeofday_check()[-1], t.minute / float(60), 1 - (t.minute / float(60)))
        elif t.timeofday == "dawn":
            return If(t.hour == t.timeofday_check()[-1] + 1, 1 - t.minute / float(60), t.minute / float(60))
        else: 
            return 0

layeredimage sky_day:
    if (t.month == "Winter" or weather_var == 4):
        "bg_sky_day_snow"
    elif weather_var == 1:
        "bg_sky_day_sunny"
    elif weather_var in (2,3):
        "bg_sky_day_cloudy"

layeredimage sky_dawn_layer:
    if (t.month == "Winter" or weather_var == 4):
        "bg_sky_dawn_snow"
    elif weather_var == 1:
        "bg_sky_dawn_sunny"
    elif weather_var in (2,3):
        "bg_sky_dawn_cloudy"

image sky_dawn:
    "sky_dawn_layer"
    sky_dawn_transform()

layeredimage sky_night:
    if (t.month == "Winter" or weather_var == 4):
        "bg_sky_night_snow"
    elif weather_var == 1:
        "bg_sky_night_sunny"
    elif weather_var in (2,3):
        "bg_sky_night_cloudy"

layeredimage sky:
    group dummy:
        attribute bg_sky_dummy_attribute:
            null
    if t.timeofday == "day":
        "sky_day"
    else:
        "sky_night"
    if not junk_var:
        "sky_dawn"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
