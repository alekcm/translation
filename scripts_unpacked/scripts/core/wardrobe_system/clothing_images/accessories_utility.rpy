define config.gl2 = True

init python:
    makeup_colours = {

    "brown" : Color(rgb = (0.713, 0.619, 0.478)),
    "orange" : Color(rgb = (0.968, 0.454, 0.101)),
    "pink" : Color(rgb = (1, 0.411, 0.705)),
    "purple" : Color(rgb = (0.392, 0.098, 0.615)),
    "red" : Color(rgb = (0.847, 0.192, 0.192)),
    "crimson" : Color(rgb = (0.411, 0.180, 0.239)),
    "magenta" : Color(rgb = (0.662, 0.168, 0.623)),
    "hotpink" : Color(rgb = (1, 0.019, 0.521)),

    }
    metal_colours = {


    "gold" : Color(rgb = (0.929, 0.827, 0.207)),
    "silver" : Color(rgb = (0.474, 0.474, 0.505)),


    }

    def get_accessories_colour_name(tab_left_acc, is_primary):
        suffix = "_primary_colour"
        if not is_primary:
            suffix = "_secondary_colour"
        
        return getattr(acc, tab_left_acc + suffix)

    def get_accessories_colour(tab_left_acc, is_primary):
        return clothing_colours[get_accessories_colour_name(tab_left_acc, is_primary)]

    def get_lipstick_filename():
        filename = "pc_lipstick_mouth_" + str(player.mouth)
        return filename



    def get_accessories_filename(name, tab_left_acc, breasts=False, preg=False):
        filename = "pc_" + tab_left_acc + "_" + name
        
        if breasts:
            if not (c.cansee_breasts and not c.bra) or grope_breasts1 or grope_breasts2:
                filename = filename + "_c"
            filename = filename + "_" + str(player.breasts)
        elif preg:
            return filename + "_" + str(player.pregnancy)
        
        return filename 

    def get_nails_colour():
        if acc.nails:
            return accessories_primary_colour_transform("nails")
        else:
            return get_skin_colour(True)

transform accessories_tint_transform(tab_left_acc, is_primary, opacity=1):
    matrixcolor TintMatrix(get_accessories_colour(tab_left_acc, is_primary)) * OpacityMatrix(opacity)

transform accessories_primary_colour_transform(tab_left_acc, opacity=1):
    accessories_tint_transform(tab_left_acc, True, opacity)
transform accessories_secondary_colour_transform(tab_left_acc, opacity=1):
    accessories_tint_transform(tab_left_acc, False, opacity)
transform eyeshadow_colour_transform():
    accessories_tint_transform("eyeshadow", True, opacity=If(acc.makeup_on and acc.eyeshadow,0.6,0))
transform blush_opacity_transform():
    matrixcolor OpacityMatrix(min((player.desire + player.drunk) / float(400), 1.0))
transform nails_colour_transform():
    matrixcolor TintMatrix(get_nails_colour())
transform gag_colour_transform():
    matrixcolor TintMatrix(If(player.has_perk(perk_gagged_locked), clothing_colours["red"], clothing_colours["pink"]))
transform gag_metal_transform():
    matrixcolor TintMatrix(clothing_colours["steel"])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
