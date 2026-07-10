label quest_mira_missing_debug_picker:
    if not "kidnapped" in mira.list and not quest_mira_missing.active:
        jump quest_mira_missing_debug_start
    elif not quest_mira_missing.active:
        "Triggering cass approaching Sammy."
        jump quest_mira_missing_cass_approach
    elif log.interactive("mira_missing_01"):
        jump quest_mira_missing_debug_ask_about_1
    elif log.interactive("mira_missing_02"):
        "You return to cass and tell her about what you discovered"
        jump quest_mira_missing_return_to_cass
    elif log.interactive("mira_missing_03"):
        "You have given cass enough time to think and now she approaches you."
        jump quest_mira_missing_cass_whore_idea
    elif log.interactive("mira_missing_04"):
        "You meet cass after school to go to the highway together."
        jump quest_mira_missing_go_highway_first_prompt
    elif log.interactive("mira_missing_05"):
        jump quest_mira_missing_debug_ask_about_2
    elif log.interactive("mira_missing_06"):
        jump quest_mira_missing_cass_only_whores
    elif log.interactive("mira_missing_07"):
        $ walk(loc_revel_backstreet)
        jump quest_mira_missing_cass_whore_clothes
    elif log.interactive("mira_missing_08"):
        jump quest_mira_missing_debug_get_intel
    elif not "told_cass_all_intel" in quest_mira_missing.list:
        jump quest_mira_missing_intel_complete
    elif log.interactive("mira_missing_09"):
        $ walk(loc_hospital_office)
        show tucker at right1 with dissolve
        jump quest_mira_missing_tucker_ending
    else:
        "The quest probably ends here or I made a mistake because it doesn't know what to do now."
        jump travel

label quest_mira_missing_debug_start:
    "Here I will max out your affinity with cass and mira and make mira go missing."
    $ cass.add_love(5000)
    $ mira.add_love(5000)
    $ quest_mira_missing_kidnap()
    jump travel

label quest_mira_missing_debug_ask_about_1:
    "Who will you ask about if they have seen mira?"
    menu:
        "Dan":
            "This assumes you already asked the soccer boys about her."
            $ add_to_list(dan.list, "asked_about_mira")
            jump quest_mira_missing_dan_approach

label quest_mira_missing_debug_ask_about_2:
    "You will ask about to see if anyone knows how you can get info from the whores."
    menu:
        "Security":
            "This option will only be open if you have met them during the main storyline."
            $ walk(loc_checkpoint_lobby)
            jump quest_mira_missing_whore_investigation_security
        "Simon":
            "This option will only be available if you have done the simon main mission and then discovered his PI office."
            "NOTE The PI office is not ingame, so impossible to go this route right now"
            "He will also be approachable in the pub."
            jump quest_mira_missing_whore_investigation_simon

label quest_mira_missing_debug_get_intel:
    "Here you will get all the intel for this quest."
    $ inv.take(item_mira_intel, 10)
    $ log.find("mira_missing_08", 10)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
