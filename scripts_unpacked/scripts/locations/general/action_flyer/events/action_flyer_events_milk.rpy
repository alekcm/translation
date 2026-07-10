label action_flyer_event_milk_1:
    "Man" "The milk is really from cows?"
    pc "Yes, two legged cows."
    "Man" "Thanks."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_milk_2:
    "Man" "Any of the milk come from you?"
    if player.lactating and shop_milk.qty(item_scrap_milkbottle):
        pc "Yup, fresh milk from me and other cows."
    else:
        pc "No, other girls give their milk."
    "Man" "Thanks."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_milk_3:
    "Man" "We getting fresh milk from you?"
    if player.lactating and shop_milk.qty(item_scrap_milkbottle):
        pc "Yup, Me and other cows provide milk daily."
    else:
        pc "Not this time. Other cows are providing the milk fresh."
    "Man" "Thanks."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
