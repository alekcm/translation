label main_quest_02_meet:
    $ walk(loc_revel)
    pc "Here we are, so... A white chalk mark on the door."
    menu:
        "Put the chalk mark":
            pc "Ok, it's done."
            pc "Now to go to the meeting spot I suppose."
            jump main_quest_02_meet_highway
        "Wait for another time":

            pc "Hmm, I don't think I am ready for this just now..."
            jump travel


label main_quest_02_meet_highway:
    $ main_quest_02.stage = 3
    $ walk(loc_revel_backstreet)
    with dissolve

    pc "..."
    pc "... ..."
    $ player.face_worried()
    pc "Where the hell is he?"
    pc "..."
    pc "Did he realise it was all a ploy?"
    pc "Well, no choice but to just wait..."

    $ stroll(30)
    $ player.face_worried()
    "I just hang around killing time while keeping a look out for [simon.name]."

    if "school" in tab_top:
        pc "Hmm, standing here for a while and people are starting to give me the eye. Wearing my school uniform in such a place was probably a bad idea."
        pc "I've ended up looking like some age play whore or something."
    elif player.allure > 100:
        pc "Hmm, standing here all this time dressed like this is bringing me a lot of attention. Not quite the right place to just loiter since I no doubt look like a whore."
    else:
        pc "Hmm, standing here for a while and people are starting to give me the eye. Probably not a place where a young girl should be hanging around."
        pc "Standing around these backstreets makes me look weird..."
    pc "..."
    pc "Huffff. How much longer is he going to take?"

    $ stroll(30)
    $ player.face_worried()
    "I keep waiting around trying to avoid the expectant looks of the men passing. Avoiding looking like a whore while hanging around a seedy back alley."
    $ player.face_annoyed()
    pc "Ok... It's been over an hour and I can't see [simon.name] anywhere."
    pc "Do I just keep waiting or do I assume he isn't coming?"
    $ player.face_worried()
    pc "Luckily none of the shady guys looking for some fun at night have came up to me. But that won't last long if I stay here much longer."
    pc "So it's not just my target or missions that might be dangerous, but the places I will have to go to as well..."
    pc "[tucker.name] put me in dance class at school but wouldn't it have been better to give me some martial arts training or something like that?"
    pc "Heh, who am I kidding? I'm barely 5 feet tall and weigh less than most 12 year old boys. Even if I was training for years, I would still be squashed by a fat drunkard."
    pc "Hmmm, what the hell do I do on these missions if someone wants to harm me? Fighting is totally out of the question."
    pc "Eh, never really thought about it before, but could I be in danger doing this stuff? I was pretty quick to agree without really knowing what I might be getting myself into."
    show simon at right5 with Dissolve(0.2)

    $ player.face_shock()
    pc "EEEHHHH!"
    simon.name "Shhhhh! [nadia], it's me."
    $ player.face_worried()
    pc "Phew..."
    simon.name "Here, take this..."
    "[simon.name] thrusts a small satchel into my hands."
    $ inv.take(item_simon_satchel)
    simon.name "Keep your eye out for some sneaky young girl poking around."
    hide simon with dissolve
    pc "..."
    pc "Well... Okay then..."
    pc "That's that then I suppose. Fuck... All that worrying and it's done in 5 seconds."
    $ log.markdone("mq_02_c")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
