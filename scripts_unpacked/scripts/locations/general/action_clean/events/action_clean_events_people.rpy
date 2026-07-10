label action_clean_event_robin_1:
    pc "Just here to clean up."
    $ show_cleaning_image()
    robin.name "Thanks [name]!"
    "I go around cleaning all the junk off of [robin.name]'s bedroom floor and collect it all into a bin."
    pc "There you go."
    jump action_clean_event_picker

label action_clean_event_robin_2:
    robin.name "Cleaner [name]!"
    pc "Yup. Got to get that rent down."
    $ show_cleaning_image()
    robin.name "Yeah."
    "I go around cleaning all the junk out of [robin.name]'s bedroom and give the floor a bit of a sweep."
    pc "All nice and clean."
    jump action_clean_event_picker

label action_clean_event_robin_3:
    pc "Hey [robin.name]. Just cleaning up."
    robin.name "Don't mind me."
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pcm "There we go..."
    jump action_clean_event_picker

label action_clean_event_oskar_1:
    pc "Don't mind me."
    oskar.name "I won't."
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    if not oskar.can_sex:
        pcm "Has he been watching me the whole time?"
        pcm "Whatever..."
    else:
        jump action_clean_event_oskar_sex_ask
    jump action_clean_event_picker

label action_clean_event_oskar_2:
    pc "Just here to do some cleaning."
    oskar.name "..."
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    pc "Hope you haven't been looking at my arse this whole time."
    oskar.name "Never."
    pc "Hmmm..."
    if oskar.can_sex:
        jump action_clean_event_oskar_sex_ask
    jump action_clean_event_picker

label action_clean_event_oskar_sex_ask:
    if rent_total_owed():
        $ quest_rent.soldprice = player.set_whore_price(2)
        pcm "Should I tease him a bit to lower the rent?"
    else:
        pcm "Should I tease him a bit for fun?"

    menu:
        "Tease him":
            jump oskar_sex_foreplay_start
        "Just keep cleaning":

            pcm "Better just clean up."
            jump action_clean_event_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
