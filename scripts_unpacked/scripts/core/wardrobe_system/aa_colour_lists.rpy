init python:
    def get_color_name(rgb):
        rgb = rgb.rgb 
        
        
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        
        rgb = (r,g,b)
        colors = {
            "red": (255, 0, 0),
            "orange": (255, 128, 0),
            "yellow": (255, 255, 0),
            "lime": (128, 255, 0),
            "green": (0, 255, 0),
            "light green": (0, 255, 128),
            "sky blue": (0, 255, 255),
            "light blue": (0, 128, 255),
            "blue": (0, 0, 255),
            "purple": (128, 0, 255),
            "pink": (255, 0, 255),
            "hot pink": (255, 0, 128),
            
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "grey": (128, 128, 128),
            "dark grey": (40, 40, 40),
            "grey": (200, 200, 200),
            "brown": (128, 64, 32),
        }
        min_distance = float("inf")
        closest_color = None
        for color, value in colors.items():
            distance = sum([(i - j) ** 2 for i, j in zip(rgb, value)])
            if distance < min_distance:
                min_distance = distance
                closest_color = color
        
        return closest_color



default clothing_colours = {
    "black" : Color(rgb = (0.25, 0.25, 0.3)),
    "white" : Color(rgb = (0.898, 0.949, 1)),
    "blue" : Color(rgb = (0.352, 0.529, 0.635)),
    "cyan" : Color(rgb = (0.145, 0.831, 0.827)),
    "ocean" : Color(rgb = (0.145, 0.509, 0.831)),
    "brown" : Color(rgb = (0.713, 0.619, 0.478)),
    "green" : Color(rgb = (0.286, 0.360, 0.125)),
    "orange" : Color(rgb = (0.968, 0.454, 0.101)),
    "pumpkin" : Color(rgb = (0.913, 0.513, 0.384)),
    "pink" : Color(rgb = (1, 0.411, 0.705)),
    "purple" : Color(rgb = (0.392, 0.098, 0.615)),
    "red" : Color(rgb = (0.847, 0.192, 0.192)),
    "crimson" : Color(rgb = (0.411, 0.180, 0.239)),
    "sky" : Color(rgb = (0.682, 0.811, 0.933)),
    "yellow" : Color(rgb = (0.929, 0.827, 0.207)),
    "grey" : Color(rgb = (0.474, 0.474, 0.505)),
    "navy" : Color(rgb = (0.129, 0.184, 0.250)),
    "magenta" : Color(rgb = (0.662, 0.168, 0.623)),
    "hotpink" : Color(rgb = (0.890, 0.086, 0.498)),
    "lime" : Color(rgb = (0.364, 0.662, 0.062)),

    "custom1" : Color(rgb = (0.25, 0.25, 0.3)),
    "custom2" : Color(rgb = (0.474, 0.474, 0.505)),
    "custom3" : Color(rgb = (0.898, 0.949, 1)),
    "custom4" : Color(rgb = (0.129, 0.184, 0.250)),
    "custom5" : Color(rgb = (0.352, 0.529, 0.635)),
    "custom6" : Color(rgb = (0.411, 0.180, 0.239)),
    "custom7" : Color(rgb = (0.713, 0.619, 0.478)),
    "custom8" : Color(rgb = (0.286, 0.360, 0.125)),
    "custom9" : Color(rgb = (0.913, 0.513, 0.384)),
    "custom10" : Color(rgb = (1, 0.411, 0.705)),
    "custom11" : Color(rgb = (0.662, 0.168, 0.623)),
    "custom12" : Color(rgb = (0.929, 0.827, 0.207)),

    "custommakeup1" : Color(rgb=(0.8000, 0.7294, 0.3333)),
    "custommakeup2" : Color(rgb=(0.6627, 0.0627, 0.5647)),
    "custommakeup3" : Color(rgb=(0.4314, 0.3255, 0.7137)),
    "custommakeup4" : Color(rgb=(0.0627, 0.5725, 0.6627)),
    "custommakeup5" : Color(rgb=(0.6627, 0.3020, 0.0627)),
    "custommakeup6" : Color(rgb=(0.6627, 0.0627, 0.4314)),
    "custommakeup7" : Color(rgb=(0.3137, 0.0784, 0.1176)),
    "custommakeup8" : Color(rgb=(0.8588, 0.6314, 0.8863)),

    
    "silver" : Color(rgb = (0.827, 0.772, 0.827)),
    "steel" : Color(rgb = (0.443, 0.376, 0.443)),
    "gold" : Color(rgb = (0.784, 0.662, 0.054)),

    }


default skin_colours = {
    "1_0_base" : Color(rgb = (0.976, 0.827, 0.729)),
    "1_0_shad" : Color(rgb = (0.945, 0.682, 0.556)),
  
    "2_0_base" : Color(rgb = (0.894, 0.709, 0.607)),
    "2_0_shad" : Color(rgb = (0.752, 0.525, 0.447)),

    "3_0_base" : Color(rgb = (0.545, 0.407, 0.333)),
    "3_0_shad" : Color(rgb = (0.364, 0.258, 0.231)),

    "4_0_base" : Color(rgb = (0.686, 0.509, 0.486)),
    "4_0_shad" : Color(rgb = (0.490, 0.349, 0.352)),

    "5_0_base" : Color(rgb = (0.972, 0.843, 0.717)),
    "5_0_shad" : Color(rgb = (0.819, 0.627, 0.517)),

    "6_0_base" : Color(rgb = (0.976, 0.827, 0.729)),
    "6_0_shad" : Color(rgb = (0.945, 0.682, 0.556)),
  
    "7_0_base" : Color(rgb = (0.894, 0.709, 0.607)),
    "7_0_shad" : Color(rgb = (0.752, 0.525, 0.447)),

    "8_0_base" : Color(rgb = (0.545, 0.407, 0.333)),
    "8_0_shad" : Color(rgb = (0.364, 0.258, 0.231)),

    "9_0_base" : Color(rgb = (0.686, 0.509, 0.486)),
    "9_0_shad" : Color(rgb = (0.490, 0.349, 0.352)),

    "10_0_base" : Color(rgb = (0.972, 0.843, 0.717)),
    "10_0_shad" : Color(rgb = (0.819, 0.627, 0.517)),

    }

default npc_skin_colours = {
    "base_1" : Color(color=("#e9bca7")),
    "shad_1" : Color(color=("#d99980")),

    "base_2" : Color(color=("#c89d8a")),
    "shad_2" : Color(color=("#a27566")),

    "base_3" : Color(color=("#e7c0a4")),
    "shad_3" : Color(color=("#b28a76")),

    "base_4" : Color(color=("#bc8f80")),
    "shad_4" : Color(color=("#a37162")),

    "base_5" : Color(color=("#73594b")),
    "shad_5" : Color(color=("#4d3934")),

    "base_6" : Color(color=("#93716d")),
    "shad_6" : Color(color=("#684e4f")),

    "base_7" : Color(color=("#927266")),
    "shad_7" : Color(color=("#6f544c")),

    "base_8" : Color(color=("#4e4038")),
    "shad_8" : Color(color=("#342927")),

    "base_9" : Color(color=("#655250")),
    "shad_9" : Color(color=("#47393a")),

    "base_10" : Color(color=("#b8917d")),
    "shad_10" : Color(color=("#7d6357")),
    }

default nipple_colours = {
    "1" : Color(rgb = (0.854, 0.572, 0.462)), 
    "2" : Color(rgb = (0.709, 0.458, 0.368)),
    "3" : Color(rgb = (0.286, 0.211, 0.192)),
    "4" : Color(rgb = (0.415, 0.301, 0.305)),
    "5" : Color(rgb = (0.741, 0.509, 0.380)),
    "6" : Color(rgb = (0.815, 0.517, 0.482)),
    "7" : Color(rgb = (0.929, 0.603, 0.623)),
    "8" : Color(rgb = (1, 0.729, 0.745)),

    "9" : Color(rgb = (0.854, 0.572, 0.462)),
    "10" : Color(rgb = (0.709, 0.458, 0.368)),
    "11" : Color(rgb = (0.286, 0.211, 0.192)),
    "12" : Color(rgb = (0.415, 0.301, 0.305)),
    "13" : Color(rgb = (0.741, 0.509, 0.380)),
    }

default nipple_colours_list = ("1","2","3","4","5","6","7","8")
default nipple_colours_custom_list = ("9","10","11","12","13")

default vagina_colours = {
    "1" : Color(rgb = (0.996, 0.6, 0.533)),
    "2" : Color(rgb = (0.713, 0.454, 0.364)),
    "3" : Color(rgb = (0.392, 0.207, 0.129)),
    "4" : Color(rgb = (0.501, 0.266, 0.152)),
    "5" : Color(rgb = (0.996, 0.6, 0.533)),
    }

default hair_colours = {
    "hair1" : Color(rgb = (0.960, 0.941, 0.784)),
    "hair2" : Color(rgb = (0.898, 0.815, 0.568)),
    "hair3" : Color(rgb = (0.843, 0.607, 0.372)),
    "hair4" : Color(rgb = (0.576, 0.396, 0.294)),
    "hair5" : Color(rgb = (0.333, 0.278, 0.274)),
    "hair6" : Color(rgb = (0.227, 0.219, 0.223)),
    "hair7" : Color(rgb = (0.603, 0.388, 0.227)),
    "hair8" : Color(rgb = (0.835, 0.337, 0.211)),

    "hair9" : Color(rgb = (0.960, 0.941, 0.784)),
    "hair10" : Color(rgb = (0.898, 0.815, 0.568)),
    "hair11" : Color(rgb = (0.843, 0.607, 0.372)),
    "hair12" : Color(rgb = (0.576, 0.396, 0.294)),
    "hair13" : Color(rgb = (0.333, 0.278, 0.274)),
    "hair14" : Color(rgb = (0.227, 0.219, 0.223)),
    "hair15" : Color(rgb = (0.603, 0.388, 0.227)),
    "hair16" : Color(rgb = (0.835, 0.337, 0.211)),
    }

default eye_colours = {
    "eye0" : Color(rgb = (0.635, 0.423, 0.337)),
    "eye1" : Color(rgb = (0.545, 0.803, 0.886)),
    "eye2" : Color(rgb = (0.094, 0.509, 0.647)),
    "eye3" : Color(rgb = (0.337, 0.862, 0.298)),
    "eye4" : Color(rgb = (0.729, 0.780, 0.788)),
    "eye5" : Color(rgb = (0.4, 0.450, 0.458)),
    
    "eye6" : Color(rgb = (0.635, 0.423, 0.337)),
    "eye7" : Color(rgb = (0.545, 0.803, 0.886)),
    "eye8" : Color(rgb = (0.094, 0.509, 0.647)),
    "eye9" : Color(rgb = (0.337, 0.862, 0.298)),
    "eye10" : Color(rgb = (0.729, 0.780, 0.788)),
    "eye11" : Color(rgb = (0.4, 0.450, 0.458)),
    }

default desire_colours = {
    "1" : Color(rgb = (0.168, 0.486, 0.654)),
    "2" : Color(rgb = (0.333, 0.474, 0.662)),
    "3" : Color(rgb = (0.580, 0.450, 0.678)),
    "4" : Color(rgb = (0.854, 0.423, 0.698)),
    "5" : Color(rgb = (0.996, 0.411, 0.705)),
    "6" : Color(rgb = (0.439, 0.141, 0.141)),
    }
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
