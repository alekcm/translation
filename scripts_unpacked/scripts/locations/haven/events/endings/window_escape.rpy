label haven_window_escape:
    $ add_to_list(main_quest_05.list, "jumped_window")
    pc "Ungh!!"
    pcm "Jump jump jump!"
    havguard "Grab her!"
    show screen blackout(100)
    $ renpy.scene()
    with hpunch
    $ walk(loc_haven_exterior)
    $ bruise.all(4)
    $ bruise.ass = 1
    $ blood.face = 5
    $ blood.special = "haven"
    $ bruise.special = "haven"
    $ player.add_drunk(-100)
    $ player.add_desire(-100)
    $ player.add_perk(perk_recovering, days=5)
    with vpunch
    $ player.face_normal()
    $ player.face_pain()
    show screen blackout(50) with Dissolve(2)
    pc "Uggggg."
    show screen blackout(75) with dissolve
    show screen blackout(50) with dissolve
    havmuff "She jumped!"
    pc "Ahhhhh..."
    show screen blackout(75) with dissolve
    show screen blackout(50) with dissolve
    havmuff "...down there and get her!"
    pc "Fuuuuuccccccck..."
    show screen blackout(75) with Dissolve(1)
    $ player.eye = 3
    pc "Uhhh..."
    show haven_guard3 at right1 with dissolve
    havmuff "Still here."
    havmuff "What do we do?"
    show haven_guard2 at right2 with dissolve
    havmuff "..."
    havmuff "No fucking idea!"
    havmuff "Just drag her inside and let..."
    show police_gen mask at right4:
        xzoom -1
    show police_gen2 mask at right5:
        xzoom -1
    with hpunch
    havmuff "The fuck are you lot doing? Get away from her!"
    havmuff "The fuck are you doing here? This ain't your business so fuck off!"
    havmuff "We are making it our business. Get out of here and let us deal with it."
    havmuff "No fucking way! This ain't got anything to do with..."
    show screen blackout(100) with dissolve
    pause 1
    $ walk(loc_hospital_ward)
    $ renpy.scene()
    $ pc_strip()
    $ work.outfit_primary_colour = "sky"
    $ c.outfit = 1
    $ blood.special = 0
    $ bruise.special = 0
    $ t.day = 5
    $ bruise.all(4)
    $ bruise.ass = 1
    $ acc.makeup_on = False
    $ player.face_worried()
    $ player.eye = 3
    show screen blackout(75) with Dissolve(1)
    pc "Uggggghhhhh..."
    $ player.eye = 2
    pc "Where am I?"
    emile.name "She's coming round!"
    show screen blackout(50)
    show emile suitshirt worried at right3
    show nurse at right1
    with dissolve
    emile.name "You are awake? Don't move!"
    pc "[emile.name]?"
    pc "What's going on?"
    emile.name "You were injured. Took a bit of a fall."
    show screen blackout(25) with dissolve
    pc "Ugh, that would explain... Ouch! Would explain the pain..."
    pc "What happened?"
    emile.name "No idea. Was hoping you could tell us."
    emile.name "Security keeping an eye on [haven] heard a huge commotion and noticed you on the floor covered in blood."
    pc "Ah..."
    hide screen blackout with dissolve
    pc "..."
    pc "It was too dangerous to stay in there anymore and had to get out."
    emile.name "What? You jumped?"
    pc "Ugh!"
    pc "It was that or something worse..."
    emile.name "Oh..."
    emile.name "Ok..."
    show emile neutral
    pc "Ugh, here now so looks like it was the right choice..."
    $ haven_complete_questlog()
    pc "How badly did I hurt myself?"
    nurse.name "Looked a lot worse than it was. You came in here more blood than person but once it was all cleaned up there weren't too many serious injuries."
    $ player.face_worried()
    pc "Too many?"
    nurse.name "Your legs took a beating from what I guess was the landing but the bones were easy to set. The big worry was head injuries. But fortunately it was mostly lacerations and no serious head or brain injury."
    pc "Wait hold on. Set the bones? My leg is broken?"
    nurse.name "Both of them were broken in multiple places along with some bone bruising of your hips and ribs."
    nurse.name "You also got a spiral fracture on your wrist and a dislocated shoulder from what we guess was you trying to break your fall with your arms."
    nurse.name "We have had you sedated for a few days while you underwent surgery to set the bones correctly and monitor any swelling or fluid in your skull."
    pc "Am I going to be able to walk again?"
    nurse.name "Yes. You were brought here right away by security and you were taken care of right away. Most of the breaks were clean so they will heal nicely. No nerve damage or anything else that might cause long term complications."
    nurse.name "Basically, you will make a full recovery."
    emile.name "The boffins in the lab also got their knickers in a twist about it as well. Research data on how the body deals with heavy injuries is valuable apparently so pretty much half the hospital was up and about tending to you."
    pc "Oh?"
    emile.name "Nothin' to worry about. Turns out that while you aren't more resistant to injury than the rest of us, you heal faster than normal."
    $ player.brow = 1
    pc "Really?"
    emile.name "Don't be thinking anything weird. You are not a superhero who can shrug off bullets. You have an extremely alert system that is always prepared for injury so deals with wounds a lot faster than anyone else."
    emile.name "Not sure what it means entirely but the guys in the lab seemed to be very happy about it."
    nurse.name "It means you will be able to walk out of here when we let you go. That's all that matters for now."
    pc "When will the pain go away?"
    nurse.name "Soon. You still have a lot of micro fractures all over your body. They will heal naturally in time."
    nurse.name "For now you just need bed rest. So I will give you a mild sedative and you should get some sleep."
    pc "Ugh, if you say so..."
    emile.name "I'm happy to see you well [name]."
    pc "Mmmm..."
    hide emile with dissolve
    nurse.name "Here we go. Rest."
    pc "Yeah..."
    $ player.eye = 3


    show screen blackout(100) with dissolve
    $ t.day = 5
    $ bruise.face = 0
    $ bruise.chest = 0
    $ bruise.belly = 0
    hide nurse
    $ time_sleep(300)
    show emile suitvest at right1
    pause 0.5
    $ player.add_mood(30)
    $ player.shower()
    $ player.face_sleep()
    show screen blackout(50) with dissolve
    emile.name "...sleep but you should get up."
    emile.name "Wake up!"
    $ player.face_annoyed()

    pc "[emile.name]?"
    emile.name "Yup, come on. Wake up."
    hide screen blackout with dissolve
    $ player.face_normal()
    pc "Ugh. What's going on?"
    emile.name "[nik.name] is preparing to get rid of your tattoos and go over your bloodwork so get your ass up."
    pc "They not already done all that?"
    emile.name "No, the focus was on getting your injuries dealt with so [nik.name] hasn't had much chance to look you over."
    pc "It wasn't [nik.name] dealing with my injuries?"
    emile.name "No, they had trauma surgeons dealing with that. Now that you are doing a lot better, you are back in the hands of [nik.name]."
    emile.name "[tucker.name] has also insisted you speak to [psy.name] after you get checked out."
    pc "Ok. I just want to get back to normal."
    emile.name "Well won't be long."
    nik.name "Ok, we are mostly ready. [emile.name], if you would give us some privacy."
    emile.name "Sure. See you in a bit [name]."
    pc "Yeah."
    hide emile with dissolve
    show nikolas at right3
    show nurse at right1
    with dissolve
    nik.name "Okay Miss [sname]. Let's see what we are dealing with here."
    nik.name "First, need to get you cleaned up and remove those tattoos. In the meantime we will give you a quick check up and make sure everything is ok."
    pc "Still got 2 legs so that's a good thing."
    nik.name "I am more concerned with anything that might have happened before you left the building through the window."
    if main_quest_05.rape > 0:
        pc "Oh..."
    else:
        pc "Should be fine. I didn't really have much issue in there."
    nurse.name "Well, let's get you cleaned up and see."
    pc "Sure."
    show screen blackout(100) with dissolve
    $ t.hour = 2
    $ player.shower()
    $ acc.makeup_on = False
    $ tattoo.chest = 0
    $ tattoo.ass = 0
    $ pc_strip()
    $ acc_strip()
    $ player.eye_liner = 1
    $ c.outfit = 1
    hide nikolas
    hide nurse
    pause 0.5
    jump haven_ending_wrapup_beaten_catcher
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
