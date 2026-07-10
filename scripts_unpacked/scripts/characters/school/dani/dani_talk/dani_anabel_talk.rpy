label dani_anabel_talk_picker:
    if dani_here() and anabel_here():
        jump expression WeightedChoice([
        ("dani_anabel_talk_subject", 100),
        ("dani_talk_subject", 70),
        ("anabel_talk_subject", 70),
        ])
    elif dani_here():
        jump dani_talk_subject
    else:
        jump anabel_talk_subject

label dani_anabel_talk_subject:
    if dani.hate:
        $ player.face_angry()
        pcm "I don't want to talk while that bitch is around."
        jump travel





    show dani at right2
    show anabel at right1
    with dissolve

    jump expression WeightedChoice([

    ("dani_anabel_talk_dance_1", 100),
    ("dani_anabel_talk_dance_2", 100),
    ("dani_anabel_talk_dance_3", 100),
    ("dani_anabel_talk_dance_4", 100),
    ("dani_anabel_talk_dance_5", 100),


    ])

label dani_anabel_talk_dance_1:
    dani.name "Why is it so cold in the gym?"
    anabel.name "Such a huge space. And we don't have any heating."
    dani.name "I swear it's colder in the gym than outside."
    anabel.name "Yeah..."
    jump dani_anabel_talk_end

label dani_anabel_talk_dance_2:
    dani.name "Any of the boys tried to sneak in the showers after you?"
    anabel.name "Actually no. Well, not really."
    dani.name "Not really?"
    anabel.name "I have seen some boys in there, but they were usually brought in by someone else."
    dani.name "Ah."
    jump dani_anabel_talk_end

label dani_anabel_talk_dance_3:
    anabel.name "Do you think [rachel.name] really did that?"
    dani.name "Probably..."
    anabel.name "But that's crazy."
    pc "Crazy and [rachel.name] are basically the same thing."
    jump dani_anabel_talk_end

label dani_anabel_talk_dance_4:
    dani.name "having fun on the buses?"
    anabel.name "Ugh, don't remind me."
    pc "Oh? [anabel.name] one of those bus perverts I hear about."
    dani.name "Hmm, the amount of fun she seems to have, I think she might."
    anabel.name "C'mon you guys..."
    jump dani_anabel_talk_end

label dani_anabel_talk_dance_5:
    anabel.name "I wonder why [svet.nname] set up the dance club?"
    dani.name "She used to be a professional dancer."
    anabel.name "She was?"
    dani.name "So [rachel.name] told me."
    jump dani_anabel_talk_end


label dani_anabel_talk_test:
    dani.name "Testing we are working."
    anabel.name "What about me?"
    pc "Hopefully fine."
    jump dani_anabel_talk_end

label dani_anabel_talk_end:
    $ relax(20, [dani, anabel])
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide dani
    hide anabel
    with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
