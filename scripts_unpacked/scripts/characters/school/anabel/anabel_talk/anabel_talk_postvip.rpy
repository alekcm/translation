



label anabel_talk_post_vip_0:
    $ anabel.dict["dance_vip_post"] += 1
    pc "Don't really blame you not going to the parties."
    anabel.name "What about the other girls?"
    pc "Not sure about [dani.nname], but I imagine [svet.nname] agrees with you."
    anabel.name "You think so?"
    pc "Yeah, she has never pushed for anything the entire time. Mostly been [dani.nname] and her need for cash."
    anabel.name "Hmmm..."
    jump anabel_talk_end

label anabel_talk_post_vip_1:
    $ anabel.dict["dance_vip_post"] += 1
    anabel.name "What about [rachel.name]?"
    pc "I don't think she cares much about anything."
    anabel.name "Ha, true. Probably why no matter what, she always seems so happy."
    pc "Yeah."
    jump anabel_talk_end

label anabel_talk_post_vip_2:
    $ anabel.dict["dance_vip_post"] += 1
    anabel.name "[dani.nname]... Why do you think she cares if I am not going to the party?"
    pc "Honestly, I think she just wants her friend with her."
    anabel.name "But why? She knows I don't like doing this stuff."
    pc "Yeah, she knows. But do you think she likes it?"
    anabel.name "What do you mean?"
    jump anabel_talk_end

label anabel_talk_post_vip_3:
    $ anabel.dict["dance_vip_post"] += 1
    pc "[dani.nname] hates all of this stuff just as much as you do."
    anabel.name "No she doesn't. She is always trying to go to these kinds of places or doing weird things."
    pc "And you think she does it because she likes it?"
    anabel.name "Why else would she?"
    pc "..."
    jump anabel_talk_end

label anabel_talk_post_vip_4:
    $ anabel.dict["dance_vip_post"] += 1
    pc "When you have spoken to her about this stuff, does she ever sound happy or excited for the next time?"
    anabel.name "Huh, what do you mean?"
    pc "It's a simple question. When you speak to her about this, does she have an excited look on her face or happily tell you about things?"
    anabel.name "But then why does she keep going?"
    pc "Not the question I am asking."
    jump anabel_talk_end

label anabel_talk_post_vip_5:
    $ anabel.dict["dance_vip_post"] += 1
    pc "I think you really need to speak to [dani.nname] about this stuff."
    anabel.name "But why?"
    pc "Because she hates all this stuff just as much as you do."
    anabel.name "No, she always wants to go."
    pc "You call [dani.nname] your friend..."
    jump anabel_talk_end

label anabel_talk_post_vip_6:
    $ anabel.dict["dance_vip_post"] += 1
    $ anabel.dict["dance_vip_post_dani_conv_date"] = t.day
    anabel.name "[dani.nname] is my friend... Or was... I don't know..."
    pc "Doesn't sound like you understand anything she is going through."
    anabel.name "I do! She just always wants..."
    pc "Stop. You are just imagining what you want. Seems you have no intention of actually understanding her."
    anabel.name "..."
    jump anabel_talk_end





label anabel_talk_postvip_dani_reconcile_chain_0:
    $ anabel.dict["anabel_post_vip_dani_reconcile_chain"] += 1
    anabel.name "Thanks [name]."
    pc "Err, you're welcome. What did I do?"
    anabel.name "I had a chat with [dani.nname] after our conversation."
    pc "Oh..."
    jump anabel_talk_end

label anabel_talk_postvip_dani_reconcile_chain_1:
    $ anabel.dict["anabel_post_vip_dani_reconcile_chain"] += 1
    anabel.name "Maybe I was being a bit selfish."
    pc "Maybe."
    anabel.name "[dani.nname] has been going through a lot."
    pc "I know..."
    anabel.name "She tried to tell me but I didn't really listen. I was just too angry."
    jump anabel_talk_end

label anabel_talk_postvip_dani_reconcile_chain_2:
    $ anabel.dict["anabel_post_vip_dani_reconcile_chain"] += 1
    pc "Well whatever. I'm glad you are both talking again."
    anabel.name "Yeah... So am I."
    pc "..."
    anabel.name "She told me how you looked after her."
    pc "All I did was ply her with lots of wine."
    anabel.name "Haha."
    jump anabel_talk_end

label anabel_talk_postvip_dani_reconcile_chain_3:
    $ anabel.dict["anabel_post_vip_dani_reconcile_chain"] += 1
    anabel.name "I think I might rejoin the outings."
    pc "Really? It's not like anything has changed."
    anabel.name "I know..."
    pc "Yet you will still come? Don't get angry at us if something bad happens."
    anabel.name "Ugh..."
    jump anabel_talk_end

label anabel_talk_postvip_dani_reconcile_chain_4:
    $ anabel.dict["anabel_post_vip_dani_reconcile_chain"] += 1
    anabel.name "Speaking to [dani.nname], looking at [rachel.name] and hearing some things about you..."
    anabel.name "Kinda realise this bad stuff is already happening all around me."
    pc "Well yeah. We live in a shithole. Took you this long to realise?"
    anabel.name "No, but it's easy to think this sort of thing only happens to other people who you don't care about."
    pc "There isn't a person between here and the wall that isn't going through shit and getting screwed over."
    anabel.name "..."
    jump anabel_talk_end

label anabel_talk_postvip_dani_reconcile_chain_5:
    $ anabel.dict["anabel_post_vip_dani_reconcile_chain"] += 1
    anabel.name "Well, I am maybe thinking if we are going to live such a horrible life, it would be better together."
    pc "Probably."
    anabel.name "Yeah..."
    anabel.name "So even though I don't like it. Maybe it will be better I come along with you all."
    pc "On the plus side, I'm sure those tits will earn a fortune."
    anabel.name "Don't make me change my mind!"
    $ remove_from_list(anabel.list, "dance_event_refuse")
    jump anabel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
