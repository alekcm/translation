init python:

    def arrival_travel(): 
        global speaking_char, whore_street_sex_end_jumper, event_end_interrupt_label, quest_temp
        lust_blocker = False 
        call_blocker = False 
        reset_call_stack() 
        arrival_reset_images() 
        player.reset_sex_status() 
        pc_loose_clothes() 
        location_closed()
        arrival_event_catcher()
        speaking_char = None
        whore_street_sex_end_jumper = "" 
        event_end_interrupt_label = "" 
        player.sex_holes = []
        player.sex_man_amount = 0
        remove_from_list(quest_whore.list, "should_pay")
        if isinstance(quest_temp, QuestClass):
            quest_temp.workcycle = 0
        quest_temp = None
        if "work" in tab_top: 
            pc_set_temp_outfit()
        player.cover_reset()
        game_tick()
        perk_exhib_counter()
        player.reset_sex_status(True)
        reset_temp_vars()
        refresh_avatar()


    def arrival():
        global late_final_warning, night, go_sleep_prompt, district_home, shower_warning
        
        
        
        
        
        arrival_travel()
        if "time" in loc_motel_room.dict and loc_motel_room.open() and (t.hours_total - 24) > loc_motel_room.dict["time"]:
            loc_motel_room.locked = True
            if loc(loc_motel_room):
                renpy.jump("motel_room_kickedout") 
        
        if not (dis_cur == dis_haven and main_quest_05.isactive()):
            if loc_cur in dis_home.locs and (player.tired < 3 or (player.tired < 10 and go_sleep_prompt == False)):
                if player.tired < 3:
                    renpy.jump('world_tired_trigger_home')
                elif player.tired < 10 and go_sleep_prompt == False:
                    renpy.jump('world_tired_trigger_home')
            
            else:
                if player.tired < 5:
                    renpy.jump('world_tired_trigger')
        
        if not loc_cur.visited:
            loc_cur.visited = True
            if renpy.has_label(loc_cur.name + "_visit"):
                renpy.jump(loc_cur.name + "_visit")
        
        if wolfgang_can_play():
            renpy.jump("random_event_wolfgang_picker")
        
        if (player.covering and loc_cur.population >= 2 and not dis(dis_beach)) or block_action_bar_because_naked():
            renpy.jump("random_event_generic_exhib")    
        
        renpy.jump("random_event_picker_tombola")

    def arrival_reset_images():
        renpy.scene()
        for i in ["polaroid_popup", "drink", "text_char_speak", "grope_popup_breasts_1", "grope_popup_breasts_2", "grope_popup_hips_1", "grope_popup_hips_2", "text_char_speak"]: 
            renpy.hide_screen(i)
        
        
        player.grope_end()

    def arrival_blocker(location):
        global temp_var_9
        
        
        
        if loc_cur.home_location and location.outside:
            
            temp_var_9 = location 
            renpy.jump("leave_house_checks")
        if c.exposed:
            if dis(dis_misc) and perk_exhib_weight(0) and location.population == 2:
                
                renpy.jump("random_event_generic_exhib_miscloc_find_clothes") 
            elif dis(dis_misc) and perk_exhib_weight(0) and location.population == 1:
                renpy.jump("random_event_generic_exhib_miscloc_people") 
        if location == loc_checkpoint_lobby:
            if log.interactive("mq_04_b"):
                renpy.jump("main_quest_04_checkpoint_lobby_return") 
            elif log.interactive("mq_04_d"):
                renpy.jump("main_quest_04_checkpoint_lobby_complete") 
            elif not t.hour in workhours:
                renpy.jump("main_quest_04_checkpoint_lobby_closed") 
            elif log.interactive("mq_04_c"):
                renpy.jump("main_quest_04_policestation_return") 
            elif renpy.has_label(location.name + "_arrival"):
                renpy.jump(location.name + "_arrival") 
        if not dis(dis_park) and location in dis_park.locs and acc.choker == 6 and not "warned_pc" in quest_wolfgang.list and quest_wolfgang.active:
            renpy.jump("wolfgang_first_park_enter_warning") 

    def arrival_event_catcher():
        
        
        if loc_cur == loc_bedroom:
            if log.interactive("mq_03_b"):
                renpy.jump("main_quest_03_fixer_home") 
        if loc_cur == loc_checkpoint:
            if log.interactive("mq_04_a") and not main_quest_04.stage == 2:
                renpy.jump("main_quest_04_loc_checkpoint_visit")
        if loc_cur == loc_checkpoint_lobby:
            if log.interactive("mq_04_a"):
                renpy.jump("main_quest_04_policestation") 

    def arrival_character_speech_popup():
        if not numgen(0,8):
            renpy.show_screen("text_char_speak", text=rlist.avatar_comments_general_sandbox)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
