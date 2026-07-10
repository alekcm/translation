label quest_photo_startingout_picker:
    if log.interactive("photo_first_01"):
        jump quest_photo_startingout_mags_bring
    if log.interactive("photo_first_02"):
        jump quest_photo_startingout_photoshoot
    if log.interactive("photo_first_03"):
        jump quest_photo_startingout_wait
    if log.interactive("photo_first_04"):
        jump quest_photo_startingout_ready
    else:
        jump quest_photo_startingout_start

label quest_photo_startingout_start:
    pc "So, about this magazine idea of yours. What do you have in mind?"
    felix.name "Well, I am being allowed to use all this equipment and being paid a small amount to basically print propaganda material."
    pc "Propaganda?"
    felix.name "Yeah, stuff that makes this place seem nice. Get people off the streets and in here."
    pc "That was for the fliers, but how does that work with a magazine?"
    felix.name "The fliers we were just giving away and perverts were stealing them."
    pc "Right..."
    felix.name "So we sell them the material instead."
    if "mags_porn" in jaylee.conversation_topics and not jaylee.dead:
        pc "A friend does something similar, cuts up old magazines and puts the photos together."
        felix.name "Really? Do you have any of them?"
        if inv.qty(item_mag_porn):
            pc "Err... Yeah..."
            felix.name "Great! I would love to see them."
            pc "I bet you would."
        else:
            pc "Err, no. I don't."
            felix.name "Shame. I would love to see them."
            pc "I bet."
        felix.name "Actually I was going to ask you if you have seen anything like that around. Good to see what others are doing."
        felix.name "I came across the one I showed you before, but that one was old and from before things went to shit."
    elif inv.qty(item_mag_ent) or inv.qty(item_mag_porn):
        pc "I've seen stuff around, actually have some here."
        felix.name "You do? That's great. We can see what others are doing."
    else:
        felix.name "I know others are doing something similar so would be great to get a look at their magazines."
    felix.name "I don't really care what the content is. Porn or more innocent, but if you can give me a few magazines before we start it would be great."
    pc "Sure you just don't want me doing the running around to buy you porn?"
    felix.name "If only. Bring me a few and we can have a look at them and see where wo go from there."
    pc "Right, okay..."
    $ log.assign("Starting the magazine")
    $ felix.can_gift = True
    jump travel

label quest_photo_startingout_mags_bring:
    felix.name "Bring some magazines so we can have a look at them and see what others are doing."
    pc "Okay."
    jump travel

label quest_photo_startingout_magazines:
    felix.name "This should be enough magazines for now. Want to take a look?"
    if player.check_sex_agree(3, exhibitionist=True):
        pc "Sure, sitting down with a guy looking at porn mags. What could be more fun?"
        if not felix.inv.qty(item_mag_porn):
            felix.name "I didn't see any porn here. Looks fairly normal to me."
            pc "Why let the truth get in the way of a joke?"
            felix.name "Right..."
        else:
            pc "If you take your willy out, I'm leaving."
            felix.name "I'll keep that in mind."
    else:
        pc "Yeah... sure. Let's look at dirty mags together..."
    felix.name "Hmmm, most of these look like they are chopped up pictures from old magazines and just reordered."
    felix.name "Some pictures are even hand drawn."
    pc "Drawings are quite nice."
    felix.name "Mmm, they are."
    felix.name "This one is just an old magazine like the one I showed you before. So nothing new here."
    pc "So what are you thinking?"
    felix.name "Well, I imagine these are fine for the perverts, but there is nothing new here. Other than the drawings."
    felix.name "All the photos are old cut outs which is good."
    pc "Why good?"
    felix.name "Well, first of all it means there is a limited supply. Mags to cut up will run out eventually."
    felix.name "And I think anything new will be way more popular. People like imagining that they can actually meet the people in these photos."
    pc "Talking from experience?"
    felix.name "I might not be running around stealing fliers, but I am still a guy..."
    pc "Right... You're the expert."
    felix.name "Getting new photos means as long as we have print material then we can push out as many magazines as we want."
    felix.name "Can actually maybe even create a brand. People may look forward to the new issue we put out."
    pc "Will people actually pay money for them though?"
    felix.name "Guess there is only one way to find out."
    pc "Make a magazine?"
    felix.name "Yes."
    pc "How are you going to sell it?"
    felix.name "Hmm, First I will speak to the needle girls. They sell a lot of weird stuff so should be their kind of thing."
    felix.name "There is also a shop on Revel that sells sex related things so such things should be good for them as well."
    pc "Err, but we aren't doing porn, why would they care?"
    felix.name "Because they know just as we do the real reason. Plus we need someone here to do the actual selling."
    pc "Huh?"
    felix.name "It is disguised as a Blaston Academy magazine, so need to actually sell it here."
    pc "Right. Well whatever. So let's do this then?"
    felix.name "Yes, I'll get a few things ready. Come talk to me when you are ready for another shoot."
    pc "Okay."
    jump travel

label quest_photo_startingout_photoshoot:
    show felix at right1 with dissolve
    felix.name "So, ready for a photo shoot?"
    menu:
        "Sure, let's do it":
            $ NullAction()
        "Not just now":
            felix.name "Okay, well come see me when you are ready."
            hide felix with dissolve
            jump travel

    pc "What do you have in mind anyway?"
    felix.name "Well, we still need to keep things innocent while we work things out and see how far we can push things."
    felix.name "So I was thinking another shoot in your gym clothes, but with some more \"creative\" angles."
    felix.name "But go get changed and we will see as things go."
    pc "Right, in the gym again?"
    felix.name "Yeah."
    hide felix
    $ walk(loc_school_locker_girls)
    pause 0.5
    $ photo_clothes_vball_modest()
    $ pc_strip_tops()
    pause 0.5
    $ pc_strip()
    pause 0.5
    $ pc_dress_quick("work")
    $ player.set_hair("pony")
    pc "There we go..."
    $ walk(loc_school_gym, trans=False)
    show felix at right1 with dissolve
    pc "Okay. Here we go."
    felix.name "Hmmm..."
    pc "What?"
    felix.name "The top covers a lot but the shorts are quite small."
    pc "Yeah, they are."
    felix.name "I am thinking some shots that focus more on your shorts."
    pc "You mean my ass?"
    felix.name "I am trying to be sensitive here."
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "It's fine. I've no issue bending over for the camera. Get some good shots."
    else:
        pc "We both know what we are doing here..."
    felix.name "Okay then. So do some volleyball poses I guess and I'll try and get some interesting shots."
    pc "Okay."
    felix.name "And, err... maybe pull them up a bit."
    pc "So they go up my ass?"
    felix.name "If you don't mind."
    hide felix
    show ps_pose_vballass
    with dissolve
    pc "How's this?"
    felix.name "Looks good."
    "I pose in some neutral volleyball poses while [felix.name] walks around me taking shots. Most of the time he is behind me while taking photos."
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "Getting a good look at my ass?"
    felix.name "Should look innocent enough while making the perverts happy."
    "He walks around some more, this time focusing very heavily on one area while taking his shots."
    felix.name "Okay, now try something with the ball."
    pc "Hmmm..."
    hide ps_pose_vballass
    show ps_pose_vballball
    with dissolve
    pc "Should be good like this."
    felix.name "Great."
    "[felix.name] carries on taking photos, but I barely see him unless I look over my shoulder. I just stand there holding the ball while listening to the clicks of his camera."
    pc "If they are all of my arse, won't it be too obvious?"
    felix.name "Yeah, I'll have to mix in some other photos. But the ones we took before are fine for that."
    pc "Okay."
    hide ps_pose_vballball
    show ps_pose_vballpoint
    with dissolve
    pc "How's something like this?"
    felix.name "Err, does it mean something?"
    pc "Yeah, you use your fingers to tell your team mates what play to do next."
    felix.name "If you say so."
    "He carries on taking more pictures and I just stand there waiting to hear something other than the click of the camera."
    felix.name "Well, that should be enough of that."
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "Don't want me to take my shorts off?"
        felix.name "What? No! Err, why?"
        pc "More wank material?"
        felix.name "No, can't print that. It's too much."
        pc "For now."
    hide ps_pose_vballpoint
    show felix at right1
    with dissolve
    felix.name "Wonderful."
    if player.has_perk(perk_exhibitionist, notif=True):
        pc "Should try it in my bikini next time."
        felix.name "That's not a bad idea."
    felix.name "So I will get to work on these and keep you updated when I have things finished."
    pc "Sounds good."
    pc "Err, how do I get paid in all this?"
    felix.name "Oh, we didn't talk about that did we?"
    pc "Nope."
    felix.name "Well, it's a bit of a risk, but you will take profits from the sales."
    pc "Oh, so no sales no money?"
    felix.name "Unfortunately for both of us. On the other hand, more sales is more money."
    felix.name "We will soon see if any of this is worth it."
    pc "Okay."
    hide felix with dissolve
    $ pc_dress_event("party", loc_school_locker_girls)
    $ log.markdone("photo_first_02")
    $ quest_photo.workedtoday = t.day
    jump travel

label quest_photo_startingout_wait:
    felix.name "Still working on the magazine, come back later and I should have it ready."
    pc "Okay."
    hide felix with dissolve
    jump travel

label quest_photo_startingout_ready:
    felix.name "Here, take a look."
    $ inv.take(item_mag_felix)
    pc "Oooh, already seems better than the ones I gave you."
    pc "And it's not all sticky like your one."
    if polaroid_list_sold:
        pc "And you already have some of the polaroids I sold you in here?"
        felix.name "Yeah, they will do great for helping to pad out the magazine."
    else:
        pc "What are these other pictures?"
        felix.name "Well I can't just have pictures of your ass in here, so had to go around the academy taking photos of locations to pad the mag out."
    pc "And what's this? An ad?"
    felix.name "Yeah sort of. They used to do this a lot with their magazines."
    pc "What's it advertising?"
    felix.name "Nothing, I added it in to fill some pages and to let people know they can advertise in here."
    pc "More money for us?"
    felix.name "More money for us indeed."
    pc "So, they selling?"
    felix.name "Not gave them out yet, I used these as samples to speak to the needle girls and the shop on Revel. They have agreed to take some and I am just printing them off now."
    felix.name "It will probably take a while more before we find out how much we might be earning out of this."
    pc "Shame."
    felix.name "For now though, let me print these off and get them in people's hands. Once that's done we should start working on a new issue."
    pc "Oh? Any ideas?"
    felix.name "A few, but should probably still try to keep things mild for now until we find out more."
    pc "If you say so."
    felix.name "Come back in a couple of days once these are printed and we will take new photos."
    pc "Okay."
    hide felix with dissolve
    $ shop_needle.add_to_stock(item_mag_felix, 5)
    $ shop_funwear.add_to_stock(item_mag_felix, 5)
    $ log.markdone("photo_first_04")
    $ log.set_done("photo_02")
    $ quest_photo.workedtoday = t.day
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
