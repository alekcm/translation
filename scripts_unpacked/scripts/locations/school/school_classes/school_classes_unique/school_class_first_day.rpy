label school_class_first_day:
    show bg_school_gym_people_attendance onlayer bg_screen
    $ walk(loc_school_gym)
    headt "Good morning boys and girls... Or should I say ladies and gentlemen?"
    headt "Now as I am sure you are all aware, the classes you are enrolled in are a bit unique and unexpected. But for any of you who are unaware, I will go through a few things that might not be so obvious."
    headt "So, all of your fellow students are people whose lives and education were heavily impacted during the Plague we suffered from. And as such have been given the opportunity to continue your education here."
    headt "This will allow all of you who had to abandon your studies due to the pandemic to continue them here and now in an environment catered towards your situation."
    headt "And because of this, many normal school rules no longer apply or have been modified for your needs. The main one you should be aware of is regards your attendance."
    headt "We are fully aware many of you have priorities that impact your studies. I know many of you here are caring for relatives disabled due to the pandemic. Many others have unexpectedly been thrust into the working world to make ends meet."
    headt "And to that effect, attendance is NOT mandatory. Of course you still have to attend to learn, but there will be no punishment for missing classes without notice. We will try to work around your schedule."
    headt "Classes start at 9am and end at 2pm. But unfortunately because of the way the lessons are structured, you will have to arrive at least before 10 to not upset the lesson plan."
    headt "Additionally, the school will remain open until 8pm for those of you who need a quiet place to study or just want a safe place to relax."
    headt "Your teachers would probably have went home, but all the school facilities will still be available for use. Please do not abuse this trust we have placed in you all by allowing you free reign of the school."
    headt "We have also created some new classes whose aim is to teach you more about the life changes caused by the pandemic. The classes are..."
    headt "\"Modern History\". Its aim is to give you a propaganda free account of what happened these past years in regards to the pandemic and how countries and government institutions were affected."
    headt "\"Modern Economics\". This class discusses the impact the pandemic had for the economy. But its main goal is to better prepare you for the workplace and how to manage your finances."
    headt "And finally for the girls here, \"Modern Women's History\". I will let your teacher explain in depth what that is about."
    headt "The rest I am sure you will find out on your own."
    "With the introduction over, people start heading out of the gym and head to the cafeteria for lunch."
    hide bg_school_gym_people_attendance onlayer bg_screen with dissolve

    $ time_round_to_hour()
    if t.hour == 9:
        $ stroll(180)
    elif t.hour == 10:
        $ stroll(120)
    else:
        $ stroll(60)
    jump travel

label school_class_first_day_missed:
    if t.day > 15:
        headt "Good morning Miss [sname]. It's been a while since the school term started but I will go over the important details for you."
    else:
        headt "Good morning Miss [sname]. Since you missed orientation I will go over the important details for you."
    headt "Since this course is designed specifically for students effected by the Plague, we have adjusted the rules to fit the situation better."
    headt "So first of all, attendance is not mandatory. You will not be punished for missing classes. But of course if you want to pass your exams you will still need to learn the material. A school uniform is still mandatory."
    headt "School starts at 9 and ends at 2. But because of the way we structure our lessons you will have to be here before 10. And a school uniform is still mandatory to attend classes."
    headt "You will also have special modern history classes to better prepare you for the changed world. Modern History, Modern Economics and Modern Women classes. I'll let your teachers give you the details on those."
    headt "After your class you will have lunch at 12, then a physical education class. In the aftermath of the Plague, physical fitness is now of paramount importance."
    headt "And that's about it, I look forward to your success."
    pc "Thank you."
    pcm "Ok, that seems reasonable."
    pcm "Lessons, modern history and physical education. Just what the doctor ordered."

    $ time_round_to_hour()
    if t.hour == 9:
        $ stroll(180)
    elif t.hour == 10:
        $ stroll(120)
    else:
        $ stroll(60)
    jump travel


label school_class_gym_first_day:



    $ walk(loc_school_gym)
    show mason at right1 with dissolve
    mason.name "Okay ladies gather round. I don't want to take up much of your time, so I will be brief."
    mason.name "I am Mr Mason and I am the personal trainer for your physical education classes."
    mason.name "On Mondays you will have track and Wednesdays you will have volleyball."
    mason.name "Tuesday, Thursday and Friday you will be with the clubs you chose when applying for the school. Any question, come and see me. That is all."
    pc "Err, Mr Mason, I didn't pick a club."
    mason.name "[sname] is it? I have you down here as attending the dance classes. Your club leader is [svet.fullname] if I am not mistaken."
    pc "Ok, thank you."
    hide mason with dissolve
    pcm "Dance class. [tucker.name] put me down for dance? Hmmm..."
    pcm "Although thinking about it, I suppose it's not a bad idea. Dance will no doubt help me with my coordination."
    pcm "Suppose I will give it a proper go and try and get the most out of it."
    $ stroll(60)
    pcm "But that's my first day over with. Time to leave."
    $ school_day += 1
    jump travel

label school_class_gym_first_day_missed:
    $ walk(loc_school_gym)
    show mason at right1 with dissolve
    mason.name "[fname] [sname] is it? I am Mr Mason your physical education teacher. You missed the first day orientation so I will go over the main points."
    mason.name "Tuesday and Thursday is your club days. I see you have dance chosen for your club. That will be with [svet.fullname]."
    mason.name "Monday is track, Wednesday is volleyball and Friday is swimming. Everything else you will pick up during the lessons. Now if that's all I will be getting back to the lesson."
    pc "Yes, that's all."
    hide mason with dissolve
    pcm "Dance class. [tucker.name] put me down for dance? Hmmm..."
    pcm "Although thinking about it, I suppose it's not a bad idea. Dance will no doubt help me with my coordination."
    pcm "Suppose I will give it a proper go and try and get the most out of it."
    $ stroll(60)
    pcm "But that's my first day over with. Time to leave."
    $ school_day += 1
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
