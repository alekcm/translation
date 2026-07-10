init python:

    def flyer_locations_picker():
        global flyer_locations
        
        
        flyer_locations = []
        location_list = []
        if dis(dis_revel):
            flyer_locations = [loc_market, loc_revel, loc_revel_backstreet]
            if quest_flyers.missionvar1 == "milkmaid":
                flyer_locations.append(loc_market_stall_milk)
            if quest_flyers.missionvar1 == "needle":
                flyer_locations.append(loc_market_stall_needle)
        elif dis(dis_truckstop):
            flyer_locations = [loc_motel, loc_truckstop, loc_highway, loc_highway_slum, loc_highway_slum_street]
        elif dis(dis_lake):
            flyer_locations = [loc_boardwalk, loc_beach_gym, loc_beach_hangout, loc_beach_fire, loc_lake]
        else:
            for i in dis_cur.locs:
                if i.outside and i.population and (i.open and not i.locked):
                    flyer_locations.append(i)
        return flyer_locations

    def flyer_area():
        global flyer_locations
        flyer_locations.remove(loc_cur)
        working(10)

    def outfit_hucow():
        global tab_top
        work.bra_primary_colour = "white"
        work.bra_secondary_colour = "black"
        work.pants_primary_colour = "white"
        work.pants_secondary_colour = "black"
        work.gloves_primary_colour = "white"
        work.gloves_secondary_colour = "black"
        work.socks_primary_colour = "white"
        work.socks_secondary_colour = "black"
        work.hat_primary_colour = "white"
        work.hat_secondary_colour = "black"
        for i in clothes_wardrobe_list:
            setattr(work, i, 0)
        work.bra = 13
        work.pants = 16
        work.socks = 20
        work.gloves = 6
        work.hat = 10

    def outfit_funwear():
        global tab_top
        work.pants_primary_colour = "black"
        work.pants_secondary_colour = "hotpink"
        work.bottom_primary_colour = "black"
        work.bottom_secondary_colour = "hotpink"
        work.top_primary_colour = "black"
        work.top_secondary_colour = "hotpink"
        work.socks_primary_colour = "black"
        work.socks_secondary_colour = "hotpink"
        for i in clothes_wardrobe_list:
            setattr(work, i + "primary_trans", "trans_normal")
            setattr(work, i + "secondary_trans", "trans_normal")
        work.top_primary_trans = "trans_trans"
        work.bottom_primary_trans = "trans_trans"
        work.socks_primary_trans = "trans_trans"
        for i in clothes_wardrobe_list:
            setattr(work, i, 0)
        work.bottom = 34
        work.top = 42
        work.pants = 8
        work.socks = 9
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
