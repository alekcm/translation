

























































define action_bg = 0
define action_againstwall = 1


image againstwall_a = LayeredImageProxy("againstwall", Transform(align=(0.5, 0.2)))







screen againstwall_screen(xa, ya):
    zorder 5
    add "againstwall":
        zoom .6

        at transform:
            align (xa, ya)
            linear 0.5 alpha 1.0
screen spank(xa, ya):
    zorder 6
    frame pos (xa, ya) at icon_fadeout:
        background None
        add "beer"
    timer 1.0 action Hide('drink')
layeredimage againstwall:

    group bgscene:
        attribute red:
            "against_wall_bg_red"
        attribute pink default:
            "against_wall_bg_pink"
    if player.drunk >= 60 or player.high >= 40:
        "against_wall_bg_drunk"
    if player.desire >= 60:
        "against_wall_bg_horny"





    group actionscene:





        attribute wait:
            "against_wall_pc_back_wait"
        attribute jerkhighslow:
            "against_wall_pc_back_wait"
        attribute jerkhigh:
            "against_wall_pc_back_wait"
        attribute jerklow:
            "against_wall_pc_back_wait"
        attribute jerklowfast:
            "against_wall_pc_back_wait"
        attribute insert1:
            "against_wall_pc_back_insert1"
        attribute insert2:
            "against_wall_pc_back_insert2"
        attribute poke:
            "against_wall_pc_back_poke"
        attribute pokerandom:
            "against_wall_pc_back_pokerandom"
        attribute pokedeeperfull:
            "against_wall_pc_back_pokedeeperfull"
        attribute pokedeeper:
            "against_wall_pc_back_pokedeeper"
        attribute insertfull:
            "against_wall_pc_back_insertfull"
        attribute insertpoke:
            "against_wall_pc_back_insertpoke"
        attribute loopslow:
            "against_wall_pc_back_loop_s"
        attribute loop:
            "against_wall_pc_back_loop_n"
        attribute loopfast:
            "against_wall_pc_back_loop_f"
        attribute cumdeep:
            "against_wall_pc_back_cumdeep"
        attribute cumdeep_pullout:
            "against_wall_pc_back_cumdeep_pullout"
        attribute cumpoke:
            "against_wall_pc_back_cumpoke"
        attribute cumpoke_pullout:
            "against_wall_pc_back_cumpoke_pullout"
        attribute cumonass:
            "against_wall_pc_back_cumonass"
        attribute pokecumonass:
            "against_wall_pc_back_pokecumonass"
        attribute cumonassjerkhigh:
            "against_wall_pc_back_cumonassjerkhigh"




        attribute wait:
            "against_wall_pc_front_wait"
        attribute jerkhighslow:
            "against_wall_pc_front_wait"
        attribute jerkhigh:
            "against_wall_pc_front_wait"
        attribute jerklow:
            "against_wall_pc_front_wait"
        attribute jerklowfast:
            "against_wall_pc_front_wait"
        attribute insert1:
            "against_wall_pc_front_insert1"
        attribute insert2:
            "against_wall_pc_front_insert2"
        attribute poke:
            "against_wall_pc_front_poke"
        attribute pokerandom:
            "against_wall_pc_front_pokerandom"
        attribute pokedeeperfull:
            "against_wall_pc_front_pokedeeperfull"
        attribute pokedeeper:
            "against_wall_pc_front_pokedeeper"
        attribute insertfull:
            "against_wall_pc_front_insertfull"
        attribute insertpoke:
            "against_wall_pc_front_insertpoke"
        attribute loopslow:
            "against_wall_pc_front_loop_s"
        attribute loop:
            "against_wall_pc_front_loop_n"
        attribute loopfast:
            "against_wall_pc_front_loop_f"
        attribute cumdeep:
            "against_wall_pc_front_cumdeep"
        attribute cumdeep_pullout:
            "against_wall_pc_front_cumdeep_pullout"
        attribute cumpoke:
            "against_wall_pc_front_cumpoke"
        attribute cumpoke_pullout:
            "against_wall_pc_front_cumpoke_pullout"
        attribute cumonass:
            "against_wall_pc_front_cumonass"
        attribute pokecumonass:
            "against_wall_pc_front_pokecumonass"
        attribute cumonassjerkhigh:
            "against_wall_pc_front_cumonassjerkhigh"





        attribute jerkhighslow:
            "against_wall_man_back_jerkhighslow"
        attribute jerkhigh:
            "against_wall_man_back_jerkhigh"
        attribute jerklow:
            "against_wall_man_back_jerklow"
        attribute jerklowfast:
            "against_wall_man_back_jerklowfast"
        attribute insert1:
            "against_wall_man_back_insert1"
        attribute insert2:
            "against_wall_man_back_insert2"
        attribute poke:
            "against_wall_man_back_poke"
        attribute pokerandom:
            "against_wall_man_back_pokerandom"
        attribute pokedeeperfull:
            "against_wall_man_back_pokedeeperfull"
        attribute pokedeeper:
            "against_wall_man_back_pokedeeper"
        attribute insertfull:
            "against_wall_man_back_insertfull"
        attribute insertpoke:
            "against_wall_man_back_insertpoke"
        attribute loopslow:
            "against_wall_man_back_loop_s"
        attribute loop:
            "against_wall_man_back_loop_n"
        attribute loopfast:
            "against_wall_man_back_loop_f"
        attribute cumdeep:
            "against_wall_man_back_cumdeep"
        attribute cumdeep_pullout:
            "against_wall_man_back_cumdeep_pullout"
        attribute cumpoke:
            "against_wall_man_back_cumpoke"
        attribute cumpoke_pullout:
            "against_wall_man_back_cumpoke_pullout"
        attribute cumonass:
            "against_wall_man_back_cumonass"
        attribute pokecumonass:
            "against_wall_man_back_pokecumonass"
        attribute cumonassjerkhigh:
            "against_wall_man_back_cumonassjerkhigh"





        attribute jerkhighslow:
            "against_wall_man_front_jerkhighslow"
        attribute jerkhigh:
            "against_wall_man_front_jerkhigh"
        attribute jerklow:
            "against_wall_man_front_jerklow"
        attribute jerklowfast:
            "against_wall_man_front_jerklowfast"
        attribute insert1:
            "against_wall_man_front_insert1"
        attribute insert2:
            "against_wall_man_front_insert2"
        attribute poke:
            "against_wall_man_front_poke"
        attribute pokerandom:
            "against_wall_man_front_pokerandom"
        attribute pokedeeperfull:
            "against_wall_man_front_pokedeeperfull"
        attribute pokedeeper:
            "against_wall_man_front_pokedeeper"
        attribute insertfull:
            "against_wall_man_front_insertfull"
        attribute insertpoke:
            "against_wall_man_front_insertpoke"
        attribute loopslow:
            "against_wall_man_front_loop_s"
        attribute loop:
            "against_wall_man_front_loop_n"
        attribute loopfast:
            "against_wall_man_front_loop_f"
        attribute cumdeep:
            "against_wall_man_front_cumdeep"
        attribute cumdeep_pullout:
            "against_wall_man_front_cumdeep_pullout"
        attribute cumpoke:
            "against_wall_man_front_cumpoke"
        attribute cumpoke_pullout:
            "against_wall_man_front_cumpoke_pullout"
        attribute cumonass:
            "against_wall_man_front_cumonass"
        attribute pokecumonass:
            "against_wall_man_front_pokecumonass"
        attribute cumonassjerkhigh:
            "against_wall_man_front_cumonassjerkhigh"



    always:
        "against_wall_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
