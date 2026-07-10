image robin_facesit_pc_base_layer:
    "robin_facesit_pc_base"
    skin_base_colour_transform()
image robin_facesit_pc_shad_layer:
    "robin_facesit_pc_shad"
    skin_shad_colour_transform()
image robin_facesit_pc_hair_layer:
    "robin_facesit_pc_hair"
    hair_colour_transform()

image robin_facesit_pc_det_eyeshadow_layer:
    "robin_facesit_pc_det_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image robin_facesit_pc_det_lips_layer:
    "robin_facesit_pc_det_lips"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image robin_facesit_pc_det_freckles_layer:
    "robin_facesit_pc_det_freckles"
    skin_shad_colour_transform()
image robin_facesit_pc_det_nails_layer:
    "robin_facesit_pc_det_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image robin_facesit_pc_eye_down_iris_layer:
    "robin_facesit_pc_eye_down_iris"
    eye_colour_transform()
image robin_facesit_pc_eye_up_iris_layer:
    "robin_facesit_pc_eye_up_iris"
    eye_colour_transform()
image robin_facesit_pc_eye_up_eyeliner_layer:
    "robin_facesit_pc_eye_up_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image robin_facesit_pc_eye_down_eyeliner_layer:
    "robin_facesit_pc_eye_down_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")


image robin_facesit_man_vag_base_layer:
    "robin_facesit_man_vag_base"
    npc_skin_base_colour_transform()
image robin_facesit_man_vag_shad_layer:
    "robin_facesit_man_vag_shad"
    npc_skin_shad_colour_transform()

image robin_facesit_man_anal_base_layer:
    "robin_facesit_man_anal_base"
    npc_skin_base_colour_transform()
image robin_facesit_man_anal_shad_layer:
    "robin_facesit_man_anal_shad"
    npc_skin_shad_colour_transform()

image robin_facesit_man_mast_base_layer:
    "robin_facesit_man_mast_base"
    npc_skin_base_colour_transform()
image robin_facesit_man_mast_shad_layer:
    "robin_facesit_man_mast_shad"
    npc_skin_shad_colour_transform()



image robin_facesit = LayeredImageProxy("robin_facesit_layered", Transform(align=(0.7, 0.0)))

layeredimage robin_facesit_layered:
    always "robin_facesit_bg"

    group mess_effect:
        attribute nomess null default
        attribute mess "robin_facesit_mess"

    always "robin_facesit_pc_base_layer"
    always "robin_facesit_pc_shad_layer"
    always "robin_facesit_pc_hair_layer"

    always "robin_facesit_pc_det_eyeshadow_layer"
    always "robin_facesit_pc_det_lips_layer"
    always "robin_facesit_pc_det_nails_layer"
    if skin_effect.face:
        "robin_facesit_pc_det_freckles_layer"

    group eyes:
        attribute up "robin_facesit_pc_eye_up_iris_layer" default
        attribute up "robin_facesit_pc_eye_up_eyes" default
        attribute up "robin_facesit_pc_eye_up_eyeliner_layer" default

        attribute down "robin_facesit_pc_eye_down_iris_layer"
        attribute down "robin_facesit_pc_eye_down_eyes"
        attribute down "robin_facesit_pc_eye_down_eyeliner_layer"

    group mess_effect:
        attribute nomess null default
        attribute mess "robin_facesit_cum"
        attribute cum "robin_facesit_cum"

    group man:
        attribute noman null default

        attribute vag "robin_facesit_man_vag_base_layer"
        attribute vag "robin_facesit_man_vag_shad_layer"

        attribute anal "robin_facesit_man_anal_base_layer"
        attribute anal "robin_facesit_man_anal_shad_layer"

        attribute mast "robin_facesit_man_mast_base_layer"
        attribute mast "robin_facesit_man_mast_shad_layer"

    always "robin_facesit_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
