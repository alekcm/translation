init python:

    def bob_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if log.interactive("mq_01_b") and t.hour in (18,19,20,21,22,23,0,1,2):
            cur_location = loc_pub
        
        elif not bob.has_met or log.completed("Becoming the Fixer"): 
            cur_location = None
        elif t.hour in (20,21,22,23,0) and global_random_noon_number in (2,3,4,5,6):
            cur_location = loc_pub
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)
layeredimage bob:
    at sprite_highlight("bob")
    always:
        "bob_base"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
