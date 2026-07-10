default main_quest_03_qs = 0

label main_quest_03_fixer:
    $ main_quest_03.stage = 1
    $ walk(loc_hospital_office)
    $ log.markdone("mq_03_a")
    show tucker at right1 with dissolve

    tucker.name "[fname], I'm glad to see you. Lock the door behind you and have a seat."
    $ player.face_shock()
    pc "I didn't expect you to be such a pervert [tucker.name]. We learned about people like you at school."
    $ player.face_worried()
    tucker.name "I am going to fill you in on a lot of the details we have been keeping from you."
    $ player.face_frown()
    pc "Nothing? Eh, no humour..."
    tucker.name "Tell me, how much do you know about [town]?"
    $ player.face_neutral()
    pc "Err, just what I see around me. Small town in the middle of nowhere. Half a million people living here at most."
    tucker.name "Hmm, well there is a lot more to the town than that. Prior to the Plague, [town] was chosen to be the site of a private research institute. I am sure you know what we were tasked with researching."
    pc "Actually no. I mean I can of course guess that my body is the result of it. But what the hell for I can't imagine."
    tucker.name "What for was never divulged to us either. And in the aftermath of the Plague, none of it mattered any more. You see, we were a division of the government and most likely a black project."
    tucker.name "But once the Plague hit, a small military detachment was assigned to protect us and the research."
    tucker.name "But instead of hiding away, we converted much of our building into wards and treated the sick while under the protection of the military."
    tucker.name "Then as you should have learned in school, a huge portion of the population died, including many working in The Institute and all the major cities became graveyards."
    tucker.name "During this time, it seems those in the government no longer realised what our true purpose was."
    tucker.name "I can only guess that those in the know died, and being that we were a black project there were no records of our true goals."
    tucker.name "Eventually a vaccine was discovered, but there was still the problem of creating enough of it and delivering it where needed. And this is where our secret purpose came in useful."
    tucker.name "Unlike most normal hospitals, our \"secret\" research labs were equipped with state of the art equipment. Such that we could produce the vaccine here. As you can imagine, this saved a lot of lives."
    tucker.name "We sent what military was left along with the remnants of the police force, fire department and other groups and aggressively inoculated as many people as we could."
    $ player.face_worried()
    pc "Aggressively?"
    tucker.name "Yes..."
    pc "Dare I ask?"
    tucker.name "It's better you don't..."
    pc "Ok..."
    tucker.name "Ahem. This also meant that we were well on our way to recovery while the rest of the country was still in flames. So the people then looked to us for guidance."
    $ player.face_frown()
    pc "Guidance? You mean governance?"
    tucker.name "I do. Much of what you see around you today is thanks to the hard work of The Institute and its local benefactors."
    tucker.name "By all coming together we managed to avoid most of the harsh realities the rest of the country suffered or is still suffering."
    pc "But what about now? The government can't be too happy with you having so much local power."
    tucker.name "The government has bigger issues to worry about. We pay taxes, have open trade and don't create problems. So there is no reason for them to care what we do."
    pc "Pay taxes?"
    tucker.name "Of course. We aren't some breakaway state. There is no way we could survive like that without major infrastructure changes."
    tucker.name "We very much work with and support the government. We just maintain local power while the government is incapable of doing so."
    pc "Ok, so that's all well and good. What does any of that have to do with me?"
    tucker.name "Yes, I am getting there. As you might expect, we do not govern alone."
    tucker.name "We rely heavily on many of the local organisations. The military that helped us through the Plague is now what consists of a police force."
    tucker.name "We also rely on the couriers and delivery drivers. The train workers, mechanics... The list goes on."
    tucker.name "If The Institute is the body, then these groups are our arms. We all work together to keep this local region alive and prosperous. But it is not without its problems."
    tucker.name "And this is where you come in. There are times where we need issues solved between The Institute and one of its arms. The person to deal with these issues will be you."
    pc "Ok, you can't use the police since the issue might be with the police. But that doesn't change the fact that I am not qualified to do this."
    tucker.name "No? You mean someone who can change their appearance to suit a mission who we can fully trust is not qualified?"
    pc "I can't fight or use a gun and I am the least intimidating person in any room. How am I supposed to deal with such conflicts?"
    tucker.name "..."
    pc "Even you agree."
    tucker.name "No, not quite. It just reminded me of something else I needed to tell you."
    if quest_homeless_start.active:
        tucker.name "You didn't see the body we made before it expired, but we had one in mind for a possible fixer."
        pc "Oh?"
        tucker.name "And honestly, you are not that far different to what we had made."
    else:
        tucker.name "Of all the bodies we could create, we made this one. Did you ever wonder why?"
        pc "..."
        pc "Honestly... I assumed it was supposed to be a sex doll."
        tucker.name "*COUGH*"
        tucker.name "Ahem..."
        tucker.name "..."
        $ player.face_worried()
        pc "Wow. Was I right?"
        tucker.name "Not quite. But not far off the truth either."
        $ player.face_frown()
    tucker.name "If we send someone to deal with an issue who are intimidating, then it looks like we are sending subtle threats and people will be a lot less cooperative."
    tucker.name "We need people to work with us after all. Anyone working against us is a problem."
    tucker.name "We felt we needed someone as non-threatening as possible while also being as likeable as possible. The more people like you, the more they are willing to help you."
    tucker.name "Most people you will deal with will be men, so having female charm is a must."
    pc "..."
    tucker.name "Not very imposing so people are not instantly afraid of you."
    tucker.name "Young so that people are more likely to try to teach you or explain things to you. Either that or underestimate you."
    tucker.name "Attractive so that people are more likely to desire you. If they desire you they are more likely to try and please you."
    if quest_homeless_start.active:
        tucker.name "So you say you are not qualified? The body we designed specifically for this job is not far off what you are. The rest is entirely up to you as a person."
    else:
        tucker.name "So you say you are not qualified? The body you are in was designed specifically for this job. The rest is entirely up to you as a person."
    tucker.name "We don't need or even want someone \"to fight or use a gun\". Just the opposite. We need someone to charm, seduce or manipulate people. Someone who can gain others' trust."
    pc "..."
    pc "Seduce...?"
    if simon.rape > 0:
        tucker.name "Yes, while what happened with [simon.fullname] was unfortunate, your body is a tool you might have to use in future missions."
    elif simon.naughty:
        tucker.name "Yes, in your last mission you already made use of it. It is something that might be required in the future as well."
    else:
        tucker.name "Yes, it is something you might have to make use of in the future."
    pc "But is that ok?"
    tucker.name "How you complete the mission is up to you. There will be no judgement from me. Do what you feel is necessary and use all of the tools you have available."
    tucker.name "And while you have the right not to do a mission if you choose, there will no doubt be tasks required of you where it will be impossible to not make use of your body."
    pc "..."
    tucker.name "Anyway. I think that is everything I need to explain. Let's get you paid."
    pc "Yes, let's."
    tucker.name "Here you go. Since you might have different names depending on your mission, you will be paid as \"The Fixer\" and not [fname] [sname]."
    tucker.name "But you are still an official employee of The Institute and considered under our protection."
    pc "\"The Fixer\"?"
    tucker.name "Yes, back in the day large companies used to have people called fixers. They used to solve sensitive issues that couldn't be dealt with by company employees."
    tucker.name "We decided to use the same term since the job is similar."
    pc "Ok, so I am \"The Fixer\"? Hmmm. \"The\" and not \"A\"? There are no others?"
    tucker.name "No, you are the first and only."
    pc "Ok, so what is my next mission?"
    tucker.name "Go home first and think over what we talked about. If you are still willing to work for us, then come and pay me a visit."
    tucker.name "And before I forget, here is your payment for the [simon.fname] mission."
    $ player.add_money(2000)
    pc "Ok. One last question."
    if quest_homeless_start.active:
        pc "You designed a body with a specific purpose but then left it to rot. Did something happen?"
    else:
        pc "You designed this body with a specific purpose but put me in it. Was someone else supposed to use it?"
    tucker.name "Yes."
    pc "And?"
    tucker.name "Remember how much importance I put on trust?"
    pc "Yes..."
    tucker.name "Goodbye [fname]."
    $ player.face_worried()
    pc "..."
    hide tucker
    $ walk(loc_hospital_lobby)
    with dissolve
    $ main_quest_03.stage = 2
    $ main_quest_03.stagedesc = "Think over what you have been told."

    jump travel

label main_quest_03_fixer_home:
    $ player.face_frown()
    pc "Ugh, that meeting with [tucker.name] was an odd one. He seems to be putting a lot of faith in me."
    pc "Is he an idiot or am I really capable of doing what he expects?"
    pc "He did mention he doesn't expect any fighting but instead to charm people..."
    pc "Sounding like a real femme fatale now. Using her body to bend those to her will."
    if player.preg_father_class == simon and player.preg_knows:
        pc "Well, I did let [simon.name] fuck a baby into me for some useless information so [tucker.name] is probably right about me."
    elif player.preg_father_class == bob and player.preg_knows:
        pc "Well, I did let [bob.name] fuck a baby into me so I could get some extra money. So [tucker.name] is probably right about me."
    elif simon.sex:
        pc "Well, I did let [simon.name] fuck me just for some useless information so [tucker.name] is probably right about me."
    elif bob.sex:
        pc "Well, I did end up getting paid by [simon.name] to fuck [bob.name]. So maybe [tucker.name] is right about me."
    elif main_quest_01.naughty:
        pc "Well, I did fool around while on the mission so [tucker.name] is probably right about me."
    else:
        pc "I wonder if I am capable of doing such a thing..."
    pc "Ah well, I suppose if it's something I am willing to do then I should just go and see him. He was right about the pay being good."
    pc "..."
    pc "Ugh, makes me sound like a whore..."
    $ log.markdone("mq_03_b")
    $ main_quest_04.activate()
    $ main_quest_03.complete()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
