label robin_oskar_sex_catch_picker:
    if not "oskar_sex_seen" in robin.list:
        jump robin_oskar_sex_firsttime
    else:
        jump robin_oskar_sex_bedroom_spy_prompt

label robin_oskar_sex_bedroom_spy_prompt:
    if "oskar_sex_seen" in robin.list:
        if oskar.rape:
            pcm "Ugh, having to pay rent with [oskar.name]."
            pcm "I'll leave her to it."
            jump travel
        else:
            pcm "Hmm, having fun with [oskar.name]?"
    else:
        pcm "Sounds like she is not alone in there. Wonder who she is with?"
    menu:
        "Spy on her" if player.check_sex_agree(2):
            jump robin_oskar_sex_spy_picker
        "Walk in and watch" if not oskar.rape and robin.isslut and player.check_sex_agree(3):
            jump robin_oskar_sex_watch_picker
        "Leave her alone":
            pcm "I'll let her keep her privacy."
    jump travel

label robin_oskar_sex_firsttime:
    $ add_to_list(robin.list, "oskar_sex_seen")
    if loc(loc_stairwell):
        $ walk(loc_office_ll)
    else:
        $ walk(loc_bedroom_robin)
    $ player.face_shock()
    pc "Ah!"
    pc "Err... Sorry..."
    $ walk(loc_from)
    pcm "..."
    pcm "Err... Wow... Okay..."
    pcm "Not what I expected when I walked in there."
    jump travel



label robin_oskar_sex_spy_picker:
    pcm "Okay..."
    pcm "Don't get caught..."
    "I stay outside the room, but poke my head in to see what is going on."
    jump expression WeightedChoice([
    ("robin_oskar_sex_bedroom_blow", 100),
    ("robin_oskar_sex_bedroom_doggy", If(robin_here(loc_bedroom_robin), 100, 0)),
    ("robin_oskar_sex_bedroom_onback", If(robin_here(loc_bedroom_robin), 100, 0)),
    ("robin_oskar_sex_bedroom_prone", If(robin_here(loc_bedroom_robin) and not robin.showing, 100, 0)),
    ("robin_oskar_sex_bedroom_desk", If(robin_here(loc_office_ll), 100, 0)),
    ])

label robin_oskar_sex_bedroom_blow:
    $ npc_race_picker(oskar)
    show robin_blowjob with dissolve
    pcm "Oh? Sucking on your landlords cock?"
    pcm "Make sure you do a good job. He knocks off more rent the better you do."
    pcm "Dirty slut!"
    pcm "Mmmmm..."
    "I watch for a bit as [robin.name] sucks off [oskar.name] and i just enjoy the show."
    jump robin_oskar_sex_spy_mast_choice

label robin_oskar_sex_bedroom_doggy:
    $ npc_race_picker(oskar)
    show robin_doggy with dissolve
    pcm "Oh? Bent over for him are you?"
    pcm "Just paying the rent? Looks like you are having way more fun than that."
    pcm "Dirty slut!"
    pcm "Mmmmm..."
    "I watch for a bit as [oskar.name] takes [robin.name] from behind and enjoy the show."
    jump robin_oskar_sex_spy_mast_choice

label robin_oskar_sex_bedroom_onback:
    $ npc_race_picker(oskar)
    show robin_onback with dissolve
    pcm "Oh? Spreading your legs for him?"
    pcm "Laying back and thinking of the rent? Yeah right, you are enjoying this way too much."
    pcm "Dirty slut!"
    pcm "Mmmmm..."
    "I watch for a bit as [oskar.name] fucks [robin.name] and her moaning away and enjoy the show they are putting on."
    jump robin_oskar_sex_spy_mast_choice

label robin_oskar_sex_bedroom_prone:
    $ npc_race_picker(oskar)
    show robin_prone with dissolve
    pcm "Oh? Letting him take you like that?"
    pcm "Just paying the rent? Yeah right. Eat that pillow!"
    pcm "Dirty slut!"
    pcm "Mmmmm..."
    "I watch for a bit as [oskar.name] takes [robin.name] from behind and enjoy the show."
    jump robin_oskar_sex_spy_mast_choice

label robin_oskar_sex_bedroom_desk:
    $ npc_race_picker(oskar)
    show robin_againstdesk with dissolve
    pcm "Oh? Coming in here to pay the rent?"
    pcm "Ha, just bent over his desk like that? I knew you were such a slut."
    pcm "Hmmm, can she see me?"
    pcm "Whatever."
    "I watch for a bit as [oskar.name] takes [robin.name] from behind and enjoy the show."
    jump robin_oskar_sex_spy_mast_choice

label robin_oskar_sex_spy_mast_choice:
    $ relax(numgen(3,6))
    $ player.add_desire_random(100)
    if perversion_can_trigger_mast():
        $ player.face_shy()
        pcm "Maybe I can do something with myself..."
        menu:
            "Touch myself":
                jump robin_oskar_sex_spy_mast_mast
            "Move away":
                pcm "Hmm, better not."
    else:
        "Eventually they start moving and I worry I will be caught, so I move away."
    $ renpy.scene()
    with dissolve
    pcm "Dirty bitch."
    jump travel

label robin_oskar_sex_spy_mast_mast:
    pc "Mmmmm..."
    $ player.masturbate(True)
    $ relax(numgen(3,6))
    pcm "Haa fuck! [robin.name] you dirty whore!"
    pcm "Letting him fuck you like that just to pay the rent."
    if oskar.sex:
        pcm "Maybe one day we will fuck him together. I bet he would love that."
    pcm "Mmmm, let him take you!"
    pcm "Haaaaa!"
    $ player.masturbate_cum()
    pcm "Fuck yes! Yes! Haaaa..."
    pcm "..."
    $ player.masturbate_end()
    $ renpy.scene()
    with dissolve
    pcm "That was fun. Hope no one saw..."
    jump travel



label robin_oskar_sex_watch_firsttime:
    $ player.face_worried()
    pcm "Hmmm, I can just pretend I walked in..."
    $ walk(robin_here(class_loc=True))
    $ player.face_shock()
    pc "Oh! Sorry, I didn't know..."
    robin.name "Ah [name]!"
    if loc(loc_bedroom_robin):
        if t.minute < 10:
            show robin_blowjob
        elif t.minute > 20 and not robin.showing:
            show robin_prone front
        else:
            show robin_onback pout
    else:
        show robin_againstdesk
    with dissolve
    $ player.face_neutral()
    pc "Err... Having fun?"
    robin.name "What are you doing here?"
    pc "I just came in..."
    robin.name "Then go away!"
    pc "..."

    if "pc_knows_likes_watching" in robin.list:
        pc "You like to watch others get fucked. This time I'll have fun watching you."
    elif robin.isslut:
        pcm "Dirty slut like you getting shy now? I think I will watch."
    else:
        pc "No, this looks fun. I think I'll watch."

    robin.name "[name]!"
    pc "[oskar.name] doesn't seem to mind."
    oskar.name "Nnng!"
    pc "See."
    $ if_showing("robin_prone", "happy", "robin_onback", "oh")
    robin.name "Whatever. You slut."
    pc "Says the one getting fucked by her landlord!"
    if oskar.sex:
        robin.name "Like you don't do the same."
        pc "Not right now."
    oskar.name "You don't need to keep talking. Keep it up and I'll bend you over."
    pc "Yeah sure. Looks like you have your hands full anyway."
    oskar.name "Nnng!"
    pc "Haha!"
    $ renpy.scene()
    $ walk(loc_from)
    pcm "Haha, that was fun."
    jump travel

label robin_oskar_sex_watch_picker:
    if not "oskar_sex_watched" in robin.list:
        $ add_to_list(robin.list, "oskar_sex_watched")
        jump robin_oskar_sex_watch_firsttime

    $ walk(robin_here(class_loc=True))
    pc "Oh? Having fun?"

    if loc(loc_bedroom_robin):
        if t.minute < 10:
            show robin_blowjob
        elif t.minute > 20 and not robin.showing:
            show robin_prone
        else:
            show robin_onback
    else:
        show robin_againstdesk
    with dissolve

    robin.name "Hey pervert."
    pc "Mmmm."
    pcm "Maybe I can have some fun as well?"
    menu:
        "Enjoy myself as well":
            jump robin_oskar_sex_watch_start
        "Leave them to it":
            pcm "Na, I should probably leave them."
            pc "Don't make too muh mess."
            $ walk(loc_from)
            jump travel

label robin_oskar_sex_watch_start:
    if not c.nude:
        pc "Want something fun to look at while you are fucking her?"
        call robin_oskar_sex_pc_strip from _call_robin_oskar_sex_pc_strip
    pc "Mmmmm..."

    hide sb_pose_showbreasts
    hide sb_pose_lookback
    $ renpy.show(random(["sb_mast_stand", "sb_pose_upvag"]), [rightover])
    with dissolve
    $ player.masturbate(True)
    $ if_showing("sb_pose_upvag", "mast")
    pc "Mmm. Keep fucking the slut."
    jump expression WeightedChoice([
    ("robin_oskar_sex_watch_mast", 100),
    ("robin_oskar_sex_watch_switch", 100),
    ("robin_oskar_sex_watch_pose", 100),
    
    ])

label robin_oskar_sex_pc_strip:
    $ pc_striptease()
    if numgen():
        show sb_pose_showbreasts happy at rightover with dissolve
        pc "[rlist.foreplay_like_boobs_ask]"
    else:
        show sb_pose_lookback happy at rightover with dissolve
        pc "[rlist.foreplay_like_ass_ask]"
    return

label robin_oskar_sex_watch_mast:
    pc "Keep going [oskar.name]!"
    pc "Get as much rent money off her as you can."
    robin.name "[name]!"
    pc "Shush! Get fucked."
    pc "By your dirty pervert of a landlord."
    pc "Mmmmmm..."
    $ player.masturbate_cum()
    pcm "Fuck yes! Yes! Haaaa..."
    pcm "..."
    $ player.masturbate_end()
    $ renpy.scene()
    with dissolve
    pc "Ha, I'll leave you to it you dirty girl."
    $ pc_dress_slow()
    $ walk(loc_from)
    pcm "Hehe."
    jump travel

label robin_oskar_sex_watch_switch:
    pc "Keep going [oskar.name]!"
    pc "Get as much rent money off her as you can."
    robin.name "[name]!"
    pc "Shush! Get fucked."
    hide robin_blowjob
    hide robin_onback
    hide robin_againstdesk
    hide robin_prone
    with dissolve
    $ add_to_list(robin.list, "no_location")
    $ add_to_list(loc_bedroom_robin.list, "light_on")
    pc "By your dirty pervert of a landlord."
    $ tempname = oskar
    $ quest_temp = quest_rent
    $ event_end_interrupt_label = "robin_oskar_sex_watch_switch_end"
    $ player.face_shock()
    $ player.masturbate_end()
    $ renpy.scene()
    if numgen():
        $ renpy.show(renpy.random.choice(["sb_onfours poke", "sb_doggy1 poke", "sb_doggy2 pokevaghold"]))
        with hpunch
        pc "Ah!"
        robin.name "Haha, slut!"
        robin.name "You get fucked."
        jump whore_street_sex_floor_vag_picker
    else:
        $ renpy.show(renpy.random.choice(["sb_againstwall2 pokeasshand wink worried", "sb_againstwall3 poke wink", "sb_table bentover happy mast"]))
        with hpunch
        pc "Ah!"
        robin.name "Haha, slut!"
        robin.name "You get fucked."
        jump whore_street_sex_standing_vag_picker

label robin_oskar_sex_watch_switch_end:
    $ renpy.scene()
    show robin happy nude at right1
    with dissolve
    pc "Ugh. Cheaters. Making me pay your rent."
    robin.name "Ha, your own fault for being nosey."
    pc "Ugh..."
    $ pc_dress_slow()
    robin.name "See ya."
    $ remove_from_list(robin.list, "no_location")
    $ remove_from_list(loc_bedroom_robin.list, "light_on")
    hide robin with dissolve
    pc "Yeah..."
    jump travel

label robin_oskar_sex_watch_pose:
    pc "Keep going [oskar.name]!"
    pc "Get as much rent money off her as you can."
    robin.name "[name]!"
    pc "Hmmm, maybe I should give you something nicer to look at?"
    hide sb_pose_upvag
    hide sb_mast_stand
    show sb_againstwall3 slant wink happy at rightover
    with dissolve
    pc "Mmmm, what do you think you perverts?"
    "I wiggle my ass at them both, giving something nice to look at."
    pc "Or maybe something like this?"
    hide sb_againstwall3
    show sb_standassup happy at rightover
    with dissolve
    pc "Hehe, can see everything like this."
    pc "You like it?"

    if not numgen(0,3):
        $ add_to_list(robin.list, "no_location")
        $ add_to_list(loc_bedroom_robin.list, "light_on")
        hide robin_blowjob
        hide robin_onback
        hide robin_againstdesk
        hide robin_prone
        with dissolve
        pc "Oh?"
        $ tempname = oskar
        $ quest_temp = quest_rent
        $ event_end_interrupt_label = "robin_oskar_sex_watch_switch_end"
        $ player.face_shock()
        $ player.masturbate_end()
        $ renpy.scene()
        $ renpy.show(renpy.random.choice(["sb_onfours poke", "sb_doggy1 poke", "sb_doggy2 pokevaghold"]))
        with hpunch
        pc "Ah!"
        robin.name "Haha, slut!"
        robin.name "You get fucked."
        jump whore_street_sex_floor_vag_picker

    "I stand there like this for a bit, but they are mostly ignoring me and just messing around with each other."
    pcm "No fun!"
    hide sb_standassup with dissolve
    pcm "Might as well have my own fun."
    $ renpy.show(random(["sb_mast_stand", "sb_pose_upvag mast"]), [rightover])
    with dissolve
    pc "Mmmmmm..."
    $ player.masturbate_cum()
    pcm "Fuck yes! Yes! Haaaa..."
    pcm "..."
    $ player.masturbate_end()
    $ renpy.scene()
    with dissolve
    pc "Ha, I'll leave you to it you dirty girl."
    $ pc_dress_slow()
    $ walk(loc_from)
    pcm "Hehe."
    jump travel

label robin_oskar_sex_watch_robin:
    "Robin jumps sammy and oskar fucks sammy"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
