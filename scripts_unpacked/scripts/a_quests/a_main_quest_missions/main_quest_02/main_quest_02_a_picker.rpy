label main_quest_02_start:

    $ temp_var_1 = t.day - main_quest_01.missionvar2
    if temp_var_1 > 0 and main_quest_01.missionvar1 == True:
        $ log.markdone("mq_02_passed_b")
        jump main_quest_02_briefing_passed
    elif log.interactive("mq_02_a_done"):
        $ log.markdone("mq_02_a_done")

        $ main_quest_02.mission_cosmetic(4,"hair5","eye4")
        jump main_quest_02_briefing
    else:
        jump tucker_generic_greeting
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
