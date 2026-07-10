layeredimage bg_slum_home_layer:
    always "bg_slum_home_base"
    if neighbour_here() or neighbour.dead:
        "bg_slum_home_neighbour_layer"
    always "bg_slum_home_fg"

layeredimage bg_slum_home_neighbour_sit1_clothed_layer:
    always "bg_slum_home_people_n_sit1"
    always "bg_slum_home_people_n_sit1_clothes"
layeredimage bg_slum_home_neighbour_sit2_clothed_layer:
    always "bg_slum_home_people_n_sit2"
    always "bg_slum_home_people_n_sit2_clothes"
layeredimage bg_slum_home_neighbour_wash_clothed_layer:
    always "bg_slum_home_people_n_wash"
    always "bg_slum_home_people_n_wash_clothes"
layeredimage bg_slum_home_neighbour_cry_clothed_layer:
    always "bg_slum_home_people_n_cry"
    always "bg_slum_home_people_n_cry_clothes"

layeredimage bg_slum_home_neighbour_dead_layer:
    if "dead_od" in neighbour.list and neighbour.dead_time and t.day <= (neighbour.dead_time + 2):
        "bg_slum_home_people_n_highdf"
    elif "dead_od" in neighbour.list:
        "bg_slum_home_people_n_highd"
    elif "dead_choke" in neighbour.list and neighbour.dead_time and t.day <= (neighbour.dead_time + 2):
        "bg_slum_home_people_n_chokef"
    elif "dead_choke" in neighbour.list:
        "bg_slum_home_people_n_choke"

layeredimage bg_slum_home_neighbour_layer:

    if neighbour.dead and (neighbour.dead_time + 7) > t.day:
        "bg_slum_home_neighbour_dead_layer"
    elif not neighbour.dead:
        "bg_slum_home_neighbour_alive_layer"

layeredimage bg_slum_home_neighbour_alive_layer:

    if t.hour in [10,11,12,13,14,15,16,17] and (t.minute in irange(1,15) or t.minute in irange(31,45)):
        "bg_slum_home_people_n_layback"
    elif t.hour in [10,11,12,13,14,15,16,17]:
        "bg_slum_home_people_n_layfront"


    elif "sex_time" in neighbour.dict and abs(neighbour.dict["sex_time"] - t.minutes_total) <= 3 and "sex" in neighbour.list:
        "bg_slum_home_neighbour_wash_clothed_layer"
    elif "sex_time" in neighbour.dict and abs(neighbour.dict["sex_time"] - t.minutes_total) <= 6 and "sex" in neighbour.list:
        "bg_slum_home_people_n_cry"


    elif "sex" in neighbour.list and t.minute in range(0,60,5):
        "bg_slum_home_people_n_sex_mast"
    elif "sex" in neighbour.list and t.minute in range(1,60,5):
        "bg_slum_home_people_n_sex_doggy"
    elif "sex" in neighbour.list and t.minute in range(2,60,5):
        "bg_slum_home_people_n_sex_cow"
    elif "sex" in neighbour.list and t.minute in range(3,60,5):
        "bg_slum_home_people_n_sex_arch"
    elif "sex" in neighbour.list and t.minute in range(4,60,5):
        "bg_slum_home_people_n_sex_spoon"


    elif t.hour == 7 and t.minute < 30:
        "bg_slum_home_people_n_sit1"
    elif t.hour in [7, 8, 9, 10]:
        "bg_slum_home_people_n_high"

    elif t.minute in range(0,60, 3):
        "bg_slum_home_neighbour_sit1_clothed_layer"
    elif t.minute in range(1,60, 3):
        "bg_slum_home_neighbour_sit2_clothed_layer"
    else:
        "bg_slum_home_neighbour_cry_clothed_layer"

image bg_highway_slum_home:
    "bg_slum_home_layer"
    bg_tint_transform(True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
