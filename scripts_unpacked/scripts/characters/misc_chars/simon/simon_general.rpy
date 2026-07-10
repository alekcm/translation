init python:
    def simon_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if log.interactive("mq_01_b") and t.hour in (18,19,20,21,22,23,0,1,2): 
            cur_location = loc_pub
        
        elif not simon.has_met: 
            cur_location = None
        elif t.hour in (20,21,22,23,0) and global_random_noon_number < 5: 
            cur_location = loc_pub
        elif loc_office_pi.opening_hours and loc_office_pi.open: 
            cur_location = loc_office_pi
        elif "has_key" in loc_office_pi.list: 
            
            if t.hour in (9,10,11):
                cur_location = None
            elif t.hour in irange(1,7): 
                cur_location= loc_office_pi_back
            else:
                cur_location = loc_office_pi
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

layeredimage simon:
    at sprite_highlight("simon")
    always:
        "simon_base"

    group face auto:
        attribute frown default

label simon_talk_subject:






    show simon at right1 with dissolve

    jump expression WeightedChoice([

    ("simon_talk_test", 100),

    ("simon_talk_test_stay", If(loc_office_pi_back.locked, 100, 0)),

    
    
    
    
    ])

label simon_talk_test:
    simon.name "Testing testing i am here"
    simon.name "test test am i wearing the right clothes?"
    jump simon_talk_end

label simon_talk_test_stay:
    simon.name "I don't have any dialogue yet. But you will be able to come and talk to me eventually."
    simon.name "If i like you enough, I will let you stay with me in the back office."
    simon.name "Of course this comes with the implication of sex."
    simon.name "But I will unlock the back area for you anyway and even if you dont stay, you can change and wash up."
    $ loc_office_pi_back.locked=False
    pc "How nice of you!"
    simon.name "I will also give you a key to the office, so you can come and go at any hour."
    $ add_to_list(loc_office_pi.list, "has_key")
    $ loc_office_pi.opening_hours=[]
    simon.name "For now this stuff is unlocked, but you will have to put in effort later."
    jump simon_talk_end

label simon_talk_end:
    $ relax(20, simon)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide simon with dissolve
    jump travel

label simon_work_picker:
    "No content yet"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
