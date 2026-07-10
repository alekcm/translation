init python:
    def bg_mood_happy_opcaity():
        return round(float(percent_scaler(80, 200, player._mood)) / 100, 2)
    def bg_mood_sad_opcaity():
        return round(float(percent_scaler(-50, 20, int(player._mood), True)) / 100, 2)
    def bg_mood_drunk_blur():
        return percent_scaler(50, 150, player.drunk) / 15

    def bg_colour_contrast():
        amount = 1 
        amount = amount + (bg_mood_happy_opcaity() / 10)
        return amount
    def bg_colour_saturation():
        amount = 1 
        amount = amount + (bg_mood_happy_opcaity() / 3)
        amount = amount + -(bg_mood_sad_opcaity())
        if renpy.count_displayables_in_layer("master"):
            
            amount = 0.5
        return amount
    def bg_colour_brightness():
        if renpy.count_displayables_in_layer("master"):
            
            amount = -0.15
        return amount
    def bg_colour_blur():
        amount = 0
        if bg_mood_drunk_blur():
            amount = bg_mood_drunk_blur()
        elif renpy.count_displayables_in_layer("master"):
            amount = 2
        return amount

screen background_scene():

    zorder -1

    add "sky" + bg_sky_dummy():
        if bg_mood_happy_opcaity():
            matrixcolor ContrastMatrix(1 + bg_mood_happy_opcaity() / 10) * SaturationMatrix(1 + bg_mood_happy_opcaity() / 3)
        if bg_mood_sad_opcaity():
            matrixcolor SaturationMatrix(1 + -(bg_mood_sad_opcaity()))
        if renpy.count_displayables_in_layer("master"):
            matrixcolor BrightnessMatrix(-0.15) * SaturationMatrix(0.5)
            blur 2

        blur bg_mood_drunk_blur()
    add "bg_scene" + bg_scene_dummy():

        if bg_mood_happy_opcaity():
            matrixcolor ContrastMatrix(1 + bg_mood_happy_opcaity() / 10) * SaturationMatrix(1 + bg_mood_happy_opcaity() / 3)
        if bg_mood_sad_opcaity():
            matrixcolor SaturationMatrix(1 + -(bg_mood_sad_opcaity()))
        if renpy.count_displayables_in_layer("master"):
            matrixcolor BrightnessMatrix(-0.15) * SaturationMatrix(0.5)
            blur 2

        blur bg_mood_drunk_blur()

    add "bg_effect_mood" + bg_moodscene_dummy()


image bg_effect_mood_happy:
    "mood_overlay_happy"
    matrixcolor OpacityMatrix(bg_mood_happy_opcaity() / 2)
image bg_effect_mood_sad:
    "mood_overlay_sad"
    matrixcolor OpacityMatrix(bg_mood_sad_opcaity() / 2)

layeredimage bg_effect_mood:
    group dummy:
        attribute bg_moodscene_dummy_attribute:
            null
    always "bg_effect_mood_happy"
    always "bg_effect_mood_sad"

image bg_snow_layer:
    "bg_snow"
    matrixcolor OpacityMatrix(0.5)

screen foreground_scene():
    zorder -1
    if player.has_perk(perk_blind):
        add "bg_blindfold"

    if loc(loc_beach_water):
        add "fg_water"
    if loc(loc_bus_interior):
        add "fg_bus_interior"

    if weather_var == 3 and loc_cur.outside:
        add "bg_rain"
    elif weather_var == 4 and loc_cur.outside:
        add "bg_snow_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
