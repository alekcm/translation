define tuc = Character("Dr. Tucker", color="#ffffff")
define tucker = "Tucker"
default met_tucker = False

layeredimage tucker:
    at sprite_highlight("tucker")
    always "tucker_base"

    group face auto:
        attribute frown default



label tucker_picker:
    if met_tucker == False:
        $ met_tucker = True
        jump main_quest_01_briefing

    elif main_quest_01.isactive():
        if main_quest_01.stage == 2:
            jump main_quest_01_debrief



    elif main_quest_02.isactive():
        if main_quest_02.stage == 0:
            jump main_quest_02_start
        elif main_quest_02.stage == 3:
            jump main_quest_02_debrief



    elif main_quest_03.isactive():
        if main_quest_03.stage == 0:
            jump main_quest_03_fixer



    elif main_quest_04.isactive():
        if main_quest_04.stage == 0:
            jump main_quest_04_intro
        elif main_quest_04.stage == 4:
            jump main_quest_04_outro

    elif main_quest_05.isactive():
        if log.interactive("mq_04_f"):
            jump main_quest_05_intro
        elif log.interactive("mq_05_prep_d"):
            jump main_quest_05_main_start





    jump tucker_generic_greeting



label tucker_generic_greeting:
    $ walk(loc_hospital_office)
    show tucker smile at right1 with dissolve
    if t.hour in morning:
        tucker.name "Good morning, [name]. How can I help you?"
    elif t.hour in afternoon:
        tucker.name "Good afternoon, [name]. How can I help you?"
    else:
        tucker.name "Good to see you, [name]. How can I help you?"
    jump tucker_generic_list

label tucker_generic_cont:
    tucker.name "Was there anything else?"
    jump tucker_generic_list

label tucker_generic_list:
    menu:
        "What did you want me to do again?":
            jump main_quest_recap

        "I need help rescuing a friend" if log.interactive("mira_missing_09"):
            jump quest_mira_missing_tucker_ending
        "Nothing for now thanks.":
            tucker.name "Ok. Well you know where I am if you need anything."
            hide tucker
            $ walk(loc_hospital_lobby)
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
