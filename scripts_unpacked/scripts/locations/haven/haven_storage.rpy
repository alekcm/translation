label haven_storage_stool_join:
    show havman at right1 with dissolve
    hav "Whatcha doing in 'ere luv?"
    show haven_storage headdown
    hide havman
    with dissolve
    $ player.face_worried()
    pc "Err..."
    hav "Gettin wood for the fire? Ere, lemme give ya a hand."
    pc "Err, no it's..."
    show haven_storage man hold with dissolve
    hav "Gotta be careful in ere. Be sure you don't fall and crack ya head."
    pc "It's fine. I got what I wanted from here. Let go so I can get down."
    hav "Ah is that right?"
    $ c.bottom = 0
    $ c.pants = 0
    show haven_storage shortsdown with vpunch
    $ player.sex_forced(havenman, main_quest_05)
    pc "Hey, what are you doing?!"
    hav "Oh look at that. Yer shorts fell down."
    $ player.face_angry()
    pc "Fuck you!"
    "I try to step off the stool and push against him, but the shorts around my legs are pinning my thighs together and preventing me from properly taking a step."
    show haven_storage with hpunch
    "Taking my hands off the shelves to pull them up ends up making me wobble on the stool and almost fall off."
    show haven_storage thigh with dissolve
    pc "Hey! I am going to fall if you keep this up!"
    hav "Then stop struggling an ya won't fall on yer head."
    pc "Fuck you. Stop groping me!"
    hav "An where would the fun in that be?"
    pc "Cunt!"
    hav "An what is this you have up your arse? A nice little toy for me to play with."
    $ player.face_worried()
    pc "Leave me alone."
    hav "You sure? Not like you couldn't get some wood from the lower shelves so what you doing up 'ere anyway? Bet you wanted this to happen."
    pc "What? No!"
    hav "Lot of weird girls in this place. Gotta take these chances as they come."
    show haven_storage finger with dissolve
    "I feel his thumb at my entrance slide inside me while his fingers bury themselves between my lips."
    pc "Ahhh hey what are you doing?"
    hav "Taking the chance that has come."
    "He gently thumb fucks me while his fingers press against and massage my clit while doing so."
    if player.desire >= 80:
        hav "Already soaking wet down ere. Looks like you did want this to happen. Bet you been standin' up there for ages waiting for someone to come in and stick somethin in ya."
    else:
        hav "Not much resistance getting inside you. Looks like you are already a horny bitch."
    pcm "Fuck, this plug they gave me is always making me horny."
    show haven_storage mast with dissolve
    pc "What are you doing?"
    hav "No point in only you getting off on this. I can have some fun as well."
    pcm "Fuck!"
    pcm "Well if he gets off then he will lose interest in me. So might as well not complain."
    "I stand there on the wobbly stool, trying not to fall off while he fucks me with his thumb while rubbing my clit with his fingers."
    $ junk_var_1 = 0
    if player.check_sex_agree(3, notif=False):
        $ junk_var_1 += 1
        pc "Haaaa ♥"
        pcm "..."
    "His thumb fucking grows in intensity and I find my hips rocking with the motion of his hand."
    if player.check_sex_agree(4, notif=False):
        $ junk_var_1 += 1
        pc "Ahhh ♥"

    if junk_var_1 == 2:
        hav "Mmm, having fun are you? I'll give you something much bigger if you want."
    if player.has_perk([perk_sucu, perk_slut], notif=True) or (junk_var_1 == 2 and player.check_sex_agree_choice(diff=5, option1="Mmmmmm \u2665", option2="Ah stop!")):
        jump haven_storage_stool_join_sex
    else:
        jump haven_storage_stool_join_cont

label haven_storage_stool_join_sex:
    show haven_storage noshorts with dissolve
    "He pulls my shorts fully down to my feet making it possible to step out of them and onto the floor"
    hide haven_storage with dissolve
    "But instead of getting myself proper, I bend over and present myself to him without a word."
    $ c.top = 0
    show haven_presentass lookback at right with dissolve
    "He wastes little time considering my offer..."
    show haven_presentass poke lookdown with dissolve
    $ player.beingraped = False
    $ player.sex_vag(havenman, main_quest_05)
    show haven_presentass inside with dissolve
    pc "Haaaa ♥"
    "I stay there with my eyes closed, concentrating on what is penetrating me from behind. I think I hear him saying something but I don't pay any attention."
    "My focus is entirely on the hard, throbbing cock that is slamming into me with deep, aggressive thrusts."
    $ player.spank()
    pc "Mmmmm ♥"
    hav "Ah you dirty girl."
    hav "Haaaa!"
    hav "Such broken whores in this place looking for kicks."
    "I mostly ignore him and just get off on what he is giving me. He is a bit clumsy but I am mostly having fun."
    "Then I start feeling his thrusts getting more erratic and his breathing heavy..."
    $ player.sex_cum_location_offer(
    difficulty=3, choice_inside="Keep going!", choice_pullout="Not inside.",  
    cum_want="haven_storage_stool_join_sex_cum_want", 
    cum_notwant="haven_storage_stool_join_sex_cum_notwant", 
    cum_pullout="haven_storage_stool_join_sex_cum_pullout",   
    )

label haven_storage_stool_join_sex_cum_want:
    pcm "Is he going to fill me?"
    $ player.sex_cum(havenman, "inside", main_quest_05)
    hav "Ahhhhhh yes!"
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    "I just lay there feeling the warmth in my belly, wondering if he will father me a child."
    show haven_presentass poke lookback with dissolve
    show haven_presentass noman with dissolve
    pcm "..."
    pcm "Suppose I had better get dressed."
    hide haven_presentass
    show havman at right1
    with dissolve
    jump haven_storage_stool_join_sex_post

label haven_storage_stool_join_sex_cum_notwant:
    pcm "Is he pulling out?"
    $ player.sex_cum(havenman, "inside", main_quest_05)
    hav "Ahhhhhh yes!"
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    pcm "Fuck!"
    "I just lay there feeling the warmth in my belly, wondering if he will father me a child."
    show haven_presentass poke lookback with dissolve
    show haven_presentass noman with dissolve
    pcm "..."
    pcm "Suppose I had better get dressed."
    hide haven_presentass
    show havman at right1
    with dissolve
    jump haven_storage_stool_join_sex_post

label haven_storage_stool_join_sex_cum_pullout:
    pcm "I know what this means..."
    pcm "Better suck him off before he puts something inside me."
    hide haven_presentass with dissolve
    show haven_blow cum with dissolve
    show haven_blow 1h with dissolve
    "It only takes a little bit of effort before..."
    $ player.sex_cum(havenman, "mouth", main_quest_05)
    hav "Ahhhhhh yes!"
    pc "Mmmmfff!"
    hav "Ahahaaa..."
    show haven_blow wait ub with dissolve
    show haven_blow neutral with dissolve
    pause 2
    hide haven_blow
    show havman at right1
    with dissolve
    jump haven_storage_stool_join_sex_post

label haven_storage_stool_join_sex_post:
    "Without a word, I put my shorts on, remembering to grab the crowbar, and leave the room."
    $ pc_dress()
    pause 0.5
    hide havman
    $ walk(loc_haven_lounge)
    pause 0.5
    $ player.face_annoyed()
    pc "*Tsk*"
    pcm "I shouldn't have got carried away like that..."
    $ player.face_normal()
    jump travel

label haven_storage_stool_join_cont:
    $ player.sex_cum(havenman, "self", main_quest_05)
    with hpunch
    pc "Ahhhhhh ♥"
    "I get caught in the throes of orgasm and my knees turn to jelly. All that is stopping me from falling off the stool is the guy holding me up with the hand that has his thumb now buried to the knuckle into my vagina."
    pc "Ah fuck!"
    pc "Haaaa!"
    "Despite almost falling off from having an orgasm, he doesn't let up and continues to thumb fuck me while furiously masturbating himself."
    hav "Enjoy that did ya."
    pc "..."
    pc "Huff..."
    hav "Ahhhhh..."
    $ player.sex_cum(havenman, "floor", main_quest_05)
    "He cums all over the floor and shelves while still burying his thumb deep in my vagina."
    "And without waiting around much, he pulls his thumb out with a *pop* and quickly heads out the door before I can recover."
    show haven_storage noman
    hide havman
    with dissolve
    pc "Arsehole..."
    $ pc_dress()
    show haven_storage shortsup with dissolve
    pc "*Sigh*"
    hide haven_storage with dissolve
    pause 0.5
    $ player.face_annoyed()
    pc "*Tsk*"
    pcm "I shouldn't have got carried away like that..."
    pcm "Well, at least he didn't notice the tool I managed to swipe."
    $ player.face_normal()
    jump travel

label haven_storage_stool:
    pcm "I can see something there that would hold my weight so I can get to that toolbox."
    if haven_time_empty():
        pcm "The room is empty, I should take this chance while it lasts."
    else:
        pcm "There are people in here but maybe they won't pay me any attention."
        pcm "Maybe..."
        menu:
            "Take it":
                $ NullAction()
            "Not now":
                pcm "I'll wait for a better time."
                jump travel
    "I pick up the stool and walk to the storage room with it."
    $ walk(loc_haven_storage)
    pcm "Hope no one saw me..."
    show haven_storage with dissolve
    pcm "Hmmm, too heavy for me to take down without it landing on my head first."
    pcm "What is inside?"
    pcm "..."
    pcm "Screws, nails and other little bits and bobs. Looks like it was collected after this place fell to ruin so no luck in finding any proper tools."
    pcm "Actually, what is this?"
    pcm "Seems like some kind of improvised crowbar."
    pcm "Well, not much else worth anything in there so might as well take it just in case it comes in handy."
    $ add_to_list(loc_haven_storage.list, "took_toolbox")
    $ inv.take(item_haven_crowbar)
    $ haven_storage_stool_join_chance()
    hide haven_storage with dissolve
    pcm "There we go. Not entirely sure what I will do with this. But looks like someone made it from a flat metal rod. Should be able to pry stuff with it without much issue, though no idea what."
    pcm "Not as heavy as a crowbar so can't use it to club someone with. That will at least make it easier to keep hidden at least."

    jump travel

label haven_storage_investigate:
    $ loc_haven_storage.explored = True
    pcm "A lot of junk around here. I might be able to scavenge around and find something useful."
    pcm "Best be careful though. Someone from the lounge might hear me and come see what's going on."
    pcm "Looking around while the lounge is empty would be best."
    jump travel

label haven_storage_investigate_stop:
    $ add_to_list(loc_haven_storage.list, "searched_all")
    pcm "Already searched everywhere I can think of. Doubt I am going to find anything else."
    jump travel

label haven_storage_beer1:
    pcm "Old bottle holders. Looks like they have been collected here. I guess so they can be reused to hold jars of the homemade brew they make here."
    $ add_to_list(loc_haven_storage.list, "searched_beer1")
    $ working(5)
    jump travel_arrival

label haven_storage_beer2:
    pcm "Old bottle holders. They all seem to be of the same brand, wonder if there used to be a brewery somewhere nearby."
    $ add_to_list(loc_haven_storage.list, "searched_beer2")
    $ working(5)
    jump travel_arrival

label haven_storage_boxclose:
    pcm "Old wooden crates. They don't look like they will be very useful for storing anything in so I am guessing they are used for firewood."
    $ add_to_list(loc_haven_storage.list, "searched_boxclose")
    $ working(5)
    jump travel_arrival

label haven_storage_cardboard1:
    pcm "Old paperwork and documents. Nothing important and probably used as kindling for the fires."
    $ add_to_list(loc_haven_storage.list, "searched_cardboard1")
    $ working(5)
    jump travel_arrival

label haven_storage_cardboard2:
    pcm "Old documents, but can't make out the writing on them. Not that it matters as they are just used for kindling."
    $ add_to_list(loc_haven_storage.list, "searched_cardboard2")
    $ working(5)
    jump travel_arrival

label haven_storage_crate1:
    pcm "Nothing inside other than chunks of wood. Wooden crates stored as firewood being used to hold smaller bits of kindling."
    $ add_to_list(loc_haven_storage.list, "searched_crate1")
    $ working(5)
    jump travel_arrival

label haven_storage_crate2:
    pcm "Just some kindling inside these crates."
    $ add_to_list(loc_haven_storage.list, "searched_crate2")
    $ working(5)
    jump travel_arrival

label haven_storage_debris:
    pcm "Scrap wood. Too damaged to use for repairing parts of the building so it's collected here as firewood."
    $ add_to_list(loc_haven_storage.list, "searched_debris")
    $ working(5)
    jump travel_arrival

label haven_storage_ele:
    pcm "An electric breaker box. I am going to assume it doesn't work since I haven't seen anything powered in this building since I arrived."
    $ add_to_list(loc_haven_storage.list, "searched_ele")
    $ working(5)
    jump travel_arrival

label haven_storage_shelf:
    pcm "Better not mess around with that. Don't want it falling even more and trapping me or something."
    $ add_to_list(loc_haven_storage.list, "searched_shelf")
    $ working(5)
    jump travel_arrival

label haven_storage_wood:
    pcm "Better not poke around up there. That stuff is likely to fall down and land on my head if I am not careful."
    $ add_to_list(loc_haven_storage.list, "searched_wood")
    $ working(5)
    jump travel_arrival

label haven_storage_toolbox:
    if not "searched_toolbox" in loc_haven_storage.list:
        pcm "There is some kind of toolbox up there that could have something useful inside it."
        pcm "No way I am getting to it though. Can't reach it and nothing in this room is safe to stand on. I wonder if there is anything out in the lounge?"
        $ add_to_list(loc_haven_storage.list, "searched_toolbox")
        $ working(5)
        jump travel_arrival
    else:
        pcm "I need to find something to stand on if I want to reach that. Nothing in here will support my weight though so will have to look in the lounge."
        jump travel

label haven_storage_vent:
    $ add_to_list(loc_haven_storage.list, "searched_vent")
    pcm "An air vent of sorts. Probably doesn't function any more considering how much dust is floating around in here."
    if inv.qty(item_haven_crowbar):
        pcm "I could probably pry it off with that tool I found. Might end up making some noise though..."
    jump travel

label haven_storage_vent_picker:
    if not "vent_open" in loc_haven_storage.list:
        jump haven_storage_vent_pry_prompt
    elif not "vent_investigate" in loc_haven_storage.list:
        jump haven_storage_vent_pry_investigate
    elif not "vent_climbedin" in loc_haven_storage.list:
        jump haven_storage_vent_pry_climbin


label haven_storage_vent_pry_prompt:
    pcm "I could pry the vent to see if there is anything behind. It will make a lot of noise though."
    menu:
        "Pry the vent open":
            pcm "Ok, here goes..."

            window hide
            pause 0.5
            $ add_to_list(loc_haven_storage.list, "vent_open")
            with vpunch

            pause 0.5
            window auto
            pcm "..."
            pcm "Did anyone hear..."
            pcm "..."
            $ haven_storage_join_chance()
            pcm "Ok, looks like I am good."
            $ working(10)
            jump travel
        "Not right now":


            pcm "I will wait for a better time."
            jump travel


label haven_storage_vent_pry_investigate:
    pcm "Hmm, it is pretty dark in there. I can see some stuff at the back but whether it is anything useful or just dead rats I have no idea."
    pcm "I am going to pretty much climb right in to investigate..."
    pcm "Fuck, that's just asking for trouble. Knowing the shits in this place, if I get caught stuck in there then... Ugh!"
    $ add_to_list(loc_haven_storage.list, "vent_investigate")
    jump travel

label haven_storage_vent_pry_climbin:
    pcm "So, am I going to risk diving in there to see what's inside?"
    menu:
        "No, not worth it":
            pcm "Better not right now."
            jump travel
        "Yes, let's see what might be in there":
            $ add_to_list(loc_haven_storage.list, "vent_climbedin")
            $ player.face_worried()
            pcm "..."
            pcm "*Sigh*"
            $ player.face_normal()
            pcm "Uff, here goes."
            show haven_vent at right2 with dissolve
            pcm "..."
            pcm "Let's see here..."
            show haven_vent shock with hpunch
            pc "Eek!"
            pcm "No idea what that was but I am not touching it again..."
            show haven_vent neutral
            pcm "..."
            pcm "Hmm, this feels more promising..."
            pcm "A bag maybe?"
            $ haven_storage_vent_join_chance()
            pcm "What's in it?"
            $ haven_storage_vent_join_chance()
            $ working(15)
            hide haven_vent with dissolve
            pcm "Cigs? 1, 2... 4 packs of cigs and 2 bottles of brew."
            $ inv.take(item_brew, 2)
            $ inv.take(item_cigs, 4)
            $ player.face_happy()
            pcm "Not like I can go and retire from this. But better than nothing."
            $ player.face_normal()
            pcm "But better get out of here before I am caught with my bounty."
            pause 0.5
            $ walk(loc_haven_lounge)
            pcm "Nothing at all suspicious. Pay no attention to me..."
            $ walk(loc_haven_hallway_2f)
            pcm "Looks good to me."
            jump travel

label haven_storage_ventopen_join:
    $ add_to_list(loc_haven_storage.list, "vent_caught")
    show haven_vent man with dissolve
    $ player.face_worried()
    pcm "Huh?"
    show haven_vent conf with dissolve
    pcm "..."
    pcm "Thought I felt something."
    $ c.bottom = 0
    $ c.pants = 0
    show haven_vent shortsoff shock with vpunch
    $ player.face_angry()
    pc "Ah fuck what are you doing!"
    show haven_vent with hpunch
    pc "Fuck..."
    show haven_vent with hpunch
    pc "Off!"
    pcm "Ah fuck no!"
    pcm "I can feel his cock against me. What do I do..."
    pcm "Fuck fuck fuck!"
    $ player.sex_forced(havenvent, main_quest_05)
    $ player.sex_vag(havenvent, main_quest_05)
    $ player.face_pain()
    show haven_vent giveup tears with dissolve
    pcm "Ah fuck no! No no no!"
    $ player.face_cry()
    pc "*Sob*"
    pcm "I... Can't... Get out...!"
    show haven_vent with hpunch
    pcm "..."
    show haven_vent with hpunch
    pc "Get off!"
    pc "*Sob*"
    show haven_vent with hpunch
    pcm "All I am doing is pushing harder on his cock."
    pcm "..."
    pc "*Sob*"
    "I lay in the vent defeated and just rock back and forward to his aggressive thrusts. With no way out, all I can do is just lay there and take it."
    "Knowing there is nothing I can do to resist, he takes his time fucking me so my ordeal seems to go on and on..."
    $ working(20)
    "Until I can feel it."
    $ player.sex_cum(havenvent, "inside", main_quest_05)
    pcm "..."
    show haven_vent neutral with dissolve
    pc "*Sob*"
    pcm "Is he done?"
    show haven_vent noman with dissolve
    pcm "Fucking bastard. Get off me!"
    show haven_vent with hpunch
    $ randomnum = renpy.random.randint(1, 10)
    if randomnum == 1:
        jump haven_storage_ventopen_join_end

    "As he pulls out, I try to push against him to get out of the vent, but I feel a pair of hands pushing against me and preventing me from getting out."
    show haven_vent man with dissolve
    pcm "Fucking fuck. What is he doing?"
    show haven_vent shock with dissolve
    pcm "Ahh no. He's trying to put it back in me?!"
    pcm "I felt him go soft inside me... No no... This is someone else?"
    pc "*Sob*"
    $ player.sex_forced(havenvent, main_quest_05)
    $ player.sex_vag(havenvent, main_quest_05)
    pc "At shit!"
    show haven_vent giveup with dissolve
    pc "*Sob*"
    "The new intruder wastes no time in fucking me, seemingly not caring that I have already just been fucked and probably came in."
    pcm "Hurry and be over."
    pcm "Hurry up and be over."
    pcm "Hurry and be over."
    $ working(20)
    $ player.sex_cum(havenvent, "inside", main_quest_05)
    pcm "..."
    show haven_vent noman conf with dissolve
    pcm "Is it over?"

    $ randomnum = renpy.random.randint(1, 10)
    if randomnum == 1:
        jump haven_storage_ventopen_join_end
    else:
        show haven_vent man giveup with dissolve
        "Ah he pulls out, I am still held into the vent. I don't put up much resistance when I feel a new person lining themselves up with my slit."
        $ player.sex_forced(havenvent, main_quest_05)
        $ player.sex_vag(havenvent, main_quest_05)
        "Once again I am fucked with little regard. Taken like some toy attached to the wall for all of their entertainment."
        $ working(20)
        pcm "..."
        $ player.sex_cum(havenvent, "inside", main_quest_05)
        pc "*Sob*"
        show haven_vent noman with dissolve
        $ randomnum = renpy.random.randint(1, 10)
        if randomnum == 1:
            jump haven_storage_ventopen_join_end
        else:
            jump haven_storage_ventopen_join_cont

label haven_storage_ventopen_join_cont:
    pause 1
    show haven_vent man with dissolve
    pause 1
    $ player.sex_forced(havenvent, main_quest_05)
    $ player.sex_vag(havenvent, main_quest_05)
    "And I am fucked again..."
    pause 1
    $ working(20)
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        $ player.sex_cum(havenvent, "pullout", main_quest_05)
        "And came on again..."
    else:
        $ player.sex_cum(havenvent, "inside", main_quest_05)
        "And came in again..."
    pause 1
    show haven_vent noman with dissolve

    $ randomnum = renpy.random.randint(1, 8)
    if randomnum == 1:
        "Until eventually when the last guy leaves, no one comes to take his place."
        jump haven_storage_ventopen_join_end
    else:
        jump haven_storage_ventopen_join_cont

label haven_storage_ventopen_join_end:
    $ player.face_cry()
    pc "*SOB*"
    pc "..."
    show haven_vent conf with dissolve
    pcm "Are they done?"
    pcm "I had better get out of here..."
    $ player.face_normal()
    pcm "Nnng."
    hide haven_vent with dissolve
    pcm "Fuck fuck fucking bastards!"
    show sb_pose_upvag with dissolve
    pcm "Fuckers. I am leaking like shit..."
    pcm "ARSEHOLES!"
    hide sb_pose_upvag with dissolve
    pcm "I can't believe that just happened..."
    pcm "And all for a bag with cigs and brew in it."
    $ inv.take(item_brew, 2)
    $ inv.take(item_cigs, 4)
    pcm "..."
    $ haven_drink_brew()
    $ player.face_worried()
    pc "*HACK* *COUGH*"
    pcm "..."
    $ pc_dress()
    $ player.face_cry()
    pcm "*SOB*"
    $ walk(loc_haven_lounge)
    $ player.face_cry()
    $ walk(loc_haven_hallway_2f)
    $ player.face_cry()
    $ walk(loc_haven_landing)
    $ player.face_cry()
    $ walk(loc_haven_lobby)
    $ player.face_cry()
    $ walk(loc_haven_hallway_1f)
    $ player.face_cry()
    $ walk(loc_haven_bedroom)
    $ player.face_cry()
    $ walk(loc_haven_bed)
    $ player.face_cry()
    pcm "Shitty fuckers!"
    pcm "*SOB*"
    jump haven_bed_sleep
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
