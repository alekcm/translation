

label pinkroom_first_time:
    $ add_to_list(loc_motel_pinkroom.list, "first_time")
    $ loc_motel_pinkroom.dict["sex_groups"] = True
    $ loc_motel_pinkroom.dict["sex_extreme"] = False
    $ player.face_worried()
    pcm "Hmmm... Love bed and porn all over the walls. Why am I not surprised?"
    if not player.preg_knows:
        pcm "Hope they clean this place. Feels like I might end up pregnant just breathing the air..."
        pcm "Ugh, idiot me. Gonna end up pregnant from all the men sticking their things in me..."
    pcm "..."
    pcm "I can guess the rings on the bed are for tying me up. But what the hell is the one on the ceiling for?"
    pcm "Probably the same thing..."
    pcm "Well, guess it means some people might want to tie me up. I should be sure to mark my preferences on the door."
    $ walk(loc_motel_shower)
    pcm "Shower seems ok. Gonna end up dirty so good to have this handy."
    $ walk(loc_motel_pinkroom)
    pcm "Well, might as well get undressed and shake my arse by the window."
    $ pc_striptease()
    $ pc_set_temp_outfit()
    if player.showing:
        pcm "Hope they don't mind girls with a fat belly."
    jump travel

label pinkroom_advertise_firsttime:
    $ add_to_list(loc_motel_pinkroom.list, "advertised")
    pcm "Right... So I am supposed to just stick my tits against the window for passersby?"
    pcm "Ugh..."
    if not c.nude:
        pcm "Better undress I suppose. Glad they have a wardrobe here."
        $ pc_striptease()
        pcm "Okay then..."
    jump pinkroom_advertise_cycle

label pinkroom_groups_picker:
    if loc_motel_pinkroom.dict["sex_groups"]:
        pcm "I think I will stop accepting groups for now."
    else:
        pcm "I think it would be okay to have group sex."
    $ loc_motel_pinkroom.dict["sex_groups"] = not loc_motel_pinkroom.dict["sex_groups"]
    jump travel

label pinkroom_extreme_picker:
    if loc_motel_pinkroom.dict["sex_extreme"]:
        pcm "I think I need a break from all the extreme stuff people ask for."
    else:
        pcm "Ugh, might get me in trouble, but it pays more. I think I will accept extreme sex things."
    $ loc_motel_pinkroom.dict["sex_extreme"] = not loc_motel_pinkroom.dict["sex_extreme"]
    jump travel

label pinkroom_sex_end:
    $ walk(loc_motel_pinkroom)
    tempname.name "[rlist.sex_end_goodbye]"
    "I help the guy clean himself up and lead him out the door."
    $ player.face_happy()
    pc "Cya!"
    hide male_generic with dissolve
    $ player.face_normal()
    jump travel

label pinkroom_leave:
    if inv.qty(item_pinkticket):
        pcm "I have tickets I can cash in."
    else:
        pcm "I don't even have any tickets to cash in."
    if c.nude or "temp_outfit" in tab_top or "home" in tab_top or "swim" in tab_top:
        $ pc_strip()
        $ pc_dress_slow("party")
    $ walk(loc_motel)
    $ loc_motel_pinkroom.locked=True
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
