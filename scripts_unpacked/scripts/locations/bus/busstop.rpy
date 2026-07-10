label busstop:
    if loc_to == "residential_area":
        $ walk(True, "busstop_residential_area", 1)
    elif loc_to == "commercial_area":
        $ walk(True, "busstop_commercial_area", 1)
    elif loc_to == "school_exterior":
        $ walk(True, "busstop_school_exterior", 1)
    elif loc_to == "revel":
        $ walk(True, "busstop_revel", 1)
    elif loc_to == "lake_entrance":
        $ walk(True, "busstop_lake_entrance", 1)
    elif loc_to == "highway_local":
        $ walk(True, "busstop_highway_local", 1)
    elif loc_to == "checkpoint":
        $ walk(True, "busstop_checkpoint", 1)
    elif loc_to == "industrial_area":
        $ walk(True, "busstop_industrial_area", 1)
    elif loc_to == "park_local":
        $ walk(True, "busstop_park_local", 1)
    elif loc_to == "truckstop":
        $ walk(True, "busstop_truckstop", 1)

    $ arrival()

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
