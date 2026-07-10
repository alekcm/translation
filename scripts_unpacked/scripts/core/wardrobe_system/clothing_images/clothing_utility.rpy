define config.gl2 = True

















































init python:


    def update_wardrobe_colours(input_colour, hex):
        if not input_colour:
            return
        if renpy.get_screen("wardrobe_screen"):
            update_clothing_hex_colours(input_colour, hex)
        elif "hair" in tab_left_acc:
            update_hair_hex_colours(input_colour, hex)
        elif tab_left_acc == "eyes":
            update_eye_hex_colours(input_colour, hex) 
        elif tab_left_acc in ("skin", "skin_effect", "breasts"):
            update_skin_hex_colours(input_colour, hex) 
            update_skin_hex_colours(input_colour.replace("base", "shad"), skin_colour_shadow(hex)) 
        elif "nip" in tab_left_acc:
            update_nip_hex_colours(input_colour, hex) 
        else:
            update_clothing_hex_colours(input_colour, hex)


    def update_clothing_hex_colours(input_colour, hex):
        clothing_colours.update({input_colour: Color(color=(hex))})
        return hex

    def update_hair_hex_colours(input_colour, hex):
        hair_colours.update({input_colour: Color(color=(hex))})
        return hex

    def update_eye_hex_colours(input_colour, hex):
        eye_colours.update({input_colour: Color(color=(hex))})
        return hex

    def update_skin_hex_colours(input_colour, hex):
        skin_colours.update({input_colour: Color(color=(hex))})
        return hex

    def update_nip_hex_colours(input_colour, hex):
        nipple_colours.update({input_colour: Color(color=(hex))})
        vagina_colours.update({"1": Color(color=(hex))})
        return hex


    def get_wardrobe_colours():
        if "hair" in tab_left_acc:
            return hair_colours[player.hair_colour]
        elif tab_left_acc == "eyes":
            return eye_colours[player.eye_colour]
        else:
            return clothing_colours[picker.color_slot]





    def get_custom_clothing_colours(input_colour):
        global red_value, green_value, blue_value
        red_value = clothing_colours[input_colour][0] / float(255)
        green_value = clothing_colours[input_colour][1] / float(255)
        blue_value = clothing_colours[input_colour][2] / float(255)

    def update_clothing_colours(input_colour, r, g, b):  
        red = round(r,3)
        green = round(g,3)
        blue = round(b,3)
        clothing_colours.update({input_colour: Color(rgb = (red, green, blue))})
        return (red,green,blue)



    def get_custom_hair_colours(input_colour):
        global red_value, green_value, blue_value
        red_value = hair_colours[input_colour][0] / float(255)
        green_value = hair_colours[input_colour][1] / float(255)
        blue_value = hair_colours[input_colour][2] / float(255)

    def update_hair_colours(input_colour, r, g, b):
        red = round(r,3)
        green = round(g,3)
        blue = round(b,3)
        hair_colours.update({input_colour: Color(rgb = (red, green, blue))})
        return (red,green,blue)

    def get_custom_eye_colours(input_colour):
        global red_value, green_value, blue_value
        red_value = eye_colours[input_colour][0] / float(255)
        green_value = eye_colours[input_colour][1] / float(255)
        blue_value = eye_colours[input_colour][2] / float(255)

    def get_custom_skin_colours(input_colour):
        global red_value, green_value, blue_value
        red_value = skin_colours[input_colour][0] / float(255)
        green_value = skin_colours[input_colour][1] / float(255)
        blue_value = skin_colours[input_colour][2] / float(255)

    def get_custom_nip_colours(input_colour):
        global red_value, green_value, blue_value
        red_value = nipple_colours[input_colour][0] / float(255)
        green_value = nipple_colours[input_colour][1] / float(255)
        blue_value = nipple_colours[input_colour][2] / float(255)

    def update_eye_colours(input_colour, r, g, b):
        red = round(r,3)
        green = round(g,3)
        blue = round(b,3)
        eye_colours.update({input_colour: Color(rgb = (red, green, blue))})
        return (red,green,blue)


    def get_clothing_colour_name(tab_top, tab_left, is_primary):
        suffix = "_primary_colour"
        if not is_primary:
            suffix = "_secondary_colour"
        
        return getattr(globals()[tab_top], tab_left + suffix)

    def get_clothing_brightness(tab_top, tab_left, is_primary):
        suffix = "_primary_brightness"
        if not is_primary:
            suffix = "_secondary_brightness"
        
        return getattr(globals()[tab_top], tab_left + suffix)

    def get_clothing_saturation(tab_top, tab_left, is_primary):
        suffix = "_primary_saturation"
        if not is_primary:
            suffix = "_secondary_saturation"
        
        return getattr(globals()[tab_top], tab_left + suffix)

    def get_clothing_colour(tab_top, tab_left, is_primary):
        return clothing_colours[get_clothing_colour_name(tab_top, tab_left, is_primary)]

    def get_clothing_filename(name, tab_left, is_base=True, breasts=False, preg=False, arm=False, gloves=False):
        filename = "pc_" + tab_left + "_" + name + "_"
        if arm:
            if arm == "larm":
                filename = filename + "larm_"
                if gloves and player.left_hand in ["flyer", "hat", "beer_bottle", "wine_bottle", "brew"]:
                    if player.left_hand == "beer_bottle":
                        filename = filename + "beerb_" 
                    elif player.left_hand == "wine_bottle":
                        filename = filename + "wine_" 
                    elif player.left_hand in ["brew", "flyer", "hat"]:
                        filename = filename + "jar_" 
                    else:
                        filename = filename + "cover_" 
                
                elif player.left_hand in ["flyer", "hat", "beer", "beer_bottle", "wine_bottle", "brew"]:
                    filename = filename + "beer_" 
                elif player.cover_breasts:
                    filename = filename + "cover_" 
                else:
                    filename = filename + "down_"
                if is_base:
                    filename = filename + "base"
                else:
                    filename = filename + "trim"
            else:
                filename = filename + "rarm_"
                if weather_var in (3,4) and loc_cur.outside:
                    filename = filename + "umb_"
                elif player.right_hand == "beer":
                    filename = filename + "beer_"
                elif player.right_hand == "coffee":
                    filename = filename + "beer_"
                elif player.cover_vagina:
                    filename = filename + "coverv_"
                elif player.cover_breasts:
                    filename = filename + "coverb_"
                else:
                    filename = filename + "down_"
                if is_base:
                    filename = filename + "base"
                else:
                    filename = filename + "trim"
        
        
        elif breasts and preg:
            if isinstance(is_base, str):
                filename = filename + "belly_" + is_base + "_"
            elif is_base:
                filename = filename + "belly_base_"
            else:
                filename = filename + "belly_trim_"
            
            filename = filename + str(player.breasts) + "_" + str(player.pregnancy) 
        
        elif breasts:
            if isinstance(is_base, str):
                filename = filename + "breasts_" + is_base + "_"
            elif is_base:
                filename = filename + "breasts_base_"
            else:
                filename = filename + "breasts_trim_"
            
            filename = filename + str(player.breasts)
        
        else:
            
            if isinstance(is_base, str):
                filename = filename + is_base
            elif is_base:
                filename = filename + "base"
            else:
                filename = filename + "trim"
            if preg:
                filename = filename + "_" + str(player.pregnancy) 
        return filename

    def get_clothing_filename_pure(name, preg=True, breasts=False):
        filename = name
        if preg:
            return filename + "_" + str(player.pregnancy)
        elif breasts:
            return filename + "_" + str(player.breasts)
        return filename
    def get_cg_clothing_filename(name, preg=False, breasts=False):
        filename = name
        if preg:
            return filename + "_" + str(player.pregnancy)
        elif breasts:
            return filename + "_" + str(player.breasts)
        return filename


    def get_bra_filename(name, base=True, breasts=False, preg=False, arm=False):
        return get_clothing_filename(name, "bra", base, breasts, preg, arm)

    def get_pants_filename(name, base=True, breasts=False, preg=False, arm=False):
        return get_clothing_filename(name, "pants", base, breasts, preg, arm)

    def get_bsuit_filename(name, base=True, breasts=False, preg=False, arm=False):
        return get_clothing_filename(name, "bsuit", base, breasts, preg, arm)

    def get_top_filename(name, base=True, breasts=False, preg=False, arm=False):
        return get_clothing_filename(name, "top", base, breasts, preg, arm)

    def get_nips_filename():
        return "pc_extra_pokenips_" + str(player.breasts)

    def get_milkstain_filename():
        return "pc_extra_milkstain_" + str(player.breasts)

    def get_bottom_filename(name, base=True, breasts=False, preg=False, arm=False):
        return get_clothing_filename(name, "bottom", base, breasts, preg, arm)

    def get_jacket_filename(name, base=True, breasts=False, preg=False, arm=False):  
        return get_clothing_filename(name, "jacket", base, breasts, preg, arm)

    def get_coat_filename(name, base=True, breasts=False, preg=False, arm=False):  
        return get_clothing_filename(name, "coat", base, breasts, preg, arm)

    def get_outfit_filename(name, base=True, breasts=False, preg=False, arm=False):
        return get_clothing_filename(name, "outfit", base, breasts, preg, arm)

    def get_gloves_filename(name, base=True, breasts=False, preg=False, arm=False, gloves=False):
        return get_clothing_filename(name, "gloves", base, breasts, preg, arm, gloves)

    def get_hat_filename(name, base=True, breasts=False, preg=False, arm=False):
        return get_clothing_filename(name, "hat", base, breasts, preg, arm)

    def get_high_socks_filename(name, is_base=True):
        return get_clothing_filename(name, "socks", is_base, preg=True)
    def get_low_socks_filename(name, is_base=True):
        return get_clothing_filename(name, "socks", is_base, preg=False)

    def cycle_trans_material(tab_top, tab_left, is_primary):  
        suffix = "_primary"
        if not is_primary:
            suffix = "_secondary"
        current = get_trans_material(tab_top, tab_left, is_primary)
        if current == "trans_normal":
            current = "trans_sheer"
        elif current == "trans_sheer":
            current = "trans_trans"
        elif current == "trans_trans":
            current = "trans_mesh"
        elif current == "trans_mesh":
            current = "trans_fish"
        elif current == "trans_fish":
            current = "trans_net"
        else:
            current = "trans_normal"
        setattr(globals()[tab_top], tab_left + suffix + "_trans", current)
        setattr(c, tab_left + suffix + "_trans", current)


    def get_trans_material(tab_top, tab_left, is_primary):
        suffix = "_primary"
        if not is_primary:
            suffix = "_secondary"
        return getattr(globals()[tab_top], tab_left + suffix + "_trans")

    def get_nipple_poke_opacity():
        base = 0
        if loc_cur.outside:
            base += 25
        if player.desire >= 200:
            base += ((player.desire - 200) / 4)
        if base >= 100:
            base = 100
        return float(base) / 100

    def get_wetness_opacity():
        if player.hygiene <= 0:
            return "pc_wet_clothes_effect_3"
        elif player.hygiene <= 20:
            return "pc_wet_clothes_effect_2"
        elif player.hygiene <= 40:
            return "pc_wet_clothes_effect_1"
        else:
            return "trans_opaque"

transform clothing_tint_transform(tab_left, is_primary, opacity=1):
    matrixcolor TintMatrix(get_clothing_colour(tab_top, tab_left, is_primary)) * OpacityMatrix(opacity)




transform clothing_alpha_transform(name, tab_left, is_primary=True):
    AlphaMask(AlphaMask(name, get_trans_material(tab_top, tab_left, is_primary)), clothing_wet_transform(name))

transform clothing_wet_transform(name):
    AlphaMask(name, get_wetness_opacity())

transform bra_primary_colour_transform(opacity=1):
    clothing_tint_transform("bra", True, opacity)
transform bra_secondary_colour_transform(opacity=1):
    clothing_tint_transform("bra", False, opacity)

transform pants_primary_colour_transform(opacity=1):
    clothing_tint_transform("pants", True, opacity)
transform pants_secondary_colour_transform(opacity=1):
    clothing_tint_transform("pants", False, opacity)

transform bsuit_primary_colour_transform(opacity=1):
    clothing_tint_transform("bsuit", True, opacity)
transform bsuit_secondary_colour_transform(opacity=1):
    clothing_tint_transform("bsuit", False, opacity)

transform top_primary_colour_transform(opacity=1):
    clothing_tint_transform("top", True, opacity)
transform top_secondary_colour_transform(opacity=1):
    clothing_tint_transform("top", False, opacity)

transform bottom_primary_colour_transform(opacity=1):
    clothing_tint_transform("bottom", True, opacity)
transform bottom_secondary_colour_transform(opacity=1):
    clothing_tint_transform("bottom", False, opacity)

transform jacket_primary_colour_transform(opacity=1):
    clothing_tint_transform("jacket", True, opacity)
transform jacket_secondary_colour_transform(opacity=1):
    clothing_tint_transform("jacket", False, opacity)

transform coat_primary_colour_transform(opacity=1):
    clothing_tint_transform("coat", True, opacity)
transform coat_secondary_colour_transform(opacity=1):
    clothing_tint_transform("coat", False, opacity)

transform outfit_primary_colour_transform(opacity=1):
    clothing_tint_transform("outfit", True, opacity)
transform outfit_secondary_colour_transform(opacity=1):
    clothing_tint_transform("outfit", False, opacity)

transform gloves_primary_colour_transform(opacity=1):
    clothing_tint_transform("gloves", True, opacity)
transform gloves_secondary_colour_transform(opacity=1):
    clothing_tint_transform("gloves", False, opacity)

transform hat_primary_colour_transform(opacity=1):
    clothing_tint_transform("hat", True, opacity)
transform hat_secondary_colour_transform(opacity=1):
    clothing_tint_transform("hat", False, opacity)

transform socks_primary_colour_transform(opacity=1):
    clothing_tint_transform("socks", True, opacity)
transform socks_secondary_colour_transform(opacity=1):
    clothing_tint_transform("socks", False, opacity)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
