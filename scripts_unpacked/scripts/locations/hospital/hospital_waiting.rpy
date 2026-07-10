label hospital_waiting_reception:
    if player.drunk > 30:
        pcm "I should probably come back when I am a bit more sober."
        jump travel
    elif player.cum_visible:
        pcm "I shouldn't let [tucker.sname] see me with cum all over me. I should shower before heading in."
        jump travel
    elif player.blind:
        pcm "I'm not going to go marching in there when I can't see a thing."
        jump travel
    elif player.gagged:
        pcm "How am I going to speak to anyone when I can't even speak?"
        jump travel
    show receptionist at right1 with dissolve
    if t.hour in morning:
        receptionist.name "Good morning. How can I help you?"
    elif t.hour in afternoon:
        receptionist.name "Good afternoon. How can I help you?"
    else:
        receptionist.name "Good day. How can I help you?"
    menu:
        "I am here to see [emile.fullname]" if log.interactive("quest_homeless_start_04"):
            if not t.hour in workhours:
                receptionist.name "I'm sorry, she isn't here right now. She will be back during the day."
                pc "Okay, thanks."
                hide receptionist with dissolve
                jump travel
            receptionist.name "She told me you would be coming. Head right in, second door on the right."
            pc "Thanks."
            hide receptionist with dissolve
            pcm "Hmmm, second door..."
            jump start_homeless_meet_sister_institute

        "I am here to see [tucker.name]" if main_quest_01.active:
            if not "seen_tucker" in receptionist.list:
                $ add_to_list(receptionist.list, "seen_tucker")
                receptionist.name "[tuc.name]? Can I ask why you want to see him?"
                pc "Err... He asked me to."
                receptionist.name "Do you have an appointment?"
                pc "No. He just said to come by."
                receptionist.name "Right... Sure..."
                receptionist.name "What's your name?"
                pc "[fname]. [fname] [sname]."
                receptionist.name "Right. One moment."
                hide receptionist with dissolve
                pcm "Hmm, not very friendly it seems..."
                pcm "Although she was until I mentioned [tucker.sname]."
                pcm "Whatever..."
                show receptionist at right1 with dissolve
                receptionist.name "Err... He said for you to head right in."
                pc "Okay... Where do I go?"
                receptionist.name "Just through there on the right."
                pc "Okay."
                hide receptionist with dissolve
                jump tucker_picker
            elif t.hour in workhours:
                receptionist.name "Miss [sname]? Head right in."
                if not "seen_pregnant" in receptionist.list and receptionist.showing:
                    $ add_to_list(receptionist.list, "seen_pregnant")
                    pc "Err... Congratulations?"
                    receptionist.name "Ugh. Thanks..."
                    pc "Condolences?"
                    receptionist.name "Yeah..."
                    pc "..."
                hide receptionist with dissolve
                jump tucker_picker
            elif t.hour in (19,20,21):
                receptionist.name "I'm afraid [tucker.name] has left for the day. He will be back tomorrow."
            elif t.hour in (22,23,0,1,2):
                receptionist.name "[tucker.name] finishes work at 18:00 so has already gone home. He will be back tomorrow."
            else:
                receptionist.name "[tucker.name] will be here at 08:00 so you will have to come back later to see him."
            hide receptionist with dissolve
            jump travel

        "I am here to see [nik.name]." if main_quest_02.active == 2:
            if t.hour in workhours:
                receptionist.name "Miss [sname]? Head right in."
                hide receptionist with dissolve
                jump doc_surgery
            elif t.hour in (19,20,21):
                receptionist.name "I'm afraid [nik.name] has left for the day. He will be back tomorrow."
            elif t.hour in (22,23,0,1,2):
                receptionist.name "[nik.name] finishes work at 18:00 so has already gone home. He will be back tomorrow."
            else:
                receptionist.name "[nik.name] will be here at 08:00 so you will have to come back later to see him."
            hide receptionist with dissolve
            jump travel
        "Sorry, nothing.":
            hide receptionist with dissolve
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
