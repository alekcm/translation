init python:
    def tired_home():
        if player.tired < 5:
            renpy.jump('world_tired_trigger')
        if t.hour in night and late_final_warning == False:
            renpy.jump('world_late_trigger')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
