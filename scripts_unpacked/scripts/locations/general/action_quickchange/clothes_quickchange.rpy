label clothes_quickchange_school:
    call clothes_quickchange_call from _call_clothes_quickchange_call
    $ tab_top = "school"
    jump clothes_quickchange_end

label clothes_quickchange_daily:
    call clothes_quickchange_call from _call_clothes_quickchange_call_1
    $ tab_top = "daily"
    jump clothes_quickchange_end

label clothes_quickchange_party:
    call clothes_quickchange_call from _call_clothes_quickchange_call_2
    $ tab_top = "party"
    jump clothes_quickchange_end

label clothes_quickchange_sport:
    call clothes_quickchange_call from _call_clothes_quickchange_call_3
    $ tab_top = "sport"
    jump clothes_quickchange_end

label clothes_quickchange_swim:
    call clothes_quickchange_call from _call_clothes_quickchange_call_4
    $ tab_top = "swim"
    jump clothes_quickchange_end

label clothes_quickchange_home:
    call clothes_quickchange_call from _call_clothes_quickchange_call_5
    $ tab_top = "home"
    jump clothes_quickchange_end

label clothes_quickchange_call:
    $ travel_walk(loc_cur.isolate_loc)
    $ player.face_worried()
    pause 0.5
    $ player.eye = 5
    pause 0.5
    $ player.eye = 6
    pause 0.5
    $ player.face_worried()
    pcm "No one around..."
    $ pc_striptease()
    pause 0.5
    return

label clothes_quickchange_end:
    $ pc_dress_slow()
    pcm "There we go."
    $ travel_walk(loc_from, arrival=True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
