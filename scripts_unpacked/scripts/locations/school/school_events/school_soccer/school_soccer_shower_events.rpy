label school_field_soccer_play_end_shower:
    if school_soccer_quest_hangout_prompt == True:
        drake.name "We are going to call it a day and head to the showers. Meet us out the back after if you want to hang out."
        pcm "Hmm, should I shower as well?"
        menu:
            "Shower together with the boys" if player.check_sex_agree(4, exhibitionist=True):
                $ drake.add_lust(10)
                $ nate.add_lust(10)
                $ dan.add_lust(10)
                pc "Think I'll join you guys."
                if robin_here([loc_school_field_back, loc_school_field]):
                    $ add_to_list(robin.list, "soccerboys_seen_shower")
                    $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
                $ walk(loc_school_locker_old)
                pause 0.5
                $ shower_scene_start()
                $ renpy.show(renpy.random.choice(["shower", "shower_back"]))
                $ renpy.with_statement(dissolve)
                $ player.shower()

                $ rand_choice = WeightedChoice([
                ("school_field_soccer_play_end_shower_end", 10),
                ("school_field_soccer_play_end_shower_comment", 100),
                ("school_field_soccer_play_end_shower_tease", 70),
                ("school_field_soccer_play_end_shower_join", If (school_soccer_pick_boy("lust") > 70, 100, 10)), 
                ("school_field_soccer_play_end_shower_sex_offer", If (school_soccer_cansex() and player.check_sex_agree(4) and player.desire >= 80, 30, 0)),
                ])
                jump expression rand_choice
            "Go take a shower":

                $ walk(loc_school_locker_girls)
                pause 0.5
                $ shower_scene(outfit="party")
                jump travel
            "Don't bother":
                pc "Ok, see you."
                jump travel


    elif school_soccer_hangout_offer():
        $ loc_school_field_back.locked = False
        $ loc_school_locker_old.locked = False
        drake.name "We are going to call it a day and head to shower. If you want to, you can join us out back for some beers or whatever."
        pc "Out back?"
        drake.name "Yeah, after playing we usually go hang out by the old locker rooms over there. Not got much else better to do so we just hang out."
        drake.name "Feel free to join if you want."
        pc "Ok, thanks."
        $ school_soccer_quest_hangout_prompt = True
    else:

        drake.name "We are gonna call it a day. See you around [name]."
        pc "Sure, see you."
    jump travel

label school_field_soccer_play_end_shower_comment:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_end_shower_comment_1", 100),
    ("school_field_soccer_play_end_shower_comment_2", 100),
    ("school_field_soccer_play_end_shower_comment_3", 100),
    ("school_field_soccer_play_end_shower_comment_4", 100),
    ("school_field_soccer_play_end_shower_comment_5", 100),
    ("school_field_soccer_play_end_shower_comment_6", 100),
    ("school_field_soccer_play_end_shower_comment_7", 100),
    ("school_field_soccer_play_end_shower_comment_8", 100),
    ])
    jump expression rand_choice

label school_field_soccer_play_end_shower_comment_1:
    nate.name "{color=#b3b3b3}Fuck...{/color}"
    drake.name "{color=#b3b3b3}Right?{/color}"
    nate.name "{color=#b3b3b3}...that she is...{/color}"
    pc "I can hear you idiots."
    nate.name "Umm..."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_comment_2:
    pcm "They can't keep their eyes off me."
    if player.check_nowill():
        $ player.face_shy()
        pcm "Kind of embarrassing..."
        pcm "And nice..."
    else:
        pcm "Well, didn't come here to be ignored."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_comment_3:
    $ npc_race_picker(drake, drake)
    show drake nude soft at right6
    if renpy.showing("shower"):
        show shower stand
    elif renpy.showing("shower_back"):
        show shower_back man_front
    with dissolve
    drake.name "Joining us for a beer?"
    pc "Yeah probably."
    drake.name "Great, see you out there."
    pc "Mmm."
    if renpy.showing("shower"):
        show shower noman_front
    elif renpy.showing("shower_back"):
        show shower_back noman_front
    hide drake
    with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_comment_4:
    show dan nude soft at right1 with dissolve
    dan.name "What's wrong with the girl's shower?"
    pc "Huh?"
    dan.name "What you doing in here with us?"
    pc "Got a problem with it?"
    dan.name "Err, no. Not really. You come here just to show off?"
    pc "Hmm, alone in the girls' shower at this time? Safer in here with you perverts."
    dan.name "Oh..."
    hide dan with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_comment_5:
    show nate nude soft at right6 with dissolve
    nate.name "See you outside for drinks [name]."
    $ player.spank()
    pc "Ah!"
    hide nate with dissolve
    nate.name "Hehe!"
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_comment_6:
    show nate nude hard at right6 with dissolve
    nate.name "Like what you see?"
    pc "Huh?"
    pcm "What the hell. His cock is huge!"
    nate.name "Mmmm?"
    pc "I have seen that thing before and it was never that big. What you doing around all these boys with that thing standing up? Something to tell us [nate.name]?"
    nate.name "It's all me baby!"
    pc "Pfft. Yeah right."
    hide nate with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_comment_7:
    nate.name "Waaaaaaaa!!!"
    pcm "What the?"
    nate.name "No no no!"
    dan.name "C'mere!"
    with vpunch
    nate.name "Ahhhh!"
    pcm "Nope, ignoring whatever those idiots are up to."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_comment_8:
    pc "♪ I'll put my armour on, show you how strong I am ♪"
    pc "♪ I'll put my armour on, I'll show you that I am ♪"
    nate.name "Whoo!"
    pcm "Fuck, forgot I'm not alone..."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_tease:

    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_end_shower_tease_1", 100),
    ("school_field_soccer_play_end_shower_tease_2", 100),
    ("school_field_soccer_play_end_shower_tease_3", 100),
    ("school_field_soccer_play_end_shower_tease_4", 100),
    ("school_field_soccer_play_end_shower_tease_5", 100),
    ("school_field_soccer_play_end_shower_tease_6", 100),
    ("school_field_soccer_play_end_shower_tease_7", 100),
    ("school_field_soccer_play_end_shower_tease_8", 100),
    ])
    jump expression rand_choice

label school_field_soccer_play_end_shower_tease_1:
    pc "*Psst* [nate.name]."
    show nate nude soft at right1 with dissolve
    nate.name "Mmm?"
    show sb_pose_showbreasts shower tounge with dissolve
    nate.name "Oh...?"
    hide sb_pose_showbreasts with dissolve
    pc "Heh."
    hide nate with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_tease_2:
    show nate nude soft at right1 with dissolve
    nate.name "Nice ass [name]."
    pc "Thanks ♥"
    nate.name "Err, no insult?"
    show sb_againstwall2 shower tounge with dissolve
    pc "Did I drop the soap?"
    pc "Ah no, here it is."
    hide sb_againstwall2 with dissolve
    nate.name "Err..."
    pc "Haha!"
    hide nate with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_tease_3:
    pcm "They watching me I wonder...?"
    pc "♪ Wash my ass do do do do do do ♪"
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_tease_4:
    pcm "Hmm. They have nice bodies. Guess a diet of only football and fake beer keeps you in shape."
    pcm "Starvation probably doesn't help though."
    show drake nude soft at right1 with dissolve
    drake.name "Starting to wonder who the pervert is here [name]."
    pc "Huh?"
    drake.name "Isn't it us who're supposed to be eyeing you up?"
    pc "My turn today."
    drake.name "Hrmf."
    hide drake with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_tease_5:
    pcm "Hmmm, three nude guys and naked me, all alone in here..."
    pc "Isn't it supposed to be more dangerous for me in here?"
    nate.name "What you talking about?"
    pc "Little ol me, alone and naked here with a bunch of burly guys?"
    drake.name "You find some dirty mag in the bushes and been reading the stories or something?"
    pc "You lumps!"
    dan.name "If you did find a mag, I can sell it for good money if it's not too sticky."
    pc "Ugh, I didn't find a mag."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_tease_6:
    pc "Hey [drake.name]."
    show drake nude soft at right1 with dissolve
    drake.name "Huh?"
    show sb_pose_lookback shower tounge with dissolve
    pc "Does my ass look big in this?"
    drake.name "Ugh."
    pc "Heh."
    drake.name "It will look big after I bend you over and spank you bright red."
    if bruise.ass > 0.4:
        pc "It's red enough as it is. Don't need any more spankings."
    else:
        pc "Yeah yeah, promises promises."
    hide sb_pose_lookback
    hide drake
    with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_tease_7:
    pc "What you looking at?"
    show dan nude soft at right1 with dissolve
    dan.name "Hmm?"
    pc "I see you looking at my ass."
    dan.name "Then you know what I was looking at. No need to ask."
    pc "Err, okaaaay. That is not how things should go."
    dan.name "Hmm?"
    pc "You are supposed to act all coy and look away."
    dan.name "Right. Ok. I'll keep that in mind."
    pc "..."
    pc "Might believe that if your eyes weren't glued to my tits..."
    dan.name "They are nice."
    pc "..."
    pc "Thanks."
    hide dan with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_tease_8:
    show dan nude soft at right1 with dissolve
    pc "Enjoying the view [dan.name]?"
    dan.name "Yup"
    show sb_pose_showbreasts up happy shower with dissolve
    pc "Better?"
    dan.name "Better."
    hide sb_pose_showbreasts
    show sb_pose_lookback happy smile shower
    with dissolve
    pc "How about from this side?"
    dan.name "Mmmm."
    hide sb_pose_lookback with dissolve
    pc "Heh"
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_join:
    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_end_shower_join_drake", drake.lust),
    ("school_field_soccer_play_end_shower_join_dan", dan.lust),
    ("school_field_soccer_play_end_shower_join_nate", nate.lust),
    ("school_field_soccer_play_end_shower_join_1", nate.lust),
    ("school_field_soccer_play_end_shower_join_2", dan.lust),
    
    
    
    ])
    jump expression rand_choice

label school_field_soccer_play_end_shower_join_drake:
    $ npc_race_picker(drake)
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    pc "Mmmm...?"
    drake.name "Looked like you need some help."
    pc "Oh did it now?"
    drake.name "Mmm, seems like you were struggling a bit so thought I would help out."
    if renpy.showing("shower"):
        show shower grope with dissolve
    elif renpy.showing("shower_back"):
        show shower_back grope with dissolve
    pc "Oooh?"
    if player.check_sex_agree(4):
        menu:
            "Let him continue":
                jump school_field_soccer_play_end_shower_sex_offer_drake1
            "Cool him down":
                $ NullAction()
    jump school_field_soccer_play_end_shower_sex_offer_drake_reject

label school_field_soccer_play_end_shower_join_dan:
    $ npc_race_picker(dan)
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    pc "Mmmm...?"
    dan.name "Want some help?"
    pcm "Ah, it's [dan.name]. Man of many words as always."
    if player.check_sex_agree(4):
        menu:
            "Let him continue":
                "Being that it's [dan.name] behind me, I don't even answer and just lean back against him."
                jump school_field_soccer_play_end_shower_sex_offer_dan1
            "Cool him down":
                $ NullAction()
    jump school_field_soccer_play_end_shower_sex_offer_dan_reject

label school_field_soccer_play_end_shower_join_nate:
    $ npc_race_picker(nate, nate)
    if renpy.showing("shower"):
        show shower stand with dissolve
    elif renpy.showing("shower_back"):
        show shower_back man_front with dissolve
    nate.name "Need help you dirty girl?"
    pc "From a pervert like you?"
    nate.name "No one else here. Course me."
    if player.check_sex_agree(4):
        menu:
            "Sure, give me a hand":
                jump school_field_soccer_play_end_shower_sex_offer_nate1
            "Cool him down":
                $ NullAction()
    jump school_field_soccer_play_end_shower_sex_offer_nate_reject

label school_field_soccer_play_end_shower_join_1:
    $ npc_race_picker(nate, nate)
    if renpy.showing("shower"):
        show shower stand with dissolve
    elif renpy.showing("shower_back"):
        show shower_back man_front with dissolve

    pc "Err, [nate.name]? What are you doing?"
    nate.name "Wanking."
    pc "I see that... Mind telling me why you are doing it with me standing here."
    nate.name "No porn anymore. Thought I could use you."

    if player.check_sex_agree(2):
        pc "Wow..."
        pc "Then hurry it up. Don't want to be here all day."
        nate.name "Thanks."
        "I stand there watching him wank off with morbid curiosity as he looks at my body and grips his free hand on my bum."
        pcm "Is he getting closer? Can't really tell."
        if player.check_sex_agree(3):
            menu:
                "Help him out":
                    pc "You look pitiful [nate.name]. Come here."
                    $ tempname = nate
                    jump school_field_soccer_play_end_shower_sex_bj
                "Just keep showering":
                    $ NullAction()
        pcm "Whatever, he's on his own."
        "I keep showering like normal while being constantly molested by roaming hands. Eventually he presses his body right up against me and groans while rubbing his cock against my bum."
        $ player.sex_cum(nate, "ass")
        nate.name "Ah fuck [name] you dirty bitch!"
        pc "Mmmm."
        nate.name "Ahhhh Haaaaa..."
        pc "Have your fun?"
        nate.name "Mmmm. Thanks."
        pc "Good, now shoo so I can wash your cum from my arse."
        nate.name "Right."
        $ player.spank()
        pc "Ah!"
        if renpy.showing("shower"):
            show shower noman_front with dissolve
        elif renpy.showing("shower_back"):
            show shower_back noman_front with dissolve
        jump school_field_soccer_play_end_shower_end
    pc "Shoo. Let me shower in peace."
    nate.name "Really? Ok..."
    "He takes along, lingering look at my naked body before heading into one of the other stalls, presumably to carry on having fun."
    if renpy.showing("shower"):
        show shower noman_front with dissolve
    elif renpy.showing("shower_back"):
        show shower_back noman_front with dissolve
    pc "Heh, idiot."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_join_2:
    $ npc_race_picker(dan, dan)
    if renpy.showing("shower"):
        show shower stand
    elif renpy.showing("shower_back"):
        show shower_back man_front
    show dan nude at right6
    with dissolve
    pc "Hey [dan.name]. What's..."
    $ player.eye = 6
    pause 0.4
    $ player.eye = 1
    pc "Oh."
    dan.name "Was going to do something about it but thought I would show you and see if you had any ideas."
    if player.check_sex_agree(3):
        menu:
            "Blow him":
                pc "Sure, close your eyes."
                dan.name "Ok."
                $ tempname = dan
                hide dan with dissolve
                jump school_field_soccer_play_end_shower_sex_bj
            "Let him deal with it alone":
                $ NullAction()
    pc "No thanks. You on your own with this problem."
    dan.name "Ok."
    if renpy.showing("shower"):
        show shower noman_front
    elif renpy.showing("shower_back"):
        show shower_back noman_front
    hide dan
    with dissolve
    jump school_field_soccer_play_end_shower_end




label school_field_soccer_play_end_shower_sex_offer:
    $ player.face_shy()
    pcm "Hmm, should I invite one of them to help me in the shower?"
    menu:
        "Yes, invite them":
            $ player.face_normal()
            pc "Any of you perverts want to help me wash?"
        "No, better not.":
            $ player.face_normal()
            jump school_field_soccer_play_end_shower_end

    $ rand_choice = WeightedChoice([
    ("school_field_soccer_play_end_shower_sex_offer_drake", drake.lust),
    ("school_field_soccer_play_end_shower_sex_offer_dan", dan.lust),
    ("school_field_soccer_play_end_shower_sex_offer_nate", nate.lust),
    ("school_field_soccer_play_end_shower_sex_offer_dp", drake.lust + nate.lust / 2),
    ])
    jump expression rand_choice

label school_field_soccer_play_end_shower_sex_offer_drake:
    $ npc_race_picker(drake)
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    pc "Mmmm..."
    drake.name "You such a dirty girl you can't even deal with it alone?"
    pc "Easier with some help."
    if renpy.showing("shower"):
        show shower grope with dissolve
    elif renpy.showing("shower_back"):
        show shower_back grope with dissolve
    drake.name "Yeah sure."
    jump school_field_soccer_play_end_shower_sex_offer_drake1

label school_field_soccer_play_end_shower_sex_offer_drake1:
    "I stand there as [drake.name] rubs his hands all over my body. Oddly enough, while he is rubbing me in places I never thought someone would touch, he is also doing a good job of washing me."
    $ player.face_happy()
    pc "Mmmm, doing a good job there [drake.name]."
    drake.name "If you say so."
    if renpy.showing("shower_back"):
        show shower_back penis with dissolve
    $ player.face_worried()
    pcm "That his cock poking me?"
    pcm "No surprise I guess..."
    $ player.face_shy()
    pc "Your friend there seems to need a wash as well."
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    drake.name "He's happy where he is."
    pc "Is he?"
    $ renpy.scene()
    show sb_againstwall2 shower pokevag
    with dissolve
    "I bend over and lean against the wall to give him a perfect view of what he was just poking at."
    pc "You sure?"
    pc "Shower is nice and warm, but I have somewhere warmer for a pervert like you."
    $ randomnum = renpy.random.randint(1, 20)
    if randomnum == 1:
        $ player.spank()
        pc "Ah!"
        drake.name "Come on, stop presenting yourself like a bitch and come for some beer."
        show sb_againstwall2 worried frown
        $ player.spank()
        pc "Huh?"
        show sb_againstwall2 noman with dissolve
        pc "..."
        show sb_againstwall2 angry
        pcm "Did that idiot really leave?"
        pcm "Arsehole."
        pc "..."
        pcm "Hmmm..."
        menu:
            "Finish myself off":
                jump school_field_soccer_play_end_shower_sex_mast
            "Get ready to leave":
                pc "*Sigh*"
                pcm "Not much choice..."
                hide sb_againstwall2
                $ renpy.show(renpy.random.choice(["shower", "shower_back"]))
                with dissolve
                jump school_field_soccer_play_end_shower_end
    drake.name "You are always calling me the pervert, but you are the one bent over asking to be fucked."
    pc "Not asking. Just standing here innocently washing."
    drake.name "Yeah right."
    $ player.sex_location_offer()
    $ tempname = drake
    if player.want_sexlocation == 0:
        pcm "Gonna get poked at this rate and not sure I want that..."
        jump school_field_soccer_play_end_shower_sex_bj
    elif player.want_sexlocation == 1:
        jump school_field_soccer_play_end_shower_sex_vag
    else:
        jump school_field_soccer_play_end_shower_sex_anal

label school_field_soccer_play_end_shower_sex_offer_drake_reject:
    pc "Think you need a cold shower [drake.name]."
    drake.name "Do I?"
    pc "Yup. Thanks for the offer though."
    drake.name "Right."
    if renpy.showing("shower"):
        show shower noman_behind with dissolve
    elif renpy.showing("shower_back"):
        show shower_back noman_behind with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_offer_dan:
    $ npc_race_picker(dan)
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    pc "Mmmm..."
    dan.name "..."
    pcm "Not saying anything. Must be [dan.name] behind me."
    jump school_field_soccer_play_end_shower_sex_offer_dan1

label school_field_soccer_play_end_shower_sex_offer_dan1:
    "[dan.name] makes a half hearted attempt at pretending to wash me, not that I mind. I relax in the hot water and close my eyes to the feeling of his hands over every part of my body."
    if renpy.showing("shower_back"):
        show shower_back penis with dissolve
    "It's not until I feel something that is not his hand poking between my legs that I am shook out of my wandering mind."
    "The whole point of me inviting someone was so I could have fun, so I part my legs a little and let his cock slide up directly against my labia."
    "It's not possible to penetrate me from this angle. But he is perfectly capable of humping me and getting me off like this. Basically masturbating me with his cock."
    pc "Haaaaaaa... ♥"
    "I gyrate my hips letting him rub me between my folds and helping get him off as well. I can feel his hands digging into me more and pulling me harder onto his cock."
    pc "Mmm, enjoying?"
    dan.name "Mmm..."
    pcm "Huh, he is pressing on my back trying to bend me over..."
    menu:
        "Let him":
            $ tempname = dan
            jump school_field_soccer_play_end_shower_sex_vag
        "Stay upright":
            $ NullAction()
    if player.vvirgin:
        pcm "He will take my virginity without a doubt if I bend over. And he's pretty close to cumming already so better not bend over."
    elif player.has_perk(perk_preg_notwant):
        pcm "He isn't far off blowing his load. If I bend over, I doubt I am leaving here without leaking."
    "I resist his attempts to bend me over and fuck me, and instead keep moving my hips so I am sliding my lips up and down his cock."
    "His cock is rock hard and poking right into me so I get to slide him from tip to base. He tries to angle enough to poke inside me but I make sure he can't manage it."
    "Eventually he starts thrusting between my thighs with much more aggression..."
    pc "Mmmmm..."
    pc "Going to make me even wetter down there?"
    if renpy.showing("shower"):
        show shower grope with dissolve
    elif renpy.showing("shower_back"):
        show shower_back grope with dissolve
    dan.name "Nnngg!"
    $ player.sex_cum(nosex, "pullout")
    dan.name "Ahhh!"
    pc "Oooh, I feel it throbbing ♥"
    pc "Mmmm, so dirty cumming between my legs..."
    dan.name "Ahhh..."
    dan.name "*Phew*"
    dan.name "..."
    dan.name "Err, ok... See you for beers?"
    if renpy.showing("shower"):
        show shower noman_behind with dissolve
    elif renpy.showing("shower_back"):
        show shower_back noman_behind with dissolve
    pc "Sure..."
    pcm "Nice talking to you."
    pc "..."
    pcm "Maybe I should have bent over. Still so horny..."
    pcm "Oh well."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_offer_dan_reject:
    pc "Thanks [dan.name], but not this time thanks."
    dan.name "Mmm"
    if renpy.showing("shower"):
        show shower noman_behind with dissolve
    elif renpy.showing("shower_back"):
        show shower_back noman_behind with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_offer_nate:
    $ npc_race_picker(nate, nate)
    if renpy.showing("shower"):
        show shower stand with dissolve
    elif renpy.showing("shower_back"):
        show shower_back man_front with dissolve
    nate.name "How can I turn an offer like that down?"
    pc "You? Couldn't imagine it."
    jump school_field_soccer_play_end_shower_sex_offer_nate1

label school_field_soccer_play_end_shower_sex_offer_nate1:
    if renpy.showing("shower"):
        show shower finger with dissolve
    pc "Ha, you know, most people will at least pretend to wash me at the start."
    if player.isslut:
        nate.name "No need to pretend around a slut like you."
    elif school_soccer_quest_boys_know["whore"]:
        nate.name "Not going to turn down my chance at a freebie with a whore so why pretend?"
    else:
        nate.name "Pretty obvious what you want. Why beat around the bush."
    pc "It's called foreplay [nate.name]. Warm a girl up before the big show with some teasing."
    if nate.naughty:
        pc "No wonder you have to rely on me to get yourself off with an oafish attitude like that."
    else:
        pc "Not going to have any volunteers to get you off with an oafish attitude like that."
    nate.name "Shhh, don't pretend you don't like it. We both know you are a dirty girl."
    pc "Do we now?"
    nate.name "Showering with the boys? Inviting me here while the others watch?"
    nate.name "Come here..."
    $ player.sex_location_offer()
    $ tempname = nate
    if player.want_sexlocation == 0:
        jump school_field_soccer_play_end_shower_sex_bj
    elif player.want_sexlocation == 1:
        jump school_field_soccer_play_end_shower_sex_vag
    else:
        jump school_field_soccer_play_end_shower_sex_anal

label school_field_soccer_play_end_shower_sex_offer_nate_reject:
    pc "No thanks, go and have some fun with him on your own."
    nate.name "No tits on my own."
    pc "Then get a good look while they are here and think about them when you close your eyes."
    nate.name "Right..."
    if renpy.showing("shower"):
        show shower noman_front with dissolve
    elif renpy.showing("shower_back"):
        show shower_back noman_front with dissolve
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_offer_dp:
    $ npc_race_picker(drake,nate)
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    pc "Mmmm..."
    drake.name "You such a dirty girl you can't even deal with it alone?"
    if renpy.showing("shower"):
        show shower stand with dissolve
    elif renpy.showing("shower_back"):
        show shower_back man_front with dissolve
    nate.name "What have we here?"
    pc "Err..."
    if renpy.showing("shower"):
        show shower grope with dissolve
    elif renpy.showing("shower_back"):
        show shower_back grope with dissolve
    pc "Okaaay. We are carrying on are we?"
    nate.name "Dirty girl like you needs all the cleaning help she can get."
    pc "Ummm..."
    if renpy.showing("shower"):
        show shower finger with dissolve
    pc "Ah, straight there [nate.name]?"
    nate.name "Yup."
    if renpy.showing("shower_back"):
        show shower_back penis with dissolve
    pc "Ahh."
    pcm "This got very pokey and proddy very fast..."
    "The boys continue to rub me all over my body, two pairs of hands \"washing\" every unknown place of my body. Of course most of the focus is my breasts and between my legs..."
    "All the while I feel the hard cock poking behind me trying to wiggle it's way between my thighs and between my legs."
    pc "Ah fuck. You guys are all over me."
    nate.name "Just like in your dreams I bet. Sandwiched between two men?"
    pc "Errr..."
    pc "No. ♥"
    "I start to arch my back a bit, giving the cock poking at my behind a bit of room to move, but he doesn't actually move it between my legs and instead prods at my bum..."
    pc "Err, you got the right place there?"
    drake.name "Well, [nate.name] is in front, so I'll take the back."
    pc "Oh?"
    pcm "Ooooohh..."
    pcm "Fuck, they want to do *that*..."
    pcm "..."
    if renpy.showing("shower"):
        show shower hold with dissolve
    elif renpy.showing("shower_back"):
        show shower_back hold with dissolve
    pcm "Wow... Ok."
    "[drake.name]'s hands slide down to my hips and he starts to pull me back onto his cock. With it pressed right against my arsehole, there is only one place it is going to end up."
    "I arch my back more to give a better angle and he very slowly starts to strech me open and ever so slowly start to make his way inside me."
    $ player.sex_anal(drake)
    pc "Haaaahaaaa... ♥"
    "I focus only on the pleasure of the cock in my arse while [nate.name] in front of me rubs at my clit. I was already horny before but this is becoming something quite different."
    nate.name "Lift her leg up."
    drake.name "Hmmm."
    drake.name "Like this?"
    $ renpy.scene()
    $ npc_race_switch()
    show sb_dpstand banal back oh
    with dissolve
    nate.name "Ah yeah, like that."
    pc "Err, what for?"
    show sb_dpstand poke forward with dissolve
    pc "Oh fuck!"
    show sb_dpstand vag ag with dissolve
    $ player.sex_vag(nate)
    "[nate.name] wastes little time in lining up and penetrating me from the front. At this point I totally lose it, mind swimming in the pleasure of having their two cocks inside me."
    "I am not even sure I could tell how long they fucked me like this. With my mind lost in such raw sexual lust, I was mostly a ragdoll being held upright only because I was impaled in both holes."
    "They kept a good rhythm, sometimes both entering me and sliding out at the same time, so there was a moment of total, blissful fullness followed by total emptiness and a desire to be filled again."
    "Other times one would pull out just as the other is all the way in. Leaving my head to just loll around on my shoulders, not giving me a moment to catch my wits."
    "It wasn't until their motions became more erratic that my mind was able to awake from the paralysing pleasure, realising that they may well be coming to the end of their limits."
    "I just lent my weight onto [drake.name] who was behind me and just hoped I would be able to walk properly after this..."
    $ npc_race_switch()
    $ player.sex_cum(drake, "anal")
    drake.name "Aaah fucking hell yes!"
    drake.name "Ahhhhh."
    pc "UuuuUuuu..."
    drake.name "Ufffff..."
    $ npc_race_switch()
    show sb_dpstand bpoke with dissolve
    show sb_dpstand bnoman with dissolve
    nate.name "Ah fuck!"
    hide sb_dpstand
    show sb_blowjob worried face shock shower
    with dissolve
    "[nate.name] quickly pulls out of me and puts me straight on his knees, slapping his cock on my face as I look up at him with a dumb look on my face."
    $ player.sex_cum(nate, "face")
    show sb_blowjob closed
    "I am not even pulled out of it when [nate.name] cums all over my face..."
    nate.name "Ah fuck [name]. That was the best."
    show sb_blowjob poke with dissolve
    show sb_blowjob suck with dissolve
    pause 0.5
    show sb_blowjob poke shock with dissolve
    show sb_blowjob face with hpunch
    nate.name "Mmmm."
    nate.name "Meet you back outside."
    show sb_blowjob up with dissolve
    pc "Uhhh huuhhh..."
    show sb_blowjob noman with dissolve
    $ player.face_neutral()
    pcm "Fuck..."
    pcm "That was something..."
    pcm "Well, better get my arse up off the shower floor I suppose."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_mast:
    pcm "Hmmm... ♥"
    show sb_againstwall2 mast closed with dissolve
    pcm "Mmmmm..."
    call masturbate_fantasy_picker from _call_masturbate_fantasy_picker_1
    call expression rand_choice from _call_expression_8
    pc "Haaaaaa..."
    show sb_againstwall2 ag with dissolve
    $ player.sex_cum(nosex, "self")
    pc "Ahhh yes yes!"
    pc "..."
    $ player.face_neutral()
    pause 0.5
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_hj:
    show sb_handjob down nohand notop shower with dissolve
    pc "Hmm, what's this? Something standing to attention?"
    tempname.name "It tends to do that when a girl shakes her naked ass around it."
    pc "Oh? Better do something about it then."
    show sb_handjob ballrub with dissolve
    pc "Wonder what happens when I do this?"
    tempname.name "Ah fuck you tease?"
    show sb_handjob up with dissolve
    pc "What? Never!"
    show sb_handjob mast with dissolve
    tempname.name "Mmmmm..."
    pc "Like that?"
    tempname.name "Yeah."
    pc "How about..."
    jump school_field_soccer_play_end_shower_sex_bj

label school_field_soccer_play_end_shower_sex_bj:
    $ renpy.scene()
    show sb_blowjob up happy shower
    with dissolve
    show sb_blowjob face 1h with dissolve
    $ player.sex_oral(tempname)
    tempname.name "What are yo... Ah..."
    show sb_blowjob poke down tounge with dissolve
    tempname.name "Ooohh."
    show sb_blowjob swallow with dissolve
    show sb_blowjob suck with dissolve
    pc "Mmmmm."
    "Now that [tempname.name] realises what is going on, he rests is hands on my head and relaxes. Getting lost in the pleasure I am giving him with my mouth."
    show sb_blowjob 2h with dissolve
    tempname.name "Ah yes!"
    pc "*Mmmmff*"
    pc "*Hyuk* *Hyuk* *Hyuk*"
    "I wank him off with my hands as well as with my lips, but decide it's not just him who should be having fun."
    show sb_blowjob 0h with dissolve
    "So I take my hands off his cock and slip one between my legs, letting myself get off as well."
    pc "Mmmmm..."
    show sb_blowjob closed with dissolve
    "With no hands to keep rhythm, he takes my head in his hands and begins to face fuck me. He isn't too rough or deep so it feels nice. I close my eyes and start to get lost in the nice feeling."
    tempname.name "Ah fuck yes!"
    tempname.name "You're gonna make me cum!"
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        pc "Mmmff."
        tempname.name "Ah yes keep goingggg..."
        tempname.name "Ah yes!!"
        $ player.sex_cum(tempname, "mouth")
        tempname.name "Ah fuck yes!!!"
        show sb_blowjob up with dissolve
        tempname.name "Yesss!"
        tempname.name "Ah shit. That was good."
        show sb_blowjob poke ub with dissolve
        show sb_blowjob noman with dissolve
        show sb_blowjob frown with dissolve
        show sb_blowjob swallow with dissolve
        pc "Ahhhh."
        tempname.name "Nice, swallowed it all up?"
    elif randomnum == 2:
        show sb_blowjob poke swallow up with dissolve
        pc "Cun in ny noughh."
        show sb_blowjob down 2h with dissolve
        "I keep wanking him off while licking his cock, getting ready to catch his load in my mouth."
        $ player.sex_cum(tempname, "mouth")
        tempname.name "Ah fuck yes!!!"
        show sb_blowjob up with dissolve
        tempname.name "Yesss!"
        tempname.name "Ah shit. That was good."
        show sb_blowjob poke ub with dissolve
        show sb_blowjob noman with dissolve
        show sb_blowjob frown with dissolve
        show sb_blowjob swallow with dissolve
        pc "Ahhhh."
        tempname.name "Nice, swallowed it all up?"
    else:
        show sb_blowjob face swallow up 1h with dissolve
        "I lick the shaft of his cock while wanking him off with my hand, waiting for him to cum all over my face."
        $ player.sex_cum(tempname, "face")
        show sb_blowjob closed with dissolve
        tempname.name "Ah fuck yes!!!"
        tempname.name "Yesss!"
    show sb_blowjob suck closed 0h with dissolve
    "I scoop up his cum covered cock with my mouth before it starts to get soft and carry on sucking him while still getting myself off."
    tempname.name "Fuuuck. Haaa I am too sensitive..."
    pc "Mmmmmm..."
    tempname.name "Ah you dirty girl..."
    pc "MMMMmmmmmm!!!"
    $ player.sex_cum(nosex, "self")
    pc "Mmmmmmm..."
    show sb_blowjob neutral up face 1h with dissolve
    pc "*Phew*"
    tempname.name "Ahh. Have fun?"
    show sb_blowjob laugh
    pc "I did. ♥"
    tempname.name "Good."
    show sb_blowjob neutral
    pc "Now go away, I need to clean up my face."
    tempname.name "Oh it's like that is it?"
    pc "Heh, yes it is."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_vag:
    show sb_againstwall2 shower pokevag with dissolve
    "I arch my back against him and press back on his cock, allowing him to poke me pretty deep. He gets the message where to fuck me and starts to build a bit of a rhythm with his poking."
    if player.vvirgin:
        "It doesn't take long for his poking thrusts to be full on penetrative thrusts and I am losing my virginity while being fucked against the shower wall."
    else:
        "It doesn't take long for his poking thrusts to be full on penetrative thrusts and I am being fucked against the shower wall."
    $ player.sex_vag(tempname)
    show sb_againstwall2 insidevag closed ag worried with dissolve
    pc "Ahh fuck! ♥"
    tempname.name "Mmmmm. So warm."
    "I get lost in the pleasure between my legs and even manage to forget the other two are probably watching me get fucked by [tempname.name]."
    "I don't care though and press back against his cock, making sure his thrusts hit me as deep as they possibly can."
    pc "Haaa fuck yes!"
    $ player.spank()
    pc "Nnng."
    $ player.spank()
    pc "Haaaaa..."
    "He grips his hands into my arse to get a better hold of me so he can pull me down on his cock and much as possible, with each thrust ending in a loud *Slap* as my cheeks hit against his hips."
    "His thrusts start getting much more aggressive and I hear him groaning behind me. He is clearly close."
    $ player.sex_cum_location_offer("Keep quiet", "Make sure to pull out!", 0)
    if player.want_pullout:
        jump school_field_soccer_play_end_shower_sex_vag_pullout
    else:
        jump school_field_soccer_play_end_shower_sex_vag_cumin

label school_field_soccer_play_end_shower_sex_vag_cumin:
    "He continues erratically thrusting inside me until his fingers grip me almost enough to hurt, and I can feel it..."
    pc "Oh fuck yes keep going. Don't stop!"
    "He slams into me one last time and stays there as deep inside me as he possibly can, and I feel his twitching inside me."
    $ player.sex_cum(tempname, "inside")
    tempname.name "Ah fuck yes! Fuuuck!"
    pc "Oh yes! Fuck so good!"
    pc "Haaaaa ♥"
    show sb_againstwall2 open happy with dissolve
    $ player.face_neutral()
    tempname.name "Mmmmmm fuck that was nice."
    pc "Mmmmm."
    show sb_againstwall2 pokevag with dissolve
    show sb_againstwall2 noman with dissolve
    "He slowly slides his cock out of me, and I feel it being followed by a trickle of cum leaking out of me and down my leg before getting washed away in the shower."
    pc "Mmmm, you left me more dirty than I was when you offered to clean me."
    tempname.name "Consider it a present."
    if not player.has_perk(perk_preg_want):
        pc "Just not a 3 seasons present."
    $ player.spank()
    pc "Oh!"
    tempname.name "I'll get a beer ready for you."
    pc "Mmm."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_vag_pullout:
    pc "Pullout!"
    show sb_againstwall2 pokevaghand with dissolve
    show sb_againstwall2 cum mast with dissolve
    "I start to rub between my legs as he furiously wanks himself over my bum, both of us ready to cum at any moment."
    $ player.spank()
    tempname.name "Fuck you bad girl!"
    pc "I am ♥"
    tempname.name "Ahhh!"
    "I feel him rub his cock between his cheeks and groan as he cums all over my bum, it is enough to also set me off and I can feel it building inside me as well."
    $ player.sex_cum(tempname, "pullout")
    tempname.name "Ah fuck yes! Fuuuck!"
    pc "Oh yes! Fuck so good!"
    pc "Haaaaa ♥"
    show sb_againstwall2 open happy wall with dissolve
    $ player.face_neutral()
    tempname.name "Mmmmmm fuck that was nice."
    pc "Mmmmm."
    show sb_againstwall2 pokevaghand with dissolve
    "I feel him rubbing his cock between my slit to leave the last drops of himself on me before finishing up."
    show sb_againstwall2 noman with dissolve
    pc "Mmmm, you left me more dirty than I was when you offered to clean me."
    tempname.name "Consider it a present."
    $ player.spank()
    pc "Oh!"
    tempname.name "I'll get a beer ready for you."
    pc "Mmm."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_anal:
    pc "Hmm, better my bum."
    tempname.name "Really?"
    if player.has_perk(perk_preg_notwant) and not player.preg_knows:
        pc "Don't want any accidents happening."
    else:
        pc "Yup. I like it there."
    show sb_againstwall2 shower pokevaghand with dissolve
    show sb_againstwall2 shower pokeasshand with dissolve
    tempname.name "Sure."
    show sb_againstwall2 pokeass with dissolve
    pc "Ohh!"
    tempname.name "Ready?"
    pc "Mmmmm. ♥"
    "I feel him ease his way into my arse and feel myself stretching as he fills me up. He takes gentle thrusts with each one getting deeper and deeper until I can feel his body pressing against my ass."
    $ player.sex_anal(tempname)
    show sb_againstwall2 insideass happy wink worried with dissolve
    pc "Ooooh fuck!"
    pc "Yes, keep going!"
    $ player.spank()
    pc "Mmmm."
    "I press against him in time with his thrusts making sure I take him as deep as possible in my arse, enjoying the feeling of him filling me up."
    "His hands grip into my arse as he squeezes it to pull himself deeper into me and I arch my back giving him the perfect angle."
    tempname.name "Ah fuck yes you dirty bitch. Take it in your arse like a good girl!"
    show sb_againstwall2 ag closed with dissolve
    pc "Fuck yes, put it in me!"
    tempname.name "Ahhh yes!"
    $ player.sex_cum(tempname, "anal")
    tempname.name "Haaaaaa!"
    pc "OoOoo!"
    pc "Ahhh I feel it!"
    tempname.name "Nnnnngg."
    show sb_againstwall2 open straight neutral with dissolve
    $ player.face_neutral()
    pc "Phheeewww."
    pc "That was nice."
    $ player.spank()
    pc "Mmm."
    show sb_againstwall2 pokeass with dissolve
    show sb_againstwall2 noman with dissolve
    "[tempname.name] slides his cock out of me and following it I feel a trickle of his cum leak out of me and run down between my legs before getting washed away in the running water."
    $ player.shower()
    tempname.name "It was great. I'll have a beer ready for you while you clean up."
    pc "Mmm, see you out there."
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_sex_dp:
    "Double penetration in the shower"
    jump school_field_soccer_play_end_shower_end

label school_field_soccer_play_end_shower_end:

    if not (renpy.showing("shower") or renpy.showing("shower_back")):
        $ relax(15)
        $ renpy.scene()
        $ renpy.show(renpy.random.choice(["shower", "shower_back"]))
        with dissolve
    $ relax(5)
    $ player.shower()
    "I finish up my shower and start to head out."
    $ renpy.scene()
    $ renpy.with_statement(dissolve)
    $ shower_scene_end()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
