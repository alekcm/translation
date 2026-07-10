label rachel_talk_exhib_bitching_start:
    show rachel at right1 with dissolve
    if not c.nude:
        jump rachel_talk_exhib_strip

    if not "bitch_intro_spoke" in rachel.list:
        $ add_to_list(rachel.list, "bitch_intro_spoke")
        pc "So you know you were telling me about that girl in the park."
        rachel.name "Yeah. She was having fun!"
        pc "Well, I kinda found out what she was up to."
        rachel.name "Did you get chased?"
        pc "Err, kind of."
        pc "It turns out it's a game people play in the park."
        rachel.name "Yeah, I saw that."
        pc "..."
        pc "Well, it didn't sound like it at first."
        rachel.name "Why not?"
        pc "Err... Never mind. Anyway, I found out how they do it."
        rachel.name "Go there naked?"
        pc "A little more to it than that. There is a collar you have to wear to show you are playing."
        rachel.name "Yeah? Do you have one?"
        pc "I do... But only one."
        rachel.name "Give it! Give it!"
        pc "If you want, let's go there together."
        rachel.name "Okay! Lets go!"
    else:
        rachel.name "Ready to show me what they were doing in the park?"
    menu:
        "Go now":
            $ NullAction()
        "Another time":
            rachel.name "Aww! Well, hurry up!"
            pc "Right..."
            jump travel

    if loc_walk_school_forest.visited:
        pc "Want to walk there naked or get the bus?"
        rachel.name "Walk there naked? We will get jumped on."
        pc "I know a back way through the trees. Should be ok to go like that."
        rachel.name "Err, sure? Up to you."

        menu:
            "Get the bus":
                pc "Bus is probably better. I'll go get changed."
                rachel.name "Okay."
                jump rachel_talk_exhib_bitching_travel_bus
            "Walk naked through the trees":

                jump rachel_talk_exhib_bitching_travel_trees
    else:

        pc "Okay, but we should probably dress up. We need to get the bus."
        rachel.name "Ugh, if you insist."
        jump rachel_talk_exhib_bitching_travel_bus

label rachel_talk_exhib_bitching_travel_bus:
    hide rachel
    $ pc_dress_event("party", loc_school_locker_girls)
    show rachel at right1
    pc "Ok, ready?"
    rachel.name "Yeah."

label rachel_talk_exhib_bitching_travel_trees:
    pc "Okay then, let's go."
    rachel.name "Sure!"
    $ player.uncover()
    show rachel at left1 with dissolve
    $ walk(loc_school_hallway)
    pc "Got to go through the back way like this."
    $ walk(loc_school_field)
    pc "Don't get caught!"
    $ walk(loc_school_secret_entrance)
    pc "Okay, should be safe here."
    show rachel at right5 with dissolve
    rachel.name "Outside naked with a street just over there?"
    pc "Yeah, close enough."
    rachel.name "Where now?"
    pc "Now there is a path down a dark and scary forest with rapists hiding in the trees."
    rachel.name "Oooh, scary."
    pc "First, take this."
    if acc.choker == 6:
        $ acc.choker = 0
    $ show_notif_popup("Gave " + rachel.setname + " the Bitch collar")
    rachel.name "Okay. Do I wear it?"
    pc "Of course."
    $ add_to_list(rachel.list, "can_bitch")
    show rachel with dissolve
    rachel.name "What does it do?"
    pc "It makes the rapists rape you."
    rachel.name "Don't need a collar for that. They do it anyway."
    pc "Err, well these aren't real rapists."
    rachel.name "No?"
    pc "It's some guys pretending to be dogs and they will fuck anyone with that collar on."
    rachel.name "Oh? And I just stand here?"
    pc "No, go down the dark and scary path."
    rachel.name "Okay."
    hide rachel with dissolve
    pcm "Wow, no hesitation."
    pcm "..."
    pcm "I should probably follow."
    $ walk(loc_walk_park_forest)
    pcm "..."
    jump rachel_talk_exhib_bitching_arrived


label rachel_talk_exhib_bitching_arrived:
    $ walk(loc_park_gazebo)
    pcm "Can't seem to see her."
    show wolfman roar at right1 with dissolve
    pc "No collar doggie."

    if "can_bitch" in robin.list:
        show wolfman stand with dissolve
        wolf.name "I know. Sent another one our way have you?"
        pc "Yeah. Not sure this one will be as easy to deal with though."
        if "can_bitch" in rachel.list:
            wolf.name "The short hair girl was easy enough."
            pc "Yeah, this one is a bit of a mixed bag. She might leave your guys running instead."
            wolf.name "Heh, we will see."
        else:
            wolf.name "I'm sure we can manage."
        hide wolfman with dissolve
    else:
        call robin_action_park_adventure_firsttime_explain from _call_robin_action_park_adventure_firsttime_explain

    "With nothing better to do, I just hang around waiting. Pretty sure [rachel.name] should come this way and I should be able to catch her."
    $ relax(30)
    pcm "Hope everything is ok..."
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
    "Wolfman" "She is a feisty one isn't she?"
    $ player.face_happy()
    pc "That's one way to put it."
    pc "She having fun?"
    wolf.name "I wasn't sure at first. She fought back pretty hard so I called the guys off."
    pc "Oh?"
    wolf.name "But then she started chasing after the guys."
    pc "Really?"
    wolf.name "Last I saw, she had jumped on one of their backs shouting \"giddy up\"."
    pc "Hahahaha!! Really?"
    wolf.name "I think she will be alright."
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
            jump rachel_talk_exhib_bitching_wait_bitch

        "Wait around naked" if c.nude:
            jump rachel_talk_exhib_bitching_wait_naked

        "Wait around like normal" if not c.nude:
            "I end up jut standing around in the park bored out of my mind, kicking the odd stone I see on the floor."
            "I see some people creeping around in the bushes, but since I know they wont jump me I mostly ignore them."
            $ relax(20)
            "In fact knowing they are hiding there makes me feel a lot safer standing here alone in the dark since they will kick the ass of any actual rapists."
            jump rachel_talk_exhib_bitching_recover


label rachel_talk_exhib_bitching_wait_naked:
    pcm "Hmm, well it's dark here and I am alone and naked."
    $ player.eye = 6
    pcm "..."
    $ player.eye = 5
    pcm "Might as well have some fun."
    $ player.face_neutral()
    $ player.uncover()
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
    jump rachel_talk_exhib_bitching_recover

label rachel_talk_exhib_bitching_wait_bitch:
    pcm "No point in letting [rachel.name] have all the fun."
    $ acc.choker = 6
    pcm "Hmmm, I thought that pervert would have been spying on me and ready to jump out."
    pcm "Oh well, I suppose I will..."
    $ player.grope()
    $ player.face_shock()
    wolf.name "Gotcha!"
    pc "Ah! I knew it!"

    call action_wolfpack_grabbed_strip_call from _call_action_wolfpack_grabbed_strip_call_2

    pc "Aiiee!"
    wolf.name "I knew a bitch like you couldn't resist."
    pc "Woof!"
    wolf.name "Haha!"
    $ event_end_interrupt_label = "rachel_talk_exhib_bitching_wait_bitch_end"
    $ npc_race = 1
    jump action_wolfpack_grabbed_resist_sex_prepare_doggy

label rachel_talk_exhib_bitching_wait_bitch_end:
    pcm "Phew. Well, that went just as expected."
    pcm "Better take the collar off though or I'll get jumped again and miss [rachel.name]."
    $ acc.choker = 0
    pcm "Hope I haven't already missed her."
    $ pc_dress_slow()
    jump rachel_talk_exhib_bitching_recover


label rachel_talk_exhib_bitching_recover:
    show wolfman stand at right4 with dissolve
    "Wolfman" "Heads up, looks like your friend is making her way back. Should be here soonish."
    pc "Ah, thanks."
    hide wolfman with dissolve
    $ relax(5)
    "I wait around and catch sight of [rachel.name] rushing through the trees."
    pcm "Hmm, is that actually her? I think it is."
    "I wait for her to come over."
    show rachel bitch_effects happy at right1 with dissolve
    $ player.face_worried()
    pc "Oh wow. Err, is that blood?"
    rachel.name "Where?"
    pc "On your face."
    rachel.name "Maybe."
    pc "Maybe? What happened?"
    rachel.name "They want me to be a doggie. Some doggies bite."
    pc "You bit them?"
    rachel.name "Only some of them."
    rachel.name "They escaped me afterwards."
    pc "Err. Okay..."
    rachel.name "It was fun. Can I keep the collar?"
    pc "Sure, I got a new one form some naked pervert."
    rachel.name "Great."
    rachel.name "Wait..."
    show rachel evil at left4 with dissolve
    rachel.name "I SEE YOU THERE!!!"
    hide rachel with hpunch
    "I watch as [rachel.name] chases down of of the perverts."
    pc "Wow..."
    pc "Okay..."
    pcm "Guess I will leave her be then..."
    pcm "Have fun."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
