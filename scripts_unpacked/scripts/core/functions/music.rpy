




init python:
    def music_location_play():
        if block_walk_music:
            return
        elif dis([dis_bus_interior, dis_misc, dis_walk]): 
            return
        track = "music_" + dis_cur.name
        if renpy.music.get_playing(channel='music') != globals()[track] and renpy.loadable(globals()[track]):
            renpy.music.play(globals()[track], "music", loop=True, fadeout=1.0, fadein=1.0, tight=True)


default block_walk_music = False

define main_menu_music = "audio/hayden-folker-to-see-the-past.mp3"
define music_intro = "audio/hayden-folker-the-way-out-despair.mp3"

define music_dis_residential = "audio/hayden-folker-grace.mp3"
define music_dis_school = "audio/hayden-folker-downpour.mp3"
define music_dis_revel = "audio/hayden-folker-i-spy.mp3"
define music_dis_lake = "audio/hayden-folker-parallax-mix-new-4.mp3"
define music_dis_checkpoint = "audio/hayden-folker-the-scavengers.mp3"
define music_dis_truckstop = "audio/hayden-folker-abandoned-the-outskirts.mp3"

define music_dis_haven = "audio/hayden-folker-drifting-away.mp3"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
