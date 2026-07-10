image bg_checkpoint:
    get_background_filename("checkpoint")
    bg_tint_transform()

layeredimage bg_checkpoint_lobby:
    always "bg_checkpoint_lobby_scene"
    if paige_here() and not renpy.showing("paige"):
        "bg_checkpoint_lobby_people_recep"

image bg_trainstation_outside_layer:
    get_background_filename("trainstation_outside")
    bg_tint_transform()
image trainstation_outside_shutters_layer:
    "trainstation_outside_shutters"
    bg_tint_transform()
image bg_trainstation_outside_police_layer:
    "bg_trainstation_outside_police"
    bg_tint_transform()

layeredimage bg_trainstation_outside:

    always:
        "bg_trainstation_outside_layer"

    if t.hour in dark:
        "trainstation_outside_shutters_layer"
    if 6 <= t.hour <= 22:
        "bg_trainstation_outside_police_layer"

image bg_trainstation_platform_layer:
    get_background_filename("trainstation_platform", True, False)
    bg_tint_transform()
image bg_trainstation_platform_train_layer:
    "bg_trainstation_platform_train"
    bg_tint_transform()

layeredimage bg_trainstation_platform:

    always:
        "bg_trainstation_platform_layer"

    if (t.hour in (7,8,9) and t.wkday in ("Monday", "Thursday")) or (t.hour in (16, 17, 18) and t.wkday in ("Wednesday", "Sunday")):
        "bg_trainstation_platform_train_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
