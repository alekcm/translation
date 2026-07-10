image jaylee_pose_bed = LayeredImageProxy("jaylee_pose_bed_layered", Transform(align=(0.7, 0.0)))

layeredimage jaylee_pose_bed_layered:
    always "jaylee_pose_bed_base"  
    group pants_g:
        attribute pants default "jaylee_pose_bed_pants"
        attribute no_pants null
        attribute nude null

image jaylee_pose_stand = LayeredImageProxy("jaylee_pose_stand_layered", Transform(align=(0.5, 0.0)))

layeredimage jaylee_pose_stand_layered:
    always "jaylee_pose_stand_base"
    group pants_g:
        attribute pants default "jaylee_pose_stand_pants"
        attribute no_pants null
        attribute nude null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
