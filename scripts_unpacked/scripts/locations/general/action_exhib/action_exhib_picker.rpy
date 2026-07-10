label action_strip_event_tombola:
    $ walk(loc_cur.isolate_loc)
    $ player.eye = 5
    pause 0.4
    $ player.eye = 6
    pause 0.4
    $ player.eye = 1
    pcm "Mmmm..."
    $ pc_striptease(True)
    pcm "Better keep my clothes close in case I need them."
    $ walk(loc_from)
    $ renpy.show(random(["sb_pose_showbreasts happy forward", "sb_pose_lookback smile"]))
    with dissolve
    pcm "Like what you see perverts?"
    pcm "Hehe."
    $ renpy.scene()
    with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
