init python:
    def gloryhole_customer():
        chance = 100
        if loc_cur in dis_school.locs:
            chance = chance * 0.8
            if not school_open_hours():
                return False
            if t.wkday in weekday and t.hour in irange(9,14): 
                chance = chance * 0.1
        elif loc_cur in dis_pub.locs:
            chance = chance * 1.2
            if not t.timeofday == "night":
                chance = chance * 0.1
        
        if numgen(0,250) < chance:
            return True
        else:
            return False

label gloryhole_event_cheat:
    if not quest_gloryhole_create.active:
        jump school_field_soccer_hangout_gloryhole_ask
    if log.interactive("quest_gloryhole_a"):
        "Updating quest log. This is where you will find out what tools you need to make a hole"
        $ log.markdone("quest_gloryhole_a")
        $ log.activate("quest_gloryhole_b_saw")
    if log.interactive("quest_gloryhole_b_chis"):
        if not inv.qty(item_chis):
            "You do not have a chisel. Giving you one now."
            $ inv.take(item_chis)
        jump school_field_soccer_hangout_gloryhole_chis
    if log.interactive("quest_gloryhole_b_saw"):
        if not inv.qty(item_saw):
            "You do not have a saw. Giving you one now."
            $ inv.take(item_saw)
        jump school_field_soccer_hangout_gloryhole_saw
    if log.interactive("quest_gloryhole_b_tape"):
        if not inv.qty(item_tape):
            "You do not have tape. Giving you one now."
            $ inv.take(item_tape)
        jump school_field_soccer_hangout_gloryhole_tape
    if log.interactive("quest_gloryhole_c") and nate.inv.qty(item_chis) and nate.inv.qty(item_saw) and nate.inv.qty(item_tape):
        if not t.timeofday == "night":
            "This normally needs to be done at night."
        jump school_field_soccer_hangout_gloryhole_create
    if quest_gloryhole_create.iscomplete() and nate.inv.qty(item_chis):
        jump school_field_soccer_hangout_gloryhole_give_tools
    "Looks like this quest has been complete."
    jump travel

label gloryhole_make_picker:
    if loc_from in dis_pub.locs and not t.hour in irange(10, 16):
        pcm "I should probably make a hole earlier when the pub is less busy."
        jump travel
    elif dis(dis_lake) and not t.timeofday == "night":
        pcm "I should wait until it's night time and less people around before doing this."
        jump travel
    elif all([inv.qty(item_chis), inv.qty(item_saw), inv.qty(item_tape)]):
        jump gloryhole_make_create
    else:
        if not inv.qty(item_tape):
            pcm "I need to get more tape to smooth over the hole otherwise no one will bother using it."
        else:
            pcm "I don't have the tools to make a hole any more. I need both a chisel and a saw."
        jump travel

label gloryhole_make_create:
    if loc_cur.mens_room:
        pcm "I had better do it from the girls side. If I get caught doing it here I'll end up in trouble."
        jump travel
    pcm "Right... Let's do this I suppose..."
    $ walk(globals()[loc_cur.name + "_stall"])
    $ player.face_grit()
    with vpunch
    "I spend the next hour or so working at the wall, first making a hole with the chisel."
    $ working(numgen(25,35))
    $ player.face_grit()
    with hpunch
    "Then using the saw to make a larger, circular hole. Finally smoothing it out with some tape."
    $ working(numgen(25,35))
    $ player.face_frown()
    $ inv.use(item_tape)
    $ loc_cur.has_gloryhole = True
    $ loc_from.has_gloryhole = True
    if get_opposite_gender_room(loc_from):
        $ get_opposite_gender_room(loc_from).has_gloryhole = True
    pc "Phew..."
    pcm "Harder than it looks."
    $ walk(loc_from)
    pcm "Right, hopefully no one saw me doing that..."
    jump travel

label pub_waitress_work_gloryhole:
    pcm "Hmmm..."
    $ walk(loc_pub_toilet_girls)
    $ walk(loc_pub_toilet_girls_stall)
    "Not currently written yet, but there will be a chance that Dani trixie or some random girl is using it"
    jump gloryhole_wait

label gloryhole_enter:
    if not quest_gloryhole_create.active and not "seen_hole" in quest_gloryhole.list:

        $ add_to_list(quest_gloryhole.list, "seen_hole")
        pcm "Errr, what is that?"
        pcm "Ugh, why do I even need to ask myself that..."
        pcm "First time seeing one though. Didn't think men would be stupid enough to stick their dicks in random holes."
        pcm "Well, whatever. That's their problem to worry about."
        jump travel

    if loc_cur.mens_room:
        if player.has_perk(perk_male):
            pcm "Unless I somehow get my cock back, there isn't anything for me to do on this side of the wall."
        else:
            pcm "Not much I can do on this side of the wall."
        jump travel
    elif npc_any_here(globals()[loc_cur.name + "_stall"]):
        pcm "Oh? It's locked. Someone is already inside..."
        jump travel
    elif not global_random_hour_number:
        pcm "Oh? It's locked. Someone is already inside..."
        jump travel




    elif player.has_perk([perk_slut, perk_sucu, perk_whore, perk_preg_want, perk_blackout], notif=True) or player.check_sex_agree(4):
        if rachel_here():
            rachel.name "Have fun!"
        $ walk(globals()[loc_cur.name + "_stall"])


        jump gloryhole_wait
    else:

        $ player.face_worried()
        pcm "Yeah, sucking dicks from a hole isn't for me..."
        jump travel

label gloryhole_undress:
    pcm "Going to get messy so I should probably put my clothes somewhere..."
    $ pc_striptease()
    return

label gloryhole_wait:
    if not ("work" in tab_top and loc_from == loc_pub_toilet_girls and c.outfit == 6) and not c.nude:
        call gloryhole_undress from _call_gloryhole_undress
    if "work" in tab_top and loc_from == loc_pub_toilet_girls:
        $ pub_waitress.workcycle += 1
    show gh_blow_behind idle no_man_hole with dissolve
    "I knock on the wall to show I am here and wait to see if there is someone on the other side."
    $ working(5)
    if gloryhole_customer():
        "And almost right away someone responds..."
        jump gloryhole_start
    $ working(5)
    "No one responds right away so I just wait while periodicity knocking."
    if gloryhole_customer():
        "But it's not long until someone shows up..."
        jump gloryhole_start
    $ working(5)
    pcm "Still no one?"
    if gloryhole_customer():
        "Eventually someone shows up..."
        jump gloryhole_start
    $ working(5)
    pcm "Come on..."
    if gloryhole_customer():
        "Finally someone shows up..."
        jump gloryhole_start
    pcm "Damn, no one coming? *Sigh*"
    jump gloryhole_end_nocust
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
