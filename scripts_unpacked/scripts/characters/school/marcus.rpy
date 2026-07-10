init python:
    def marcus_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        text_desc = ""
        
        if t.time_from_to(09.00, 18.00): 
            cur_location = dis_school
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

image marcus_sick_layer:
    "marcus_sick"
    matrixcolor OpacityMatrix(If(t.day - shane.dict["took_poison"] >= 10, 1, (t.day - shane.dict["took_poison"]) / float(10)))

layeredimage marcus:
    at sprite_highlight("marcus")
    always "marcus_main"
    if "poisoned" in shane.list:
        "marcus_sick_layer"
    group face auto:
        attribute smile default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
