label main_quest_04_policestation:
    $ walk(loc_checkpoint_lobby)
    show police_gen mask at right
    show police_gen2 handfront wrap at right2
    with dissolve

    if player.cum_visible:
        $ player.face_worried()
        police1.name "Fuck off you dirty whore! Go on, get your dirty arse outta here."
        hide police_gen
        hide police_gen2
        with dissolve
        $ walk(loc_checkpoint)
        pcm "Ugh, should probably clean myself up first."
        jump travel
    elif player.drunk >= 40:
        police1.name "This ain't a pub you drunk bitch, fuck off out of 'ere."
        pc "I am here to..."
        police1.name "I said fuck off!"
        $ player.face_worried()
        police2.name "Should we take her round back?"
        police1.name "Tsk."
        police1.name "Piss off or I will let him take you round back and you won't walk right for a week."
        $ walk(loc_checkpoint)
        pcm "Ugh, I should come back when I have sobered up."
        hide police_gen
        hide police_gen2
        with dissolve
        jump travel
    $ log.markdone("mq_04_a")
    if player.pregnancy >= 2:
        police1.name "Go away girl. The father of your bastard isn't here."
        pc "I am here to..."
        police1.name "Yeah yeah, go spill your story somewhere else. No one here is looking for a girl who has already been knocked up."
        $ player.face_angry()
        pcm "Who are these idiots?"
        police1.name "What are you still here for. I told you to get going."
        police2.name "Yeah little girl, get going. Unless you are looking for someone else to fill yer holes."
        police1.name "Mmm yeah not a bad idea. You can come round the back and we can take turns on you. I'm sure the baby won't mind."
        police2.name "Won't mind at all if you fuck her in the arse."
        police1.name "Ah yeah..."
    elif "school" in tab_top:
        police1.name "Go away girl, school is on the other side of the town."
        pc "I am here to..."
        police1.name "We are fresh out of pink teddies. Now go home."
        $ player.face_angry()
        pcm "Who are these idiots?"
        police2.name "Don't forget to drink yer milk and eat your veggies. Then you can grow up to be big and strong."
        police1.name "Ehehe. Tell your Ma she can come and pay us a visit though. Looks like you come from good stock."
        police2.name "Ahaha. Then you will get a new baby brother or sister."
        police1.name "We will treat her rea..."
    elif player.has_perk([perk_slutty, perk_pervert], notif=True):
        police1.name "Go away girl. No one is looking for company here."
        pc "I am here to..."
        police1.name "Don't care. I'm sure you know where the highway is. That's where you will find people wanting their cocks sucked."
        $ player.face_angry()
        pcm "Who are these idiots?"
        police2.name "Want me to show you where it is?"
        police1.name "What? You interested?"
        police2.name "Sure, she's cute. Show her where the highway is and fuck her on the way. It's a good price."
        police1.name "Hmmm true. Hey, how about you take us both? Then he'll show you where you can sell yourself."
        police2.name "One at a time though. I don't wanna end up crossing sw..."
    else:
        police1.name "On your way girl. Nothing for you here."
        pc "I am here to..."
        police1.name "Don't care. Be about your business somewhere else."
        $ player.face_angry()
        pcm "Who are these idiots?"
        police1.name "Still standing there? Go on, get! Or I'll take you inside for a spanking."
        if c.skirt:
            police2.name "That'd be nice. Get to see what colour your pants are under that skirt."
        elif c.ass:
            police2.name "Nice arse as well. Wouldn't complain to some alone time with it."

    show betty angry at left3 with dissolve

    $ player.face_neutral()
    betty.name "The hell you knuckle draggers up to?"
    police1.name "Just shooing away the riff raff, mam."
    betty.name "Then what are you still doing here? Piss off."
    police1.name "Mam?"
    show betty neutral at right4 with dissolve
    betty.name "[fname] [sname] I presume?"
    pc "That's right."
    betty.name "Chief's been waiting for you. I'll take you to him."
    pc "Ok."
    police2.name "The Chief...?"

    hide police_gen
    hide police_gen2
    with dissolve
    "She waves her hand dismissively at the guards and leads you past the reception desk."
    betty.name "Scum like that need to be treated like the rabid dogs they are."
    pc "Nice welcoming committee for a police station."
    betty.name "Don't be fooled by the name. The people that work here are the same type of people who cause all the trouble out there."
    betty.name "Only difference is, these dogs have a collar round their neck."
    pc "Nice, filth looking over the filth."
    betty.name "Anyway, I am [betty.fullname]. [tucker.name] told us to expect you. The Chief's in his office, I'll take you there."
    pc "Sounds good."
    if "school" in tab_top:
        betty.name "[tucker.name] didn't tell us much about you, but I certainty didn't expect you to show up in a school uniform."
        pc "..."
        pcm "Yeah, probably should have changed before I came here."
    elif player.has_perk([perk_slutty, perk_pervert], notif=True):
        betty.name "[tucker.name] didn't tell us much about you, but I certainly didn't expect you to show up dressed as you are."
        pc "..."
        pcm "Yeah, probably should have changed before I came here."
    else:
        betty.name "[tucker.name] didn't tell us much about you, but you are certainty not what I was expecting."
        pc "..."
        pc "That's kind of the point."

    betty.name "Well, here we are. Wait here and I'll tell him you have arrived."
    pc "Ok."
    hide betty with dissolve
    "She knocks on the door and without waiting for a response she opens it and walks in and closes the door behind her."
    pcm "[betty.name]? One rank up and she talked to those door idiots like they were less than scum. Although the fools did deserve it."
    pcm "I wonder if she has more influence here than her rank suggests."
    pcm "..."
    pcm "Shouldn't take this long to tell him I arrived..."
    pcm "..."
    show betty at right1 with dissolve
    "The door opens and [betty.name] comes out."
    betty.name "It was nice meeting you Miss [sname]. You can head on in now."
    pc "Thanks."
    hide betty
    show chief at right1
    $ walk(loc_checkpoint_office)
    miller.name "Miss [sname]. Please, come in. I would offer you a seat but as you can see, we are pretty short on space around here."
    pc "I can see that. I expected a police station. What was this place before you guys moved in?"
    miller.name "The station wasn't fit for purpose after all the chaos died down so we decided to move our main base of operations to this old storage building since it was closer to where we were needed."
    pc "Judging by the clowns at the door, I'm guessing that you needing to be here has nothing to do with crime prevention."
    miller.name "..."
    miller.name "*Sigh* Those idiots..."
    miller.name "Unfortunately, most of our time is spent trying to maintain the checkpoints into the city. It doesn't leave a lot of time for the more traditional policing."
    pc "That would explain a few things."
    miller.name "Yes it would..."
    miller.name "Anyway, as [tucker.name] asked, we have gathered up all the info he wanted. Can't say it's a lot because computers aren't what they used to be without the internet so we are stuck using paper again."
    miller.name "Follow me."
    $ walk(loc_checkpoint_lobby)
    miller.name "[tucker.name] wasn't very specific on what he wanted so we had to just gather almost everything we had on The Institute."
    miller.name "But I'm guessing you know what you are after so you can sift through all the junk."
    pc "Mmm."
    $ walk(loc_checkpoint_office_empty)
    miller.name "Here we go. Everything we have is here. Check the labels first because there are files here from before we gathered what [tucker.name] asked for."
    pc "Ok, great."
    "[miller.name] stands there uncomfortably for a few moments before turning around and leaving the room."
    hide chief with dissolve
    pcm "Clearly he wants something but is hesitant to say what."
    $ player.face_worried()
    pcm "And all these boxes... I'm gonna be here for ages looking through all this junk."
    pcm "Ok, whatever. I need to find anything related to [ant.fullname] and any of his family members. I should note down anyone he is related to or anyone who stands out."
    $ reset_temp_vars()
    $ temp_var_10 = 0
    $ player.face_neutral()
    call screen mission_police_empty_office

label main_quest_04_policestation_screen:
    if temp_var_10 == 9:
        jump main_quest_04_policestation_cont
    elif temp_var_2 and temp_var_7 and temp_var_8:
        pcm "I have some good leads, should I keep looking or head to [miller.name] and have him look these people up?"
        menu:
            "Keep looking around":
                call screen mission_police_empty_office
            "Go to see [miller.name]":

                jump main_quest_04_policestation_cont
    else:
        pcm "Suppose I should keep looking..."
    call screen mission_police_empty_office

label main_quest_04_policestation_1:
    $ player.face_worried()
    pcm "Who dumps all this stuff on a chair like that? Hmmm..."
    $ player.face_normal()
    pcm "..."
    pcm "Stuff about The Institute at least. But nothing that I can see to do with [ant.name]."
    pcm "Looks like it is all reports where both security and The Institute were involved. Almost entirely drunken pub fights that resulted in someone going to the hospital."
    pcm "Doesn't look like I will find anything relating to [ant.name] here. Although, what is this..."
    show police_office_screen_police with dissolve
    pcm "One of the delivery trucks that come in and out of here was involved in an accident just outside the city. The driver wasn't paying much attention since there are almost no cars on the highways anymore."
    pcm "Ended up ploughing into a small civilian car and forcing it off the road. The weight behind the truck meant that the truck driver was fine. But a passenger of the civilian car was ejected from the vehicle and seriously injured."
    pcm "Security arrived in force in case of sabotage or terrorist actions. Once determined it was just an accident, the injured patient was taken to the hospital along with the driver of the car."
    pcm "..."
    pcm "Dates are a match as well..."
    hide police_office_screen_police with dissolve
    jump main_quest_04_policestation_screen

label main_quest_04_policestation_2:
    $ player.face_angry()
    pcm "Random papers just put here. How am I supposed to know if this is relevant or not?"
    $ player.face_normal()
    pcm "Well, let's see here..."
    pcm "Looks like it's all the information on the people [ant.name] treated between the lockdown and him fleeing."
    pcm "I have no idea what any of this stuff means... Medical mumbo jumbo... More mumbo jumbo..."
    show police_office_screen_misc with dissolve
    pcm "Submitted complaints? By all accounts [ant.name] was a competent doctor. But here are complaints from his fellow staff members. The dates are shortly before and after his personality change."
    pcm "Hmmm. Almost all of these complaints are because he was short tempered and snapping at this staff. But this one is unusual... He submitted unauthorised blood samples for testing."
    pcm "Who was the patient... Let's see if I can find the papers here."
    pcm "Here we go. Nothing seems to stand out other than the diagnosis. White blood cells... Marrow... Myeloma... Ugh, can hardly understand most of this."
    pcm "But if I am understanding correctly, this person had an advanced case of blood cancer."
    pcm "There is almost no info on the patient, when he was admitted or discharged. No family record or next of kin. No address. Nothing. The people at the reception would never allow someone to submit such an incomplete form."
    pcm "If we assume [tucker.name] is correct that [ant.name] got a fatal diagnosis, then I would bet this is it."
    hide police_office_screen_misc with dissolve
    jump main_quest_04_policestation_screen

label main_quest_04_policestation_3:
    pcm "Riiight. Let's see here."
    pcm "Doesn't look like these have anything to do with The Institute. Officer complaint forms it looks like."
    pcm "Well, I am working with these people so doesn't hurt to be a bit nosy."
    show police_office_screen_misc with dissolve
    pcm "..."
    pcm "A million complaints for wrongful arrest. Almost all the names are female. Judging by what is written here, they are highway whores."
    pcm "If those fools that greeted me are anything to go by, they probably wanted to fuck these girls for free. When they refused they got arrested. Either that or they wanted \"commission\""
    pcm "Hmmm, this is interesting. There aren't many complaints here by men, but most of them involve [betty.name]."
    pcm "Fuck, if true, some of these are pretty bad. All of them are accusations of abuse, and a few are complaints of sexual abuse."
    pcm "She accused those clowns of being rabid dogs, but reading this stuff makes her seem like a bitch in heat."
    pcm "I should be careful around her. Although since these are all complaints by men, I might be ok."
    hide police_office_screen_misc with dissolve
    jump main_quest_04_policestation_screen

label main_quest_04_policestation_4:
    pcm "No labels and I have no idea what \"ASII\" means. Suppose I will just have a dig around anyway."
    pcm "Even looking at the papers here, I still don't have much of a clue what this is for."
    pcm "But seems like it has something to do with machinery. Vehicle maintenance maybe?"
    pcm "Whatever, nothing to do with [ant.name]."
    jump main_quest_04_policestation_screen

label main_quest_04_policestation_5:
    pcm "Stacked right at the back and labels I can't read. Risking an avalanche here."
    pcm "Aaand nothing. Looks like it is all to do with the delivery drivers. Issues they had on the way here."
    pcm "Looks like there can be a fair amount of trouble on the roads. While it doesn't seem like it happens often, looks like people living in the ruins sometime try to hijack delivery trucks."
    pcm "Security is then sent to try and flush them out. Damn this is brutal..."
    pcm "Looks like once they find out where people are hiding, they burn the building down forcing the people inside to flee. Useful prisoners are taken and the rest are allowed to go."
    pcm "Useful? There isn't much mention of who they take, but what little there is it looks like they are all young girls."
    pcm "Ugh... Let's not think about it..."
    jump main_quest_04_policestation_screen

label main_quest_04_policestation_6:
    pcm "Nice storage. \"Na, we don't need to put a pile of loose papers in a box.\""
    pcm "Delivery papers. Looks like The Institute has dedicated deliveries that are separated from the usual ones."
    pcm "No cargo manifest or details on what it might be. Well, can't get any info from snooping in these files since they keep details to a minimum."
    jump main_quest_04_policestation_screen

label main_quest_04_policestation_7:
    $ player.face_worried()
    pcm "Ugh, how am I going to get to those? If I fall and die I am going to haunt this place."
    $ player.face_exercise()
    pcm "Hupp... Ok..."
    $ player.face_normal()
    pcm "Looks like this is all documents and paperwork recovered from [ant.name]'s house. Almost entirely junk by the look of things."
    show police_office_screen_home with dissolve
    pcm "Bills, bills, bills..."
    pcm "Hmmm, four tickets to see a football match. [ant.name], his wife, wife's sister and her husband. But the sister's last name doesn't match her husband's..."
    pcm "Ugh I'm an idiot, wife's sister's second name is different here than in the other documents. Considering the dates I am guessing he was her first husband and she married someone else after."
    pcm "Better make sure to add his name to the list."
    hide police_office_screen_home with dissolve
    jump main_quest_04_policestation_screen

label main_quest_04_policestation_8:
    pcm "\"PCR reports\"? No idea what \"PCR\" means but \"reports\" sound good. Might find one on [ant.name] if I'm lucky."
    pcm "Hmmm... Personnel reports. This looks good..."
    pcm "[ant.sname]... [ant.sname]..."
    pcm "Great! Here we go."
    show police_office_screen_personnel with dissolve
    pcm "Name... Qualifications... Married but no children."
    pcm "Oh... Wife was visiting her sister when the outbreak started to be seen as serious. Wasn't able to travel back and ended up sick..."
    pcm "This caused [ant.name] to be put on watch through fear he would break quarantine to see her. She eventually died."
    pcm "..."
    pcm "No mention of the sister or husband. I suppose I should add their name to my list of people to look into."
    pcm "Wife died long before [ant.name]'s personality change so it doesn't seem like this is the reason he decided to do what he did."
    hide police_office_screen_personnel with dissolve
    jump main_quest_04_policestation_screen

label main_quest_04_policestation_9:
    pcm "Oooookayyy. No idea what the labels mean, but at least the folders are easy to reach."
    pcm "Nothing at all to do with The Institute. Looks like paperwork relating to uniform replacements."
    pcm "According to this, it is hard to keep the equipment they have repaired and they can't make new things."
    pcm "Firearms, tasers and pepper spray are completely locked down due to how rare they are. And stab vests are becoming harder to repair and supply has run out."
    pcm "Seems like many officers are settling for putting books in the lining of their stab vests for protection and just resorting to batons or other kind of blunt weapon to pacify violent people."
    pcm "Makes them seem even more like thugs..."
    jump main_quest_04_policestation_screen


label main_quest_04_policestation_cont:
    pcm "Ok, so looks like [tucker.name] was right and that [ant.fullname] had a fatal condition but only found out about it after the start of the pandemic."
    pcm "At least we can rule out him being a malicious agent and instead just a desperate person doing what he could to survive."
    pcm "So I think the first thing to do now is to look into his family members. I could talk to [miller.name] about them. Maybe he can help get the paperwork on them."
    $ walk(loc_checkpoint_lobby)
    with dissolve
    pcm "No smoking gun or anything though. This stuff might also just lead to a dead end."
    "I make my way to [miller.name]'s door and knock on it."
    miller.name "Enter."
    $ walk(loc_checkpoint_office)
    show chief at right1
    with dissolve
    miller.name "Ah Miss [sname]. Hope your search was worthwhile."
    pc "We will see. I have a few breadcrumbs to follow. Probably all dead ends but it's all I have."
    pc "Here, I need to know as much about these people as possible."
    "I hand [miller.name] the list of names."
    pc "Some of the people here are already dead, but I need to track down any family members or..."
    miller.name "This one."
    $ player.brow = 2
    pc "Huh?"
    miller.name "[alex.fname] [alex.sname]."
    miller.name "I don't know anything about the other names on this list, but there is a good chance he is who you are looking for."
    $ player.face_worried()
    pc "Ok. Who is he? A known criminal?"
    miller.name "I wouldn't go so far as to call him a criminal, but he has been on our radar for quite some time."
    $ player.face_neutral()
    miller.name "He took up residence in a building that was abandoned long before the Plague hit. Since the place was a wreck, no one really cared."
    miller.name "It has since become a place where many of the Urchins and Gamines live. Most of the flats were gutted to make room for people to lay down and sleep with a roof over their head."
    miller.name "While we haven't been able to prove any criminal activity from him and his \"gang\", this type of place attracts a lot of criminal types. Low level stuff usually."
    miller.name "Theft, drugs, bootleg alcohol, selling illegal goods... Most of it fairly benign so we don't spend too much time dealing with it as long as it doesn't spill out into the general population."
    miller.name "The people that live there call it [haven]."
    $ player.face_happy()
    pc "Sounds just like the kind of place I should pay a visit."
    $ player.face_neutral()
    miller.name "Don't even think about going there yourself. Nothing good will come of it."
    $ player.mouth = 8
    pc "Give me everything you have on this place. Since you spotted the name right away, I'm guessing you have the files easily to hand."
    miller.name "Miss [sname]. I mean this with all respect, but no. Speak to [tucker.name] and get him to let us deal with whatever you have going on there. I will not have you going there yourself."
    pc "Unfortunately what I need from there needs a much more delicate hand. And if those clods I met at the door are anything to go by, they will do much more harm than good."
    pc "I can't have those clowns putting our objective in the grave before it's even started."
    miller.name "I understand. But someone such as yourself going there might end up in... Uncomfortable situations. [haven] isn't the type of place you want to be hanging around."
    if player.iswhore or player.isslut:
        pc "I appreciate your concern, but I am not the kind of girl to shy away from such degenerates wanting to fuck me."
    elif main_quest_01.sex:
        pc "I appreciate your concern, but getting fucked by degenerate shits to reach my objectives is not new to me."
    elif main_quest_01.osex:
        pc "I appreciate your concern, but sucking some cocks to reach my objectives is not new to me."
    elif main_quest_01.hsex:
        pc "I appreciate your concern, but putting my hands in some degenerates pants to reach my objective is not new to me."
    elif player.sold >= 5:
        pc "I appreciate your concern, but using my body in the way you are suggesting is not something new to me."
    elif player.vvirgin:
        pc "I appreciate your concern, I will be sure to leave the situation as pure as I entered it."
    else:
        pc "I appreciate your concern but it is something I have to do. I can't rely on others to get this done."
    "[miller.name] stands there shocked with his mouth agape and struggles to splutter out his next sentence."
    miller.name "B-b-but... What? You are the same age as my daughter would have been. You are just a child! How can [tucker.name] expect you to go to such a place. How can you even consider it yourself."
    $ player.face_angry()
    if "school" in tab_top:
        pc "Don't let the school uniform fool you. I am no child."
    else:
        pc "Don't let my looks fool you, I am no child."
    pc "Now, I don't want to ask again. I want all the info you have on [alex.fname] [alex.sname] and this so-called [haven]."
    $ player.face_neutral()
    "[miller.name] stands looking shocked and looks like he is struggling to comprehend the situation."
    miller.name "..."
    miller.name "*Sigh* [tucker.name] is a monster sending you here..."
    miller.name "I need time to get things together and photocopied. Can you come back tomorrow for them?"
    $ player.face_happy()
    pc "No problem. Thanks for your help."
    $ player.face_neutral()
    hide chief
    $ walk(loc_checkpoint_lobby)
    with dissolve
    pcm "..."
    $ player.face_surprised()
    pcm "Phew. My heart is beating so fast. I was quite mean to him."
    $ player.face_neutral()
    pcm "As expected though, they won't dare push me since they know it might upset [tucker.name]."
    pcm "Ok, I'll come back tomorrow to get the files."
    $ walk(loc_checkpoint)
    $ player.face_normal()
    with dissolve
    $ main_quest_04.stage = 3
    $ main_quest_04.dict["wait"] = t.day
    jump travel


label main_quest_04_policestation_return:
    pcm "I wonder if I will have to deal with those fools again. They might hold a grudge."
    $ walk(loc_checkpoint_lobby)
    with dissolve
    "As I enter the refitted police station, the two clowns stand to attention and don't say a word as I pass them."
    pcm "I guess they got told off for last time..."
    pcm "Ok, off to see [miller.name] and get these files."
    "I approach [miller.name]'s office door and prepare to knock, but the door is ajar and I can hear [miller.name] talking with someone."
    miller.name "...er sweet face fool you. She is a wolf in sheep's clothes."
    $ player.face_worried()
    anon.name "You are getting soft. Letting a little girl push you around."
    miller.name "If you say so. Just don't be fooled."
    pcm "Hmm, looks like being a bit mean to him has shaken him a bit. Seems [tucker.name] carries a lot of weight with these people, and me by extension."
    pcm "How should I deal with the new voice?"
    $ player.face_annoyed()
    if player.check_nowill():
        pcm "Better not cause more waves than I already have..."
        jump main_quest_04_policestation_return_polite
    else:
        menu:
            "Enter without knocking and shake him up a bit.":
                jump main_quest_04_policestation_return_shake
            "Be polite and knock. No need to tease him as well.":
                jump main_quest_04_policestation_return_polite

label main_quest_04_policestation_return_shake:
    $ main_quest_04.missionvar2 = True
    $ walk(loc_checkpoint_office, trans=False)
    show chief at right1
    show chief_cam at right3
    with dissolve
    "I open the door without knocking first and walk directly into the room."
    $ player.mouth = 8
    pc "I don't quite appreciate being called little and you would do well to remember that in future."
    cam.name "Miss [sname]? Hello, I am..."
    pc "Someone who was just talking shit about me. Yes?"
    $ player.face_happy()
    if t.hour in morning:
        pc "Good morning, [miller.name]. I hope you have everything ready for me."
    elif t.hour in afternoon:
        pc "Good afternoon, [miller.name]. I hope you have everything ready for me."
    else:
        pc "Good evening, [miller.name]. I hope you have everything ready for me."
    miller.name "Err, yes I do. Everything about [alex.fname] [alex.sname] is in this folder."
    $ log.markdone("mq_04_c")
    $ player.face_neutral()
    pc "Thank you."
    $ player.mouth = 8
    "I turn and look at the unknown man in the office and just look him in the eyes expectantly without saying a word."
    cam.name "*Ahem* I am [cam.name]. I am in charge of overseeing operations at the train station."
    $ player.eye = 2
    pc "..."
    cam.name "..."
    pc "..."
    cam.name "Err. I am sorry for what you may have overheard. Seems I should pay more attention to what my colleague has to say."
    $ player.brow = 2
    $ player.mouth = 3
    $ player.eye = 3
    pc "I am [fname] [sname]. Pleased to meet you."
    $ player.face_neutral()
    pc "How can I help you?"
    jump main_quest_04_policestation_return_cont

label main_quest_04_policestation_return_polite:
    $ main_quest_04.missionvar2 = False
    "I knock on the door to announce myself."
    miller.name "Enter."
    $ walk(loc_checkpoint_office, trans=False)
    show chief at right1
    show chief_cam at right3
    with dissolve
    miller.name "Miss [sname]. Glad to see you. This is my colleague [cam.name]."
    cam.name "Hello Miss [sname]. I am in charge of overseeing operations at the train station."
    $ player.face_happy()
    pc "Pleased to meet you."
    $ player.face_normal()
    pc "I expect you have the files I asked for [miller.name]?"
    miller.name "Yes, here you go. Everything about [alex.fname] [alex.sname] is in this folder."
    $ log.markdone("mq_04_c")
    pc "Thank you [miller.name]."
    pc "So [cam.name], I am guessing that since you were talking about me before I arrived, you are here to see me?"
    "[cam.name] shares an awkward look with [miller.name]."
    jump main_quest_04_policestation_return_cont

label main_quest_04_policestation_return_cont:
    cam.name "Ermm, well maybe I should let [miller.name] start with that."
    miller.name "Well yes. After you last spoke, I called [tucker.name] and had a very unpleasant conversation with him."
    $ player.face_frown()
    pc "Oh?"
    miller.name "Sorry, but I felt I couldn't allow you to ignore my advice about your plans to go to [haven]."
    pc "Ok. And what did [tucker.sname] say?"
    miller.name "[tucker.sname]... [tucker.name]... Shared your \"couldn't care less\" attitude on the subject."
    pc "Mmm, as expected. So you brought your friend here to help change my mind?"
    miller.name "No... Regardless of how I feel, [tucker.name]'s words put an end to that subject. No, he has asked us to show you how things operate around here."
    cam.name "May I?"
    cam.name "[tucker.name] assures us that you can be of help to us. That your speciality is to solve issues that we can't have our own people sort out."
    pc "Sounds about right. So, what kind of issues are you having?"
    cam.name "Nothing major, but ones that would help us if they were smoothed out. Supplies going missing, conflicts between departments causing delays. That sort of thing."
    cam.name "We can't have our own people deal with it because our own people are the ones causing the problems. So [tucker.name] has asked us to make use of you to deal with the problems."
    cam.name "So, if you would come by the train station whenever you are free, I will give you the tour and explain in more detail."
    pc "Sounds good. I will pop by when I have time."
    cam.name "Thank you."
    hide chief_cam with dissolve
    pc "I am guessing you are having similar issues?"
    miller.name "Indeed. But the art for me to introduce them isn't in the game yet so we will leave it at that for the moment."
    miller.name "But when the art is in, I will introduce you to a rookie who will show you around the building, show you the checkpoint functions and give more lore about how we work."
    miller.name "Then he will take you to the highway and show the homeless and crackwhore problem."
    miller.name "Then I will introduce the betty storyline. While she has always been a strong woman, recently she has become mean and abusive. You should get close to her and find out what is going on and try to fix her."
    miller.name "This will be a new vegas style quest where you find out she was raped and she is taking her rage out, and you either convince her to seek therapy or just be more discreet in her abuse of prisoners."
    miller.name "You can also offer her to abuse you in some sexy domination/bdsm lesbian play."
    pc "Ok, I will look into it."
    miller.name "Thank you."
    hide chief
    $ walk(loc_checkpoint_lobby)
    pcm "I should get back to [tucker.name] and show him these documents."
    $ walk(loc_checkpoint)
    $ main_quest_04.stage = 4
    jump travel



screen mission_police_empty_office:

    if temp_var_1 == False:
        imagebutton auto "police_office_screen_1_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_1", True), Jump("main_quest_04_policestation_1")] focus_mask True
    if temp_var_2 == False:
        imagebutton auto "police_office_screen_2_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_2", True), Jump("main_quest_04_policestation_2")] focus_mask True
    if temp_var_3 == False:
        imagebutton auto "police_office_screen_3_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_3", True), Jump("main_quest_04_policestation_3")] focus_mask True
    if temp_var_4 == False:
        imagebutton auto "police_office_screen_4_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_4", True), Jump("main_quest_04_policestation_4")] focus_mask True
    if temp_var_5 == False:
        imagebutton auto "police_office_screen_5_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_5", True), Jump("main_quest_04_policestation_5")] focus_mask True
    if temp_var_6 == False:
        imagebutton auto "police_office_screen_6_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_6", True), Jump("main_quest_04_policestation_6")] focus_mask True
    if temp_var_7 == False:
        imagebutton auto "police_office_screen_7_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_7", True), Jump("main_quest_04_policestation_7")] focus_mask True
    if temp_var_8 == False:
        imagebutton auto "police_office_screen_8_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_8", True), Jump("main_quest_04_policestation_8")] focus_mask True
    if temp_var_9 == False:
        imagebutton auto "police_office_screen_9_%s" action [SetVariable("temp_var_10", temp_var_10 + 1), SetVariable("temp_var_9", True), Jump("main_quest_04_policestation_9")] focus_mask True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
