image rachel_pose_peace = LayeredImageProxy("rachel_pose_peace_layered", Transform(align=(0.7, 0.0)))

layeredimage rachel_pose_peace_layered:

    always "rachel_pose_peace_base"
    if rachel.heavy_preg:
        "rachel_pose_peace_preg_2"
    elif rachel.showing:
        "rachel_pose_peace_preg_1"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
