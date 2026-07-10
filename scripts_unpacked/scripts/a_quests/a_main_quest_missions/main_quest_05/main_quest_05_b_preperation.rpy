init python:
    def haven_outfit_set():
        main_quest_05.top_primary_colour = "grey"
        main_quest_05.top_secondary_colour = "black"
        main_quest_05.bottom_primary_colour = "black"
        main_quest_05.bottom_secondary_colour = "grey"
        main_quest_05.pants_primary_colour = "black"
        main_quest_05.pants_secondary_colour = "black"
        main_quest_05.socks_primary_colour = "black"
        main_quest_05.socks_secondary_colour = "grey"
        main_quest_05.gloves_primary_colour = "black"
        main_quest_05.gloves_secondary_colour = "white"
        
        for i in clothes_wardrobe_list:
            setattr(main_quest_05, i, 0)
        
        for i in clothes_wardrobe_list:
            setattr(main_quest_05, i + "_primary_trans", "trans_normal")
            setattr(main_quest_05, i + "_secondary_trans", "trans_normal")
        
        main_quest_05.top = 11
        main_quest_05.bottom = 10
        main_quest_05.pants = 3
        main_quest_05.socks = 6
        main_quest_05.gloves = 1
        
        for i in clothes_wardrobe_list:
            if getattr(main_quest_05, i):
                wardrobe.take(globals()["item_" + i + "_" + str(getattr(main_quest_05, i))])

    def haven_outfit():
        global tab_top
        tab_top = "work"
        for i in clothes_wardrobe_list:
            setattr(work, i + "_primary_colour", getattr(main_quest_05, i + "_primary_colour"))
            setattr(work, i + "_secondary_colour", getattr(main_quest_05, i + "_secondary_colour"))
            setattr(work, i + "_primary_trans", "trans_normal")
            setattr(work, i + "_secondary_trans", "trans_normal")
            setattr(work, i, getattr(main_quest_05, i))
            setattr(c, i + "_primary_colour", getattr(main_quest_05, i + "_primary_colour"))
            setattr(c, i + "_secondary_colour", getattr(main_quest_05, i + "_secondary_colour"))
            setattr(c, i + "_primary_trans", "trans_normal")
            setattr(c, i + "_secondary_trans", "trans_normal")

label main_quest_05_preperation:
    tucker.name "Wonderful, then give me some time and I will rouse [nik.name] and..."
    tucker.name "Wait here, I will come and get you when everyone is ready."
    pc "Ok."
    hide tucker with dissolve
    pc "... ..."
    pc "..."
    $ player.face_worried()
    pcm "He didn't mention how long he would be..."
    $ player.face_normal()
    "I spend the next hour or so looking at the pictures on the walls and doing whatever I can to ward off the boredom while waiting."
    $ relax(68)
    show tucker at right1 with dissolve
    $ player.face_surprised()
    pc "Ah!"
    tucker.name "Ok, everything is getting sorted now."
    $ player.face_normal()
    pc "Ok..."
    tucker.name "While they are doing that, I will go over the plan."
    tucker.name "We have had people monitoring the building since you returned with the report on [alex.fname] [alex.sname]. There isn't much in the way of security at the entrance to the building."
    tucker.name "As long as you look like you belong, we believe you will have no issues getting inside."
    pc "Ok, so looking the part is where [nik.name] comes in."
    tucker.name "Along with our analyst who will be dealing with your clothes and makeup."
    pc "Ok..."
    tucker.name "The best time we believe for you to enter will be around 4 to 5am tomorrow morning. There aren't many people watching what's going on and there is fairly high foot traffic with the highway hookers returning to the building."
    $ player.face_worried()
    pc "Are you planning to dress me as a cheap whore?"
    tucker.name "Not quite, you will be dressed as a street gamine. If we dress you as a whore then the other whores might notice you don't belong."
    $ player.face_neutral()
    tucker.name "Once in, look around and see if you can find [ant.name]."
    pc "Ok, so what does he look like?"
    tucker.name "You are forgetting we have no idea what [ant.name] looks like right now. Our only info is he is a white male of average height and build."
    tucker.name "Height he can't change but his build has probably gotten worse."
    pc "Average. Thought you would have made a giant buff guy."
    tucker.name "No, a \"giant buff guy\" would be pretty useless in combat and would stand out too much on the subtler missions."
    pc "The male was designed for combat? Should I be worried if I run into him?"
    tucker.name "Doubt it. Takes a lot of time and effort to maintain such a body. Not something a likely underfed doctor who is used to maintaining a pampered lifestyle could do."
    tucker.name "If he is hiding in there, you are likely to find someone who is malnourished and weak."
    pc "Hmm ok. Any way I can spot him?"
    tucker.name "Possibly. You know how you are able to change your hair, skin and eye colour?"
    pc "Yes..."
    tucker.name "Well when he stole the body, he didn't have time to set these types of things properly. So the person we are looking for likely has large patches of uncoloured skin or hair."
    pc "Uncoloured as in pure white."
    tucker.name "Yes, but he is unlikely to show it easily. If his hair has white patches he would no doubt cut those parts off, or shave his head entirely. But he can't do that with his skin."
    pc "Yeah, but no doubt he will cover those parts up so I am not sure how I would be able to get a look."
    tucker.name "No doubt about that. But if you see someone inside wearing gloves, a scarf or some kind of face wrap, then they are someone worth trying to look into."
    pc "Ok, so basically check anyone out who looks suspicious. How do I inform you if I find him?"
    tucker.name "Find an appropriate time to leave and do so. The building will be monitored so one of our people will follow you. Once you are in an isolated spot they will make contact."
    tucker.name "Fill them in on all the details and they will take it from there."
    tucker.name "Or depending on the situation, you can run out screaming and our people will rush over to you. They will react based on the situation."
    pc "Once you know who and where he is, you are not afraid to get heavy handed?"
    tucker.name "That's right, subtlety is unnecessary at that point and the priority is getting [ant.name] into custody."
    tucker.name "If you are unable to locate [ant.name], I want you to somehow have a talk with [alex.fname] [alex.sname] and find out what he knows."
    tucker.name "We might not get another chance to get on [ant.name]'s tail so I don't want you leaving empty handed on this."
    $ player.face_shame()
    if main_quest_01.sex:
        pcm "He isn't some small time investigator so doubt he would be content with bending me over in an alleyway like [simon.name] was."
    elif main_quest_01.osex:
        pcm "He isn't some small time investigator so doubt he would be content with a blowjob like [simon.name] was."
    elif main_quest_01.hsex:
        pcm "He isn't some small time investigator so doubt he would be content with a handjob like [simon.name] was."
    elif player.iswhore or player.isslut:
        pcm "He isn't some small crook I can fuck for the info."
    elif player.sold >= 5:
        pcm "He isn't some small crook so I doubt offering him my body will convince him."
    else:
        pcm "He isn't the kind of person who will tell me after I ask nicely and flutter my eyes."
    pc "He won't tell me just because I asked nicely."
    tucker.name "If it were that easy then great. If not, you may have to use more creative methods."
    $ player.face_normal()
    pc "Can't I just offer him money?"
    tucker.name "If we do our job correctly, you will look like every other stray dog in the building. So he would have no reason to believe you can afford to pay."
    tucker.name "But if you can convince him, sure."
    pc "Ok, look for [ant.fullname]. If I can't find him, speak to [alex.fname] [alex.sname] and convince him to tell me what he knows."
    tucker.name "Great, now let's go pay [nik.name] and the analyst a visit for your makeover."
    $ walk(loc_hospital_ward)
    with dissolve
    tucker.name "..."
    tucker.name "We are here."
    show emile suitvest at right4 with dissolve
    $ player.face_surprised()
    pc "[emile.name]?!"
    show emile happy
    emile.name "[name]!"
    $ player.face_neutral()
    $ player.mouth = 8
    show emile neutral
    pc "Err... What are you doing here?"
    emile.name "You didn't mention anything about me yet?"
    tucker.name "I thought an explanation was better coming from you. I think I will go and see what [nik.name] is doing."
    hide tucker with dissolve
    pc "Err, ok... Why do they have you here?"
    emile.name "They have me supporting you on this mission. I will be dealing with your outfits and..."
    $ player.mouth = 2
    pc "You are working for The Institute?"
    emile.name "Yes, I've worked here since shortly after the crash."
    $ player.face_angry()
    pc "And you pick right now to let me know?"
    show emile worried
    emile.name "..."
    emile.name "They... We, didn't want you to get the wrong idea when you were offered the chance to work here as well."
    $ player.face_neutral()
    $ player.mouth = 8
    if quest_homeless_start.active:
        emile.name "If you knew I was working here, you might think me a hostage or some other weird thoughts when they said you should work for them."
    else:
        emile.name "Your resurrection was pretty shady and if you knew I was working here, you might think me a hostage or some other weird thoughts."
    $ player.face_shy()
    pc "That sounds nothing like me!"
    show emile neutral
    $ player.face_normal()
    $ player.face_neutral()
    $ player.mouth = 8
    emile.name "Heh, not at all!"
    pc "..."
    pc "Ok... Now what?"
    emile.name "Now... I suppose I get you ready to send you into that shithole..."
    emile.name "Are you sure you are up to this? It isn't too late to back out."

    pc "Worried about me? It's just a place where some of the lowest in society call their home. What is there to worry about?"
    show emile worried
    emile.name "I know we haven't hung out much since you left the hospital, but 'course I'm worried. It's a place full of whores, drunks and scummy people."



    if quest_homeless_start.active:
        pc "Can't be much worse than the shithole I arrived in. Junkie whores slumming it everywhere."
        pc "I only managed a place to stay because the last person staying there left as a corpse."
    elif pub_waitress.timesworked >= 10:
        pc "Doesn't sound much different to the pub I waitress at."
    else:
        pc "Not much different to the park then."

    emile.name "I am serious [name]!"
    if player.confidence >= 60:
        pc "Look, I can deal with this so don't worry."
    elif player.confidence >= 40:
        pc "I am pretty sure I can handle myself there so stop worrying."
    elif player.confidence >= 20:
        pc "I know this isn't ideal, but it's what I am tasked to do. Plus I need the money, so stop worrying."
    else:
        pc "I know, I can't say I am looking forward to this myself. It's pretty scary going there but it's what I am here for. And no way [tucker.name] is letting his top secret body come to harm so stop worrying."

    if player.confidence >= 40:
        pc "Anyway, what kind of whore are you going to dress me up as?"
    else:
        pc "Anyway, what kind of outfits have you picked out for me?"
    show emile frown
    emile.name "*Sigh*"
    emile.name "Here we go. This is all the stuff we picked out for you on the table here."
    "I look over the clothes on the table and notice a small pair of shorts and a weird looking top."
    if player.confidence <= 20:
        pc "Wow, not much there is there? I thought I was dressing as a gamine and not a whore?"
    else:
        pc "Not much to the outfit. Could almost pass as a whore."
    emile.name "You will be going as a street gamine. They tend to have... Odd fashion choices."
    pc "Well, if you say so."
    pc "And am I hoping for too much that those earrings are clip-ons?"
    emile.name "'Fraid not. We will get you pierced to put them on. And they aren't earrings, we have a pair for your nipples and one for your belly button."
    $ player.eye = 2
    $ player.mouth = 2
    pc "Fuck."
    if player.male_origin:
        pc "Not happy with the extra holes this body came with. You want to poke more in me..."
    emile.name "Well, that's not the worst part..."
    $ player.face_neutral()
    $ player.face_worried()
    pc "What kind of look is that?"
    show emile happy
    emile.name "What look?"
    show emile neutral
    pc "You are enjoying this aren't you? Getting some sadistic pleasure in torturing me."
    show emile happy
    emile.name "Only a little bit."
    show emile neutral
    $ player.face_neutral()
    $ player.mouth = 8
    emile.name "But this part you won't like. We need to give you a tracker."
    pc "Ok... Get to the part where I get tortured."
    emile.name "Well, there is no GPS any more so we can't track you with a tiny microchip under your skin or something. We will need to use radiolocation instead."
    emile.name "Problem with that is the transmitter is bigger than a microchip and needs a bigger power supply so we can't just put it under your skin. You will need to wear a tracker on you."
    pc "Ok, and I can't just put it in my pocket?"
    emile.name "No, your clothes are pretty tight and it would bulge. Plus it would be much easier to find on the off chance you are searched."
    emile.name "R'n'D have been looking into this for a while for you. They poured over a bunch of different ways to put something of this size on your body and eventually came up with this."
    "She hands me a clear plastic bag with a pink object inside. It clearly looks like a fairly large..."
    $ player.face_shame()
    if player.asex > 5:
        pc "Oh, a butt plug."
    else:
        pc "A butt plug!?!"
    emile.name "It is pretty well hidden and won't affect your mobility. And if it is discovered people won't scrutinise it much considering where it has been. And being that you are a gamine, it's not totally unusual."

    if acc.anus:
        pc "Errm, I kinda already have one..."
        emile.name "Do you mean at home?"
        emile.name "Please say you mean at home..."
        pc "If we wanna start calling my ass \"home\", then yes..."
        emile.name "Right... Then we will have to swap it out. This might be a bit bigger than your one."
        pc "Okay."
        emile.name "Pervert!"
        pc "Yeah yeah..."
    elif player.asex == 1:
        pcm "Well, this will at least be more pleasant than that guy..."
    elif player.asex >= 15:
        pcm "Well, not like I haven't already let a bunch of guys fuck my bum so this shouldn't be a problem."
    elif player.asex >= 5:
        pcm "Well, not like I haven't had worse up there..."
    elif player.asex > 1:
        pcm "Now even my sister wants to put things in my arse..."
    else:
        pcm "Fuck, I have never done anything like this before..."

    $ player.face_worried()
    pc "..."
    emile.name "Don't worry [name], once it's in, you won't notice it's there. The only hard part is putting it in."
    pc "Speaking from experience?"
    if tattoo.any():
        if tattoo.chest and tattoo.ass:
            emile.name "I was also planning to give you some tattoos, but looks like my practice won't be needed."
            pc "Oh? Well good job I came prepared."
        else:
            emile.name "Looks like you won't need to worry too much about getting tattoos."
            pc "Tattoos?"
            emile.name "Yes, we were planning to send you in with some cheap looking tattoos. But looks like you have some of your own."
            emile.name "So no need to worry about getting more."
        pc "What other horrors are you planning to inflict on me?"
    else:
        show emile frown
        emile.name "The worst part is still to come. We will also be giving you some tattoos. Since gamines tend to have street tattoos, I have been tasked with doing that as well."
        $ player.face_angry()
        show emile neutral
        pc "Wait no. No no no! Everything else I can remove after. But you want me to get a permanent tattoo for this mission?"
        emile.name "Na don't worry. [nik.name] can just remove it afterwards so you will be back to yourself after the mission. Anyway, we should probably get started since we don't have much time 'til you will be heading in there."
        $ player.face_worried()
    emile.name "[nik.name], we are ready over here."
    $ player.face_shame()
    pc "Wait, no we aren't."
    show tucker at right1 with dissolve
    tucker.name "Great, well there is no need for me here so I will leave you to your preparations. Good luck [fname]."
    $ player.face_sad()
    pc "*Sigh*"
    hide tucker with dissolve
    emile.name "First we will deal with your skin, hair and eyes."
    show nikolas at right1 with dissolve
    nik.name "Everything is ready over here. Please undress, Miss [sname] and we can get started."
    pc "Right, let's get this torture over with so I can go and relax in [haven] away from you monsters."
    if acc.makeup_on:
        nik.name "But before we start, that make up needs to go. Take these wipes."
        pc "Ok."
        $ acc.makeup_on = False
        nik.name "Great."
    $ acc.acc_remove()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    $ player.face_neutral()
    $ player.mouth = 8

    if player.is_dirty() or (writing.check_writing(), writing.check_writing("perm") or writing.check_writing("tattoo")):
        nik.name "So first of all let's clean you up and deal with your skin."
        $ writing.clean_writing(10)
        $ player.shower()
        if writing.check_writing("tattoo"):
            nik.name "Hmm, while the tattoos might be fitting for such a place, they might make you more of a target than you will already be."
            menu:
                "Keep them":
                    nik.name "Okay then. But be careful."
                "Get rid of them":
                    nik.name "Right..."
                    $ writing.clean_writing(tattoo=True)
                    nik.name "There we go."
    else:

        nik.name "So first of all let's deal with your skin."

    $ player.skin_colour = "1_0_base"
    $ player.nip_colour = 7
    $ refresh_avatar()





    if not player.breasts == 2:
        if player.breasts == 1:
            nik.name "And your breasts. Let's give them a bit of a boost."
        else:
            nik.name "And your breasts. Let's tone them down a little bit."
        $ player.breasts = 2
    $ player.nip_size = 2
    if player.has_perk(perk_lactating):
        nik.name "Hmm, you are lactating. I think I will have to put a stop to that."
        $ perk_lactating_end()
        $ refresh_avatar()

    nik.name "Long dark hair. [emile.name] can style it later."
    $ player.hair_style = "loose"
    $ player._hair_length = 20
    $ player.hair_fringe = 1
    $ player.hair_colour = "hair6"
    $ refresh_avatar()
    if player.phair == 0:
        nik.name "Some body hair. Girls where you are going don't have time to maintain that area."
        $ player.phair_fullgrow()

    if player.eye_colour == "eye0":
        nik.name "And the eyes can stay as they are."
    else:
        nik.name "And darker eyes."
        $ player.eye_colour = "eye0"
    $ refresh_avatar()

    nik.name "Well, that's everything from my side of things. Good luck with the rest Miss [sname]."
    pc "Yeah... Thanks."
    $ relax(30)
    hide nikolas with dissolve
    if quest_homeless_start.active:
        emile.name "Here you go, put this on for now."
    else:
        emile.name "Here, this should bring back memories."
        pc "Heh, yeah..."
    $ c.outfit = 1
    if all([tattoo.chest, tattoo.ass, acc.nipring, acc.navelring]):
        emile.name "Errm, I was planning on tattoos and piercings, but I don't think there is much more I can do that you haven't already done youself."
        emile.name "You already look the part."
        pc "Thanks."
        emile.name "It wasn't a complement."
        pc "I know..."
    else:
        emile.name "Come here, first I will deal with your tattoos to give them time to heal. Then I will give you your piercings."
        pc "Wonderful."
        emile.name "You will heal from these pretty quickly [name] so no need to stress. Some of this would normally take months to fully heal but with you it is less than a day."
        pc "Really?"
        emile.name "Yeah, that body of yours with [nik.name]'s weird injections can deal with stuff like this very rapidly. So none of this should cause you much pain."
        pc "Well, that's pretty good I suppose."
        emile.name "This might take some time, so relax. For a lot of people it's better to just close your eyes and listen to some music or something."
        emile.name "Now off with your gown and lay down here, I'll start on your back."
        show emile suitvest at right1 with dissolve
        $ c.outfit = 0
        pause 0.5

        if tattoo.ass:
            show prepare_image ass
            with dissolve
            emile.name "You already look like an easy lay with the tramp stamp, so no need to do anything there."
            pc "Wonderful."
        else:
            show prepare_image ass with dissolve
            emile.name "Good, now keep still. I've only practised this for a couple of days. Might be a bit messy but that might help it look the part. A street gamine can't afford a pro."
            $ player.face_pain()
            pc "Damn this hurts!"
            emile.name "Little bit more."
            pc "..."

            $ tattoo.ass = 1
            $ t.minute = 30


            emile.name "That should do it. You are now the proud owner of a genuine [emile.name] original tramp stamp."
            $ player.face_neutral()
            $ player.mouth = 8
            pc "What better way to look like an easy lay."

        if tattoo.chest:
            show prepare_image breasts
            with dissolve
            if tattoo.ass:
                emile.name "This one will also get the job done, so no need there either."
            else:
                emile.name "I was thinking something similar to this one. So no need to change anything here."
        else:
            emile.name "Well, it gets better, you are going to get a super original butterfly tat on your tit."
            $ player.eye = 2
            pc "..."
            emile.name "Shush! That was funny. Now here we go."
            $ player.eye = 1
            show prepare_image breasts with dissolve

            pc "Be gentle..."
            emile.name "No worries, I have been practising the art of tattooing for 2 whole days so you are in good hands."
            pc "One day I will take that needle and you will wake up with a permanent moustache."
            emile.name "Yeah yeah, you have been threatening that since we were kids and I am still 'stacheless."
            pc "One day..."

            $ tattoo.chest = 1
            $ relax(30)

            emile.name "Nice, it came out better than I thought it would."
            $ player.face_neutral()
            if not acc.nipring:
                pc "Hmm, actually it did. Maybe you found a new calling."
                emile.name "Could be, now let me poke some holes in you. Since you are here we will start with your nipples."
        if acc.nipring:
            emile.name "No need to do anything here for nipple rings..."
        else:
            $ acc.nipring = 1
        if acc.navelring:
            show prepare_image belly with dissolve
            if acc.nipring:
                emile.name "Or here."
            else:
                emile.name "This one you have will do the job."
        else:
            emile.name "There we go. Just don't be getting them caught on anything. And finally for the belly."
            show prepare_image belly with dissolve
            emile.name "This one might hurt more than the nips."
            $ acc.navelring = 1
            $ relax(30)
        emile.name "And there we have it."
        pc "Well that was a bit of a nightmare..."

        show emile at right1
        show prepare_image
        hide prepare_image with dissolve

    emile.name "Let's give that hair of yours a bit more scruff. Probably best not to brush it when you wake up tomorrow either."
    $ player.hair_style = "haven"
    $ refresh_avatar()

    emile.name "Mmm, makeup and clothes we will deal with later. But this next step is a bit of a pain in the arse."
    if player.has_perk(perk_buttplug):
        pc "I already have a pain in the arse."
        emile.name "Ha ha ha!"
        pc "I'm not talking about you."
        emile.name "Huh?"
        pc "I have a plug in my ass."
        emile.name "What? You do?"
        pc "I thought it would be fun. I didn't expect you would be wanting to put another one up there."
        emile.name "Okay then..."
        emile.name "Then I suppose we had better get that one out and the tracker put in."
    else:
        $ player.brow = 4
        $ player.eye = 2
        $ player.mouth = 8
        $ player.tear = 0
        pc "You. Are. Joking!"
        show emile happy
        pc "I will kill you!"
        show emile neutral
        emile.name "We should get this in you tonight so you can get used to it. Then you can get some sleep."
        $ player.face_neutral()
        $ player.mouth = 8
    emile.name "You will be in [haven] for some time so you might also want to find a place there you can rest up for a bit."
    pc "Yeah, better find myself a shank first in case someone decides to join me."
    emile.name "Speaking of which, let's get this inside you and then we can be done with this whole ordeal."
    pc "You are such a romantic. Is that how you speak to all the ladies?"
    emile.name "I already have you stripped naked so we are a bit past such romance, now bend over."
    pc "*Sigh*"
    pc "Let's get this over with..."
    if player.has_perk(perk_buttplug):
        show prepare_plug slant plugged with dissolve
        hide emile with dissolve
        show prepare_plug up with dissolve
        emile.name "You really do have one in your arse. I thought you were joking."
        pc "..."
        emile.name "Well, lets get this one out then."
        show prepare_plug slant plugin with dissolve
        emile.name "Ready?"
        pc "Yeah yeah."
        show prepare_plug plug with dissolve
        show prepare_plug nolarm with dissolve
        emile.name "There we go."
        emile.name "The one I am giving you is a fair bit bigger."
    else:
        show prepare_plug slant with dissolve
        hide emile with dissolve
        show prepare_plug up with dissolve

    pc "Out of curiosity, do you even have any training for this?"
    emile.name "Putting a huge plug in someone's arse? Not specifically. But I have some nurse training."
    show prepare_plug ass with dissolve
    emile.name "Most important thing is to relax."
    if player.asex > 0:
        pc "..."
    else:
        pc "Relax? How can I relax when you want to put something like that up my arse?"

    show prepare_plug lube down with dissolve
    show prepare_plug wink with dissolve
    $ player.add_desire(1)
    pc "Ahh cold."
    emile.name "Sorry, just putting a bit of lube there to make it easier."
    pc "..."

    show prepare_plug finger squint ah with dissolve
    if player.asex >= 5:
        $ player.add_desire(5)
    if player.asex > 0:
        pc "Ah, some warning would have been nice."
    else:
        pc "Haaaaiiieeeeee."
        pc "Fuck, some warning next time!"
    show prepare_plug neutral
    emile.name "Sorry, I thought you would be more used to this?"
    pc "Ahh yeah, this isn't the first time I have had my sister finger fuck my arse. How could I forget?"
    show prepare_plug up lube with dissolve
    if player.asex >= 5:
        $ player.add_desire(5)

    emile.name "Okay ok. Point taken."
    show prepare_plug down flat finger with dissolve
    if player.asex >= 5:
        $ player.add_desire(5)

    emile.name "Sorry."
    show prepare_plug lube with dissolve
    if player.asex >= 5:
        $ player.add_desire(5)

    emile.name "It's just safer to... y'know... Use the backdoor."
    pc "..."
    show prepare_plug up finger with dissolve
    if player.asex >= 5:
        $ player.add_desire(5)

    pc "School has also tried to hammer that point home but not really a topic I want to have with my sister while bent over a hospital bed."
    emile.name "..."
    show prepare_plug lube with dissolve
    if player.asex >= 5:
        $ player.add_desire(5)

    emile.name "How has it been going back to school?"
    show prepare_plug norarm nolarm with dissolve
    pc "..."
    emile.name "Yeah. Probably not the best time to ask."
    show prepare_plug plug ass with dissolve
    if player.asex >= 5:
        $ player.add_desire(5)
    pc "The plug would do better in your mouth. Might keep you quiet."
    if player.male_origin:
        emile.name "Stop complaining and take it like a man."
    else:
        emile.name "Yeah yeah, keep complaining and I won't be so gentle."
    pc "..."
    pc "I actually met some nice people."
    emile.name "Huh?"
    pc "At school. It *Ah* hasn't been entirely horrible."
    emile.name "Well, that's good. Right?"
    pc "I suppose."
    pc "A lot of *Ahh* people there who are in worse situations than us. Well, than me."
    emile.name "Not living the high life myself here y'know."
    pc "Well wouldn't know. Never saw you again after you left."
    emile.name "..."

    $ acc.anus = 1
    $ show_notif_popup("Tracker received")
    show prepare_plug plugin ah closed with dissolve

    if player.asex >= 5:
        $ player.add_desire(10)
    if player.check_horny(extreme=True):
        $ player.sex_cum(emile, "self", no_sex=True)
        pc "Ahhhhh fuck fuck..."
        emile.name "..."
        emile.name "Well, can't say that was the reaction I was expecting."
        pc "*Huff* *Huff*"
        emile.name "Well, seems I was worrying about nothing. Looks like you will take well to being plugged."
        show prepare_plug wink with dissolve
        pc "Mention this again and you will lose your tongue."
        emile.name "Okay ok."
    else:
        pc "Ah fuck fuck fuck."
        emile.name "There we go."
        pc "Haaaaaaa."
    show prepare_plug plugged ah norarm wink with dissolve
    emile.name "Considering how hard it was to put in, it shouldn't be very easy to take out."
    show prepare_plug neutral flat with dissolve
    pc "Lucky me. Haaaa..."
    emile.name "I will go and wash up. While I am gone you can put on the outfit you will head off in."
    show prepare_plug nohead neutral with dissolve
    if player.desire == 40:
        emile.name "And don't play too much with your new friend."
        pc "Shoo!"
    else:
        pc "Ok."
    pcm "Fuck, that was an experience..."
    if player.asex == 0 and player.desire == 0:
        pcm "Is that what anal sex feels like? Fuck, first experience and it's with my sister. And on top of that she made me cum."
        pc "*Sigh*"
    elif player.asex == 0:
        pcm "Is that what anal sex feels like? Fuck, first experience and it's with my sister."
    elif player.desire >= 80:
        pcm "And I am so fucking horny after that."
    elif player.desire == 0:
        pcm "I can't believe she made me cum like that. She must think me such a slut."
    pcm "Ok... How am I going to get used to this. I can feel it filling up my insides."
    hide prepare_plug with dissolve
    $ relax(30)
    pcm "Suppose I just have to get used to it. Might be wearing it for quite a while."
    if player.desire == 0:
        pcm "I wonder if they will let me keep it?"
    pcm "Anyway, time to try out these clothes I think."
    $ haven_outfit_set()
    $ haven_outfit()
    $ pc_strip()
    pcm "Hmm, let's see here. Glad it's not a thong. No idea how I would wear one with this plug in my arse."

    $ c.pants = work.pants

    pcm "Shorts that show off my arse and a top that my tits will spill out of if I'm not careful."

    $ c.top = work.top
    $ c.bottom = work.bottom
    if pub_waitress.timesworked >= 5:
        pcm "Well, at least it's not a tiny skirt. That barmaid dress I have to wear shows off my arse every time I walk. Not sure how I could get away with something like that at [haven]."
        if player.has_perk(perk_preg_want, notif=True):
            pcm "Although if I did wear something like that, the amount of pervs who will jump on me would mean I would at least leave with a bun cooking in the oven. Hmmmm..."
    pcm "Anyway. Next are some socks and gloves."
    $ c.socks = work.socks
    $ c.gloves = work.gloves
    $ t.minute = 15
    pcm "Ok... Let's find somewhere to sit and rela... Stand and relax I suppose. Lean against?"
    show emile suitvest at right1 with dissolve
    emile.name "Looking good. How you feeling?"
    if quest_homeless_start.active:
        pc "Not bad considering what I just went through. That weird injection the doctor gave me might be doing something."
        emile.name "Yeah, hopefully it keeps doing it's job."
        pc "Hopefully?"
        emile.name "C'mon, we can use one of the offices to relax a bit before all hell breaks loose."
    else:
        pc "Not bad considering what I just went through. This body's pretty resistant it seems."
        emile.name "Yeah, kinda lucked out that it wasn't an old banger. C'mon, we can use one of the offices to relax a bit before all hell breaks loose."
    pc "Sure."
    $ walk(loc_hospital_psy)
    pc "Ah, this room has a sofa at least. Maybe I can sit down properly."
    emile.name "I brought us some beer as well. Pretty sure you could do with one. And I need to get your makeup done."
    pc "Now? Not tomorrow?"
    "[emile.name] opens a couple of beers and hands me one."
    emile.name "Here we are. No, better now so it's all a bit messy like a gamine would look after staying out all night."
    $ player.add_perk(perk_drinking_beerbottle_2)
    show emile suitshirt with dissolve
    pc "Cheers. So... How come you didn't visit after you left my place?"
    emile.name "I wanted to... They felt it better if I didn't. Claimed I could harm your rehabilitation or some such if I were around too much. They was afraid I would dote on you or you would grow dependent on me."
    pc "You dote? Have they met you?"
    $ acc.makeup_reset()
    $ acc.makeup_on = True
    $ acc.eyeshadow_primary_colour = "purple"
    $ acc.eyeshadow = 1
    emile.name "..."
    emile.name "Things were a bit different after we arrived here. The world started to settle down a bit after all the chaos but it didn't settle down to the world it used to be."
    $ acc_eyeliner_primary_colour = "black"
    $ acc.eyeliner = 2
    emile.name "It is close enough to the old world to trick you into thinking it is the same. But if you let it trick you then you will end up in a horrible situation with no one to help you out of it..."
    if quest_homeless_start.active:
        emile.name "After you went missing when we came here, I worried a lot. You could have been dead for all I knew."
        emile.name "And I know it wasn't easy for you when you arrived. All the more reason to try and help you out."
    else:
        emile.name "With Mum and Dad who knows where and you in hospital, I started to think a bit differently. Having to adjust to this world alone... I didn't want you to have to do the same."
    emile.name "And I know we weren't some inseparable duo when we were growing up, but we were still close. And that old life is long dead and this new one is a bit shit."
    emile.name "So who else could I trust or turn to other than you?"
    emile.name "And so they didn't let me stay with you because yes, I would have doted on you so you didn't have to have such a horrible time adjusting."
    pc "..."
    if player.iswhore:
        pc "Well, not sure what to say. The way things have gone I might fit right in at [haven]. Might have been different if you were around."
    if player.rape >= 5:
        pc "Well, so much shit has happened I have gotten pretty numb to it by now."
    elif player.rape > 0:
        pc "Well, yeah. Had some pretty shit experiences out there that I would much rather forget."
    elif player.sold > 0:
        pc "Well yeah. I've had to do some things I would never have considered in he past just to get by."
    elif player.isslut:
        pc "Well. I think I have had a pretty good ride out of this situation all things considered."
    else:
        pc "Well I can't say it's been wonderful, but it wasn't as horrible as it could have been."

    if player.pregbabies and player.has_perk(perk_preg_want):
        pc "At least I got to bring a wonderful new life into the world though, even if I wasn't able to keep it."
    elif player.pregbabies:
        pc "Can't say having to bring a baby to term in this world is the most pleasant experience in the world though."

    $ acc.lipstick_primary_colour = "purple"

    pc "..."
    $ player.drink_current()
    pc "Would have been nice to have you around [emile.name]."
    emile.name "You just weren't equipped to be sent out alone. You got this new hot body that you had no idea about and had to face off in the world alone. It was cruel to make you do it."
    pc "It is what it is. Nothing you should be beating yourself up about."
    $ acc.nails_primary_colour = "purple"
    $ acc.nails = 1
    emile.name "..."
    emile.name "At least after my ordeals I was able to land somewhat on my feet working a nice safe job with The Institute. But you..."
    pc "Want to talk about what happened with you?"
    emile.name "*Sigh*"
    show emile suitvest with dissolve
    emile.name "Another time maybe. You should get some sleep. See you tomorrow."
    hide emile with dissolve
    "She doesn't wait for my response and just heads straight out the door without another word."
    pc "..."
    pcm "Shit... That doesn't sound like a good story."
    pc "..."
    $ player.drink_current()
    pcm "Ok..."
    pcm "I should get some sleep. Tomorrow will be a tough day."
    $ player.face_sleep()
    pause 0.2
    show screen blackout() with dissolve


    $ time_advance_to(4,55)
    $ player.set_tired(95)
    $ player.add_drunk(-100)
    if player.mood < 70:
        $ player.add_mood((70 - player.mood))



    pause 1
    show emile suitvest at right1
    $ player.face_sleep()
    hide screen blackout with dissolve
    emile.name "Time to wake up [name]!"
    $ player.eye = 2
    pc "Ugh. What the hell, it's still the middle of the night."
    emile.name "That's right. Perfect time to be sneaking you into [haven] without anyone noticing."
    emile.name "Now get your arse up. There is time for some coffee while we go over the final details then you will be heading in."
    pc "Ugh, go away. Let me sleep. You go to [haven]."
    $ player.eye = 3
    emile.name "..."
    with hpunch
    "[emile.name] walks over and grabs me by the foot and drags me off the sofa onto the floor."
    $ player.face_angry()
    $ player.eye = 2
    pc "Ah, bitch!"
    if quest_homeless_start.active:
        emile.name "Would think staying in a homeless slum would keep you on edge. They could rob you and you would complain they are making too much noise."
    else:
        emile.name "Nice to see even in your new body, you are a ray of sunshine in the morning. Now c'mon, we are waiting for you in [tucker.name]'s office."
    $ player.brow = 1
    pc "Yeah yeah."
    emile.name "And don't think about going back to sleep!"
    hide emile with dissolve
    pc "Fuck..."
    pc "..."
    pc "Better get to it then..."

    $ walk(loc_hospital_office)
    with dissolve

    $ player.eye = 2
    $ player.mouth = 8
    show tucker smile at right1
    show emile suitvest at right3
    with dissolve
    emile.name "Here you go sleeping, err, not such a beauty."
    $ player.right_hand = "coffee"
    pc "Would The Institute be upset if she were to wash up in the lake after being brutally murdered?"
    show tucker frown
    tucker.name "If that were to happen, it would probably be you who would be tasked into finding out how she was murdered."
    show emile happy
    emile.name "Would be a shame if the tracker started beeping while you were in [haven]."
    show emile neutral
    pc "Might be a relief if they remove it."
    if inv.qty(item_cigs) and player.has_perk(perk_smoker) and not player.has_perk(perk_smoking):
        "I take a cig out and light it."
        $ item_cig_smoke(False)
    tucker.name "Ok, so you will be heading into [haven] shortly so drink up and let's get you over there."
    tucker.name "You will walk there alone but some of our people will be following you at a distance and will only intervene if you are attacked or something while trying to get inside."
    tucker.name "But once you are in, we will lose visibility of you, so if you need to communicate with us, you will need to head outside or find a window."
    $ player.hands_reset()
    $ player.face_neutral()
    pc "Ok, let's get to it then."
    tucker.name "Before you head off, you had better leave your belongings here. Your money and other items will be waiting for you when you return."
    pc "Ok."



    $ main_quest_05.reward_counter = player.cash
    $ player.cash = 0
    $ inv_transfer(inv, inv_backup)




    tucker.name "Good luck."
    hide emile
    hide tucker
    $ walk(loc_hospital_lobby)
    pc "Will be a walk in the park..."
    $ walk(loc_hospital_entrance)
    pause 0.5
    $ walk(loc_revel)
    pc "Not even close to the place yet and my heart is pounding in my chest."
    if player.confidence <= 20:
        pc "I feel like I might puke."
    $ walk(loc_truckstop, time_amount=15)
    if t.wkday in weekends:
        pc "The whores around here still seem active right now."
    else:
        pc "Can still see some of the whores looking for work but seems mostly quiet right now"
    $ walk(loc_highway)
    $ walk(loc_highway_slum)
    pc "Ok, not far now. Some people giving me an odd look but probably just think I am a whore since I am out so late."
    pc "[haven] is just ahead. The odd person hanging around but nothing unusual looking."
    $ walk(loc_haven_exterior)
    $ loc_haven_exterior.locked = True

    $ loc_haven_landing.dict["gate_open"] = False
    $ main_quest_05.dict["day_entrance"] = t.day
    $ main_quest_05.reward = 200

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
