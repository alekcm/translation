label main_quest_02_briefing_passed:

    $ cosmetic_surgery_tutorial = True

    $ walk(loc_hospital_office)
    show tucker smile at right1 with dissolve

    if t.hour in morning:
        tucker.name "Good morning, [name]. I am glad you are here."
    elif t.hour in afternoon:
        tucker.name "Good afternoon, [name]. I am glad you are here."
    else:
        tucker.name "Good to see you, [name]. I am glad you are here."
    pc "Well, you asked me to come."
    tucker.name "I did. [nik.name] is ready for you so let's go and see him now."
    pc "Ok..."
    $ walk(loc_hospital_ward, trans=False)
    show tucker smile at right1
    show nikolas at right3
    with dissolve
    if t.hour in morning:
        tucker.name "Good morning, [nik.name]."
    elif t.hour in afternoon:
        tucker.name "Good afternoon, [nik.name]."
    else:
        tucker.name "Good to see you, [nik.name]."

    if quest_homeless_start.active:
        if nik.has_met:
            nik.name "Ah [tucker.name]. Good to see you too. And Miss [sname], what a wonderful sight."
            pc "Err, Hi again."
        else:
            nik.name "Ah [tucker.name]. Good to see you too. And Miss [sname], my name is [nik.fullname]. I suspect we will be seeing each other often."
            pc "Err, okay. Hi."
        nik.name "But I imagine you are curious as to why you are here. Have you told her anything, [tucker.name]?"
        tucker.name "Not at all. I thought I would let you do the honours."
        nik.name "Ok. Wonderful. Well, where should I start I wonder..."
        nik.name "Without boring you with the details, here at The Institute we were tasked with making artificial bodies."
        pc "Okay, wow. Did they work?"
        nik.name "One did, but not as we had planned. I'm sure [tucker.name] will fill you in there."
        nik.name "The other died in the lab since we didn't have much use for it. We had the body but no mind to go with it."
        pc "Okay..."
        tucker.name "I think we are losing her."
        nik.name "Yes, well. The body had some perks that we can give to you."
        pc "Err, why would I care?"
        nik.name "Because we can change you physical attributes. Skin colour, hair, eyes."
        nik.name "It will feel very much like having a new body from a simple little injection."
        with hpunch
        pc "OW!"
    else:
        nik.name "Ah [tucker.name]. Good to see you too. And Miss [sname], what a wonderful sight. I am so happy to see you up and about."
        if player.fitness >= 20:
            nik.name "And looking after that body I see. It looks a lot more trim than when I saw you leave. Thank you for taking good care of it."
            pc "Ah... Well. No problem?"
        nik.name "But I imagine you are curious as to why you are here. Have you told her anything, [tucker.name]?"
        tucker.name "Not at all. I thought I would let you do the honours."
        nik.name "Ok. Wonderful. Well, where should I start I wonder..."
        nik.name "As you are aware miss [sname], your body is not a natural one but grown by us in a lab."
        pc "Grown?"
        nik.name "Well, to not go deep into the science, yes. Grown is the best way to put it. And as such it has some peculiarities that normal bodies do not have."
        pc "Errr. I'm not going to fall apart and die or something am I."
        nik.name "I would hope not. But that's not the point here. The point is we can make some subtle changes to your body and it will be accepted like it is normal."
        nik.name "For example, skin colour is just a pigment that your body produces. We can change that. The same with hair and eye colour."
    pc "Hmm, you can change how I look basically? Will it wear off?"
    nik.name "That's the best part. Your body will treat it as normal and keep producing the pigment. So for example your hair."
    nik.name "If we were to dye it, when your new hair grows in it will grow in its natural colour."
    nik.name "But with this method, all new hair grown will grow the new colour. The changes will be permanent. Well at least until we change it again if you so wished."
    pc "Ok, but there must be a catch or side effects."
    nik.name "Side effects? None that we know of."
    if player.pregnancy >= 2:
        pc "What about with my baby, will it cause any harm?"
        nik.name "No, it will be perfectly safe."
    nik.name "There are two catches though. One is that it can only be done to you. While we are using this to study how it can be done to the wider population, you will serve as our first basis of study."
    nik.name "Catch two is the expense. If it's mission critical we will cover the cost. But if you are feeling like a change then you will have to cover the cost yourself."
    nik.name "Oh, one last thing I should mention. We can remove things like a suntan or a tattoo, but not add them. To get those you need to do it the natural way."
    pc "Ah ok. Well I suppose it sounds reasonable."
    nik.name "Indeed. But for now we need to give this a trial run, so you are in luck. You can have a one time freebie so we can test the system properly."
    nik.name "First I need you to undress. I need to make sure you can be seen fully to be sure there are no issues."
    if not player.has_perk([perk_exhibitionist, perk_whore, perk_slut, perk_commando]) or player.check_nowill(notif=False):
        pc "Errm..."
        nik.name "I helped create this body. I have seen more of it than you can imagine. Don't worry."
        pcm "Well, still feels a bit uncomfortable."
    pc "Ok..."
    $ pc_strip_tops()
    pause 1
    $ pc_strip()
    nik.name "Let's see here..."
    nik.name "You are probably used to the wardrobe system by now so I am sure you can figure this one out on your own. So lets jump right into testing it shall we?"

    call screen surgery_screen()


label main_quest_02_briefing_passed_post_cosmetic:
    $ pc_strip()
    nik.name "Wonderful, everything seems to have gone fine. You can dress up now."
    $ pc_dress_slow()
    nik.name "For now I believe that is everything. If you want to make any further changes then come back later and we will sort you out."
    tucker.name "Excellent. Thank you [nik.name]. Now [name], you have an appointment with [psy.name]. Let's head over there now."
    nik.name "Goodbye Miss [sname]."
    pc "Goodbye [nik.name]."
    hide nikolas with dissolve
    pc "Hmm, so this [psy.name]? Is she aware of things?"
    tucker.name "Fully. It would be useless to talk to her if she wasn't."
    jump main_quest_02_psychologist
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
