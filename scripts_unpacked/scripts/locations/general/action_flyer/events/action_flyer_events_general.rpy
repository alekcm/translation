label action_flyer_event_general_1:
    pcm "Anyone?"
    pc "[rlist.flyering_area_dialogue]"
    pc "Here you go."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_general_2:
    "I hand flyers to people passing."
    pc "[rlist.flyering_area_dialogue]"
    pc "Here you go."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_general_3:
    pc "Discounts with the flyer!"
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_general_4:
    $ player.grope_ass()
    pc "Here, take it."
    "Man" "Cheers [rlist.name_deg]."
    $ player.grope_end()
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_general_5:
    $ player.spank()
    pc "Ah!"
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker

label action_flyer_event_general_6:
    "Man" "How much you selling for [rlist.name_deg]?"
    pc "Ugh..."
    pc "[rlist.flyering_area_dialogue]"
    jump action_flyer_event_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
