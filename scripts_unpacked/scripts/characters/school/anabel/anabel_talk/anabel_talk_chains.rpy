label anabel_talk_dani_split_0:
    $ anabel.dict["dani_split"] += 1
    pc "Hanging out here alone a bit more than usual. Everything okay?"
    anabel.name "Yeah it's fine. Just need a bit of time alone y'know."
    pc "Yeah, I can understand that."
    anabel.name "Mmm."
    jump anabel_talk_end

label anabel_talk_dani_split_1:
    $ anabel.dict["dani_split"] += 1
    pc "Still here?"
    anabel.name "Yeah."
    pc "..."
    jump anabel_talk_end

label anabel_talk_dani_split_2:
    $ anabel.dict["dani_split"] += 1
    pc "So what's going on with you and [dani.nname]?"
    anabel.name "Ugh. I don't know. I don't really want to talk about it."
    pc "Err, okay then."
    jump anabel_talk_end

label anabel_talk_dani_split_3:
    $ anabel.dict["dani_split"] += 1
    anabel.name "It's just... I'm not sure what she is doing or thinking."
    pc "Err, well that's normal for everyone."
    anabel.name "Not like that. It's like... I dunno."
    anabel.name "She is different. Or something."
    jump anabel_talk_end

label anabel_talk_dani_split_4:
    $ anabel.dict["dani_split"] += 1
    anabel.name "Me and [dani.name] came here together. Went though the same stuff."
    pc "Okay."
    anabel.name "And now she is doing things I wouldn't expect of her."
    pc "Like what?"
    show anabel worried
    anabel.name "That's the thing. I don't even know. But it worries me."
    jump anabel_talk_end

label anabel_talk_dani_split_5:
    $ anabel.dict["dani_split"] += 1
    pc "So you are mad at [dani.nname] for doing unknown things?"
    anabel.name "Yes... No... It's hard to explain."
    pc "Sure you aren't being too harsh or over thinking things?"
    anabel.name "Maybe, but I don't think so."
    jump anabel_talk_end

label anabel_talk_dani_split_6:
    $ anabel.dict["dani_split"] += 1
    pc "So what do you think is going on with [dani.nname]?"
    anabel.name "It's hard to say..."
    pc "Try?"
    anabel.name "Let me think..."
    jump anabel_talk_end

label anabel_talk_dani_split_7:
    $ anabel.dict["dani_split"] += 1
    anabel.name "So I don't know if you know, but a lot of us that arrived from outside were in refugee camps for a while."
    pc "I think I heard something about that."
    anabel.name "Well [dani.name] and I stayed in one for some time."
    anabel.name "It was horrible there. The men there were animals."
    jump anabel_talk_end

label anabel_talk_dani_split_8:
    $ anabel.dict["dani_split"] += 1
    anabel.name "And now it's like [dani.nname] forgot all that."
    pc "What do you mean?"
    anabel.name "I mean like this with dance stuff and other things. She seems to forget what these men can be like."
    anabel.name "And just seems okay with them."
    jump anabel_talk_end

label anabel_talk_dani_split_9:
    $ anabel.dict["dani_split"] += 1
    pc "And what would you have her do? Stalk the streets and night looking for someone alone and put a knife in their back?"
    anabel.name "I would expect that sooner than her being all friendly with them."
    pc "Why?"
    anabel.name "Because of everything we went though. How can she just go on like normal with these people?"
    jump anabel_talk_end

label anabel_talk_dani_struggle_0:
    $ anabel.dict["dani_struggle"] += 1
    pc "You ask \"How can she go on like its normal\" but have you not seen how much she is struggling?"
    anabel.name "What?"
    pc "I take that as a no..."
    anabel.name "..."
    jump anabel_talk_end

label anabel_talk_dani_struggle_1:
    $ anabel.dict["dani_struggle"] += 1
    anabel.name "What do you mean struggling? She is off having fun and doing weird stuff."
    pc "Is that what you really think it is?"
    anabel.name "Well what else is it?"
    pc "Not to sound like an ass here, but looks like you have spent too much time judging her and not enough trying to understand."
    anabel.name "What? She is my best friend!"
    pc "Is she?"
    jump anabel_talk_end

label anabel_talk_dani_struggle_2:
    $ anabel.dict["dani_struggle"] += 1
    anabel.name "We went though all the same things together. All this..."
    pc "Hmmm..."
    anabel.name "And you are saying what? You understand her more than I do?"
    pc "Didn't say I understand her more than you, I said she is struggling and you cant see it."
    jump anabel_talk_end

label anabel_talk_dani_struggle_3:
    $ anabel.dict["dani_struggle"] += 1
    anabel.name "How can she be struggling? We went through all the same stuff!"
    pc "Ask her that maybe."
    anabel.name "She should know just like I do what it's like here."
    anabel.name "But she is still doing all this stuff, I don't even know what!"
    jump anabel_talk_end

label anabel_talk_dani_struggle_4:
    $ anabel.dict["dani_struggle"] += 1
    anabel.name "How can she be struggling but still do all this stuff?"
    anabel.name "She should know just like I do what it is like."
    pc "..."
    jump anabel_talk_end

label anabel_talk_dani_struggle_5:
    $ anabel.dict["dani_struggle"] += 1
    anabel.name "Ugh! Whatever. Let her have her fun!"
    pc "..."
    anabel.name "If she didn't learn already what it's like, she will soon."
    pc "Yeah I don't think..."
    anabel.name "Enough, I don't want to talk about her any more. Let her do what she wants!"
    pc "..."
    jump anabel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
