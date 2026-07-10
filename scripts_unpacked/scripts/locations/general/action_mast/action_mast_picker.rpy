init python:
    def action_mast_event_catch_weight(amount=100):
        total = danger_weight() / 8
        if total < 2:
            
            total = 2
        weightgen(total, amount)

label action_mast_event_start:

    if dis(dis_home) or loc_cur.home_location:
        if dis(dis_home) and not loc(loc_bedroom):
            $ walk(loc_bedroom)
        jump bedroom_masturbate

    $ player.face_worried()
    pcm "Hmmm, I can have a little fun..."
    pcm "Hope I don't get caught."
    if player.has_perk(perk_exhibitionist, notif=True):


        jump action_mast_event_nude_mast_start
    else:

        pcm "Maybe somewhere like here?"
        $ walk(loc_cur.isolate_loc)
        pcm "Should be pretty quiet"
        if perk_exhib_total_value() > 300:

            jump action_mast_event_nude_mast_start

        elif perk_exhib_total_value() > 150:

            $ pc_strip_lower(slow=True)

            if c.nude:

                jump action_mast_event_nude_mast_start

            pcm "Mmm, ass out for anyone to see..."
            show sb_pose_upvag with dissolve
            show sb_pose_upvag mast with dissolve
            $ player.masturbate()
            $ if_showing("sb_pose_upvag", "mast")
            with dissolve
            pcm "Mmmmmm..."
            jump action_mast_event_mast
        else:


            pcm "I hope no one can see me..."
            $ player.face_shy()
            pcm "Fuck, am I really doing this?"
            pcm "..."
            $ player.masturbate()
            jump action_mast_event_mast

label action_mast_event_nude_mast_start:
    $ pc_striptease()
    pcm "Hehe, look at me boys. I am naked."
    if numgen():
        show sb_pose_showbreasts happy
        with dissolve
        pcm "[rlist.foreplay_like_boobs_ask]"
    else:
        show sb_pose_lookback happy
        with dissolve
        pcm "[rlist.foreplay_like_ass_ask]"
    pcm "Naked and all alone here."
    $ renpy.scene()
    $ renpy.show(random(["sb_mast_stand", "sb_pose_upvag"]), [right5])
    with dissolve
    $ player.masturbate()
    $ if_showing("sb_pose_upvag", "mast")
    with dissolve
    pcm "Mmmmmm..."
    jump action_mast_event_mast

label action_mast_event_mast:
    "I stand there touching myself, heart beating hard in my chest at fear of getting caught."
    pcm "Mmm, hope no one catches me being a slut. Seeing me do these naughty things."
    call masturbate_fantasy_picker from _call_masturbate_fantasy_picker_6
    call expression rand_choice from _call_expression_29

    if action_mast_event_catch_weight():
        jump action_mast_event_caught_tombola

    pc "Haaaaaa..."
    $ player.masturbate_cum()
    pc "Ahhh yes yes!"
    pc "..."
    $ player.face_shame()
    pc "Fuuuu..."

    if action_mast_event_catch_weight():
        jump action_mast_event_caught_tombola


    $ renpy.scene()
    with dissolve
    pcm "No one saw me did they?"
    pcm "..."
    pcm "Hehe."
    $ pc_dress_slow()
    jump travel

label action_mast_event_caught_tombola:
    jump expression WeightedChoice([

    ("action_mast_event_caught_grabbed_fun", 100),
    ("action_mast_event_caught_grabbed_leave", 100),
    ("action_mast_event_caught_grabbed_sex", 100),
    ("action_mast_event_caught_tease", 100),
    ("action_mast_event_caught_shout", 100),
    ("action_mast_event_caught_alsomast", 100),
    ("action_mast_event_caught_grabbed_force", If(danger_weight(), 100, 0)),
    ])

label action_mast_event_caught_grabbed_fun:
    $ tempname = streetguy
    $ npc_race_picker()
    $ player.face_shock()
    $ renpy.scene()
    $ player.grope()
    pc "Ah!"
    $ player.grope()
    tempname.name "Nice one darlin'!"
    pc "Hey!"
    tempname.name "Having fun are ya?"
    $ player.grope()
    tempname.name "Plenty a guys that would do this for ya."
    pc "Shoo!"
    tempname.name "Pervert having fun here all alone?"
    tempname.name "Maybe you wanna guy ta come an' giv' ya something?"
    $ player.grope()
    pc "Yeah right. Go away."
    tempname.name "Sure love."
    $ player.grope_end()
    tempname.name "Keep yaself safe. Lotta weirdos around 'ere."
    $ player.face_annoyed()
    pc "Idiot."
    pcm "..."
    $ player.face_worried()
    pcm "Got caught..."
    $ pc_dress_slow()
    jump travel

label action_mast_event_caught_grabbed_leave:
    $ tempname = streetguy
    $ npc_race_picker()
    $ player.face_shock()
    $ renpy.scene()
    $ player.grope()
    pc "Ah!"
    $ player.grope()
    tempname.name "Nice one darlin'!"
    pc "Hey!"
    $ player.grope()
    tempname.name "Haha."
    $ player.grope_end()
    tempname.name "Cheers love."
    $ player.face_annoyed()
    pc "Idiot."
    pcm "..."
    $ player.face_worried()
    pcm "Got caught..."
    $ pc_dress_slow()
    jump travel

label action_mast_event_caught_grabbed_sex:
    $ tempname = streetguy
    $ npc_race_picker()
    $ male_npc_create_all()
    $ player.face_shock()
    $ renpy.scene()
    $ player.grope()
    pc "Ah!"
    $ player.grope()
    tempname.name "Nice one darlin'!"
    pc "Hey!"
    $ player.grope()
    tempname.name "Haha."
    $ player.grope_poke()
    pc "Ah hey! What are you doing?"
    tempname.name "How about I give you something more fun?"
    pc "Pervert!"
    menu:
        "Bend over":

            pcm "..."
            $ player.grope_end()
            $ event_end_interrupt_label = "action_mast_event_caught_sex_end"
            jump whore_street_sex_sex_picker
        "Shoo him away":
            pc "No thanks!"
            $ player.grope_end()
            with hpunch
            "I wiggle out of his arms and he makes no attempt to keep me there."
            tempname.name "No problem darling."
            "I watch as he slowly walks away, still looking at me as he leaves."
            $ player.face_annoyed()
            pc "Idiot."
            pcm "..."
            $ player.face_worried()
            pcm "Got caught..."
            $ pc_dress_slow()
            jump travel

label action_mast_event_caught_grabbed_force:
    $ tempname = rapist
    $ npc_race_picker()
    $ player.face_shock()
    $ renpy.scene()
    $ player.grope()
    pc "Ah!"
    $ player.grope()
    pc "Hey!"
    pc "Let go!"
    $ player.grope()
    "He keeps groping me and his touch is very rough and kinda hurts."
    pc "Stop it. You are too rough!"
    jump whore_street_sex_forced_attack

label action_mast_event_caught_tease:
    $ tempname = streetguy
    $ npc_race_picker()
    $ male_npc_create_all()
    show male_generic at right5 with dissolve
    pcm "..."
    $ renpy.scene()
    $ player.face_shock()
    $ player.force_cover()
    with hpunch
    pc "Ah!"
    pc "Fuck!"
    tempname.name "Just watching the show."
    pc "Fucking sneaking up on me like that. Near have a heart attack!"
    tempname.name "I was here for a while."
    pc "Really? So you...?"
    tempname.name "Saw everything? Yes."
    pc "Shit."
    tempname.name "Ah shows over now anyway so I'll leave you be."
    pc "Right..."
    hide male_generic with dissolve
    pcm "..."
    $ player.face_worried()
    pcm "Got caught..."
    $ pc_dress_slow()
    jump travel

label action_mast_event_caught_shout:
    $ tempname = streetguy
    $ npc_race_picker()
    tempname.name "*Some girl getting off over here!*"
    $ player.face_shock()
    $ renpy.scene()
    with hpunch
    pc "Huh?"
    tempname.name "*Go at it girl!*"
    $ player.face_angry()
    pcm "Fuck!"
    $ pc_dress_slow()
    pcm "Arsehole."
    if loc(dis_misc) and loc_from not in dis_misc.locs:
        $ walk(loc_from)
    pcm "Can't even have a little fun..."
    jump travel


label action_mast_event_caught_alsomast:
    $ tempname = streetguy
    $ npc_race_picker()
    $ male_npc_create_all()
    show male_generic nude at right5 with dissolve
    pcm "..."
    $ renpy.scene()
    $ player.face_shock()
    $ player.force_cover()
    pc "The hell?"
    tempname.name "Aww, let me join in."
    tempname.name "We can wank together."
    pc "..."
    menu:
        "Wank together":
            pc "..."
            pc "Don't do anything else."
            tempname.name "Okay."
            if not c.nude:
                $ pc_strip()
            $ renpy.show(renpy.random.choice(["sb_againstwall2", "sb_againstwall3"]))
            "I bend over for the guy to see me better while we have some fun."
            $ if_showing("sb_againstwall2", "wink happy mast cum", "sb_againstwall3", "slant wink happy cum")
            pc "Wanking only."
            tempname.name "Yup, wanking only."
            "I continue touching myself while feeling the guy behind me wanking and no and then hitting me with his cock."
            $ player.spank()
            "I don't mind as long as he keeps just wanking, although might be a bit fun if he did try and poke me."
            tempname.name "[rlist.foreplay_badgirl_comment]"
            pc "[rlist.sex_exclaim_like]"
            tempname.name "[rlist.having_sex_man_close_dialogue]"
            $ player.sex_cum(tempname, "ass", quest_temp)
            "[rlist.having_sex_cumming_pullout_action]"
            tempname.name "Ahh yes!"
            pc "[rlist.having_sex_cumming_pullout_reaction]"
            "Feeling him cumming on my ass excites me and brings me close as well."
            $ player.masturbate_cum()
            pc "Mmmmm..."
            pc "Ahhh yeah cover my ass!"
            pc "..."
            $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman")
            tempname.name "Thanks darling."
            pc "Ha, sure."
            pc "..."
            $ renpy.scene()
            with dissolve
            pcm "Heh..."
            $ pc_dress_slow()
            jump travel
        "Shoo him away":

            pc "No, go away."
            tempname.name "Huh, thought we could have a little fun together."
            pc "..."
            show male_generic dressed with dissolve
            tempname.name "Don't worry darling. I'll go."
            pc "Thanks."
            hide male_generic with dissolve
            pcm "Shit."
            pcm "..."
            $ player.face_worried()
            pcm "Got caught..."
            $ pc_dress_slow()
            jump travel

label action_mast_event_caught_sex_end:
    $ renpy.scene()
    show male_generic at right4 with dissolve
    with dissolve
    tempname.name "Ha, never thought I would catch a naked girl in the street looking for fun."
    pc "Yeah, nor me."
    tempname.name "Well, I'll leave you to whatever you are doing."
    pc "Sure, cya."
    hide male_generic with dissolve
    pcm "..."
    $ player.face_worried()
    pcm "Got caught and fucked the guy..."
    pcm "Haha."
    $ pc_dress_slow()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
