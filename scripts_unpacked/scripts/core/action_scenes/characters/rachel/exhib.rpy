image rachel_exhib_run = LayeredImageProxy("rachel_exhib_run_layered", Transform(align=(0.7, 0.0)))

layeredimage rachel_exhib_run_layered:

    always "rachel_exhib_run_base"
    if rachel.showing:
        "rachel_exhib_run_belly"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
