label school_photo_quest_photoshoot_santa:
    $ school_photo_shoots_done += 1
    $ school_photo_date = t.day
    $ add_to_list(school_photo_quest.list,["santa","ass"])
    felix.name "The Santa shoot? Ok, I have the outfit ready so head in back to change and meet me on the set when you are ready."
    felix.name "Also, I think it's a good idea to put some red makeup on."
    pc "Right."
    hide felix
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ photo_clothes_santa()
    $ pc_strip_tops()

    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    pause 0.5
    pc "Red makeup? Hmmm..."
    if acc.makeup_on == True:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_santa()
        $ acc.makeup_on = False
        pause 0.5
    else:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_santa()
    pc "Let's see..."
    $ acc.makeup_on = True
    pc "That should do it."
    pause 0.5
    $ walk(loc_school_photostudio)
    show felix at right1
    $ player.face_happy()
    pc "How's this?"
    felix.name "Perfect!"
    $ player.face_neutral()
    pc "Ok, so what's the plan?"
    felix.name "Right... So..."
    $ player.face_annoyed()
    pc "Out with it."
    felix.name "Right, ok. So I was thinking you would sit on this and swing on it."
    $ player.face_neutral()
    pc "Ok, so why get all coy?"
    felix.name "Because I was thinking your skirt would sway while you are swinging and give a tease of your arse."
    $ player.face_worried()
    pc "At right. Will that fly? I mean isn't that too much?"
    felix.name "We will see. I will do some post production adding all Christmas effects and make it look like you are swinging on a tree bauble."
    felix.name "If it's too much then I'll hide your arse with some snowflakes or something."
    $ player.face_neutral()
    pc "Ok, well whatever. Up to you."
    pc "Sit on this?"
    felix.name "Yup."
    hide felix
    show ps_santa
    with dissolve
    pc "Hmm, skirt does ride up a fair bit. Getting a good view?"
    felix.name "I am. Now big smile."
    show ps_santa happy with dissolve
    $ player.face_happy()
    felix.name "Come on, you can do better than that."
    show ps_santa vhappy with dissolve
    felix.name "Better. Ok... Great."
    pc "Weee!"
    pc "Sorry..."
    felix.name "Mmm."
    "I sit on the swing for a while swinging around and having [felix.name] take photos from all angles. He tries for some higher up ones that probably conceal my ass and some lower ones that I doubt hides anything."
    pc "Smiling like this is making my face numb."
    felix.name "It's fine, almost done."
    felix.name "Just a few more."
    "[felix.name] gets closer for some more face shots while I sit there swinging around trying to keep a big smile on my face. Eventually it looks like he might be done."
    felix.name "Wonderful."
    if school_photo_special_request:
        felix.name "I am out of film for now, but if you want we could do some erotic or nudes with the same setting once I have developed these ones."
        pc "Right."
    felix.name "That's it for now. Get changed and meet me back in the darkroom."
    hide ps_santa
    show felix at right1
    with dissolve
    pc "Ok, and pay me?"
    felix.name "Of course."
    hide felix
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ acc = accphotobak
    pause 0.5
    $ pc_dress_quick("daily")
    pause 0.5
    $ walk(loc_school_darkroom)
    show felix at right1
    pc "All good?"
    $ photo_pay("done")
    felix.name "Yeah, here is your pay."
    pc "Great. Well, 'til next time."
    $ walk(loc_school_hallway)
    jump travel

label school_photo_quest_photoshoot_elf:
    $ school_photo_shoots_done += 1
    $ school_photo_date = t.day
    $ add_to_list(school_photo_quest.list,"elf")
    felix.name "The Elf shoot? Ok, we have a dress works. Combine that with some of the Santa bits and it should do the job."
    felix.name "The stuff should be in the back room. Go and get changed and I'll set up in the studio."
    pc "Ok."
    hide felix
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ photo_clothes_elf()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    pause 0.5
    pc "Should go for some makeup as well I suppose."
    if acc.makeup_on == True:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_elf()
        $ acc.makeup_on = False
        pause 0.5
    else:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_elf()
    $ acc.makeup_on = True
    pc "There we go. Should do the trick."
    pause 0.5
    $ walk(loc_school_photostudio)
    show felix at right1
    $ player.face_happy()
    pc "How do I look?"
    felix.name "Oh wow. Shorter than I expected."
    $ player.face_worried()
    pc "That a problem?"
    felix.name "We are taking pictures for people to wank over. What do you think?"
    $ player.face_neutral()
    pc "Hmm right."
    if "santa" in school_photo_quest.list:
        pc "So then, what's the plan? Don't think I can get away with flapping my skirt around in this outfit like with the Santa shoot. Already showing my arse off and I am just standing here."
    else:
        pc "So then, what's the plan?"
    felix.name "I was thinking you sit on this box which I will make look like a present and show off some thigh."
    pc "Only thigh?"
    felix.name "Let's see what else we can get away with considering how short the skirt is."
    pc "Ok..."
    hide felix
    show ps_elf
    with dissolve
    pc "How's this?"
    felix.name "Oooh perfect. Not only thigh but it teases a bit more."
    pc "Ok, great I guess."
    felix.name "Big smile."
    show ps_elf happy with dissolve
    $ player.face_happy()
    "I sit on the \"present\" with a big smile on my face while [felix.name] tries to find an angle that shows a good balance between modesty and sexiness."
    "The dress I am wearing hides very little so it seems a bit difficult to get a shot that doesn't look too erotic. I just leave it to him to find the right balance."
    felix.name "These ones are going to fly off the shelf."
    pc "Thanks..."
    "[felix.name] gets closer for some more face shots while I sit there trying to look happy. He also seems to be trying to get shots between my legs and of the curve of my bum."
    pc "Bit up close there no?"
    felix.name "Probably, but never know what might turn out good."
    felix.name "Not long now, almost out of film."
    "He takes a few more shots and this time it seems like he is being careful with the photos since he is low on film."
    if school_photo_special_request:
        felix.name "I am out of film for now, but if you want we could do some erotic or nudes with the same setting once I have developed these ones."
        pc "Right."
    felix.name "That's it for now. Get changed and meet me back in the darkroom."
    pc "Ok, sounds good."
    hide ps_elf
    with dissolve
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ acc = accphotobak
    pause 0.5
    $ pc_dress_quick("daily")
    pause 0.5
    $ walk(loc_school_darkroom)
    show felix at right1
    pc "All good?"
    felix.name "Yeah, here is your pay. I'll get these all developed and put in the holiday issue of the magazine."
    pc "Great."
    $ photo_pay("done")
    $ walk(loc_school_hallway)
    jump travel

label school_photo_quest_photoshoot_santa_special_picker:
    if not "santa_tasteful" in school_photo_quest.list:
        jump school_photo_quest_photoshoot_santa_tastefulnude
    elif not "elf_tasteful" in school_photo_quest.list:
        jump school_photo_quest_photoshoot_elf_tastefulnude
    elif not "santa_topless" in school_photo_quest.list:
        jump school_photo_quest_photoshoot_santa_topless
    elif not "elf_topless" in school_photo_quest.list:
        jump school_photo_quest_photoshoot_elf_topless
    else:
        $ renpy.jump(renpy.random.choice(["school_photo_quest_photoshoot_santa_topless", "school_photo_quest_photoshoot_elf_topless"]))


label school_photo_quest_photoshoot_santa_tastefulnude:
    $ photo_advance_checker("tasteful")
    $ add_to_list(school_photo_quest.list,["santa", "santa_tasteful","tasteful","ass"])
    $ school_photo_shoots_done += 1
    $ school_photo_date = t.day

    felix.name "So interested in going a bit further with the Santa shoot?"
    pc "I suppose. What do you have in mind?"
    felix.name "I already have the scene set up so pretty much the same, but with less clothes."
    pc "Of course."
    felix.name "Did you expect anything else?"
    pc "Well, no. Ok, I'll go change."
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ photo_clothes_santa()
    $ pc_strip_tops()

    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    pause 0.5
    if acc.makeup_on == True:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_santa()
        $ acc.makeup_on = False
        pause 0.5
    else:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_santa()
    $ acc.makeup_on = True
    pc "That should do it."
    pause 0.5
    $ walk(loc_school_photostudio)
    pc "Overdressed I guess. How much do you want me to remove?"
    felix.name "Just the dress. Keep the hat and socks on so we still have the same theme going on."
    $ player.face_neutral()
    pc "Ok..."
    $ c.outfit = 0
    pc "Like this?"
    felix.name "Err..."
    pc "My knickers as well?"
    felix.name "Yup."
    pc "Right."
    $ c.pants = 0
    felix.name "Perfect, so like before, have a seat up here. We will take some shots from behind and get a good view of your ass."
    show ps_santa nooutfit with dissolve
    pc "Like this?"
    felix.name "No, move your hand up a bit. Don't want everything on display."
    pc "We don't?"
    felix.name "Not yet anyway. Tease them with these and bleed them for more money offering some more."
    pc "Ah right."
    show ps_santa armup with dissolve
    felix.name "Perfect! Big smile."
    pc "Be quick. My arse is freezing on this thing."
    felix.name "Yeah yeah. Think yourself lucky I am not having you sit on something else."
    show ps_santa worried
    pc "Yet..."
    felix.name "Yet. Now c'mon, big smile."
    show ps_santa up vhappy with dissolve
    $ player.face_neutral()
    pc "Happy happy Santa..."
    felix.name "Good."
    "[felix.name] makes his way around me taking as many pictures as he can. Unlike before he is less concerned about keeping a balance between modestly and sexiness and instead is looking to make it as naughty as possible."
    "But he does make a conscious effort not to capture my breasts or between my legs. Wouldn't want to give away the goods just yet."
    felix.name "Looks good to me."
    pc "Yeah?"
    felix.name "Mmm, we will do a full display one another time if you are up for it."
    pc "We will see."
    pc "So we done?"
    felix.name "Yeah, you can dress up and see me after."
    hide ps_santa with dissolve
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ acc = accphotobak
    pause 0.5
    $ pc_dress_quick("daily")
    pause 0.5
    $ walk(loc_school_darkroom)
    pc "All good?"
    $ photo_pay("tasteful")
    felix.name "Yeah, here is your pay. I'll get working on these in the meantime."
    $ walk(loc_school_hallway)
    jump travel

label school_photo_quest_photoshoot_santa_topless:
    $ photo_advance_checker("topless")
    $ school_photo_shoots_done += 1
    $ school_photo_date = t.day
    $ add_to_list(school_photo_quest.list,["santa", "santa_topless","topless","ass","breasts"])
    felix.name "Ok, let's show of the best gift's Santa has to give."
    pc "Were you working on that joke."
    felix.name "Don't ask questions you already know the answer to."
    pc "Right, okay then... I'll go change."
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ photo_clothes_santa()
    $ pc_strip_tops()

    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    pause 0.5
    if acc.makeup_on == True:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_santa()
        $ acc.makeup_on = False
        pause 0.5
    else:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_santa()
    $ acc.makeup_on = True
    pause 0.5
    $ walk(loc_school_photostudio)
    pc "So this full nude or what?"
    felix.name "No no. We will still have the hat and socks on."
    felix.name "Just without the dress so the shoot will be more full frontal."
    pc "Ok."
    $ c.outfit = 0
    pause 0.5
    $ c.pants = 0
    pc "Sit on the swing again?"
    felix.name "Yeah, want them to be similar to the earlier shoots."
    show ps_santa nooutfit with dissolve
    felix.name "Perfect. Big smile now!"
    show ps_santa vhappy with dissolve
    pc "Get a good view you perverts."
    felix.name "Err, who?"
    pc "The perverts you will sell these photos to."
    felix.name "Ah."
    if photo_all("sex"):
        felix.name "Well, you have been fucked on camera so pretty sure they have already had the best view."
    elif photo_all("errotic"):
        felix.name "Well, you have shown off a lot more than you are now in other photos, so pretty sure they have already had a good view."
    elif photo_all("nude"):
        felix.name "Well, you have shown off a bit more in other photos, but people will still enjoy these ones."
    else:
        felix.name "Well, it is the first time showing off your tits, so pretty sure people will be getting a good rise out of them."
    pc "Mm, well either way these photos are probably going to end up all sticky, so might be able to sell them replacements."
    felix.name "Let's hope."
    felix.name "Ok, ready?"
    "As usual, I set there trying to look happy or seductive while [felix.name] takes as many photos as he can. He doesn't care this time round about capturing too much."
    "Why would he? The whole point is to show off my \"assets\" to get as many sales as possible."
    felix.name "Hmm, Give us a Santa \"Ho ho ho\" would you?"
    pc "What? Why? They can't hear me."
    felix.name "Errr."
    felix.name "I want you to open your mouth."
    pc "Err, why?"
    pc "Oh? Right..."
    show ps_santa open cheeky with dissolve
    pc "Ho, ho and ho you pervert."
    felix.name "It's what the people want."
    pc "Yeah, pretty sure you are enjoying as well."
    if felix.sex:
        felix.name "Err, well unlike these perverts, I have been inside you. But doesn't stop me from enjoying the view anyway."
    else:
        felix.name "Of course I am. But we are professionals here. Or at least try to be."
        pc "Yeah yeah, I had better not find a private collection in the dark room."
        felix.name "Err, of course I have one. I keep copies of everything."
        pc "Ok, well a sticky collection."
        if player.isbroken:
            felix.name "And would you care if I did?"
            pc "Err, not really. Have fun I suppose."
        elif player.isslut:
            felix.name "Not that I do, but knowing you, even if I did you wouldn't mind."
            felix.name "Probably even like it."
            pc "Err..."
        elif player.iswhore:
            felix.name "Knowing you, I doubt you care much as long as your pockets are lined."
            pc "Err, well..."
            pc "Got to do what's necessary..."
        else:
            felix.name "Not sure if you actually care, but no. I wouldn't treat the photo's with such little care."
            felix.name "Expensive to print them again."
    "He starts being more conservative with his photos so I assume he is running low on film now. Which is good since I am getting pretty tired just sitting here."
    felix.name "Looks good to me."
    show ps_santa neutral up
    pc "Yeah?"
    felix.name "Mmm, that will be us for the Santa stuff but we still have a topless elf to expose."
    pc "You don't want me to go further with the Santa stuff?"
    felix.name "Was thinking to have you sit on a dildo while swinging there. But then decided it would be better without the Santa stuff restricting us."
    show ps_santa worried
    pc "Right..."
    pc "So that's us done?"
    felix.name "Yeah, you can dress up and see me after."
    hide ps_elf with dissolve
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ acc = accphotobak
    pause 0.5
    $ pc_dress_quick("daily")
    pause 0.5
    $ walk(loc_school_darkroom)
    pc "All good?"
    felix.name "Yeah, here is your pay. I'll get these all developed and put them out to the buyers."
    pc "Great."
    $ photo_pay("topless")
    $ walk(loc_school_hallway)
    jump travel

label school_photo_quest_photoshoot_elf_tastefulnude:
    $ photo_advance_checker("tasteful")
    $ school_photo_shoots_done += 1
    $ school_photo_date = t.day
    $ add_to_list(school_photo_quest.list,["elf", "elf_tasteful","thigh"])
    felix.name "We are going to do a bit more of a nude shoot with the Elf outfit for the holidays"
    felix.name "The one you did before that was printed in the gazette should get people asking about something more."
    pc "Right, sounds good. I'll go change then."
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ photo_clothes_elf()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    pause 0.5
    if acc.makeup_on == True:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_elf()
        $ acc.makeup_on = False
        pause 0.5
    else:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_elf()
    $ acc.makeup_on = True
    pause 0.5
    $ walk(loc_school_photostudio)
    pc "I guess you want me to lose the dress like with the Santa shoot?"
    felix.name "Of course."
    pc "Ok."
    $ c.outfit = 0
    pc "And the pants?"
    felix.name "Yup."
    $ c.pants = 0
    felix.name "Ok, back on the box. I put a cloth down this time so your bits don't freeze while we are doing this."
    $ player.face_happy()
    pc "Thanks."
    show ps_elf nooutfit with dissolve
    $ player.face_neutral()
    pc "Hmm..."
    show ps_elf cover with dissolve
    pc "How's this for teasing? Does it cover enough?"
    felix.name "Oh perfect. Keep it pointed at the camera and it should do the job perfectly."
    pc "Great."
    show ps_elf vhappy with dissolve
    "[felix.name] starts taking a bunch of pictures while I try to keep the present in my hand angled in front of the camera so I don't expose too much."
    "He doesn't seem to worry too much about capturing my ass or what is between my crossed legs."
    "But he does try to avoid taking anything too exposing. This is a teasing shot after all."
    felix.name "Looks good to me."
    pc "Yeah?"
    felix.name "Mmm, that will be us for the Christmas shoots unless you want to show off your tits. Can make a lot of money after selling off these teasing shots."
    if photo_all("topless"):
        pc "Yeah, see what we can do next time."
    else:
        pc "We will see."
    pc "So we done?"
    felix.name "Yeah, you can dress up and see me after."
    hide ps_elf with dissolve
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ acc = accphotobak
    pause 0.5
    $ pc_dress_quick("daily")
    pause 0.5
    $ walk(loc_school_darkroom)
    pc "All good?"
    felix.name "Yeah, here is your pay. I'll get these all developed and put in the holiday issue of the magazine."
    pc "Great."
    $ photo_pay("tasteful")
    $ walk(loc_school_hallway)
    jump travel

label school_photo_quest_photoshoot_elf_topless:
    $ photo_advance_checker("topless")
    $ school_photo_shoots_done += 1
    $ school_photo_date = t.day
    $ add_to_list(school_photo_quest.list,["elf", "elf_topless","topless","breasts"])
    felix.name "Ready to show off your elvish assets?"
    pc "Rare sight. Never before seen elf gets her tits out on camera. Pay us all the money you have to see them."
    felix.name "I'll take that as a \"yes\". Go an get changed while I set things up."
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ photo_clothes_elf()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    pause 0.5
    if acc.makeup_on == True:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_elf()
        $ acc.makeup_on = False
        pause 0.5
    else:
        $ accphotobak = copy.copy(acc)
        $ photo_acc_elf()
    $ acc.makeup_on = True
    pause 0.5
    $ walk(loc_school_photostudio)
    pc "Same type of shoot like before? Sitting on the present?"
    felix.name "That's right. We will have you sitting on something else another time."
    if photo_all("errotic"):
        pc "As long as you pay me."
    else:
        pc "Yeah, we will see."
    $ c.outfit = 0
    pause 0.5
    $ c.pants = 0
    pc "Hup."
    show ps_elf nooutfit with dissolve
    $ player.face_neutral()
    pc "This good?"
    felix.name "It's perfect."
    felix.name "Now just give us an elfish smile."
    show ps_elf wink slant happy with dissolve
    pc "Come and get your presents everyone."
    felix.name "Oooh. It will get them running."
    "[felix.name] gets to taking photos of me while I try to stick my chest out. Not sure if it's because I am naked and exposed to the air or the excitement of the shoot, but my nipples are erect the entire time."
    if player.phair:
        "He makes very little attempt to keep things modest and no doubt catches glimpses of my hair down below. I am not sure if he will edit that out or sell it as an extra, but it doesn't bother me."
    else:
        "He makes very little attempt to keep things modest and if it wasn't for me being shaved, I am sure he would catch more than we initially planned."
    pc "Getting good shots?"
    felix.name "I am. These should fly off the shelves. So to speak."
    show ps_elf tounge with dissolve
    pc "More fun with my mouth?"
    felix.name "You are getting used t this aren't you?"
    if photo_all("sex"):
        pc "Well, can't compete with sex on camera but they should still enjoy it."
    elif photo_all("errotic"):
        pc "Well, shown off all the goods in other shoots so good to spice things up a bit."
    elif photo_all("nude"):
        pc "Well, shown off more in other shoots so good to give them something of interest."
    else:
        pc "Got to give them something of interest."
    felix.name "Too right."
    "[felix.name] carries on taking shots as I make different faces more fitting for the nude shots. They mostly involve me having my tongue out or my mouth open."
    "It is pretty obvious why the perverts who would buy these photos would also appreciate seeing me with my mouth open or tongue hanging out."
    "I don't much mind though. In fact it almost makes me happy, I am earning some money and at the same time making some sad perverts life a little more enjoyable."
    felix.name "Ok, that's me out of film so we can call it a day."
    pc "Yeah? okay then. I'll clean up and meet you after."
    felix.name "Mmm. And good work."
    pc "Thanks."
    hide ps_elf with dissolve
    $ walk(loc_school_photo_changingroom)
    pause 0.5
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ acc = accphotobak
    pause 0.5
    $ pc_dress_quick("daily")
    pause 0.5
    $ walk(loc_school_darkroom)
    pc "All good?"
    felix.name "Yeah, here is your pay. I'll get these all developed and put in the holiday issue of the magazine."
    pc "Great."
    $ photo_pay("topless")
    $ walk(loc_school_hallway)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
