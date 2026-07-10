label start_home_1:
    $ walk(loc_kitchen)
    $ player.brow = 1
    show emile at right1
    emile.name "This place should have everything you need. Kitchen, bathroom, bedroom and living room. When I was staying here there were others living here as well."
    emile.name "But seems no one is here for now. Probably gone for the summer break."
    $ walk(loc_bedroom)
    show emile at right1
    emile.name "Here is your room, same one I stayed in."
    pc "Not exactly luxury living here."
    if emile.dict["tut_anger"] <= 1:
        emile.name "Nope, sorry [name] but it's about all The Institute has. I asked them if they had anything nicer when they set me up here as well."
        emile.name "\"We are not a rental agency, want something better? Find something better.\""
        pc "True..."
        emile.name "A coat of paint and some better furniture and it will be nice, don't worry."
    else:
        emile.name "Better than nothing. And don't worry, a once over with a broom will fix this place right up."

    pc "What's the neighbourhood like?"
    emile.name "Hmmm... Pretty much what you would expect from a suburban area. Lots of green space, shops that sell only the bare essentials, no nightlife and don't stay out past midnight."
    $ player.face_worried()
    pc "Don't stay out past midnight? Are things not safe round here?"
    show emile worried
    emile.name "Yeah, things have changed..."
    pc "Since I have been away, yeah you keep saying but not giving any details."
    if emile.dict["tut_anger"] == 0:
        emile.name "Yeah law and order aren't what it used to be so you can't rely on that to keep you safe."
        $ player.brow = 3
        emile.name "And sorry to say this, but the more unscrupulous types are not against just taking what they want from you."
        $ player.mouth = 9
    elif emile.dict["tut_anger"] > 3:
        if player.male_origin:
            emile.name "You'll find a cock between your legs again but it won't be your own."
            emile.name "And you won't be having any fun with it."
        else:
            emile.name "Unless you wanna get yourself gang raped in a piss smelling alleyway, don't be out past midnight."
        $ player.face_shock()
        if c.thong:
            emile.name "I'm sure that thong up your arse will make a nice trophy. Assuming a baby in your belly isn't enough of one already."
        else:
            emile.name "Be lucky if you escape without a baby in your belly."
        emile.name "Then I have no doubt that hanging from your neck from this light fixture will become an attractive option."
    else:

        emile.name "[fname], trust me... You should know what will happen so just keep yourself safe."


    pc "Ok..."
    $ player.face_neutral()
    show emile neutral
    pc "And day time?"
    emile.name "It's fine. It could be a lot worse."
    emile.name "You have a big park not far from here, a small shopping area and an outdoor market so you can buy most of what you need."
    emile.name "After you speak with the counsellor tomorrow you should probably go out and explore."
    pc "Counsellor? Like a shrink?"
    emile.name "No. More like someone who will help you out. Like it was him that got this place set up for you."
    emile.name "He's also dealing with your new ID and I imagine some other stuff. Or at least getting other people to deal with it."







    $ home.bra = daily.bra
    $ home.pants = daily.pants


    $ school.outfit = 0
    $ sport.outfit = 0
    $ swim.outfit = 0
    $ party.outfit = 0
    if c.outfit > 0:
        $ tab_left = "outfit"

    emile.name "Anyway, while we are here let's have a look at your wardrobe. You don't have much for now but I am sure in time you will get a nice collection."
    show emile at left_tutorial with dissolve:
        xzoom -1
    $ wardrobe_tutorial = True
    show screen wardrobe_screen_tutorial with dissolve


    emile.name "Here we go. Take a look here. This is your wardrobe."
    emile.name "You can pick and choose what to wear from here so pay attention."
    emile.name "At the top you can see a line of buttons, this is what style of outfit you have selected. Uniform, Daily, Formal, Sports and so on."
    emile.name "On the left the clothes are sorted into tops, bottoms, bras... You get the picture. Just press the button and you can change."
    if c.outfit:
        emile.name "Right now we are looking at outfits since the only thing you own is that dress we bought. It's in the outfits section since it covers your upper and lower body."
    else:
        emile.name "You can see right now we have tops, bottoms and underwear since that's all you own right now."
    emile.name "Now I'm sure you can see the coloured boxes all lined up. These allow you to change the colour of your clothes. Like so."
    $ daily.top_primary_colour = "white"
    $ daily.top_secondary_colour = "pink"
    $ daily.outfit_primary_colour = "pink"
    $ refresh_avatar()
    if not player.has_perk(perk_bimbo):
        pc "Pink? Not sure if that's my colour."
    else:
        pc "Pink? That's more like it."
    emile.name "I like it so we will go with it for now but you can change it to whatever colour you like afterwards. Although I think you should keep the pink."
    emile.name "You can also do the same with your underwear."
    if player.has_perk(perk_commando):
        emile.name "You can also do the same with your underwear. If you had any that is. Since you don't, I'll skip that part."
    else:
        $ tab_left = "pants"
        $ pc_strip_tops()
        $ player.mouth = 9
        pc "Ahhh!"
        show emile happy
        emile.name "Haha, calm down. Let's see..."
        $ daily.pants_primary_colour = "white"
        $ daily.pants_secondary_colour = "pink"
        $ daily.bra_primary_colour = "white"
        $ daily.bra_secondary_colour = "pink"
        $ refresh_avatar()
        emile.name "There we go! Now your underwear match."
        if player.has_perk(perk_bimbo):
            $ player.face_happy()
            pc "Oooh!"
        else:
            $ player.mouth = 8
            pc "C'mon! Pink everywhere?"

    if daily.outfit and daily.outfit in [4,11]:
        emile.name "It's too tempting. But don't worry, you can easily change it afterwards. You can put your clothes back on now."
        $ pc_dress_tops()
        emile.name "Something else you can do is change how see through things are. Have a look."
        $ daily.outfit_primary_trans = "trans_fish"
        $ refresh_avatar()
        emile.name "See, fishnet. The button on the far right of the colour pallet does this."
        $ daily.outfit_primary_trans = "trans_normal"
        $ refresh_avatar()
    else:
        emile.name "Something else you can do is change how see through things are. Have a look."
        $ daily.pants_primary_trans = "trans_fish"
        $ refresh_avatar()
        emile.name "See, fishnet. The button on the far right of the colour pallet does this. You can put your clothes back on now."
        $ daily.pants_primary_trans = "trans_normal"
        $ refresh_avatar()
        $ pc_dress_tops()


    $ home.pants_primary_colour = daily.pants_primary_colour
    $ home.pants_secondary_colour = daily.pants_secondary_colour
    $ home.bra_primary_colour = daily.bra_primary_colour
    $ home.bra_secondary_colour = daily.bra_secondary_colour


    show emile neutral
    $ player.face_neutral()
    emile.name "It's good to set up proper outfits in advance because there are some times where you will be automatically dressed. After attending the gym for example."
    emile.name "If the outfits you have picked are not appropriate then it will switch you to another outfit instead."
    pc "What's considered appropriate?"
    emile.name "Well you can't be walking around topless. Stuff like that. The outfit icon will display red instead of pink if an outfit is not appropriate. Don't worry, it's fairly flexible so you shouldn't run into trouble."
    pc "Hmm. Most of them are red."
    emile.name "Yeah. You don't have outfits picked out for those yet so they show as red. Later when you buy more stuff you can fix that."
    emile.name "The rest of the wardrobe stuff I'm sure you can figure out on your own."




    hide screen wardrobe_screen_tutorial

    $ player.mouth = 1
    $ player.brow = 1
    emile.name "But anything you buy will automatically be sent to your wardrobe."
    emile.name "And whatever you are wearing when you close the wardrobe will become your default outfit."
    emile.name "This is important. As it will count across all outfits. If you change your sportswear, then switch to your daily clothes, then close the wardrobe. The sports outfit will be saved for your sportswear automatically."
    pc "Ok, sounds a bit complicated but I'm sure I'll figure it out."
    emile.name "You will, but now we need to go to the bathroom."
    pc "We do?"
    emile.name "Yup, c'mon."
    $ walk(loc_bathroom)
    show emile at left_tutorial:
        xzoom -1

    $ show_notif_popup("Got makeup set")
    $ inv.take(item_razor, 2)

    emile.name "Here we go. Anywhere there is a mirror you can do your makeup."
    emile.name "All you do is press the mirror to put your makeup on no matter where you are."
    emile.name "But if you want to change colours or style you can only do that at home. How you do that is similar to the wardrobe, just press what colour you want."
    $ acc.eyeshadow = 1
    $ acc.blush = 1
    $ acc.lipstick = 1
    $ acc.makeup_on = True
    emile.name "And there we go, better already."
    pc "More pink? I look forward to seeing you out partying and all dolled up."
    emile.name "Not sure you will ever see that."
    if emile.days_pregnant > (global_pregnancy_length * 0.3) and player.has_perk(perk_broodmother):
        pc "Pop the baby out, get you all dressed up and we can go make some new ones."
        emile.name "Ugh!"
    else:
        pc "Sure..."
    emile.name "But now that's done, I'll leave the rest of the stuff I bought here in the cupboard. I'll go and prepare something to eat while you clean yourself up."
    pc "Yeah ok..."
    show emile happy
    emile.name "And don't do anything that will make you go blind!"
    $ player.eye = 2
    $ player.mouth = 8
    pc "Bah, shoo!!"
    emile.name "Hahaha!"
    hide emile with dissolve
    $ player.eye = 1
    $ player.mouth = 1
    pcm "Ok..."
    pcm "I'm supposed to shower now..."
    pcm "..."
    pcm "Uff, suppose I should just treat it as my own body and not be afraid of it."
    $ pc_strip_tops()
    pcm "..."
    pcm "[emile.name] was right. It looks like I might well need some time on the treadmill if I want to get rid of this belly."
    $ player.mouth = 3
    pcm "So no luck in getting some super model body that can do kung-fu or something like on TV."
    $ pc_strip()
    $ player.mouth = 1
    pcm "Ok, here we go."
    show shower with dissolve
    $ acc.makeup_on = False
    pcm "Ufff, this feels nice. First time since waking up I am not being ushered around."
    pcm "Maybe I should just stay in here."
    $ player.eye = 2
    $ player.mouth = 8
    pcm "Hah, yeah right. [emile.name] is probably already waiting outside the door for me."
    $ player.eye = 1
    $ player.mouth = 1
    pcm "Let's go..."
    hide shower with dissolve
    pause 1
    $ pc_dress()
    $ pc_strip_tops()
    pause 1
    $ pc_dress()

    pcm "Hopefully [emile.name] has made something nice to eat. Hmmm, I wonder if food will taste the same?"
    pcm "Well let's find out."
    $ walk(loc_kitchen)
    show emile pyjamas at right1 with dissolve
    emile.name "Hey. You managed to find the kitchen so you are not suddenly blind."
    $ player.eye = 2
    $ player.mouth = 8
    pc "I'm going to paint a moustache on your face while you are sleeping!"
    emile.name "Okay ok. I'm sorry."
    show emile neutral
    $ player.eye = 1
    $ player.mouth = 1
    emile.name "Anyway, sit down. I made some food but I hope it doesn't kill you."
    pc "Well it's you who cooked it so I'm sure I will be back in the hospital in a few hours."
    emile.name "Smartarse! I mean because the food is whatever was left in the fridge. I have no idea how long it's been in there. Smelled okay though."
    $ player.mouth = 2
    $ player.brow = 2
    pc "Certain death..."
    emile.name "Soon..."
    $ player.mouth = 3
    pc "Hahaha."
    $ player.mouth = 1
    $ player.brow = 1
    pc "Well, it's just toast and eggs, should be fine."
    pc "..."
    pc "So..."
    pc "Mind telling me what the hell is going on here?"
    emile.name "Well... What do you want to know?"
    $ player.mouth = 8
    pc "What I want to know??? How about everything? I understand I pretty much died and was reborn. But why in the world would they care to do something like that to me?"
    pc "It just seems like some joke to me. I am nobody to them!"
    emile.name "Hmmm. From what I understand, it is because you are a nobody that they did this to you. They didn't expect it to work..."
    $ player.mouth = 2
    pc "So it would be okay for me to just die for real? How do they even have permission to do such things?"
    show emile worried
    emile.name "Permission? Sorry [name] but a lot has happened since you were put in the hospital."
    $ player.brow = 3
    pc "The virus?"
    emile.name "You remember it?"
    show emile neutral
    pc "Well hard to forget. It's why we were coming here. Trying to get to a less populated region..."
    emile.name "Well yeah... But things got so much worse..."
    pc "How bad?"
    emile.name "..."
    $ player.mouth = 9
    pc "How bad!?"
    emile.name "Hufff... Very bad. Virtually everyone over the age of 40 dead. Economic collapse. Mass protests killing even more people..."
    pc "And what did the government do about all that?"
    emile.name "In most countries' case, collapse..."
    pc "What???"
    emile.name "You could say we were lucky. In our case, most public services were privatised and this prevented total collapse."
    $ player.mouth = 8
    pc "But?"
    emile.name "But it basically means that the government is a shell of what it was. Very little actual control. Only people like us have to abide by laws."
    emile.name "Places like The Institute don't need to worry since they are basically more powerful than the government."
    emile.name "Sorry [name], but the world you left doesn't exist anymore. We are quite literally living in a dystopian future you read about in books."
    show emile frown
    emile.name "And it all took less than a year..."
    pc "Ok... But that still doesn't explain why me and why they would do it at all."
    emile.name "Why you, again because they could. You were a test subject gifted to them on a silver platter."
    emile.name "And why at all? I'm not sure you realise the implications of what you are."
    pc "What I am? A teenage girl? So what?"
    emile.name "Yes, a teenager again. Young again..."
    $ player.brow = 2
    $ player.mouth = 4
    pc "Ah..."
    pc "Possible immortality?"
    $ player.brow = 1
    $ player.mouth = 8
    emile.name "Yes. And more. A cure for any illness if you can just swap bodies."
    pc "Wasn't there a book where people lived in new bodies and the ruling elite were basically immortal overlords?"
    emile.name "No idea. Probably. But sounds somewhat like our future now considering your new body."
    pc "Ok, so why aren't I locked in some lab somewhere?"
    emile.name "You pretty much were. You have been gone for over half a year already."
    pc "And now they release me?"
    emile.name "Yeah. Don't know why."
    pc "..."
    pc "So I wonder if I am safe. Can I even start living again or am I to keep looking over my shoulder in case I am dragged off into some dark room underground?"
    emile.name "Can't see why they would release you then just pull you back. Maybe just enjoy the now."
    emile.name "And hopefully the counsellor coming tomorrow will give us more info."
    pc "Hope so."
    emile.name "Anyway. You should get some rest. I'm tired myself so you must be exhausted."
    pc "Not really, but some time to let things settle would be good I suppose."
    emile.name "Ok."
    $ walk(loc_bedroom)
    show emile neutral at right1
    emile.name "Well, here is your room so feel free to explore it. I will sleep on the sofa in the living room."
    pc "Ok."
    emile.name "Goodnight [name]."
    $ player.mouth = 1
    if emile.love > 3:
        pc "Goodnight [emile.name]. Thanks for being here."
    else:
        pc "Goodnight [emile.name]."
    hide emile with dissolve

    pcm "Some day this has been. I don't even know what to say."
    pcm "Doesn't look like there is any going back. No finding my real body and returning to it."
    pcm "Hmm, would I even want to if given the chance I wonder."
    pcm "I don't suppose it really matters. I'm here now..."
    pcm "While it is good that I get a new lease on life, it's not like I was a wrinkly old crone before. I still had plenty of life left."
    pcm "Come to think of it. I wonder how many years this body has left anyway. Should I count starting from my physical appearance or how old the body actually is. This body can't be any more than a year old if it was grown in a lab."
    pcm "Might end up with a decade or two extra if that's the case."
    pcm "But from what [emile.name] has been saying about the world, I'm not sure if that's much of a blessing."
    if emile.days_pregnant > (global_pregnancy_length * 0.3):
        pcm "And she has a new \"blessing\". Did she find a boyfriend or something?"
    pcm "Ah well, let's find out tomorrow. I can ask whoever it is that's coming all the details about what is going on."
    $ pc_strip_tops()
    pcm "..."
    pcm "Hmmmm..."
    menu:
        "Check out my body.":
            $ pc_strip_tops()
            pcm "Since I am alone..."
            $ c.bra = 0
            show sb_pose_lookback with dissolve
            pcm "Not a single mark or blemish. Not even a mole. And of course no scars."
            pcm "My ass seems quite nice. Not a very big one but it's nice and smooth."
            if c.thong == True:
                pcm "looking nice in these pants as well. Not sure why [emile.name] was so against me buying them."
            if player.male_origin:
                if player.breasts == 1:
                    pcm "And these breasts... My breasts I suppose. Fairly modest but a decent size."
                elif player.breasts == 2:
                    pcm "And these breasts... My breasts I suppose. Although not huge, for someone my size they are pretty big."
                else:
                    pcm "And these breasts... My breasts I suppose. Not sure they could have fit any bigger ones onto my small body."
            else:
                if player.breasts == 1:
                    pcm "And my breasts... Fairly modest but a decent size."
                elif player.breasts == 2:
                    pcm "And my breasts... Although not huge, for someone my size they are pretty big."
                else:
                    pcm "And my breasts... Not sure they could have fit any bigger ones onto my small body."
            show sb_pose_showbreasts down oh with dissolve
            hide sb_pose_lookback
            pcm "..."
            if player.breasts == 1:
                pcm "Decent size and pretty firm."
            elif player.breasts == 2:
                pcm "Quite firm actually. I thought they would be softer."
            else:
                pcm "They gave me ones that are huge, though a lot firmer than I thought they would be."
            pcm "Yup, can't complain at all"
            show sb_pose_showbreasts forward worried neutral with dissolve
            pcm "..."
            pcm "Ok, enough of that..."
            hide sb_pose_showbreasts with dissolve
            if player.isfat:
                pcm "But this belly I have... [emile.name] was right about needing some time on the treadmill."
                $ player.pregnancy = 0

                $ player.mouth = 10
                pcm "Huuuuuuup."
                pcm "..."
                $ player.pregnancy = 1

                $ player.mouth = 1
                pcm "Uffffff..."
                if emile.days_pregnant > (global_pregnancy_length * 0.3):
                    pcm "Yup, could stand to trim a fair bit off."
                else:
                    pcm "Yup, could stand to trim a fair bit off if I want to be as slim as [emile.name]."
                pcm "..."
            pcm "Damn [emile.name] making me think weird things."
            if player.male_origin:
                $ c.pants = 0
                pc "Hmmm..."
                $ player.face_shy()
                show sb_mast_stand with dissolve
                pc "Do normal girls shave here or is it just in porn that they do?"
                pc "I'll decide what to do with it later. But [emile.name] did buy me razors as if it's normal so I guess it means she shaves as well."
                hide sb_mast_stand
                show sb_pose_upvag
                with dissolve
                show sb_pose_upvag spread with dissolve
                pc "..."
                $ player.face_shock()
                pc "Ah! Enough for now or I'll risk going blind."
                hide sb_pose_upvag with dissolve
                $ player.face_annoyed()
                pc "Damn [emile.name] making me think weird things."

            $ pc_set_outfit("home")
            $ pc_dress(ignore_naked=True)
            pause 1
        "Just go to sleep.":



            pc "I'll investigate another day."
    $ pc_set_outfit("home")
    $ pc_dress(ignore_naked=True)
    pcm "No pyjamas so I guess my underwear will do."
    if c.thong == True:
        pcm "Maybe these pants were not such a good idea after all. Gonna be sleeping with my arse hanging out."
    if not c.bra:
        pcm "And no bra... Whatever..."
    $ player.face_sleep()
    pause 0.3
    show screen blackout() with dissolve
    $ player.face_sleep()
    pause 1
    show emile at right1
    play music music_dis_residential fadeout 1.0 fadein 1.0
    $ block_walk_music = False
    hide screen blackout with dissolve
    pcm "ZZZZZZZZ"
    emile.name "Morning sleepy head."
    emile.name "..."
    with hpunch
    emile.name "MORNING SLEEPY HEAD!"
    $ player.eye = 2
    pc "Eeeeee..."
    emile.name "Ah good. You are awake."
    pc "Uggggg. Yeah, I wonder why."
    emile.name "I wonder. Anyway, get yourself dressed. We have the meeting soon."
    pc "Ugh, ok..."
    emile.name "I'll try and rustle up something to eat for when you are ready."
    show emile happy
    pc "Ok..."
    pc "What?"
    emile.name "Nothing."
    hide emile with dissolve
    pc "Weirdo."
    pcm "..."
    $ player.eye = 1
    pause 0.5
    $ walk(loc_kitchen)

    $ walk(loc_bathroom)
    $ pc_striptease()
    pause 0.3
    show shower with dissolve
    $ player.shower()
    pcm "Ufffff..."
    $ player.brow = 3
    pcm "Can't say I'm looking forward to this so called meeting. Feels like I find out the price I paid for selling my soul to the devil."
    pcm "Well, it's not like they killed me then are offering my life back. They saved me from my own dumb mistake. So I suppose it's a price I'll have to pay willingly."
    pcm "Still leaves a bad taste in my mouth though."
    $ player.brow = 1
    hide shower with dissolve
    pcm "Ok, let's see here."
    $ acc.makeup_on = True
    pcm "Not sure if this style fits my new face, but it will do for now."
    pause 0.5
    $ tab_top = "daily"
    $ pc_dress_under()
    pause 0.5
    $ walk(loc_kitchen)
    $ walk(loc_bedroom)
    $ pc_dress()
    pcm "I suppose at some point I should look into getting some new clothes. These are going to get smelly real fast."
    pcm "Could go to that market [emile.name] took me to yesterday. I don't have a bean to my name though."
    pcm "Ugh, same old story. It'll be the good day when I am not dead broke."
    $ walk(loc_kitchen)
    show emile at right1 with dissolve
    emile.name "Morning [name]."
    $ player.mouth = 1
    pc "Hey, food smells nice."
    show emile happy
    emile.name "What? No comment about calling an ambulance?"

    $ player.face_evil()
    pc "Ugh, I'm saving my snarky comments for later. Looks like I have a long day ahead of me."
    show emile neutral
    $ player.face_neutral()

    emile.name "You think so? Should just be a quick meeting and then that's that."
    show emile frown
    $ player.mouth = 8
    pc "Yeah right! Shady medical institute did all this out of the goodness of their heart?"
    emile.name "Well... Maybe just for the research data?"
    pc "We can only hope."
    emile.name "Well, don't worry too much. If they wanted to put a rope round your neck I'm sure they would have done it straight from the hospital."
    $ player.brow = 3
    pc "Can't say I'm worried. Terrified might be more accurate. I'm just trying my hardest to roll with the whole situation."
    emile.name "Good [name]. Good..."
    $ player.eye = 2
    $ player.mouth = 10
    $ player.puke = 1
    $ player.brow = 3
    pc "Plus, nothing is more scary than your cooking."
    show emile happy
    emile.name "Ahhh there you go."
    pc "I'm not joking..."
    $ player.mouth = 8
    show emile neutral
    emile.name "Shut up and enjoy it!"
    $ player.eye = 1
    $ player.brow = 1
    pc "Enjoy? It's not enough to just eat it. I'm forced to enjoy it as well? What kind of torture is this you have thought up?"
    emile.name "Don't make me hold you down and force feed you!"
    $ player.puke = 0
    pc "The horror!"
    emile.name "Anyway. How are you feeling?"
    pc "Feeling? No idea really. I suppose it depends on what this supposed councilor has to say."
    pc "If nothing horrible comes from it, I suppose I'm doing as well as can be given the situation."
    emile.name "That's good. He's arranged to come here first thing. It's why I woke you. So won't be long till we find out about what's going on."
    pc "Mmmm."
    "*KNOCK* *KNOCK*"
    emile.name "Speak of the devil."
    pc "Not literally I hope."
    emile.name "I'll answer the door, you go to the living room."
    pc "Ok."
    hide emile with dissolve
    pause 0.5
    $ walk(loc_common)
    pcm "..."
    pcm "Hmm, first time I've been in here actually. Let's hope it's not my last."
    show emile at right3 with dissolve
    show tucker smile at right1 with dissolve
    emile.name "Here we go. [name], this is [tucker.name], we spoke a lot about you while you were sleeping in the hospital. It was him who set up this apartment for me and for you now."
    tucker.name "Thank you [emile.name]. [fname], it's good to finally meet you. My name is [tucker.fullname]."
    tucker.name "As [emile.name] was just saying, I have been looking over the both of you since you both came into the care of The Institute."
    pc "Err. Nice to meet you...?"
    tucker.name "No need to sound so concerned. Nothing bad will happen here today. I am just here to fill in all the missing pieces you no doubt have and explain how things will be moving forward."
    pc "Well yes, the moving forward part is what I am most concerned with."
    tucker.name "Don't worry, we will get to that. First of all, [emile.name], my apologies but could I trouble you to prepare some tea while we speak alone for a bit?"
    show emile worried
    emile.name "Err, sure. [name]?"
    pc "It's fine I suppose."
    show emile frown
    emile.name "Ok..."
    hide emile with dissolve
    tucker.name "Ok, so first I will start with saying that my primary role in your case is to look after your well being."
    tucker.name "This means that although I am employed by The Institute, it was determined that I should be on your side so to speak."
    tucker.name "The Institute's goal when it comes to your case is to secure your well-being. For some people that means different things. So I have been assigned to act as your representative."
    pc "But?"
    tucker.name "But we are both still part of The Institute. So while we will do what's best for you, we are still limited in what we can do for you."
    pc "Such as?"
    tucker.name "Such as? Hmmmm. For example this apartment. It is of course within The Institutes power to put you in a luxurious mansion, but that would be counter productive for everyone involved."
    pc "Luxury living sounds good to me."
    tucker.name "On the surface yes. But there is a lot of work still needing to be done with your body. You still need to grow into it so to speak."
    pc "Grow into it?"
    tucker.name "Yes, much like a baby would grow into theirs as they get older. If we were to pamper you, you wouldn't get the stimulation needed and your body would rapidly degrade."
    tucker.name "That brings us to the reason you have been released quite suddenly. In the hospital your body had already started to degrade."
    tucker.name "It's a common occurrence when it comes to coma patients but with you it was considerably worse."
    tucker.name "We need you out here living a normal life for this project to continue to be a success."
    pc "Ok, so I understand that. My main question though is why me?"
    tucker.name "As far as I am aware, no reason. Just good timing on your part."
    tucker.name "The people in the labs were researching... Well, this. Whatever you would want to call it."
    tucker.name "They created a body. But then what? The body would just sit there and die. Allowing it to die was the initial plan as it was already a huge leap in their research."
    tucker.name "But then things went a bit south with the plague, then you turned up."
    if player.male_origin:
        pc "And what? They just thought \"Why not just stick him in there?\""
    else:
        pc "And what? They just thought \"Why not just stick her in there?\""
    tucker.name "I'm sure it was more complicated than that, but in essence, yes."
    tucker.name "You were basically dead. If it works, wonderful and everyone wins. If not, then they would get more research data."
    pc "Ok... But now what?"
    tucker.name "Before we get into that. I would like to ask how much you remember of before you woke up in the hospital?"
    pc "..."
    tucker.name "Is it that bad?"
    pc "..."
    pc "It's very fuzzy. I remember key aspects of before but almost no details. Almost as if I just listed my life in bullet points on one page."
    pc "I know how to speak of course. I recognised [emile.name]... We were running away from... The pandemic I think, or the riots?"
    tucker.name "Can you remember how old you were?"
    pc "I'm pretty sure I was older than [emile.name], but by how much I have no idea."
    tucker.name "What makes you think that?"
    pc "Just the way our relationship feels I suppose. Just like I am the older one... Hard to explain but it was just what I thought and didn't really consider it might not be the case."
    tucker.name "Ok, and what did you look like? Any details that come to mind."
    pc "What I looked like? I remember..."
    pc "..."
    pc "Not much actually. I can remember what [emile.name] looked like but not myself."
    tucker.name "Probably because you rarely look at yourself but you would look at [emile.name] all the time."
    pc "Will I remember more as time passes?"
    tucker.name "We don't know I'm afraid. It's something we need you to tell us."
    tucker.name "And that brings us to your initial question of \"Now what?\""
    tucker.name "Now we need two things from you. One simple and one not so simple. Beyond that you are free to do as you please."
    tucker.name "First of all we need you to just live a normal life. We need to know how you and the body are adapting to... Well, each other, for lack of a better term."
    pc "Should I be afraid of suddenly going blind or my teeth falling out or something?"
    tucker.name "Worried? Not at all. The eggheads are very confident in things going well or else they wouldn't have allowed you out of the lab."
    tucker.name "But of course if something like that does happen, we need to know right away."
    pc "Ok, and the second?"
    tucker.name "The second is a little more complicated. And I will start by saying that this part is outside of my ability to look after your best interests."
    $ player.face_worried()
    pc "Uh oh."
    tucker.name "\"Uh oh\" indeed I am afraid. It essentially boils down to a job only you can be trusted to do."
    tucker.name "I will give you more info on it in the coming weeks. But basically there is something The Institute wants. And you are in a unique position to get it for them."
    tucker.name "Once that is done, you are free to do as you wish."
    pc "Ok, I have more questions..."
    tucker.name "Yes, what they want has something to do with the research related to what happened to you. Beyond that, I can't tell you just yet."
    tucker.name "And why you? Hmmm... How to say this..."
    tucker.name "There is some level of forced trust between you and The Institute."
    tucker.name "You can't let anyone know about what happened for your own safety. And they can't trust anyone else with this information."
    pc "Ah, I can't say anything because then it's my neck on the chopping block."
    tucker.name "Pretty much, yes."
    pc "I'm afraid to ask, but what if I refuse?"
    tucker.name "Honestly? Probably nothing. It's why they are arranging payments on completion of tasks."
    pc "Money being the best motivation, huh?"
    tucker.name "More so these days. You have been gone for quite some time but the world is not the same one you died in. But I will let [emile.name] fill you in on those details."
    emile.name "I heard my name! Does that mean it's okay to come back?"
    tucker.name "Heh, yes it does. We are just finishing up here."
    show emile at left1 with dissolve:
        xzoom -1
    emile.name "The tea is already stone cold."
    tucker.name "That's fine, we have just one more thing. Your new legend."
    pc "\"Legend\"?"
    show emile at left1 with dissolve
    tucker.name "Yes, you already have your new name. Here we have the rest of the documentation for you. I'm afraid that for reasons beyond me, you are no longer siblings, legally speaking."
    tucker.name "Apparently it's harder to invent a new person into an already existing family than it is to just create an entirely new one. So here we are."
    pc "Miss [fname] [sname]... 18 years old... Orphan?"
    tucker.name "Yes, the academy we have set you up with is one specialised for taking in young people whose education was stopped short due to the chaos. Many of whom are now orphans."
    $ player.face_shock()
    pc "An academy!? What??"
    tucker.name "Ah yes, I almost forgot. So much info to tell..."
    $ player.face_worried()
    tucker.name "I've taken enough of your time so I will try to be brief."
    tucker.name "Since you need as much mental and physical stimulation as possible, the academy was seen as the perfect place for both."
    tucker.name "Now pay attention here. It is very important to keep on top of both your mental and physical needs. You can monitor them here."
    $ t.hour = 2
    $ t.minute = 16
    show screen right_menu
    tucker.name "See that up top?"
    pc "Ah, what's that?"
    tucker.name "It allows you to keep an eye on all your physical and mental needs. Hover over them for more information."
    tucker.name "If you don't keep on top of the more pressing needs, there might be consequences."
    emile.name "I don't see anything. What are you guys talking about?"
    tucker.name "I will pay you a visit some time later when I have more info on what is expected of you. For now, just get used to things as they are."
    tucker.name "Also I left a bag in the doorway with some clothes you will need and a bit of cash to help you get by."
    pc "Ok."
    tucker.name "Goodbye."
    emile.name "I'll show you out."
    $ log.assign("Introduction to The Institute")
    $ player.add_money(200)
    $ wardrobe.take(item_top_12)
    $ wardrobe.take(item_bottom_5)
    $ wardrobe.take(item_socks_3)
    $ wardrobe.take(item_top_8)
    $ wardrobe.take(item_bottom_8)


    $ school.top = 8
    $ school.bottom = 5
    $ school.socks = 3
    $ sport.top = 8
    $ sport.bottom = 8
    $ swim.outfit = 0

    $ school.bra = daily.bra
    $ school.pants = daily.pants
    $ sport.bra = daily.bra
    $ sport.pants = daily.pants

    $ school.inappropriate_check()
    $ daily.inappropriate_check()
    $ party.inappropriate_check()
    $ swim.inappropriate_check()
    $ home.inappropriate_check()


    $ rent_ledger.append(0)
    $ rent_ledger.append(0)

    hide tucker
    hide emile
    with dissolve


    pcm "Ok..."
    pcm "That wasn't the horror story I was expecting."
    pcm "But an academy? *Huff*"
    show emile at right1 with dissolve

    emile.name "Wish I knew he was going to bring you some clothes. I wouldn't have spent my money on that stuff for you."
    pc "How much of that were you listening to?"
    emile.name "All of it of course. Did it put your mind more at ease?"
    pc "I suppose so. As long as what they want me to do isn't too crazy then it should all be good."
    emile.name "Is it all good? I mean this new body and all?"
    pc "Well, I was thinking last night. I mean it's not like my body was stolen from me or something. I died. So I suppose I should be grateful that I am not dead anymore."
    emile.name "So no misgivings?"
    pc "Well..."
    if player.confidence >= 5:
        pc "Not really I suppose... Maybe it hasn't had time to settle in or something. But death is death. Not sure things can get much worse than that."
        pc "And I haven't woken up to having half my limbs amputated or organs removed. This body is young and healthy so I suppose I should look at this like some kind of second chance."
    else:
        pc "Hmmm maybe. Things weren't too bad for me from what little I can remember. But with the alternative being death I can't complain too much."
    emile.name "That's good that you are looking at things positively. Would hate to have a depressive little chick moping around the house."
    pc "Yeah..."
    emile.name "Let's go to the kitchen and this time I will actually make some tea for us."
    $ walk(loc_kitchen)

    emile.name "So, it seems you will be going to the academy they set up. It should be a good chance for you to meet some new people."
    pc "Maybe, but I am not a child so not sure how well I will fit in."
    $ player.right_hand = "coffee"
    emile.name "Here. The academy isn't for children. I lived with a few of them while I was here and you will probably be one of the youngest ones there. At least according to your paperwork."
    pc "Really?"
    emile.name "A lot of people were going to college or university in subjects that are just irrelevant these days. What use is an art degree when things are in such ruin."
    emile.name "So the academy basically wants to set up a safe place for people like that to adjust to the new world. Kind of like a community center."
    pc "I am guessing you didn't attend?"
    emile.name "No, I got a bit more of a helping hand from The Institute. But it wasn't easy and I got a first hand view of what can go on around here."
    emile.name "I will explain more later, for now just get used to your new body."
    $ player.right_hand = ""

    emile.name "And I should probably give you a bit of freedom. I'll be staying here for the next few days since it seems the others are away for the summer break."
    emile.name "So if there is anything you need to ask about, I'm here for you."
    pc "Ok..."
    hide emile
    show screen people_screen(_layer="bg_screen")
    with dissolve
    $ player.face_normal()
    $ talk_counter = 0
    $ diary_list = []
    $ diary_first_day = Diary_Class("Alive again", "Today was a weird day. Woke up in the hospital, told I died then rushed out onto the streets. Ugh. I have no idea what is going on. At least my sister seems to have somewhat of a clue.")

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
