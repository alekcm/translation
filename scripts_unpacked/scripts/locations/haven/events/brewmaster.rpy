label haven_brewmaster_picker:
    $ show_notif_popup("Mood too low")
    if not "brew_stage" in havenvik.dict:
        $ havenvik.dict["brew_stage"] = 0
    if not havenvik.has_met:
        jump haven_brewmaster_ask
    elif renpy.has_label("haven_brewmaster_" + str(havenvik.dict["brew_stage"])):
        jump expression "haven_brewmaster_" + str(havenvik.dict["brew_stage"])
    elif "free_brew" in havenvik.conversation_topics:
        jump haven_brewmaster_free_brew
    else:
        jump haven_brewmaster_repeatable_sex_start

label haven_brewmaster_1:
    $ havenvik.dict["brew_stage"] += 1
    pcm "..."
    pcm "I really want something more to drink, but I have ran out."
    $ player.face_worried()
    pcm "Fuck, looks like I have to go back to [havenvik.name] and try and get some more..."
    pcm "*Sigh*"
    show screen blackout(100) with dissolve
    $ pc_dress()
    $ acc_shower_dress()
    $ acc.makeup_on = True
    $ walk(loc_haven_lounge)
    hide screen blackout with dissolve
    pc "Err, [havenvik.name]..."
    show haven_viktor at right1 with dissolve
    $ player.face_worried()
    havenvik.name "Back for more sweetheart?"
    pc "Yeah..."
    havenvik.name "Got money?"
    $ player.eye = 6
    pc "..."
    havenvik.name "Then your body?"
    pc "..."
    show haven_grope avoid stern with dissolve
    havenvik.name "Gonna let me ave a go with them nice firm tits?"
    pc "You got bottles for me?"
    havenvik.name "Sure, just like last time. 2 bottles."
    pc "..."
    show haven_grope grope with dissolve
    havenvik.name "Mmmm, just like I thought. So firm."
    pc "..."
    havenvik.name "Y'know love, you better start earning money round 'ere else your gonna be paying a high price to push the pain away."
    $ player.eye = 1
    show haven_grope forward neutral with dissolve
    if player.int <= 20:
        pc "What do you mean?"
        havenvik.name "You a bit dim or something?"
    else:
        pc "Next time you won't want this?"
    havenvik.name "Today I am rubbing these nice tits. Tomorrow who knows."
    havenvik.name "But without money it's not gonna be long til half of Haven is fucking you just so you can get a fix."
    show haven_grope stern with dissolve
    pc "..."
    show haven_grope neutral with dissolve
    pc "Then stop raising your prices."
    havenvik.name "Yeah right. If I give away bottles for every whore who wants to numb the pain, I'd run out before the day is out with nothing to show for it."
    havenvik.name "Only giving your tits a go because you aren't some broken down hag like most in here. But won't be long til you are all broken."
    havenvik.name "Getting my hands on some fresh meat before it gets rotten."
    show haven_grope stern with dissolve
    havenvik.name "You get it now?"
    show haven_grope waist with dissolve
    pc "..."
    hide haven_grope with dissolve
    havenvik.name "Here, 2 bottles."
    pc "Thanks..."
    havenvik.name "Mmmm."
    hide haven_viktor
    $ walk(loc_haven_hallway_2f)
    $ inv.take(item_brew, 2)
    pcm "Well, got what I wanted at least..."
    pcm "Hup."
    $ haven_drink_brew()
    pcm "..."
    pcm "Bastard is right, I have to get out of here before I end up bent over a barrel to buy some shitty booze."
    jump travel

label haven_brewmaster_2:
    $ npc_race_picker(havenvik)
    $ havenvik.dict["brew_stage"] += 1
    pcm "..."
    pcm "I really need to do what I came here for and get out."
    $ player.face_worried()
    pcm "Paying [havenvik.name]'s price just to stop me from jumping from a window is going to become too much..."
    pcm "*Sigh*"
    show screen blackout(100) with dissolve
    $ pc_dress()
    $ acc_shower_dress()
    $ acc.makeup_on = True
    $ walk(loc_haven_lounge)
    hide screen blackout with dissolve
    pc "Hi..."
    show haven_viktor at right1 with dissolve
    $ player.face_worried()
    havenvik.name "My favourite little whore."
    if not player.iswhore:
        pc "I am not a whore!"
        havenvik.name "No? Then are you paying with cash this time?"
        pc "..."
        havenvik.name "Thought so."
    pc "Let's get this over with."
    havenvik.name "Ok, but somewhere more private first."
    pc "Huh, why?"
    havenvik.name "Come."
    pc "..."
    $ walk(loc_haven_storage)
    havenvik.name "Ok, show me the goods."
    show haven_grope
    hide haven_viktor
    with dissolve
    pc "..."
    havenvik.name "C'mon, off with it."
    show haven_grope with dissolve
    $ c.top = 0
    show haven_grope grope with dissolve
    havenvik.name "Mmm, wonder how long these will stay as sexy and firm as this. Girl like you, probably not long til someone puts a baby in you and makes you all fat."

    if player.has_perk(perk_preg_want):
        pc "I'm looking forward to it."
        havenvik.name "Really? Even though you don't keep the baby? Crazy girl."
        havenvik.name "Maybe I should bend you over and give you your wish."
        if player.check_sex_agree(5):
            pc "10 bottles and you can."
            havenvik.name "What? Really?"
            pc "If you are potent enough, sure. 10 bottles and you can put your baby in me."
            havenvik.name "Fuck yes. C'mere!"
            hide haven_grope with dissolve
            show haven_bentover frown at right with dissolve
            pc "Ah, A bit eager aren't you?"
            havenvik.name "Not every day some hot little bitch comes and asks me to knock her up. These days you risk getting stabbed in the eye for it."
            pc "Well, still don't know if you are up to the task."
            show haven_bentover mast with dissolve
            havenvik.name "That's not gonna stop me from trying."
            show haven_bentover with dissolve
            $ c.bottom = 0
            $ c.pants = 0
            pc "Mmm."
            havenvik.name "What is this you have up your arse?"
            show haven_bentover smile
            pc "It's something to make sure you idiots put your cock in the right place. Can't get pregnant if you fuck me in the bum."
            havenvik.name "Yeah right. You really are a fucked up pervert."
            show haven_bentover neutral
            pc "Maybe."
            show haven_bentover poke with dissolve
            pc "Ah, you see. You aim for the right hole straight away. ♥"
            havenvik.name "You are already sopping wet. What the hell does living out in the streets do to you girls? You gotta be one of the most fucked up cunts I have ever seen."
            $ player.sex_vag(havenvik)
            show haven_bentover inside ah with dissolve
            pc "Ah fuck yes! ♥"
            show haven_bentover with hpunch
            pc "Fuck me! ♥"
            show haven_bentover with hpunch
            pc "Let me feel your cock throbbing inside me!"
            havenvik.name "You fucking slut. You will be feeling it soon. I'm gonna give you a bit fat belly and milk tits like the cow you are."
            show haven_bentover happy
            pc "Yes! Make me a fat cow!"
            pc "Haaaa so nice."
            havenvik.name "Ahhhh. Dirty girl."
            pc "Are you cumming?"
            havenvik.name "Ahh soon."
            pc "Mmmmmm yes fill me up."
            $ player.sex_cum(havenvik, "inside")
            havenvik.name "Ahhh yes!"
            pc "Ah I feel it!"
            pc "Mmmm. So nice."
            show haven_bentover poke with dissolve
            pc "Hmm, pulling out so quickly and letting everything escape?"
            havenvik.name "Fuck you really are a crazy bitch who wants to get knocked up?"
            show haven_bentover inside neutral with dissolve
            pc "I already told you I do. You not listening?"
            havenvik.name "Haa. Never know with weirdos like you."
            pc "I can feel it getting soft."
            havenvik.name "Course! I don't have the stamina of someone your age."
            pc "Shame. Could pump me fill of more."
            show haven_bentover poke with dissolve
            show haven_bentover noman with dissolve
            pc "Oh, it slipped out."
            havenvik.name "..."
            pc "Wonder if it worked? Although I guess you will never find out."
            pc "But I will know. ♥"
            havenvik.name "Come and get your bottles and get out of here. You are starting to freak me out."
            hide haven_bentover with dissolve
            pc "Give me a sec..."
            $ pc_dress()
            pcm "It's leaking into my pants..."
            $ walk(loc_haven_lounge)
            havenvik.name "..."
            havenvik.name "Here..."
            $ inv.take(item_brew, 10)
            pc "Thanks."
            havenvik.name "Not sure if I want to see you again or not."
            pc "We will find out next time."
            havenvik.name "Yeah."
            hide haven_viktor
            $ walk(loc_haven_hallway_2f)
            pcm "10 bottles should last me some time. Although if he did his job properly, maybe I shouldn't be drinking..."
            pcm "Ah well, I will cross that bridge when I get there."
            $ haven_drink_brew()
            pc "*HACK* *COUGH*"
            pc "*PHEW*"
            pcm "That hit the *COUGH* spot."
            pcm "Mmmmm..."
            $ player.pregnancy = 1
            pause 0.5
            $ player.pregnancy = 2
            pause 0.5
            $ player.pregnancy = 3
            pcm "Heh. Maybe..."
            pcm "A bit round belly and giant milk tits. Will be wonderful."
            pcm "Will find out when I leave this shithole."
            $ player.pregnancy = 0
            jump travel
        elif player.pregbabies > 0:
            pc "Already been knocked up before and not sure I want to carry your baby while in this shithole."
        else:
            pc "While getting knocked up sounds like a good plan. Think I will wait until I leave this shithole first."

    elif player.pregbabies > 0:
        pc "Been there. Still managed to get my body back in shape."
        havenvik.name "Mmm lucky you. Most of the hags round here turn to shit afterwards. Having the baby taken doesn't help much."

    elif player.has_perk(perk_preg_notwant):
        pc "Yeah not gonna happen. Not letting any of you perverts put a baby in me."
    else:
        pc "Keep your perversions to yourself."

    havenvik.name "Whatever. At least I get a go of them now while they are still nice. How 'bout you gimme a hand?"
    pc "Huh?"
    havenvik.name "Put your hands to use. These tits are making me hard."
    pc "Ugh..."
    pc "*Sigh*"
    $ player.sex_hand(havenvik)
    show haven_grope mast penis stern with dissolve
    havenvik.name "That's better."
    show haven_grope neutral
    pc "All these whores around and you get hard so easily?"
    havenvik.name "Think I wanna do anything with most of the rotten hags in this place? Fresh meat like you is rare."
    havenvik.name "Not sure I have ever seen any tits as nice as these in Haven."
    pc "Nice. I am just a pair of tits am I?"
    havenvik.name "No, I will have a go at that pussy as well soon."
    pc "Degenerate."
    havenvik.name "You are the one whoring these tits out for some bottles of brew. So don't you be looking down on me."
    havenvik.name "In fact..."
    "He puts his hands on my shoulders and pushes me down."
    hide haven_grope
    show haven_blow wait
    with dissolve
    havenvik.name "Much nicer when a little slut is looking up at you. Have a closer look."
    pc "..."
    havenvik.name "Well, don't be shy. Get to work."
    pcm "Work... Fuck..."
    show haven_blow ballrub with dissolve
    pcm "Good job the fuckers in this place are washed and clean or I might puke with my face this close."
    if player.check_sex_agree(2):
        pcm "It's actually kind of a nice cock..."
        if player.check_sex_agree(4):
            $ player.sex_oral(havenvik)
            show haven_blow 2h with dissolve
            havenvik.name "Haaa fuck. Didn't expect that..."
            havenvik.name "Shit shit..."
            havenvik.name "Nooo..."
            $ player.sex_cum(havenvik, "mouth")
            havenvik.name "Haaaa shit aaaaaaaa..."
            havenvik.name "Ah fuck..."
            havenvik.name "Haaaaa."
            show haven_blow wait ub with dissolve
            pause 0.5
            show haven_blow neutral with dissolve
            pc "Didn't manage to last very long."
            havenvik.name "Fuck, I wasn't expecting you to put it in your mouth. Caught me off guard."
            pc "What else does a girl do when on her knees with a cock in her face?"
            havenvik.name "..."
            hide haven_blow with dissolve
            pc "Now your end of the bargin."
            havenvik.name "Sure, follow me."
            pc "Hold on."
            $ pc_dress()
            pc "Ok."
            $ walk(loc_haven_lounge)
            havenvik.name "Here."
            $ inv.take(item_brew, 4)
            pc "Thanks. 4 bottles?"
            havenvik.name "Yeah, now sod off."
            pc "Ha. Sure."
            hide haven_viktor
            $ walk(loc_haven_hallway_2f)
            pcm "Well, got more than I wanted. 4 bottles of brew to wash his cum down with..."
            pcm "Hup."
            $ haven_drink_brew()
            jump travel

    pcm "Oh well, let's get to \"work\"."
    havenvik.name "Ah those tits of yours look even more sexy from this angle."
    pc "So glad to know that..."
    havenvik.name "Mmmmm."
    pc "Your cock is hard as a rock. Not gonna last long are you?"
    havenvik.name "Fuck no. Not often someone as sexy as you comes along."
    pc "Been a while since it's been someone else's hand?"
    havenvik.name "Too long... *Huff*"
    pc "Surprised you guys don't just go all spartan and help each other out."
    havenvik.name "It happens, but I have something to trade so can usually attract someone nicer."
    pc "I can see that..."
    havenvik.name "Haaaa..."
    pc "And feel that..."
    havenvik.name "Ah I am cumming... Nnnngg."
    if player.check_sex_agree(3):
        show haven_blow cum with dissolve
        havenvik.name "Ah fuck, you want it there?"
        show haven_blow lookup
        pc "*Nnk*"
        show haven_blow lookdown
        havenvik.name "Haaaa yesss!"
        $ player.sex_cum(havenvik, "mouth")
        havenvik.name "Haaaaa."
        havenvik.name "Yes!!!"
        show haven_blow wait ub with dissolve
        pause 0.5
        show haven_blow neutral with dissolve
        pc "Now your end of the bargin."
        havenvik.name "Haaa..."
        hide haven_blow with dissolve
        havenvik.name "Yeah... Follow me."
        pc "Hold on."
        $ pc_dress()
        pc "Ok."
        $ walk(loc_haven_lounge)
        havenvik.name "Here."
        $ inv.take(item_brew, 3)
        pc "Thanks. 3 bottles?"
        havenvik.name "Yeah, now sod off."
        pc "Ha. Sure."
        hide haven_viktor
        $ walk(loc_haven_hallway_2f)
        pcm "Well, got more than I wanted. 3 bottles of brew to wash his cum down with..."
        pcm "Hup."
        $ haven_drink_brew()
        jump travel
    else:

        show haven_blow wait ah with dissolve
        $ player.sex_cum(havenvik, "face")
        havenvik.name "Haaaaa."
        havenvik.name "Yes!!!"

        pc "All over my face..."
        pc "*Sigh* Gonna need to go to the showers."
        show haven_blow neutral with dissolve
        havenvik.name "Could have put it in your mouth."
        pc "Yeah right. Let's see those bottles."
        hide haven_blow with dissolve
        havenvik.name "Yeah... Follow me."
        pc "Hold on."
        $ pc_dress()
        pc "Ok."
        $ walk(loc_haven_lounge)
        havenvik.name "Here."
        $ inv.take(item_brew, 2)
        pc "Thanks."
        hide haven_viktor
        $ walk(loc_haven_hallway_2f)
        pcm "Well, got what I wanted but going to have to wash my face. Hope no one sees me."
        pcm "Who am I kidding. Place full of whores, doubt anyone gives a shit seeing one covered in cum."
        pcm "Hup."
        $ haven_drink_brew()
        jump travel

label haven_brewmaster_3:
    $ havenvik.dict["brew_stage"] += 1
    pcm "*Sigh* Do I really need to go back to that [havenvik.name] for another drink?"
    $ player.face_worried()
    pcm "..."
    pcm "Let's get this over with."
    show screen blackout(100) with dissolve
    $ pc_dress()
    $ acc_shower_dress()
    $ acc.makeup_on = True
    $ walk(loc_haven_lounge)
    show haven_viktor at right1
    hide screen blackout with dissolve
    havenvik.name "Back for more?"
    pc "Yeah..."
    if havenvik.vsex > 0:
        havenvik.name "How did you manage to go through that many bottles in that amount of time. You should've had plenty."
        pc "..."
        havenvik.name "Don't tell me you just come back for another fucking? Wanna make sure I put a baby in you for sure?"
        pc "I just want more bottles..."
    elif havenvik.osex > 0:
        havenvik.name "Well, won't say no to you sucking my cock again."
    havenvik.name "Let's go somewhere more private."
    pc "..."
    $ walk(loc_haven_storage)
    havenvik.name "I wanna see everything you have to offer."
    pc "What?"
    havenvik.name "Take off your clothes. I wanna see it all."
    pc "Ok."
    $ c.top = 0
    havenvik.name "Will never get tired of those tits. Easier to suck on them without the rings though."
    if havenvik.vsex > 0:
        havenvik.name "If I did put a baby in you and they get all milky, come back and let me suck on them some. I gave you my milk so only fair you give me yours."
        pc "Maybe I will bottle it and sell it to the rest of the scum in this place. Might let me buy the brew instead of getting fucked for it."
        havenvik.name "Hah, good idea. Set up a real milking machine in here for you."
        pc "Heh."
    if not havenvik.vsex > 0:
        havenvik.name "But I am eager to see the rest down below."
        havenvik.name "Hmm, wonder if it is hairy or shaved."
        pc "Yeah right. Like I am going to use a razor in the shared showers. Not like I can get my hands on disposable razors anymore."
        havenvik.name "Yeah, but I had some hope I would see a nice clean shaved pussy."
        pc "You been looking at too many porn mags from before the pandemic."
        havenvik.name "Yeah right. Any porn you get your hands on these days have all the pages stuck together."
        havenvik.name "But c'mon, get em off."
        pc "..."
        $ c.bottom = 0
        $ c.pants = 0
    else:
        havenvik.name "But let's see that hairy pussy of yours."
        pc "You already got a pretty good close up of it before. What is so special about seeing it again."
        havenvik.name "So what? I will never reject seeing a hot naked girl."
        pc "*Sigh*"
        $ c.bottom = 0
        $ c.pants = 0

    havenvik.name "Ahh lovely."
    pc "..."
    havenvik.name "..."
    pc "What? If that's it, then hand over some bottles."
    havenvik.name "I am just getting a good look."
    pc "..."
    havenvik.name "Fuck. So sexy."
    havenvik.name "I want you to suck my cock."
    pc "What?"
    havenvik.name "Suck my cock. I want you to get on your knees and put my cock in your mouth."
    if havenvik.vsex > 0:
        pc "Would have thought you would want to fuck me again."
        havenvik.name "Well it was nice, but I want something new. You haven't sucked my cock yet so it's what I want."
        pc "Well, ok..."
        havenvik.name "Disappointed?"
        pc "Just not what I expected."
        havenvik.name "Got plenty of chances for me to fuck a baby in you."
    pc "Ok..."
    show haven_blow wait neutral with dissolve
    pc "..."
    $ player.sex_oral(havenvik)
    show haven_blow 1h with dissolve
    havenvik.name "Mmmm. Just like that..."
    havenvik.name "You must make a pretty good whore out there."
    pc "Mmmmm."
    havenvik.name "Suck on my balls and I will give you a couple more."
    if player.iswhore:
        pcm "Fuck, a whore out there and one in here..."
    else:
        pcm "Fuck, being treated like a real whore here."
    show haven_blow ballsuck with dissolve
    havenvik.name "Ah fuck yes!"
    havenvik.name "Never had a girl do this to me before."
    pcm "Lucky me..."
    havenvik.name "Haa yes so nice. Suck on them you little slut."
    havenvik.name "My balls are full of cum and waiting for you to swallow it. I haven't cum since the last time you were selling yourself."
    if player.has_perk(perk_preg_want):
        if havenvik.vsex > 0:
            pc "So not trying again to get me pregnant?"
        else:
            pcm "He wants to cum in my mouth so no chance of babies for me?"
    else:
        pcm "Hmm yes. Better make him cum in my mouth before he changes his mind and tries to fuck me."
    show haven_blow 2h with dissolve
    pc "*Huk huk*"
    havenvik.name "Ah yeah suck it you bitch!"
    pc "*Huk huk*"
    havenvik.name "Ahhhh. Yes!"
    havenvik.name "Dirty little bitch!"
    havenvik.name "Ah yes yes I can feel it."
    if player.has_perk(perk_preg_want) and havenvik.vsex > 0 and player.check_sex_agree(5):
        show haven_blow wait with dissolve
        pc "Wait, put it in my pussy before you cum!"
        havenvik.name "Ah fuck, c'mere quick."
        hide haven_blow
        show haven_bentover mast happy
        with dissolve
        pc "Quick, before you blow your load."
        $ player.sex_vag(havenvik)
        show haven_bentover inside with hpunch
        pc "Yes!"
        havenvik.name "Ahhhhh!"
        $ player.sex_cum(havenvik, "inside")
        pc "Yes, cum in me!"
        havenvik.name "Haaaa fuck..."
        show haven_bentover smile
        pc "Good, now stay in there. Don't let them escape."
        pc "Mmmm, good."
        havenvik.name "Uffff."
        havenvik.name "Fuck."
        show haven_bentover neutral
        pc "You are getting soft, don't be letting it slide out."
        havenvik.name "Not got much choice darlin, it does what it wants."
        pc "Shame."
        show haven_bentover poke with dissolve
        show haven_bentover noman with dissolve
        pc "Well, suppose that is good enough."
        hide haven_bentover with dissolve
        pc "So..."
        pc "How many was that worth?"
        havenvik.name "I think you need to get your head checked out."
        pc "Maybe. How many?"
        havenvik.name "Look, just take another 10 or something. I don't care. Whatever you want."
        pc "Hmm, was that fucking so good or something?"
        havenvik.name "Honestly, you are a fucking weirdo and I am not sure I wanna deal with you again. But next time you come here my cock will want you and I won't be able to say no."
        havenvik.name "The more bottles I give you, the longer you will stay away. So take as many as you want."
        havenvik.name "Just... Fuck off. Please."
        hide haven_viktor with dissolve
        pc "..."
        pc "Not sure if I should be happy or sad."
        pc "Whatever. Free bottles and I can get someone else to knock me up."
        $ pc_dress()
        pause 0.5
        $ walk(loc_haven_lounge)
        pc "Well, I will help myself I suppose."
        "I help myself to the bottles, not even counting how many I have taken."
        pc "That should last a while."
        $ add_to_list(havenvik.conversation_topics, "free_brew")
        $ inv.take(item_brew, 10)
        $ walk(loc_haven_hallway_2f)
        pcm "Calling me a weirdo..."
        pcm "Whatever."
        $ haven_drink_brew()
        pc "*HACK* *COUGH*"
        pc "*PHEW*"
        pcm "That hit the *COUGH* spot."
        jump travel
    else:
        pc "*Mmmmffff*"
        $ player.sex_cum(havenvik, "mouth")
        havenvik.name "Ahhh yes!"
        havenvik.name "Hahaaaa..."
        havenvik.name "Ah yes you dirty little bitch. Swallow it all up."

        show haven_blow wait ub with dissolve
        pause 0.5
        show haven_blow neutral with dissolve
        pause 0.5
        show haven_blow ah with dissolve
        pc "Pheeeew."
        havenvik.name "Enjoy your free meal?"
        pc "Could have been worse."
        havenvik.name "Mmm."
        hide haven_blow with dissolve
        pc "And now?"
        havenvik.name "Huh?"
        pc "The bottles?"
        havenvik.name "Ah, yeah come and see me after you have cleaned up."
        pc "Ok."
        hide haven_viktor with dissolve
        $ pc_dress()
        pause 0.5
        $ walk(loc_haven_lounge)
        show haven_viktor at right1
        havenvik.name "Here, take an extra one to wash out your mouth with."
        pc "Ohhh how kind of you."
        pc "Idiot."
        havenvik.name "Here, just take em."
        $ inv.take(item_brew, 3)
        pc "Sure."
        hide haven_viktor
        $ walk(loc_haven_hallway_2f)
        if havenvik.vsex == 0:
            pc "Well, got what I wanted again. But next time he will want to fuck me for sure."
        $ haven_drink_brew()
        pc "*PHEW*"
        jump travel

label haven_brewmaster_repeatable_sex_start:
    pcm "*Sigh* Out of brew again..."
    $ player.face_worried()
    pcm "..."
    pcm "Ok, let's get this over with."
    show screen blackout(100) with dissolve
    $ pc_dress()
    $ acc_shower_dress()
    $ acc.makeup_on = True
    $ walk(loc_haven_lounge)
    show haven_viktor at right1
    hide screen blackout with dissolve
    havenvik.name "Sexy little bitch is back. Here for some more?"
    pc "What else would I come here for?"
    $ dialouge = WeightedChoice([
    ("Thought you might come to see your old pal Vik.", 1),
    ("Aw, I feel used. Not even a hello.", 1),
    ("So not come for a chat then?", 1),
    ("To see the sights. Relax next to the fire...", 1),
    ("Another taste of my cock?", If (havenvik.osex > 0,1,0)),
    ("Can't get enough of me fucking you in the store room?", If (havenvik.vsex > 0,1,0)),
    ("Not here to get me to knock you up again?", If (player.has_perk(perk_preg_want) == True and havenvik.vsex > 0,1,0)),
    ])
    havenvik.name "[dialouge]"
    pc "Whatever."
    havenvik.name "Well, lets go."
    pc "..."
    $ walk(loc_haven_storage)
    $ dialouge = WeightedChoice([
    ("Let me see that naked body of yours.", 1),
    ("Mm, take off your clothes.", 1),
    ("Can't wait to see that naked body again.", 1),
    ("Seeing you undress always makes my day", 1),
    ])
    havenvik.name "[dialouge]"
    $ c.top = 0
    pause 0.5
    $ c.bottom = 0
    $ c.pants = 0
    $ dialouge = WeightedChoice([
    ("So fucking sexy.", 1),
    ("Ahhh those tits.", 1),
    ("Mmm, such nice tits.", 1),
    ("Sexy little ass.", 1),
    ("Mmm that lovely tight pussy.", 1),
    ("Still with the plug in your arse I see.", 1),
    ])
    havenvik.name "[dialouge]"
    jump expression WeightedChoice([
    ("haven_brewmaster_repeatable_grope", 1),
    ("haven_brewmaster_repeatable_grope", If (player.has_perk(perk_preg_notwant) == True, 1, 0)), 
    ("haven_brewmaster_repeatable_blow", 1),
    ("haven_brewmaster_repeatable_blow", If (player.has_perk(perk_preg_notwant) == True, 1, 0)), 
    ("haven_brewmaster_repeatable_sex", 1),
    ("haven_brewmaster_repeatable_sex", If (player.has_perk(perk_preg_want) == True, 1, 0)), 
    ])

label haven_brewmaster_repeatable_grope:
    show haven_grope grope hold with dissolve
    $ dialouge = WeightedChoice([
    ("Mmmm, you sexy little bitch.", 1),
    ("Ah what a nice little whore.", 1),
    ("Could play with these sexy tits all day.", 1),
    ("You are turning into one of my favourite sluts in this place.", 1),
    ("No better sight than seeing your tits in front of me.", 1),
    ])
    havenvik.name "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Such a romantic", 1),
    ("Speak to all the girls like that?", 1),
    ("If that is your idea of sweet talking a girl, it's a good job you have jars of brew.", 1),
    ])
    pc "[dialouge]"
    $ dialouge = WeightedChoice([
    ("Better put your hands to use if you want to earn your brew.", 1),
    ("If you want to hurry this up, you better put your hands to work.", 1),
    ("Well, my cock ain't gonna beat it's self off.", 1),
    ("How about wrapping those fingers round my cock?", 1),
    ])
    havenvik.name "[dialouge]"
    pc "..."
    show haven_grope mast penis with dissolve
    $ player.sex_sold(havenvik, 0)
    $ player.sex_hand(havenvik)
    havenvik.name "Nothing better than having you wank me off while I play with these lovely tits. Bet you make good money out of the streets."
    if player.iswhore:
        pc "I get by."
        havenvik.name "I bet you do. If I had a bed, I might even offer you to spend the nights with me."
        pc "Such a shame you don't."
    else:
        pc "I don't sell myself out there."
        havenvik.name "No? Just in here for some booze eh?"
        pc "Something like that."
    havenvik.name "Huuuu."
    show haven_grope happy
    pc "Having fun? Like my fingers round your cock?"
    if player.check_sex_agree(4):
        havenvik.name "Ah yes. Go faster."
        pc "Mmmm, like this?"
        havenvik.name "Ah yeah like that. Ah fuck yes."
        havenvik.name "Haaaa I'm cumming!"
        $ player.sex_cum(havenvik, "stomach")
        hide haven_grope with dissolve
        havenvik.name "Ah yes!"
        pc "Mmmmm."
        havenvik.name "So nice."

        jump haven_brewmaster_repeatable_end
    else:
        havenvik.name "Of course, but would prefer something else round my cock."
        show haven_grope stern
        pc "Like what?"
        hide haven_grope with dissolve
        $ rand_choice = WeightedChoice([
        ("haven_brewmaster_repeatable_blow", 1),
        ("haven_brewmaster_repeatable_blow", If (player.has_perk(perk_preg_notwant) == True, 1, 0)), 
        ("haven_brewmaster_repeatable_sex", 1),
        ("haven_brewmaster_repeatable_sex", If (player.has_perk(perk_preg_want) == True, 1, 0)), 
        ])
        jump expression rand_choice

label haven_brewmaster_repeatable_blow:
    havenvik.name "Get on your knees and let's see those lips sucking me."
    pc "..."
    $ player.sex_oral(havenvik)
    show haven_blow wait with dissolve
    havenvik.name "A whore on her knees. Just where she belongs."
    pc "Thanks..."
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show haven_blow cum with dissolve
        show haven_blow 2h with dissolve
    elif randomnum == 2:
        show haven_blow cum with dissolve
        show haven_blow 1h with dissolve
    else:
        show haven_blow ballsuck with dissolve
    havenvik.name "Ah fuck yes, you little cocksucking slut."
    if player.desire > 80:
        pc "Mmmmmm."
    havenvik.name "Bet you love having a cock in your mouth even if your are whoring for it."
    if player.desire > 80:
        pc "♥"
    havenvik.name "Still got that plug in your arse?"
    show haven_blow wait with dissolve
    pc "Of course, I'm a dirty whore remember."
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show haven_blow cum with dissolve
        show haven_blow 2h with dissolve
    elif randomnum == 2:
        show haven_blow cum with dissolve
        show haven_blow 1h with dissolve
    else:
        show haven_blow ballsuck with dissolve
    if player.check_sex_agree(4, notif=False):
        havenvik.name "Haaaa. A whore that is perfect at sucking cock."
        pc "*Hyuk*"
        havenvik.name "Ah yes come here. Take it."
        show haven_blow cum with dissolve
        havenvik.name "Fuck yes!"
        $ player.sex_cum(havenvik, "mouth")
        havenvik.name "Ahhh yes yeeeeessss."
        havenvik.name "Take it in your mouth you whore!"
        havenvik.name "Ahhhhhh..."
        show haven_blow wait ub with dissolve
        show haven_blow neutral with dissolve
        havenvik.name "That's right. Swallow it all down. Bet you love it don't you?"
        pc "What else am I going to do with it?"
        havenvik.name "Mmmm, good girl."
        hide haven_blow with dissolve
        jump haven_brewmaster_repeatable_end
    else:
        havenvik.name "Damn right you are. Perfect at sucking a cock."
        havenvik.name "But a good little whore bends over and gets a good fucking as well."
        show haven_blow wait with dissolve
        pcm "Shit."
        havenvik.name "Over there."
        hide haven_blow with dissolve
        jump haven_brewmaster_repeatable_sex

label haven_brewmaster_repeatable_sex:
    havenvik.name "Turn around, I want to fuck your nice little pussy."
    pc "..."
    show haven_presentass mast with dissolve
    havenvik.name "Good girl. Sexy and obedient."
    pc "Gonna give me some jars if I tell you to go fuck yourself?"
    havenvik.name "Heh."
    havenvik.name "No such luck, will be you getting fucked."
    pc "Looks that way..."
    show haven_presentass poke with dissolve
    $ player.sex_vag(havenvik)
    show haven_presentass inside lookdown with dissolve
    havenvik.name "Ahhh yes, fucking hell so nice."
    havenvik.name "I'm gonna fuck you and make you beg for more."
    pcm "Doubt that, I am just here for the booze."
    havenvik.name "Ah yes you little slut."
    if player.desire >= 90:
        pcm "Although the fucking is not too bad. Might actually enjoy it if I wasn't selling myself to him."
    havenvik.name "Take it! Take it!"
    havenvik.name "Oh yes! I'm cumming!"
    pc "Ah!"
    $ player.sex_cum_location_offer(
    difficulty=1, 
    cum_want="haven_brewmaster_repeatable_sex_cum_inside", 
    cum_notwant="haven_brewmaster_repeatable_sex_cum_inside", 
    cum_pullout="haven_brewmaster_repeatable_sex_cum_pullout",
    cum_pullout_bj="haven_brewmaster_repeatable_sex_cum_bj",  
    cum_pullout_poke="haven_brewmaster_repeatable_sex_cum_poke",
    cum_bj="haven_brewmaster_repeatable_sex_cum_bj",    
    
    block_anal_check=True
    )

label haven_brewmaster_repeatable_sex_cum_pullout:
    show haven_presentass mast lookback with dissolve
    havenvik.name "Ah fuck yes."
    $ player.sex_cum(havenvik, "pullout")
    havenvik.name "Ahhh yes. Fuck. Take it all over you."
    pc "Mmmm, give it to me."
    havenvik.name "Ahhhhh."
    pc "Mmmm so warm."
    havenvik.name "Wheeewww."
    havenvik.name "Lovely little whore."
    hide haven_bentover with dissolve
    jump haven_brewmaster_repeatable_end

label haven_brewmaster_repeatable_sex_cum_poke:
    show haven_presentass poke lookback with dissolve
    havenvik.name "Ah fuck yes."
    $ player.sex_cum(havenvik, "inside")
    havenvik.name "Ahhh yes. Fuck. Take it all over you."
    pc "Mmmm, give it to me."
    havenvik.name "Ahhhhh."
    pc "Mmmm so warm."
    havenvik.name "Wheeewww."
    havenvik.name "Lovely little whore."
    hide haven_presentass with dissolve
    jump haven_brewmaster_repeatable_end


label haven_brewmaster_repeatable_sex_cum_inside:
    havenvik.name "Ah fuck yes."
    $ player.sex_cum(havenvik, "inside")
    havenvik.name "Ahhh yes. Fuck. Take it in you."
    pc "Mmmm, give it to me."
    if not player.has_perk(perk_preg_want):
        pcm "Fuck!"
    havenvik.name "Ahhhhh."
    pc "Mmmm so nice."
    havenvik.name "Wheeewww."
    show haven_presentass mast with dissolve
    havenvik.name "Lovely little whore."
    hide haven_presentass with dissolve
    jump haven_brewmaster_repeatable_end

label haven_brewmaster_repeatable_sex_cum_bj:
    hide haven_presentass with dissolve
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        show haven_blow cum with dissolve
        show haven_blow 2h with dissolve
    elif randomnum == 2:
        show haven_blow cum with dissolve
        show haven_blow 1h with dissolve
    else:
        show haven_blow ballsuck with dissolve
    havenvik.name "Haaaa. A whore that is perfect at sucking cock."
    pc "*Hyuk*"
    havenvik.name "Ah yes come here. Take it."
    show haven_blow cum with dissolve
    havenvik.name "Fuck yes!"
    $ player.sex_cum(havenvik, "mouth")
    havenvik.name "Ahhh yes yeeeeessss."
    havenvik.name "Take it in your mouth you whore!"
    havenvik.name "Ahhhhhh..."
    show haven_blow wait ub with dissolve
    show haven_blow neutral with dissolve
    havenvik.name "That's right. Swallow it all down. Bet you love it don't you?"
    pc "What else am I going to do with it?"
    havenvik.name "Mmmm, good girl."
    hide haven_blow with dissolve
    jump haven_brewmaster_repeatable_end

label haven_brewmaster_repeatable_end:
    pc "Ok, had your fun?"
    havenvik.name "Damn right. I'll meet you outside when you have dressed."
    hide haven_viktor with dissolve
    pc "Mmm."
    pause 0.5
    $ pc_dress()
    show haven_viktor at right1
    $ walk(loc_haven_lounge)
    pause 0.5
    $ inv.take(item_brew, 4)
    havenvik.name "Here you go, look forward to seeing you again."
    pc "..."
    pc "Sure."
    pause 0.5

    hide haven_viktor
    $ walk(loc_haven_hallway_2f)
    $ haven_drink_brew()
    pc "*HACK* *COUGH*"
    pc "*PHEW*"
    pcm "That hit the *COUGH* spot."
    jump travel

label haven_brewmaster_0:
label haven_brewmaster_ask:
    $ havenvik.dict["brew_stage"] += 1
    pcm "Fuck, I feel like complete shit and can't be heading off to the pub or anything right now."
    pcm "Well, the people round here must have something to numb the pain."
    if loc_cur == loc_haven_shower_stall:
        call haven_shower_dress_call from _call_haven_shower_dress_call_4
        $ walk(loc_haven_hallway_1f)
    pc "Hey, where can I get a pick me up around here?"
    show havenman at right1 with dissolve
    hav "Viktor. He sells homebrew on the cheap."
    pc "Thanks, where is he?"
    hav "Next ta the firepits in the lounge."
    pc "Cheers."
    hide havenman with dissolve
    if havenvik.has_met:
        pcm "I wonder if it's the same [havenvik.name] I met in the slums?"
    else:
        pcm "Ok, let's see what this Viktor is all about."
    show screen blackout() with Dissolve(0.3)
    $ walk(loc_haven_lounge)
    hide screen blackout with Dissolve(0.3)
    if havenvik.has_met:
        pcm "Yup, is the same guy..."
        show haven_viktor at right1 with dissolve
        pc "Hey, [havenvik.name]. Looking for a pick me up."
    else:
        pcm "Hmm, that's probably him over there sitting on a crate full of bottles."
        show haven_viktor at right1 with dissolve
        pc "Hey, I'm looking for Viktor."
    havenvik.name "I'm ya man, 'ow many ya want?"
    pc "What will it cost me?"
    havenvik.name "Sweet thing like you? £5 a jar or we can talk 'bout a service."
    pcm "Well I don't have any money on me, so that's not an option."
    pc "Service?"
    havenvik.name "Ya, doesn't look like you're broken in too much so I'm willing to have yer body as payment."
    if player.has_perk([perk_slut, perk_whore, perk_sucu]):
        pc "Specifics. What for how much?"
    else:
        pcm "Fuck!"
    havenvik.name "Tell ya what. Since you're new 'round ere, flash them tits and I'll part with a couple o bottles. We can negotiate next time."
    if player.has_perk([perk_slut, perk_whore, perk_sucu]):
        pc "Sure. Sounds good."
    else:
        pcm "Fuck, well at least it's not a high price."
        pcm "If things carry on like this I will jump out a window before I manage to find out where [ant.name] is."
        pc "Err, ok..."
    havenvik.name "Nice, get 'em out."
    $ c.top = 0
    if bruise.belly:
        havenvik.name "Mmmm, nice and ripe. Not like the usual hags round 'ere. Though looks like your last punter got a bit heavy on you."
    else:
        havenvik.name "Mmmm, nice and ripe. Not like the usual hags round 'ere"
    havenvik.name "Big for a girl as skinny as you. Next time I might have to 'ave a go at 'em. Get my teeth inta those rings you got there."
    havenvik.name "'Ere, as promised."
    $ inv.take(item_brew, 2)
    $ player.mouth = 1
    pc "Thanks."
    $ pc_dress()
    havenvik.name "Be seein' ya."
    $ player.face_normal()
    hide haven_viktor with dissolve
    pc "Right, time to check these out."
    show screen blackout() with Dissolve(0.3)
    $ walk(loc_haven_bed)
    hide screen blackout with Dissolve(0.3)
    pcm "Ugh, the smell alone is enough to make your hair stand on end."
    pcm "Ok... Hup."
    $ haven_drink_brew()
    pc "*HACK* *COUGH*"
    pc "*PHEW*"
    pcm "Shit, this stuff is pretty much a chemical weapon."
    pcm "*Phew*"
    pcm "Better go easy on these or else I will be seeing pink elephants in no time."
    jump travel

label haven_brewmaster_free_brew:
    pcm "..."
    pcm "I really want something more to drink, but I have ran out."
    $ player.face_worried()
    pcm "Looks like I'll have to pay [vic] another visit."
    show screen blackout(100) with dissolve
    $ walk(loc_haven_lounge)
    hide screen blackout with dissolve
    pc "Hi [havenvik.name]..."
    "Once he notices me, he just looks away and ignores me."
    pcm "Ok. I'll help myself then."
    "[vic] can't resist sneaking a glance and I give him a wink."
    pc "Thanks ♥"
    $ inv.take(item_brew, 10)
    $ walk(loc_haven_hallway_2f)
    pcm "Well, got what I wanted at least..."
    pcm "Hup."
    $ haven_drink_brew()
    pc "*HACK* *COUGH*"
    pc "*PHEW*"
    pcm "That hit the *COUGH* spot."
    jump travel

label haven_brewmaster_drink_lowmood:
    $ show_notif_popup("Mood too low")
    jump haven_brewmaster_drink

label haven_brewmaster_drink:
    if player.has_perk([perk_drinking_wine_4, perk_drinking_wine_3, perk_drinking_wine_2, perk_drinking_wine_1]):
        pcm "I should finish the bottle of wine first."
        jump travel
    elif player.has_perk([perk_drinking_beerbottle_2, perk_drinking_beerbottle_1]):
        pcm "I'm already drinking a beer."
        jump travel
    elif player.has_perk([perk_drinking_brew_2, perk_drinking_brew_1]):
        pcm "I am already drinking a brew."
        jump travel

    pcm "Hmmm, how about a little snifter"
    if inv.qty(item_brew) == 1:
        pcm "Last one, hope I can get my hands on some more."
    $ inv.drop(item_brew)
    $ player.add_perk(perk_drinking_brew_1, mins=10)
    $ player.drink(amount=40, spiked=True)
    pc "*HACK* *COUGH*"
    pc "*PHEW*"
    pcm "That hit the *COUGH* spot."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
