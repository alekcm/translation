label rachel_talk_bitching_0:
    $ rachel.dict["rachel_bitching_talk"] += 1
    pc "Still wearing that collar?"
    rachel.name "Yeah. Why?"
    pc "Well, means you will get jumped doesn't it?"
    rachel.name "Yeah."
    pc "..."
    jump rachel_talk_end

label rachel_talk_bitching_1:
    $ rachel.dict["rachel_bitching_talk"] += 1
    pc "So since your still wearing the collar, I guess you had fun?"
    rachel.name "Yeah. Finally got to run around the park naked like that girl."
    pc "And get jumped by a bunch of guys."
    rachel.name "They started to run away from me so I had to chase them."
    jump rachel_talk_end

label rachel_talk_bitching_2:
    $ rachel.dict["rachel_bitching_talk"] += 1
    pc "Maybe if you bit them less, they wouldn't run away."
    rachel.name "They want to play doggie. Why wouldn't I bite?"
    pc "Err, so they can have fun with you."
    rachel.name "It's fun for me."
    pc "Maybe not so much for them."
    jump rachel_talk_end

label rachel_talk_bitching_3:
    $ rachel.dict["rachel_gloryhole_talk"] += 1
    $ add_to_list(rachel.list, "using_gloryhole")
    rachel.name "If they didn't want me to bite, why would they want a doggie?"
    pc "Errm..."
    pc "Well, just go easy on them."
    rachel.name "If I do, then they will be rough with me."
    pc "That can also be fun."
    jump rachel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
