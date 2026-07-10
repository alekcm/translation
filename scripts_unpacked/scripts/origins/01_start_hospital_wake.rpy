screen origin_debug:
    hbox:
        text "conf [player.confidence]"
        text "love [emile.love]"

define origin_start_tutorial = False




label start_hospital_intro:
    $ block_walk_music = True
    $ walk(loc_hospital_ward)


    play music music_intro

    show screen background_scene(_layer="bg_screen")
    show screen foreground_scene(_layer="fg_bg_screen")

    show screen blackout(100, _layer="master") with Dissolve(2)
    $ renpy.scene()
    show screen blackout(100, _layer="master")
    show nurse at right1
    $ weather_var = 1

    $ player.hair_fringe = numgen(1, 6)
    $ player._hair_length = numgen(1,35)
    $ player.hair_colour = random(hair_colours_custom_list)
    $ player.eye_colour = random(eye_colours_custom_list)
    $ player.breasts = numgen(1, 3)

    $ player.add_perk(perk_virgin)
    $ player.add_perk(perk_fresh, days=14)
    $ player.cycle_gamestart_randomiser()

    me "Uuuuuhhhhhh..."
    nurse.name "..."
    nurse.name "[nik.name]!"

    show screen blackout(number=75, _layer="master") with dissolve


    nurse.name "[nik.name]! The patient is starting to wake up."
    nurse.name "Don't worry, you are safe, the doctor is on his way now. You are in a hospital."
    me "Ung..."
    nurse.name "Doctor!"
    show nikolas at right3 with dissolve
    nik.name "Yes yes, I'm here. How's our patient looking? Heart rate normal... No respiratory distress..."
    show screen blackout(number=50, _layer="master") with dissolve
    nik.name "Things are looking good..."
    me "A hospital...? How...? What happened...?"
    nik.name "I'm afraid you were in a car accident and you were quite severely injured."
    me "How seriously? Is that why I can't feel my legs?"
    nik.name "Your legs...?"
    nik.name "Oh no no. Not to worry, that's just the medication we have you on. Your legs, and the rest of your body for that matter, should be fine."

    nik.name "But with that said, when you arrived your body was very badly hurt. I'm afraid had you had your accident anywhere else, we wouldn't be having this conversation."

    me "What do you mean? *Cough* How did you fix me?"
    show screen blackout(number=25, _layer="master") with dissolve
    nik.name "Well... We didn't fix you..."

    me "What?"
    nik.name "This institute that you are in isn't a typical hospital. More of a private research institute you see."
    nik.name "Because of the nature of our research, we were in a very unique position to help you."
    nik.name "Our research involves... well... specifically cases like yours. Someone whose body is injured beyond repair but whose mind is still perfectly functional."
    nik.name "I suppose you could call it a body swap or mind transplant, if you want it in layman's terms. But because you were not a planned procedure, we had to work with what we had available to us."
    nik.name "So I'm afraid the body we gave you might not have been your first choice."

    show screen blackout(number=0, _layer="master") with dissolve
    $ renpy.hide_screen("blackout", layer="master")

    me "My body? What? Can you start making sense!"
    nik.name "Ok. To put it even simpler, you were on the verge of death, so we put your mind in a new body."
    me "..."
    nik.name "I suppose it's probably best just to show you."
    "He gets a mirror from near my bed and hands it to me so I can see myself."
    mem "Why a mirror...?"
    me "Ugh..."
    mem "Huh, who is that in the mirror?"
    mem "I see a strange girl. She looks..."
    $ daily.outfit_primary_colour = "blue"
    $ c.outfit_primary_colour = "blue"
    $ c.outfit = 0
    $ player.add_fitness(25)
    $ player.brow = 3
    $ player.mouth = 8
    $ player.uncover()
    show screen pc_avatar(_layer="pc_avatar") with dissolve
    call screen surgery_screen()
    $ pc_strip()
    $ c.outfit = 1
    $ player.cover_reset()
    $ player.remove_fitness(100)
    nik.name "This is you in your new body."
    $ player.face_shock()
    me "What? New body?"
    me "But..."

    menu:
        "I didn't look like this! (Female origin)":
            $ player.male_origin = False
            $ player.add_conf(10)
            $ player.add_comfort(-50)
        "I'm a girl?! (Male origin)":

            $ player.male_origin = True
            $ player.add_comfort(-200)
            $ player.origin_perk = perk_male
            $ player.add_perk(perk_male)

    nik.name "As I mentioned earlier, we had to work with what we had available to us. With it being such an emergency, we had two choices, use the only body we had, or let you die."

    nik.name "I hope you can see why we picked the former option."
    $ player.mouth = 8
    me "..."
    me "... Yes..."
    nik.name "Wonderful, here now, drink this. It will perk you up a bit."
    nik.name "You have been in here for quite some time. We are quite eager to get you back on your feet."
    nurse.name "Your sister is out there waiting for you. She is dealing with some last minute details and paperwork."
    me "[emile.name]? Wasn't she in the car with me? Is she ok?"
    nurse.name "Yes she was fine. She actually had her seatbelt on so had only minor injuries."
    nurse.name "You on the other hand didn't, and were thrown out of the car where you got wrapped around a tree. Quite a gruesome sight."
    me "..."
    nurse.name "Well, you are alive now, that's all that counts, right?"
    menu:
        "I suppose so":

            $ player.add_conf(5)
            $ player.add_comfort(10)
            $ player.brow = 1
            me "I suppose so... Especially with the alternative being death..."
            nurse.name "That's the spirit! Who knows what could have happened if you hadn't arrived here."
            nurse.name "Personally I dread to think..."
        "...":

            nurse.name "I know it's a lot to process. But you are still here and that counts for something, right?"
        "But this isn't me!":

            $ player.add_comfort(-20)
            $ player.mouth = 2
            nurse.name "Now c'mon, it's not that bad. You are still you but you just look a little different that's all."

    me "..."
    $ player.brow = 1
    $ player.mouth = 8
    nurse.name "Anyway... Let's get you back on your feet and off to meet that sister of yours. She has been kicking up a fuss at least once a week trying to get you out of here."
    me "Wait. Once a week? How many weeks? How long have I been in here??"
    nurse.name "Hmm, quite a while I'm afraid. You came in somewhere around late autumn and it's nearly summer now. So about two seasons."
    $ player.mouth = 4
    me "Two sea..."
    nurse.name "We had to keep you under constant observation. You are the first and only person to have such a procedure you see."
    nurse.name "I think such a thing was only allowed because of the condition you came here in. I don't believe human trials have actually been approved yet, so you are a very unique case."
    nurse.name "Anyway... I think your sister is almost done with your discharge papers. So not long till we get you out of here."
    nurse.name "By the way, you might want to think of a new name for yourself. We have you down as Samantha for dealing with the legal paperwork. But now might be your last chance to change it."
    $ player.mouth = 8
    nurse.name "What do you think?"
    if not player.male_origin:
        me "What's wrong with my old name?"
        nurse.name "Nothing. Put that down if it's what you want to be called. We didn't know your real name until some time after the procedure and so the name \"Samantha\" ended up sticking."
    menu:
        "Samantha is fine":

            $ fname = "Samantha"
            $ name = "Sammy"
            jump start_hospital_3
        "I would prefer to name myself":

            jump start_hospital_2_q2





label start_hospital_2_q2:

    $ fname = renpy.input("What do you want your new first name to be?", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=12)
    $ fname = fname.strip()

    if fname == "":
        $ fname = "Samantha"

    $ name = renpy.input("[fname]. Okay got it, a bit formal though isn't it? What do you want people to normally call you? Something short and cute.", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=12)
    $ name = name.strip()

    if name == "" and fname == "Samantha":
        $ name = "Sammy"
    elif name == "":
        $ name = fname





label start_hospital_3:
    nurse.name "Ok, [fname] it is."
    pc "Does [emile.name] know what happened to me?"
    nurse.name "She does. With the amount of harassment she has been giving us, it was hard to keep it quiet."
    nurse.name "Now c'mon, up we get! Seems like [emile.name] has dealt with everything so we are kicking you out."
    hide nikolas with dissolve
    $ walk(loc_hospital_lobby, time_amount=0)
    nurse.name "Here we go, she will be with you in a few minutes."
    nurse.name "And take it easy, you haven't done any physical exercise... well... at all really. You will need time to adjust to your new body."
    hide nurse with dissolve
    pcm "New body? They talk about this stuff like it's normal for them."
    pcm "Is it normal for them? \"Hey wake up! Here's your new body. Now off you go.\""
    pcm "Come to think of it, where even am I?"
    jump start_sismeet_1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
