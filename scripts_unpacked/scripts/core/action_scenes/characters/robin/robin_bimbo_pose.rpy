image robin_bimbo_pose_front_bg_layer:
    "robin_bimbo_pose_front_bg_" + loc_cur.loc_type

layeredimage robin_bimbo_pose_front:
    always "robin_bimbo_pose_front_bg_layer"
    always "robin_bimbo_pose_front_base"

    group underwear:
        attribute thong default:
            "robin_bimbo_pose_front_thong"
        attribute no_thong:
            null

    group outfit:
        attribute bimbo default:
            "robin_bimbo_pose_front_bimbo"
        attribute slut:
            "robin_bimbo_pose_front_slut"
        attribute no_outfit:
            null

image robin_bimbo_pose_back_bg_layer:
    "robin_bimbo_pose_back_bg_" + loc_cur.loc_type

layeredimage robin_bimbo_pose_back:
    always "robin_bimbo_pose_back_bg_layer"
    always "robin_bimbo_pose_back_base"

    group underwear:
        attribute thong default:
            "robin_bimbo_pose_back_thong"
        attribute no_thong:
            null

    group outfit:
        attribute bimbo default:
            "robin_bimbo_pose_back_bimbo"
        attribute slut:
            "robin_bimbo_pose_back_slut"
        attribute no_outfit:
            null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
