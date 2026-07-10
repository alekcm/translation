define surgery_extraservices_asked = False
define surgery_serious = 0

label doc_surgery:
    $ walk(loc_hospital_ward)
    show nikolas at right1 with dissolve
    nik.name "Miss [sname]. Here for some cosmetic changes? Remember, it will cost you."
    jump surgery_menu

label surgery_menu_cont:
    if not t.hour in workhours:
        nik.name "Have a good night [fname]. Anything else you need can wait until tomorrow."
        pc "Ok, goodnight [nik.name]."
        jump surgery_leave
    elif surgery_serious == t.day:
        nik.name "Get some rest miss [sname]. If you need anything else I can see you tomorrow."
        pc "Ok, thanks [nik.name]."
        jump surgery_leave
    else:
        nik.name "Was there anything else you needed?"
        jump surgery_menu

label surgery_leave:
    hide nikolas
    hide nurse
    $ walk(loc_hospital_lobby)
    with dissolve
    jump travel

label surgery_menu:
    menu:
        "Yes (£ 300)"(enabled=player.cash >= 300):
            $ player.remove_money(300)
            nik.name "Ok, undress please."
            $ pc_strip()
            nik.name "Great, what changes do you want?"
            call screen surgery_screen()
            jump surgery_menu_cont
        "Ask about extra services":

            if surgery_extraservices_asked:
                jump surgery_extra_menu
            else:
                jump doc_surgery_extra_services
        "Not right now.":

            nik.name "Ok, well come see me when you have need of my services."
            jump surgery_leave

label surgery_extra_menu:
    nik.name "What else did you have in mind?"
    menu:
        "Remove tattoos (£ 250)"(enabled=player.cash >= 250):
            $ player.remove_money(250)
            jump doc_surgery_extra_services_tattoo
        "Repair hymen (£ 1200)"(enabled=not player.vvirgin and player.cash >= 1200):

            $ player.remove_money(1200)
            jump doc_surgery_extra_services_virgin
        "Heal cuts and bruises (£ 100)"(enabled=player.cash >= 100):

            $ player.remove_money(100)
            jump doc_surgery_extra_services_heal
        "Change name (£ 100)"(enabled=player.cash >= 100):

            $ player.remove_money(100)
            jump doc_surgery_extra_services_name
        "Nothing right now":

            jump surgery_menu_cont

label surgery_close:
    jump surgery_menu_cont
    nik.name "Wonderful, I look forward to seeing you again."
    hide nikolas
    $ walk(loc_hospital_lobby)
    with dissolve
    jump travel

label surgery_serious_reject:
    nik.name "Sorry miss [sname]. You need time to recover from your last operation before I am willing to perform that."
    nik.name "Go home and get some rest."
    pc "Right..."

label doc_surgery_extra_services_bc:
    nik.name "Okay. I'll get it prepared for you."
    hide nikolas with dissolve
    pc "Okay."
    show nikolas with dissolve
    nik.name "Ok, give me your arm."
    with hpunch
    nik.name "There we go."
    nik.name "Remember, this will only last until you get your next period. You can come and see me again for another shot."
    pc "Ok."
    $ relax(10)
    jump surgery_menu_cont

label doc_surgery_extra_services_virgin:
    nik.name "Ok, I'll go and prepare while you change into a gown."
    nik.name "How far do you want us to go with this?"
    menu:
        "Just my hymen":
            $ player.surgery_vvirgin()
        "Just my anus":
            $ player.surgery_avirgin()
        "Hymen and anus":
            $ player.surgery_vvirgin()
            $ player.surgery_avirgin()
        "Everything":
            $ player.surgery_all_sex_stats()
    nik.name "Ok, I'll be right back."
    hide nikolas with dissolve
    call doc_surgery_extra_services_surgery_start from _call_doc_surgery_extra_services_surgery_start
    call doc_surgery_extra_services_surgery_wake from _call_doc_surgery_extra_services_surgery_wake
    jump surgery_leave

label doc_surgery_extra_services_tattoo:
    nik.name "Ok, I'll go and prepare while you change into a gown."
    pc "Okay."
    hide nikolas with dissolve
    call doc_surgery_extra_services_surgery_start from _call_doc_surgery_extra_services_surgery_start_3
    $ writing.clean_writing(tattoo=True)
    $ tattoo.chest = 0
    $ tattoo.ass = 0
    call doc_surgery_extra_services_surgery_wake from _call_doc_surgery_extra_services_surgery_wake_3
    jump surgery_leave

label doc_surgery_extra_services_heal:

    nik.name "Ok, I'll go and prepare while you change into a gown."
    hide nikolas with dissolve
    call doc_surgery_extra_services_surgery_start from _call_doc_surgery_extra_services_surgery_start_1
    $ blood.heal_all()
    $ bruise.heal_all()
    call doc_surgery_extra_services_surgery_wake from _call_doc_surgery_extra_services_surgery_wake_1
    jump surgery_leave

label doc_surgery_extra_services_abortion:
    nik.name "Ok, I'll go and prepare while you change into a gown."
    hide nikolas with dissolve
    call doc_surgery_extra_services_surgery_start from _call_doc_surgery_extra_services_surgery_start_2
    $ player.preg_abortion()
    call doc_surgery_extra_services_surgery_wake from _call_doc_surgery_extra_services_surgery_wake_2
    jump surgery_leave

label doc_surgery_extra_services_pregtest:
    nik.name "Right then. Let's get a little blood sample..."
    $ player.face_worried()
    with hpunch
    pc "Ouch!"
    nik.name "I'll run the test. Wait here for a few minutes."
    pc "Ok."
    hide nikolas with dissolve
    if player.has_perk(perk_preg_want):
        pcm "Please be pregnant please be pregnant please be pregnant..."
    elif player.has_perk(perk_preg_notwant):
        pcm "Don't be pregnant don't be pregnant don't be pregnant..."
    else:
        pcm "Hmmm..."
    show nikolas at right1 with dissolve
    if player.pregnant:
        $ player.preg_knows = True
        nik.name "Congratulations. It came back positive."
        if player.has_perk(perk_preg_want):
            pcm "YES!"
        elif player.has_perk(perk_preg_notwant):
            pcm "FUCK!"
    else:

        nik.name "Negative result. You are not pregnant."
        if player.has_perk(perk_preg_notwant):
            pcm "YES!"
        elif player.has_perk(perk_preg_want):
            pcm "FUCK!"
    pc "Ok, thanks [nik.name]..."
    jump surgery_menu_cont

label doc_surgery_extra_services_name:
    nik.name "Ok, let's see here..."
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

    if quest_whore.isactive():
        $ wname = renpy.input("What about your highway name?", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=12)
        $ wname = wname.strip()
        if wname == "":
            $ wname = "Doxie"

    if quest_whore.isactive():
        nik.name "Ok. So that's [fname] \"[name]\" [sname]? Or [wname] depending on what you are doing."
    else:
        nik.name "Ok. So that's [fname] \"[name]\" [sname]?"
    menu:
        "That's right":
            nik.name "Okay then, I'll get the paperwork submitted."
            $ relax(10)
            jump surgery_menu_cont
        "No, Let me pick again":
            jump doc_surgery_extra_services_name

label doc_surgery_extra_services_surgery_start:
    $ pc_striptease()
    pause 0.5
    $ c.outfit = 1
    pause 0.5
    show nikolas at right2
    show nurse at right1
    with dissolve
    nik.name "Ok, for this we are going to have to put you under."
    pc "Okay."
    nik.name "Close your eyes and count to ten."
    $ player.face_sleep()
    pc "One... Two... Three.............."
    show screen blackout() with dissolve
    pause 1
    $ relax(120)

    hide nikolas
    $ surgery_serious = t.day
    return

label doc_surgery_extra_services_surgery_wake:
    hide screen blackout with Dissolve(1)
    pc "Uggghhh,"
    nurse.name "Take it slow..."
    nurse.name "Everything went well. So once you are ready, you are free to leave."
    pc "Great. I feel like shit."
    nurse.name "That will pass. Go home and get some sleep. You should feel better after some good rest."
    pc "Okay..."
    nurse.name "I'll leave you to get dressed."
    hide nurse with dissolve
    pc "Ugh!"
    $ pc_strip()
    pause 0.5
    $ pc_dress_slow()
    pcm "Right then, time to sleep off this killer hangover..."
    return

label doc_surgery_extra_services:
    $ surgery_extraservices_asked = True
    nik.name "Well, there are some services we are willing to provide."
    pc "Err, anything strange?"
    nik.name "Nothing of the sort. Just things that are a bit more unique to your body such as remove tattoos or advance your healing."
    nik.name "And since some missions might call for it, we can repair your hymen so you can pass as a virgin again."
    nik.name "And while it's not really anything to do with your body, I can also submit the paperwork to have your name changed."
    pc "Oh, that's good to know."
    nik.name "We are at your service."
    nik.name "For a fee of course."
    pc "Right."
    jump surgery_menu_cont
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
