



label dani_talk_postvip_goodend_chain_0:
    $ dani.dict["dani_post_vip_chain"] += 1
    dani.name "So that party kinda went a little wild."
    pc "Yeah, although anything involving [rachel.name] tends to go a bit crazy."
    dani.name "Seemed she enjoyed it."
    pc "What about you?"
    dani.name "Hmmm..."
    jump dani_talk_end

label dani_talk_postvip_goodend_chain_1:
    $ dani.dict["dani_post_vip_chain"] += 1
    if dani.iswhore and partyman in dani.sex_who_class:
        dani.name "Not sure I enjoyed the party, but the money it got me was certainly good."
        pc "Oh? You went off and got some extra pay?"
        dani.name "Yeah. I mean isn't that why we were there?"
        if partyman.sex:
            pc "I suppose so. Just whores for their entertainment."
        else:
            pc "I didn't end up going off with someone. The pay alone was good enough."
    elif dani.iswhore:
        dani.name "Was mostly feeling it out for now. I know they pretty much wanted whores but I thought I would wait."
        pc "Ah, so only the flat fee?"
        dani.name "Yeah, I know why we were there, but..."
        pc "Yeah, all those men surrounding us, things can get out of hand fast."
    else:
        dani.name "Wasn't much to enjoy at the party. They spent all night trying to get me drunk and into bed with them."
        pc "Yeah, was pretty clear we were meant to be whores."
        if partyman in dani.sex_who_class:
            dani.name "Ugh, it worked as well..."
            pc "It did? Someone manage to drag you off? Hope you at least got paid."
            dani.name "Yeah, got paid..."
        else:
            dani.name "Need to be careful next time."
            pc "Or not. We all need the money."
    jump dani_talk_end

label dani_talk_postvip_goodend_chain_2:
    $ dani.dict["dani_post_vip_chain"] += 1
    dani.name "Looks like [anabel.name] managed to get out of the party okay."
    if "anabel_help" in quest_dancevip.list:
        pc "Yeah, the idiot was walking right into a trap with the booze so I had to help her out."
        dani.name "What do you mean."
        pc "Ugh, [anabel.name] drunk around that lot? She was half a glass away from being dragged off for the night."
        pc "So I ended up trying to get her to calm down on the booze"
        dani.name "Haha, I would have liked to see that. Maybe she could do with being dragged off."
        pc "Haha."
    else:
        pc "Yeah, piss drunk but at least she wasn't passed around like meat."
        dani.name "Not sure how she managed it. They were all trying to get us drunk."
        pc "Lucky I guess."
    dani.name "I suppose that's why she doesn't want to come any more. Only a matter of time before something happens."
    pc "Yeah..."
    jump dani_talk_end

label dani_talk_postvip_goodend_chain_3:
    $ dani.dict["dani_post_vip_chain"] += 1
    pc "So how are you and [anabel.name] holding up anyway?"
    dani.name "Dunno, we barely talk any more."
    pc "No?"
    dani.name "She was always being judgemental before this party. Always making snide comments or acting superior."
    dani.name "Now after this party I just don't want to deal with her."
    pc "..."
    jump dani_talk_end

label dani_talk_postvip_goodend_chain_4:
    $ dani.dict["dani_post_vip_chain"] += 1
    pc "Have you, I dunno, tried to have a heart to heart with [anabel.name] or something?"
    dani.name "Ugh, doubt she cares"
    pc "..."
    dani.name "I have to do stuff to keep rent and food. She doesn't. So she can't see anything my way..."
    pc "Hmmm..."
    pcm "Maybe I should have a chat with [anabel.name] and see if I can smooth things over."
    $ add_to_list(anabel.list, "dani_post_vip_talk")
    jump dani_talk_end





label dani_talk_postvip_anabel_reconcile_chain_0:
    $ dani.dict["dani_post_vip_anabel_reconcile_chain"] += 1
    dani.name "By the way, had a chat with [anabel.name]..."
    pc "Oh?"
    dani.name "Yeah, kinda sorted our differences..."
    pc "That's good isn't it? Why don't you sound happy?"
    dani.name "I am happy..."
    pc "Right..."
    jump dani_talk_end

label dani_talk_postvip_anabel_reconcile_chain_1:
    $ dani.dict["dani_post_vip_anabel_reconcile_chain"] += 1
    dani.name "It should be water under the bridge with [anabel.name] shouldn't it?"
    pc "I guess."
    dani.name "It feels a little too late."
    pc "How so?"
    dani.name "..."
    jump dani_talk_end

label dani_talk_postvip_anabel_reconcile_chain_2:
    $ dani.dict["dani_post_vip_anabel_reconcile_chain"] += 1
    dani.name "She was supposed to be my friend."
    pc "And she is isn't she?"
    dani.name "So she says. But I was having a difficult time you know."
    pc "Yeah."
    dani.name "Yet it was her who pushed me away through it while it was you that helped me."
    pc "All I did was fill you with wine."
    dani.name "Haha."
    jump dani_talk_end

label dani_talk_postvip_anabel_reconcile_chain_3:
    $ dani.dict["dani_post_vip_anabel_reconcile_chain"] += 1
    dani.name "Well, the wine helped. Thanks [name]."
    pc "No reason to push her away because she failed at being a friend. Maybe it can bring you closer or something."
    dani.name "Doubt it, but no point causing more fights over it."
    pc "Still want the wine?"
    dani.name "Damn right I do."
    $ add_to_list(dani.list, "freakout_blocked")
    jump dani_talk_end





label dani_talk_postvip_badend_chain_0:
    $ dani.dict["dani_post_vip_chain"] += 1
    pc "So... [anabel.name] didn't take that all too well."
    dani.name "Yeah, no surprise. She is bitching at me constantly about what I do."
    dani.name "Then she has a few drinks and is passed around at the party."
    pc "..."
    jump dani_talk_end

label dani_talk_postvip_badend_chain_1:
    $ dani.dict["dani_post_vip_chain"] += 1
    dani.name "The bitch can't even hold herself to her own standards for one night."
    pc "Bit harsh. She was piss drunk."
    dani.name "Even worse. She did it without needing to. I have to do all this for money."
    pc "Still, she was kind of taken advantage of..."
    jump dani_talk_end

label dani_talk_postvip_badend_chain_2:
    $ dani.dict["dani_post_vip_chain"] += 1
    dani.name "Everyone is getting taken advantage of. [oskar.name] takes advantage of my need for a place to live."
    dani.name "Pub drunks take advantage of me needing money."
    dani.name "She got piss drunk at a whore party and allowed herself to be passed around for free."
    pc "..."
    dani.name "Serves her right."
    jump dani_talk_end

label dani_talk_postvip_badend_chain_3:
    $ dani.dict["dani_post_vip_chain"] += 1
    pc "C'mon, [anabel.name] wasn't prepared for this kind of thing. She is... Dunno, coddled?"
    dani.name "Yeah, and look where it got her. The same shitty place as the rest of us."
    dani.name "Pretending to uphold old world morals just screws you over even more when someone forces their dick in your ass."
    pc "..."
    jump dani_talk_end

label dani_talk_postvip_badend_chain_4:
    $ dani.dict["dani_post_vip_chain"] += 1
    pc "Don't you feel a little bad about it?"
    dani.name "Of course I do. But she brought it on herself. Too busy bitching at me instead of seeing the world for what it is."
    dani.name "Ugh!"
    dani.name "Enough about her. I have my own issues to worry about without caring about her fuck ups."
    dani.name "She doesn't give a shit about my issues, why should I care about hers?"
    jump dani_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
