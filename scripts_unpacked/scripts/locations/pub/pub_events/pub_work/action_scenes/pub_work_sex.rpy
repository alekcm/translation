label pub_waitress_work_sex_debug:
    "Pub sex scene testing jump"
    "Are you selling yourself?"
    menu:
        "Yes":
            $ player.set_whore_price(0)

            "Where did you agree to have sex?"
            menu:
                "Handjob":
                    $ player.soldrequest = "hand"
                "Blowjob":
                    $ player.soldrequest = "oral"
                "Anal sex":
                    $ player.soldrequest = "anal"
                "Vag sex":
                    $ player.soldrequest = "vag"
                "No agreement was made":
                    $ player.soldrequest = ""
        "No":



            $ NullAction()

    jump pub_waitress_work_sex

label pub_waitress_work_sex:
    if player.soldprice > 0:
        pc "Let's go somewhere more private."
    else:
        pc "Let's go somewhere else to have some fun."
    patron "Ok, lead the way."
    if player.prop:
        pc "Let me just put these down."
        $ player.prop = ""
        pc "Ok, lets go."

    $ renpy.scene()
    with dissolve
    $ walk(renpy.random.choice([loc_pub_toilet_girls, loc_pub_toilet_boys, loc_pub_changingroom, If(weather_var >= 3, loc_pub_toilet_boys, loc_alley)]))
    if loc_cur == loc_pub_toilet_girls:
        pc "Not many girls around so it'll be fine in here."
    elif loc_cur == loc_pub_toilet_boys:
        pc "No one will see anything strange with a barmaid being in here."
    elif loc_cur == loc_pub_changingroom:
        pc "No one will disturb us in here."
    else:
        pc "Should be fine out here."
        if not numgen(0, (player.int + 20)):
            jump pub_waitress_work_sex_alley_abduct
    patron "Ok."

label pub_waitress_work_sex_jump:
    if player.soldprice > 0:
        $ dialouge = WeightedChoice([
        ("So... money first.", 1),
        ("Ok, hand over the money.", 1),
        ("Money before we do anything more.", 1),
        ("Pay up before we do anything more.", 1),
        ])
        pc "[dialouge]"
        $ dialouge = WeightedChoice([
        ("Sure, here you go.", 1),
        ("Right... Here we go.", 1),
        ("Ah right. Here you are.", 1),
        ("Sure.", 1),
        ])
        patron "[dialouge]"
        $ player.add_money(player.soldprice)
        $ randomnum = renpy.random.randint(1, 3)

    if player.soldrequest:
        if player.soldrequest == "hand":
            jump pub_waitress_work_sex_handjob
        elif player.soldrequest in ("oral", "blow"):
            jump pub_waitress_work_sex_blowjob
        elif player.soldrequest in ("anal", "ass"):
            jump pub_waitress_work_sex_start
        elif player.soldrequest == "vag":
            jump pub_waitress_work_sex_start
    else:

        pcm "Hmmm... What should I do..."
        $ player.sex_location_offer(option3="Get on my knees")
        menu:
            "Change my mind and leave" if not player.soldprice:
                jump pub_waitress_work_sex_bail
            "Get on my knees" if player.check_sex_agree(1, notif=False):
                jump expression renpy.random.choice(["pub_waitress_work_sex_handjob", "pub_waitress_work_sex_blowjob"])
            "Turn around and bend over" if player.check_sex_agree(3, notif=False):
                jump pub_waitress_work_sell_socks_sex_want





label pub_waitress_work_sex_handjob:
    $ dialouge = WeightedChoice([
    ("Mmm, show me what you have down there.", 1),
    ("Mmm, can't wait to see what you are packing.", 1),
    ("Show me what you got.", 1),
    ])
    pc "[dialouge]"
    $ player.sex_hand(pubpatron, pub_waitress)
    show sb_handjob down with dissolve

    $ dialouge = WeightedChoice([
    ("Oh, not a disappointment at all.", 1),
    ("Already up eh?", 1),
    ("Looks like your friend is happy to see me.", 1),
    ])
    pc "[dialouge]"
    show sb_handjob up
    $ dialouge = WeightedChoice([
    ("Not every day a slutty barmaid drags you off somewhere alone.", 1),
    ("Mmm. Getting a chance with a dirty little barmaid makes it stand up pretty quickly.", 1),
    ("Those giant tits of yours had me hard before we even came in here.", If (player.breasts == 3, 1, 0)),
    ("A drunken barmaid rushes me off somewhere alone so of course I am ready to go. Can't have you sobering up and changing your mind.", If (player.check_drunk(2), 1, 0)),
    ("Why else would I pay you to get me off if I wasn't already horny?", If (player.soldprice > 0, 1, 0)),  
    ])
    patron "[dialouge]"
    show sb_handjob down
    $ dialouge = WeightedChoice([
    ("Mmm, so warm and hard in my hand.", 1),
    ("Ha it feels so nice to have it in my hand.", 1),
    ("Solid as a rock. Been a while has it?", 1),
    ("With a cock like this, not even sure why you are paying me. Could easily get someone to do it for free.", If (player.selling, 1, 0)),
    ("Always nice when people paying me have nice cocks like this.", If (player.selling, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I stroke his cock with a nice rhythm and it seems he's enjoying it by the sounds he is making.", 1),
    ("I grip his warm cock in my hand and stroke it back and forth, slowly picking up the pace as I hear groans of pleasure from his mouth.", 1),
    ("I take his cock in my hand and start working at the shaft, stroking him while he looks at my naked tits.", 1),
    ("It is hardly the first cock I have had in my hand and I start wanking him off with expert skill. The noises he is making letting me know how fast or slow to go.", If (player.hsex > 15,1,0)),
    ("Even though he is paying me to do it, I still try to put in a good performance and make sure he gets as much pleasure out of it as possible.", If (player.selling, 1, 0)),
    ("Even though he is paying me, his cock in my hand still feels nice so I put in effort to make sure to give him as much pleasure as I can give him.", If (player.selling, 1, 0)),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ah yes! Keep going like that. So nice!", 1),
    ("Fuck! You slutty little barmaid!", 1),
    ("Ah fuck it feels nice. Love a little bitch like you wanking me off.", 1),
    ("Ah yes, like that.", 1),
    ("Fuck, you know what you are doing don't you?", If (player.hsex > 15,1,0)),
    ("Mmm, whores sure know what they are doing down there.", If (player.selling, 1, 0)),
    ("Having a whore grab your cock is great, they know how to treat it well.", If (player.selling, 1, 0)),
    ])
    patron "[dialouge]"

    show sb_handjob up
    $ dialouge = WeightedChoice([
    ("Mmm you dirty pervert, you like it when I do this?", 1),
    ("Bet you love it seeing a girl on her knees with your cock in her hand.", 1),
    ("Such a big one as well. Feels so nice and firm in my hand.", 1),
    ])
    pc "[dialouge]"

    patron "Mmmmmm!"
    if (player.selling and player.check_sex_agree(4)) or (not player.selling and player.check_sex_agree(2)):
        $ dialouge = WeightedChoice([
        ("Bet you would like it more if it were my lips around it instead of my hand.", 1),
        ("Wonder what it tastes like. I'm sure you don't mind if I have a try.", 1),
        ("Looks nice and big in my hand, but think I will try it in my mouth just to be sure.", 1),
        ("Mmm, starting to think it might be better off in my mouth.", 1),
        ("Want your slutty barmaid to suck you off?", 1),
        ])
        pc "[dialouge]"
        patron "Ah fuck yes!"
        jump pub_waitress_work_sex_blowjob_jump

    show sb_handjob down
    $ dialouge = WeightedChoice([
    ("Oooh, what was that? I think I can feel it pulsing.", 1),
    ("Wow, getting even harder now. Ready to blow on me are you?", 1),
    ("Enjoying that are you? I can feel your cock throbbing.", 1),
    ])
    pc "[dialouge]"

    $ dialouge = WeightedChoice([
    ("Ah fuck yes!", 1),
    ("Ah fuck! Sluts like you know how to work a cock.", 1),
    ("Ah yes, like that.", 1),
    ("Fuck! How many guys have you wanked off? This feels so good!", If (player.hsex > 15,1,0)),
    ("Ah fuck you dirty whore! Keep going.", If (player.selling, 1, 0)),
    ])
    patron "[dialouge]"
    patron "Ahhhhhhhhh..."
    patron "Yes!!"
    $ player.sex_cum(pubpatron, "hand", pub_waitress)
    $ dialouge = WeightedChoice([
    ("Oooh, it's coming out.", 1),
    ("Mmm it's throbbing.", 1),
    ("Mmmmm.", 1),
    ("Ooooh.", 1),
    ])
    pc "[dialouge]"
    patron "Haaaaa..."
    $ dialouge = WeightedChoice([
    ("Looks like someone enjoyed himself.", 1),
    ("Mmm, all sticky...", 1),
    ("Mmmmm. Made a bit of a mess there. \u2665", 1),
    ("Mmm so warm.", 1),
    ])
    pc "[dialouge]"
    patron "*Phew*"
    jump pub_waitress_work_sex_end

label pub_waitress_work_sex_blowjob:
    $ dialouge = WeightedChoice([
    ("Mmm, show me what you have down there.", 1),
    ("Mmm, can't wait to see what you are packing.", 1),
    ("Show me what you got.", 1),
    ("Show me what I am going to be sucking on.", 1),
    ])
    pc "[dialouge]"
    jump pub_waitress_work_sex_blowjob_jump

label pub_waitress_work_sex_blowjob_jump:
    $ player.sex_oral(pubpatron, pub_waitress)
    $ renpy.scene()
    show sb_blowjob up
    with dissolve
    show sb_blowjob face 1h with dissolve
    $ renpy.show(renpy.random.choice(["sb_blowjob 1h suck down", "sb_blowjob 2h suck down"]))
    with dissolve
    $ dialouge = WeightedChoice([
    ("He relaxes back against the wall as I take his warm cock in my hand and wrap my lips around it. It feels so nice and warm being there.", 1),
    ("I take his cock in my hands and start to stroke him while I put the tip of his cock in my mouth.", 1),
    ("I see his large cock in front of my face and take it in my hands. Then slowly I lick the tip of his penis and slide my lips around his cockhead.", 1),
    ("Seeing his huge cock in front of me fills me with excitement. I take him fully in my mouth while I wrap my fingers around his cock and stroke it.", 1),
    ("Even though I am being paid to suck him off. Seeing his huge cock in front of me still makes me excited and I happily take it in my hands and wrap my lips around it.", If (player.selling, 1, 0)),
    ])
    "[dialouge]"
    show sb_blowjob up
    pc "Mmmm ♥"
    show sb_blowjob down
    patron "Ahhhh!"
    $ dialouge = WeightedChoice([
    ("It's clear from his reactions that he's enjoying himself so I continue to work at his cock and swirling my tongue around him inside my mouth.", 1),
    ("His actions make it clear he is having fun. I speed up working his shaft with my hands as I use my tongue to pleasure his cockhead.", 1),
    ("He rubs his fingers through my hair and tries to push his cock deeper into my mouth. I happily accept it and start working his shaft with my hands.", 1),
    ("He starts thrusting into my mouth in time with my head bobbing and eventually he is slowly fucking my mouth. I help him out by stroking his cock in time with his thrusts.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Mmmfff. Soo nice.", 1),
    ("Ah, more!", 1),
    ("Mmmff. So warm and nice.", 1),
    ("*Slurp*", 1),
    ("*Hyuk* *Hyuk* *Hyuk*", 1),
    ])
    pc "[dialouge]"
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        $ dialouge = WeightedChoice([
        ("Ah so nice. How about you bend over and let me fuck you?", 1),
        ("Mmm, come here. Show me that arse of yours so I can fill you with my cock.", 1),
        ("Ah you dirty slut. Turn around and let me fuck you.", 1),
        ("Ah you dirty bar bitch. Come here and let me fuck you.", 1),
        ("Such a nice little whore. Turn around so I can put my cock in you.", If (player.selling, 1, 0)),
        ])
        patron "[dialouge]"
        if player.check_drunk(5):
            pc "Mmmm."
            jump pub_waitress_work_sex_start
        elif player.selling and player.check_whore():
            show sb_blowjob up
            $ dialouge = WeightedChoice([
            ("That will cost more.", 1),
            ("Offer up more money if you want to fuck me there.", 1),
            ("You didn't pay for that so it will be extra.", 1),
            ])
            pc "[dialouge]"
            $ randomnum = renpy.random.randint(1, 3)
            if randomnum == 1:
                $ dialouge = WeightedChoice([
                ("Shit. I can't afford anything more. Keep sucking then.", 1),
                ("Ah fuck no. Keep sucking me off then.", 1),
                ("Never mind then. I will stick to your mouth.", 1),
                ])
                patron "[dialouge]"
            else:
                $ player.soldprice = player.set_whore_price(0) / 4
                patron "How about an extra £[player.soldprice]?"
                menu:
                    "Agree":
                        $ player.add_money(player.soldprice)
                        jump pub_waitress_work_sex_start
                    "Refuse":
                        $ dialouge = WeightedChoice([
                        ("(Not really worth it. I'll keep sucking him off.", 1),
                        ("(For that I would rather just suck him off.", 1),
                        ])
                        pc "[dialouge]"
        else:
            menu:
                "Agree" if player.check_sex_agree(3):
                    jump pub_waitress_work_sex_start
                "Refuse":
                    $ dialouge = WeightedChoice([
                    ("Just keep sucking him. Not interested in being fucked right now.", 1),
                    ("Better not. Stick to him in my mouth", 1),
                    ])
                    pcm "[dialouge]"

label pub_waitress_work_sex_blowjob_jump_cum:
    show sb_blowjob down
    $ dialouge = WeightedChoice([
    ("Sexy little slut. Keep going!", 1),
    ("Ah fuck, keep going like that and you will make me cum.", 1),
    ("Yes, fuck! Keep going...", 1),
    ("*Huff* *Huff* *Huffff*", 1),
    ])
    patron "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I start to feel his cock tensing up and his movements become erratic. I know he is about to cum very soon.", 1),
    ("His groaning lets me know he is not far off cumming so I pick up the pace and blow him even faster than I was before.", 1),
    ("He is gripping onto my head and thrusting quite aggressively now. I know he won't last much longer at this rate so I work his shaft harder with my hands to try and push him over the edge.", 1),
    ])
    "[dialouge]"
    show sb_blowjob angry closed
    $ player.sex_cum(pubpatron, "mouth", pub_waitress)
    $ dialouge = WeightedChoice([
    ("I feel his start to throb and push his cock deep in my mouth. He starts to cum and I feel his warmth squirting from his cock and get a good taste of his cum.", 1),
    ("He starts throbbing in my mouth and I feel the salty warmth from his cock enter my mouth.", 1),
    ("His cock starts to swell until he tenses up and releases his load in my mouth. Its warmth fill it up and I have no choice but to swallow most of it down.", 1),
    ("He throbs in my mouth and I feel the first wave fill me. I quickly swallow it down before another pulse shoots more on my tongue. I eagerly swallow that down as well until it seems he is all out of steam.", 1),
    ])
    "[dialouge]"
    show sb_blowjob up happy
    patron "Ahhhh! Yeeeeess..."
    patron "Haaaa..."
    pc "Mmmmm..."
    jump pub_waitress_work_sex_end





label pub_waitress_work_sex_start:
    if c.pants:
        show pub_undress with dissolve
        show pub_undress pants_off with dissolve
        $ c.pants = 0
        show pub_undress stand with dissolve
        $ dialouge = WeightedChoice([
        ("Like what you see?", 1),
        ("Is my skirt a little short? I hope I am not revealing myself.", 1),
        ("Enjoying the show?", 1),
        ])
        pc "[dialouge]"
        show pub_undress man with dissolve
        patron "Mmmm."
        $ renpy.scene()
        $ renpy.show(renpy.random.choice(["sb_againstwall2 pokevaghand wink worried", "sb_againstwall3 poke wink"]))
        with dissolve
    else:
        $ renpy.scene()
        $ renpy.show(renpy.random.choice(["sb_againstwall2 cum wink worried", "sb_againstwall3 cum wink"]))
        with dissolve
        $ dialouge = WeightedChoice([
        ("Looks like I left my knickers somewhere.", 1),
        ("Is my skirt a little short? I hope I am not revealing myself.", 1),
        ("Enjoying the show?", 1),
        ])
        pc "[dialouge]"
        patron "Mmmm."
    pc "I'm all yours baby."
    "I feel his cock rubbing up and down my wet slit as he is jerking his cock of."
    jump pub_waitress_work_sell_socks_sex_want





label pub_waitress_work_sex_vag:

    if player.vvirgin == True:
        jump pub_waitress_work_sex_vag_virgin
    $ if_showing("sb_againstwall2", "pokevaghand", "sb_againstwall3", "mast")
    $ dialouge = WeightedChoice([
    ("I feel his cock sliding between my lips as he wanks himself off a bit.", 1),
    ("I can feel him stroking his cock as the tip of his penis slides between my wet folds.", 1),
    ])
    "[dialouge]"
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke")
    if player.want_sexlocation == 2:
        $ dialouge = WeightedChoice([
        ("He is starting to poke me instead of switching to my arse...", 1),
        ("His cock should be wet enough already so he should have already put it somewhere else...", 1),
        ("Ah, he is starting to push deeper. If I let this go on he might end up trying to fill my pussy...", 1),
        ])
        pcm "[dialouge]"

        $ dialouge = WeightedChoice([
        ("That's not my arse you are poking.", 1),
        ("You are poking at the wrong hole.", 1),
        ("Wrong hole, I told you to take me in the bum.", 1),
        ])
        pc "[dialouge]"
        if player.check_speech(2):
            $ dialouge = WeightedChoice([
            ("I know. Just getting lubed up.", 1),
            ("Ah yeah...", 1),
            ("Did you? Okay sure.", 1),
            ("Don't worry, just getting it ready.", 1),
            ("Mmm, I know.", 1),
            ("Uh huh. Just having a bit of fun where it's wet.", 1),
            ])
            patron "[dialouge]"
            jump pub_waitress_work_sex_ass
        else:
            if (not player.check_sex_agree(3)) or (not player.pregpills and player.cycle_conditions["stage"] == "ovulate" and not player.has_perk(perk_preg_want)) or (player.vvirgin):
                jump pub_waitress_work_sex_forced_anal
            else:
                $ dialouge = WeightedChoice([
                ("I know. Just have some fun with it.", 1),
                ("Mmm, it's so nice here.", 1),
                ("So warm and wet here.", 1),
                ("You are so wet. Sure you want it in the arse?", 1),
                ])
                patron "[dialouge]"

    $ dialouge = WeightedChoice([
    ("His cock starts to push deeper and I feel him slowly start to stretch my pussy and fill me up inside.", 1),
    ("I feel him start to enter deeper and deeper with each poke until he is deep enough inside me that it's no longer poking but actual fucking.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ])
    "[dialouge]"


    $ player.sex_vag(pubpatron, pub_waitress)
    $ player.face_excited()
    $ if_showing("sb_againstwall2", "insidevag ag wink", "sb_againstwall3", "sex wink ag")
    if player.want_sexlocation == 2:
        $ dialouge = WeightedChoice([
        ("Ahhh. \u2665 That's not my bum...", 1),
        ("*Huff* \u2665 Wrong... Hole...", 1),
        ("\u2665", 1),
        ("\u2665 Thats not where I told you to put it.", 1),
        ])
        pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I feel him start to take long and deep thrusts inside me. Pushing his cock balls deep into me before pulling almost all the way out, then pushing it back in again. ", 1),
    ("He seems eager and I feel him taking quick and shallow thrusts while gripping onto my hips. He is fucking me like a horny little rabbit.", 1),
    ("He takes it slow and rhythmically thrusts in and out of me. My tits bounce back and forth in time with his thrusting and it feels very pleasant and hypnotic.", 1),
    ("He thrusts deeply into me before slowly sliding his cock out almost all the way. Then aggressively slams back into me in a quick and hard thrust.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("He starts to get into it more and spanks me or reaches round to grope at my tits as he is thrusting deep inside me.", 1),
    ("He starts to build momentum and it's not long before I hear his body slapping against my ass with each thrust into me.", 1),
    ("He builds up speed as I get used to him inside me and it's not long until he is harshly gripping my sides and pulling me against his thrusting cock.", 1),
    ("I am already soaking wet down there and it doesn't take him long to start hammering away at me. Fucking me hard and fast while smacking me on the arse.", If (player.desire > 80, 1, 0)),
    ("Having a cock in me is a familiar feeling and I start to thrust back against him so he can fill me deeper. He takes notice and grabs my hips and starts to slam into me, gripping hard against me as he thrusts.", If (player.vsex > 10, 1, 0)),
    ])
    "[dialouge]"

    if numgen():
        call pub_waitress_work_sex_spank from _call_pub_waitress_work_sex_spank

    $ dialouge = WeightedChoice([
    ("Ah fuck this is so nice. You are such a dirty girl!", 1),
    ("Ah yes this is so nice. You are gripping onto my cock!", 1),
    ("Ah fuck you are so warm. So nice having my cock in you.", 1),
    ("Damn you are soaked. Sexy girl, you want this more than me.", If (player.desire > 80, 1, 0)),
    ("Ah fuck, yes keep going like that. Fuck you are such a horny bitch.", If (player.desire > 80, 1, 0)),
    ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.vsex > 10, 1, 0)),
    ])
    patron "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Haaaaa... \u2665", 1),
    ("Ah fuck!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Keep going! Fuck yes! Fuck me! Fuck me!", If (player.desire > 80, 1, 0)),
    ("Ahhhhh \u2665 Fuuuuck! \u2665 Take me!", If (player.desire > 80, 1, 0)),
    ])
    pc "[dialouge]"

    if not numgen(0,10):
        call pub_waitress_work_sex_anal_switch from _call_pub_waitress_work_sex_anal_switch

    $ dialouge = WeightedChoice([
    ("My mind starts to lose focus as I focus only on the cock thrusting in and out of me. I can feel the pleasure building up inside me.", 1),
    ("My mind goes blank as I focus only on the approaching orgasm gripping my body.", 1),
    ("My pussy starts to tighten around his cock as he brings me closer and closer to orgasm.", 1),
    ("I focus only on the man behind me pounding his nice cock in and out of me. I can barely focus as he brings my dripping pussy to orgasm.", If (player.desire > 80, 1, 0)),
    ])
    "[dialouge]"
    $ player.face_orgasm()
    $ dialouge = WeightedChoice([
    ("Yes, yes! \u2665", 1),
    ("Ahhhhh!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh I am close~.", 1),
    ("Ahhhhh \u2665", 1),
    ])
    pc "[dialouge]"
    jump pub_waitress_work_sex_vag_cum

label pub_waitress_work_sex_spank:
    $ player.spank()
    $ if_showing("sb_againstwall2", "closed shock", "sb_againstwall3", "closed grit")
    $ dialouge = WeightedChoice([
    ("Haa \u2665", 1),
    ("Ooooh!", 1),
    ("Unnngg. \u2665", 1),
    ("Oh yes!", If (player.desire > 80, 1, 0)),
    ("Ah fuck.", If (player.desire > 80, 1, 0)),
    ])
    pc "[dialouge]"
    $ if_showing("sb_againstwall2", "wink happy", "sb_againstwall3", "wink happy")
    $ player.spank()
    $ dialouge = WeightedChoice([
    ("Oh you like that?", 1),
    ("Knew a bitch like you would like that.", 1),
    ("Dirty girls always love their ass being beat.", 1),
    ("Knew a dirty slut like you would love that.", If (player.isslut, 1, 0)),
    ("Ah the slut likes being spanked?", If (player.isslut, 1, 0)),
    ("Oh even whores love a good spanking?", If (player.iswhore, 1, 0)),
    ])
    patron "[dialouge]"
    $ if_showing("sb_againstwall2", "open vhappy", "sb_againstwall3", "up")
    $ dialouge = WeightedChoice([
    ("Yes! Do it again. \u2665", 1),
    ("Ah fuck!", 1),
    ("Mmmmmm.", 1),
    ("\u2665", 1),
    ("More!", 1),
    ])
    pc "[dialouge]"
    $ player.spank()
    $ if_showing("sb_againstwall2", "wink ag", "sb_againstwall3", "wink ag")
    return

label pub_waitress_work_sex_anal_switch:
    $ if_showing("sb_againstwall2", "pokevaghand", "sb_againstwall3", "mast")
    $ if_showing("sb_againstwall2", "pokeasshand")
    $ if_showing("sb_againstwall2", "pokeass", "sb_againstwall3", "poke")

    if player.want_sexlocation == 2:
        $ dialouge = WeightedChoice([
        ("Finally aiming for the hole I asked for? \u2665", 1),
        ("*Huff* \u2665 About time you found it.", 1),
        ("\u2665", 1),
        ("\u2665 About time you are putting it where I asked.", 1),
        ])
        pc "[dialouge]"
    else:
        $ dialouge = WeightedChoice([
        ("Thats my arse. \u2665", 1),
        ("*Huff* \u2665 You are poking my arsehole.", 1),
        ("\u2665", 1),
        ("\u2665 Haa, that's my other hole.", 1),
        ])
        pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I feel slide his cock out of my wet vagina and press it against my asshole and slide it inside.", 1),
    ("He pulls his cock out of my vagina and presses it against my asshole. Already slick with my juices and precum, he is able to easily penetrate me without issue.", 1),
    ("He pulls out of my vagina and presses his already lubed cock against my ass and he starts to masturbate while putting pressure against it and gently sliding it inside me.", 1),
    ("He pulls out and his cock is covered in my juices as he presses it against my asshole, wasting no time to start sliding it inside me.", 1),
    ])
    "[dialouge]"
    $ player.sex_anal(pubpatron, pub_waitress)
    $ if_showing("sb_againstwall2", "insideass", "sb_againstwall3", "sex")
    pc "♥"
    jump pub_waitress_work_sex_ass_jump





label pub_waitress_work_sex_ass:
    $ if_showing("sb_againstwall2", "pokevaghand")
    $ if_showing("sb_againstwall2", "pokeasshand")
    $ if_showing("sb_againstwall2", "pokeass", "sb_againstwall3", "poke")
    $ dialouge = WeightedChoice([
    ("I feel him slide his cock from my wet vagina and press it against my asshole while masturbating.", 1),
    ("He rubs his cock between my legs, making sure it is nice and slick before pressing it against me asshole.", 1),
    ("He presses his already lubed cock against my ass and he starts to masturbate while putting pressure against it.", 1),
    ("His cock is covered in my juices as he presses it against my asshole, ready to start sliding it inside me.", 1),
    ])
    "[dialouge]"



    $ player.sex_anal(pubpatron, pub_waitress)
    $ player.face_excited()
    $ if_showing("sb_againstwall2", "insideass", "sb_againstwall3", "sex wink ag")
    $ dialouge = WeightedChoice([
    ("He then gently presses it harder against my ass until I feel it easing its way deeper into my arse. Slowly until it is all the way inside me filling me up.", 1),
    ("He wiggles his cock against my asshole as he slowly presses it more firmly against me. It starts to slide inside me until I can feel his pelvis press against my ass checks.", 1),
    ("He gently prods against my asshole, with each prod sliding his cock a little deeper inside me. Eventually the prods turn to thrusting and I realise he has already got it all the way in and is fucking me.", 1),
    ("I gently ease back onto his slick cock and feel him start to enter me. Sliding inside deeper and deeper until he is all the way in.", 1),
    ])
    "[dialouge]"
    patron "Ahhhhhh so warm."
    if player.asex == 0:
        pc "Ahhh fuck! Ahhhhhahhhhh..."
        pc "Nnnnnggggggg."
        pcm "Fuck, never had it in the ass before and without proper lube, this fucking hurts..."
    elif player.asex <= 5:
        pc "Ahhhhh fuck..."
        pcm "I hope this gets easier the more I do it..."
    else:
        $ dialouge = WeightedChoice([
        ("Ahhh \u2665 You are so big!", 1),
        ("Ah fuck! It feels so huge inside me.", 1),
        ("Ah shit. You are opening me up.", 1),
        ("Ahhh haaa, it is so big. It totally fills me up.", 1),
        ])
        pc "[dialouge]"

    pc "Haaaa ♥"
    $ dialouge = WeightedChoice([
    ("He relentlessly fucks me in the ass while pressing me up against the wall. I feel his hard cock pumping in and out as he roughly grips onto my ass cheeks, spreading them so he can thrust in deeper.", 1),
    ("He slowly starts to pick up the pace and places his hands on my arse cheeks, spreading them while also using them as handholds to pull me deeper onto his cock.", 1),
    ("He spreads me as he slowly fucks me in the arse. He starts out gentle but starts picking up the pace once he realises I have adjusted to his huge cock filling me up.", 1),
    ("He seems to take pleasure in pulling his cock out right to the tip, then grabbing me by the hips and pulling me balls deep back onto his cock. While it is a bit rough, it is not without its pleasure.", 1),
    ("He barely waits for me to adjust to him being in my ass before he is pounding away at me with determination. He is gripping onto my hips and thrusting like a madman. While it does hurt a bit, it is far more pleasurable than painful.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Haaaaa... \u2665", 1),
    ("Ah fuck!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Keep going! Fuck yes! Fuck me! Fuck me!", If (player.desire > 80, 1, 0)),
    ("Ahhhhh \u2665 Fuuuuck! \u2665 Take me!", If (player.desire > 80, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("He keeps pounding away while groaning or muttering some dirty words. He doesn't make much sense though as he is lost in the pleasure of fucking me in the ass.", 1),
    ("He rhythmically fucks my asshole and I get lost in the hypnotic pleasure it brings. My breasts swinging back and forth in time with each thrust.", 1),
    ("I hear my ass cheeks clapping against his body as he continuously thrusts in and out of me. I find the rhythms and sound quite exciting and get lost in the pleasure of it all.", 1),
    ("He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.", 1),
    ])
    "[dialouge]"
    if randomnum == 1:
        call pub_waitress_work_sex_spank from _call_pub_waitress_work_sex_spank_1
    jump pub_waitress_work_sex_ass_jump

label pub_waitress_work_sex_ass_jump:
    $ dialouge = WeightedChoice([
    ("Ah fuck this is so nice. You are such a dirty girl!", 1),
    ("Ah yes this is so nice. You are gripping onto my cock!", 1),
    ("Ah fuck you are so warm. So nice having my cock in you.", 1),
    ("Ah fuck. You bar whores know how to give good service.", 1),
    ("Damn fucking your ass is great, seems they teach you young girls good things in school.", If (player.desire > 80, 1, 0)),
    ("Ah fuck, yes keep going like that. Fuck you are such a horny bitch.", If (player.desire > 80, 1, 0)),
    ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.vsex > 10, 1, 0)),
    ])
    patron "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Haaaaa... \u2665", 1),
    ("Ah fuck!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Keep going! Fuck yes! Fuck me! Fuck me!", If (player.desire > 80, 1, 0)),
    ("Ahhhhh \u2665 Fuuuuck! \u2665 Take me!", If (player.desire > 80, 1, 0)),
    ])
    pc "[dialouge]"

    $ dialouge = WeightedChoice([
    ("His grip on me starts to get stronger and a little painful as he gets more and more excited. His breathing is now getting more ragged with each thrust.", 1),
    ("His grip on my cheeks is now hard enough to leave marks on my skin as his thrusts start to become erratic. He is clearly enjoying this and may not last much longer.", 1),
    ("His hands are all over my body as he starts to put himself over the edge. His breathing becoming heavy and he starts to thrust much more aggressively into me.", 1),
    ("He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.", 1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("He must be close... And so am I, despite his cock being in my ass and not my pussy.", 1),
    ("I can feel myself close to orgasm despite the fact he is fucking me in the ass and not in my vagina.", 1),
    ("My body starts to tense up as I get closer to orgasm. Unexpected as it is my ass he is fucking.", 1),
    ("My body starts to quiver as his ass fucking brings me closer and closer to orgasm.", 1),
    ])
    "[dialouge]"
    $ player.face_orgasm()
    $ dialouge = WeightedChoice([
    ("Ahhh, I'm about to come!", 1),
    ("Ah fuck I am close...", 1),
    ("Fuck so good. I am not going to last much longer.", 1),
    ("Ah yes! I am cumming!", 1),
    ])
    patron "[dialouge]"
    $ player.face_orgasm()
    $ dialouge = WeightedChoice([
    ("Yes, yes! \u2665", 1),
    ("Ahhhhh!", 1),
    ("Yes! Yes! Yes!", 1),
    ("Ahhh so am I~.", 1),
    ("Ahhhhh \u2665", 1),
    ])
    pc "[dialouge]"

    jump pub_waitress_work_sex_ass_cum





label pub_waitress_work_sex_vag_cum:

    $ player.sex_cum_location_offer(
    difficulty=3, choice_inside="Keep going!", choice_pullout="Not inside.",  
    cum_want="pub_waitress_work_sex_vag_cum_want", 
    cum_notwant="pub_waitress_work_sex_vag_cum_notwant", 
    cum_pullout="pub_waitress_work_sex_cum_pullout",
    cum_pullout_anal="pub_waitress_work_sex_cum_pullout_anal", 
    cum_pullout_bj="pub_waitress_work_sex_cum_pullout_blowjob",  
    cum_pullout_poke="pub_waitress_work_sex_cum_pullout_poke",
    cum_bj="pub_waitress_work_sex_cum_pullout_blowjob_init",    
    )

label pub_waitress_work_sex_vag_cum_want:
    $ dialouge = WeightedChoice([
    ("Fuck! I want my first time to end with me being cummed in!", If (player.virgin_pregcheck, 100, 0)),
    ("Ahh! Cum in my virgin pussy!", If (player.virgin_pregcheck, 100, 0)),
    ("Cum inside me.", 1),
    ("You can finish inside me if you want.", 1),
    ("Keep going. Don't stop.", 1),
    ("Yes keep going. \u2665", 1),
    ("I'm close. Don't pull out! \u2665", 1),
    ("Ahh it feels so nice. Don't take it out. \u2665", 1),
    ("Keep going. Yes! Don't stop! \u2665", 1),
    ("Ah yes! \u2665", 1),
    ("I can feel you. Don't you dare pull out!", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Don't pull out. I want to feel you cum inside me! \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Keep going. Cum inside and give me what I want. \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Ahh wait. Ahh fuck yes. Stop! Keep going!", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Ah fuck yes. Haa, be careful...", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Ah fuck unload in me like a slut!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to brand me like a slut.", If (player.isslut, 1, 0)),
    ("Keep going. I love it when men cum inside me.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    pc "♥"

    $ dialouge = WeightedChoice([
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Come here and let me fill you up.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to fill you up.", 1),
    ("Ah get ready for carrying my baby!", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Haaa fuck I am going to knock you up!", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Get ready for my baby you bitch.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Ahhh yes take it deep inside. Hope you're feeling lucky.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Better hope you are lucky cos I am going to fill you up!", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("You dirty slut. Take me inside you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    patron "[dialouge]"

    $ player.sex_cum(pubpatron, "inside", pub_waitress)
    $ dialouge = WeightedChoice([
    ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
    ("His cock pulses inside me, unloading his cum deep inside me.", 1),
    ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
    ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
    ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
    ("I feel his cock pumping me full of cum and hope he is lucky enough to put a baby inside me.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("I feel euphoric as he tries to knock me up by pushing his cock balls deep inside me while it throbs and fill me full of his cum.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("I feel like a right bitch as I hope he can knock me up while cumming inside me.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("I have mixed feelings as I feel his cock throbbing inside me, ready to try and get me pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("I am caught between euphoria and dread as I orgasm on a cock that is trying to put a child inside me.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
    ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
    ])
    "[dialouge]"
    $ if_showing("sb_againstwall2", "happy", "sb_againstwall3", "happy")
    pc "Ahh yes."

    $ dialouge = WeightedChoice([
    ("Ahhh. I can feel it throbbing in me.", 1),
    ("Mmmmm \u2665 I can feel you pumping it in!", 1),
    ("Ah yes. Fill me up.", If (player.has_perk(perk_preg_notwant), 0, 1)),
    ("Haaaaaaaa \u2665", 1),
    ("Mmmmmmmmm \u2665", 1),
    ("Ohhh I feel it throbbing. \u2665", 1),
    ("Yes pump it in me! \u2665", If (player.has_perk(perk_preg_notwant), 0, 1)),
    ("Ah yes! \u2665", 1),
    ("Mmmm pump it in. Make me fat.", If (player.has_perk(perk_preg_want), 1, 0)),
    ("You going to make me carry your baby round for the next few seasons? \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Mmmm, are you gonna give me huge milk tits? \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
    ("Mmmm I can feel it. But you better not get me pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Mmmm so nice. Even if there is some risk...", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Mmmm. I never get bored of men filling me up.", If (player.isslut, 1, 0)),
    ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
    ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"

    jump pub_waitress_work_sex_end

label pub_waitress_work_sex_vag_cum_notwant:
    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Make sure to pull out! \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ahh wait. Take it out and cum somewhere else! I am not protected.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Don't finish inside me, I don't have protection.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"

    $ dialouge = WeightedChoice([
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Fuck that. Take it inside!", 1),
    ("Ah I am cumming! Can't stop!", 1),
    ("Nng fuck I am cumming.", 1),
    ("I want to fill you up.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to fill you up.", 1),
    ("Ah get ready for carrying my baby!", If (not player.pregnancy > 1, 1, 0)),
    ("Haaa fuck I am going to knock you up!", If (not player.pregnancy > 1, 1, 0)),
    ("Get ready for my baby you bitch.", If (not player.pregnancy > 1, 1, 0)),
    ("Ahhh yes take it deep inside. Hope you're feeling lucky.", If (not player.pregnancy > 1, 1, 0)),
    ("Better hope you are lucky cos I am going to fill you up!", If (not player.pregnancy > 1, 1, 0)),
    ("Take it you fat bitch!", If (player.pregnancy > 1, 1, 0)),
    ("Ah bet you love this. How you ended up pregnant in the first place.", If (player.pregnancy > 1, 1, 0)),
    ("You dirty slut. Take me inside you.", 1),
    ("Ah fuck yes you filthy slut.", 1),
    ])
    patron "[dialouge]"

    $ player.sex_cum(pubpatron, "inside", pub_waitress)
    $ if_showing("sb_againstwall2", "shock", "sb_againstwall3", "grit")
    $ dialouge = WeightedChoice([
    ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
    ("His cock pulses inside me, unloading his cum deep inside me.", 1),
    ("I try to move away from him, but his hands grip my thighs and pulls me balls deep on his cock as I feel it throb inside me.", 1),
    ("Lost in the throes of orgasm I am too late to pull away when he starts to cum and I just let him stay there even as I feel him cumming inside me and filling me up.", 1),
    ("Caught between my own orgasm and the feeling of him cumming inside me, I fail to get him to pull out properly and he unloads everything inside me.", 1),
    ("I feel his cock pumping me full of cum and my stomach sinks as I realise that now is a dangerous time to be having a man's cum inside me.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
    ("My orgasm is cut short as I realise that right now is a terrible time of the month to let a man cum inside.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
    ("He grips my hips and pushes his cock deep inside me. I am hit by a wave of terror as I realise right now is the most fertile time of the month.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
    ("I am caught between orgasm and trying to resist the guys attempts to cum inside but the feeling of his throbbing let's me know I didnt do a good enough job of getting off his cock.", 1),
    ("I feel the arsehole throbbing inside me and am filled with horror as I realise he could be getting me pregnant right now.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ])
    "[dialouge]"
    patron "Ahh yes."
    pc "Ah what are you doing?"
    if player.pregpills:
        $ dialouge = WeightedChoice([
        ("You are lucky I am on the pill or I would kick you for ignoring me and cumming inside.", 1),
        ("*Sigh* I told you to pull out. Now I am going to be leaking.", 1),
        ("Idiot. You are going to have me leaking now.", 1),
        ("Does \"pull out\" mean nothing to you? I'm going to have your cum trickling out of me for ages now...", 1),
        ("*Tsk* What did you go and do that for? You are going to have me leaking now...", 1),
        ])
        pc "[dialouge]"
    else:
        $ dialouge = WeightedChoice([
        ("What the hell? I don't want to be ending up with your shitty child in my belly.", 1),
        ("Idiot. I don't want to be carrying your baby around for the next few seasons.", 1),
        ("You do that on purpose or something? I don't want your accident in me.", 1),
        ("You trying to get me pregnant?", 1),
        ("Fuck, \"pull out\" mean nothing to you? I don't want your baby in me.", 1),
        ])
        pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("*Huff* It was too nice being inside you to pull out.", 1),
    ("Ah I didn't hear you. Was too busy enjoying that pussy of yours.", 1),
    ("Sorry, I thought I could last longer...", 1),
    ("It felt far too nice to stop.", 1),
    ("Ah it was so good in there.", 1),
    ])
    patron "[dialouge]"
    $ if_showing("sb_againstwall2", "frown", "sb_againstwall3", "pout")
    pc "*Sigh*"
    jump pub_waitress_work_sex_end

label pub_waitress_work_sex_cum_pullout_anal:
    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Make sure to pull out! \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ahh wait. Take it out and cum somewhere else! I am not protected.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Don't finish inside me, I don't have protection.", If (player.has_perk(perk_preg_notwant), 1, 0)),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Then I'll put it somewhere else warm.", 1),
    ("If not your pussy, then...", 1),
    ("Then take it in your arse!", 1),
    ("Ah then I'm gonna fuck your arse.", 1),
    ("I paid to put it somewhere warm. Then take it in your arse.", If (player.selling, 1, 0)),
    ("Ah you shitty whore. Take it in your arse then.", If (player.selling, 1, 0)),
    ("AH, then in your arse. Slut like you probably have enough cocks in there for it to be ready.", If (player.isslut, 1, 0)),
    ("Ah pulling out of a slut like you? Na, take it in the arse instead.", If (player.isslut, 1, 0)),
    ])
    patron "[dialouge]"
    $ if_showing("sb_againstwall2", "pokevaghand", "sb_againstwall3", "mast")
    $ if_showing("sb_againstwall2", "pokeasshand")
    $ if_showing("sb_againstwall2", "pokeass", "sb_againstwall3", "poke")
    $ player.sex_anal(pubpatron, pub_waitress)
    $ if_showing("sb_againstwall2", "insideass", "sb_againstwall3", "sex")
    $ dialouge = WeightedChoice([
    ("I feel slide his cock out of my wet vagina and press it against my asshole and slide it inside.", 1),
    ("He pulls his cock out of my vagina and presses it against my asshole. Already slick with my juices and precum, he is able to easily penetrate me without issue.", 1),
    ("He pulls out of my vagina and presses his already lubed cock against my ass and he starts to masturbate while putting pressure against it and gently sliding it inside me.", 1),
    ("He pulls out and his cock is covered in my juices as he presses it against my asshole, wasting no time to start sliding it inside me.", 1),
    ])
    "[dialouge]"
    pc "♥"

    $ player.sex_cum(pubpatron, "anal", pub_waitress)
    $ dialouge = WeightedChoice([
    ("He spreads my cheeks and pumps his load deep into my ass. Throb after throb unloading more into me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything into my ass.", 1),
    ("His cock pulses inside me, unloading his cum deep in my ass.", 1),
    ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
    ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
    ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
    ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
    ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
    ])
    "[dialouge]"
    patron "Ahh yes."

    $ dialouge = WeightedChoice([
    ("Ahhh. I can feel it throbbing in me.", 1),
    ("Mmmmm \u2665 I can feel you pumping it in!", 1),
    ("Ah yes. Fill me up.", 1),
    ("Ah yes. Pump my arse full!", 1),
    ("Haaaaaaaa \u2665", 1),
    ("Mmmmmmmmm \u2665", 1),
    ("Ohhh I feel it throbbing. \u2665", 1),
    ("Ah yes! \u2665", 1),
    ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
    ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"

    jump pub_waitress_work_sex_end

label pub_waitress_work_sex_cum_pullout_poke:
    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Make sure to pull out! \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ahh yes you dirty slut. Take it over you!", 1),
    ("Ah yes! Take it on your arse.", 1),
    ("Ah you dirty bitch. Take it all over you.", 1),
    ("Ah fuck I'm gonna cover you in it.", 1),
    ("Ah yes. Take it over you.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to cover you with my cum.", 1),
    ("You dirty slut. Take me over you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    patron "[dialouge]"
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke")
    $ player.sex_cum(pubpatron, "pullout", pub_waitress)
    $ dialouge = WeightedChoice([
    ("He pulls out and I can feel him poking me while cumming all over my pussy.", 1),
    ("He pulls out but still presses his cock against me as he cums.", 1),
    ("He pulls out as his cock pulses inside me, unloading his cum inside me and all over my lips.", 1),
    ("His cock slips out of me and I can feel his cock spraying it's load over my pussy.", 1),
    ("I feel his cock somewhat still inside me and I can feel him cumming and filling me up.", 1),
    ])
    "[dialouge]"
    if player.want_pullout:
        $ if_showing("sb_againstwall2", "frown", "sb_againstwall3", "pout")
        $ dialouge = WeightedChoice([
        ("You're too deep, pull out more!", 1),
        ("Idiot. Take it all out!", 1),
        ("*Huff* It's too deep. Take it out.", 1),
        ("Hey, pull it out more.", 1),
        ("Not so deep. Pull it out more!", 1),
        ("It's still inside. Take it out.", 1),
        ])
        pc "[dialouge]"
        $ if_showing("sb_againstwall2", "cum", "sb_againstwall3", "cum")
        $ dialouge = WeightedChoice([
        ("He finally pulls out all the way and I feel his last drops on my pussy lips and arse.", 1),
        ("He pulls out all the way and I can feel his warm cum hitting my naked arse.", 1),
        ("He pulls his cock out and starts jerking it. I can hear him moaning as he cums all over my bum.", 1),
        ("He eventually pulls out and I feel him spraying his load all over my arse and pussy.", 1),
        ("He pulls his cock out of me then presses his cockhead against my arsehole. I feel it throbbing as he grunts and then a warm trickle running down my arsehole and pussy.", 1),
        ])
        "[dialouge]"
        if player.pregpills:
            $ dialouge = WeightedChoice([
            ("You are lucky I am on the pill or I would kick you for ignoring me and cumming inside.", 1),
            ("*Sigh* I told you to pull out. Now I am going to be leaking.", 1),
            ("Idiot. You are going to have me leaking now.", 1),
            ("Does \"pull out\" mean nothing to you? I'm going to have your cum trickling out of me for ages now...", 1),
            ("*Tsk* What did you go and do that for? You are going to have me leaking now...", 1),
            ])
            pc "[dialouge]"
        else:
            $ dialouge = WeightedChoice([
            ("Next time pull out all the way. I don't want to be ending up with your shitty child in my belly.", 1),
            ("Idiot. I don't want to be carrying your baby around for the next few seasons. Pull out properly next time.", 1),
            ("You do that on purpose or something? I don't want your accident in me.", 1),
            ("You trying to get me pregnant?", 1),
            ("Fuck, \"pull out\" mean nothing to you? I don't want your baby in me.", 1),
            ])
            pc "[dialouge]"

        jump pub_waitress_work_sex_end
    else:
        $ dialouge = WeightedChoice([
        ("Ahhh. I can feel it throbbing in me.", 1),
        ("Mmmmm \u2665 I can feel you pumping it in!", 1),
        ("Ah yes. Fill me up.", If (player.has_perk(perk_preg_notwant), 0, 1)),
        ("Haaaaaaaa \u2665", 1),
        ("Mmmmmmmmm \u2665", 1),
        ("Ohhh I feel it throbbing. \u2665", 1),
        ("Yes pump it in me! \u2665", If (player.has_perk(perk_preg_notwant), 0, 1)),
        ("Ah yes! \u2665", 1),
        ("Mmmm pump it in. Make me fat.", If (player.has_perk(perk_preg_want), 1, 0)),
        ("You going to make me carry your baby round for the next few seasons? \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
        ("Mmmm, are you gonna give me huge milk tits? \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
        ("Mmmm I can feel it. But you better not get me pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
        ("Mmmm so nice. Even if there is some risk...", If (player.has_perk(perk_preg_notwant), 1, 0)),
        ("Mmmm. I never get bored of men filling me up.", If (player.isslut, 1, 0)),
        ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
        ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
        ])
        pc "[dialouge]"
    jump pub_waitress_work_sex_end

label pub_waitress_work_sex_cum_pullout_blowjob:
    patron "Ahhh fuck. Come here bitch and get on your knees!"
    $ renpy.scene()
    with dissolve
    show sb_blowjob up 2h poke with dissolve
    show sb_blowjob suck with dissolve
    jump pub_waitress_work_sex_blowjob_jump_cum

label pub_waitress_work_sex_cum_pullout_blowjob_init:
    pc "Don't cum in me. Here, let me put it somewhere else."
    $ renpy.scene()
    with dissolve
    show sb_blowjob up 2h poke with dissolve
    show sb_blowjob suck with dissolve
    jump pub_waitress_work_sex_blowjob_jump_cum





label pub_waitress_work_sex_ass_cum:

    if player.check_pullout():
        jump pub_waitress_work_sex_ass_cum_want
    else:

        menu:
            "Mmm, fill me up!":

                jump pub_waitress_work_sex_ass_cum_want
            "Mmm. Pull out and cover me with your cum!":

                if player.check_speech(2):
                    jump pub_waitress_work_sex_cum_pullout
                else:

                    jump pub_waitress_work_sex_ass_cum_notwant

label pub_waitress_work_sex_ass_cum_want:
    $ dialouge = WeightedChoice([
    ("Ah yes. Put it all in my ass!", 1),
    ("Cum inside me.", 1),
    ("You can finish inside me if you want.", 1),
    ("Keep going. Don't stop.", 1),
    ("Yes keep going. \u2665", 1),
    ("I'm close. Don't pull out! \u2665", 1),
    ("Ahh it feels so nice. Don't take it out. \u2665", 1),
    ("Keep going. Yes! Don't stop! \u2665", 1),
    ("Ah yes! \u2665", 1),
    ("Ah fuck unload in me like a slut!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to brand me like a slut.", If (player.isslut, 1, 0)),
    ("Keep going. I love it when men cum inside me.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    pc "♥"

    $ dialouge = WeightedChoice([
    ("Ah fuck you dirty little butt slut.", 1),
    ("Ah yes! Take it in your arse.", 1),
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Come here and let me fill you up.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to fill you up.", 1),
    ("You dirty slut. Take me inside you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    patron "[dialouge]"
    $ if_showing("sb_againstwall2", "happy", "sb_againstwall3", "happy")
    $ player.sex_cum(pubpatron, "anal", pub_waitress)
    $ dialouge = WeightedChoice([
    ("He spreads my cheeks and pumps his load deep into my ass. Throb after throb unloading more into me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything into my ass.", 1),
    ("His cock pulses inside me, unloading his cum deep in my ass.", 1),
    ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
    ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
    ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
    ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
    ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
    ])
    "[dialouge]"
    patron "Ahh yes."

    $ dialouge = WeightedChoice([
    ("Ahhh. I can feel it throbbing in me.", 1),
    ("Mmmmm \u2665 I can feel you pumping it in!", 1),
    ("Ah yes. Fill me up.", 1),
    ("Ah yes. Pump my arse full!", 1),
    ("Haaaaaaaa \u2665", 1),
    ("Mmmmmmmmm \u2665", 1),
    ("Ohhh I feel it throbbing. \u2665", 1),
    ("Ah yes! \u2665", 1),
    ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
    ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    $ if_showing("sb_againstwall2", "neutral", "sb_againstwall3", "smile")
    jump pub_waitress_work_sex_end

label pub_waitress_work_sex_ass_cum_notwant:
    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ah fuck you dirty little butt slut.", 1),
    ("Ah yes! Take it in your arse.", 1),
    ("Ah you dirty bitch. Take it inside.", 1),
    ("Ah fuck I'm gonna put it inside you.", 1),
    ("Ah yes. Take it.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Come here and let me fill you up.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to fill you up.", 1),
    ("You dirty slut. Take me inside you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    patron "[dialouge]"

    $ player.sex_cum(pubpatron, "anal", pub_waitress)
    $ dialouge = WeightedChoice([
    ("He spreads my cheeks and pumps his load deep into my ass. Throb after throb unloading more into me.", 1),
    ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything into my ass.", 1),
    ("His cock pulses inside me, unloading his cum deep in my ass.", 1),
    ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
    ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
    ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
    ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
    ])
    "[dialouge]"
    patron "Ahh yes."
    $ if_showing("sb_againstwall2", "frown", "sb_againstwall3", "pout")
    $ dialouge = WeightedChoice([
    ("I told you outside. It's gonna be leaking for the rest of my shift.", 1),
    ("You arse. It's going to be leaking while I work.", 1),
    ("Ugh, I told you outside.", 1),
    ("...", 1),
    ("Now it's going to get all sticky...", 1),
    ("*Sigh* It's going to get all sticky and make it hard to walk", 1),
    ("*Sigh* Just cum where you want why don't you?", 1),
    ("Just because you are paying me, doesn't mean you can just ignore me.", If (player.soldprice, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("*Huff* It was too nice being inside you to pull out.", 1),
    ("Ah I didn't hear you. Was too busy enjoying that pussy of yours.", 1),
    ("Sorry, I thought I could last longer...", 1),
    ("It felt far too nice to stop.", 1),
    ("Ah it was so good in there.", 1),
    ])
    patron "[dialouge]"
    pc "*Sigh*"
    pc "Whatever..."
    jump pub_waitress_work_sex_end

label pub_waitress_work_sex_cum_pullout:
    $ dialouge = WeightedChoice([
    ("Pull out. Don't cum inside me.", 1),
    ("Take it out and cum on my ass.", 1),
    ("*Huff* Take it out and put it on my ass.", 1),
    ("Ah yes, cum on my ass. \u2665", 1),
    ("Ahh! \u2665 Not inside...", 1),
    ("Ahh take it out. Cum over me. \u2665", 1),
    ("Make sure to pull out! \u2665", 1),
    ("Ah yes! Cum over me! \u2665", 1),
    ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
    ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
    ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ahh yes you dirty slut. Take it over you!", 1),
    ("Ah yes! Take it on your arse.", 1),
    ("Ah you dirty bitch. Take it all over you.", 1),
    ("Ah fuck I'm gonna cover you in it.", 1),
    ("Ah yes. Take it over you.", 1),
    ("Ah I am cumming!", 1),
    ("Nng fuck I am cumming.", 1),
    ("Yes, yes!", 1),
    ("Ah yes! I am going to cover you with my cum.", 1),
    ("You dirty slut. Take me over you.", If (player.isslut, 1, 0)),
    ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
    ])
    patron "[dialouge]"
    $ if_showing("sb_againstwall2", "cum", "sb_againstwall3", "cum")
    $ player.sex_cum(pubpatron, "ass", pub_waitress)
    $ dialouge = WeightedChoice([
    ("He pulls out and starts to come on my pussy lips and arse.", 1),
    ("He pulls out and I can feel his warm cum hitting my naked arse.", 1),
    ("He pulls his cock out and starts jerking it. I can hear him moaning as he cums all over my bum.", 1),
    ("He pulls out at the last moment and with a loud grunt, I feel him spraying his load all over my arse and pussy.", 1),
    ("He pulls his cock out of me then presses his cockhead against my arsehole. I feel it throbbing as he grunts and then a warm trickle running down my arsehole and pussy.", 1),
    ("He pulls out and furiously masturbates as he starts to groan. He sprays his load all over my ass cheeks and the back of my thighs. He then rubs his cock against my arsehole to get the last bits out.", 1),
    ("He pulls out and masturbates with one hand while gripping my arse cheek with the other. I feel him cumming over my bum and then he uses his hand to rub it all over my cheeks and between my legs.", 1),
    ("He pulls out and humps his cock between my bum cheeks. I can hear him groaning at the same time as I feel a wet warmth on my lower back. He slows as I start to feel the wetness run down to my arse and pussy.", 1),
    ])
    "[dialouge]"
    patron "Ahh yes!"
    $ dialouge = WeightedChoice([
    ("Mmmmm \u2665 I can feel it on my arse.", 1),
    ("Mmm. I can feel you have put it all over me.", 1),
    ("Ah yes. Put it all on me!", 1),
    ("Ah yes. Cover me in your cum!", 1),
    ("Ahh. \u2665 Now I am even wetter than when we started.", 1),
    ("Mmmm. I hope it's true that this stuff makes a good skin cream. \u2665", 1),
    ])
    pc "[dialouge]"

    jump pub_waitress_work_sex_end





label pub_waitress_work_sex_vag_virgin:
    if player.want_sexlocation == 1:
        if player.desire >= 80:
            pcm "I am so fucking wet right now and I can feel him prodding at me down there."
        elif player.desire <= 20:
            pcm "Maybe I shouldn't have offered my pussy. I can feel him posing me but I am not really wet..."
        else:
            pcm "I can feel him poking me and has starting to make me all wet."
        patron "You dirty little girl."
        if player.selling:
            pcm "Hope he makes me feel good. Even though I am selling myself to him, I still want to enjoy my first time..."
            pcm "Fuck... I am such a whore..."
        else:
            pcm "Hope he makes me feel good. I still want to enjoy my first time..."
        "I feel his penis start to enter me. The first time I have ever felt such an intrusion. While is it a bit uncomfortable, he isn't so deep yet so I can still enjoy it."
        patron "Fuck, you are so tight."
        pc "Well you are about to fuck a virgin."
        patron "What?"
        "He pulls out a little and his next thrust is much more persistent. I feel my lips being stretched and a fullness I have never felt before."
        $ if_showing("sb_againstwall2", "pokevag")
        $ if_showing("sb_againstwall2", "insidevag closed ag", "sb_againstwall3", "sex closed ag")


        $ player.sex_vag(pubpatron, pub_waitress)
        "Despite the pain, my mind is swimming with euphoria as I feel for the first time what it feels like to have a sex. A virile man penetrating and having his way with me."
        $ player.face_excited()
        pc "Ahh ♥ Fuck yes!"
        pc "Haaaaa"
        patron "Ahhhhhh yes. Take it!"

    elif player.check_sex_agree(5):
        $ if_showing("sb_againstwall2", "pokevaghand", "sb_againstwall3", "poke")
        "I feel his penis rubbing my slit to get it ready for my arse when I start to feel myself opening up more."
        pc "Ahh ♥ I told you to put it in my bum!"
        "He pulls out a little and starts rubbing deep in my slit."
        "But his next thrust is much more persistent. Instead of pulling out and aiming at my arse, he instead enters me deeper."
        $ if_showing("sb_againstwall2", "pokevag")
        $ if_showing("sb_againstwall2", "insidevag closed shock", "sb_againstwall3", "grit closed sex")


        $ player.sex_vag(pubpatron, pub_waitress)
        "Despite the pain, my mind is swimming with euphoria as I feel for the first time what it's like to have a sex. A virile man penetrating and having his way with me."
        $ player.face_excited()
        $ if_showing("sb_againstwall2", "wink ag", "sb_againstwall3", "wink ag")
        pc "Ahh ♥ That's not my bum!"
        pc "Haaaaa"
        patron "Ahhhhhh so warm and tight. I couldn't resist."
    else:

        $ if_showing("sb_againstwall2", "pokevaghand", "sb_againstwall3", "poke")
        "I feel his penis rubbing my slit to get it ready for my arse when I start to feel myself opening up more."
        $ if_showing("sb_againstwall2", "shock", "sb_againstwall3", "grit")
        pc "Not there. In the other one!"
        $ if_showing("sb_againstwall2", "pokevag")
        $ if_showing("sb_againstwall2", "insidevag closed pain", "sb_againstwall3", "grit closed sex")
        $ player.sex_forced(pubpatron, pub_waitress)
        $ player.sex_vag(pubpatron, pub_waitress)
        "His next thrust is much more persistent. He grips onto my hips and pushes himself inside me. I feel him sliding inside my virgin pussy and filling me with his rock hard cock, robbing me of my virginity."
        $ player.face_angry()
        pc "Fuck I told you not inside me. Take it out now!"
        patron "Don't worry, I will pull out."
        pc "Take it out!"
        jump pub_waitress_work_forcesex

    pc "Ahhh ♥ You are so big!"
    pc "Haaaa ♥"
    "He relentlessly fucks me up against the wall. I can feel his hard cock pumping in and out as he roughy grips my ass cheeks to pull himself deeper into me."
    "Pounding into me, he gets faster and faster as I get more and more excited. His grip on my arse no doubt leaving red marks on my skin and his breathing getting more ragged with every thrust."
    "He must be close... And so am I."
    $ player.face_orgasm()
    patron "Ahhh, I'm about to come!"
    jump pub_waitress_work_sex_vag_cum





label pub_waitress_work_sex_forced_anal:
    $ if_showing("sb_againstwall2", "insidevag pain closed angry", "sb_againstwall3", "closed sex grit")
    $ player.sex_forced(pubpatron, pub_waitress)
    $ player.sex_vag(pubpatron, pub_waitress)
    $ player.face_angry()
    $ dialouge = WeightedChoice([
    ("His cock starts to push deeper and I feel him slowly start to stretch my pussy and fill me up inside.", 1),
    ("I feel him start to enter deeper and deeper with each poke until he is deep enough inside me that it's no longer poking but actual fucking.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
    ])
    "[dialouge]"
    $ if_showing("sb_againstwall2", "wink", "sb_againstwall3", "wink")
    $ dialouge = WeightedChoice([
    ("Fuck I told you not inside me. Take it out now!", 1),
    ("You deaf? I told you in my arse. Take it out right fucking now!", 1),
    ("Ah take it out. I told you not to put it in there!", 1),
    ("Ah take it out, now!", 1),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Don't worry, I'll pull out.", 1),
    ("It's ok. I'll try not to cum inside.", 1),
    ("Don't worry. Just relax and enjoy.", 1),
    ("It's ok. I just want to make you feel good.", 1),
    ])
    patron "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Take it out!", 1),
    ("Get it out of me.", 1),
    ("I told you take it out!", 1),
    ("I said take it out of me.", 1),
    ])
    pc "[dialouge]"
    jump pub_waitress_work_forcesex

label pub_waitress_work_forcesex:
    if player.check_fight(2):
        $ player.face_angry()
        $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman", trans=vpunch)
        "I push as hard as I can against the wall, managing to push him off me and stumbles to the floor. Realising his predicament, he quickly pulls his trousers up and runs away."
        $ renpy.scene()
        with dissolve
        pc "What the fuck! What a cunt!"
        $ player.face_cry()
        $ pc_dress()
        $ walk(loc_pub)
        if player.has_perk([perk_whore, perk_numb]):
            $ player.sex_end()
            pcm "Fuck that was a close one. I need to be more careful."
            pc "*Phew*"
            jump pub_waitress_work_cycleend
        pc "*SOB*"
        if player.virgin_pregcheck:
            pc "My first time comes to this..."
        $ player.sex_end()
        $ walk(loc_pub_changingroom)
        $ pub_reset_vars()
        pc "I quickly get changed and leave."
        $ pub_waitress.work()
        $ pc_strip()
        pause 1
        $ tab_top = pub_waitress.clothes
        $ pc_dress()
        $ walk(loc_pub)
        pc "*SOB*"
        $ walk(loc_revel)
        pc "I can't believe that just happened..."
        pc "..."
        jump travel
    else:

        $ player.face_angry()
        with hpunch
        "I try to push against the wall to shove him away, but I am not strong enough and he pins me down harder."
        $ player.face_cry()
        pc "Fuck!"
        if player.selling:
            patron "Stop struggling, I paid to fuck you!"
        else:
            patron "This will go a lot easier if you stop struggling!"
        pc "Fuck you!"
        "He continues to pin me against the wall as he thrusts inside me. Fucking me with increased vigour knowing that I can't push him off."
        if player.virgin_pregcheck:
            patron "Mmmmm, such a lovely young slut. And is that blood? Were you a virgin?"
            patron "Oh man having popped the cherry of some little teenage slut. I will have to tell everyone."
            pc "*SOB*"
        else:
            patron "Mmmmm, such a lovely young slut."
            pc "*SOB*"
        patron "Ahhhhhh!"
        pc "*SOB*"
        $ player.sex_cum(pubpatron, "inside", pub_waitress)
        patron "Ahhh yes!"
        pc "*SOB*"
        $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman")
        "Once he is finished inside me, he quickly pulls out, puts his trousers on and leaves. Leaving me in the room alone."
        $ wardrobe.drop(item_pants_5)
        $ renpy.scene()
        with dissolve
        pcm "Bastard!"
        pc "*SOB*"
        $ walk(loc_pub_changingroom)
        $ pub_reset_vars()
        pc "I quickly get changed and leave."
        $ pub_waitress.work()
        $ pc_strip()
        pause 1
        $ tab_top = pub_waitress.clothes
        $ pc_dress()
        $ walk(loc_pub)
        pc "*SOB*"
        $ walk(loc_revel)
        pcm "I can't believe that just happened..."
        pcm "..."
        jump travel

label pub_waitress_work_sex_alley_abduct:
    $ player.grope_breasts()
    $ player.face_shock()
    patron "Got the bitch."
    patron "Hurry and deal with her."
    pcm "What the fuck!"
    if player.check_fight(3):
        $ player.grope_end()
        with hpunch
        "I kick the guy in the legs while trying to elbow him and just about manage to slip out of his grasp."
        $ walk(loc_pub, trans=False)
        $ player.add_mood(-50)
        $ player.add_desire(-50)
        with vpunch
        $ player.face_worried()
        pcm "Fuck! That almost went badly..."
        pc "*Phew*"
        show trixie at right5 with dissolve
        trixie.name "You ok?"
        pc "Yeah..."
        pc "Some fuckers in the alleyway..."
        trixie.name "Ugh. Arseholes."
        hide trixie with dissolve
        pc "..."
        pc "Well... Better get back to it."
        jump pub_waitress_work_cycleend
    else:
        with hpunch
        "I kick the guy in the legs while trying to elbow him but he holds me tighter and I can't get away from him."
        $ player.punch(True)
        pc "Ah!"
        show screen blackout(50)
        $ player.punch(True)
        pc "Haaaa fuck!"
        show screen blackout(100)
        $ player.punch(True)
        $ player.grope_end()
        $ walk(loc_highway, trans=False)
        $ walk(loc_bushes, trans=False)
        $ pc_strip()

        $ ko_assault(quest=pub_waitress)

        pause 2
        $ player.face_sleep()
        hide screen blackout with dissolve
        pc "Nnnng..."
        $ player.face_pain()
        pc "What the fuck!"
        pc "Ahhh shit!"
        $ player.face_cry()
        pc "Ah fuck it hurts so much!"
        pc "*Sniff*"
        pc "What the fuck even happened?"
        pc "Cunts!"
        pc "*SOB*"
        jump travel





label pub_waitress_work_sex_end:
    $ if_showing("sb_againstwall2", "open happy cum", "sb_againstwall3", "smile mast")
    patron "So nice."
    $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman")
    $ dialouge = WeightedChoice([
    ("That's why I love this place. Such lovely little sluts working here.", 1),
    ("Fucking you slutty little barmaids is always the highlight of my week", 1),
    ("Nothing better than coming here for some beers and ending the evening with a little slut on the end of your cock.", 1),
    ("Came here for some beers. But getting a little girl on the end of my cock is the best.", 1),
    ])
    patron "[dialouge]"
    patron "Cheers love. I'm gonna head back now."
    $ renpy.scene()
    with dissolve
    pc "I had better clean up before heading back out there."
    "I head to the sink and clean up any cum from my body."
    $ player.cum_clean_outside()
    if wardrobe.qty(item_pants_6):
        if not numgen(0,5):
            $ wardrobe.drop(item_pants_6)
            $ player.face_angry()
            pc "Did he take my pants as well? Fuck!"
            $ player.face_normal()
        else:
            $ pc_dress()
    pc "Ok, let's get back to it."
    if not numgen(0,4) and loc_cur == loc_pub_toilet_boys:
        jump pub_waitress_work_sex_post_offer
    jump pub_waitress_work_cycleend

label pub_waitress_work_sex_post_offer:
    patron "Hey luv. Got time for another customer?"
    pc "Huh? Oh?"
    if player.check_whore():
        menu:
            "Sure, I have time.":
                jump pub_waitress_work_sex_post_offer_agree
            "Sorry, I need to clean up.":
                jump pub_waitress_work_sex_post_offer_refuse
    else:
        jump pub_waitress_work_sex_post_offer_refuse

label pub_waitress_work_sex_post_offer_agree:
    $ player.set_whore_price(0)
    $ player.soldrequest = ""
    $ npc_race_picker()
    patron "How's £ [player.soldprice] sound?"

    if player.cum_locations["cum_vagin"] or player.cum_locations["cum_assin"]:
        pc "Err, I am kind of leaking everywhere down there so probably only good for a blowjob until I clean up."
        if not numgen(0,4):
            patron "I can settle for that."
            pc "Ok."
            $ player.soldrequest = "oral"
            jump pub_waitress_work_sex_jump
        else:
            if not numgen(0,10):
                patron "I'm fine with sloppy seconds for a discount."
                pc "Wow, ok..."
                $ player.soldprice = (int(player.soldprice * 0.65))
                $ player.soldrequest = "vag"
                jump pub_waitress_work_sex_jump
            else:
                jump pub_waitress_work_sex_post_offer_refuse

    elif player.cum_locations["cum_vagin"]:
        pc "Err, I'm kind of leaking right now so only anal or a blowjob."
        if not numgen():
            patron "I can settle for a blowie."
            pc "Ok."
            $ player.soldrequest = "oral"
            jump pub_waitress_work_sex_jump
        else:
            patron "Won't say no to fucking you in the ass."
            pc "Ok."
            $ player.soldrequest = "anal"
            jump pub_waitress_work_sex_jump

    pc "Sounds good."
    jump pub_waitress_work_sex_jump

label pub_waitress_work_sex_post_offer_refuse:
    if danger_gen(30, 1):
        patron "Well, wasn't really asking."
        jump pub_waitress_work_ko
    patron "No worries. I'll ask one of the other girls then."
    pc "Have fun."
    jump pub_waitress_work_cycleend





label pub_waitress_work_sex_bail:
    $ player.face_worried()
    pc "Err..."
    pc "Actually I don't think I can do this..."
    pc "I am going to go..."
    $ rand_choice = WeightedChoice([
    ("pub_waitress_work_sex_bail_beat", If(danger_content, 130 - player.int, 0)),
    ("pub_waitress_work_sex_bail_curse", 200 - player.int),
    ("pub_waitress_work_sex_bail_pay", 150),
    ("pub_waitress_work_sex_bail_leave", 500),
    ])
    jump expression rand_choice

label pub_waitress_work_sex_bail_leave:
    patron "Err, okay..."
    pc "Sorry..."
    $ walk(loc_pub)
    pc "*Sigh*"
    jump pub_waitress_work_cycleend

label pub_waitress_work_sex_bail_pay:
    patron "What if I offered to pay?"
    pc "Pay?"
    if player.check_whore():
        $ player.set_whore_price(0)
        pc "Hmm, how much?"
        patron "Let's see... How about £[player.soldprice]?"
        pc "..."
        menu:
            "Agree":
                pc "Okay then. I guess so."
                patron "Great!"
                jump pub_waitress_work_sex_jump
            "Refuse":
                pc "Sorry, I can't..."
                jump pub_waitress_work_sex_bail_leave

label pub_waitress_work_sex_bail_curse:
    patron "Fuckin teasing bitch!"
    pc "Wha..."
    pcm "Fuck, better get out of here..."
    patron "CUNT!"
    $ walk(loc_pub)
    $ player.add_mood(-20)
    pcm "What the hell... Arsehole."
    jump pub_waitress_work_cycleend

label pub_waitress_work_sex_bail_beat:
    patron "Fuckin teasing bitch!"
    pc "Wha..."
    pcm "Fuck, better get out of..."
    jump pub_waitress_work_ko
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
