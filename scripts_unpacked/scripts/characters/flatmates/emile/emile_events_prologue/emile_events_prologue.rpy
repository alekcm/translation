init python:
    def emile_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not emile.isactive:
            cur_location = None
        
        elif t.day < 6 and t.hour in irange(7,18):
            cur_location = loc_kitchen
        elif t.day < 6:
            cur_location = loc_common
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

label emile_tutorial_info:
    if t.hour in irange(0,6):
        pcm "She is asleep. I shouldn't disturb her."
        jump travel
    show emile at right1 with dissolve
    if not "prologue_event_date" in emile.dict:
        $ emile.dict["prologue_event_date"] = 0
    if not "prologue_event" in emile.dict:
        $ emile.dict["prologue_event"] = 1
    if not "tutorial_info" in emile.dict:
        $ emile.dict["tutorial_info"] = 0

    if renpy.has_label("emile_prologue_event_" + str(emile.dict["prologue_event"])) and not emile.dict["prologue_event_date"] == t.day:
        $ emile.dict["prologue_event_date"] = t.day
        jump expression "emile_prologue_event_" + str(emile.dict["prologue_event"])

    if renpy.has_label("emile_tutorial_info_" + str(emile.dict["tutorial_info"])):
        jump expression "emile_tutorial_info_" + str(emile.dict["tutorial_info"])
    else:

        jump expression renpy.random.choice([
        "emile_tutorial_info_0",
        "emile_tutorial_info_1",
        "emile_tutorial_info_2",
        "emile_tutorial_info_3",
        "emile_tutorial_info_4",
        "emile_tutorial_info_5",
        "emile_tutorial_info_6"
        ])

label emile_tutorial_info_0:
    emile.name "Hey [name]. Ready to start your school life?"
    pc "Err, I'm not sure. In fact when does it start?"
    if t.wkday in weekend:
        emile.name "It's never stopped. You can probably go there now but since it's the weekend it will be empty."
    else:
        emile.name "It never stopped so is open now. Can go there and start your classes whenever you want."
    pc "Sounds wonderful..."
    emile.name "I don't envy you. While it would be nice to be young again, I'm not sure I would look forward to going back to school. Do you even remember much from your lessons before?"
    pc "Not really. Kinda forgot all that as soon as I left school. Didn't really learn much of the topics, just memorised what to write for the exam."
    emile.name "Ha, sounds about right."
    emile.name "Well, [tucker.name] has already arranged a uniform for you, you can find it in your wardrobe."
    pc "Damn, I have to wear a uniform again?"
    emile.name "Haha, 'fraid so [name]. On the bright side the girls don't wear ties like the boys."
    pc "Yeah, but they have skirts..."
    jump emile_tutorial_info_end

label emile_tutorial_info_1:
    emile.name "By the way, the landlord lives in the same building, if you have any issues you should pay him a visit. The next weeks rent is paid up but from then you should start paying him yourself."
    pc "Damn, I hadn't considered I need to pay rent. Is it expensive?"
    emile.name "Not so much, all of the people that live here are those who suffered from the virus. Mostly young people who's parents died. So the landlord gets a subsidy to keep the rent low."
    pc "Low, but not free?"
    emile.name "If only we were so lucky."
    pc "So why aren't you still living here?"
    emile.name "I didn't expect you would want to share a room with your sister. There wouldn't have been any other options as space here is hard to come by."
    pc "And I dread to ask, but what happens if I can't pay?"
    emile.name "Then [oskar.name] will put you to work cleaning the building or working in the cafe he runs down the street."
    pc "So, that's good? Isn't it?"
    emile.name "Well yes and no. Good because it means you aren't kicked out on your arse. Bad in the way that he will no doubt work you like a donkey. You are better off trying to pay with cash money."
    pc "Ok, I'll keep that in mind."
    jump emile_tutorial_info_end

label emile_tutorial_info_2:
    emile.name "You should probably look out for any work you can find out there. It's not very easy to earn a living these days."
    pc "Well, not that it was easy before. But what changed? Is it really that much worse now?"
    emile.name "Yeah, sorry to say but it's pretty terrible out there now."
    emile.name "A lot of people died to the Plague so of course that's less customers spending money. Entire industries collapsed almost overnight."
    emile.name "So you have a lot of desperate people out there looking for work and being taken advantage of by employers. As you can imagine, wages are in the toilet."
    pc "So jobs are hard to come by? Are there alternative ways to earn some money?"
    emile.name "Well The Institute did offer you something so I would look into that and speak to [tucker.name] once you are settled in."
    emile.name "I suppose you could also go door to door and see if people need odd jobs done."
    emile.name "But be careful if you are considering something shady. The police aren't what they used to be so vigilante justice is what most people will resort to."
    pc "Errr... Ok, I'll keep that in mind."
    jump emile_tutorial_info_end

label emile_tutorial_info_3:
    emile.name "If you are looking to lose some of that pudge you have, you might want to go for a run in the park."
    pc "Didn't [tucker.name] mention something about exercising in school?"
    emile.name "He did, but there are other places to do that as well. Might be best to get on top of this now while you can. When you are going to school and looking for work I doubt you'll have time."
    pc "Hmmm you might be right. Are there any gyms nearby?"
    emile.name "I haven't seen a gym anywhere. Gyms were the first to get locked down when the Plague kicked off and they never really recovered."
    emile.name "Plus, who wants to be spending money on that kinda stuff these days when a jog in the park will do the job. Not like we are able to get big and fat like before anyway."
    pc "We can't?"
    emile.name "Course not! While food isn't scarce, you don't have all the junk food places on every corner like before. Most of the food we eat now is from local farmers cooked in the shop."
    pc "I'm sure I saw a bunch of food stand type things out there."
    emile.name "Yeah, since all the fast food chains have gone, you have a lot of ordinary folk selling food from those wheelie things."
    pc "Wheelie things? You talking about the carts with grills on them?"
    emile.name "Yeah, no idea what they are called. Some have grills and some have fridges in them. Local people wheel them around trying to sell food and earn a living."
    emile.name "But they are a far cry from back when you could make a phone call and have all manner of food delivered. The carts are good for getting food when you are out but not really a good idea to eat from there all the time."
    pc "Well... Okay then."
    jump emile_tutorial_info_end

label emile_tutorial_info_4:
    emile.name "You should already know, but be careful with what you wear out there. If you dress in a certain way then people might get the wrong idea."
    pc "What are you talking about?"
    emile.name "Hmmm. If you end up dressing too slutty then people might mistake you for a strumpet or a gamine."
    pc "A what and a what?"
    emile.name "A strumpet, a whore. It's what people round here call them."
    emile.name "And a gamine... Well they are young women who have no family, job, education or anything really and have to rely on day work."
    pc "Sounds like me..."
    emile.name "Well... Yeah. Lotta people now have to rely on day work to make ends meet. But a bunch of the girls are asked to use their body since they are easy prey for shady men."
    pc "So I might end up getting asked weird stuff if I wear revealing clothes? Hmmm. Good to know."
    jump emile_tutorial_info_end

label emile_tutorial_info_5:
    pc "I was wondering, do you think school is going to be the same as when we went there?"
    show emile happy
    emile.name "Getting worried are you?"
    show emile neutral
    emile.name "I spoke to [tucker.name] about that and no, things are entirely different. It's not so much a school but a kind of reform program."
    pc "Reform program? Don't prisoners and such have to do those?"
    emile.name "Yeah, they need help adjusting to life outside of prison. And most of the students in school need help adjusting to how the world is today."
    emile.name "Most of the people you'll be in school with would've lead pampered lives or been preparing to head off to uni. Then suddenly the world goes and breaks."
    emile.name "So they have no ability to function in today's society. What good is your advanced knowledge of Greco Roman architecture in today's world? So many lived somewhat comfortable lives but now we are all face deep in the shit together."
    pc "Hmm I see. And I suppose that most people who were face deep in the mud before the world went upside down are doing a lot better for themselves now?"
    emile.name "\"In the land of the blind, the one eyed man is king\""
    pc "Hrmf."
    jump emile_tutorial_info_end

label emile_tutorial_info_6:
    emile.name "It's best if you don't stay out too late at night if you want to keep safe."
    pc "How late is too late?"
    emile.name "You should make sure to be home before midnight, probably a bit earlier since a lot of drunks will be leaving the pubs about that time so it's when most trouble happens."
    pc "Ah, streets full of drunks. But doesn't that mostly happen on the weekends?"
    emile.name "Weekends are worse but normal days can still be bad. People now just switch between work, booze n sleep so the pubs are packed all the time."
    pc "Hmmm, nothing worth living for except trying to find life and the bottom of a glass?"
    emile.name "Pretty much."
    pc "Ugh... Ok, home before midnight. Got it."
    jump emile_tutorial_info_end

label emile_tutorial_info_end:
    $ emile.dict["tutorial_info"] += 1
    $ relax(20, emile)
    $ dialouge = renpy.random.choice([
    "I hang out talking and joking about random stuff.",
    "I hang out for a while chatting and joking around about random topics.",
    "We hang out chatting and laughing about whatever comes up.",
    "We chat and have a bit of a laugh about random stuff."
    ])
    "[dialouge]"
    hide emile with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
