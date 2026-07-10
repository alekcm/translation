

label world_time_checkers:

    if t.hour > 9 and school_checked_science == False:
        $ school_checked_science = True
    if t.hour > 9 and school_checked_maths == False:
        $ school_checked_maths = True
    if t.hour > 9 and school_checked_english == False:
        $ school_checked_english = True
    if t.hour > 9 and school_checked_history == False:
        $ school_checked_history = True
    if t.hour > 9 and school_checked_sport == False:
        $ school_checked_sport = True
    pc "test to check call"
    return

label pass_time:

    if player.tired < 4:
        jump world_tired_trigger
    elif player.tired < 15 and go_sleep_prompt == False:
        "I should probably stop waiting around and get some sleep instead."
        $ go_sleep_prompt = True
    else:
        $ time_kill(60)
        "You spend 30 minutes wandering around and killing time"



    if player.tired < 4:
        jump world_tired_trigger
    elif player.tired < 15 and go_sleep_prompt == False:
        "I should probably stop waiting around and get some sleep instead."
        $ go_sleep_prompt = True


    jump travel

label pass_time_15:
    if main_quest_05.active == 1 and loc_cur in district_haven:
        if loc_cur == "haven_cell":
            pc "(I should look for a way to get out of here.)"
        else:
            pc "If I have time to just hang around then I should use it to try and gather info on [ant.name]. I don't want to be in here any longer than I need to be."
        jump travel
    elif player.tired < 4:
        jump world_tired_trigger
    elif player.tired < 15 and go_sleep_prompt == False:
        pc "I should probably stop waiting around and get some sleep instead."
        $ go_sleep_prompt = True
    else:
        $ stroll(30)
        "You spend half an hour wandering around and killing time"



    if player.tired < 4:
        jump world_tired_trigger
    elif player.tired < 15 and go_sleep_prompt == False:
        "I should probably stop waiting around and get some sleep instead."
        $ go_sleep_prompt = True
    jump travel
    jump travel


label pass_day:
    $ t.hour = 20
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
