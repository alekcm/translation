

init python:

    def get_blend_color(is_base, front_alpha=1, back_alpha=0):  
        color1 = get_skin_notan_colour(is_base)
        if len(color1) < 4:
            color1 = get_skin_notan_colour(is_base)[0]
        color2 = get_skin_tan_colour(is_base)
        if len(color2) < 4:
            color2 = get_skin_tan_colour(is_base)[0]
        front_alpha = float(front_alpha)
        alpha = (1.0 - (1.0 - back_alpha)*(1.0 - front_alpha));
        red   = (color1[0]  * (1.0 - front_alpha) + color2[0]   * front_alpha);
        green = (color1[1]  * (1.0 - front_alpha) + color2[1]   * front_alpha);
        blue  = (color1[2]  * (1.0 - front_alpha) + color2[2]   * front_alpha);
        return Color((int(red), int(green), int(blue)))

    def skin_colour_shadow(colour):
        Color(colour).hsv 
        h,s,v=Color(colour).hsv 
        h = (clamp((h * 360) - 7, 0, 360)) / 360
        s = (clamp((s * 100) + 10, 0, 100)) / 100
        v = (clamp((v * 100) - 13, 0, 100)) / 100
        return Color(hsv=(h,s,v))


    red_value = 1.000
    green_value = 1.000
    blue_value = 1.000

    def get_skin_set():
        r = skin_colours["6_0_base"][0]
        g = skin_colours["6_0_base"][1]
        b = skin_colours["6_0_base"][2]
        
        r_shad = min(255, r*0.8)
        g_shad = min(255, g*0.8)
        b_shad = min(255, b*0.9)
        shad_colours = (int(r_shad), int(g_shad), int(b_shad))
        skin_colours["6_0_shad"] = Color(shad_colours)
        return shad_colours

    def update_colours(listname, r, g, b):
        red = round(r,3)
        green = round(g,3)
        blue = round(b,3)
        skin_colours.update({'6_0_base': Color(rgb = (red, green, blue))})
        
        return (red,green,blue)

    def get_skin_colour(is_base):
        
        if is_base:
            return skin_colours[player.skin_colour]
        else:
            next_colour = player.skin_colour.replace("base", "shad")
            return skin_colours[next_colour]
        filename = str(player.race) + "_0_"
        if is_base: 
            filename = filename + "base"
        else:
            filename = filename + "shad"
        return skin_colours[filename]

    def get_preg_colour():
        return player.preg_father_colour

    def get_skin_notan_colour(is_base):
        if is_base:
            return skin_colours[player.skin_colour]
        else:
            next_colour = player.skin_colour.replace("base", "shad")
            return skin_colours[next_colour]
        filename = str(player.race) + "_0_"
        if is_base:
            filename = filename + "base"
        else:
            filename = filename + "shad"
        return skin_colours[filename]

    def get_skin_tan_colour(is_base):
        if is_base:
            return skin_colours[player.skin_colour]
        else:
            next_colour = player.skin_colour.replace("base", "shad")
            return skin_colours[next_colour]
        filename = str(player.race) + "_0_"
        if is_base:
            filename = filename + "base"
        else:
            filename = filename + "shad"
        return skin_colours[filename]









    def get_npc_skin_colour(is_base):
        global npc_race
        if not isinstance(npc_race, Npc):
            if is_base:
                filename = "base_" + str(npc_race)
            else:
                filename = "shad_" + str(npc_race)
            return npc_skin_colours[filename]  
        else:
            if is_base:
                return npc_race.skinbase
            else:
                return npc_race.skinshad
    def get_npc2_skin_colour(is_base):
        global npc_race2
        if not isinstance(npc_race2, Npc):
            if is_base:
                filename = "base_" + str(npc_race2)  
            else:
                filename = "shad_" + str(npc_race2)
            return npc_skin_colours[filename]
        else:
            if is_base:
                return npc_race2.skinbase
            else:
                return npc_race2.skinshad
    def get_npc3_skin_colour(is_base):
        global npc_race3
        if not isinstance(npc_race3, Npc):
            if is_base:
                filename = "base_" + str(npc_race3)  
            else:
                filename = "shad_" + str(npc_race3)
            return npc_skin_colours[filename]
        else:
            if is_base:
                return npc_race3.skinbase
            else:
                return npc_race3.skinshad



    def get_skin_colour_button(race, is_base):
        filename = str(race) + "_0_"
        if is_base:
            filename = filename + "base"
        else:
            filename = filename + "shad"
        return skin_colours[filename]

    def get_skin_filename(name, preg=False, breasts=False):  
        filename = name
        if preg:
            return filename + "_" + str(player.pregnancy)
        elif breasts:
            return filename + "_" + str(player.breasts)
        return filename

    def get_avatar_skin_filenme(name, has_pregnancy_variations):
        return "pc_" + get_skin_filename(name, has_pregnancy_variations)

    def get_avatar_preg_belly_filenme(is_base):
        if player.pregnancy:
            filename = "pc_body_belly_" + str(player.pregnancy)
        elif player.isfat:
            filename = "pc_body_belly_1"
        if is_base:
            filename = filename + "_base"
        else:
            filename = filename + "_shad"
        return filename

    def get_breasts_filename(is_base):
        filename = "pc_body_breast_"
        if not (c.cansee_breasts and not (c.bra or c.bsuit)) or grope_breasts1 or grope_breasts2:
            filename = filename + "c_"
        filename = filename + str(player.breasts) + "_"
        if is_base:
            filename = filename + "base"
        else:
            filename = filename + "shad"
        return filename

    def get_nipple_filename(is_nude):
        filename = "pc_body_nips_"
        if not (c.cansee_breasts and not (c.bra or c.bsuit)) or grope_breasts1 or grope_breasts2:
            filename = filename + "c_"
        filename = filename + str(player.breasts) + "_" + str(player.nip_size)
        return filename

    def get_nipple_colour():
        return nipple_colours[str(player.nip_colour)]
    def get_vagina_colour():
        return nipple_colours[str(player.nip_colour)]


transform shad_notan_transform(colour):
    matrixcolor skin_tint_transform(True) * SaturationMatrix(-0.1)
transform base_tan_transform(colour):
    matrixcolor skin_tint_transform(True) * BrightnessMatrix(-0.2)
transform shad_tan_transform(colour):
    matrixcolor shad_notan_transform(colour) * BrightnessMatrix(-0.2)


transform skin_tint_transform(is_base, opacity=1):
    matrixcolor TintMatrix(get_blend_color(is_base,player.suntan)) * OpacityMatrix(opacity)
transform skin_tint_notan_transform(is_base, opacity=1):
    matrixcolor TintMatrix(get_skin_notan_colour(is_base)) * OpacityMatrix(opacity)
transform skin_tint_tan_transform(is_base, opacity=1):
    matrixcolor TintMatrix(get_skin_tan_colour(is_base)) * OpacityMatrix(opacity)
transform photo_skin_tint_transform(photo_class, is_base, opacity=1):
    matrixcolor TintMatrix(get_photo_skin_colour(photo_class, is_base)) * OpacityMatrix(opacity)
transform npc_skin_tint_transform(is_base, opacity=1):
    matrixcolor TintMatrix(get_npc_skin_colour(is_base)) * OpacityMatrix(opacity)
transform npc2_skin_tint_transform(is_base, opacity=1):
    matrixcolor TintMatrix(get_npc2_skin_colour(is_base)) * OpacityMatrix(opacity)
transform npc3_skin_tint_transform(is_base, opacity=1):
    matrixcolor TintMatrix(get_npc3_skin_colour(is_base)) * OpacityMatrix(opacity)

transform nipple_colour_transform(opacity=1):
    matrixcolor TintMatrix(get_nipple_colour()) * OpacityMatrix(opacity)
transform vagina_colour_transform(opacity=1):
    matrixcolor TintMatrix(get_vagina_colour()) * OpacityMatrix(opacity)

transform skin_base_colour_transform(opacity=1):
    skin_tint_transform(True, opacity)
transform skin_shad_colour_transform(opacity=1):
    skin_tint_transform(False, opacity)
transform skin_base_notan_colour_transform(opacity=1):
    skin_tint_notan_transform(True, opacity)
transform skin_shad_notan_colour_transform(opacity=1):
    skin_tint_notan_transform(False, opacity)





transform photo_skin_base_colour_transform(photo_class, opacity=1):
    photo_skin_tint_transform(photo_class, True, opacity)
transform photo_skin_shad_colour_transform(photo_class, opacity=1):
    photo_skin_tint_transform(photo_class, False, opacity)
transform photo_nipple_colour_transform(photo_class, opacity=1):
    matrixcolor TintMatrix(nipple_colours[str(photo_class.race)]) * OpacityMatrix(opacity)
transform photo_vagina_colour_transform(photo_class, opacity=1):
    matrixcolor TintMatrix(vagina_colours[str(photo_class.race)]) * OpacityMatrix(opacity)

transform npc_skin_base_colour_transform(opacity=1):
    npc_skin_tint_transform(True, opacity)
transform npc_skin_shad_colour_transform(opacity=1):
    npc_skin_tint_transform(False, opacity)

transform npc2_skin_base_colour_transform(opacity=1):
    npc2_skin_tint_transform(True, opacity)
transform npc2_skin_shad_colour_transform(opacity=1):
    npc2_skin_tint_transform(False, opacity)

transform npc3_skin_base_colour_transform(opacity=1):
    npc3_skin_tint_transform(True, opacity)
transform npc3_skin_shad_colour_transform(opacity=1):
    npc3_skin_tint_transform(False, opacity)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
