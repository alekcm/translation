init python:

    def cleaner_outfit_set():
        quest_rent.outfit_primary_colour = "blue"  
        quest_rent.outfit_secondary_colour = "white"
        quest_rent.gloves_primary_colour = "yellow"
        
        for i in clothes_wardrobe_list:
            setattr(quest_rent, i, 0)
        quest_rent.outfit = 19
        quest_rent.gloves = 4

    def cleaner_outfit():
        global tab_top
        work.outfit_primary_colour = quest_rent.outfit_primary_colour
        work.outfit_secondary_colour = quest_rent.outfit_secondary_colour
        work.pants_primary_colour = globals()[tab_top].pants_primary_colour
        work.pants_secondary_colour = globals()[tab_top].pants_secondary_colour
        work.bra_primary_colour = globals()[tab_top].bra_primary_colour
        work.bra_secondary_colour = globals()[tab_top].bra_secondary_colour
        work.gloves_primary_colour = quest_rent.gloves_primary_colour
        work.gloves_secondary_colour = quest_rent.gloves_secondary_colour
        for i in clothes_wardrobe_list:
            setattr(work, i, 0)
        work.outfit = quest_rent.outfit
        work.gloves = quest_rent.gloves
        work.pants = c.pants
        work.bra = c.bra

    def maid_outfit_set():
        for i in clothes_wardrobe_list:
            setattr(work, i, 0)
        
        work.outfit_primary_colour = "black"
        work.outfit_secondary_colour = "white"
        work.pants_primary_colour = "black"
        work.pants_secondary_colour = "white"
        work.socks_primary_colour = "black" 
        work.socks_secondary_colour = "white"
        work.hat_primary_colour = "white"
        
        work.outfit = 20
        work.socks = 14
        work.hat = 8
        work.pants = 13

    def clean_locations_picker():
        global clean_locations
        clean_locations = []
        location_list = []
        if dis(dis_home_area) or dis(dis_home): 
            location_list = [loc_stairwell, loc_office_ll, loc_office_ll_back, loc_kitchen, loc_common, loc_bathroom, loc_bedroom_robin]
        elif dis(dis_pub): 
            location_list = [loc_pub, loc_pub, loc_pub, loc_pub, loc_pub, loc_pub, loc_pub_toilet_girls, loc_pub_toilet_boys]
        elif dis(dis_motel): 
            location_list = [loc_motel, loc_motel_lobby, loc_motel_room, loc_motel_room2, loc_motel_pinkroom, loc_motel_pinkroom2, loc_motel_shower]
        else:
            location_list = loc_cur.get_district().locs 
        for i in location_list:
            if (i.open and not i.locked) or dis(dis_motel): 
                clean_locations.append(i)
        return clean_locations

    def clean_area():
        global clean_locations
        clean_locations.remove(loc_cur)
        working(10)

    def show_cleaning_image():
        image_list = ["activity_broom"]
        if not loc_cur.outside and "work" in tab_top:
            image_list.append("sb_table")
        if c.outfit in (6,19,20):
            for i in ["sb_doggy1 no_head", "sb_doggy2 head_forward", "sb_onfours", "activity_sweep", "activity_sweep"]:
                image_list.append(i)
        if loc(loc_pub) and c.outfit == 6:
            image_list = image_list + ["sb_table", "sb_table", "sb_table", "sb_table", "sb_table"]
        renpy.show(renpy.random.choice(image_list))
        renpy.with_statement(dissolve)

define clean_locations = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
