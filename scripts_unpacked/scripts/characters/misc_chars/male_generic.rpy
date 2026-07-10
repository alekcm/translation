init python:

    def male_npc_create_all(race=True, scav=False):
        
        
        male_npc_create(race, scav)
        male2_npc_create(race, scav)
        male3_npc_create(race, scav)

    def male_npc_create(race=True, scav=False):
        male1_npc_create(race, scav)

    def male1_npc_create(race=True, scav=False):
        
        
        global male_npc_face, male_npc_outfit, male_npc_scale
        
        if scav or dis(dis_junkyard):
            male_npc_face = numgen(9,11)
        elif dis(dis_lake):
            male_npc_face = numgen(1,8)
        elif dis(dis_school):
            male_npc_face = random([3,7,8])
        else:
            male_npc_face = numgen(1,6)
        
        if race:
            npc_race_picker_1()
        
        if scav or dis(dis_junkyard):
            male_npc_outfit = numgen(29,33)
        elif dis(dis_lake):
            male_npc_outfit = numgen(24,28)
        elif dis(dis_school):
            male_npc_outfit = numgen(21,23)
        else:
            male_npc_outfit = numgen(1,19)
        
        if dis(dis_school):
            scale = numgen(97, 100)
        else:
            scale = numgen(97, 103)
        
        male_npc_scale = scale / float(100)

    def male2_npc_create(race=True, scav=False):
        global male_npc_face, male_npc2_face, male_npc2_outfit, male_npc2_scale
        
        if scav or dis(dis_junkyard):
            male_npc2_face = numgen(9,11)
        elif dis(dis_lake):
            male_npc2_face = numgen(1,8)
        elif dis(dis_school):
            male_npc2_face = random([3,7,8])
        else:
            male_npc2_face = numgen(1,6)
        
        if male_npc2_face == male_npc_face:
            
            male2_npc_create(race, scav)
        
        if race:
            npc_race_picker_2()
        
        if scav or dis(dis_junkyard):
            male_npc2_outfit = numgen(29,33)
        elif dis(dis_lake):
            male_npc2_outfit = numgen(24,28)
        elif dis(dis_school):
            male_npc2_outfit = numgen(21,23)
        else:
            male_npc2_outfit = numgen(1,19)
        
        if dis(dis_school):
            scale = numgen(97, 100)
        else:
            scale = numgen(97, 103)
        
        male_npc2_scale = scale / float(100)

    def male3_npc_create(race=True, scav=False):
        global male_npc_face, male_npc2_face, male_npc3_face, male_npc3_outfit, male_npc3_scale
        
        if scav or dis(dis_junkyard):
            male_npc3_face = numgen(9,11)
        elif dis(dis_lake):
            male_npc3_face = numgen(1,8)
        elif dis(dis_school):
            male_npc3_face = random([3,7,8])
        else:
            male_npc3_face = numgen(1,6)
        
        if(male_npc3_face == male_npc_face or male_npc3_face == male_npc2_face):
            
            male3_npc_create(race, scav)
        
        if race:
            npc_race_picker_3()
        
        if scav or dis(dis_junkyard):
            male_npc3_outfit = numgen(29,33)
        elif dis(dis_lake):
            male_npc3_outfit = numgen(24,28)
        elif dis(dis_school):
            male_npc3_outfit = numgen(21,23)
        else:
            male_npc3_outfit = numgen(1,19)
        
        if dis(dis_school):
            scale = numgen(97, 100)
        else:
            scale = numgen(97, 103)
        
        male_npc3_scale = scale / float(100)



    def get_male_face_pathname(layer="base"):
        return "male_face_" + str(male_npc_face) + "_" + layer
    def get_male_outfit_pathname():
        return "male_outfit_" + str(male_npc_outfit)

    def get_male2_face_pathname(layer="base"):
        return "male_face_" + str(male_npc2_face) + "_" + layer
    def get_male2_outfit_pathname():
        return "male_outfit_" + str(male_npc2_outfit)

    def get_male3_face_pathname(layer="base"):
        return "male_face_" + str(male_npc3_face) + "_" + layer
    def get_male3_outfit_pathname():
        return "male_outfit_" + str(male_npc3_outfit)

    def get_male_name():
        try:
            return tempname.name
        except NameError:
            return ""

default male_npc_face = 1
default male_npc_outfit = 1
default male_npc_scale = 1
default male_npc2_face = 1
default male_npc2_outfit = 1
default male_npc2_scale = 1
default male_npc3_face = 1
default male_npc3_outfit = 1
default male_npc3_scale = 1

image male_npc_face_base:
    get_male_face_pathname("base")
    npc_skin_base_colour_transform()
image male_npc_face_shad:
    get_male_face_pathname("shad")
    npc_skin_shad_colour_transform()
image male_npc_face_col:
    get_male_face_pathname("col")

image male2_npc_face_base:
    get_male2_face_pathname("base")
    npc2_skin_base_colour_transform()
image male2_npc_face_shad:
    get_male2_face_pathname("shad")
    npc2_skin_shad_colour_transform()
image male2_npc_face_col:
    get_male2_face_pathname("col")

image male3_npc_face_base:
    get_male3_face_pathname("base")
    npc3_skin_base_colour_transform()
image male3_npc_face_shad:
    get_male3_face_pathname("shad")
    npc3_skin_shad_colour_transform()
image male3_npc_face_col:
    get_male3_face_pathname("col")

image male_npc_body_base:
    "male_body_base"
    npc_skin_base_colour_transform()
image male_npc_body_shad:
    "male_body_shad"
    npc_skin_shad_colour_transform()

image male2_npc_body_base:
    "male_body_base"
    npc2_skin_base_colour_transform()
image male2_npc_body_shad:
    "male_body_shad"
    npc2_skin_shad_colour_transform()

image male3_npc_body_base:
    "male_body_base"
    npc3_skin_base_colour_transform()
image male3_npc_body_shad:
    "male_body_shad"
    npc3_skin_shad_colour_transform()

image male_npc_outfit:
    get_male_outfit_pathname()
image male2_npc_outfit:
    get_male2_outfit_pathname()
image male3_npc_outfit:
    get_male3_outfit_pathname()

layeredimage male_generic:
    at sprite_highlight("nothing")
    always "male_npc_body_base"
    always "male_npc_body_shad"

    always "male_npc_face_base"
    always "male_npc_face_shad" 
    always "male_npc_face_col"

    group clothes:
        attribute nude null
        attribute dressed "male_npc_outfit" default

layeredimage male2_generic:
    at sprite_highlight("nothing")

    always "male2_npc_body_base"
    always "male2_npc_body_shad"

    always "male2_npc_face_base"
    always "male2_npc_face_shad"
    always "male2_npc_face_col"

    group clothes:
        attribute nude null
        attribute dressed "male2_npc_outfit" default

layeredimage male3_generic:
    at sprite_highlight("nothing")

    always "male3_npc_body_base"
    always "male3_npc_body_shad"

    always "male3_npc_face_base"
    always "male3_npc_face_shad"
    always "male3_npc_face_col"

    group clothes:
        attribute nude null
        attribute dressed "male3_npc_outfit" default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
