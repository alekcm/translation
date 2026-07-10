label robin_action_park_adventure_picker:
    if not robin_here(dis_home.locs):
        pcm "I should ask when we are at home since the park is nearby."
        jump travel
    if not t.timeofday == "night":
        pcm "I should wait until night before inviting her."
        jump travel
    show robin at right1 with dissolve

    if not "park_bitch_intro" in robin.list:
        jump robin_action_park_adventure_invite
    else:
        "This will be a repeatable event for park bitching. very soon but not written yet. Next build"
        jump travel

label robin_action_park_adventure_invite:
    $ add_to_list(robin.list, "park_bitch_intro")
    pc "Sooo..."
    robin.name "Mmm?"
    pc "I found something new and fun to do."
    show robin happy
    robin.name "Oh? What is it?"
    pc "Do you trust me?"
    show robin worried
    robin.name "Err... No way. Not while you have that look on your face."
    pc "Okay, do you trust me not to send you off to be killed?"
    robin.name "Mostly."
    pc "Good enough. Follow me."
    show robin neutral
    robin.name "Okay..."
    show robin at left1
    $ walk(loc_stairwell)
    robin.name "This to do with the bus?"
    pc "No, much closer. Fun on our doorstep."
    $ walk(loc_residential)
    pc "So remember, this is all for fun."
    robin.name "Huh? You aren't going to tell me what it is?"
    pc "No. I want you to experience it in the most fun way I can think of."
    robin.name "Right..."
    $ walk(loc_park)
    pc "So... Put this on."
    if acc.choker == 6:
        $ acc.choker = 0
    show robin at right6 with dissolve
    robin.name "A collar?"
    pc "Yup."
    robin.name "Right..."
    show robin bitch with dissolve
    pc "Now you know the back entrance to the school?"
    robin.name "Yeah, through the dark and shady trees."
    pc "Yeah, go there and come back."
    robin.name "What? That's all?"
    pc "Yup."
    robin.name "Why do I feel there is more to this than that?"
    pc "Just remember, to bail on the fun, just take the collar off."
    robin.name "..."
    $ player.face_evil()
    pc "Go! Before monsters get you!"
    robin.name "Right..."
    robin.name "School and back?"
    $ player.face_neutral()
    pc "That's right, take you no time at all."
    robin.name "..."
    hide robin with dissolve
    "I stand there watching as [robin.name] walks slowly through the park. She keeps looking back and is suspicious as hell."
    "But seems she trusts me enough so pushes forward until I can no longer see her."
    pcm "Right, what do I do with myself now. I told her 10 minutes but if all does to plan, she will take ages."
    show wolfman roar at right4 with hpunch
    "Wolfman" "Rwaaa!"
    $ player.face_shock()
    pc "Ah!"
    pc "No collar!"
    if "can_bitch" in rachel.list:
        show wolfman stand with dissolve
        wolf.name "I know. Sent another one our way have you?"
        pc "Yeah. Show her a good time."
        if "can_bitch" in rachel.list:
            wolf.name "She going to be as much trouble as the last one you sent?"
            pc "Na, she should be more willing to go along with your games."
            wolf.name "Heh, we will see."
        else:
            wolf.name "That we can do."
        hide wolfman with dissolve
    else:
        call robin_action_park_adventure_firsttime_explain from _call_robin_action_park_adventure_firsttime_explain_1
    "With nothing better to do, I just hang around waiting. Pretty sure [robin.name] should come this way and I should be able to catch her."
    $ relax(30)
    pcm "Maybe I should have went with her. Boring just hanging around here..."
    show wolfman roar at right6 with hpunch
    "Wolfman" "Raaaaa!"
    $ player.face_annoyed()
    pc "I heard you in the bushes."
    show wolfman stand with dissolve
    "Wolfman" "Getting better at this."
    $ player.face_neutral()
    pc "How's my friend doing?"
    "Wolfman" "Err, good."
    pc "Good?"
    "Wolfman" "She's trying to fight them off. But it's clear she is having fun so I told the guys to go wild."
    $ player.face_happy()
    pc "Ah that's good. Send her back a mess."
    "Wolfman" "That's the plan."
    "Wolfman" "Here, another collar. Something tells me your friend will want to keep hers."
    $ wardrobe.take(item_choker_6, all_notif=True)
    $ player.face_neutral()
    pc "How long is she going to be? Getting boring hanging out here."
    "Wolfman" "I don't think she is going to be in a hurry to return so you're gonna be here a while."
    pc "Ugh. Thanks."
    hide wolfman with dissolve
    pcm "So going to be standing around here for ages..."
    pcm "Maybe I should do something to pass the time?"
    menu:
        "Put on the collar":
            jump robin_action_park_adventure_invite_bitch
        "Get naked and mess around":

            jump robin_action_park_adventure_invite_strip
        "Wait around like normal":

            "I end up jut standing around in the park bored out of my mind, kicking the odd stone I see on the floor."
            "I see some people creeping around in the bushes, but since I know they wont jump me I mostly ignore them."
            $ relax(20)
            "In fact knowing they are hiding there makes me feel a lot safer standing here alone in the dark since they will kick the ass of any actual rapists."
            jump robin_action_park_adventure_invite_recover

label robin_action_park_adventure_invite_bitch:
    pcm "No point in letting [robin.name] have all the fun."
    $ acc.choker = 6
    pcm "Hmmm, I thought that pervert would have been spying on me and ready to jump out."
    pcm "Oh well, I suppose I will..."
    $ player.grope()
    $ player.face_shock()
    wolf.name "Gotcha!"
    pc "Ah! I knew it!"

    call action_wolfpack_grabbed_strip_call from _call_action_wolfpack_grabbed_strip_call_1

    pc "Aiiee!"
    wolf.name "I knew a bitch like you couldn't resist."
    pc "Woof!"
    wolf.name "Haha!"
    $ event_end_interrupt_label = "robin_action_park_adventure_invite_bitch_end"
    $ npc_race = 1
    jump action_wolfpack_grabbed_resist_sex_prepare_doggy

label robin_action_park_adventure_invite_bitch_end:
    pcm "Phew. Well, that went just as expected."
    pcm "Better take the collar off though or I'll get jumped again and miss [robin.name]."
    $ acc.choker = 0
    pcm "Hope I haven't already missed her."
    $ pc_dress_slow()
    jump robin_action_park_adventure_invite_recover

label robin_action_park_adventure_invite_strip:
    pcm "Hmm, well it's dark here and I am alone..."
    $ player.eye = 6
    pcm "..."
    $ player.eye = 5
    pcm "Why not?"
    $ player.face_neutral()
    $ player.uncover()
    $ pc_strip()
    pc "..."
    show ps_dance with dissolve
    pc "♪ I'm naked in the park. I'm naked in the park. ♪"
    $ renpy.scene()
    show dance_behind
    with dissolve
    pc "Doo do de do de do I'm naked in the park. ♪"
    pcm "Hehe, no collar so the perverts in the bushes can only watch."
    hide dance_behind
    show sb_doggy1 ah
    with hpunch
    pc "Oooooh noooooo... I fell over."
    pc "While naked."
    pc "Nothing to protect me from perverts."
    pc "It's a good job no weirdos are hiding in the bushes watching me."
    pc "Who knows what would happen if there were people hiding."
    pc "Oooooh noooooo..."
    pc "Hahahaha!"
    hide sb_doggy1 with dissolve
    pc "Phew."
    show sb_pose_lookback with dissolve
    pc "♪ I have a naked ass. I have a naked ass. ♪"
    pc "Doo do de do de do I have a naked ass. ♪"
    hide sb_pose_lookback with dissolve
    pc "..."
    show sb_sitting right with dissolve
    with grope_trans
    pc "Ah!"
    pc "Bench is cold..."
    pcm "Better not get a splinter in my ass."
    $ relax(15)
    "I sit around waiting, watching the perverts skulk around in the bushes and just killing time."
    "Then I manage to see one of them coming out and over to me."
    hide sb_sitting with dissolve
    jump robin_action_park_adventure_invite_recover

label robin_action_park_adventure_invite_recover:
    show wolfman stand at right4 with dissolve
    "Wolfman" "Heads up, looks like your friend is making her way back. Should be here soonish."
    pc "Ah, thanks."
    hide wolfman with dissolve
    $ pc_dress_slow()
    $ relax(5)
    "I wait around and finally manage to see what looks like [robin.name] staggering around in the dark."
    pcm "Hmm, is that actually her? I think it is."
    "I walk over to her and realise she is a complete mess."
    show robin cuffed gagged bitch park_cum mess at right1 with dissolve
    $ player.face_laugh()
    pc "Oh wow. You look way worse than my first time."
    robin.name "Mmmmff!!"
    $ player.face_happy()
    pc "Yeah, something like that. Wanna go home?"
    robin.name "Mmmmmmfff Unnggg mmmfff!"
    pc "Sure, no problem. Let's go."
    hide robin
    $ walk(loc_park)
    pcm "Hehe."
    show robin cuffed gagged bitch park_cum mess at right6 with dissolve
    robin.name "MMMMMFFFFFFF!!! FFFMMMMMMMMM!!"
    pc "Oh? You want me to free you?"
    robin.name "Mmmmfffff!"
    $ add_to_list(robin.list, "no_location")
    menu:
        "Get her free":
            pc "I suppose so..."
            pc "Turn around."
            show robin at left1 with dissolve
            pc "Let's see here..."
            show robin worried with dissolve
            pc "There we go."
            show robin
            robin.name "Ugh, I can hardly walk."
            pc "Fucked that much were you?"
            robin.name "And someone put a huge fucking butt plug in me!"
            pc "Oh? Haha. They really did show you a fun time."
            robin.name "Are you going to undo my arms?"
            pc "Oh? I suppose so."
            show robin arm_up with dissolve
            robin.name "Thanks."
            show robin neutral at right1 with dissolve
            robin.name "That was way more than I expected..."
            pc "Have fun?"
            robin.name "Yeah..."
            robin.name "Was a bit scary when the first guy jumped out the bushes. But he reassured me before doing anything."
            pc "Did you make it to the school entrance?"
            robin.name "Barely made it anywhere."
            pc "Shame. Going to have to send you there again then and keep your end of the deal."
            robin.name "Haha. Yeah right. I'd like to see you try."
            pc "I have tried."
            pc "Failed. But tried."
            robin.name "Let's go home instead of talking naked in the park."
            pc "Only you are naked. I am fine talking here."
            robin.name "C'mon."
            hide robin with dissolve
            pc "..."
            pcm "She going home alone?"
            pc "..."
            show robin worried bitch park_cum mess at right1 with dissolve
            robin.name "Come on. Don't leave me walking home alone butt naked."
            pc "Why not?"
            robin.name "It's embarrassing."
            pc "You just let anyone within 20 mins walk of here fuck you, and now you are embarrassed?"
            robin.name "Ugh..."
            hide robin with dissolve
            pc "Haha!"
            $ walk(loc_residential)
            pcm "Hmmm, did she actually go home?"
            $ walk(loc_stairwell)
            pcm "Can't see her anywhere."
            $ walk(loc_kitchen)
            pc "[robin.name]?"
            $ add_to_list(loc_bedroom_robin.list, "light_on")
            show robin bitch park_cum mess at right1
            $ walk(loc_bedroom_robin)
            pc "Ah, you did get home ok?"
            robin.name "Yeah, no help from you."
            pc "I untied you at least."
            robin.name "Yeah, but left me naked in the wind."
            pc "Well, got to have a little fun myself."
            robin.name "Yeah, and now it's my turn."
        "Walk home":

            pc "Okay, turn around so I can get this."
            show robin at left1 with dissolve
            robin.name "Mmff..."
            hide robin
            $ walk(loc_residential)
            pcm "Hehe."
            $ walk(loc_stairwell)
            pcm "Have fun [robin.name]."
            $ walk(loc_kitchen)
            pcm "I'll wait here for her."
            pcm "..."
            $ relax(10)
            pcm "Hmm, she is taking her time..."
            pcm "Hope she isn't waiting for me to come back."
            pcm "Oh, I head her."
            show robin cuffed gagged bitch park_cum mess at right1 with dissolve
            pc "Took your time."
            robin.name "Mmmmmf!"
            pc "Ok, seriosuly now, I'll take that off."
            show robin at left1 with dissolve
            pc "Let's see here..."
            show robin worried with dissolve
            pc "There we go."
            show robin
            robin.name "I can hardly walk. So of course it took ages."
            pc "Fucked that much were you?"
            robin.name "And someone put a huge fucking butt plug in me!"
            pc "Oh? Haha. They really did show you a fun time."
            robin.name "Are you going to undo my arms?"
            pc "Oh? I suppose so."
            show robin arm_up with dissolve
            robin.name "Thanks."
            show robin neutral at right1 with dissolve
            robin.name "That was way more than I expected..."
            pc "Have fun?"
            robin.name "Yeah..."
            robin.name "Was a bit scary when the first guy jumped out the bushes. But he reassured me before doing anything."
            pc "Did you make it to the school entrance?"
            robin.name "Barely made it anywhere."
            pc "Shame. Going to have to send you there again then and keep your end of the deal."
            robin.name "Haha. Yeah right. I'd like to see you try."
            pc "I have tried."
            pc "Failed. But tried."
            robin.name "Let's go to your room instead of standing out here."
            pc "Okay."
            $ walk(loc_bedroom)
            robin.name "You can also help me get this thing out my ass."
            pc "Hey now. What's in your ass is your business."
            robin.name "And now yours!"

    $ player.face_worried()
    pc "Huh?"
    $ player.face_shock()
    show robin happy at right6 with hpunch
    "Without much warning, she grabs hold of me and starts pulling my clothes off."
    pc "Hey, what are you doing you crazy slut?"
    $ pc_strip_random(group=True)
    with grope_trans
    pc "Hey!"
    $ pc_strip()
    with grope_trans
    show robin happy
    robin.name "Revenge."
    $ player.face_worried()
    pc "By making me naked?"
    "Without warning, she pulls me down on the bed."
    pc "What are you..."
    hide robin
    show robin_facesit mess
    with vpunch
    robin.name "Having some more fun."
    pc "Hey, didn't you have fun with the mmmmmfffff unnngg ffffff..."
    robin.name "Stop talking."
    "[robin.name] shoves herself in my mouth as I was trying to talk, which quickly makes anything I say all muffled."
    "She doesn't even play coy, and aggressively starts humping my face as I try to gasp fo breath."
    "Breathing is not easy though as half the park seems to leak out of her and into my mouth."
    "Trying to speak just ends up with me blowing bubbles from the cum."
    "I feel her fingers invade between my legs as she is humping my face. My only real thought is trying to breathe before I choke on the cum stuck in my mouth."
    "She picks up speed and seems like she is about to cum, which I thought was a good thing."
    "Until I realise her contractions are squeezing more cum out of her and on my face. Some of which leaking into my nose."
    pc "Mmmmff blllaaaaaabb!!!"
    robin.name "Almooooostt!!!"

    $ renpy.show_screen("cum_action", "pink", numgen(1,2), False)
    robin.name "Ahhh fuck yes!!"
    pc "Mmmmmmfff!"
    robin.name "Ahhh yes."
    $ player.cum_locations["cum_mouth"] += 5
    $ player.cum_locations["cum_face"] += 3
    "She doesn't get up just yet and just sits on my face for a bit enjoying the afterglow. But at least I can manage a little bit of air."
    "Then she just gets up and walks out the room."
    hide robin_facesit with dissolve
    $ player.face_shock()
    pc "*GAAAAASP*"
    pc "*Huff* *Huff* *Huff*"
    pc "Christ [robin.name]. Almost killed me."
    pcm "Hmmm, where did she go?"
    $ player.face_puke()
    pc "*Ubbb*"
    pcm "How many people ended up fucking her for that amount to come out?"
    $ player.face_neutral()
    pcm "Hmm, sounds like she is in the shower."
    if not loc(loc_bedroom):
        $ walk(loc_bedroom)
    pcm "Guess I will wait til she is done."
    $ pc_dress()
    $ remove_from_list(loc_bedroom_robin.list, "light_on")
    $ remove_from_list(robin.list, "no_location")
    $ add_to_list(robin.list, "done_bitching")
    $ add_to_list(robin.list, "can_bitch")
    jump travel

label robin_action_park_adventure_firsttime_explain:


    show wolfman stand with dissolve
    "Wolfman" "I know. I was hiding and listening to you two."
    $ player.face_annoyed()
    pc "Creep."
    "Wolfman" "Well, yeah."
    $ player.face_neutral()
    "Wolfman" "Let's talk somewhere quiet so I'm not standing out here in the open."
    pc "Okay."
    $ walk(loc_park_gazebo)
    "Wolfman" "I saw you send your friend in there with the collar. Want me to make sure the guys take it easy on the newbie?"
    pc "Take it easy? Why? Don't remember you guys ever going easy on me."
    "Wolfman" "Hmm, usually we try and go easy on new girls. Don't want to scare them away."
    "Wolfman" "More fun when they keep coming back."
    pc "Ah, don't need to worry about her. If you go easy on her then she would probably just prefer dragging guys from the pub to the motel."
    "Wolfman" "Oh? So not new to messing around?"
    pc "Na, We have our fun. Better if you do the opposite and make sure she is targeted."
    "Wolfman" "Seriously?"
    pc "Yeah. Pretty sure she will wear the whole park out before she takes that collar off."
    "Wolfman" "Remember we take making the girls happy seriously. If this is some kind of prank then you will be a target."
    pc "No worries. It's all good fun."
    "Wolfman" "I'll still keep an eye out just in case."
    pc "Sure. Go make sure she is having fun."
    "Wolfman" "Mmmm..."
    hide wolfman with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
