image sb_againstwall_bg_layer:
    "sb_againstwall_bg"
    desire_colour_transform()

image sb_againstwall_body_base_layer:
    "sb_againstwall_body_base"
    skin_base_colour_transform()
image sb_againstwall_body_shad_layer:
    "sb_againstwall_body_shad"
    skin_shad_colour_transform()
image sb_againstwall_body_vag_layer:
    "sb_againstwall_body_vag"
    vagina_colour_transform()

image sb_againstwall_belly_base_layer:
    get_skin_filename("sb_againstwall_belly_base", True)
    skin_base_colour_transform()
image sb_againstwall_belly_shad_layer:
    get_skin_filename("sb_againstwall_belly_shad", True)
    skin_shad_colour_transform()

image sb_againstwall_penis_idle_base_layer:
    "sb_againstwall_penis_idle_base"
    npc_skin_base_colour_transform()
image sb_againstwall_penis_idle_shad_layer:
    "sb_againstwall_penis_idle_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall_penis_vagpoke_base_layer:
    "sb_againstwall_penis_vagpoke_base"
    npc_skin_base_colour_transform()
image sb_againstwall_penis_vagpoke_shad_layer:
    "sb_againstwall_penis_vagpoke_shad"
    npc_skin_shad_colour_transform()
image sb_againstwall_hand_vagpoke_base_layer:
    "sb_againstwall_hand_vagpoke_base"
    npc_skin_base_colour_transform()
image sb_againstwall_hand_vagpoke_shad_layer:
    "sb_againstwall_hand_vagpoke_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall_penis_vagin_base_layer:
    "sb_againstwall_penis_vagin_base"
    npc_skin_base_colour_transform()
image sb_againstwall_penis_vagin_vag_layer:
    "sb_againstwall_penis_vagin_vag"
    vagina_colour_transform()
image sb_againstwall_penis_vagin_shad_layer:
    "sb_againstwall_penis_vagin_shad"
    npc_skin_shad_colour_transform()



image sb_againstwall_penis_asspoke_base_layer:
    "sb_againstwall_penis_asspoke_base"
    npc_skin_base_colour_transform()
image sb_againstwall_penis_asspoke_shad_layer:
    "sb_againstwall_penis_asspoke_shad"
    npc_skin_shad_colour_transform()
image sb_againstwall_hand_asspoke_base_layer:
    "sb_againstwall_hand_asspoke_base"
    npc_skin_base_colour_transform()
image sb_againstwall_hand_asspoke_shad_layer:
    "sb_againstwall_hand_asspoke_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall_penis_assin_base_layer:
    "sb_againstwall_penis_assin_base"
    npc_skin_base_colour_transform()
image sb_againstwall_penis_assin_shad_layer:
    "sb_againstwall_penis_assin_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall_penis_cumout_base_layer:
    "sb_againstwall_penis_cumout_base"
    npc_skin_base_colour_transform()
image sb_againstwall_penis_cumout_shad_layer:
    "sb_againstwall_penis_cumout_shad"
    npc_skin_shad_colour_transform()

layeredimage sb_againstwall:

    always:
        "sb_againstwall_bg_layer"




    always:
        "sb_againstwall_body_base_layer"
    always:
        "sb_againstwall_body_shad_layer"
    always:
        "sb_againstwall_body_vag_layer"

    always:
        "sb_againstwall_belly_base_layer"
    always:
        "sb_againstwall_belly_shad_layer"

    if player.cum_locations["cum_vagin"]:
        "sb_againstwall_body_cum_vag"
    if player.cum_locations["cum_assin"]:
        "sb_againstwall_body_cum_anal"
    if player.cum_locations["cum_assout"] or player.cum_locations["cum_vagout"]:
        "sb_againstwall_body_cum_out"



    group penis:
        attribute nopenis:
            null

        attribute wait default:
            "sb_againstwall_penis_idle_base_layer"
        attribute wait default:
            "sb_againstwall_penis_idle_shad_layer"

        attribute vagpoke:
            "sb_againstwall_penis_vagpoke_base_layer"
        attribute vagpoke:
            "sb_againstwall_penis_vagpoke_shad_layer"


        attribute vagpoke_hand:
            "sb_againstwall_penis_vagpoke_base_layer"
        attribute vagpoke_hand:
            "sb_againstwall_penis_vagpoke_shad_layer"
        attribute vagpoke_hand:
            "sb_againstwall_hand_vagpoke_base_layer"
        attribute vagpoke_hand:
            "sb_againstwall_hand_vagpoke_shad_layer"


        attribute vagin:
            "sb_againstwall_penis_vagin_base_layer"
        attribute vagin:
            "sb_againstwall_penis_vagin_vag_layer"
        attribute vagin:
            "sb_againstwall_penis_vagin_shad_layer"



        attribute asspoke:
            "sb_againstwall_penis_asspoke_base_layer"
        attribute asspoke:
            "sb_againstwall_penis_asspoke_shad_layer"


        attribute asspoke_hand:
            "sb_againstwall_penis_asspoke_base_layer"
        attribute asspoke_hand:
            "sb_againstwall_penis_asspoke_shad_layer"
        attribute asspoke_hand:
            "sb_againstwall_hand_asspoke_base_layer"
        attribute asspoke_hand:
            "sb_againstwall_hand_asspoke_shad_layer"

        attribute assin:
            "sb_againstwall_penis_assin_base_layer"
        attribute assin:
            "sb_againstwall_penis_assin_shad_layer"



        attribute cumout:
            "sb_againstwall_penis_cumout_base_layer"
        attribute cumout:
            "sb_againstwall_penis_cumout_shad_layer"
    always:
        "sb_againstwall_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
