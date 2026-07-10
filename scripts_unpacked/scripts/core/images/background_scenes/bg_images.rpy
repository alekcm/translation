init python:

    bg_scene_dummy_bool = True
    bg_sky_dummy_bool = False
    bg_mood_dummy_bool = True
    def bg_scene_dummy():
        global bg_scene_dummy_bool
        bg_scene_dummy_bool = not bg_scene_dummy_bool
        return " bg_scene_dummy_attribute" if bg_scene_dummy_bool else ""
    def bg_sky_dummy():
        global bg_sky_dummy_bool
        bg_sky_dummy_bool = not bg_sky_dummy_bool
        return " bg_sky_dummy_attribute" if bg_sky_dummy_bool else ""
    def bg_moodscene_dummy():
        global bg_mood_dummy_bool
        bg_mood_dummy_bool = not bg_mood_dummy_bool
        return " bg_moodscene_dummy_attribute" if bg_mood_dummy_bool else ""

image bg_scene_image:
    get_background_imagename()

layeredimage bg_scene:
    group dummy:
        attribute bg_scene_dummy_attribute:
            null
    always:
        "bg_scene_image"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
