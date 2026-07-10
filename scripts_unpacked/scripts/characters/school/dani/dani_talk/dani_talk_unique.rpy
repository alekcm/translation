
label dani_talk_pregnant_discover:
    $ add_to_list(dani.list, "seen_pregnant_" + str(dani.preg))
    if not dani.love >= 50:

        jump dani_talk_subject
    if dani.preg == 1:
        pc "Oh? Pregnant? How'd you manage that?"
    else:
        pc "Pregnant again? Bet that makes you happy?"
    show dani worried
    dani.name "Ugh, yeah..."
    pc "How did that happen?"
    if dani.pregnant_who == oskar:
        dani.name "That arse that makes me pay rent."
        pc "Oh..."
        pc "You going to charge him rent now?"
        dani.name "I should!"
    elif dani.pregnant_who == busgroper:
        dani.name "Probably on the bus."
        pc "Ah shit."
        dani.name "Can't even get around without stuff like this happening."
    elif dani.pregnant_who == lover:
        dani.name "Err, I think it was someone I kinda messed about with."
        pc "Oh? Well that's not too bad."
        dani.name "It's terrible."
        dani.name "But better than some cunt dragging me into the bushes and doing it."
        pc "Yeah I guess."
    elif dani.pregnant_who == pubpatron:
        dani.name "Some drunk shit from the pub I think."
        pc "Oh? Hope he paid enough to be worth it."
        dani.name "Yeah right. Even my ass barely earns enough to pay rent and eat."
    elif any(x == dani.pregnant_who for x in [punter, highpayer]):
        dani.name "Ugh!"
        dani.name "Someone kinda offered some money for fun."
        pc "Ah."
        dani.name "Yeah..."
        pc "Got more than he paid for then."
        dani.name "Yeah, should have got more money off him if I knew I would end up like this."
    elif dani.pregnant_who == rapist:
        dani.name "Don't ask."
        pc "Ah, shit. Sorry."
        dani.name "Yeah..."
    elif dani.pregnant_who == partyman:
        dani.name "This? Got it at the dance party."
        pc "Oh, well... Must have been a good party for that guy."
        dani.name "Yeah, it probably was."
    else:
        dani.name "Err, I have no idea how I ended up like this."
        pc "Oh?"
        dani.name "Yeah..."
    jump dani_talk_end

label dani_talk_anabel_chain_0:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    pc "So you and [anabel.name] seem close."
    dani.name "Yeah, kind of knew each other before all this stuff happened."
    pc "Oh? Childhood friends?"
    dani.name "Somewhat. But not really."
    jump dani_talk_end

label dani_talk_anabel_chain_1:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    dani.name "Me and [anabel.nname] went to the same school as kids. Lived near each other."
    dani.name "Weren't friends since we hung out with different groups. But still saw each other and would say \"hello\"."
    pc "So what? You are both from [town]?"
    dani.name "No, but not too far. Some place that is probably just ash now."
    jump dani_talk_end

label dani_talk_anabel_chain_2:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    dani.name "World went to shit. Stuff happened and I ended up here."
    pc "\"Stuff\"? Sounds ominous."
    dani.name "Pretty sure everyone went though \"stuff\" before finding their way here."
    pc "I guess."
    if player.male_origin:
        pcm "I ended up dead and resurrected and woke up without a willy."
    else:
        pcm "I ended up dead and resurrected..."
    jump dani_talk_end

label dani_talk_anabel_chain_3:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    dani.name "After arriving here, going through the medical stuff in their tents. I saw [anabel.nname] there as well."
    dani.name "To be honest, we barely even spoke. But just seeing someone familiar was comforting or something."
    pc "From what I hear about it all, I imagine it was comforting."
    dani.name "We stuck together since."
    jump dani_talk_end

label dani_talk_anabel_chain_4:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    dani.name "Ha, it was actually a month or so before we actually properly spoke."
    pc "Really?"
    dani.name "Yeah, usually we would just stick together. I guess she went though as much shit as we all did."
    dani.name "So need time to process. Just being together, I dunno, sort of helps you relax a bit and think things over."
    jump dani_talk_end

label dani_talk_anabel_chain_5:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    dani.name "Plus at this point we were still living in communal tents. Gotta stick together so no one drags you off and rapes you."
    pc "That was common?"
    dani.name "Too common back then. Would find a few corpses every morning of some girl that wandered off."
    dani.name "Got to the point where you were ready to stab anyone that has a cock within twenty meters of you."
    jump dani_talk_end

label dani_talk_anabel_chain_6:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    pc "No one dealing with what was happening in the camps?"
    dani.name "Police or something? No. There were even rumours that it was the security doing it all."
    dani.name "Started getting to the point where you would have a ring of women surrounding the tents ready to kill any men coming near."
    pc "Fuck, that sounds like some shit you would read in a bad novel."
    jump dani_talk_end

label dani_talk_anabel_chain_7:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    dani.name "It ended up getting worse. Corpses were still getting found. The women were getting pretty worked up."
    dani.name "One night some women broke into another tent and just stabbed all the men sleeping and ran away."
    pc "Wow, shit."
    dani.name "Happened again for a few nights, but the surprise was gone so was less effective."
    pc "Fucking hell, just camps out murdering each other."
    dani.name "Yeah."
    jump dani_talk_end

label dani_talk_anabel_chain_8:
    $ dani.dict["dani_talk_anabel_chain"] += 1
    dani.name "Pretty sure a mini civil war would have broke out if it kept like this."
    dani.name "But then they started moving people out of the camps. The drugs did their work or whatever. We were allowed to go."
    pc "Yup, just let all the rapists and murderers into the town. Nothing would go wrong there."
    dani.name "Well it's pretty much what happened. Me and [anabel.nname] also got told we should go to the academy."
    dani.name "No reason to refuse so we did."
    jump dani_talk_end

label dani_talk_upstairs_0:
    $ dani.dict["dani_talk_upstairs_chain"] += 1
    pc "Hmm, odd seeing you up here."
    dani.name "Yeah, just want a bit of alone time."
    pc "Ah okay, I'll leave you to it then."
    show dani worried
    dani.name "No, I mean... From [anabel.name]..."
    pc "Ah..."
    jump dani_talk_end

label dani_talk_upstairs_1:
    $ dani.dict["dani_talk_upstairs_chain"] += 1
    pc "You and [anabel.nname] have a fight or something?"
    dani.name "No, nothing like that."
    pc "Okay..."
    jump dani_talk_end

label dani_talk_upstairs_2:
    $ dani.dict["dani_talk_upstairs_chain"] += 1
    dani.name "Just sometimes I feel like I am being judged."
    pc "Oh, for what?"
    dani.name "She and I don't see eye to eye on some things..."
    jump dani_talk_end

label dani_talk_upstairs_3:
    $ dani.dict["dani_talk_upstairs_chain"] += 1
    pc "Not seeing eye to eye about what?"
    dani.name "Ugh, about what I do to get by."
    pc "Oh? Earning money?"
    dani.name "Yeah. Not like I enjoy it this way but I don't want to end up sleeping under a bridge."
    pc "Right..."
    jump dani_talk_end

label dani_talk_upstairs_4:
    $ dani.dict["dani_talk_upstairs_chain"] += 1
    dani.name "She just... Does not understand."
    pc "Hmmm."
    dani.name "What?"
    pc "Nothing. I just can't say much. I have no idea what she does to earn."
    dani.name "Not a lot..."
    jump dani_talk_end

label dani_talk_upstairs_5:
    $ dani.dict["dani_talk_upstairs_chain"] += 1
    dani.name "Doesn't matter anyway. Every time I mention something about money I end up getting a lecture."
    dani.name "Yeah I know it isn't a good thing. But I don't want to starve. Not like I can change it even if I wanted to."
    pc "Right..."
    dani.name "So just hanging out here to avoid her judgemental comments."
    jump dani_talk_end

label dani_talk_upstairs_6:
    $ dani.dict["dani_talk_upstairs_chain"] += 1
    dani.name "We just went though a lot in the past..."
    pc "Yeah, I remember."
    dani.name "And now she acts like I am betraying her or something. Like I should be ready to murder any man I see."
    pc "Ah, yeah kinda sounds like her."
    jump dani_talk_end

label dani_talk_upstairs_7:
    $ dani.dict["dani_talk_upstairs_chain"] += 1
    dani.name "We left all that behind and I just want to forget it. Those problems are gone now."
    dani.name "But there are new problems to deal with."
    pc "..."
    dani.name "Ugh!"
    jump dani_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
