label oskar_talk_picker:
    if not "oskar_ask_work" in oskar.dict:
        $ oskar.dict["oskar_ask_work"] = 0
    if not "rent_sex_offer_day" in oskar.dict:
        $ oskar.dict["rent_sex_offer_day"] = 0
    show oskar at right1 with dissolve

    jump expression WeightedChoice([
    ("oskar_talk_meet_office", If(not log.interactive("quest_rent_a"), 1000, 0)),
    ("oskar_talk_ask_work_again", If(oskar.dict["oskar_ask_work"] and t.day > oskar.dict["oskar_ask_work"] and not log.interactive("quest_rent_b"), 100, 0)),


    ("oskar_talk_generic", 20),    
    ])

label oskar_talk_generic:
    if not rent_total_owed():
        oskar.name "What do you want?"
        pc "Err... Sorry, nothing."
        oskar.name "Well, this isn't somewhere to just hang out. So show yourself out."
        hide oskar with dissolve
        jump travel
    else:
        oskar.name "What do you want? Here to pay the rent?"
        jump oskar_talk_pay_rent_choices
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
