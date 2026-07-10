label loc_mall_closed:
    if t.timeofday == "night":
        pc "Im too late, the mall closes at 22:00. I'll have to come back tomorrow."
    else:
        pc "The Mall isn't open yet. It opens at 8:00"

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
