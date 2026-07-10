label loc_school_sewroom_visit:
    pcm "Hmm, what is this place?"
    show saskia at right1 with dissolve
    saskia.name "Got something for us?"
    pc "Huh?"
    saskia.name "What you got?"
    $ player.face_worried()
    pc "Err, not sure what you mean."
    show frida happy at right2 with dissolve
    frida.name "Seen you already. New girl?"
    saskia.name "New girl?"
    show frida neutral
    frida.name "Ya, saw her looking round. What you doing here? Lost ya boyfriend?"
    pc "Err, I was just..."
    show saskia happy
    saskia.name "She has a boyfriend?"
    frida.name "Dunno. You got a boyfriend?"
    pc "Umm, no?"
    show saskia neutral
    frida.name "Looking for one?"
    pc "Not really..."
    frida.name "So what you doing here then?"
    pc "I... Err, what has being here and boyfriends got to do with it?"
    frida.name "Nothing."
    pc "Nothing?"
    frida.name "Nope."
    pc "..."
    pc "So why ask?"
    saskia.name "We make clothes."
    pc "Okay..."
    show saskia happy
    saskia.name "Fancy clothes."
    pc "Right..."
    pc "I'm lost."
    show saskia neutral
    saskia.name "I can see that."
    pc "I'm gonna go now..."
    frida.name "Come back if you want to buy."
    saskia.name "We also buy junk clothes. Come here if you find something."
    hide saskia
    hide frida
    if loc(loc_school_sewroom):
        $ walk(loc_school_hallway_2f)
    else:
        $ walk(loc_market)
    pcm "..."
    pcm "Weirdos..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
