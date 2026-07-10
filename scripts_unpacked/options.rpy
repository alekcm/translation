












define config.developer = True

define config.name = _("The Fixer")

define config.layers = [ 'bg_screen', 'pc_avatar', 'backgrounds', 'master', 'fg_bg_screen', 'fg_screen', 'transient', 'screens', 'overlay' ]




define gui.show_name = True




define config.version = "0.3.6.04"





define gui.about = _p("""
""")






define build.name = "TheFixer"







define config.has_sound = False
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "audio/hayden-folker-to-see-the-past.mp3"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15


define config.predict_statements = 0
define config.predict_statements_callback = None














define config.save_directory = "TheFixer-1582640956"






define config.window_icon = "gui/window_icon.webp"





init python:






















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('**.log', None)
    build.classify('**.yaml', None)


    build.archive("scripts", "all")
    build.archive("images", "all")


    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")


    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")







    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
