label rachel_talk_gloryhole_0:
    $ rachel.dict["rachel_gloryhole_talk"] += 1
    rachel.name "Hey [name]! C'mere."
    pc "What's up?"
    rachel.name "You know."
    pc "Hmm?"
    rachel.name "In there. The stall."
    pc "Yeah?"
    rachel.name "There is a hole!"
    pc "Ah."
    jump rachel_talk_end

label rachel_talk_gloryhole_1:
    $ rachel.dict["rachel_gloryhole_talk"] += 1
    rachel.name "If you go in there. What do you think happens?"
    pc "Someone puts a present in the hole?"
    rachel.name "Exactly!"
    pc "Huh? I was jok..."
    rachel.name "I was in there and someone put their thingy in."
    pc "Ah right..."
    jump rachel_talk_end

label rachel_talk_gloryhole_2:
    $ rachel.dict["rachel_gloryhole_talk"] += 1
    pc "So what you do with the thing?"
    rachel.name "What thing?"
    pc "The thing he put in the hole."
    rachel.name "I looked at it."
    pc "It's all?"
    rachel.name "Yeah? What else would I do?"
    pc "Err... Suck it?"
    rachel.name "What?"
    jump rachel_talk_end

label rachel_talk_gloryhole_3:
    $ rachel.dict["rachel_gloryhole_talk"] += 1
    $ add_to_list(rachel.list, "using_gloryhole")
    rachel.name "You think they will let me suck it?"
    pc "What else would you do with it?"
    rachel.name "Dunno. Never seen it in a hole before."
    pc "Pretty sure they are putting it there for some fun."
    rachel.name "Ahhh!"
    jump rachel_talk_end

label rachel_talk_gloryhole_4:
    pc "Been having fun in there?"
    if not ghman.name in rachel.sex_who:
        rachel.name "No. Not yet."
        jump rachel_talk_end
    $ rachel.dict["rachel_gloryhole_talk"] += 1
    rachel.name "I did. They didn't seem to mind."
    pc "Of course. Why else would they do it?"
    rachel.name "Dunno. Make us happy?"
    pc "Ha. Right. Okay..."
    jump rachel_talk_end

label rachel_talk_gloryhole_5:
    $ rachel.dict["rachel_gloryhole_talk"] += 1
    rachel.name "Why'd they keep putting money in?"
    pc "Err... To pay for cleaning your clothes?"
    rachel.name "Ah ok. I should probably take it next time then."
    pc "You wasn't already?"
    rachel.name "No. Why would I?"
    pc "Err... Yeah, why would you..."
    jump rachel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
