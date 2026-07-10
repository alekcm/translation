label rachel_talk_picker:


    if not "rachel_gloryhole_talk" in rachel.dict:
        $ rachel.dict["rachel_gloryhole_talk"] = 0
    if not "rachel_exhib_talk" in rachel.dict:
        $ rachel.dict["rachel_exhib_talk"] = 0
    if not "rachel_exhib_try" in rachel.dict:
        $ rachel.dict["rachel_exhib_try"] = 0
    if not "rachel_exhib_inside_talk" in rachel.dict:
        $ rachel.dict["rachel_exhib_inside_talk"] = 0
    if not "rachel_talk_exhib_chain" in rachel.dict:
        $ rachel.dict["rachel_talk_exhib_chain"] = 0
    if not "rachel_talk_exhib_games_chain" in rachel.dict:
        $ rachel.dict["rachel_talk_exhib_games_chain"] = 0
    if not "rachel_bitching_talk" in rachel.dict:
        $ rachel.dict["rachel_bitching_talk"] = 0
    if not "rachel_homeless_talk" in rachel.dict:
        $ rachel.dict["rachel_homeless_talk"] = 0



    show rachel at right1 with dissolve

    if not any([player.has_perk([perk_bimbo, perk_slut, perk_sucu, perk_princess]), rachel.love > 30, player.int < 20]):
        jump rachel_talk_reject
    if "exhib_wait_outside" in rachel.list and loc(loc_school):
        jump rachel_talk_exhib_show
    jump expression WeightedChoice([

    ("rachel_talk_subject", 100),

    
    ("rachel_talk_homeless_" + str(rachel.dict["rachel_homeless_talk"]), If(renpy.has_label("rachel_talk_homeless_" + str(rachel.dict["rachel_homeless_talk"])) and rachel.love > 50, 200, 0)),
    
    
    ("rachel_talk_gloryhole_" + str(rachel.dict["rachel_gloryhole_talk"]), If(renpy.has_label("rachel_talk_gloryhole_" + str(rachel.dict["rachel_gloryhole_talk"])) and rachel_here(loc_school_toilet_girls), 1000, 0)),
    
    
    ("rachel_talk_exhib_" + str(rachel.dict["rachel_exhib_talk"]), If(loc_school_secret_entrance.visited and rachel.love >= 60 and not svet_here() and renpy.has_label("rachel_talk_exhib_" + str(rachel.dict["rachel_exhib_talk"])), 1000, 0)),
    ("rachel_talk_exhib_inside_talk_" + str(rachel.dict["rachel_exhib_inside_talk"]), If("exhib_inside_academy" in rachel.list and t.hour > 20 and t.day > rachel.dict["rachel_exhib_try"] and renpy.has_label("rachel_talk_exhib_inside_talk_" + str(rachel.dict["rachel_exhib_inside_talk"])), 5000, 0)),
    ("rachel_talk_exhib_strip", If(rachel_exhib_stripping_show() and not c.nude, 5000, 0)),
    ("rachel_talk_exhib_chain_start_" + str(rachel.dict["rachel_talk_exhib_chain"]), If(renpy.has_label("rachel_talk_exhib_chain_start_" + str(rachel.dict["rachel_talk_exhib_chain"])) and loc(loc_school_gym) and rachel_exhib_stripping_show(), 1000, 0)),
    
    
    ("rachel_talk_bitching_" + str(rachel.dict["rachel_bitching_talk"]), If(renpy.has_label("rachel_talk_bitching_" + str(rachel.dict["rachel_bitching_talk"])) and "can_bitch" in rachel.list, 100, 0)),
    
    ("rachel_talk_exhib_subject", If(rachel_exhib_stripping_show() and c.nude and loc(loc_school_gym), 100, 0)),
    
    ])

label rachel_talk_subject:
    jump expression WeightedChoice([
    
    
    ("rachel_talk_general_1", 100),
    ("rachel_talk_general_2", 100),
    ("rachel_talk_general_3", 100),
    ("rachel_talk_general_4", 100),
    ("rachel_talk_general_5", 100),

    
    ("rachel_talk_academy_1", If(dis(dis_school), 100, 0)),
    ("rachel_talk_academy_2", If(dis(dis_school), 100, 0)),

    
    ("rachel_talk_gen_gloryhole_1", If(loc_school_toilet_girls.has_gloryhole and not renpy.has_label("rachel_talk_gloryhole_" + str(rachel.dict["rachel_gloryhole_talk"])), 100, 0)),
    ("rachel_talk_gen_gloryhole_2", If(loc_school_toilet_girls.has_gloryhole and not renpy.has_label("rachel_talk_gloryhole_" + str(rachel.dict["rachel_gloryhole_talk"])), 100, 0)),
    ("rachel_talk_gen_gloryhole_3", If(loc_school_toilet_girls.has_gloryhole and not renpy.has_label("rachel_talk_gloryhole_" + str(rachel.dict["rachel_gloryhole_talk"])), 100, 0)),

    
    
    ("rachel_talk_person_dani_1", If(dani.has_met and dani.love > 10, 100, 0)),
    ("rachel_talk_person_dani_2", If(dani.has_met and dani.love > 10, 100, 0)),

    
    ("rachel_talk_person_anabel_1", If(dani.has_met and dani.love > 10, 100, 0)),

    
    ("rachel_talk_person_needle_1", If(saskia.has_met and frida.has_met, 100, 0)),
    ("rachel_talk_person_needle_2", If(saskia.has_met and frida.has_met, 100, 0)),

    
    ("rachel_talk_person_felix_1", If(felix.has_met, 100, 0)),
    ("rachel_talk_person_felix_2", If(felix.has_met, 100, 0)),

    
    ("rachel_talk_person_soccerboys_1", If(any([drake.name in rachel.sex_who, nate.name in rachel.sex_who, dan.name in rachel.sex_who]), 100, 0)),
    ("rachel_talk_person_soccerboys_2", If(any([drake.name in rachel.sex_who, nate.name in rachel.sex_who, dan.name in rachel.sex_who]), 100, 0)),
    ("rachel_talk_person_soccerboys_3", If(any([drake.name in rachel.sex_who, nate.name in rachel.sex_who, dan.name in rachel.sex_who]), 100, 0)),

    
    ("rachel_talk_sex_drake", If(drake.setname in rachel.conversation_topics and not "told_sex_" + drake.setname in rachel.conversation_topics,500,0)),
    ("rachel_talk_sex_nate", If(nate.setname in rachel.conversation_topics and not "told_sex_" + nate.setname in rachel.conversation_topics,500,0)),
    ("rachel_talk_sex_dan", If(dan.setname in rachel.conversation_topics and not "told_sex_" + dan.setname in rachel.conversation_topics,500,0)),
    ("rachel_talk_sex_forced", If("rape" in rachel.conversation_topics,500,0)),
    ("rachel_talk_sex_lover", If("lover" in rachel.conversation_topics,500,0)),
    ("rachel_talk_sex_groper", If("groper" in rachel.conversation_topics,500,0)),
    
    
    ("rachel_talk_preg_soccer", If(any(item in ["pregnant_" + drake.setname, "pregnant_" + nate.setname, "pregnant_" + dan.setname] for item in rachel.conversation_topics), 1000, 0)),


    ])





label rachel_talk_reject:
    jump expression WeightedChoice([

    ("rachel_talk_reject_1", 100),
    ("rachel_talk_reject_2", 100),
    ])

label rachel_talk_reject_1:
    rachel.name "Heya [name]!"
    pc "Hey..."
    pc "..."
    jump rachel_talk_reject_end

label rachel_talk_reject_2:
    rachel.name "[name]!"
    pc "Hey [rachel.name]."
    jump rachel_talk_reject_end

label rachel_talk_reject_end:


    $ relax(20, If(numgen(), rachel, None))
    $ player.face_worried()
    $ dialouge = renpy.random.choice([
    "We stand there having a bit of an awkward conversation. It's clear we don't really connect.",
    "We chat a bit, but conversation is strained and it is a bit awkward.",
    "We have a bit of small talk before an awkward silence.",
    "We talk about random stuff, but don't really have any topics we can connect on."
    ])
    "[dialouge]"
    hide rachel with dissolve
    jump travel





label rachel_talk_general_1:
    rachel.name "You know somewhere else to dance?"
    pc "Huh? Not sure I do."
    rachel.name "I wanna do like they did before. Nightclubs!"
    rachel.name "Go out and drink. Dance. Sounded like fun."
    pc "Yeah, wake up in bed the next day with a guy whose name you didn't catch."
    rachel.name "Yeah!"
    jump rachel_talk_end

label rachel_talk_general_2:
    rachel.name "[svet.nname] is always telling me off."
    pc "Err... Well you do get up to some weird stuff."
    rachel.name "And?"
    pc "Err, and nothing."
    jump rachel_talk_end

label rachel_talk_general_3:
    rachel.name "[name]!"
    pc "Hey, what you up to?"
    rachel.name "Nothing. Is there something fun to do?"
    pc "Probably not."
    jump rachel_talk_end

label rachel_talk_general_4:
    rachel.name "People out there are weird!"
    pc "That's why it's nice hanging out in here."
    rachel.name "They can be fun though."
    pc "If you don't mind being dragged into an alleyway, sure."
    jump rachel_talk_end

label rachel_talk_general_5:
    rachel.name "People out there are weird!"
    pc "That's why it's nice hanging out in here."
    rachel.name "They can be fun though."
    pc "If you don't mind being dragged into an alleyway, sure."
    jump rachel_talk_end




label rachel_talk_academy_1:
    rachel.name "Why do people come here?"
    pc "Same reason as you probably."
    rachel.name "I came here cos [svet.nname] told me to."
    pc "Oh?"
    jump rachel_talk_end

label rachel_talk_academy_2:
    rachel.name "Can still have fun here though."
    pc "What do you mean?"
    rachel.name "Lots of boys, lots of girls. And they put us in this place all alone."
    rachel.name "It's kind of like a party."
    pc "Err, sure it is."
    jump rachel_talk_end




label rachel_talk_gen_gloryhole_1:
    rachel.name "Way more fun in this place now the boys are putting their dicks in the hole."
    pc "I bet. You been having fun in there?"
    rachel.name "Of course!"
    jump rachel_talk_end

label rachel_talk_gen_gloryhole_2:
    rachel.name "The boys sometimes put their hand in the hole."
    pc "Oh? Why do they do that?"
    rachel.name "No idea. I can't suck their hand."
    pc "Maybe they want to touch you?"
    rachel.name "I don't care what they want."
    jump rachel_talk_end

label rachel_talk_gen_gloryhole_3:
    rachel.name "I get some money from the holes though. I can buy fun stuff!"
    pc "Yeah. And probably better than some jobs."
    rachel.name "Blowjobs is the best job!"
    pc "Ha, yeah."
    jump rachel_talk_end





label rachel_talk_person_dani_1:
    rachel.name "[dani.name] can actually dance!"
    pc "Yeah, she's pretty good."
    rachel.name "Maybe I should practice more."
    pc "Maybe. Do you care though?"
    rachel.name "Not really."
    jump rachel_talk_end

label rachel_talk_person_dani_2:
    rachel.name "[dani.name] lives near you?"
    if loc_kitchen.locked:
        pc "Err, used to. I got kicked out for not paying rent."
        pc "She lives in the same complex I used to though."
    else:
        pc "Err, yeah. In the same complex."
    rachel.name "You should go out and have some fun with her."
    pc "Not sure we have the same idea of what's fun."
    rachel.name "She's cute. The guys will love her."
    jump rachel_talk_end

label rachel_talk_person_anabel_1:
    rachel.name "I don't think [anabel.name] likes me."
    pc "Err, probably not."
    rachel.name "Why not?!"
    pc "Err, she's kinda scared of guys."
    rachel.name "I'm not a guy!"
    pc "Yeah... But you like having fun with them."
    rachel.name "Sure I do. What does that matter?"
    pc "Errr... No idea..."
    jump rachel_talk_end

label rachel_talk_person_needle_1:
    rachel.name "So glad the girls upstairs sell clothes for cheap."
    pc "Why is that?"
    rachel.name "I can't afford expensive stuff and keep losing mine."
    pc "Maybe keep them on more often, then you wont lose them."
    rachel.name "Pfft. Don't be silly!"
    jump rachel_talk_end

label rachel_talk_person_needle_2:
    rachel.name "The girls upstairs sometimes give me free stuff."
    pc "Really?"
    rachel.name "Yeah, they make me dress in weird things first."
    pc "Oh, wow. Yeah they do have weird tastes."
    rachel.name "I should steal their clothes!"
    jump rachel_talk_end

label rachel_talk_person_felix_1:
    rachel.name "When can your photo boyfriend take photos of me?"
    pc "Err, he would probably be happy to."
    rachel.name "I asked. He got scared of me."
    pc "Really?"
    rachel.name "Yeah. I think he was scared I would do something bad."
    pc "You absolutely would do something bad!"
    jump rachel_talk_end

label rachel_talk_person_felix_2:
    rachel.name "I want to shake my ass on camera."
    pc "That's probably why he's scared of you."
    rachel.name "He doesn't like my ass??"
    pc "Err, not sure. But on camera he has to keep things innocent."
    rachel.name "I am innocent!"
    pc "Sure you are."
    jump rachel_talk_end

label rachel_talk_person_soccerboys_1:
    rachel.name "Those boys love their beer."
    pc "Yeah they do. Seems like you do too."
    rachel.name "But it's all they do."
    pc "That and fuck you."
    rachel.name "Haha, it's the only reason I drink the beer with them."
    jump rachel_talk_end

label rachel_talk_person_soccerboys_2:
    rachel.name "Why do they play football?"
    pc "Err, fun I guess?"
    rachel.name "There are no teams to play with."
    pc "No, don't think there is."
    rachel.name "Seems silly."
    jump rachel_talk_end

label rachel_talk_person_soccerboys_3:
    rachel.name "Should send the boys to the pub."
    pc "Why?"
    rachel.name "Have a big fun night out like before."
    pc "Ah, yeah that would be nice actually."
    jump rachel_talk_end







label rachel_talk_homeless_0:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "Where do you live anyway?"
    rachel.name "Huh? I live here."
    pc "I mean where in the city. You don't talk about your place."
    rachel.name "My place? What do you mean?"
    pc "Err, your home."
    rachel.name "Oh? I don't have one of those."
    jump rachel_talk_end

label rachel_talk_homeless_1:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "What do you mean you don't have one of those?"
    rachel.name "Huh? One of what?"
    pc "A home. Where do you sleep at night?"
    rachel.name "Hmm, dunno. Places."
    pc "..."
    jump rachel_talk_end

label rachel_talk_homeless_2:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "So you sleep in places? What? Like in the bushes?"
    rachel.name "Sometimes."
    pc "Err, I was just joking..."
    rachel.name "It rains a lot though."
    pc "..."
    jump rachel_talk_end

label rachel_talk_homeless_3:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "So you don't live in an apartment or anything?"
    rachel.name "Of course not."
    pc "Err, why not?"
    rachel.name "I don't have one."
    pc "You can pay for one."
    rachel.name "I don't have money."
    jump rachel_talk_end

label rachel_talk_homeless_4:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "Don't have money? You don't work or anything?"
    rachel.name "Not really. I'm not very good at it."
    pc "So... You just sleep in the bushes instead?"
    rachel.name "Nooo. Not always."
    jump rachel_talk_end

label rachel_talk_homeless_5:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "Okay, not always sleeping in the bushes. So where?"
    rachel.name "I try to meet some nice guy and stay at his place."
    pc "Oh..."
    pc "Why not just get the guy to pay you?"
    rachel.name "Why would he do that?"
    pc "Men will pay for company."
    rachel.name "No they wont, silly!"
    jump rachel_talk_end

label rachel_talk_homeless_6:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "Men will pay. You have a lot of girls at the highway for that."
    rachel.name "Oh? I went there once. They beat me up."
    pc "The guys did?"
    rachel.name "No, the girls. They didn't like me."
    pc "Why not?"
    rachel.name "Dunno."
    jump rachel_talk_end

label rachel_talk_homeless_7:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "Well, sometimes men will pay for sex."
    rachel.name "Why would they do that?"
    pc "To... Err, to fuck you?"
    rachel.name "They don't need money for that."
    pc "But they could."
    rachel.name "But I don't cost money. That's weird."
    pc "Right..."
    jump rachel_talk_end

label rachel_talk_homeless_8:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "There is also the slum near the highway."
    rachel.name "Yeah. I stayed there a few times."
    pc "Oh? Why not more often?"
    rachel.name "They steal my clothes and fuck me while I sleep."
    rachel.name "I am always so tired in the morning with them doing funny things."
    jump rachel_talk_end

label rachel_talk_homeless_9:
    $ rachel.dict["rachel_homeless_talk"] += 1
    pc "So it's safer to sleep in the park bushes?"
    rachel.name "Not always the bushes! Sometimes someone's house, an alleyway or go into an old building."
    pc "And no one joins you at night?"
    rachel.name "If they find you they will."
    rachel.name "Better to sleep naked so they can't steal your clothes."
    pc "..."
    jump rachel_talk_end





label rachel_talk_sex_drake:
    rachel.name "Soooo..."
    if "told_sex_" + rachel._original_name in drake.conversation_topics:
        pc "Something to tell me?"
        rachel.name "Oh?"
        if player.isslut:
            pc "I heard a story about one of my friends fucking a dirty little slut."
        else:
            pc "Someone has been having fun."
        rachel.name "Ahh he told you?"
        $ player.face_happy()
        pc "Of course."
        rachel.name "Hah."
    elif player.isslut:
        show rachel at right6 with dissolve
        rachel.name "I flirted with that boy you like fucking."
        pc "Err, what one?"
        rachel.name "The blondie. [drake.name]."
        pc "Ah, you fucking him now too?"
        rachel.name "Yeah. Cant let you hog all the fun."
    else:
        rachel.name "So I have been chatting to that boy you hang out with."
        pc "Err, what one?"
        rachel.name "The blondie. [drake.name]."
        pc "Ok?"
        rachel.name "Err, nothing..."
    $ remove_from_list(rachel.conversation_topics, drake.name)
    $ add_to_list(rachel.conversation_topics, "told_sex_" + drake.name)
    jump rachel_talk_end

label rachel_talk_sex_nate:
    rachel.name "Soooo..."
    if "told_sex_" + rachel._original_name in nate.conversation_topics:
        pc "Something to tell me?"
        rachel.name "Oh?"
        if player.isslut:
            pc "I heard a story about one of my friends fucking a dirty little slut."
        else:
            pc "Someone has been having fun."
        rachel.name "Ahh he told you?"
        $ player.face_happy()
        pc "Of course."
        rachel.name "Hah."
    elif player.isslut:
        show rachel at right6 with dissolve
        rachel.name "I flirted with that boy you like fucking."
        pc "Err, what one?"
        rachel.name "The pretty boy. [nate.name]."
        pc "Ah, careful with that one. He's a dirty pervert."
        rachel.name "That a bad thing?"
        pc "Well, no. I guess not."
    else:
        rachel.name "So I have been chatting to that boy you hang out with."
        pc "Err, what one?"
        rachel.name "The pretty boy. [nate.name]."
        pc "Two perverts chatting. Only one way that ends."
        rachel.name "Ha, right?"
    $ remove_from_list(rachel.conversation_topics, nate.name)
    $ add_to_list(rachel.conversation_topics, "told_sex_" + nate.name)
    jump rachel_talk_end

label rachel_talk_sex_dan:
    rachel.name "I started talking to that [dan.name] that you like hanging out with."
    pc "Oh? He can be a bit difficult to talk to. Doesn't say a lot."
    rachel.name "Oh? So wasn't just me then."
    if player.isslut:
        pc "Na, someone like his it's better to just tell him what you want and not play the usual games."
        rachel.name "Ah really?"
        pc "You want to fuck him I guess?"
        rachel.name "Well, we fooled about but dunno about him."
        pc "Just tell him to fuck you then all good."
        show rachel happy
        rachel.name "Okay~"
    else:
        pc "So? What you been chatting about?"
        show rachel happy
        rachel.name "Well, was less chatting and more..."
        pc "Okay okay..."
    $ remove_from_list(rachel.conversation_topics, dan.name)
    $ add_to_list(rachel.conversation_topics, "told_sex_" + dan.name)
    jump rachel_talk_end

label rachel_talk_sex_lover:
    show rachel happy
    rachel.name "I met some guy!"
    pc "Err, okay. Is that unusual?"
    $ temp_var_1 = numgen(1,4)
    if temp_var_1 == 1:
        rachel.name "We met in the park and went to the toilets together?"
        pc "Oh? Kind of a nasty place to have some fun."
        rachel.name "I was wearing a skirt so I didn't have to undress and put clothes somewhere."
        rachel.name "I saw more of the nasty wall than his face."
        pc "Haha!"
    elif temp_var_1 == 2:
        rachel.name "I didn't even know his name. Some trucker guy."
        rachel.name "Went in the back of his truck and he had a bed there."
        pc "Oh? Better place than most."
    elif temp_var_1 == 3:
        rachel.name "Some drunk guy came up and asked how much I cost."
        pc "Oh?"
        rachel.name "Idiot. I don't cost. What a silly question."
        pc "Bet that made him happy."
        rachel.name "Why would it make him happy? Anyway we went into some alleyway. Kinda smelled like piss."
    elif temp_var_1 == 4:
        rachel.name "He came up to me asking if I want some fun."
        pc "Oh?"
        rachel.name "I love having fun. Rather have sex though."
        pc "Err, I think that's the same thing."
        rachel.name "Fun is like... Dunno, talking or jokes or something. I fucked him instead."
    $ remove_from_list(rachel.conversation_topics, "lover")
    jump rachel_talk_end

label rachel_talk_sex_groper:
    rachel.name "These morning bus rides can really be fun."
    pc "You been doing weird things on the bus?"
    rachel.name "Me? No!"
    rachel.name "Other people do."
    pc "And I bet you just let them."
    rachel.name "Of course! Good start to the day."
    rachel.name "Although I keep having to buy new knickers."
    $ remove_from_list(rachel.conversation_topics, "groper")
    jump rachel_talk_end

label rachel_talk_sex_forced:
    rachel.name "These people can be so not fun!"
    pc "Huh? What people?"
    show rachel angry
    rachel.name "People that live here."
    pc "Err, okay. Why?"
    rachel.name "I got pulled into some smelly alleyway. Wasn't very fun."
    pc "Oh? You okay?"
    rachel.name "They could just be nicer!"
    show rachel neutral
    $ remove_from_list(rachel.conversation_topics, "rape")
    jump rachel_talk_end





label rachel_talk_preg_soccer:
    rachel.name "So..."
    show rachel worried
    rachel.name "..."
    pc "Err. What's the problem"
    rachel.name "Maybe you can help me with telling the father I am preggo."
    pc "Do I know who it is?"
    show rachel neutral
    rachel.name "It's [rachel.pregnant_who.name]'s baby."
    $ player.face_shock()
    pc "Oooooohhh..."
    if player.preg_knows and player.preg_father_class == rachel.pregnant_who:
        $ player.face_angry()
        pc "That bastard."
        rachel.name "What?"
        pc "Who you think knocked me up?"
        show rachel happy
        rachel.name "Really? Hahahha. Lucky shit."
        pc "Hrmf!"
    else:
        $ player.face_neutral()
        pc "Yeah sure. I'll have a chat with him."
        rachel.name "Thanks."
    $ remove_from_list(rachel.conversation_topics, "pregnant_" + rachel.pregnant_who._original_name)
    $ add_to_list(rachel.pregnant_who.conversation_topics, "pregnant_" + rachel._original_name)
    jump rachel_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
