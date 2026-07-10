init python:
    def shane_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        text_desc = ""
        
        if t.time_from_to(09.00, 18.00): 
            cur_location = dis_school
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

image shane_sick_layer:
    "shane_sick"
    matrixcolor OpacityMatrix(If(t.day - shane.dict["took_poison"] >= 10, 1, (t.day - shane.dict["took_poison"]) / float(10)))

layeredimage shane:
    at sprite_highlight("shane")
    always "shane_main"
    if "poisoned" in shane.list:
        "shane_sick_layer"
    group face auto:
        attribute frown default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
