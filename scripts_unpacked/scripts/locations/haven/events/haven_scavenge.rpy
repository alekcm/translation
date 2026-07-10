label loc_haven_storage_scavenge:
    $ dialouge = renpy.random.choice([
    "Let's see here. Better be quiet.",
    "Don't make too much noise...",
    "Hopefully I can find something useful.",
    "Hmmm...",
    ])
    pcm "[dialouge]"

    $ rand_choice = WeightedChoice([
    ("haven_storage_beer1", If(not "searched_beer1" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_beer2", If(not "searched_beer2" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_boxclose", If(not "searched_boxclose" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_cardboard1", If(not "searched_cardboard1" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_cardboard2", If(not "searched_cardboard2" in loc_haven_storage.list, 1000, 0)),  
    ("haven_storage_crate1", If(not "searched_crate1" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_crate2", If(not "searched_crate2" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_debris", If(not "searched_debris" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_ele", If(not "searched_ele" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_shelf", If(not "searched_shelf" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_toolbox", If(not "searched_toolbox" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_vent", If(not "searched_vent" in loc_haven_storage.list, 1000, 0)),
    ("haven_storage_wood", If(not "searched_wood" in loc_haven_storage.list, 1000, 0)),
    ("haven_utilities_scav_generic_1", 1),
    ("haven_utilities_scav_generic_2", 1),
    ("haven_utilities_scav_generic_3", 1),
    ("haven_utilities_scav_generic_4", 1),
    ("haven_utilities_scav_generic_5", 1),
    ("haven_utilities_scav_generic_6", 1),
    ])
    call expression rand_choice from _call_expression_2

label loc_haven_utilities_scavenge:
    $ dialouge = renpy.random.choice([
    "Let's see here. Better be quiet.",
    "Don't make too much noise...",
    "Hopefully I can find something useful.",
    "Hmmm...",
    ])
    pcm "[dialouge]"

    $ rand_choice = WeightedChoice([
        
    ("haven_utilities_boiler", If(not "checked_boiler" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_bigpipe", If(not "checked_bigpipe" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_bluepipes", If(not "checked_bluepipes" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_cables", If(not "checked_cables" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_ceilingpipe", If(not "checked_ceilingpipe" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_cutoff", If(not "checked_cutoff" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_elebox", If(not "checked_elebox" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_fire", If(not "checked_fire" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_gas", If(not "checked_gas" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_redpipes", If(not "checked_redpipes" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_trash", If(not "checked_trash" in loc_haven_utilities.list, 1000, 0)),
    ("haven_utilities_vents", If(not "checked_vents" in loc_haven_utilities.list, 1000, 0)),
    ])
    jump expression rand_choice

label loc_haven_bedroom_scavenge:
    if not haven_time_empty():
        pcm "Trying to poke around while people are here will just get me in trouble."
        jump travel
    $ dialouge = renpy.random.choice([
    "Let's see here. Better be quiet.",
    "Don't get caught...",
    "Hopefully I can find something useful.",
    "Hmmm...",
    ])
    pcm "[dialouge]"
    $ rand_choice = WeightedChoice([
        
    ("haven_bedroom_bedbag1", 100),
    ("haven_bedroom_bedbag2", 100),
    ("haven_bedroom_bedbag3", 100),
    ("haven_bedroom_bedbag4", 100),
    ("haven_bedroom_bedcorner", 100),
    ("haven_bedroom_beddoor", 100),
    ("haven_bedroom_bedfar", 100),
    ("haven_bedroom_bedright", 100),
    ])
    jump expression rand_choice




























label dis_haven_scavenge_lounge_brew:
    if havenvik.has_met:
        pcm "Oooh, looks like [havenvik.name] left some brew behind."
    else:
        pcm "Oooh, looks like someone left some brew behind."
    $ inv.take(item_brew)
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_lounge_fluid:
    pcm "Hmm, what is this?"
    pcm "Some accelerant for the fire pits. No idea if I have a use for this but won't get many other chances to nab it so might as well keep it."
    $ inv.take(item_haven_fluid)
    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_generic_1:
    "Temp scav event"
    $ inv.take(item_cigs)
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_generic_2:
    $ inv.take(item_cigs)
    "Temp scav event"
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_generic_3:
    $ inv.take(item_brew)
    "Temp scav event"
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_generic_4:
    $ inv.take(item_map_pill)
    "Temp scav event"
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_generic_5:
    "Temp scav event"
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_generic_6:
    "Temp scav event"
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_generic_7:
    "Temp scav event"
    $ working(10)
    jump travel_arrival

label dis_haven_scavenge_generic_8:
    "Temp scav event"
    $ working(10)
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
