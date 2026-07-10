label haven_shower_dress:
    $ walk(loc_haven_shower)
    $ pc_dress_slow()
    $ acc_shower_dress()
    $ acc.makeup_on = True
    jump travel

label haven_shower_dress_call:
    $ walk(loc_haven_shower)
    $ pc_dress_slow()
    $ acc_shower_dress()
    $ acc.makeup_on = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
