label haven_room1_peek_intro:
    $ add_to_list(loc_haven_room1.list, "found_peephole")
    $ player.face_surprised()
    pcm "Some kind of light coming out of the wall here..."
    show haven_peeping at right1 with dissolve
    $ player.face_worried()
    pcm "What the hell! Looks right into the showers."
    if player.has_perk(perk_exhibitionist):
        $ player.face_happy()
        pcm "Oh wow. Someone's been spying on us while we shower..."
        $ player.add_desire_random(20)
        pcm "Wonder if I have been watched?"
        pcm "Mmmm."
        pcm "Wonder if I should let the girls know this is here. Doubt they will enjoy being looked at like me."
    else:
        $ player.face_angry()
        pcm "Fuck, some dirty perv probably made this to spy on the girls while they are having a shower."
        pcm "I should probably let the girls know this is here..."
    $ player.face_neutral()
    pcm "..."
    pcm "Although if some pervert is able to spy on the girls and have a wank from here while not getting caught, it would be a good place for me to spy on people to try and listen for info about [ant.name]."
    pcm "Hmmmm..."
    hide haven_peeping with dissolve
    pcm "Maybe I will keep this to myself. Better make sure not to get caught though."
    pcm "It's a fair bet that whoever made this is perving on the girls so coming here while the girls are showering will probably get me caught."
    $ player.face_shy()
    pcm "That leaves me looking at all the naked men..."
    pcm "..."
    jump travel

label haven_room1_peek:
    if not "found_peephole" in loc_haven_room1.list:
        jump haven_room1_peek_intro

    elif haven_time_empty():
        show haven_peeping at right1 with dissolve
        pcm "Hmm, showers are empty right now so spying is pointless. I should come back when they have more people in them."
        hide haven_peeping with dissolve
        jump travel
    else:

        show haven_peeping at right1 with dissolve
        $ dialouge = WeightedChoice([
        ("Ok, let's hear what you have to say.", 1),
        ("Hopefully I can overhear something about this doctor.", 1),
        ("Let's listen and see if I can hear anything.", 1),
        ("Hopefully I can hear something of interest.", 1),
        ("Ignore the naked bodies and try to hear something interesting.", If (player.desire > 80,1,0)),
        ("Okay let's have a look. No harm in enjoying the view while eavesdropping.", If (player.desire > 80,1,0)),
        ("Got anything good to show me?", If (player.desire > 80,1,0)),
        ("Let's see if I can hear anything.", 1),
        ])
        pcm "[dialouge]"
        jump haven_room1_peek_setter

label haven_room1_peek_setter:
    if haven_time_empty():
        pcm "Showers are empty right now so spying is pointless. I should come back when they have more people in them."
        jump travel

    if haven_intel_chance():
        jump expression WeightedChoice([
        ("haven_intel_11", If(haven_time_safe() or haven_time_normal(), 1, 0)),
        ("haven_intel_9", If(haven_time_normal() or haven_time_danger(), 1, 0)),
        ("haven_intel_10", If(haven_time_normal() or haven_time_danger(), 1, 0)),
        ])
    else:

        jump expression WeightedChoice([
        ("haven_room1_listen_genericinfo_girls", If(haven_time_safe() or haven_time_normal(), 1, 0)),
        ("haven_room1_listen_genericinfo", If(haven_time_normal() or haven_time_danger(), 1, 0)),
        ])

label haven_room1_listen_genericinfo_girls:
    $ dialouge = WeightedChoice([
    ("The conversations are just muffled noise. I can't make out anything of interest.", 1),
    ("Hmm, seems like these girls are lovers of sorts. But other than their private stuff there isn't really anything of interest.", 1),
    ("These girls giggling away. Do they really think other people don't notice their water splashing and tickling are just shy excuses to grope each other?", 1),
    ("Far too muffled and I can't make anything out.", 1),
    ("Hmm, the girls aren't really speaking to each other. Just heading in to shower then leaving.", 1),
    ("Nothing at all of any real interest. Just general topics about the work the girls are doing. I thought a lot more of them were whores but seems the majority are gamines.", 1),
    ("I can't make out much over the sound of the showers and the wall being between me and the conversation.", 1),
    ("I'm not able to pick out anything of interest.", 1),
    ])
    pcm "[dialouge]"
    jump haven_room1_listen_end

label haven_room1_listen_genericinfo:
    $ dialouge = WeightedChoice([
    ("The guys are mostly talking about the work they do. Nothing of real interest to me.", 1),
    ("Can't really hear anything. It's all muffled.", 1),
    ("They are just laughing and joking about. Nothing of any real substance.", 1),
    ("Just talking about which one of the girls they want to fuck most.", 1),
    ("Talking about jobs they have done and people they have cheated. Not much of interest.", 1),
    ("Mostly quiet in there right now. Lots of people but not many are having conversations.", 1),
    ("Hmm, mostly muffled and I can't make out what they are talking about.", 1),
    ("Just general chit chat. Nothing of interest to me.", 1),
    ("Ah, I was too busy watching and not really listening.", If (player.desire > 80,1,0)),
    ("Hmm, I wonder how much they would punish me if they caught me spying on them.", If (player.desire > 80,1,0)),
    ])
    pcm "[dialouge]"
    jump haven_room1_listen_end

label haven_room1_listen_end:
    $ player.add_desire_random(5)
    $ working(20)
    $ haven_room1_join_chance()
    $ dialouge = WeightedChoice([
    ("Should probably leave for now.", 1),
    ("Ok, let's head out before I am caught hanging around", 1),
    ("Ok, that's enough of staring at a room full of naked people.", 1),
    ("Right, that's enough for now.", 1),
    ])
    pcm "[dialouge]"
    $ shower_listen_masturbate()
    hide haven_peeping with dissolve
    jump travel_arrival

label haven_room1_listen_join:
    if renpy.random.randint(1, 4) == 1:
        jump haven_room1_listen_punish

    if not havenpeeper.has_met:
        $ havenpeeper.dict["joined_room1"] = 1
        show haven_peeping catch with dissolve
        havenpeeper.name "Didn't expect someone else would be having a look into the showers."
        show haven_peeping talk mouth_shocked brow_worried eye_man with dissolve
        pc "I... Err, wasn't... I was... There was a hole and..."
        pcm "Fuck!"
        havenpeeper.name "No worries. I'll come back later to enjoy the sights. You have fun now and clean up after yourself."
        havenpeeper.name "Actually, don't clean up."
        show haven_peeping brow_conf mouth_open
        pc "Err. Ok?"
        havenpeeper.name "See ya round."
        show haven_peeping noman eye_penis with dissolve
        pcm "Fuck, caught red handed looking in the showers. Luckily it was just a pervert and not someone more upstanding."
        show haven_peeping peep with dissolve
        pcm "..."
        pcm "I should probably finish up."
        $ working(20)
        hide haven_peeping with dissolve
        jump travel

    elif havenpeeper.dict["joined_room1"] == 1:
        $ havenpeeper.dict["joined_room1"] += 1
        show haven_peeping catch with dissolve
        pcm "..."
        pcm "C'mon, say something interesting..."
        pcm "..."
        show haven_peeping talk mouth_shocked brow_worried eye_man with dissolve
        havenpeeper.name "Only me."
        show haven_peeping mouth_flat brow_straight with dissolve
        pc "Frightened the life out of me sneaking up like that."
        havenpeeper.name "Didn't want to spoil your fun."
        pc "Then shouldn't you have left?"
        havenpeeper.name "Na, I come here to spy on hot girls. You can look at all the guys you want and I'll be content with looking at my fellow pervert."
        pc "Fellow pervert? I..."
        havenpeeper.name "Second time I have seen you here. You don't come back unless you like what you see."
        pc "I..."
        pcm "Fuck, can't tell him why I am really here."
        pc "If you say so..."
        show haven_peeping peep with dissolve
        pcm "Just keep ignoring him and maybe he will go away."
        pcm "..."
        pcm "It's hard to make out what they are saying most of the time."
        show haven_peeping noman with dissolve
        pcm "Someone talk about [ant.name] would you."
        pcm "..."
        if haven_time_safe():
            pcm "Starting to feel like a real pervert spying on all he naked girls."
        else:
            pcm "Starting to feel like a real pervert. Spying on all these naked men with their cocks swinging around..."
            $ player.add_desire_random(10)
        show haven_peeping talk eye_back mouth_flat brow_straight with dissolve
        pcm "Ah, he did eventually leave."
        show haven_peeping peep with dissolve
        pcm "..."
        pcm "Never mind. I should stop for now."
        pcm "Not really hearing much of interest anyway."

        $ shower_listen_masturbate()

        $ working(20)
        hide haven_peeping with dissolve
        jump travel

    elif havenpeeper.dict["joined_room1"] == 2:
        $ havenpeeper.dict["joined_room1"] += 1
        show haven_peeping catch with dissolve
        pcm "..."
        if haven_time_safe():
            pcm "Come on girls, say something. I didn't come here to stare at your naked arses."
        else:
            pcm "Come on guys, say something. I didn't come here to see you swinging your dicks around."
            $ player.add_desire_random(10)
        havenpeeper.name "Enjoying the view?"
        show haven_peeping talk mouth_shocked brow_worried eye_man with dissolve
        pc "AH!"
        show haven_peeping mouth_flat brow_straight with dissolve
        pc "You need to stop sneaking up on me. Not sure my heart would last another jump like that."
        havenpeeper.name "And miss your reaction? Na."
        havenpeeper.name "So, see anything you like in there?"
        show haven_peeping peep with dissolve
        if haven_time_safe():
            pc "Mostly girls in there with a few guys. You would probably enjoy the view better."
            havenpeeper.name "I am enjoying the view just fine."
        elif haven_time_empty():
            pc "The place is empty so not much to see right now."
            havenpeeper.name "Speak for yourself. My view is already interesting."
        else:
            pc "Packed full of naked guys. Not really a view you would enjoy."
            havenpeeper.name "But one you like? No worries, my view is already pretty nice."
        pcm "Pervert."
        pcm "Fuck, like I am one to talk. It's me looking through the hole..."
        show haven_peeping mast with dissolve
        pcm "Ah well, if I ignore him maybe he will go away again like last time."
        pcm "Although it is his hole, maybe I should be the one leaving."
        show haven_peeping talk eye_man mouth_flat brow_straight with dissolve
        pc "Is it..."
        show haven_peeping eye_penis mouth_open brow_conf with dissolve
        pc "Err."
        show haven_peeping eye_man with dissolve
        pc "What are you doing?"
        havenpeeper.name "That's obvious aint it?"
        pc "Ok, *Why* are you doing that? Put it away you pervert."
        havenpeeper.name "I came here to spy on sexy girls. You're usin the hole but look good enough. Why waste a trip?"
        pc "..."
        if player.check_sex_agree(2):
            pc "Whatever, just don't be pointing that thing at my face. I don't want to have to go in there and wash you off me."
            havenpeeper.name "Ok. Would be nice to spy on you washing up though."
            show haven_peeping peep with dissolve
            pc "I bet it would."
            show haven_peeping grope_ass with dissolve
            pcm "Now he's behind me. *Sigh*"
            pcm "Whatever, ignore him and try to listen."
            pcm "..."
            $ player.add_desire_random(10)
            pcm "Not getting much info out of anyone in there now."
            if not haven_time_safe():
                pcm "Hard to focus though with all those cocks swinging around while this perv gropes my arse."
                $ player.add_desire_random(10)
            else:
                pcm "Hard to focus though with him groping my arse. Shame the view isn't better."
            pcm "..."
            pcm "Maybe I could... "
            pcm "...Enjoy myself here?"
            if player.check_sex_agree(3):
                pcm "Why not?"
                show haven_peeping talk eye_back mouth_happy brow_straight with dissolve
                pc "Enjoying yourself back there?"
                havenpeeper.name "Ahhh. Such a sexy bum. And this tat you have... Mmmm."
                pc "Mmm, like it do you?"
                havenpeeper.name "Yes. Would fuck it til you scream."
                pc "Well, something is already in there so you can't. But you can keep at it and let me feel you spray your load all over my arse."
                havenpeeper.name "Already in there? Dirty slut! I want to see."
                pc "No one's stopping you."

                show haven_peeping shorts_down with dissolve
                $ c.bottom = 0
                $ c.pants = 0
                havenpeeper.name "Damn, would love to fuck that arse."
                pc "Another time. You should see the size of it filling me up."
                havenpeeper.name "Damn girl, talk like that and I'm not gonna last long."
                show haven_peeping grope_tit with dissolve
                pc "It's as big as my fist."
                pc "I can feel it whenever I walk. Totally filing me up."
                havenpeeper.name "Fuck!"
                if player.check_sex_agree(4):
                    show haven_peeping poke_out with dissolve
                    $ c.top = 0
                    $ c.pants = 0
                    pc "Having my arse filled so much makes me constantly horny. Especially with these tight shorts pressing against the plug."
                    pc "And you perverts constantly looking at me when I walk around. What they want to do to me alone in a room."
                    pc "They want to put their big cocks in me and fuck me like a dirty whore."
                    havenpeeper.name "Fuck you are a dirty whore that needs to be fucked."
                    $ player.sex_vag(havenpeeper, main_quest_05)
                    show haven_peeping poke_in enjoy with dissolve
                    pc "Oooohhhhh... Fuck yes. It's about time you stuck it in me! ♥ ♥"
                    havenpeeper.name "Ah you dirty whore!"
                    pc "Yes, fuck me!"
                    havenpeeper.name "I'm not gonna last long."
                    show haven_peeping arm_mast with dissolve
                    "I start masturbating to bring myself to climax quicker. His hard cock sliding in and out of me keeps a steady pace, but I know he won't last long."
                    show haven_peeping talk eye_back mouth_open brow_straight with dissolve
                    pc "Keep going. Keep... Ugh! Going..."
                    havenpeeper.name "Haaaa fuck!!"
                    pc "Keep fucking!"
                    show haven_peeping enjoy
                    $ player.sex_cum(havenpeeper, "inside", main_quest_05)
                    havenpeeper.name "Yesssss! Haaaaaaa."
                    pc "Ah fuck yes. Give it to me!"
                    pc "Haahaa..."
                    show haven_peeping talk eye_back mouth_flat brow_straight arm_wall shorts_down with dissolve
                    pc "Better than beating off to whores in the shower?"
                    havenpeeper.name "Mmmm yes. A whore on my cock beats my hand any day."
                    show haven_peeping poke_out with dissolve
                    havenpeeper.name "Haa. That plug in your arse makes your pussy so tight. Can feel it in you even when fucking the other hole."
                    pc "Mmmm, told you it was big."
                    havenpeeper.name "Ah well. I'm gonna go before someone hears us and discovers the hole."
                    pc "Mmmm."
                    show haven_peeping noman top_down eye_penis with dissolve
                    "He slides is cock out of my dripping pussy, pulls his trousers up and leaves the room."
                    pcm "Maybe I should also go before someone discovers my hole and I end up fucked again."
                    $ shower_listen_masturbate()
                    pcm "Up we get."
                    hide haven_peeping with dissolve
                    $ pc_dress()
                    $ working(20)
                    jump travel
                else:

                    pc "Having my arse filled so much makes me constantly horny. Especially with these tight shorts pressing against the plug."
                    pc "And you perverts constantly looking at me when I walk around. What they want to do to me alone in a room."
                    pc "They want to put their big cocks in me and fuck me like a dirty whore."
                    show haven_peeping cum_ass
                    $ player.sex_cum(nosex, "ass", main_quest_05)
                    havenpeeper.name "Haaaa fuck!!"
                    pc "Heh, have fun?"
                    havenpeeper.name "Haaaa..."
                    havenpeeper.name "Sure did, thanks to you."
                    pc "Glad to be of service."
                    havenpeeper.name "Mmmm."
                    havenpeeper.name "I'll leave you to your own perving now."
                    pc "Ok."
                    show haven_peeping noman eye_man with dissolve
                    "I watch him as he gets up to put his trousers on and then leaves the room"
                    show haven_peeping peep with dissolve
                    pcm "..."
                    pcm "Although not much to hear really. Maybe I should just get going before someone else sees me here with my arse hanging out."
                    $ shower_listen_masturbate()
                    pc "*Sigh* My bum is all wet now..."
                    hide haven_peeping with dissolve
                    $ pc_dress()
                    $ working(20)
                    jump travel
            else:

                pcm "No, not with that perv. I should just focus on this."
                show haven_peeping grope_tit with dissolve
                pcm "Focus, focus. Ignore the cock behind you and listen to them."
                if not (haven_time_safe() or haven_time_empty()):
                    pcm "Focus on the naked men... Washing their naked bodies..."
                    pcm "Fuck."
                    $ player.add_desire_random(10)
                havenpeeper.name "Haaa."
                pcm "Sounds like he's running out of stamina."
                havenpeeper.name "Ahhhhh."
                show haven_peeping cum_ass
                $ player.sex_cum(nosex, "ass", main_quest_05)
                havenpeeper.name "Ahhh yes!"
                havenpeeper.name "Haaaaa. Such a sexy ass."
                pc "Glad you like it."
                havenpeeper.name "Mmmm."
                havenpeeper.name "I'll leave you to your own perving now."
                pc "Ok."
                show haven_peeping talk brow_straight mouth_flat noman eye_man with dissolve
                "I watch him as he gets up to put his trousers on and then leaves the room"
                show haven_peeping peep with dissolve
                pcm "..."
                pcm "Although not much to hear really. Maybe I should just get going before someone else sees me here with my arse hanging out."
                $ shower_listen_masturbate()
                pc "*Sigh* My bum is all wet now..."
                hide haven_peeping with dissolve
                $ pc_dress()
                $ working(20)
                jump travel
        else:

            pc "Ugh, whatever..."
            show haven_peeping peep with dissolve
            pcm "Pervert. Can't even spy in the showers in peace."
            if haven_time_safe():
                pcm "Maybe I should just leave. Plenty of girls in the shower for him to beat off to."
            else:
                pcm "Maybe I should just leave and let him have the hole. Mostly men though so not much for him to beat off to."
            havenpeeper.name "Ung..."
            pcm "Not like I am getting much information right now anyway."
            pcm "Ok, let's leave him to it."
            show haven_peeping talk eye_man mouth_flat brow_straight with dissolve
            pcm "Hey, you want to look through the hole?"
            havenpeeper.name "Ung. Cramping your style am I."
            pc "Something like that."
            havenpeeper.name "Ahhh, no wait a bit."
            pc "Errr."
            show haven_peeping eye_penis mouth_shocked with dissolve
            pc "Wait! Fuck no..."
            show haven_peeping cum_face mouth_flat eye_closed
            $ player.sex_cum(nosex, "face", main_quest_05)
            havenpeeper.name "Ahhhh yes! Haaaaaa..."
            pc "..."
            show haven_peeping eye_man with dissolve
            pc "Fuck... Couldn't you have pointed that somewhere else?"
            havenpeeper.name "And miss the chance to cover your pretty face. No chance."
            pc "..."
            pc "Now I have to go and shower to wash this off."
            havenpeeper.name "Have fun. I'll have another round when I see you in the shower."
            pc "Pervert."
            hide haven_peeping with dissolve
            pc "*Sigh*"
            $ working(20)
            $ walk(loc_haven_hallway_1f)
            pause 0.5
            $ walk(loc_haven_shower)
            pc "That pervert will definitely be jacking off to me when I go in there, but not much choice."
            jump haven_shower_stall_arrival

    elif havenpeeper.dict["joined_room1"] == 3:
        $ havenpeeper.dict["joined_room1"] += 1
        pcm "Am I just being a pervert at this point? I know I can get info off these people by listening, but is that why I come here so often?"
        pcm "Am I like that guy who make the hole? Coming here just to spy on naked people?"
        pcm "Ah so what? This is nice. It's like two birds with one stone. I get to enjoy all these naked people while trying to find info. Win win."
        pcm "Not getting much info right now anyway so just enjoy the show."
        pcm "..."
        if player.check_sex_agree(3):
            menu:
                "Put my hands in my pants":
                    $ working(20)
                    jump haven_room1_listen_masturbate
                "Get up and leave":

                    pcm "Shouldn't do something so risky."
                    hide haven_peeping with dissolve
                    $ working(20)
                    jump travel
        else:
            hide haven_peeping with dissolve
            $ working(20)
            jump travel

    elif havenpeeper.dict["joined_room1"] == 4:
        if not (haven_time_danger() or haven_time_normal()):
            jump haven_room1_peek_setter

        show haven_peeping catch with dissolve
        $ havenpeeper.dict["joined_room1"] += 1
        hav "See anything interesting?"
        pc "Shoo!"
        hav "I take that as a yes."
        pc "Place is packed. Stop spoiling the mood."
        show haven_peeping noman with dissolve
        pc "..."
        show haven_peeping talk eye_back mouth_flat brow_straight with dissolve
        pcm "He actually left."
        show haven_peeping peep with dissolve
        pcm "Ok, back to watching..."
        pcm "..."
        pcm "Huh? What the..."
        "Through the hole I see a naked man up close. He gets closer to the hole, blocking my entire view to the showers with is lower body and exposed cock."
        "He then takes his cock in his hand and starts wiggling it in the direction of the hole, lets go of it then gives the direction of the hole a thumbs up."
        pcm "Damn pervert. Gone and went to the showers to wave his cock at me."
        pcm "No point in looking any more with him blocking the view."
        if player.check_sex_agree(3):
            pcm "Hmmm..."
            pcm "..."
            menu:
                "Maybe I can have some fun?":
                    $ working(20)
                    jump haven_room1_listen_masturbate
                "I'd better leave":
                    $ NullAction()
        $ working(20)
        hide haven_peeping with dissolve
        jump travel

    elif havenpeeper.dict["joined_room1"] == 5:
        $ havenpeeper.dict["joined_room1"] += 1
        show haven_peeping grope_ass with dissolve
        show haven_peeping talk brow_worried mouth_shocked eye_back with dissolve
        pc "!!!!"
        pc "Fucking fuck! You almost gave me a heart attack!"
        show haven_peeping brow_straight mouth_flat
        pc "Sneaking up like that. Bastard!"
        show haven_peeping grope_tit with dissolve
        havenpeeper.name "Calm down girl. Didn't mean to scare you."
        pc "Idiot."
        pc "And who told you that you could come here and start feeling up my tits?"
        havenpeeper.name "I'm sure a dirty girl like you doesn't mind. You are looking in there at all the man meat so I have come to give you a close up."
        show haven_peeping peep with dissolve
        pc "*Sigh* Who told you I wanted a close up? I am happy here without the risk of being impaled."
        havenpeeper.name "I have been wondering about that. Most of you girls are whores or selling your body in some way. No shortage of cocks in your lives. So why would someone come and spy through a hole?"
        havenpeeper.name "I am wondering if there is something else you are after. Besides the nice view of course."
        pcm "..."
        havenpeeper.name "Thought so. So... What you looking for in that hole there?"
        pcm "..."
        havenpeeper.name "I might be able to help out. Been around these parts a while."
        pcm "Hmm, that's true. A pervert like him would keep an eye on a lot of the goings on around here. Could be worth asking him what he knows."
        pcm "Bastard will make me pay for it no doubt."
        menu:
            "Ask him what he knows":
                jump haven_intel_12
            "Don't bother, I don't care what he knows":

                pc "Sorry mate, but I'm not interested in paying the price you will ask for."
                if havenpeeper.vsex > 0:
                    havenpeeper.name "I already fucked you once and you weren't complaining. You are after something and so am I so just go with it."
                    pcm "Does have a point. Already let him fuck me and it was kinda nice."
                    if havenpeeper.vvirgin == True:
                        pcm "He even took my virginity while he was at it. Though I will never let him know that he did."
                    menu:
                        "Tell me what you know.":
                            jump haven_intel_12
                        "No chance, fucking you was a mistake":
                            pc "I spent too long looking at these naked men and you caught me at a bad time."
                            havenpeeper.name "Suit yourself. I aint gonna force you. Good luck with whatever."
                            show haven_peeping talk noman eye_penis brow_straight mouth_flat with dissolve
                            pcm "He left..."
                            pcm "I should leave too."
                            $ working(20)
                            hide haven_peeping with dissolve
                            jump travel


                elif havenpeeper.naughty > 0:
                    havenpeeper.name "You let me beat off to your sexy body and cum all over you, but now you are backing off?"
                    pc "And you gonna be satisfied with that again?"
                    havenpeeper.name "No, but it's not like you haven't been fucked for money before. So why not fuck for something else you want."
                    if player.sold:
                        pcm "I have never fucked for money..."
                    pcm "..."
                    pcm "I need to find out about [ant.name] and my search isn't going so well."
                    menu:
                        "Tell me what you know.":
                            jump haven_intel_12
                        "No chance, I didn't ask you do cum over me":
                            pc "I spent too long looking at these naked men and you caught me at a bad time."
                            havenpeeper.name "Suit yourself. I aint gonna force you. Good luck with whatever."
                            show haven_peeping talk noman eye_penis brow_straight mouth_flat with dissolve
                            pcm "He left..."
                            pcm "I should leave too."
                            $ working(20)
                            hide haven_peeping with dissolve
                            jump travel
                else:
                    havenpeeper.name "Suit yourself. I aint gonna force you. Good luck with whatever."
                    show haven_peeping noman talk brow_worried mouth_flat eye_man with dissolve
                    menu:
                        "Wait!":

                            hav "So?"
                            pc "..."
                            pc "Ok..."
                            havenpeeper.name "Mmmm"
                            show haven_peeping grope_ass eye_back with dissolve
                            havenpeeper.name "I'll make sure you enjoy yourself too."
                            jump haven_intel_12
                        "Let him go":
                            pcm "He left..."
                            pcm "I should leave too."
                            $ working(20)
                            hide haven_peeping with dissolve
                            jump travel
    else:

        jump haven_room1_listen_repeatable_choice

label haven_room1_listen_repeatable_choice:
    show haven_peeping catch with dissolve
    $ dialouge = WeightedChoice([
    ("How is my favourite pervert doing?", 1),
    ("Not surprised to see you in here.", 1),
    ("Not sure if I prefer coming here and seeing this place empty or occupied anymore.", 1),
    ("Such a nice sight coming here and seeing your arse bent over looking through the hole.", 1),
    ("Coming here and seeing that nice smooth ass really makes my day.", 1),
    ("How is my favourite little fuck toy doing?", If (havenpeeper.vsex > 0,1,0)),
    ])
    havenpeeper.name "[dialouge]"
    show haven_peeping talk eye_man mouth_flat brow_straight with dissolve
    pc "..."
    if not player.check_sex_agree(4):
        menu:
            "Not really in the mood right now.":
                pc "Sorry mate, but not really into having fun with you right now."
                if player.check_sex_agree(3):
                    havenpeeper.name "Yeah sure. We will see."
                    jump haven_room1_listen_repeatable
                else:
                    havenpeeper.name "No? Shame. Thought I would be having fun with my fellow little pervert"
                    $ working(20)
                    pcm "Better get out of here before he tempts me to stay."
                    hide haven_peeping with dissolve
                    $ walk(loc_haven_hallway_1f)
                    jump travel

                hav "Thats a shame. Well whatever, I will come back later."
                show haven_peeping noman with dissolve
                jump haven_room1_peek_setter
            "Don't say anything":

                $ NullAction()

    jump haven_room1_listen_repeatable

label haven_room1_listen_repeatable:
    show haven_peeping mast eye_penis with dissolve
    $ dialouge = WeightedChoice([
    ("I'm going to enjoy this.", 1),
    ("My cock on your sexy arse is easily the highlight of my day.", 1),
    ("Seeing your arse poking out like that makes me hard every time.", 1),
    ("Why not spend your nights with me and we can have a lot of fun.", 1),
    ("I am looking forward to eventually fucking you.", If (not havenpeeper.vsex,1,0)),
    ("You should join me in bed at night and I can fuck you all night.", If (havenpeeper.vsex,1,0)),
    ])
    havenpeeper.name "[dialouge]"
    $ dialouge = WeightedChoice([
    ("He starts stroking his cock while his eyes rove all over my body.", 1),
    ("He strokes his hard cock while eyeing my ass.", 1),
    ("He stands there masturbating while looking me all over.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("How has some shitty person like you got such a huge cock? And what do you think you're doing with it?", 1),
    ("And what do you plan to do with that thing in my face?", 1),
    ("And what do you plan to do with that thing?", 1),
    ("Planning to try and put that thing in me again?", If (havenpeeper.vsex > 0,1,0)),
    ("Planning to try putting a baby in me again?", If (player.has_perk(perk_preg_want) == True and havenpeeper.vsex > 0,1,0)),
    ])
    pc "[dialouge]"
    show haven_peeping eye_man
    havenpeeper.name "Up to you? Where do you want my cock?"
    menu:
        "Not right now, sorry, not in the mood.":
            if player.check_sex_agree(1, notif=False):
                hav "Yeah right."
                jump haven_room1_listen_repeatable_mast
            else:
                hav "No? Shame. Thought I would be having fun with my fellow little pervert"
                $ working(20)
                pcm "Better get out of here before he tempts me to stay."
                hide haven_peeping with dissolve
                $ walk(loc_haven_hallway_1f)
                jump travel

        "Just stay like that stroking yourself" if player.check_sex_agree(3,notif=False):
            jump expression renpy.random.choice(["haven_room1_listen_repeatable_mast", "haven_room1_listen_repeatable_blow"])

        "Get behind me and touch my ass" if player.check_sex_agree(4,notif=False):
            jump haven_room1_listen_repeatable_grope

        "Take my shorts off and fuck me" if player.check_sex_agree(5,notif=False):
            jump haven_room1_listen_repeatable_sex

label haven_room1_listen_repeatable_mast:
    $ dialouge = WeightedChoice([
    ("No problem. I can use you as my porn.", 1),
    ("Want me all over your face do you?", 1),
    ("Mmmm ok. I can wank over your sexy face.", 1),
    ("Like looking at me stroke it?", 1),
    ])
    havenpeeper.name "[dialouge]"
    show haven_peeping eye_penis
    pc "Mmmmm."
    "I kneel there intently watching his huge cock as he strokes it while looking at my body."
    "I feel excitement knowing that he is using me as his own personal porn and wonder what he is thinking about doing to my body."
    havenpeeper.name "Ughhhh."
    show haven_peeping mouth_happy eye_man
    pc "Getting close?"
    havenpeeper.name "Huuuu yeah."
    pc "Mmm, let me feel it. I want to taste it."
    show haven_peeping mouth_tounge eye_closed
    havenpeeper.name "Ahhh yeah!"
    show haven_peeping cum_face
    $ player.sex_cum(nosex, "face", main_quest_05)
    havenpeeper.name "Ahhhhhhh!"
    pc "Nnnnnn."
    show haven_peeping eye_penis
    havenpeeper.name "Ah so nice you dirty slut."
    show haven_peeping mouth_flat
    pc "Mmmm, enjoy yourself?"
    havenpeeper.name "Always enjoy myself when you play with me."
    pc "Happy to hear. Now I have to go and clean up before someone sees me."
    hide haven_peeping with dissolve
    "I quickly get up, leaving the pervert alone with his cock in his hand and head off out."
    $ working(20)
    $ walk(loc_haven_hallway_1f)
    jump travel

label haven_room1_listen_repeatable_blow:
    hide haven_peeping with dissolve
    show haven_blow wait with dissolve
    havenpeeper.name "Oh?"
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show haven_blow cum with dissolve
        show haven_blow 2h with dissolve
    elif randomnum == 2:
        show haven_blow cum with dissolve
        show haven_blow 1h with dissolve
    else:
        show haven_blow ballsuck with dissolve

    havenpeeper.name "Ah fuck yes."
    if player.desire > 80:
        pc "Mmmmmm."
    havenpeeper.name "Bet you were waiting for me so you could do this."
    if player.desire > 80:
        pc "♥"
    havenvik.name "Still got that plug in your arse?"
    show haven_blow wait with dissolve
    pc "Of course, It goes everywhere with me."
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show haven_blow cum with dissolve
        show haven_blow 2h with dissolve
    elif randomnum == 2:
        show haven_blow cum with dissolve
        show haven_blow 1h with dissolve
    else:
        show haven_blow ballsuck with dissolve
    havenpeeper.name "Fuck yes!"
    havenpeeper.name "This is becoming the highlight of my day."
    pc "*Hyuk*"
    havenpeeper.name "Gonna be sad when you leave or get knocked up."
    show haven_blow cum with dissolve
    havenpeeper.name "Fuck yes!"
    $ player.sex_cum(havenvik, "mouth", main_quest_05)
    havenpeeper.name "Ahhh yes yeeeeessss."
    havenpeeper.name "Take it in your mouth you whore!"
    havenpeeper.name "Ahhhhhh..."
    show haven_blow wait ub with dissolve
    show haven_blow neutral with dissolve
    havenpeeper.name "That's right. Swallow it all down. Bet you love it don't you?"
    pc "What else am I going to do with it?"
    havenpeeper.name "Mmmm"

    pc "Enjoy yourself?"
    havenpeeper.name "Always enjoy myself when you play with me."
    pc "Happy to hear. Now I have to go and clean up before someone sees me."
    hide haven_blow with dissolve
    "I quickly get up, leaving the pervert alone with his cock in his hand and head off out."
    $ working(20)
    $ walk(loc_haven_hallway_1f)
    jump travel

label haven_room1_listen_repeatable_grope:
    havenpeeper.name "Mmmmm. I'm gonna start seeing this perfect ass in my sleep at this rate."
    show haven_peeping eye_man
    pc "Why dream about it when it is right here for you?"
    show haven_peeping grope_ass eye_back with dissolve
    havenpeeper.name "Mmmm, that's right. It's right here for me to play with."
    havenpeeper.name "These sexy tits as well."
    show haven_peeping grope_tit with dissolve
    $ dialouge = WeightedChoice([
    ("One day I am going to lock you to my bed by these nipple rings and keep you as my sex pet.", 1),
    ("So firm and big for such a tiny girl.", 1),
    ("Wonder how big they would grow if I put a baby in you.", 1),
    ])
    havenpeeper.name "[dialouge]"
    pc "Mmmm."
    show haven_peeping grope_ass shorts_down with dissolve
    havenpeeper.name "Ah yes. This naked bum with that plug right up you."
    "He switches between wiggling the plug inside me and groping my ass while he masturbates."
    show haven_peeping mouth_happy
    pc "Ahhh! That is so fucking big in me. It's going to drive me crazy. ♥"
    havenpeeper.name "Bet you love a huge cock in your arse as well."
    if player.check_sex_agree(5):
        pc "I do. But better fuck my pussy instead."
        havenpeeper.name "Mmm, love having both your holes filled?"
        pc "Of course!"
        jump haven_room1_listen_repeatable_sex_sex
    else:

        if not player.asex:
            pc "No idea, never had one in there. Only this plug."
        else:
            pc "It can be fun."
        havenpeeper.name "One day I will fill your arse with my cum. I will fuck your hole til you beg me to stop."
        pc "Mmmm, promises promises. Let me feel you cum all over my back instead."
        havenpeeper.name "Haaa, you was going to feel it anyway."
        havenpeeper.name "Ahhhhh!"
        show haven_peeping cum_ass with dissolve
        $ player.sex_cum(nosex, "ass", main_quest_05)
        havenpeeper.name "Huuu yes."
        pc "Mmm I can feel it. So warm."
        pc "Haaa. ♥"
        pc "Mmmm, that was fun."
        havenpeeper.name "Sure was. Love having a dirty girl like you using my spy hole."
        pc "I bet."

    havenpeeper.name "Better clean up and get out of here. You're a noisy bitch."
    show haven_peeping noman eye_man mouth_flat with dissolve
    "He gets up, puts his trousers on and quickly heads out."
    pcm "Yeah, leave me here with my arse hanging out..."
    $ working(20)
    "I get dressed and head out as well."
    hide haven_peeping with dissolve
    jump travel

label haven_room1_listen_repeatable_sex:
    jump expression WeightedChoice([
    ("haven_room1_listen_repeatable_sex_intro1", 1),
    ("haven_room1_listen_repeatable_sex_intro2", 1),
    ("haven_room1_listen_repeatable_sex_intro3", If (player.has_perk(perk_preg_want), 1,0)),
    ])

label haven_room1_listen_repeatable_sex_intro1:
    show haven_peeping eye_man
    havenpeeper.name "I love it when you are feeling like a dirty slut."
    pc "Sitting here for ages looking at all the naked bodies can do that to you."
    show haven_peeping grope_ass eye_back with dissolve
    havenpeeper.name "I know. Looking at the sexy whores in the shower does the same for me. Makes me want to come and fuck you."
    pc "Why not go and fuck one of them in the shower?"
    havenpeeper.name "Not often that the girls allow that. Too many eyes watching."
    $ c.bottom = 0
    $ c.pants = 0
    show haven_peeping grope_ass shorts_down with dissolve
    if "joined_shower" in loc_haven_shower_stall.dict and loc_haven_shower_stall.dict["joined_shower"]:
        pc "Hmm, didn't stop the guys from trying with me."
        havenpeeper.name "Well, you are a little slut. Bet you fucked them and now they all want some of you."
    else:
        pc "Doubt that will stop the perverts from trying."
        havenpeeper.name "Sexy bitch like you naked in the shower, who won't try an fuck you?"
    jump haven_room1_listen_repeatable_sex_sex

label haven_room1_listen_repeatable_sex_intro2:
    show haven_peeping eye_man
    havenpeeper.name "Thought so. Looking at all the men getting you hot?"
    pc "You could say that."
    show haven_peeping grope_ass eye_back with dissolve
    havenpeeper.name "I feel the same when looking at the girls. Would love to go in there and fuck one of em."
    pc "Why don't you? I can watch from here"
    havenpeeper.name "Too many eyes. They aren't as dirty as you are."
    $ c.bottom = 0
    $ c.pants = 0
    show haven_peeping grope_ass shorts_down with dissolve
    if "joined_shower" in loc_haven_shower_stall.dict and loc_haven_shower_stall.dict["joined_shower"]:
        pc "Hmm, doesn't stop them from trying."
        havenpeeper.name "Maybe because you let them fuck you?"
        pc "Who said I did?"
        havenpeeper.name "You are a slut so just a guess."
    else:
        pc "No one has came and tried. Not sure what I would say."
        havenpeeper.name "Give it time. Doubt it will be long before I look through that hole and see you with a dick in you?"
    jump haven_room1_listen_repeatable_sex_sex

label haven_room1_listen_repeatable_sex_intro3:
    show haven_peeping eye_man
    havenpeeper.name "Can't pass up the chance of getting knocked up again?"
    pc "That's just an added bonus."
    show haven_peeping grope_ass eye_back with dissolve
    havenpeeper.name "Doubt you are lacking offers in here. Probably collected enough cum to get half of [town] pregnant."
    pc "Only care about me getting pregnant."
    havenpeeper.name "Shame, I wouldn't say no to knocking up some of your friends as well."
    $ c.bottom = 0
    $ c.pants = 0
    show haven_peeping grope_ass shorts_down with dissolve
    pc "You would take any chance to fuck someone so that's no shock."
    havenpeeper.name "Not anyone. But sexy little things like you, yes."
    jump haven_room1_listen_repeatable_sex_sex

label haven_room1_listen_repeatable_sex_sex:
    show haven_peeping poke_out mouth_happy with dissolve
    pc "Ah, I feel you poking me. ♥"
    havenpeeper.name "Gonna make you feel more than that."
    $ player.sex_vag(havenpeeper, main_quest_05)
    show haven_peeping poke_in enjoy with dissolve
    pc "Ah fuck yes! ♥ So full!"
    "He relentlessly fucks my pussy and with each thrust his pelvis pushes my butt plug deeper in my arse making it feel like I am being fucked in both holes."
    $ player.add_desire(100)
    pc "♥ ♥ ♥"
    pc "Fuuuuuuuucc..."
    havenpeeper.name "Yes take it you slut."
    pc "Ah yes!"
    havenpeeper.name "Ah you dirty whore. I am cumming."
    pc "Haaaahhhh."
    $ player.sex_cum_location_offer(
    difficulty=3, choice_inside="Keep going!", choice_pullout="Not inside.",  
    cum_want="haven_room1_listen_repeatable_sex_cum_want", 
    cum_notwant="haven_room1_listen_repeatable_sex_cum_notwant", 
    cum_pullout="haven_room1_listen_repeatable_sex_cum_pullout", 
    )

label haven_room1_listen_repeatable_sex_cum_pullout:
    pc "Fuck yes. Cum on my arse!"
    havenpeeper.name "Haaaaa. Ahhhhhh."
    show haven_peeping grope_tit with dissolve
    $ player.sex_cum(havenpeeper, "ass", main_quest_05)
    pc "Ahhh I can feel you spraying it on me."
    havenpeeper.name "Haaa ahhhh..."
    show haven_peeping talk mouth_happy eye_back brow_straight with dissolve
    pc "Haaa. ♥"
    pc "Mmmm, that was fun."
    show haven_peeping poke_out with dissolve
    havenpeeper.name "Sure was. Love having a dirty girl like you using my spy hole."
    pc "I bet."
    jump haven_room1_listen_repeatable_sex_cum_end

label haven_room1_listen_repeatable_sex_cum_notwant:
    havenpeeper.name "Nnnng, too late! Ahhhhh!"
    show haven_peeping talk brow_worried eye_back mouth_shocked
    pc "Whaa..."
    havenpeeper.name "Haaaaa. Ahhhhhh."
    $ player.sex_cum(havenman, "inside", main_quest_05)
    pc "Ahhh I can feel you pumping in me."
    havenpeeper.name "Haaa ahhhh..."
    show haven_peeping eye_closed mouth_happy brow_straight
    pc "Mmmm."
    pc "Better not be trying to knock me up."
    havenpeeper.name "Ah sorry, you asked too late."
    show haven_peeping eye_back mouth_flat
    pc "..."
    pc "Whatever."
    jump haven_room1_listen_repeatable_sex_cum_end

label haven_room1_listen_repeatable_sex_cum_want:
    pc "Fuck yes. Fuck me!"
    havenpeeper.name "Haaaaa. Ahhhhhh."
    $ player.sex_cum(havenman, "inside", main_quest_05)
    pc "Ahhh I can feel you pumping in me."
    havenpeeper.name "Haaa ahhhh..."
    show haven_peeping talk mouth_happy eye_back brow_straight with dissolve
    pc "Haaa. ♥"
    pc "Mmmm, that was fun."
    show haven_peeping poke_out with dissolve
    havenpeeper.name "Sure was. Love having a dirty girl like you using my spy hole."
    pc "I bet."
    jump haven_room1_listen_repeatable_sex_cum_end

label haven_room1_listen_repeatable_sex_cum_end:
    havenpeeper.name "Better clean up and get out of here. You're a noisy bitch."
    show haven_peeping noman eye_man mouth_flat with dissolve
    "He gets up, puts his trousers on and quickly heads out."
    pcm "Yeah, leave me here with my arse hanging out..."
    hide haven_peeping with dissolve
    $ pc_dress_slow()
    jump travel

label haven_room1_listen_masturbate:
    pc "Mmmmm."
    pcm "Watching all this is making me a bit..."
    show haven_peeping arm_mast peep with dissolve
    $ c.pants = 0
    $ c.bottom = 0
    if player.cum_locations["cum_vagin"]:
        "I slip my hand into my shorts and start to masturbate. The cum inside my pussy is leaking out and I rub it all over my lips and use it as a lube to slide my fingers inside myself."
        "I quickly finger fuck myself in case someone hears me moaning while looking at the naked bodies in the shower."
        pcm "Mmmm, how many of them would come and put more cum in my pussy if they know I was here."
    else:
        "I slip my hand into my shorts and start to masturbate. I am so horny that I am already soaking wet so I slide my fingers right inside."
        "I quickly finger fuck myself in case someone hears me moaning while looking at the naked bodies in the shower."
        pcm "Mmmm, how many of them would come and take turns fucking me if they knew I was here fingering myself."


    pcm "Show me those giant cocks you will fill me with. I am here for you with a giant plug in my arse waiting to be ravaged!"
    pcm "Fuck me fuck me!"
    pcm "Oh yes, take turns on me and fill me to the brim. Fill me!"
    if player.has_perk(perk_preg_want):
        pcm "Let me feel your cocks throbbing as they put a baby in me. So many cocks throbbing in me I will have no idea who the father is."
        pcm "Make me a mother with giant tits that men want to milk while fucking me like a dirty cow!"
    show haven_peeping enjoy with dissolve
    $ player.sex_cum(nosex, "self", main_quest_05)
    pc "Haaaahhh yes. Ahhhh... ♥ ♥"
    pc "Mmmmmm. ♥"
    pcm "..."
    show haven_peeping peep arm_wall with dissolve
    pcm "Phew. Better get out of here in case anyone heard that."

    $ working(5)
    $ pc_dress()
    hide haven_peeping with dissolve
    jump travel

label haven_room1_listen_punish:
    jump expression WeightedChoice([
    ("haven_room1_listen_punish_1", 1),
    ("haven_room1_listen_punish_2", 1),
    ("haven_room1_listen_punish_3", 1),
    ("haven_room1_listen_punish_4", 1),
    ("haven_room1_listen_punish_5", 1),
    ])

label haven_room1_listen_punish_1:
    show haven_peeping catch with dissolve
    hav "What's so interesting there?"
    $ player.face_worried()
    show haven_peeping talk mouth_shocked brow_worried eye_man with dissolve
    pc "Errr... I... I saw..."
    $ dialouge = WeightedChoice([
    ("HEY SHOWERING PEOPLE. SOME BITCH HERE GETTING OFF ON YOU LOT!", 1),
    ("See something interesting in that hole eh? Pervert!", 1),
    ("People in this place can't even shower without someone like you getting off on them?", 1),
    ("What? Not getting enough of a dicking out there an you have ta come in and get off watching this lot?", 1),
    ("Pretty sure if you wanted more of a dicking, all you need to do is walk right in there. Sure they would love to take turns riding you.", 1),
    ])
    hav "[dialouge]"
    pcm "Better get out of here."
    $ player.add_mood(-8)
    hide haven_peeping with dissolve
    $ walk(loc_haven_hallway_1f)
    pause 0.5
    $ walk(loc_haven_lobby)
    hav "Come back and I'll show you mine!"
    $ player.add_mood(-8)
    $ walk(loc_haven_landing)
    pc "..."
    pc "Fuck. Caught red handed..."
    $ player.add_mood(-8)
    jump travel

label haven_room1_listen_punish_2:
    havgirl "What are you doing alone in here. Don't you know..."
    $ player.face_worried()
    show haven_peeping talk mouth_shocked brow_worried eye_man with dissolve
    pc "Errr... I... I saw..."
    havgirl "What? Are you spying on people?"
    havgirl "Bitch!"
    pcm "Better get out of here."
    $ player.add_mood(-8)
    hide haven_peeping with dissolve
    $ walk(loc_haven_hallway_1f)
    pause 0.5
    $ walk(loc_haven_lobby)
    havmuff "Pervert bitch!"
    $ player.add_mood(-8)
    $ walk(loc_haven_landing)
    pc "..."
    pc "Fuck. Caught red handed..."
    $ player.add_mood(-8)
    jump travel

label haven_room1_listen_punish_3:
    show haven_peeping catch with dissolve
    hav "What's so interesting there?"
    $ player.face_worried()
    show haven_peeping talk mouth_shocked brow_worried eye_man with dissolve
    pc "Errr... I... I saw..."
    $ dialouge = WeightedChoice([
    ("HEY SHOWERING PEOPLE. SOME BITCH HERE GETTING OFF ON YOU LOT!", 1),
    ("See something interesting in that hole eh? Pervert!", 1),
    ("People in this place can't even shower without someone like you getting off on them?", 1),
    ("What? Not getting enough of a dicking out there an you have ta come in and got off watching this lot?", 1),
    ("Pretty sure if you wanted more of a dicking, all you need to do is walk right in there. Sure they would love to take turns riding you.", 1),
    ])
    hav "[dialouge]"
    pcm "Better get out of here."
    $ player.add_mood(-8)
    hide haven_peeping with dissolve
    show haven_grope with hpunch
    hav "Not so fast."
    pc "Move!"
    show haven_grope grope avoid stern with dissolve
    hav "You think it's okay to watch people then it's okay for me to do what I want."
    pc "..."
    hav "Right?"
    pc "Move out of the way."
    hav "..."
    show haven_grope waist with dissolve
    hav "Go on, get!"
    pc "..."
    hide haven_grope with dissolve
    $ walk(loc_haven_hallway_1f)
    pc "..."
    $ walk(loc_haven_bedroom)
    pause 0.5
    $ walk(loc_haven_bed)
    $ player.face_angry()
    pc "Bastard!"
    if player.mood <= 20:
        pc "..."
        $ player.eye = 3
        $ player.face_cry()
        pc "*SOB*"
    $ player.face_normal()
    jump travel

    jump travel

label haven_room1_listen_punish_4:
    show haven_peeping catch with dissolve
    hav "What are you doing there?"
    $ player.face_worried()
    show haven_peeping talk mouth_shocked brow_worried eye_man with dissolve
    pc "Errr... I... I saw..."
    hav "There a hole there? Fucking bitch!"
    hav "C'mere!"
    hide haven_peeping with hpunch
    hav "Cunts like you making living in this shithole even worse."
    "He drags me over to the corner and pushes me against some junk."
    show haven_bentover at right with hpunch
    pc "Wait, I..."
    $ player.punch()
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    $ player.add_mood(-8)
    $ player.add_desire(4)
    hav "Shut up."
    $ player.punch()
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    show haven_bentover ah with dissolve
    $ player.add_mood(-8)
    $ player.add_desire(4)
    pc "Ahhh!"
    pc "Stop! Please!"
    hav "Tsk!"
    $ player.punch()
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    $ player.add_mood(-8)
    $ player.add_desire(4)
    pc "Nnnnng."
    hav "Now piss off outta 'ere!"
    hide haven_bentover with dissolve
    hav "Go!"
    $ walk(loc_haven_hallway_1f)
    pc "..."
    $ walk(loc_haven_bedroom)
    pause 0.5
    $ walk(loc_haven_bed)
    $ player.face_angry()
    pc "Bastard!"
    pc "Treating me like a child..."
    if player.mood <= 20:
        pc "..."
        $ player.eye = 3
        $ player.face_cry()
        pc "*SOB*"
    $ player.face_normal()
    jump travel

label haven_room1_listen_punish_5:
    show haven_peeping catch with dissolve
    hav "What are you doing there?"
    $ player.face_worried()
    show haven_peeping talk mouth_shocked brow_worried eye_man with dissolve
    pc "Errr... I... I saw..."
    hav "There a hole there? Fucking bitch!"
    hav "C'mere!"
    hide haven_peeping with hpunch
    hav "Cunts like you making living in this shithole even worse."
    "He drags me over to the corner and pushes me against some junk."
    show haven_bentover at right with hpunch
    pc "Wait, I..."
    $ player.punch()
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    $ player.add_mood(-8)
    $ player.add_desire(4)
    hav "Shut up."
    $ player.punch()
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    show haven_bentover ah with dissolve
    $ player.add_mood(-8)
    $ player.add_desire(4)
    pc "Ahhh!"
    pc "Stop! Please!"
    hav "Tsk!"
    $ player.punch()
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    $ player.add_mood(-8)
    $ player.add_desire(4)
    pc "Nnnnng."
    $ c.bottom = 0
    $ c.pants = 0
    show haven_bentover with hpunch
    hav "Teach little sluts like you a lesson on what happens when you fuck around in this place."
    show haven_bentover mast plead with dissolve
    pc "No no no no stop!"
    hav "Why should I?"
    pc "Please please!"
    show haven_bentover poke with dissolve
    pc "Ahhh!"
    $ player.sex_forced(havenman, main_quest_05)
    $ player.sex_vag(havenman, main_quest_05)
    show haven_bentover inside ah with hpunch
    pc "Fuck!!!"
    hav "Take it you little bitch!"
    "I close my eyes and grit my teeth as he aggressively fucks me. He doesn't care one bit about making things pleasant for me."
    show haven_bentover with hpunch
    "I just try to block out the feeling as he thrusts into me, pressing against my arse and bouncing me forward, then pulling back for another go."
    show haven_bentover with hpunch
    "Suddenly the rhythmic thrusting turns more erratic..."
    show haven_bentover with hpunch
    $ player.sex_cum(havenman, "inside", main_quest_05)
    pcm "Noooo..."
    hav "Ahhhh yes!"
    hav "Haaaaaaa..."
    show haven_bentover mast with dissolve
    hav "Mmmm."
    $ player.punch()
    show screen spank_bum(0.75,0.5,0.6) with hpunch
    pc "Ah!"
    hav "Now piss off outta 'ere!"
    hide haven_bentover with dissolve
    hav "Go!"
    "I grab my shorts and rush out of the room."
    $ walk(loc_haven_hallway_1f)
    pc "..."
    $ walk(loc_haven_bedroom)
    pause 0.5
    $ walk(loc_haven_bed)
    $ player.face_angry()
    pc "Bastard!"
    pc "..."
    pc "Fuck... That really happened..."
    if player.mood <= 20:
        pc "..."
        $ player.eye = 3
        $ player.face_cry()
        pc "*SOB*"
        if player.mood <= 0:
            pc "I want out of this place..."
    $ pc_dress_slow()
    $ player.face_normal()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
