init -1:
    transform avatar_floating_effect(xa, ya, pausetime):

        alpha 0
        zoom 0.4
        xalign xa
        yalign ya

        parallel:
            linear 8 yoffset -600
        parallel:
            ease_quad 2 xoffset -15
            ease_quad 2 xoffset 15
            ease_quad 2 xoffset -15
            ease_quad 2 xoffset 15
        parallel:
            easein 4 alpha 0.4
        parallel:
            easeout 8 zoom 2
        parallel:
            pause 4
            easein 3 alpha 0.0
        pause pausetime
        linear 0.1 yoffset 600
        repeat

    transform avatar_spinning_effect:
        anchor (0.5,0.5)
        xpos 230
        ypos 215
        zoom 1.3

        linear 32 rotate 360
        linear 0 rotate -360
        repeat

    transform avatar_bubble_big_effect(a_size=0.8, a_height=150, a_side=60, a_delay=0):
        alpha 0
        anchor (0.0, 1.0)


        xpos 320
        ypos 185

        zoom 0.1


        pause a_delay
        parallel:
            easeout 0.5 alpha 1
        parallel:
            linear 8 yoffset -a_height
        parallel:
            easein_elastic 15 xoffset a_side
        parallel:
            pause 2
            easeout_bounce 6 alpha 0
        parallel:
            linear 8 zoom a_size
        pause a_delay
        yoffset a_height
        xoffset -a_side
        repeat

image effect_heart1 = "effect_heart"
image effect_heart2 = "effect_heart"
image effect_heart3 = "effect_heart"
image effect_heart4 = "effect_heart"
image effect_heart5 = "effect_heart"
image effect_heart6 = "effect_heart"

image effect_bubble1 = "effect_bubble"
image effect_bubble2 = "effect_bubble"
image effect_bubble3 = "effect_bubble"
image effect_bubble4 = "effect_bubble"
image effect_bubble5 = "effect_bubble"
image effect_bubble6 = "effect_bubble"

image inventory_hover:
    "inventory_idle"
    matrixcolor TintMatrix("#b23f73")
image diary_hover:
    "diary_idle"
    matrixcolor TintMatrix("#b23f73")
image cheats_hover:
    "cheats_idle"
    matrixcolor TintMatrix("#b23f73")

screen avatar_floating_heart():
    zorder 6
    frame align (0.5,0.5) anchor (0.5,0.5) at avatar_floating_effect:
        background None
        add "effect_heart"
    timer 2 action Hide ('avatar_floating_heart')

define bubble_say = Frame("gui/bubble_speech.webp", 24, 7, 0, 19)
define bubble_thought = Frame("gui/bubble_thought.webp", 49, 39, 16, 34)
define bubble_burst = Frame("gui/bubble_burst.webp", 82, 31, 17, 33)

screen text_char_speak(text, how="thought"):

    layer "pc_avatar"

    if how == "say":
        frame anchor (0.0,1.0) pos (340, 320) padding (29, 4, -21, 19) xmaximum 500 xminimum 300 background bubble_say at text_hov_fade:
            text "[text]" style "hover_font_style" font "BRLNSB.TTF" size 25 align (0.0, 0.5)
    elif how == "burst":
        frame anchor (0.0,1.0) pos (340, 320) padding (77, 13, -21, 39) xmaximum 500 xminimum 300 yminimum 40 background bubble_burst at text_hov_fade:
            text "[text]" style "hover_font_style" font "BRLNSB.TTF" size 25 align (0.0, 0.5)
    else:
        frame anchor (0.0,1.0) pos (340, 320) padding (50, 24, 1, 19) xmaximum 500 xminimum 300 background bubble_thought at text_hov_fade:
            text "[text]" style "hover_font_style" font "BRLNSB.TTF" size 25 align (0.0, 0.5)

    timer 2 action [Hide('text_char_speak'), Function(player.face_normal), Function(player.cover_reset)]

screen pc_avatar_womb():
    zorder 10
    if player.pregnant and player.preg_knows:
        add "pc_womb" pos (0, 100)
    timer 2 action [Hide('pc_avatar_womb')]
init python:

    def can_show_menu():
        if not renpy.get_screen("travel_screen"):
            
            return False
        else:
            return True












    pc_avatar_dummy_bool = True
    pc_avatar_dummy_attribute = ""

    def pc_avatar_dummy(): 
        global pc_avatar_dummy_bool
        pc_avatar_dummy_bool = False
        return pc_avatar_dummy_attribute

    def refresh_avatar():
        global pc_avatar_dummy_bool, pc_avatar_dummy_attribute
        if not pc_avatar_dummy_bool:
            pc_avatar_dummy_bool = True
            pc_avatar_dummy_attribute = "pc_dummy_attribute" if pc_avatar_dummy_attribute == "" else ""


    def hud_interact_reset():
        player.cover_reset()
        player.face_normal()
        renpy.hide_screen("text_char_speak")

    def pc_avatar_eye_interact():
        hud_interact_reset()
        
        player.brow = 3
        player.eye = 3
        player.mouth = 8
        if not numgen(0,40):
            renpy.jump("action_pc_interact_eye_tombola")
        else:
            renpy.show_screen("text_char_speak", text=rlist.avatar_react_exclaim_suprise, how="burst")

    def pc_avatar_boob_interact():
        hud_interact_reset()
        if player.has_perk(perk_lactating):
            player.cover_breasts_force()
            player.eye = 6
        elif player.check_horny():
            player.eye = 6
            player.brow = 2
            player.mouth = 3 
        else:
            player.cover_breasts_force()
            player.face_annoyed()
            player.eye = 6
        if player.has_perk(perk_lactating) and item_breastpump_can_use():
            renpy.jump("item_breastpump_action_jump")
        elif not numgen(0,50):
            renpy.jump("action_pc_interact_breasts_tombola")
        else:
            renpy.show_screen("text_char_speak", text=rlist.avatar_touch_breasts_comment)

    def pc_avatar_vag_interact():
        hud_interact_reset()
        if player.check_horny(extreme=True):
            player.face_orgasm()
        
        
        elif player.check_horny():
            player.cover_vag_force()
            player.face_shock()
            player.eye = 5
        else:
            player.cover_vag_force()
            player.face_angry()
            player.eye = 5
        
        if perversion_can_trigger_mast():
            renpy.jump("action_mast_event_start")
        else:
            renpy.show_screen("text_char_speak", text=rlist.avatar_touch_vag_comment)

    def pc_avatar_belly_interact():
        hud_interact_reset()
        renpy.hide_screen("pc_avatar_womb")
        if player.preg_knows:
            if player.rapebaby:
                player.face_angry()
            elif player.soldbaby or player.has_perk(perk_unwanted_preg):
                player.face_annoyed()
            elif player.has_perk(perk_wanted_preg):
                player.face_happy()
            else:
                player.face_worried()
        
        else: 
            if player.fitness > 60:
                player.face_happy()
            
            elif player.fitness < 30:
                player.face_worried()
            else:
                player.face_neutral()
        
        
        renpy.show_screen("text_char_speak", text=rlist.avatar_touch_belly_comment)
        renpy.show_screen("pc_avatar_womb")

screen pc_avatar:
    zorder 1

    if can_show_menu():
        imagebutton:
            xalign 0.12 yalign 0.24
            idle "images/characters/pc/buttons/pc_button_eyes.png"
            action Function(pc_avatar_eye_interact)

        imagebutton:
            xalign 0.115 yalign 0.46
            idle "images/characters/pc/buttons/pc_button_breasts.png"
            action Function(pc_avatar_boob_interact)

        imagebutton:
            xalign 0.12 yalign 0.73
            idle "images/characters/pc/buttons/pc_button_vag.png"
            action Function (pc_avatar_vag_interact)

        imagebutton:
            xalign 0.12 yalign 0.6
            idle "images/characters/pc/buttons/pc_button_belly.png"
            action Function (pc_avatar_belly_interact)

    if player.drunk >= 100:
        add "pc_face_mood_blackout" at avatar_spinning_effect

    if player.desire >= 200:
        add "effect_heart2" at avatar_floating_effect(0.25,0.2,6)
        add "effect_heart3" at avatar_floating_effect(0.03,0.8,5)


    $ colour_dawn = Color(rgb = (0.905, 0.768, 0.596))
    $ colour_night = Color(rgb = (0.458, 0.470, 0.6))


    add "pc " + pc_avatar_dummy() xalign 0.0 yalign 1.0





    if player.desire >= 800:
        add "effect_heart1" at avatar_floating_effect(0.1,0.3,7)
        add "effect_heart4" at avatar_floating_effect(0.2,0.6,4)
        add "effect_heart5" at avatar_floating_effect(0.15,0.5,6)

    if player.drunk >= 60:
        add "effect_bubble1" at avatar_bubble_big_effect
        add "effect_bubble2" at avatar_bubble_big_effect(0.2, 150, 50, 2)
    if player.drunk >= 100:
        add "effect_bubble3" at avatar_bubble_big_effect(0.2, 150, 20, 4)
        add "effect_bubble4" at avatar_bubble_big_effect(0.3, 150, 30, 2)
    if player.drunk >= 130:
        add "effect_bubble5" at avatar_bubble_big_effect(0.2, 150, 10, 3)
        add "effect_bubble6" at avatar_bubble_big_effect(0.3, 150, 5, 1)

screen right_menu_button_desire():
    frame padding (0, 0) xysize (46,46) background None:
        if player.check_horny(extreme=True) or player.has_perk(perk_lebo):
            add "images/ui/stat_icons/heart_fire.png"
        imagebutton:
            if player.recovering:
                idle "images/ui/stat_icons/heart_broke.png"
                hover "images/ui/stat_icons/heart_broke_h.png"
            else:
                if player.desire < 100:
                    idle "images/ui/stat_icons/heart_1.png"
                elif player.desire < 200:
                    idle "images/ui/stat_icons/heart_2.png"
                elif player.desire < 400:
                    idle "images/ui/stat_icons/heart_3.png"
                elif player.desire < 600:
                    idle "images/ui/stat_icons/heart_4.png"
                else:
                    idle "images/ui/stat_icons/heart_5.png"
                hover "images/ui/stat_icons/heart_h.png"
                if can_show_menu():
                    action [Function(hud_interact_reset), Function(player.face_icon_desire), Show("text_char_speak", text=rlist.hud_desire_press_comment)]
        if player.recovering:
            text "X" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"
        elif player.has_perk(perk_lebo):
            text "#" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"
        else:
            text "[player.desire]" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"

screen right_menu_button_allure():
    frame padding (0, 0) xysize (46,46) background None:
        imagebutton:
            if player.allure <= 0:
                idle "images/ui/stat_icons/allure_0.png"
            elif player.allure < 100:
                idle "images/ui/stat_icons/allure_1.png"
            elif player.allure < 200:
                idle "images/ui/stat_icons/allure_2.png"
            elif player.allure < 300:
                idle "images/ui/stat_icons/allure_3.png"
            elif player.allure < 400:
                idle "images/ui/stat_icons/allure_4.png"
            elif player.allure < 500:
                idle "images/ui/stat_icons/allure_5.png"
            else:
                idle "images/ui/stat_icons/allure_6.png"
            hover "images/ui/stat_icons/allure_h.png"
            if can_show_menu():
                action [Function(hud_interact_reset), Function(player.face_icon_allure), Show("text_char_speak", text=rlist.hud_allure_press_comment)]

        text "[player.allure]" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"

screen right_menu_button_tired():
    frame padding (0, 0) xysize (46,46) background None:
        imagebutton:
            if player.tired >= 80:
                idle "images/ui/stat_icons/sleep_green.png"
            elif player.tired >= 60:
                idle "images/ui/stat_icons/sleep_lgreen.png"
            elif player.tired >= 40:
                idle "images/ui/stat_icons/sleep_yellow.png"
            elif player.tired >= 20:
                idle "images/ui/stat_icons/sleep_orange.png"
            else:
                idle "images/ui/stat_icons/sleep_red.png"
            hover "images/ui/stat_icons/sleep_h.png"
            if can_show_menu():
                action [Function(hud_interact_reset), Function(player.face_icon_tired), Show("text_char_speak", text=rlist.hud_tired_press_comment)]

        text "[player.tired]" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"

screen right_menu_button_mood():
    frame padding (0, 0) xysize (46,46) background None:
        imagebutton:
            if player.has_perk(perk_joy):
                idle "images/ui/stat_icons/mood_maxhappy.png"
                hover "images/ui/stat_icons/mood_maxhappy_h.png"
            elif player.has_perk(perk_despondent):
                idle "images/ui/stat_icons/mood_desp.png"
                hover "images/ui/stat_icons/mood_desp_h.png"
            elif player.mood >= 80:
                idle "images/ui/stat_icons/mood_vhappy.png"
                hover "images/ui/stat_icons/mood_vhappy_h.png"
            elif player.mood >= 60:
                idle "images/ui/stat_icons/mood_happy.png"
                hover "images/ui/stat_icons/mood_happy_h.png"
            elif player.mood >= 40:
                idle "images/ui/stat_icons/mood_neutral.png"
                hover "images/ui/stat_icons/mood_neutral_h.png"
            elif player.mood >= 20:
                idle "images/ui/stat_icons/mood_sad.png"
                hover "images/ui/stat_icons/mood_sad_h.png"
            else:
                idle "images/ui/stat_icons/mood_vsad.png"
                hover "images/ui/stat_icons/mood_vsad_h.png"

            if can_show_menu():
                action [Function(hud_interact_reset), Function(player.face_icon_mood), Show("text_char_speak", text=rlist.hud_mood_press_comment)]
        text "[player.mood]" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"

screen right_menu_button_conf():
    frame padding (0, 0) xysize (46,46) background None:
        imagebutton:
            if player.confidence > 80:
                idle "images/ui/stat_icons/conf_5.png"
            elif player.confidence > 60:
                idle "images/ui/stat_icons/conf_4.png"
            elif player.confidence > 40:
                idle "images/ui/stat_icons/conf_3.png"
            elif player.confidence > 20:
                idle "images/ui/stat_icons/conf_2.png"
            else:
                idle "images/ui/stat_icons/conf_1.png"
            hover "images/ui/stat_icons/conf_h.png"

            if can_show_menu():
                action [Function(hud_interact_reset), Function(player.face_icon_conf), Show("text_char_speak", text=rlist.hud_conf_press_comment)]
        text "[player.confidence]" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"

screen right_menu_button_fitness():
    frame padding (0, 0) xysize (46,46) background None:
        imagebutton:
            if player.pregnancy >= 2:
                idle "images/ui/stat_icons/body_p.png"
                hover "images/ui/stat_icons/body_p_h.png"
            elif player.pregnancy == 1:
                idle "images/ui/stat_icons/body_1.png"
                hover "images/ui/stat_icons/body_1_h.png"
            elif player.fitness > 80:
                idle "images/ui/stat_icons/body_5.png"
                hover "images/ui/stat_icons/body_5_h.png"
            elif player.fitness > 60:
                idle "images/ui/stat_icons/body_4.png"
                hover "images/ui/stat_icons/body_4_h.png"
            elif player.fitness > 40:
                idle "images/ui/stat_icons/body_3.png"
                hover "images/ui/stat_icons/body_3_h.png"
            elif player.fitness > 20:
                idle "images/ui/stat_icons/body_2.png"
                hover "images/ui/stat_icons/body_2_h.png"
            else:
                idle "images/ui/stat_icons/body_1.png"
                hover "images/ui/stat_icons/body_1_h.png"

            if can_show_menu():
                action [Function(hud_interact_reset), Function(player.face_icon_fitness), Show("text_char_speak", text=rlist.hud_conf_press_comment_fitness)]
        text "[player.fitness]" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"

screen right_menu_button_int():
    frame padding (0, 0) xysize (46,46) background None:
        imagebutton:
            if player.has_perk([perk_bimbo, perk_princess]):
                idle "images/ui/stat_icons/int_bimbo.png"
            elif player.int > 80:
                idle "images/ui/stat_icons/int_5.png"
            elif player.int > 60:
                idle "images/ui/stat_icons/int_4.png"
            elif player.int > 40:
                idle "images/ui/stat_icons/int_3.png"
            elif player.int > 20:
                idle "images/ui/stat_icons/int_2.png"
            else:
                idle "images/ui/stat_icons/int_1.png"
            if player.has_perk([perk_bimbo, perk_princess]):
                hover "images/ui/stat_icons/int_bimbo_h.png"
            else:
                hover "images/ui/stat_icons/int_h.png"

            if can_show_menu():
                action [Function(hud_interact_reset), Function(player.face_icon_int), Show("text_char_speak", text=rlist.hud_int_press_comment)]
        if player.has_perk([perk_bimbo, perk_princess]):
            text "?" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"
        else:
            text "[player.int]" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"

screen right_menu_button_cycle():
    frame padding (0, 0) xysize (46,46) background None:
        imagebutton:
            if player.preg_knows:
                idle "cycle_rib_preg_idle"
                hover "cycle_rib_preg_hover"
            elif player.has_perk(perk_period_late):
                idle "cycle_rib_periodlate_idle"
                hover "cycle_rib_periodlate_hover"
            elif player.has_perk(perk_period):
                idle "cycle_rib_period_idle"
                hover "cycle_rib_period_hover"
            elif player.has_perk(perk_ovulating):
                if player.has_perk(perk_inseminated):
                    idle "cycle_rib_ovulateinsem_idle"
                    hover "cycle_rib_ovulateinsem_hover"
                else:
                    idle "cycle_rib_ovulate_idle"
                    hover "cycle_rib_ovulate_hover"
            elif player.cycle_conditions["stage"] == "foll":
                if player.has_perk(perk_inseminated):
                    idle "cycle_rib_folinsem_idle"
                    hover "cycle_rib_folinsem_hover"
                else:
                    idle "cycle_rib_fol_idle"
                    hover "cycle_rib_fol_hover"
            elif player.cycle_conditions["stage"] == "lut":
                idle "cycle_rib_lut_idle"
                hover "cycle_rib_lut_hover"
            else:
                idle "cycle_rib_nocycle_idle"
                hover "cycle_rib_nocycle_hover"
            if can_show_menu():
                action [Function(hud_interact_reset), Function(player.face_icon_cycle), Show("text_char_speak", text=rlist.hud_cycle_press_comment)]

        if player.cycle_conditions["stage"] == "no_cycle" and not player.preg_knows:
            text "?" size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"
        elif player.preg_knows:
            text str(global_pregnancy_length - player.days_pregnant) size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"
        else:
            text str(player.cycle_days_left()) size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"


screen right_menu():

    if cheats:
        key "q" action Function(cheat_pass_time_slow)
    zorder 3


    $ currSkirt = c.skirt
    $ currclevage = c.clevage
    $ currBelly = c.belly
    $ currAss = c.ass
    $ currBraless = c.braless
    $ currPantsless = c.pantsless
    $ currThong = c.thong
    $ currSlutty = c.slutty
    $ currExposed = c.exposed
    $ currApp = c.inappropriate



    $ currHour = str(t.hour).zfill(2)
    $ currMinutes = str(t.minute).zfill(2)
    $ currDay = t.day
    $ currWkDay = t.wkday
    $ currMday = t.daym
    $ currMonth = t.month

    $ tooltip = GetTooltip()


    frame align (1.0, 0.0) xysize (1920, 57) padding (5,5):
        has hbox
        spacing 30
        frame xsize 640 yoffset -5 padding (12,0) background None:
            has hbox

            if loc_cur == loc_haven_cell:
                text "??" size 42 color '#f7f7f7' font "BRLNSB.TTF"
                text ":" size 42 color '#b23f73' font "BRLNSB.TTF"
                text "?? Unknown date" size 42 color '#f7f7f7' font "BRLNSB.TTF"
            else:

                text "[currHour]" size 42 color '#f7f7f7' font "BRLNSB.TTF"
                text ":" size 42 color '#b23f73' font "BRLNSB.TTF"
                text "[currMinutes] [currWkDay] [currMday] [currMonth]" size 42 color '#f7f7f7' font "BRLNSB.TTF"

        use right_menu_button_desire
        use right_menu_button_allure
        use right_menu_button_tired
        use right_menu_button_mood
        use right_menu_button_conf
        use right_menu_button_fitness
        use right_menu_button_int

        text "|" size 42 color '#b23f73' yoffset -5 font "BRLNSB.TTF"
        use right_menu_button_cycle

        hbox yoffset -5:
            text "£" size 42 color '#b23f73' font "BRLNSB.TTF"
            text str(player.cash) size 42 color '#f7f7f7' font "BRLNSB.TTF"

        hbox:
            imagebutton:
                idle "diary_idle"
                hover "diary_hover"
                if can_show_menu():
                    action [Hide ("text_hov"), Show(log.screen()), Hide("travel_screen"), Hide("right_menu"), SetVariable ("player.eye", 5), Function(diary_set_seen, stats_screen_tab)]
                else:
                    action NullAction()
                tooltip "My personal diary."
        hbox:
            imagebutton:
                idle "inventory_idle"
                hover "inventory_hover"


                if can_show_menu():
                    action [Hide ("text_hov"), Show("inventory_screen"), Hide("travel_screen"), SetVariable ("player.eye", 5)]
                else:
                    action NullAction()
                tooltip "My inventory."
        hbox:
            imagebutton:
                idle "cheats_idle"
                hover "cheats_hover"
                if renpy.get_screen("cheats_screen"):
                    action Hide("cheats_screen")
                else:
                    action Show("cheats_screen")
                tooltip "Cheats menu."

    hbox:
        align (0.9,0.9)
        vbox:
            if cheats == 1:
                $ cum_hand = player.cum_locations["cum_hand"]
                $ cum_mouth = player.cum_locations["cum_mouth"]
                $ cum_face = player.cum_locations["cum_face"]
                $ cum_belly = player.cum_locations["cum_belly"]
                $ cum_chest = player.cum_locations["cum_chest"]
                $ cum_vagout = player.cum_locations["cum_vagout"]
                $ cum_vagin = player.cum_locations["cum_vagin"]
                $ cum_assout = player.cum_locations["cum_assout"]
                $ cum_assin = player.cum_locations["cum_assin"]

                $ cum_visible = player.cum_visible

                $ stage =  player.cycle_conditions["stage"]
                $ stage_count =  player.cycle_conditions["count_stage"]

                $ call_stack = renpy.call_stack_depth()

                $ exhib_stat = perk_exhibitionist.dict["exhib_counter"]

                $ act_var = action_act_var
                $ sfoc = str(sprite_focus)

                text "wearing -- skirt [currSkirt] clevage [currclevage] belly [currBelly] ass [currAss] braless [currBraless] pantsless [currPantsless] thong [currThong] slutty [currSlutty] exposed [currExposed] inap [currApp]" size 15
                text "cansee -- bra [c.cansee_bra] pants [c.cansee_pants] breasts [c.cansee_breasts] vagina [c.cansee_vagina] ass [c.cansee_ass] clothed [c.clothed] underwear [c.underwear] nude [c.nude]" size 15
                text "Holes - [player.sex_holes] -- Men amount - [player.sex_man_amount] -- Men in location - [loc_cur.man_amount]" size 15
                text "Player location - [loc_cur.name] -- Last label - [store.last_label]" size 15
                text "D [player._desire] A [player._allure] T [player._tired] M [player._mood] C [player._confidence] F [player._fitness] I [player._int]" size 15
                text "hygiene [player.hygiene] hunger [player.hunger] drunk [player.drunk]" size 15
                if player.pregnant == 0:
                    text "I am not pregnant" size 15
                else:
                    text "[player.father]" size 15
                text "Exhibition stat [exhib_stat]" size 15
                text "ovirgin [player.ovirgin] vvirgin [player.vvirgin] avirgin [player.avirgin] firstvsex [player.firstvsex] person [player.person]" size 15
                text "hsex [player.hsex] osex [player.osex] vsex [player.vsex] asex [player.asex] prostitution [player.sold] rape [player.rape]" size 15
                text "hand [cum_hand] mouth [cum_mouth] face [cum_face] belly [cum_belly] chest [cum_chest] vagout [cum_vagout] vagin [cum_vagin] assout [cum_assout] assin [cum_assin] VISIBLE [cum_visible]" size 15
                text "[stage], [stage_count]" size 15
                text "talk counter [talk_counter] speaker [cheat_name_who] [speaking_char] [test_name_test]  - Call stack [call_stack] avatar bool [pc_avatar_dummy_bool], action [act_var]" size 15
                text "current version [game_version] -- version started [game_version_start]" size 15


    if tooltip:
        frame:
            xalign 0.4
            yalign 0.056
            xsize 900
            ysize 45
            text "[tooltip]" size 25 xalign 0.5

screen right_menu_cycle():
    frame padding (0, 0) xysize (46,46) background None:
        if player.preg_knows:
            imagebutton:
                idle "cycle_rib_preg_idle"
                hover "cycle_rib_preg_hover"
                action NullAction()
                tooltip "I am pregnant."
                if can_show_menu():
                    hovered If(player.has_perk(perk_unwanted_preg), Function(player.face_angry), If(player.has_perk(perk_wanted_preg), Function(player.face_happy), Function(player.face_normal)))
                    unhovered Function (player.face_normal)
        elif player.has_perk(perk_period_late):
            imagebutton:
                idle "cycle_rib_periodlate_idle"
                hover "cycle_rib_periodlate_hover"
                action NullAction()
                tooltip "I should be on my period."
                if can_show_menu():
                    hovered Function(player.face_annoyed)
                    unhovered Function (player.face_normal)
        elif player.has_perk(perk_period):
            imagebutton:
                idle "cycle_rib_period_idle"
                hover "cycle_rib_period_hover"
                action NullAction()
                tooltip "I am on my period."
                if can_show_menu():
                    hovered Function(player.face_annoyed)
                    unhovered Function (player.face_normal)
        elif player.has_perk(perk_ovulating) and player.has_perk(perk_inseminated):
            imagebutton:
                idle "cycle_rib_ovulateinsem_idle"
                hover "cycle_rib_ovulateinsem_hover"
                action NullAction()
                tooltip "I am ovulating and had unprotected sex."
                if can_show_menu():
                    hovered Function(player.face_worried)
                    unhovered Function (player.face_normal)
        elif player.has_perk(perk_ovulating):
            imagebutton:
                idle "cycle_rib_ovulate_idle"
                hover "cycle_rib_ovulate_hover"
                action NullAction()
                tooltip "I am ovulating, so this is a dangerous time."
        elif player.cycle_conditions["stage"] == "foll" and player.has_perk(perk_inseminated):
            imagebutton:
                idle "cycle_rib_folinsem_idle"
                hover "cycle_rib_folinsem_hover"
                action NullAction()
                tooltip "I'm not ovulating yet, but still had unprotected sex."
        elif player.cycle_conditions["stage"] == "foll":
            imagebutton:
                idle "cycle_rib_fol_idle"
                hover "cycle_rib_fol_hover"
                action NullAction()
                tooltip "I'm not ovulating yet but unprotected sex can still be a bit dangerous."
        elif player.cycle_conditions["stage"] == "lut":
            imagebutton:
                idle "cycle_rib_lut_idle"
                hover "cycle_rib_lut_hover"
                action NullAction()
                tooltip "My period will be soon so it's unlikley I will get pregnant."
        else:
            imagebutton:
                idle "cycle_rib_nocycle_idle"
                hover "cycle_rib_nocycle_hover"
                action NullAction()
                tooltip "My cycle has stopped. It should restart in a few days"
        if player.preg_knows:
            text str(global_pregnancy_length - player.days_pregnant) size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"
        else:
            text str(player.cycle_days_left()) size 24 color '#f7f7f7' align (1.0, 1.0) font "BRLNSB.TTF"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
