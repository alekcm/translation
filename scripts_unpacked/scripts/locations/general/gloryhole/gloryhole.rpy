label gloryhole_start:
    $ npc_race_picker()
    show gh_blow_behind idle man_hole with dissolve
    pcm "Oh?"
    if numgen():
        show gh_blow_behind mast with dissolve
    "I take the offered money from his cock."
    $ player.add_money(10)
    $ player.sex_location_offer(option3="Get on my knees")
    if player.want_sexlocation == 1:
        jump gloryhole_sex_vag_start
    elif player.want_sexlocation == 2:
        jump gloryhole_sex_anal_start
    else:
        jump gloryhole_sex_blow_start





label gloryhole_sex_vag_start:
    $ renpy.scene()
    show gh_blow_close vagpoke
    with dissolve
    $ dialouge = WeightedChoice([
    ("I press his cock between my lips, and the cum leaking out of me makes it easy to slip inside.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I press his cock against me and the cum from before makes it nice and easy to slide him inside me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I already have cum leaking out of me so it's no effort to have him slide himself inside me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I line his cock up and am already horny and dripping wet so it's no effort to slide him inside.", If(player.check_horny(extreme=True), 100, 0)),
    ("I take his cock and rub it between my slit, making it wet and easier to enter me.", If(player.check_horny(), 100, 0)), 
    ("I line him up and gently press back against him. I am not very horny or wet so it takes a few prods before I am able to get him all the way.", If(not player.check_horny(), 100, 0)),
    ("I line the cock up with my slit and rub him a bit between my legs before easing myself back on him.",1),
    ])
    "[dialouge]"
    $ player.sex_vag(ghman, quest_gloryhole)
    show gh_blow_close vagsex with dissolve
    pc "Haaa..."
    $ dialouge = WeightedChoice([
    ("Haaa...",100),
    ("Mmmmm...",100),
    ("Ooooh yes...",100),
    ("Ung fuck",100),
    ("\u2665",100),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Fuck. How many of you perverts have fucked me now already?", If(player.cum_locations["cum_vagin"] > 5, 100, 0)),
    ("Ah yes! How many of you shitty cunts have fucked my dirty pussy already? You don't even care I am leaking.", If(player.cum_locations["cum_vagin"] > 10, 100, 0)),
    ("Mmm yes. One more man ready to cum inside me. Fuck yes.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("Ahhh feels so good to have you inside me. Are you gonna fuck me and make me cum? \u2665", If(player.check_horny(extreme=True), 100, 0)),
    ("Mmmmm. Make me feel good. It feels nice having you in me.", If(player.check_horny(), 100, 0)), 
    ("Mmm, I am such a slut for fucking you guys. But I can't resist letting you! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Ha yes. Feels nice putting you inside me!",100),
    ("Haaaa fuck. Always the best part when I feel someone slip inside me.",100),
    ])
    pcm "[dialouge]"
    jump gloryhole_sex_vag_picker

label gloryhole_sex_vag_cycle:
    $ dialouge = WeightedChoice([
    ("Haa fuck. So sexy having one man leak out and another man inside me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("Fuck so hot having someone's cum to use as lube.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("Yes put more inside me so I can be full to the brim.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("Fuck yes. Fuck me you dirty pervert! Keep going! YES! \u2665", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa fuck yes. Keep going you dirty man. Fuck me harder!", If(player.check_horny(), 100, 0)), 
    ("Fuck yes. Fuck me like so many have before. Your cock isn't the first and won't be the last to make me feel good! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Ah yes, fuck my pregnant pussy. Someone else claimed me but you can still have some fun with me.", If(player.preg_knows, 100, 0)),
    ("One of your perverted cocks sticking through the hole already knocked me up. I wonder if it was you?", If(player.preg_knows and player.preg_father_class == ghman, 100, 0)),
    ("Ha fuck! Keep going. Someone already paid to put a baby in me but you can still use and cum in me!", If(player.preg_knows and player.soldbaby, 100, 0)),
    ("Ha yes. Keep going!",100),
    ("Haaaa fuck. Fuck me you pervert!",100),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I enjoy the feeling of his cum covered cock fucking me from the other side of the wall. I don't care that he is paying me and isn't the first, I just want to enjoy.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("With each trust some cum leaks out of me as he starts making me feel good.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I love that I have both someone's cum and a cock inside me. So I rock as the cock inside me while rubbing myself off using cum as lube.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("I'm really horny so I furiously hump at his cock while masturbating, hoping I can get off before him.", If(player.check_horny(extreme=True), 100, 0)),
    ("I am fairly excited so I enjoy pressing back against his cock all while masturbating to have more fun.", If(player.check_horny(), 100, 0)), 
    ("I drunkenly hump against him while trying to keep balance all while my fingers rub between my legs.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I can barely stay on my feet as I press myself against the wall trying to hum at his cock.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I keep a decent pace as I hump at the guy sticking his cock in the hole.",100),
    ("I press his cock deep into me and keep humping to get him off.",100),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Mmm. I don't care that you are paying me, maybe you can fill me up even more. Fuck me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("Fuck yes, take turns to put more cum in me you dirty perverts. People before you filled me up so maybe you will too?", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("Fuck! Paying me to give me what I want. Fill me full of your cum you dirty pervert. You and the others before you.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("Yes! Pay for getting me off. Spank me and call me a bitch! \u2665", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa yes. Having to pay someone through a hole to get off? I don't care, I am horny so fuck me!", If(player.check_horny(), 100, 0)), 
    ("Hmmm come on. Fuck me and make me feel good.", If(not player.check_horny(), 100, 0)),
    ("Ah fuck! Yes keep going! I want to fuck you and all the people after you! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Mmmm. Wonder if your cock inside me knows someone already put a baby in me? I don't care, just keep going.", If(player.preg_knows, 100, 0)),
    ("Ahh fucking you perverts and letting you knock me up. Fuck I am such a bitch. And here I am again being fucked!", If(player.preg_knows and player.preg_father_class == ghman, 100, 0)),
    ("Haaaaa. Fuck! Too late to pay me to carry yours!", If(player.preg_knows and player.soldbaby, 100, 0)),
    ("Ah fuck yes!",100),
    ("Keep going, keep fucking me!",100),
    ("Ah yes, fuck it deep in me!",100),
    ])
    pcm "[dialouge]"
    jump expression WeightedChoice([
    ("gloryhole_sex_vag_cum",100),
    ("gloryhole_sex_vag_picker",250),
    ])

label gloryhole_sex_vag_picker:
    $ having_sex(3)
    jump expression WeightedChoice([
    ("gloryhole_sex_vag_close", If (not renpy.showing("gh_blow_close"), 100, 0)), 
    ("gloryhole_sex_vag_stand", If (not renpy.showing("gh_blow_behind sex_stand"), 100, 0)), 
    ("gloryhole_sex_vag_up", If (not renpy.showing("gh_blow_behind sex_up"), 100, 0)), 
    ("gloryhole_sex_vag_down", If (not renpy.showing("gh_blow_behind sex_down"), 100, 0)), 
    ])

label gloryhole_sex_vag_close:
    $ renpy.scene()
    show gh_blow_close vagsex
    with dissolve
    $ dialouge = WeightedChoice([
    ("I rock back and forth on his cock all while using the cum from someone else as lube to get myself off.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I hump the cock poking out of the wall while playing with the cum that is leaking out of me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I love that I have both someone's cum and a cock inside me. So I rock as the cock inside me while rubbing myself off using cum as lube.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("I'm really horny so I furiously hump at his cock while masturbating, hoping I can get off before him.", If(player.check_horny(extreme=True), 100, 0)),
    ("I am fairly excited so I enjoy pressing back against his cock all while masturbating to have more fun.", If(player.check_horny(), 100, 0)), 
    ("I drunkenly hump against him while trying to keep balance all while my fingers rub between my legs.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I can barely stay on my feet as I press myself against the wall trying to hum at his cock.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I keep a decent pace as I hump at the guy sticking his cock in the hole.",100),
    ])
    "[dialouge]"

    jump gloryhole_sex_vag_cycle

label gloryhole_sex_vag_stand:
    $ renpy.scene()
    show gh_blow_behind sex_stand
    with dissolve
    $ dialouge = WeightedChoice([
    ("I arch my back and cum leaks out of me as I press against him.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I stand up and moan at the feeling of cum leaking out of me as his cock thrusts inside me ready to put more there.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("I stand and play with my tits while enjoying the feeling of being full from his cock inside me.", If(player.check_horny(extreme=True), 100, 0)),
    ("I stand and enjoy the feeling of being fucked while I play with my tits to make it feel even nicer.", If(player.check_horny(), 100, 0)), 
    ("I let him do most of the work as I stand there and just feel him pistoning inside me.", If(not player.check_horny(), 100, 0)),
    ("I try to stay upright to keep my balance and almost forget I have a cock fucking me.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I can barely keep on my feet so I just press my arse against the hole letting him do all the work while I try not to fall over.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I stand and rock against the cock that is sticking inside me from the other side of the wall.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_vag_cycle

label gloryhole_sex_vag_up:
    $ renpy.scene()
    show gh_blow_behind sex_up
    with dissolve
    $ dialouge = WeightedChoice([
    ("I hold onto the opposite wall and use that as a springboard to furiously fuck his cock while I can barely contain my moans.", If(player.check_horny(extreme=True), 100, 0)),
    ("I use the opposite wall as leverage to help bounce on the cock that is inside me.", If(player.check_horny(), 100, 0)), 
    ("I use the wall opposite to help me with momentum while bouncing on the cock sticking out of the hole.", If(not player.check_horny(), 100, 0)),
    ("I hold onto the other wall for balance and use it to press my arse firmly against the hole, giving him easy access to keep fucking me.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I rest against the wall to keep myself upright and just hope the guy behind me is happy to do most of the work.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I use the wall in front of me to help me rock back and forth on his cock.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_vag_cycle

label gloryhole_sex_vag_down:
    $ renpy.scene()
    show gh_blow_behind sex_down
    with dissolve
    $ dialouge = WeightedChoice([
    ("I put my hand on the floor and present myself like a bitch on heat, making sure he put his cock as deep inside me as he can.", If(player.check_horny(extreme=True), 100, 0)),
    ("I bend over, making sure he has as easy access as possible to keep fucking and making me feel good.", If(player.check_horny(), 100, 0)), 
    ("I present myself as easy as possible, hoping it makes things easier on me since I am not all that horny.", If(not player.check_horny(), 100, 0)),
    ("I try to balance myself on the floor while giving him easy access to fuck me.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I drunkenly stumble and have to hold onto the floor to stop myself from entirely falling over. Though I am not sure the guy behind the wall even notices.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I stick my ass in the air to give as easy access as possible for the guy who is inside me.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_vag_cycle

label gloryhole_sex_vag_cum:
    $ player.sex_cum_location_offer(
    difficulty=3,
    cum_want="gloryhole_sex_vag_cum_want", 
    cum_notwant="gloryhole_sex_vag_cum_notwant",  
    cum_pullout="gloryhole_sex_vag_cum_pullout",
    cum_pullout_bj="gloryhole_sex_vag_cum_bj",  
    cum_bj="gloryhole_sex_vag_cum_bj",    
    )

label gloryhole_sex_vag_cum_want:
    $ dialouge = WeightedChoice([
    ("I make no effort to stop even though I know he's about to cum. He can add to what is already inside me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I make no effort to pull him out of me, maybe he will make me pregnant.", If(player.has_perk(perk_preg_want) and not player.preg_knows, 100, 0)),
    ("I keep riding him like a bitch .", If(player.check_horny(extreme=True), 100, 0)),
    ("I bend over, making sure he has as easy access as possible to keep fucking and making me feel good.", If(player.check_horny(), 100, 0)), 
    ("I keep bouncing on his cock waiting to feel him pumping inside me.", If(not player.check_horny(), 100, 0)),
    ])
    "[dialouge]"
    $ player.sex_cum(ghman, "inside", quest_gloryhole)
    $ dialouge = WeightedChoice([
    ("Fuck yes! Put a baby in me!", If(player.has_perk(perk_preg_want) and not player.preg_knows, 100, 0)),
    ("Ah yes yes yes! Keep fucking me!", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa yes. Fuck that felt good!", If(player.check_horny(), 100, 0)), 
    ("Ahhh yes. Cum in the dirty slut letting you fuck me through a hole in the wall! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Yes. Fill the whore you fuck paid to fuck! \u2665", If(player.has_perk(perk_whore), 100, 0)),
    ("Ah yes, fill my pregnant belly with more cum.", If(player.preg_knows, 100, 0)),
    ("One of your perverted cocks sticking through the hole already knocked me up. I wonder if it was you?", If(player.preg_knows and player.preg_father_class == ghman, 100, 0)),
    ("Yes! You can't get me pregnant again but you can try.", If(player.preg_knows and player.soldbaby, 100, 0)),
    ("Ha yes!",100),
    ("Haaaa...",100),
    ("\u2665 \u2665",100),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("*Phew*",100),
    ("*Huff* *Huff*",100),
    ("Oooohh...",100),
    ("Mmmm...",100),
    ])
    pc "[dialouge]"
    if renpy.showing("gh_blow_behind sex_down"):
        show gh_blow_behind sex_up with dissolve
    if renpy.showing("gh_blow_behind sex_up"):
        show gh_blow_behind sex_stand with dissolve
    if renpy.showing("gh_blow_close"):
        show gh_blow_close vagpoke with dissolve
    $ dialouge = WeightedChoice([
    ("Haaa...",100),
    ("Mmmmm...",100),
    ("Ooooh yes...",100),
    ("Ung fuck",100),
    ("\u2665",100),
    ])
    pc "[dialouge]"
    if renpy.showing("gh_blow_behind"):
        show gh_blow_behind no_man_hole with dissolve
    else:
        show gh_blow_close no_pc with dissolve
        show gh_blow_close no_man_hole with dissolve
    $ dialouge = WeightedChoice([
    ("His cock softens and slips out of me followed by his cum leaking out of me.",100),
    ("He pulls out of me with his cum leaking down my leg.",100),
    ("The guy pulls his cock from me and the hole and I am left standing there feeling his cum leak out of me.",100),
    ])
    "[dialouge]"
    pcm "..."
    jump gloryhole_end

label gloryhole_sex_vag_cum_notwant:
    $ player.sex_cum(ghman, "inside", quest_gloryhole)
    $ dialouge = WeightedChoice([
    ("Ah shit. You better not make me pregnant!", If(player.has_perk(perk_preg_notwant), 100, 0)),
    ("Ah! Had enough cocks I should know by now when they are cumming...", If(player.has_perk(perk_slut), 100, 0)),
    ("Oh? Good job I can't get pregnant again, but I am going to be leaking now...", If(player.preg_knows, 100, 0)),
    ("Ah shit. I'm gonna be all leaking now...",100),
    ("Ah fuck. I didn't get him to pull out...",100),
    ])
    pcm "[dialouge]"
    if renpy.showing("gh_blow_close"):
        show gh_blow_close vagpoke with dissolve
    $ dialouge = WeightedChoice([
    ("His cock softens and slips out of me followed by his cum leaking out of me.",100),
    ("He pulls out of me with his cum leaking down my leg.",100),
    ("The guy pulls his cock from me and the hole and I am left standing there feeling his cum leak out of me.",100),
    ])
    "[dialouge]"
    pcm "..."
    jump gloryhole_end

label gloryhole_sex_vag_cum_pullout:
    $ renpy.scene()
    show gh_blow_close vagsex
    with dissolve
    show gh_blow_close vagpoke with dissolve
    $ dialouge = WeightedChoice([
    ("I can feel the guy is about to blow, so I pull him out of me so he can't add to what is already leaking out of me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I can feel his is about to cum so I pull him out of me and rub his cock against me so I can still have some fun and get off.", If(player.check_horny(extreme=True), 100, 0)),
    ("He is about to cum so I pull him out of my but keep masturbating so I can push myself over the edge...", If(player.check_horny(), 100, 0)), 
    ("He is not far off so I pull him out of me and rum against him to get the job done.", If(not player.check_horny(), 100, 0)),
    ("I pull him out of me and wait to feel his warmth as he cums against me.",1),
    ])
    "[dialouge]"
    $ player.sex_cum(ghman, "pullout", quest_gloryhole)
    $ dialouge = WeightedChoice([
    ("He pumps his cum against my pussy, making it even more wet than before. Multiple guys on me, both inside and out have now marked me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I feel him warm cum squirting against me and I rub it all over my clit and lips. I am so horny I would let him get back inside and have another go.", If(player.check_horny(extreme=True), 100, 0)),
    ("I feel his warm cum hit my hands as I am still rubbing myself.", If(player.check_horny(), 100, 0)), 
    ("I eventually feel his cum hitting against me with some muffled moans from the other side of the wall.", If(not player.check_horny(), 100, 0)),
    ("I feel his warm cum hit me and start running down my ass and legs.",1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ha fuck that felt good. Still horny as shit though so maybe I should give someone else a go?", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa yes. Fuck that felt good!", If(player.check_horny(), 100, 0)), 
    ("Ahhh yes. Cum all over the dirty slut letting you fuck me through a hole in the wall! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Yes. Cum on the dirty whore you fuck paid to fuck! \u2665", If(player.has_perk(perk_whore), 100, 0)),
    ("One of your perverted cocks sticking through the hole already knocked me up. I wonder if it was you?", If(player.preg_knows and player.preg_father_class == ghman, 100, 0)),
    ("Yes! You can't get me pregnant again but you can cum all over me and mark me your bitch.", If(player.preg_knows and player.soldbaby, 100, 0)),
    ("Ha yes!",100),
    ("Haaaa...",100),
    ("\u2665 \u2665",100),
    ])
    pcm "[dialouge]"
    jump gloryhole_end

label gloryhole_sex_vag_cum_bj:
    if numgen():
        $ if_showing("gh_blow_behind", "suck", "gh_blow_close", "cum")
        $ player.sex_cum(ghman, "face", quest_gloryhole)
        pcm "[rlist.having_sex_suprise]"
    else:
        $ if_showing("gh_blow_behind", "suck", "gh_blow_close", "suck")
        $ player.sex_cum(ghman, "mouth", quest_gloryhole)
        "[rlist.blowjob_cum_mouth]"
        pc "[rlist.blowjob_muffle]"
    jump gloryhole_end





label gloryhole_sex_anal_start:
    $ renpy.scene()
    if not player.cum_locations["cum_assin"]:
        show gh_blow_close vagpoke with dissolve
        $ dialouge = WeightedChoice([
        ("I rub his cock between my lips, and the cum leaking out of me makes his cock nice and lubed ready for my arse.", If(player.cum_locations["cum_vagin"], 100, 0)),
        ("I rub his cock against me and the cum from before lubes him up and ready for my bum.", If(player.cum_locations["cum_vagin"], 100, 0)),
        ("I already have cum leaking out of me so rub his cock between my lips getting it ready for my arse.", If(player.cum_locations["cum_vagin"], 100, 0)),
        ("I rub his cock between my lips and I am already dripping wet, so it is easy to get him ready for my arse.", If(player.check_horny(extreme=True), 100, 0)),
        ("I take his cock and rub it between my slit, making it wet and ready for my bum.", If(player.check_horny(), 100, 0)), 
        ("I line him up and gently press back against him to make him wet. I am not very horny so it takes a few attempts before I think he is ready for my bum.", If(not player.check_horny(), 100, 0)),
        ("I rub his cock between my lips to get him nice and slick before moving him over to my ass.",1),
        ])
        "[dialouge]"
        show gh_blow_close asspoke with dissolve
    else:
        show gh_blow_close asspoke with dissolve
        $ dialouge = WeightedChoice([
        ("I line his cock up and am ready right away to have him fill my insides.", If(player.check_horny(extreme=True), 100, 0)),
        ("I take his cock press it against my prepared arsehole. I am so horny that I am eager to feel him inside me.", If(player.check_horny(), 100, 0)), 
        ("My arse has already been prepared by the last person to fuck me, so it's easy to line him up and guide him inside me.", If(not player.check_horny(), 100, 0)),
        ("I press his cock against my already leaking arsehole and slide in easily inside.",1),
        ])
        "[dialouge]"
    $ player.sex_anal(ghman, quest_gloryhole)
    show gh_blow_close asssex with dissolve
    pc "Haaa..."
    $ dialouge = WeightedChoice([
    ("Haaa...",100),
    ("Mmmmm...",100),
    ("Ooooh yes...",100),
    ("Ung fuck",100),
    ("\u2665",100),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Fuck. How many of you perverts have fucked my arse by now?", If(player.cum_locations["cum_assin"] > 5, 100, 0)),
    ("Ah yes! How many of you shitty cunts have stuck your cock in my arse? You don't even care I am leaking.", If(player.cum_locations["cum_assin"] > 10, 100, 0)),
    ("Ahhh feels so good to have you inside me. Are you gonna fuck me and make me cum? \u2665", If(player.check_horny(extreme=True), 100, 0)),
    ("Mmmmm. Make me feel good. It feels nice having you in me.", If(player.check_horny(), 100, 0)), 
    ("Fuck yes. Fuck my arse! I love it!", If(player.has_perk(perk_buttslut), 100, 0)), 
    ("Yes! Yes! Pound me and keep fucking me. I love having it deep in my arse.", If(player.has_perk(perk_buttslut), 100, 0)), 
    ("Mmm, I am such a slut for fucking you guys. But I can't resist letting you! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Ha yes. Feels nice putting you inside me!",100),
    ("Haaaa fuck. Always the best part when I feel someone slip inside me.",100),
    ])
    pcm "[dialouge]"
    jump gloryhole_sex_anal_picker

label gloryhole_sex_anal_cycle:
    $ dialouge = WeightedChoice([
    ("Haa fuck. So sexy having one man leak out and another man inside me.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("Fuck so hot having someone's cum to use as lube.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("Fuck yes. Fuck me you dirty pervert! Keep going! YES! \u2665", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa fuck yes. Keep going you dirty man. Fuck me harder!", If(player.check_horny(), 100, 0)), 
    ("Fuck yes. Fuck me like so many have before. Your cock isn't the first and won't be the last to make me feel good! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Fuck! Nothing better than a huge cock up my arse! Much better than the normal way.", If(player.has_perk(perk_buttslut), 100, 0)), 
    ("Yes! Stretch my arsehole and keep fucking me deep inside!", If(player.has_perk(perk_buttslut), 100, 0)), 
    ("Fuck yes. I love your cock in my arse. Keep going!", If(player.has_perk(perk_buttslut), 100, 0)), 
    ("Fuck my legs are shaking. Take me in the arse deeper!", If(player.has_perk(perk_buttslut), 100, 0)), 
    ("Ha yes. Keep going!",100),
    ("Haaaa fuck. Fuck me you pervert!",100),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I enjoy the feeling of his cum covered cock fucking me from the other side of the wall. I don't care that he is paying me and isn't the first, I just want to enjoy.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("With each trust some cum leaks out of me as he starts making me feel good.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("I love the feeling of one man's cum leaking out of my arse while another man fucks me wanting to fill me up even more.", If(player.cum_locations["cum_assin"] and player.has_perk(perk_buttslut), 100, 0)),
    ("I'm really horny so I furiously hump at his cock while masturbating, hoping I can get off before him.", If(player.check_horny(extreme=True), 100, 0)),
    ("I am fairly excited so I enjoy pressing back against his cock all while masturbating to have more fun.", If(player.check_horny(), 100, 0)), 
    ("I drunkenly hump against him while trying to keep balance all while my fingers rub between my legs.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I can barely stay on my feet as I press myself against the wall trying to hum at his cock.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I keep a decent pace as I hump at the guy sticking his cock in the hole.",100),
    ("I press his cock deep into me and keep humping to get him off.",100),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Mmm. I don't care that you are paying me, maybe you can fill me up even more. Fuck me.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("Fuck yes, take turns to put more cum in me you dirty perverts. People before you filled me up so maybe you will too?", If(player.cum_locations["cum_assin"], 100, 0)),
    ("Fuck! Paying me to give me what I want. Full my arse full of your cum you dirty pervert. You and the others before you.", If(player.cum_locations["cum_assin"] and player.has_perk(perk_buttslut), 100, 0)),
    ("Yes! Pay for getting me off. Spank me and call me a bitch! \u2665", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa yes. Having to pay someone through a hole to get off? I don't care, I am horny so fuck me!", If(player.check_horny(), 100, 0)), 
    ("Hmmm come on. Fuck me and make me feel good.", If(not player.check_horny(), 100, 0)),
    ("Ah fuck! Yes keep going! I want to fuck you and all the people after you! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Ah fuck yes!",100),
    ("Keep going, keep fucking me!",100),
    ("Ah yes, fuck it deep in me!",100),
    ])
    pcm "[dialouge]"
    jump expression WeightedChoice([
    ("gloryhole_sex_anal_cum",100),
    ("gloryhole_sex_anal_picker",250),
    ])

label gloryhole_sex_anal_picker:
    $ having_sex(3)
    jump expression WeightedChoice([
    ("gloryhole_sex_anal_close", If (not renpy.showing("gh_blow_close"), 100, 0)), 
    ("gloryhole_sex_anal_stand", If (not renpy.showing("gh_blow_behind sex_stand"), 100, 0)), 
    ("gloryhole_sex_anal_up", If (not renpy.showing("gh_blow_behind sex_up"), 100, 0)), 
    ("gloryhole_sex_anal_down", If (not renpy.showing("gh_blow_behind sex_down"), 100, 0)), 
    ])

label gloryhole_sex_anal_close:
    $ renpy.scene()
    show gh_blow_close asssex
    with dissolve
    $ dialouge = WeightedChoice([
    ("I rock back and forth on the cock up my arse while using the cum from someone else leaking out my vagina as lube to get myself off.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I hump the cock poking out of the wall while playing with the cum that is leaking out of me.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I love that I have both someone's cum and a cock inside me. So I rock as the cock inside me while rubbing myself off using cum as lube.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("I hump the cock up my arse and hear the squelching sound of cum leaking out as he fucks me while I use the cum leaking out my vagina as lube to get myself off.", If(player.cum_locations["cum_vagin"] and player.cum_locations["cum_assin"], 100, 0)),
    ("I have cum leaking out of both holes as I hump his cock and rub the cum leaking out of my vagina all over my lips while mastubating.", If(player.cum_locations["cum_vagin"] and player.cum_locations["cum_assin"], 100, 0)),
    ("I'm really horny so I furiously hump at his cock while masturbating, hoping I can get off before him.", If(player.check_horny(extreme=True), 100, 0)),
    ("I am fairly excited so I enjoy pressing back against his cock all while masturbating to have more fun.", If(player.check_horny(), 100, 0)), 
    ("I drunkenly hump against him while trying to keep balance all while my fingers rub between my legs.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I can barely stay on my feet as I press myself against the wall trying to hum at his cock.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I keep a decent pace as I hump at the guy sticking his cock in the hole.",100),
    ])
    "[dialouge]"

    jump gloryhole_sex_anal_cycle

label gloryhole_sex_anal_stand:
    $ renpy.scene()
    show gh_blow_behind sex_stand
    with dissolve
    $ dialouge = WeightedChoice([
    ("I arch my back and cum leaks out of my arse as I press against him deep inside me.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("I stand up and moan at the feeling of cum leaking out of my pussy as his cock thrusts inside my arse ready to fill another hole.", If(player.cum_locations["cum_vagin"] and not player.cum_locations["cum_assin"], 100, 0)),
    ("I stand up feel cum leaking out of my pussy as he fucks my arse. His cock keeping the cum in there plugged inside me.", If(player.cum_locations["cum_vagin"] and player.cum_locations["cum_assin"], 100, 0)),
    ("I stand and play with my tits while enjoying the feeling of his cock stretching my arsehole as he fucks me.", If(player.check_horny(extreme=True), 100, 0)),
    ("I stand and enjoy the feeling of being ass fucked while I play with my tits to make it feel even nicer.", If(player.check_horny(), 100, 0)), 
    ("I let him do most of the work as I stand there and just feel him pistoning inside me.", If(not player.check_horny(), 100, 0)),
    ("I try to stay upright to keep my balance and almost forget I have a cock fucking me.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I can barely keep on my feet so I just press my arse against the hole letting him do all the work while I try not to fall over.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I stand and rock against the cock that is sticking inside me from the other side of the wall.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_anal_cycle

label gloryhole_sex_anal_up:
    $ renpy.scene()
    show gh_blow_behind sex_up
    with dissolve
    $ dialouge = WeightedChoice([
    ("I hold onto the opposite wall and use that as a springboard to furiously fuck his cock while I can barely contain my moans.", If(player.check_horny(extreme=True), 100, 0)),
    ("I use the opposite wall as leverage to help bounce on the cock that is inside me.", If(player.check_horny(), 100, 0)), 
    ("I use the wall opposite to help me with momentum while bouncing on the cock sticking out of the hole.", If(not player.check_horny(), 100, 0)),
    ("I hold onto the other wall for balance and use it to press my arse firmly against the hole, giving him easy access to keep fucking me.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I rest against the wall to keep myself upright and just hope the guy behind me is happy to do most of the work.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I use the wall in front of me to help me rock back and forth on his cock.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_anal_cycle

label gloryhole_sex_anal_down:
    $ renpy.scene()
    show gh_blow_behind sex_down
    with dissolve
    $ dialouge = WeightedChoice([
    ("I put my hand on the floor and present myself like a bitch on heat, making sure he put his cock as deep inside me as he can.", If(player.check_horny(extreme=True), 100, 0)),
    ("I bend over, making sure he has as easy access as possible to keep fucking and making me feel good.", If(player.check_horny(), 100, 0)), 
    ("I try to balance myself on the floor while giving him easy access to fuck my arse.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I drunkenly stumble and have to hold onto the floor to stop myself from entirely falling over. Though I am not sure the guy behind the wall even notices.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I stick my ass in the air to give as easy access as possible for the guy who is inside me.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_anal_cycle

label gloryhole_sex_anal_cum:
    if numgen():
        jump gloryhole_sex_anal_cum_inside
    else:
        jump gloryhole_sex_anal_cum_pullout

label gloryhole_sex_anal_cum_inside:
    $ dialouge = WeightedChoice([
    ("I can feel he is about to cum so I keep humping him so he can put more cum inside me.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("He is close to cumming and I keep humping him so he can fill me up just like someone before has done.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("I make no effort to pull him out of me, glad that he will be cumming up my arse and not able to make me pregnant.", If(player.has_perk(perk_preg_notwant) and not player.preg_knows, 100, 0)),
    ("I keep riding him like a bitch, letting him fuck and cum up my arse.", If(player.check_horny(extreme=True), 100, 0)),
    ("I bend over, making sure he has as easy access as possible to keep fucking and fill my arse with his cum.", If(player.check_horny(), 100, 0)), 
    ("I keep bouncing on his cock waiting to feel him pumping inside me.", If(not player.check_horny(), 100, 0)),
    ])
    "[dialouge]"
    $ player.sex_cum(ghman, "anal", quest_gloryhole)
    $ dialouge = WeightedChoice([
    ("Ah yes yes yes! Keep fucking me!", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa yes. Fuck that feels good!", If(player.check_horny(), 100, 0)), 
    ("Ahhh yes. Cum in the dirty slut letting you fuck me through a hole in the wall! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Yes. Fill the whore you fuck paid to assfuck! \u2665", If(player.has_perk(perk_whore), 100, 0)),
    ("Ha yes!",100),
    ("Haaaa...",100),
    ("\u2665 \u2665",100),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("*Phew*",100),
    ("*Huff* *Huff*",100),
    ("Oooohh...",100),
    ("Mmmm...",100),
    ])
    pc "[dialouge]"
    if renpy.showing("gh_blow_behind sex_down"):
        show gh_blow_behind sex_up with dissolve
    if renpy.showing("gh_blow_behind sex_up"):
        show gh_blow_behind sex_stand with dissolve
    if renpy.showing("gh_blow_close"):
        show gh_blow_close vagpoke with dissolve
    $ dialouge = WeightedChoice([
    ("Haaa...",100),
    ("Mmmmm...",100),
    ("Ooooh yes...",100),
    ("Ung fuck",100),
    ("\u2665",100),
    ])
    pc "[dialouge]"
    if renpy.showing("gh_blow_behind"):
        show gh_blow_behind no_man_hole with dissolve
    else:
        show gh_blow_close no_pc with dissolve
        show gh_blow_close no_man_hole with dissolve
    $ dialouge = WeightedChoice([
    ("His cock softens and slips out my arse followed by a pop and cum leaking out of me.",100),
    ("He pulls out of my arse with his cum leaking down my leg.",100),
    ("The guy pulls his cock from me and the hole and I am left standing there feeling his cum leak out of me.",100),
    ])
    "[dialouge]"
    pcm "..."
    jump gloryhole_end

label gloryhole_sex_anal_cum_pullout:
    $ renpy.scene()
    show gh_blow_close asssex
    with dissolve
    show gh_blow_close asspoke with dissolve
    $ dialouge = WeightedChoice([
    ("I can feel the guy is about to blow, so I pull him out of me so he can't add to what is already leaking out of me.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("I can feel his is about to cum so I pull him out and hump against him so I can feel him cum over my arse.", If(player.check_horny(extreme=True), 100, 0)),
    ("He is about to cum so I pull him out of my but keep masturbating so I can push myself over the edge...", If(player.check_horny(), 100, 0)), 
    ("He is not far off so I pull him out of me and rum against him to get the job done.", If(not player.check_horny(), 100, 0)),
    ("I pull him out of me and wait to feel his warmth as he cums against me.",1),
    ])
    "[dialouge]"
    $ player.sex_cum(ghman, "ass", quest_gloryhole)
    $ dialouge = WeightedChoice([
    ("He pumps his cum against my arsehole, making it even more wet than before. Multiple guys on me, both inside and out have now marked me.", If(player.cum_locations["cum_assin"], 100, 0)),
    ("I feel him warm cum squirting against me and running down my arse and between my legs. I am so horny I would let him get back inside and have another go.", If(player.check_horny(extreme=True), 100, 0)),
    ("I feel his warm cum hit my bum as I am still rubbing myself off.", If(player.check_horny(), 100, 0)), 
    ("I eventually feel his cum hitting against me with some muffled moans from the other side of the wall.", If(not player.check_horny(), 100, 0)),
    ("I feel his warm cum hit me and start running down my ass and legs.",1),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Ha fuck that felt good. Still horny as shit though so maybe I should give someone else a go?", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa yes. Fuck that felt good!", If(player.check_horny(), 100, 0)), 
    ("Ahhh yes. Cum all over the dirty slut letting you fuck me through a hole in the wall! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Yes. Cum on the dirty whore you fuck paid to fuck! \u2665", If(player.has_perk(perk_whore), 100, 0)),
    ("Ha yes!",100),
    ("Haaaa...",100),
    ("\u2665 \u2665",100),
    ])
    pcm "[dialouge]"
    jump gloryhole_end





label gloryhole_sex_blow_start:
    $ renpy.scene()
    show gh_blow_close lick
    with dissolve
    $ dialouge = WeightedChoice([
    ("I get on my knees and start slobbering all over his cockhead wondering if I should have instead bent over for him.", If(player.check_horny(extreme=True), 100, 0)),
    ("I take his cock in my hand and start licking his head all over. Wouldn' mind getting off myself but at least one of us will.", If(player.check_horny(), 100, 0)), 
    ("Still having the taste of the last cock in my mouth, I eagerly take this new one in my hands and start licking it all over.", If(player.cum_locations["cum_mouth"], 100, 0)),
    ("The cum all over my face from the last guy does little to slow me from taking this new cock in my hands and giving it a taste.", If(player.cum_locations["cum_face"], 100, 0)),
    ("I get on my knees and take his cock in my hand and start to wank him off while licking at his tip.", 100),
    ])
    "[dialouge]"
    $ player.sex_oral(ghman, quest_gloryhole)
    $ dialouge = WeightedChoice([
    ("Mmmm, so warm...",100),
    ("Ooh, he's as hard as a rock.",100),
    ("Hmm not bad. Feels quite nice in my hand.",100),
    ("Mmm, ready for some fun are you?",100),
    ("Looks like you have been waiting for this for a while.",100),
    ])
    pcm "[dialouge]"
    if numgen():
        show gh_blow_close suck with dissolve
        $ dialouge = WeightedChoice([
        ("*Hyuk*",100),
        ("Mmmmmmff...",100),
        ("*Slurp*",100),
        ("*Ug* *Ug*",100),
        ("\u2665",100),
        ])
        pc "[dialouge]"
        $ dialouge = WeightedChoice([
        ("I put my tongue under his cock and slide my lips down his shaft until I can feel him hitting the back of my mouth and unable to go any deeper. \u2665", If(player.check_horny(extreme=True), 100, 0)),
        ("I put my lips around his cock and put him deep in my mouth, bobbing up and down as I fuck his cock with my face.", 100), 
        ("I put his cock as deep into my mouth as I can and suppresing my gag reflex as it enters my troat.", If(player.has_perk(perk_slut), 100, 0)),
        ("I eagerly press my face down against his cock and relax as he hits the back of my troat.", If(player.has_perk(perk_slut), 100, 0)),
        ("I wrap my lips deep down his shaft and lick him all around from inside my mouth making is cock nice and wet for bobbing on his cock.",100),
        ])
        "[dialouge]"
    else:
        $ dialouge = WeightedChoice([
        ("Ready for me?",100),
        ("Mmm, tasty...",100),
        ("*Slurp*",100),
        ("Oooh nice.",100),
        ("\u2665",100),
        ])
        pc "[dialouge]"
        $ dialouge = WeightedChoice([
        ("I lick all over his cock while also playing with the cum that is still in my mouth that I havent swallowed yet.", If(player.cum_locations["cum_mouth"] > 5, 100, 0)),
        ("I kiss and lick the tip of his cock, getting a new taste from the one already in my mouth from the previous guy cumming there.", If(player.cum_locations["cum_vagin"] > 10, 100, 0)),
        ("I eagerly lick and slobber all over his cock while wanking him off, ready to make him squirt himself over my face.", If(player.check_horny(extreme=True), 100, 0)),
        ("I wank him off while licking him all over, knowing soon I will be tasting what will come out of it and swallow it all down.", If(player.check_horny(), 100, 0)), 
        ("I kiss and lick his cock wondering what this guys cum will taste like", If(player.has_perk(perk_slut), 100, 0)),
        ("I lick and kiss all over his throbbing cock, responding to the moans I hear muffled from the other side of the wall!",100),
        ("I lick all over his helmet and kiss it all over, making it nice and wet for putting deep in my mouth and bobbing on his cock.",100),
        ])
        "[dialouge]"

    jump gloryhole_sex_blow_picker

label gloryhole_sex_blow_cycle:
    $ dialouge = WeightedChoice([
    ("Ah fucking hell. I am leaking from my arse and pussy and now you want to cum in my mouth as well. Fuck give it to me!", If(player.cum_locations["cum_vagin"] and player.cum_locations["cum_assin"] and not player.cum_locations["cum_mouth"], 100, 0)),   
    ("Haa fuck. Cum in my pussy and a cock in my mouth ready to give me a taste.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("Mmm... Wonder if he realises it's not lube I am using but cum from one of the guys before.", If(player.cum_locations["cum_hand"], 100, 0)),
    ("Mmmm, are you as horny as I am you pervert? Cum all over me and let me drink it all up. \u2665", If(player.check_horny(extreme=True), 100, 0)),
    ("Mmm your cock is so nice in my mouth. Give it to me and let me swallow what comes out.", If(player.check_horny(), 100, 0)), 
    ("Getting fucked is nice but being on my knees sucking a guy off is something special. \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Mmm give me your cock. Deep in my mouth and let me taste it.",100),
    ("AH so nice sucking on this, I can feel every vein and bulge just using my tongue.",100),
    ])
    pcm "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I get to work pleasing his cock and sometimes rubbing myself between my legs. I am quickly reminded of the last guy I fucked when I feel I am still leaking and rubbing his cum around.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I please his cock while touching myself and playing with the cum that is leaking out from between my legs.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I'm really horny go to town on his cock, imagining how much nicer if he were instead thrusting inside me and also getting me off.", If(player.check_horny(extreme=True), 100, 0)),
    ("I am fairly excited and am getting off on having fun with his cock.", If(player.check_horny(), 100, 0)), 
    ("I drunkenly slobber over his cock and am pretty sure he's enjoying, despite my clumsyness.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I can barely focus as I work his cock. My head is spinning from the booze but I still try to get the guy off.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I lick and suck on the guy's cock making sure he gets his moneys worth.",100),
    ("I work his cock with my hands and my mouth, making sure he enjoying himself.",100),
    ])
    "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Mmm, fuck what I wouldn;t give to have you return the favour and make me feel nice. Should I stick my pussy against the hole instead? \u2665", If(player.check_horny(extreme=True), 100, 0)),
    ("Haaa yes. Having to pay someone through a hole to get off? I don't care, I am horny so give me your cock!", If(player.check_horny(), 100, 0)), 
    ("Ah fuck! Give me your cock. Let me show you that people don't call me a slut for no reason! \u2665", If(player.has_perk(perk_slut), 100, 0)),
    ("Mmmm. Does it feel different having a pregnant girl sicking your cock?", If(player.preg_knows, 100, 0)),
    ("Ahh fuck. Does a pervert like you get off knowing that one of the cocks from this hole is what gave me a fat belly?", If(player.preg_knows and player.preg_father_class == ghman, 100, 0)),
    ("Haaaaa. Fuck! Enjoying this pregnant whore sucking on your cock?", If(player.preg_knows and player.soldbaby, 100, 0)),
    ("Ah fuck yes!",100),
    ("Mmmmmmm!",100),
    ("Ah yes, so tasty!",100),
    ])
    pcm "[dialouge]"
    jump expression WeightedChoice([
    ("gloryhole_sex_blow_cum",100),
    ("gloryhole_sex_blow_picker",250),
    ])

label gloryhole_sex_blow_picker:
    $ having_sex(3)
    jump expression WeightedChoice([
    ("gloryhole_sex_blow_lick", If (not renpy.showing("gh_blow_close lick"), 100, 0)), 
    ("gloryhole_sex_blow_suck", If (not renpy.showing("gh_blow_close suck"), 100, 0)), 
    ("gloryhole_sex_blow_behind", If (not renpy.showing("gh_blow_behind suck"), 100, 0)), 
    ])

label gloryhole_sex_blow_lick:
    $ renpy.scene()
    show gh_blow_close lick
    with dissolve
    $ dialouge = WeightedChoice([
    ("I hold his cock in one hand while my other reaches between my legs and uses the cum leaking of to masturbate. My tounge licking his cockhead all over", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I use my tongue to lick the head of his cock all over while my hand furiously wanks him off.", If(player.check_horny(extreme=True), 100, 0)),
    ("I wank him off while enjoying the feel of his cock on my tongue while I lick and kiss him all over", If(player.check_horny(), 100, 0)), 
    ("I hold onto his cock and swirl by tounge all over his cock, drooling and slobbering as I do so in a drunkern stupor.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I barely even know what I am doing as I pump my hand on his cock and lick it all over. Mostly trying not to pass out or puke.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I work my tongue over his cockhead and hope that he's enjoying himself.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_blow_cycle

label gloryhole_sex_blow_suck:
    $ renpy.scene()
    show gh_blow_close suck
    with dissolve
    $ dialouge = WeightedChoice([
    ("I bob my head on his cock along with the rythmn of him face fucking me while I press my fingers between my legs, getting myself off.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I press my face against the hole, letting him facefuck me while I masturbate to the feeling of the last guy to fucked me and filled me with his cum.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("I excitedly bounce my head over his cock and fuck it with my mouth, slobbering and drooling away the entire time.", If(player.check_horny(extreme=True), 100, 0)),
    ("I fuck his cock with my lips, wanting for the pleasant taste of his precum to let me know I am going to me swallowing up his warmth.", If(player.check_horny(), 100, 0)), 
    ("I mostly go through the motions of bounching my head on his cock while he meets my momentum and trusts into me.", If(not player.check_horny(), 100, 0)),
    ("I bob my head on his cock, trying not to gag or puke from all the booze I have drunk. With his cock hitting the back of my mouth this is not make easy.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I drunkernly bounce my face on his cock. I barely know what I am up to but just hope that a pervert like him doesn't really care and just uses my mouth for his pleasure.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I wrap my lips around him and bring them down to his shaft. Then start to bob my head back and forth, fucking his cock with my lips.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_blow_cycle

label gloryhole_sex_blow_behind:
    $ renpy.scene()
    show gh_blow_behind suck
    with dissolve
    $ dialouge = WeightedChoice([
    ("I bob my head on his cock along with the rythmn of him face fucking me while I press my fingers between my legs, getting myself off.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("I press my face against the hole, letting him facefuck me while I masturbate to the feeling of the last guy to fucked me and filled me with his cum.", If(player.cum_locations["cum_vagin"] and player.has_perk(perk_creampie_lover), 100, 0)),
    ("I excitedly bounce my head over his cock and fuck it with my mouth, slobbering and drooling away the entire time.", If(player.check_horny(extreme=True), 100, 0)),
    ("I fuck his cock with my lips, wanting for the pleasant taste of his precum to let me know I am going to me swallowing up his warmth.", If(player.check_horny(), 100, 0)), 
    ("I mostly go through the motions of bounching my head on his cock while he meets my momentum and trusts into me.", If(not player.check_horny(), 100, 0)),
    ("I bob my head on his cock, trying not to gag or puke from all the booze I have drunk. With his cock hitting the back of my mouth this is not make easy.", If(player.has_perk(perk_wasted), 100, 0)),
    ("I drunkernly bounce my face on his cock. I barely know what I am up to but just hope that a pervert like him doesn't really care and just uses my mouth for his pleasure.", If(player.has_perk(perk_blackout), 100, 0)),
    ("I wrap my lips around him and bring them down to his shaft. Then start to bob my head back and forth, fucking his cock with my lips.",1),
    ])
    "[dialouge]"
    jump gloryhole_sex_blow_cycle

label gloryhole_sex_blow_cum:
    if numgen():
        $ if_showing("gh_blow_behind", "suck", "gh_blow_close", "cum")
        $ dialouge = WeightedChoice([
        ("I feel the yummy taste him about to cum so I pull him out and start wanking him off so I can have him cum all over my mouth and lips.", If(player.check_horny(extreme=True), 100, 0)),
        ("I feel the taste of him starting to leak so I wank him off while licking the end of his cock.", If(player.check_horny(), 100, 0)), 
        ("A familiar taste enters my mouth so I start to wank him off so he can mark my face like so many before have done.", If(player.has_perk([perk_slut, perk_whore]), 100, 0)), 
        ("It sounds like he is about to cum so I start wanking him off waiting for him to unload on my face.", 100),
        ("His cock stiffens and from his movements I can tell he is close. So I start licking the tip of his cock while wanking him off.", 100),
        ])
        "[dialouge]"
        $ player.sex_cum(ghman, "face", quest_gloryhole)
        $ dialouge = WeightedChoice([
        ("Ah yes all over me. Cover my face in it!", If(player.check_horny(extreme=True), 100, 0)),
        ("Mmm yes. Cover me with your cum!", If(player.check_horny(), 100, 0)), 
        ("Fuck yes. Cum all over my slutty lips and let me lick it all up afterwards! \u2665", If(player.has_perk(perk_slut), 100, 0)),
        ("Yes. Get your moneys worth and cover me with it all! \u2665", If(player.has_perk(perk_whore), 100, 0)),
        ("Ha yes!",100),
        ("Haaaa...",100),
        ("\u2665 \u2665",100),
        ])
        pcm "[dialouge]"
    else:
        $ if_showing("gh_blow_behind", "suck", "gh_blow_close", "suck")
        $ dialouge = WeightedChoice([
        ("I feel the yummy taste him about to cum but make no effort to get him out my mouth. I want him to unload while I suck him and swallow everything he has.", If(player.check_horny(extreme=True), 100, 0)),
        ("I feel the taste of him starting to leak so make sure to keep my head against the hole and let him face fuck me though it just waiting to feel him cumming.", If(player.check_horny(), 100, 0)), 
        ("A familiar taste enters my mouth so I press my head against the wall letting him fuck my face deeper.", If(player.has_perk([perk_slut, perk_whore]), 100, 0)), 
        ("It sounds like he is about to cum so I pick up the pace and bob up and down on his cock even faster.", 100),
        ("His cock stiffens and from his movements I can tell he is close. I just keep bobbing my head on his cock until I can feel it.", 100),
        ])
        "[dialouge]"
        $ player.sex_cum(ghman, "mouth", quest_gloryhole)
        $ dialouge = WeightedChoice([
        ("Come on. Let me taste and swallow it all up!", If(player.check_horny(extreme=True), 100, 0)),
        ("Mmm yes. Let me taste your cum!", If(player.check_horny(), 100, 0)), 
        ("Fuck yes. Cum in my slutty mouth and drink it all up it all! \u2665", If(player.has_perk(perk_slut), 100, 0)),
        ("Yes. Get your moneys worth and make me swallow it! \u2665", If(player.has_perk(perk_whore), 100, 0)),
        ("Ha yes!",100),
        ("Haaaa...",100),
        ("\u2665 \u2665",100),
        ])
        pcm "[dialouge]"

    if not renpy.showing("gh_blow_close cum"):
        $ renpy.scene()
        show gh_blow_close cum
        with dissolve
    $ dialouge = WeightedChoice([
    ("*Phew*",100),
    ("*Huff* *Huff*",100),
    ("Oooohh...",100),
    ("Mmmm...",100),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("I keep wanking at this cock making sure he gets everything out and is satisfied.",100),
    ("I keep wanking his cock to make sure he is satisfied and eventually e starts to soften and pulls back into the hole.",100),
    ("I keep going making sure he is done. He quickly starts to soften and disappears back into the hole.",100),
    ("I keep wanking him off until he starts of get soft and seemingly satisfied he pulls back into the hole.",100),
    ])
    "[dialouge]"
    if renpy.showing("gh_blow_behind"):
        show gh_blow_behind no_man_hole with dissolve
    else:
        show gh_blow_close no_pc with dissolve
        show gh_blow_close no_man_hole with dissolve
    jump gloryhole_end





label gloryhole_end:
    $ renpy.scene()
    show gh_blow_behind idle no_man_hole
    with dissolve
    if loc_from.closed():
        jump gloryhole_end_closed
    if player.tired < 20:
        jump gloryhole_end_tired
    $ dialouge = WeightedChoice([
    ("Should I knock again for someone else? Hope they don't mind I am leaking though.", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("Should I knock again? My pussy feels flooded with cum though so maybe I should just suck on them.", If(player.cum_locations["cum_vagin"] > 10, 100, 0)),
    ("I love it when guy's cum in me, but at this rate I am going to end up a cum balloon. Maybe I should suck off the next guy.", If(player.cum_locations["cum_vagin"] > 10 and player.has_perk(perk_creampie_lover), 100, 0)),
    ("Should I knock again even though I am leaking out of both holes?", If(player.cum_locations["cum_vagin"] and player.cum_locations["cum_assin"], 100, 0)),
    ("I'm still horny as shit and want to have fun. Should I knock again?", If(player.check_horny(extreme=True), 100, 0)),
    ("I'm still kind of excited. Wonder if I should have another go.", If(player.check_horny(), 100, 0)), 
    ("Hmm, should I knock again and wait for someone else to come?", If(not player.check_horny(), 100, 0)),
    ("Oooh staying on my feet is hard. Should I go away or wait for someone else?", If(player.has_perk(perk_wasted), 100, 0)),
    ("Ubb. Uggh... This is tough getting these cocks off when I can barely think...", If(player.has_perk(perk_blackout), 100, 0)),
    ("Washing this booze down with cum might not be the greatest idea I've ever had.", If(player.drunk > 50 and player.cum_locations["cum_mouth"], 100, 0)),
    ("Hmm, should I knock and wait for another customer?",100),
    ("Should I go for another customer?",100),
    ])
    pcm "[dialouge]"
    jump gloryhole_end_choice

label gloryhole_end_closed:
    pcm "The place is closing so I had better clean up and leave..."
    if c.outfit == 6:
        $ renpy.scene()
        with dissolve
        $ pc_dress_slow()
        $ walk(loc_from)
        $ walk(loc_pub)
        jump pub_waitress_work_home
    else:
        jump gloryhole_dress_leave

label gloryhole_end_tired:
    $ dialouge = WeightedChoice([
    ("I am flooded inside and ready to pass out. I think I should call it a day.", If(player.cum_locations["cum_vagin"] > 10, 100, 0)),
    ("As much as I want ore cum in me, I think I had better sleep first.", If(player.cum_locations["cum_vagin"] > 10 and player.has_perk(perk_creampie_lover), 100, 0)),
    ("Leaking everywhere and ready to pass out. I think I am done for now.", If(player.cum_locations["cum_vagin"] and player.cum_locations["cum_assin"], 100, 0)),
    ("Ugh, Maybe I should go and sleep off this booze.", If(player.has_perk(perk_wasted), 100, 0)),
    ("Ubb. I am ready to pass out...", If(player.has_perk(perk_blackout), 100, 0)),
    ("I'm falling asleep here so think I am done for now",100),
    ("I am exhausted. I think I should call it a day.",100),
    ])
    pcm "[dialouge]"
    if inv.qty(item_wakeup):
        menu:
            "Take some wake up":
                call item_wakeup_action from _call_item_wakeup_action_2
                jump gloryhole_end_choice
            "Call it a night":

                $ NullAction()
    if c.nude:
        jump gloryhole_dress_leave
    if c.outfit == 6:
        $ renpy.scene()
        with dissolve
        $ pc_dress_slow()
        $ walk(loc_from)
        $ walk(loc_pub)
        jump pub_waitress_work_home

label gloryhole_end_nocust:
    if loc_from.closed():
        jump gloryhole_end_closed
    if player.tired < 20:
        jump gloryhole_end_tired

    $ dialouge = WeightedChoice([
    ("Standing here waiting while these guys leak down my leg...", If(player.cum_locations["cum_vagin"], 100, 0)),
    ("Starting to get a belly ache with the amount inside me. Maybe I should call it a day?", If(player.cum_locations["cum_vagin"] > 10, 100, 0)),
    ("No one wanting to add to the cum that's inside my belly? Come on.", If(player.cum_locations["cum_vagin"] > 10 and player.has_perk(perk_creampie_lover), 100, 0)),
    ("Standing here waiting while my ass and pussy are leaking is maybe not such a good idea...", If(player.cum_locations["cum_vagin"] and player.cum_locations["cum_assin"], 100, 0)),
    ("Come on! I am horny as shit and no one is coming?", If(player.check_horny(extreme=True), 100, 0)),
    ("Standing here all horny and no one wants to join?", If(player.check_horny(), 100, 0)), 
    ("Come on... I could be off drinking more beer instead of standing here like an idiot.", If(player.has_perk(perk_wasted), 100, 0)),
    ("Ubb. Maybe I should sleep instead of standing here like a drunk idiot.", If(player.has_perk(perk_blackout), 100, 0)),
    ("No one is joining me. Should I still wait?",100),
    ("Hmm, should I keep waiting?",100),
    ])
    pcm "[dialouge]"
    jump gloryhole_end_choice

label gloryhole_end_choice:
    menu:
        "Knock again":
            jump gloryhole_wait
        "Get dressed and leave" if c.nude or ("work" in tab_top and not c.outfit == 6 and dis(dis_pub)):
            jump gloryhole_dress_leave
        "Head back into the pub" if "work" in tab_top and c.outfit == 6 and dis(dis_pub):
            $ renpy.scene()
            with dissolve
            $ pc_dress_slow()
            $ walk(loc_from)
            $ walk(loc_pub)
            jump pub_waitress_work_picker

label gloryhole_dress_leave:
    $ renpy.scene()
    with dissolve
    $ pc_dress_slow()
    $ walk(loc_from)
    if player.cum_visible:
        pcm "I am covered in cum so should probably wash up first."
    elif player.hygiene < 25:
        pcm "I am starting to smell so maybe I should wash before leaving."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
