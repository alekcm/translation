label mechanic_ali_talk:
    show ali at right1 with dissolve
    ali.name "Hi."
    if not mech_quest_ali.active:
        $ mech_quest_ali.activate()
        jump mechanic_ali_first_convo
    elif log.interactive("quest_gloryhole_a"):
        jump mechanic_gloryhole_ask_ali
    else:
        "Test"
        jump travel

label mechanic_dez_talk:
    show dez at right1 with dissolve
    dez.name "How I can help you?"
    if log.interactive("mech_quest_ali_a") and not log.interactive("mech_quest_ali_b"):
        jump mechanic_ali_dez_convo
    elif log.interactive("quest_gloryhole_a"):
        jump mechanic_gloryhole_ask_dez
    else:
        pc "Want to buy some junk?"
        jump mechanic_dez_sell

label mechanic_ali_first_convo:
    $ log.assign("Alison's deal")
    pc "So what's the deal with you and [dez.nname]?"
    ali.name "Huh? What do you care?"
    $ player.face_frown()
    pc "Maybe I don't. But I am meant to smooth out issues in places like this and it's pretty clear there is a big issue."
    ali.name "Hrmf!"
    ali.name "I know I can do this job. I used to deal with my dad's old junk before he died. But someone like him isn't gonna give a girl a chance."
    ali.name "So I kind of lead him on a bit to get him to agree and give it to me."
    $ player.face_worried()
    pc "Oh? Digging your grave there."
    ali.name "I hoped if I proved myself quickly enough I could avoid..."
    $ player.face_frown()
    pc "But he still expects you to entertain him?"
    ali.name "..."
    ali.name "I don't know what to do. I am barely getting by even with this job."
    ali.name "If I lose it, it's a matter of weeks before I am sleeping under the highway."
    ali.name "Think you can do something about it?"
    pc "Like what?"
    ali.name "Get him off my back."
    pc "Probably not."
    ali.name "Huh? Then why ask me?"
    pc "Because I thought he was abusing his position as your boss. Kind of different if it was the deal you offered him."
    ali.name "You saying I need to bend over for that arsehole? I thought you of all people would understand!"
    $ player.face_annoyed()
    pc "I do understand. Think I don't know how things work out there as well?"
    if player.rape:
        pc "Think I haven't had worse than him force themselves on me?"
    elif player.sold:
        pc "Think I haven't had to offer worse deals for some money to get by?"
    pc "Fact is, I know a lot of girls out there that would happily take the deal you offered."
    $ player.face_frown()
    ali.name "But..."
    ali.name "I don't want to..."
    ali.name "Please help me... Please..."
    pc "You have something else to offer him?"
    ali.name "Like what?"
    pc "No idea. Something of value he would prefer over you."
    ali.name "No..."
    pc "Any way to bury him?"
    ali.name "Huh?"
    pc "Evidence of something shady he is up to? Stealing stuff, selling it for a cut. Stuff like that. Something his bosses will cut him free over."
    ali.name "No... I can look out for it."
    pc "..."
    ali.name "... ..."
    pc "Gonna be honest. It doesn't look like you are going to have much of an option."
    ali.name "Please try and help. I don't want to end up having my first with him."
    pcm "First? Luckier than most..."
    pc "I'll see what I can come up with."
    ali.name "..."
    hide ali
    $ walk(loc_industrial)
    $ player.face_frown()
    pcm "Made a deal to get the job but can't go through with it..."
    pcm "She is terrified. But even if I help her, there is nothing for me to gain out of it."
    pcm "Better to stay on [dez.nname]'s side if I want to benefit out of it."
    pcm "Stupid girl..."
    jump travel

label mechanic_ali_dez_convo:
    dez.name "Hey."
    pc "Hi."
    dez.name "Tha look on yer face tells you not here for business?"
    pc "No. Well, sort of."
    pc "About the deal you and [ali.name] made."
    dez.name "She tellin you about this?"
    pc "Yes."
    dez.name "Problem? We made a deal. If no deal then I get someone better. Simple."
    dez.name "She can go and I not stop her. She is good mechanic and maybe I even help her. Give good word."
    dez.name "Nice girl."
    pc "She's between a rock and a hard place."
    dez.name "I give both. It's ok."
    pc "Ugh. She doesn't want to have sex with you."
    dez.name "She make deal."
    pc "Because if she doesn't have this job. She will be homeless and under the highway."
    dez.name "She nice girl. I treat her nice and give her job. Highway men leave her with no job and many baby."
    dez.name "It's good deal."
    pc "*Sigh*..."
    dez.name "You know this too."
    pcm "*Tsk* Better deal than she will ever get again. Working a job under The Institute..."
    if player.has_perk([perk_whore, perk_slut, perk_gamine]):
        pc "What if someone else \"helped you out\"?"
        dez.name "I can fuck whore from highway. I want nice girl. Good girl and I take care of her."
        pc "Think she is going to love you after you bully her into sex with her?"
        dez.name "Not today. Tomorrow maybe. I make her happy."
        pcm "Fuck. I thought he was some perverted cunt but he is just lonely and looking for someone nice."
    dez.name "Help her see it good deal. I look after her and we both happy."
    pc "*Sigh*"
    pc "I'll see..."
    $ walk(loc_mechanic)
    $ log.activate("mech_quest_ali_b")
    $ log.activate("mech_quest_ali_c")
    pcm "The fuck do I do?"
    hide dez
    $ walk(loc_industrial)
    pcm "She is a nice girl. Innocent to the point of being dumb, but I hate to see her put in a shitty situation."
    pcm "On the other hand, [dez.name] isn't some deviant cunt and actually seems to want to look after her..."
    pcm "Should I even help either of them? Maybe I should just leave it be and see how it pans out naturally."
    pcm "Ugh..."
    jump travel



label mechanic_gloryhole_ask_ali:
    pc "So I am looking to get my hands on something that can make a hole."
    ali.name "Err... Right... For a who or a what?"
    pc "A what. A wall."
    ali.name "Ok. So a drill?"
    pc "Maybe. A big hole. Enough to put your arm in."
    ali.name "Okaaaay. I would ask if you are trying to rob a bank, but no banks left."
    pc "Nothing strange like that. Well... Mostly."
    ali.name "Well whatever. If you want a perfect circle hole, you will need some decent tools."
    pc "No, not perfect. Just a hole."
    ali.name "Ok, so just make a hole with a chisel or a drill then open it up with a saw."
    ali.name "No need for power tools or anything like that."
    pc "Ok, do you have something like that?"
    "DEV NOTE** The rest of the dialogue assumes you have not completed Alis personal quest yet."
    ali.name "Yeah, but haven't heard anything from [dez.nname] or [tucker.name] about it so..."
    pc "It's not for that. It's just me asking."
    ali.name "Oh?"
    ali.name "Then no. I can't give [dez.name] any more excuses to use against me."
    ali.name "Deal with him for me and I'd happily stick my neck out. Otherwise you are going to have to go through him yourself."
    pc "Right. Thanks."
    hide ali with dissolve
    pcm "So make a hole with something then use a saw to cut the rest out?"
    pcm "It's going to be rough as shit though. Not something people will put their thing through so probably need something to smooth or soften the edges."
    pcm "Ugh, didn't think this would be so much work."
    jump travel

label mechanic_gloryhole_ask_dez:
    pc "I need to make a hole in a wall."
    dez.name "It strong wall?"
    pc "No, wood. Probably? Big enough for my arm."
    dez.name "It easy. But noisy. It be hard to do in secret."
    pc "That's fine. I can make noise."
    dez.name "Then easy. Use drill and make hole."
    pc "Then can I have a drill?"
    dez.name "It for [tucker.name]?"
    pc "No..."
    dez.name "Then no. Hard to replace drill and other power tools. Valuable equipment."
    pc "Can you give me anything less valuable to make a hole."
    dez.name "Use chisel to make small hole, saw to make bigger hole. It not perfect hole but good enough."
    pc "So can I have those?"
    dez.name "No."
    pc "*Sigh*"
    dez.name "Maybe. I can replace them. But still valuable. If for [tucker.name] then yes, it for you then what I get for it?"
    pc "You want me to give something for them?"
    dez.name "Of course. I not give my things for free. I need also."
    "DEV NOTE*** If the ali quest is still active, he will want you to help him with Ali before he gives you tools."
    "If the ali quest is complete and you sided with him, he will give them freely."
    "If you sided with Ali, he will demand a high price/sex. But Ali will give freely if you ask her."
    "If you sided with neither, he will demand a normal price or sex."
    hide dez
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
