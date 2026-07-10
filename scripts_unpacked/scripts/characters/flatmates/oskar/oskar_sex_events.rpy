label oskar_sex_debug:
    "Debug sex with oskar"
    menu:
        "High horny":
            jump oskar_sex_behind_rough
        "Low horny":
            jump oskar_sex_foreplay_start
        "Med horny":
            jump expression renpy.random.choice(["oskar_sex_foreplay_start", "oskar_sex_lapsit_start", "oskar_sex_behind_rough"])





label oskar_sex_striptease:
    pc "[rlist.foreplay_like_clothes_ask]"
    $ dialouge = WeightedChoice([
    ("You dirty Gamines are always walking around looking like you are asking for it.", 1),
    ("I think everyone notices those giant tits when you walk past.", If (player.breasts == 3 , 1,0)),
    ("Hard to look you girls in the eye when dressed like that.", If (c.clevage , 1,0)),
    ("The way those things bounce around it's no wonder you get attention.", If (c.clevage and not c.bra and player.breasts >= 2, 1,0)),
    ("Watching you from behind cleaning up round here is always nice.", If (c.ass , 1,0)),
    ("Seeing if you are wearing anything under that skirt is always nice.", If (c.skirt , 1,0)),
    ])
    oskar.name "[dialouge]"
    pc "[rlist.foreplay_want_undress_ask]"
    oskar.name "Sure. Let's see what you have under there."
    $ pc_striptease()
    $ renpy.scene()
    if numgen():
        show sb_pose_showbreasts happy
        with dissolve
        pc "[rlist.foreplay_like_boobs_ask]"
    else:
        show sb_pose_lookback happy
        with dissolve
        pc "[rlist.foreplay_like_ass_ask]"

    oskar.name "Mmmm."

    return





label oskar_sex_clothes_remove:
    show oskar at right6 with dissolve
    $ player.face_surprised()
    oskar.name "Get these off!"
    $ pc_strip_tops()
    with hpunch
    pc "Ah! Eager are we?"
    oskar.name "Watching you girls walk around here all day. Of course."
    $ pc_strip()
    pc "Oh?"
    return





label oskar_sex_foreplay_start:
    if not (c.nude or ("work" in tab_top and c.outfit == 20)):
        call oskar_sex_striptease from _call_oskar_sex_striptease
    $ renpy.scene()
    show sb_lapsit
    with dissolve
    pc "Don't mind if I sit here do you?"
    show sb_lapsit sit with dissolve
    pc "Mmm. Comfortable."
    show sb_lapsit grope with grope_trans
    pc "Oooh? Like that do you?"
    oskar.name "[rlist.foreplay_badgirl_comment]"
    with grope_trans
    pc "Just getting comfortable."
    oskar.name "Right."



    if numgen():
        jump oskar_sex_lapsit_start
    else:
        jump oskar_sex_behind_gentle






label oskar_sex_blowjob:
    $ renpy.scene()
    show sb_blowjob
    with dissolve
    $ player.sex_oral(oskar, quest_rent)
    "Sammy blows him."
    $ player.sex_cum(oskar, "mouth", quest_rent)
    jump travel





label oskar_sex_lapsit_start:
    if not (c.nude or ("work" in tab_top and c.outfit == 20)):
        call oskar_sex_striptease from _call_oskar_sex_striptease_1
    $ renpy.scene()
    show sb_lapsit
    with dissolve
    show sb_lapsit sit with dissolve
    pc "Whats that you got there? I can feel something."
    oskar.name "Have a look if you want."
    with grope_trans
    pc "Feels like it's trying to poke me."
    oskar.name "Sounds about right."
    show sb_lapsit squat with dissolve
    $ c.pants = 0
    show sb_lapsit poke with dissolve
    if numgen():
        show sb_lapsit sit with dissolve
        pc "Oh? What's that?"
        with grope_trans
        pc "Something is poking me. What is it?"
        oskar.name "[rlist.foreplay_badgirl_comment]"
        with grope_trans
        oskar.name "I need to let you feel what it is."
        pc "Oh?"
        show sb_lapsit squat with dissolve
        pc "Ah, something trying to sneak inside?"
    else:
        with grope_trans
        pc "Oh wow?"
        oskar.name "[rlist.foreplay_badgirl_comment]"
    $ player.sex_location_offer( 
    diff=0,
    option1="Guide his cock into my pussy",option2="Press his cock against my ass", option3="Let him decide",
    sex_vag_want="oskar_sex_lapsit_vag",
    sex_vag_notwant="oskar_sex_lapsit_vag",
    sex_anal="oskar_sex_lapsit_anal",
    who=oskar.name
    )





label oskar_sex_lapsit_vag:
    "I wiggle myself so his cock is pressed right at my opening, ready for him to slide inside."
    $ player.sex_vag(oskar, quest_rent)
    show sb_lapsit sit sex with dissolve
    "[rlist.having_sex_penetrate_vag_slow_pull]"
    "[rlist.having_sex_action]"
    oskar.name "[rlist.having_sex_man_dirtytalk]"
    "[rlist.having_sex_enjoy]"
    "[rlist.having_sex_man_close]"
    $ player.sex_cum_location_offer(
    difficulty=0, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="oskar_sex_vag_cum_want", 
    cum_notwant="oskar_sex_vag_cum_notwant", 
    cum_pullout="oskar_sex_cum_pullout",
    cum_pullout_poke="oskar_sex_cum_pullout_poke",
    cum_pullout_anal="oskar_sex_cum_pullout_anal",  
    cum_pullout_bj="oskar_sex_cum_cum_pullout_blowjob",  
    cum_bj="oskar_sex_cum_cum_blowjob",    
    )

label oskar_sex_lapsit_anal:
    "I rub his cock a bit against by vagina, making it nice and wet then reposition myself so it is pressed against my ass."
    $ player.sex_anal(oskar, quest_rent)
    show sb_lapsit sit sex with dissolve
    "[rlist.having_sex_penetrate_ass_slow_pull]"
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_man_dirtytalk]"
    "[rlist.having_sex_pc_close_anal]"
    "[rlist.having_sex_man_close]"
    menu:
        "Mmm, fill me up!":
            jump oskar_sex_ass_cum_want
        "Mmm. Pull out and cover me with your cum!":
            if player.check_speech(2):
                jump oskar_sex_cum_pullout
            else:
                jump oskar_sex_ass_cum_notwant

label oskar_sex_behind_gentle:
    if not (c.nude or ("work" in tab_top and c.outfit == 20)):
        call oskar_sex_striptease from _call_oskar_sex_striptease_2
    $ renpy.scene()
    show sb_table bentover happy
    with dissolve
    "[oskar.name] stands up and leans me over, pressing me against the table."
    show sb_table mast with dissolve
    $ c.pants = 0
    show sb_table sex with dissolve
    $ player.sex_location_offer(
    diff=4,
    option1="Let him continue",option2="Ask for anal", option3="Mmmm",
    sex_vag_want="oskar_sex_behind_gentle_vag_want",
    sex_vag_notwant="oskar_sex_behind_rough_vag_notwant",
    sex_anal="oskar_sex_behind_rough_anal",
    who=oskar.name
    )

label oskar_sex_behind_gentle_vag_want:
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ player.sex_vag(oskar, quest_rent)
    $ player.face_excited()
    show sb_table ag
    if player.want_sexlocation == 2:
        pc "[rlist.having_sex_thats_not_anal_happy]"

    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    oskar.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    if numgen():
        oskar.name "[rlist.having_sex_man_close_dialogue]"
        $ player.sex_cum_location_offer(
        difficulty=3, choice_inside="Keep going!", choice_pullout="Not inside.",
        cum_want="oskar_sex_vag_cum_want", 
        cum_notwant="oskar_sex_vag_cum_notwant", 
        cum_pullout="oskar_sex_cum_pullout",
        cum_pullout_poke="oskar_sex_cum_pullout_poke",
        cum_pullout_anal="oskar_sex_cum_pullout_anal",  
        cum_pullout_bj="oskar_sex_cum_cum_pullout_blowjob",  
        cum_bj="oskar_sex_cum_cum_blowjob",    
        )
    else:
        "[oskar.name] really starts to pick up the pace and fucks me much harder while slapping my ass."
        jump oskar_sex_behind_rough_jump

label oskar_sex_behind_rough:
    if not (c.nude or ("work" in tab_top and c.outfit == 20)):
        call oskar_sex_clothes_remove from _call_oskar_sex_clothes_remove
    $ renpy.scene()
    show sb_table bentover mast shock
    with hpunch
    "[oskar.name] roughly shoves me over the desk."
    $ player.spank()
    pc "Ah!"
    show sb_table sex happy with dissolve
    pc "Not wasting any time are you? I excite you that much?"
    "[rlist.having_sex_tease_vag]"
    $ player.sex_location_offer(
    diff=4,
    option1="Let him continue",option2="Ask for anal", option3="Mmmm",
    sex_vag_want="oskar_sex_behind_rough_vag_want",
    sex_vag_notwant="oskar_sex_behind_rough_vag_notwant",
    sex_anal="oskar_sex_behind_rough_anal",
    who=oskar.name
    )

label oskar_sex_behind_rough_vag_want:
    "[rlist.having_sex_penetrate_vag_forced]"
    $ player.sex_vag(oskar, quest_rent)
    pc "[rlist.having_sex_yes]"
    jump oskar_sex_behind_rough_jump

label oskar_sex_behind_rough_vag_notwant:
    "[rlist.having_sex_penetrate_vag_forced]"
    $ player.sex_vag(oskar, quest_rent)
    show sb_table shock
    "[rlist.having_sex_thats_not_anal_angry]"
    "He doesn't listen and keeps fucking me while gripping onto my ass."
    pc "I told you in the ass!"
    $ player.spank()
    oskar.name "[rlist.having_sex_man_dirtytalk]"
    pc "Idiot."
    pcm "Not like I have much choice if I want the rent paid."
    jump oskar_sex_behind_rough_jump

label oskar_sex_behind_rough_jump:
    "He keeps fucking me hard and his fingers dig deep into my ass while he holds onto me."
    "[rlist.having_sex_enjoy]"
    "[rlist.having_sex_action]"
    pc "[rlist.having_sex_yes]"
    $ player.sex_cum_location_offer(
    difficulty=4, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="oskar_sex_vag_cum_want", 
    cum_notwant="oskar_sex_vag_cum_notwant", 
    cum_pullout="oskar_sex_cum_pullout",
    cum_pullout_poke="oskar_sex_cum_pullout_poke",
    cum_pullout_anal="oskar_sex_cum_pullout_anal",  
    cum_pullout_bj="oskar_sex_cum_pullout_blowjob",  
    cum_bj="oskar_sex_cum_blowjob",    
    )

label oskar_sex_behind_rough_anal:
    "[rlist.having_sex_vag_to_ass]"
    $ player.sex_anal(oskar, quest_rent)
    show sb_table ag
    pc "Aiii. Be more gentle... Haaa..."
    $ player.spank()
    oskar.name "[rlist.having_sex_man_dirtytalk]"
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_man_close]"
    if numgen():
        menu:
            "Cum in my arse!":
                jump oskar_sex_ass_cum_want
            "Pull out, not inside":
                if player.check_speech(1):
                    jump oskar_sex_cum_pullout
                else:
                    jump oskar_sex_ass_cum_notwant

    $ player.sex_cum(oskar, "anal", quest_rent)
    "Without warning I feel him bucking at my ass and pushing himself as deep inside me as he can."
    oskar.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    $ player.spank()
    oskar.name "[rlist.foreplay_badgirl_comment]"
    pc "A little warning next time."
    jump oskar_sex_end





label oskar_sex_vag_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    oskar.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(oskar, "inside", quest_rent)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    $ if_showing("sb_lapsit", "squat", "sb_table", "mast")
    $ if_showing("sb_lapsit", "poke sit")
    "[rlist.having_sex_came_take_cock_out_vag]"
    jump oskar_sex_end

label oskar_sex_vag_cum_notwant:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    oskar.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(oskar, "inside", quest_rent)

    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    oskar.name "Ahh yes."
    pc "Ah what are you doing?"
    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    "[rlist.having_sex_came_take_cock_out_vag]"
    $ if_showing("sb_lapsit", "squat", "sb_table", "mast")
    $ if_showing("sb_lapsit", "poke sit")
    if not player.preg_knows:
        pc "Gonna make it harder for me to earn if you put something inside me..."
    pc "*Sigh*"
    jump oskar_sex_end

label oskar_sex_cum_pullout_poke:
    $ if_showing("sb_lapsit", "poke squat", "sb_table", "shock")
    $ player.sex_cum(oskar, "pullout", quest_rent)
    oskar.name "[rlist.having_sex_man_yes]"
    $ if_showing("sb_lapsit", "sit poke", "sb_table", "mast",)
    pc "Ah I can feel it!"
    oskar.name "[rlist.having_sex_man_yes]"
    pc "Phew."
    jump oskar_sex_end

label oskar_sex_cum_pullout:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    oskar.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ if_showing("sb_lapsit", "squat", "sb_table", "mast")
    $ if_showing("sb_lapsit", "sit poke")
    $ player.sex_cum(oskar, "ass", quest_rent)
    "[rlist.having_sex_cumming_pullout_action]"
    oskar.name "[rlist.having_sex_man_yes]"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    jump oskar_sex_end

label oskar_sex_cum_pullout_blowjob:
    pc "[rlist.having_sex_pc_cum_ass_pullout_ask]"
    $ if_showing("sb_lapsit", "squat", "sb_table", "mast",)
    $ renpy.scene()
    show sb_blowjob poke up
    with dissolve
    show sb_blowjob suck down 2h with dissolve
    $ player.sex_cum(oskar, "mouth", quest_rent)
    pc "Mmmmmfffff."
    oskar.name "[rlist.foreplay_badgirl_comment]"
    pc "Ubbbbbb."
    oskar.name "Nnnnnggggg..."
    show sb_blowjob poke up ub 2h with dissolve
    show sb_blowjob neutral with dissolve
    pc "Phew."
    jump oskar_sex_end

label oskar_sex_cum_blowjob:
    $ if_showing("sb_lapsit", "squat", "sb_table", "mast",)
    $ renpy.scene()
    show sb_blowjob poke 2h up
    with dissolve
    show sb_blowjob swallow closed with dissolve
    oskar.name "[rlist.having_sex_man_yes]"
    $ player.sex_cum(oskar, "face", quest_rent)
    oskar.name "[rlist.foreplay_badgirl_comment]"
    oskar.name "[rlist.having_sex_man_yes]"
    show sb_blowjob neutral with dissolve
    show sb_blowjob neutral up with dissolve
    oskar.name "[rlist.foreplay_badgirl_comment]"
    pc "Phew."
    jump oskar_sex_end

label oskar_sex_ass_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    oskar.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(oskar, "anal", quest_rent)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_ass_want]"
    $ if_showing("sb_lapsit", "squat", "sb_table", "mast")
    $ if_showing("sb_lapsit", "poke sit")
    "[rlist.having_sex_came_take_cock_out_ass]"
    jump oskar_sex_end

label oskar_sex_ass_cum_notwant:
    pc "[rlist.having_sex_pc_cum_ass_pullout_ask]"
    oskar.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"

    $ player.sex_cum(oskar, "anal", quest_rent)

    "[rlist.having_sex_cumming_inside_ass_notwant_action]"
    oskar.name "Ahh yes."
    pc "Ah what are you doing?"
    pc "[rlist.having_sex_came_inside_ass_notwant_reaction]"
    oskar.name "[rlist.having_sex_came_inside_ass_notwant_excuse]"
    "[rlist.having_sex_came_take_cock_out_ass]"
    $ if_showing("sb_lapsit", "squat", "sb_table", "mast")
    $ if_showing("sb_lapsit", "poke sit")
    pc "*Sigh*"
    jump oskar_sex_end

label oskar_sex_end:
    if event_end_interrupt_label and not event_end_interrupt_label == "oskar_sex_end":

        jump expression event_end_interrupt_label
    pc "Mmm."
    $ renpy.scene()
    with dissolve
    $ pc_dress()
    if rent_total_owed():
        pc "Don't forget to knock that off the rent ♥"
        oskar.name "Right."
        $ rent_pay(quest_rent.soldprice, cash=False)
        oskar.name "I'll knock off £[quest_rent.soldprice] for that."

    if rent_weeks_skipped() >= 2:
        oskar.name "You had better come up with some money soon, because you are already far behind."
        pc "Sure."
    if "work" in tab_top and quest_cleaner.workcycle:
        pcm "Well, better get back to work."
        jump action_clean_event_picker
    else:
        pc "See you."
        jump travel

label oskar_sex_home_init:

    show oskar at right1 with dissolve
    if not loc(loc_bedroom):
        $ player.face_worried()
        oskar.name "[name], lets have a chat in private."
        pc "Right... Okay."
        $ walk(loc_bedroom)
    else:
        $ player.face_shock()
        pc "Ah, knock why don't you?"
    oskar.name "Been a while since you visited my office."
    if oskar.rape or rent_total_owed():
        pc "Yeah..."
        oskar.name "How about we have some fun in here?"
        if oskar.rape:
            pcm "Better make this shit happy."
            pc "Okay."
        else:
            pc "Feeling pent up are we?"
    else:
        pc "Ah yeah, feeling lonely?"
        oskar.name "You could say that."
        pc "Mmmm..."
    $ quest_rent.soldprice = player.set_whore_price(2)
    $ tempname = oskar
    $ quest_temp = quest_rent
    $ npc_race_picker(oskar)
    $ event_end_interrupt_label = "oskar_sex_end"
    if not c.nude:
        call oskar_sex_striptease from _call_oskar_sex_striptease_3
    else:
        oskar.name "Mmmm."
    jump whore_street_sex_start_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
