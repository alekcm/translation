label stairwell_check:
    "Test just to check"
    if c.exposed:
        "I need to dress properly before leaving the house."
        jump travel
    $ travel_walk(loc_stairwell, 2, True)

label loc_stairwell_kicked_out:
    if "kicked_out" in loc_stairwell.list:
        pcm "[oskar.name] had me mugged and raped last time. I better not hang around or worse might happen..."
        pcm "Suppose I should find somewhere else to live..."
        python:
            for i in [loc_kitchen, loc_bedroom, loc_common, loc_bathroom, loc_bedroom_robin]:
                
                
                i.locked=True
                add_to_list(i.list, "kicked_out")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
