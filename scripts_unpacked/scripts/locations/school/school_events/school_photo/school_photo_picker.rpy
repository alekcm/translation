label school_photo_quest_picker:
    if log.interactive("photo_intro_01"):
        jump school_photo_intro_first_talk
    elif log.interactive("photo_intro_02"):
        jump school_photo_intro_first_shoot_ask
    elif log.interactive("photo_intro_03"):
        jump school_photo_quest_picker_return_later
    elif log.interactive("photo_intro_04"):
        jump school_photo_intro_second_shoot
    elif log.interactive("photo_intro_05"):
        jump school_photo_quest_picker_return_later
    elif log.interactive("photo_intro_06"):
        jump school_photo_intro_post_second
    elif log.interactive("photo_intro_07"):
        jump school_photo_quest_picker_investigating
    elif log.interactive("photo_intro_08"):
        jump school_photo_intro_post_investigate
    elif log.completed("Promotional material") and not quest_photo.active:
        jump school_photo_quest_picker_lamenting
    elif log.interactive("photo_01"):
        jump school_photo_intro_quest_give
    elif not log.interactive("photo_03"):
        jump school_photo_intro_quest_camera_shop
    else:
        $ walk(loc_school_darkroom)
        jump travel

label school_photo_work_picker:
    show felix at right1 with dissolve
    if log.completed("photo_02"):
        pc "Got any more work for me to do?"
        felix.name "Still dealing with the last lot [name]."
        pc "Right."
        hide felix with dissolve
        jump travel
    elif not log.completed("Starting the magazine"):
        jump quest_photo_startingout_picker
    elif not log.completed("Dancing starlet"):
        jump quest_photo_dancestarlet_start
    "*NOTE* I am still writing this. But the next quest will be doing poses in your dance gear and maybe getting Dani to pose with you"
    jump travel


label school_photo_quest_picker_return_later:
    show felix at right1
    $ walk(loc_school_darkroom)
    felix.name "Hey [name]. I am working on the last set we did. Come back in a couple of days if you want to have another session."
    pc "Ok."
    hide felix
    $ walk(loc_school_hallway_2f)
    jump travel

label school_photo_quest_picker_investigating:
    show felix at right1
    $ walk(loc_school_darkroom)
    felix.name "Hey [name]. I am still looking into things. Comeback in a few days and I might have more info."
    pc "Ok."
    hide felix
    $ walk(loc_school_hallway_2f)
    jump travel

label school_photo_quest_picker_lamenting:
    pcm "I should probably leave him alone in his misery for now. "
    jump travel


label school_photo_quest_photoshoot_picker:
    if school_photo_shoots_done == 0:
        if not player.check_sex_agree(3, exhibitionist=True):
            pcm "Don't think I am up for having my arse plastered all over the magazine he is planning..."
            jump travel
        else:
            jump school_photo_quest_photoshoot_first
    elif not school_photo_special_request and school_photo_shoots_done > 3 and player.check_sex_agree(5):
        jump school_photo_quest_photoshoot_special_request
    $ walk(loc_school_darkroom)
    show felix at right1
    felix.name "Hey [name]. What can I do for you?"

label school_photo_quest_photoshoot_picker_menu:
    if not school_photo_special_request:
        jump school_photo_quest_photoshoot_standard
    else:
        jump school_photo_quest_photoshoot_type

label school_photo_quest_photoshoot_type:
    menu:
        "Standard photoshoot":
            jump school_photo_quest_photoshoot_standard
        "See special requests":
            jump school_photo_quest_photoshoot_special
        "Nothing for now":
            felix.name "Well, you know where I am if you want to do something."
            hide felix
            $ walk(loc_school_hallway)
            jump travel

label school_photo_quest_photoshoot_standard:
    "**NOTE** As of 3.0, this quest is disabled as it is planned to be restructured."
    "Previously it was treated like a job. Turn up, do a shoot, get paid and go home."
    "I plan to instead make it a proper story focused quest instead. Involving other characters."
    "So for now this is as far as the story goes. Check back later for updates."
    hide felix
    $ walk(loc_school_hallway_2f)
    jump travel
    "**NOTE** These are NOT written yet but just an example and teaser of the images."
    menu:
        "Halloween Witch":
            jump school_photo_quest_photoshoot_witch
        "Halloween Catgirl":
            jump school_photo_quest_photoshoot_catgirl
        "Sexy dancing":
            jump school_photo_quest_photoshoot_dance
        "Christmas Miss Santa":
            jump school_photo_quest_photoshoot_santa
        "Christmas helper Elf":
            jump school_photo_quest_photoshoot_elf
        "Nothing for now":
            felix.name "Well, you know where I am if you want to do something."
            $ walk(loc_school_hallway)
            jump travel

label school_photo_quest_photoshoot_special:
    menu:
        "Christmas \"special\" shoot" if "santa" in school_photo_quest.list and "elf" in school_photo_quest.list:
            jump school_photo_quest_photoshoot_santa_special_picker
        "Teaser shoots":

            jump school_photo_quest_photoshoot_teaser
        "Nothing for now":

            felix.name "Well, you know where I am if you want to do something."
            $ walk(loc_school_hallway)
            jump travel

label school_photo_quest_photoshoot_teaser:
    menu:
        "Assplay shoot":
            jump school_photo_quest_photoshoot_assplay_1
        "Bukake shoot":
            jump school_photo_quest_photoshoot_bukake
        "Virgin shoot":
            jump school_photo_quest_photoshoot_virgin
        "Pregnant shoot":
            jump school_photo_quest_photoshoot_preg

label school_photo_quest_photoshoot_warning_done:


    return
label school_photo_quest_photoshoot_warning_tasteful:
    felix.name "This one is a nude one you know?"
    pc "Err."
    felix.name "I just point it out since you haven't done anything nude before."
    felix.name "While nothing \"important\" will be on display, it will still be quite suggestive."
    felix.name "You okay with that?"
    menu:
        "That's fine":
            return
        "Err, actually no":
            pc "Hmm, actually I don't think I am ready for something like that."
            felix.name "Ok, so anything else?"
            jump school_photo_quest_photoshoot_picker_menu

label school_photo_quest_photoshoot_warning_topless:
    if any("tasteful" in string for string in school_photo_quest.list):
        felix.name "I know you have went nude before, but this one shows off a bit more than the other ones."
    else:
        felix.name "This shoot shows off a bit more than you might be comfortable with"
    pc "Err, such as?"
    felix.name "This one has your breasts in full view. Although not between your legs. You okay with that?"
    menu:
        "That's fine":
            return
        "Err, actually no":
            pc "Hmm, actually I don't think I am ready for something like that."
            felix.name "Ok, so anything else?"
            jump school_photo_quest_photoshoot_picker_menu

label school_photo_quest_photoshoot_warning_nude:
    felix.name "This one will capture you in your full birthday suit. You haven't done anything that displays your whole body so thought I would let you know."
    menu:
        "That's fine":
            return
        "Err, actually no":
            pc "Hmm, actually I don't think I am ready for something like that."
            felix.name "Ok, so anything else?"
            jump school_photo_quest_photoshoot_picker_menu

label school_photo_quest_photoshoot_warning_errotic:
    felix.name "This shoot is pure sexual just to let you know. There will be nothing left to the imagination."
    felix.name "You haven't done such a shoot before so if you are having second thoughts, then now's the time to say so."
    menu:
        "That's fine":
            return
        "Err, actually no":
            pc "Hmm, actually I don't think I am ready for something like that."
            felix.name "Ok, so anything else?"
            jump school_photo_quest_photoshoot_picker_menu

label school_photo_quest_photoshoot_warning_asex:
label school_photo_quest_photoshoot_warning_vsex:
    felix.name "You haven't had sex on camera before. You sure you are up for it?"
    menu:
        "That's fine":
            return
        "Err, actually no":
            pc "Hmm, actually I don't think I am ready for something like that."
            felix.name "Ok, so anything else?"
            jump school_photo_quest_photoshoot_picker_menu

label school_photo_quest_photoshoot_first:
    pcm "Guess I'll go see what [felix.name] has in mind."
    if player.check_poor():
        $ randomnum = round_num(player.cash, 10)
        pcm "I could do with the money anyway. I have about £[randomnum] and it won't last very long..."
    $ walk(loc_school_darkroom)
    $ school_photo_shoots_done += 1
    show felix at right1
    with dissolve
    felix.name "Hey [name]. Come in."
    pc "Hey, how goes it?"
    felix.name "Well, I have been speaking to the needle girls and getting some hand me downs I think we can make use of."
    felix.name "So, you are here. Am I to assume you have decided you are up for the photo shoots?"
    if player.isbroken:
        pc "Done worse, so what's the harm."
    elif player.isslut:
        pc "Sure, I don't have much issue showing off."
    elif player.iswhore:
        pc "Been paid to do worse, so sure."
    else:
        pc "*Sigh* Sure, I'm willing to give it a go."
    felix.name "Great. That's wonderful news."
    if not saskia.has_met:
        pc "So \"hand me downs\"? And who are the needle girls?"
        felix.name "They are a few girls who repair old clothes, shoes, bedding and whatever has to do with fabric. They take old stuff, repair it and sell it on."
    else:
        pc "And \"hand me downs\" from those girls? I dread to think what it might be."

    felix.name "Got my hands on some stuff that no sane person would wear normally but is perfect for us to make use of."
    pc "\"No sane person\" yet you are expecting me to wear it?"
    felix.name "Ah for the photos it's great stuff. Things like this... err... bikini thing? Whatever it is."
    pc "Ah, a cat girl outfit. Think we can get away with that?"
    felix.name "It's perfect since it's a holiday season thing. We look like we are promoting the holidays but of course, well..."
    pc "Promoting my arse?"
    felix.name "Wouldn't put it that way myself, but sure."
    felix.name "Anyway, it's good news you are in. I pretty much have everything set up so whenever you want a shoot then come and see me."
    pc "Ok. I'll come over when I have time."
    felix.name "Sure."
    hide felix
    $ walk(loc_school_hallway_2f)
    pcm "Ok... So everything is ready. Should I really go through with this?"
    jump travel

label school_photo_quest_photoshoot_special_request:
    $ school_photo_special_request = True
    show felix at right1
    felix.name "Hey [name]."
    pc "Hey, all good?"
    felix.name "Yeah, but you still might want to sit for this."
    pc "Ok..."
    felix.name "So, the mag is doing well. Making a tidy profit and managing to make it all worthwhile."
    pc "I gathered that since you keep paying for more photos. So what's the problem."
    felix.name "No problem, we are still good on that front."
    felix.name "But..."
    pc "Yeeeesss...?"
    felix.name "Well, I have been getting requests."
    pc "Ok. And?"
    felix.name "Requests for things involving you."
    pc "Right, not a shock seeing as I am the model. So why are you acting all coy?"
    felix.name "It's the nature of the requests."
    pc "Well, I think I can imagine. Show boobs! Or some such anyway."
    felix.name "Well, yes. But those are the more normal ones."
    pc "Oh?"
    felix.name "Mmm."
    pc "Just spit it out."
    felix.name "Right, okay then..."
    felix.name "Let's see..."
    felix.name "A photo of your arsehole... Photo of your arse with a plug in it... Photo of your arse with your fingers in it... Photo of your arse with a cock in..."
    pc "I get the picture."
    felix.name "I am guessing these are all from the same person."
    pc "Mmm."
    felix.name "Someone asking if you are a virgin and if not, they will pay. Though they didn't specify for what."
    if player.pregnancy >= 2 or player.preg_knows:
        pc "Well, I doubt I can pull off being a virgin while pregnant."
        felix.name "Mmm."
    elif player.isbroken:
        pc "Pfft yeah right."
    elif player.pregbabies:
        pc "Well, I might have lost weight since then but I am a mother. Doubt I am pulling off the virgin routine."
        felix.name "Mmm."
    elif player.iswhore or player.isslut:
        pc "Yeah, pretty far from being a virgin so doubt I can pull that off."
        felix.name "Mmm."
    elif player.vsex >= 5:
        pc "No, not a virgin and doubt I can pull off a lie."
        felix.name "Mmm."
    elif player.vsex:
        pc "I am about as virgin as someone round here gets. Could probably just say yes and see what he wants."
        felix.name "You sure?"
        pc "No harm in checking it out."
        felix.name "Ok."
    else:
        pc "Hmmm..."
        pc "I suppose you can tell him yes..."
        felix.name "Oh? Okay then."
    if player.pregnancy >= 2:
        felix.name "People willing to pay for pregnant photos."
    else:
        felix.name "If you ever find yourself knocked up, people are willing to pay for photos of you with a big belly."
    felix.name "Other requests of you wearing specific clothes, no clothes or various objects inserted into you..."
    pc "Ok, I understand..."
    pc "Why are you telling me this?"
    felix.name "Because they are offering huge sums of money. If you are willing to fulfil the requests we stand to make a fair bit of cash."
    felix.name "Entirely up to you of course. But if you are willing to go through with it, I will take the photos with no judgement and do all the legwork."
    pc "And take a cut I assume?"
    felix.name "Of course."
    pc "Mmm, well, I will keep it in mind."
    felix.name "Great."
    hide felix
    $ walk(loc_school_hallway)
    pcm "..."
    pcm "Should have expected this."
    pcm "Oh well."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
