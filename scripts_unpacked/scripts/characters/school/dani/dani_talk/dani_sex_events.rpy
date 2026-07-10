label dani_sex_bedroom_picker:
    show dani happy at right5 with dissolve
    if not dani.want_sex():
        dani.name "Eager are we? We just messed around."
        pc "I know..."
        if not numgen(0,2) and not player.check_horny(extreme=True):
            pcm "Maybe I should calm down a bit..."
            hide dani with dissolve
            jump travel
        pc "Not going to let that stop me."
        dani.name "Oh?"
    else:
        pc "Mmm, how about a little bit of fun?"
        dani.name "Oooh."
    hide dani
    show dani_kiss
    with dissolve
    dani.name "Mmm..."
    $ dani_yan_remove(numgen(1,6))
    call dani_sex_bedroom_kissing_undress_call from _call_dani_sex_bedroom_kissing_undress_call

    $ player.sex_les(dani)

    jump expression WeightedChoice([

    
    ("dani_sex_bedroom_bentover_lick", 100),
    ("dani_sex_bedroom_laykissing", 100),
    ("dani_sex_bedroom_mast", 100),

    
    ("dani_sex_bedroom_bentover_strapon", If(dani.lust >= 50 and dani_yan_value() >= 70 and dani.dict["strapon_sex"], 300, 0)),
    ("dani_sex_bedroom_onback_strapon", If(dani.lust >= 50 and dani_yan_value() >= 70 and dani.dict["strapon_sex"], 300, 0)),
    ])

label dani_sex_bedroom_bentover_lick:
    "[dani.nname] kisses me for a bit and then pushes me onto the bed."
    hide dani_kiss
    show sb_bentover head_down
    with hpunch
    show sb_bentover head_up back worried oh with dissolve
    pc "Ohh?"
    pc "What are you up to you pervert?"
    show sb_bentover dani_lick ooh forward straight with dissolve
    pc "Oooh fuck! That's what you want to do?"
    $ player.spank()
    pc "Ah!"
    show sb_bentover head_down with dissolve
    pc "Fucking hell. Ah shit."
    "I stay there, ass in the air with my head in the pillow feeling what [dani.nname] is doing behind me."
    "She doesn't seem just content with one of my holes and tries to lick or stick her tongue in either one."
    "It doesn't feel bad, so I relax and let her do what she wants."
    show sb_bentover head_up back ooh with dissolve
    pc "Ah fuck, you are going to make me..."
    $ player.spank()
    pc "Haa!"
    show sb_bentover head_up closed ag with dissolve
    $ player.sex_cum(dani)
    pc "Ahhhhhhh!"
    pc "Fuck!"
    $ player.spank()
    pc "Huuuu..."
    show sb_bentover no_dani back oh worried with dissolve
    pc "Haa, you finished back there."
    dani.name "Yup, just admiring the view now."
    pc "Well, enjoy it."
    "I wiggle my ass for [dani.nname], then roll over and lay down."
    hide sb_bentover
    show sb_onback relaxed look_up neutral
    with dissolve
    jump dani_sex_bedroom_sex_end_nostrap

label dani_sex_bedroom_laykissing:
    hide dani_kiss
    show sb_laykiss
    with dissolve
    "She presses against me and we both fall onto the bed as we continue to kiss me."
    pc "Mmmmm.."
    dani.name "[rlist.dani_sex_comment_breasts]"
    show sb_laykiss closed with dissolve
    "Her hands are all over me, pressing me close as she kisses me more aggressively and I can feel her rubbing her body against mine."
    "I relax and go along with it. Enjoying her hands roaming all over my body, rubbing my tits while she presses her thigh between my legs."
    "I am getting pretty excited with all this, and it seems so is [dani.nname] because she starts to reposition herself."
    hide sb_laykiss
    show sb_scissoring
    with dissolve
    pc "Oh?."
    dani.name "You sexy girl."
    pc "Dunno, but I think I'm about to find out."
    "We both rub ourselves against each other and I slip my hand down between my legs to rub myself."
    "[dani.nname] starts to do the same and we both lay there pleasuring ourselves and each other."
    show sb_laykiss closed
    hide sb_scissoring
    with dissolve
    dani.name "This is so much more fun than the usual pervert."
    pc "Mmmm."
    "We kiss, touch each other and enjoy the moment."
    "We both start to breathe much heavier as we rub against each other, hands between our legs and getting ourselves off."
    "[dani.nname] kisses me way more aggressively and deeper, less of a kiss and more of a tongue invading every part of my mouth."
    "And not just my mouth, she licks my lips, nibbles on my ear and tries to press as much of her skin against mine as possible."
    dani.name "Haa fuck this is so much fun."
    "She pushes her tongue deep into my mouth while breathing heavily an bucks her hips against me."
    dani.name "Ha fuck I am going to cum."
    pc "Mmm, pervert. Do it."
    "We both rub ourselves more as we kiss and she presses herself against me."
    $ player.sex_cum(dani)
    dani.name "Mmmmmm..."
    pc "Ahhh thats nice."
    dani.name "I could get used to this."
    jump dani_sex_bedroom_sex_end_nostrap

label dani_sex_bedroom_mast:
    hide dani_kiss
    show sb_onback dani_kiss
    with dissolve
    "We move over to the bed and lay down kissing."
    dani.name "Mmmm."
    dani.name "You are so sexy."
    show sb_onback dani_lay_mast look_right mast relaxed dani_smile with dissolve
    dani.name "[rlist.dani_sex_comment_breasts]"
    show sb_onback neutral
    pc "Mmm, being a dirty girl?"
    dani.name "With you, of course."
    "We lay there kissing and telling each other dirty things while we both touch ourselves."
    dani.name "It's so fun with you being in bed with me."
    pc "Better than the usual dirty pervert."
    dani.name "Just a bit."
    if numgen() and not player.showing:
        dani.name "Mmm, I know..."
        show sb_onback look_up no_dani with dissolve
        pc "Going to do a dance for me?"
        dani.name "No."
        show sb_onback dani_facesit with dissolve
        dani.name "No need to use my hand when you have a mouth."
        pc "Mmmmfff..."
        "[dani.nname] presses herself against my face, pretty much humping it without much care if I can breathe."
        "It's fun, so I lick her when I can, and try and put my tongue inside her."
        "It's hard to do get any rhythm because she is doing whatever the ell she wants. Humping, pressing, groping me..."
        "I lay there just masturbating and trying to catch a breath now and then."
        pc "Mmmmff."
        "I am brining myself to climax, still not able to breathe or say anything to [dani.nname]."
        "Not that it matters. She is having her own fun."
        pc "Mmmmffff mmmmmmmmm."
        pc "Mmmmmmm."
        $ player.sex_cum(dani)
        pc "Mmmmmmm..."
        dani.name "Ah you came? So nice."
        pc "Mmmmfff."
        show sb_onback no_dani look_up relax with dissolve
        pc "Ah I can breathe."
        dani.name "Heh, I got a bit carried away."
        pc "You have your fun?"
        show sb_onback dani_lay_closed look_right with dissolve
        dani.name "Of course."
    else:

        dani.name "Come here."
        show sb_onback dani_kiss with dissolve
        pc "Oh?"
        "I lay there masturbating while [dani.name] kisses, gropes and licks me all over."
        pc "Mmmm, this is nice. Keep going like this and I will cum."
        dani.name "That's the plan."
        "She gets a bit more aggressive with her affection, pushing her tongue in my mouth as I start to breathe heavier."
        "I let her do what she wants as I focus between my legs, slowly brining myself to climax."
        dani.name "Oh getting closer?"
        pc "Mmmm."
        dani.name "I want to look you in the eye as you cum!"
        "As I get closer, I look at her directly and I start to cum."
        pc "Ah fuck yes."
        pc "Ahhhhhhhh."
        $ player.sex_cum(dani)
        dani.name "Ah yes, let me see that face."
        pc "Ah, weirdo."
        dani.name "Your the pervert wanking in my bed."
        pc "Ah well, not any more."
        show sb_onback dani_lay_open relax with dissolve
        dani.name "That was fun."
        pc "You didn't get off."
        dani.name "Next time."

    jump dani_sex_bedroom_sex_end_nostrap



label dani_sex_bedroom_bentover_strapon:
    $ dani.dict["strapon_sex"] += 1
    hide dani_kiss
    show sb_bentover head_down
    with hpunch
    show sb_bentover head_up back worried oh with dissolve
    pc "Ohh?"
    pc "What are you up to you pervert?"
    dani.name "Getting something nice."
    show sb_bentover dani_cum with dissolve
    pc "Ah, getting your little friend?"
    dani.name "Dirty girls like you don't want little friends."
    dani.name "I'll fuck you with this monster."
    show sb_bentover dani_poke with dissolve
    pc "Oooh?"
    dani.name "You know how sluts like us should be fucked."
    pc "Mmmmm..."
    $ player.spank()
    dani.name "Bent over like the cheap whores we are."
    $ player.spank()
    dani.name "Get ready you dirty bitch."
    $ player.sex_vag(dani)
    show sb_bentover dani_sex ooh forward
    pc "Ahh fuck it's so big."
    dani.name "Mmm, I'm sure you love something this big."
    pc "Ah fuck."
    dani.name "Dirty little slut."
    dani.name "Arse like this should be fucked all the time."
    show sb_bentover head_down with hpunch
    dani.name "You like this, slut?"
    dani.name "Stuck your head down there and eat that pillow!"
    with hpunch
    if player.showing:
        dani.name "Look at you you fat cunt! Let someone cum in you and give you that belly."
        dani.name "Bet there will be plenty more after this one."
    else:
        dani.name "Bet a dirty bitch like you wants a man to fill you up?"
        dani.name "Stick his baby in you then fuck off, leaving the rest to you."
    dani.name "If I could, I would cum in you like these fucks do with me."
    if dani.showing:
        dani.name "Look at my belly, look what they did to me!"
    else:
        dani.name "Always filling me up, making me risk their baby."
    $ player.spank()
    dani.name "Shame I can't fill you up with cum!"
    dani.name "Like these perverts, I would make you go home leaking."
    $ dani.cum()
    dani.name "Yeah you bitch!"
    show sb_bentover dani_poke with dissolve
    dani.name "Mmmm, hope that was fun for you."
    show sb_bentover head_up back oh worried with dissolve
    pc "It was... Something..."
    jump dani_sex_bedroom_sex_end_strap

label dani_sex_bedroom_onback_strapon:
    $ dani.dict["strapon_sex"] += 1
    hide dani_kiss
    show sb_onback dani_kiss
    with dissolve
    "We move over to the bed and lay down kissing."
    dani.name "Mmmm."
    dani.name "You are so sexy."
    dani.name "I think I know what a dirty girl like you needs."
    pc "Oh?"
    show sb_onback no_dani look_up relaxed neutral with dissolve
    pc "What are..."
    show sb_onback oh
    pc "Oh..."
    dani.name "Yup."
    show sb_onback dani_kiss strapon with dissolve
    dani.name "I'm going to fuck you like the dirty whore you are."
    show sb_onback dani_sex with dissolve
    dani.name "And give you this giant cock you love."
    pc "I love it do I?"
    dani.name "Mmmm."
    $ player.sex_vag(dani)
    show sb_onback ah angry
    "Without much warning, she presses it against me and starts sliding it inside me."
    pc "Ah fuck it's so big. A bit of warming up would be nice."
    dani.name "Shush. Take it like you are meant to."
    show sb_onback pout straight
    "[dani.nname] starts to fuck me. Not gentle and nice like I would expect, but somewhat aggressive right from the start."
    "I've kind of come to expect this from [dani.nname], so I relax and try to enjoy it."
    with hpunch
    dani.name "You dirty bitch, you like a big cock like this?"
    "I mostly ignore her taunts, and try to get into the flow of things."
    show sb_onback look_closed oh worried
    if not numgen(0,5):
        jump dani_sex_bedroom_matingpress_strapon
    pc "Ahh fuck. Starting to fell nice."
    dani.name "I know a slut like you would enjoy something like this."
    with hpunch
    dani.name "Such a big cock inside you!"
    "She grabs my legs and starts to fuck me even harder."
    "All the while she is calling me a slut, whore and other names. I mostly drown it out and enjoy."
    dani.name "Fuck yes you dirty bitch."
    pc "Ahhh fuck I am close."
    dani.name "Yeah!"
    $ player.sex_cum(dani)
    pc "Ahhh yes!"
    pc "Fuck..."
    dani.name "I knew you would like that."
    show sb_onback look_up
    pc "Err, yeah..."
    show sb_onback dani_kiss strapon with dissolve
    dani.name "You dirty girl."
    jump dani_sex_bedroom_sex_end_strap

label dani_sex_bedroom_matingpress_strapon:
    dani.name "Come here."
    "Without warning, she grabs my legs and lifts them up."
    hide sb_onback
    show sb_matingpress dani_poke oh
    with dissolve
    pc "Oh fuck."
    show sb_matingpress dani_vag with dissolve
    $ player.sex_vag(dani)
    pc "Ahhhh fuck, so big!"
    dani.name "Just the way you like it!"
    dani.name "Giant cock like this fucking you like a dirty bitch."
    pc "Ah fuck!"
    dani.name "Scream for me bitch!"
    with hpunch
    "[dani.nname] fucks me relentlessly. I'm not even sure at this point if I amenjoying, but I go along with it anyway."
    "She starts to get a bit heavy, calling me all manner of names and telling me how much she will fuck me."
    dani.name "How many guys have you let fuck you like this?"
    dani.name "And let them cum deep inside you!"
    dani.name "I want to cum inside you as well!"
    dani.name "Ah fuck yes!"
    "[dani.nname] mimics a guy cumming inside me, pressing herself deep inside while moaning."
    dani.name "Ah fuck yes!"
    dani.name "Dirty bitch!"
    show sb_matingpress dani_poke with dissolve
    dani.name "Shame I can't make you leak."
    pc "Mmmm..."
    jump dani_sex_bedroom_sex_end_strap

label dani_sex_bedroom_kissing_undress_call:
    if not c.nude:
        "My hands rove over her body, undressing her, while hers do the same."
        $ pc_strip_upper(slow=True, temp=True)
        dani.name "[rlist.dani_sex_comment_breasts]"
        pc "Mmmm."
        $ pc_strip_lower(slow=True, temp=True)
        dani.name "[rlist.dani_sex_comment_ass]"
    else:
        "My hands rove over [dani.nname]'s body, stripping her of her clothes."
        dani.name "[rlist.dani_sex_comment_generic]"
        pc "Mmmm!"
    return

label dani_sex_bedroom_sex_end_nostrap:
    if not renpy.showing("sb_onback"):
        $ renpy.scene()
    show sb_onback dani_lay_open relax look_right neutral relaxed dani_smile
    with dissolve

    if t.hour in (23,0,1,2,3,4,5):
        pc "Coming to bed now?"
        show sb_onback look_right dani_lay_closed dani_smile relaxed with dissolve
        pc "That was interesting."
        dani.name "Tasty."
        pc "Hehe."
        $ player.eye = 3
        show sb_onback dani_closed look_closed
        show screen blackout(100) with dissolve
        pause 0.5
        $ time_sleep_hour()
        jump bed_sleep_loop
    else:

        "We lay in bed relaxing for a bit, then get up and ready."
        $ renpy.scene()
        with dissolve
        $ pc_dress_slow("home")
        jump travel

label dani_sex_bedroom_sex_end_strap:
    if not renpy.showing("sb_onback"):
        $ renpy.scene()
    show sb_onback relax look_up neutral relaxed
    with dissolve
    if t.hour in (23,0,1,2,3,4,5):
        pc "Coming to bed now?"
        dani.name "Yeah, lemme take this off first."
        show sb_onback look_right dani_lay_closed dani_smile relaxed with dissolve
        pc "That was interesting."
        dani.name "Tasty."
        pc "Hehe."
        $ player.eye = 3
        show sb_onback dani_closed look_closed
        show screen blackout(100) with dissolve
        pause 0.5
        $ time_sleep_hour()
        jump bed_sleep_loop

    "We lay in bed relaxing for a bit, then get up and ready."
    $ renpy.scene()
    with dissolve
    $ pc_dress_slow("home")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
