init python:
    def motel_book_blue_room(men_amount=0, charge=True):
        if charge:
            player.spend(30)
        loc_motel_room.locked = False
        loc_motel_room.dict["time"] = t.hours_total
        loc_motel_room.dict["men_amount"] = men_amount

label motel_receptionist_talk:
    if log.interactive("quest_homeless_start_01") or log.interactive("quest_homeless_start_02"):

        if log.interactive("quest_homeless_start_01"):
            pcm "I doubt [emile.name] got herself a motel room with no money. I should look elsewhere."
        else:
            pcm "I don't have money to rent a room. I should look elsewhere."
        jump travel

    if not motel_recep_here():
        pc "Hello!"
        if motel_recep_here(loc_motel_room2):
            pc "..."
            distvoice "Hold on..."
            pc "... ..."

    show motel_recep at right1 with dissolve
    if not motel_recep.has_met:
        jump motel_receptionist_talk_first
    elif not "pink_room_asked" in loc_motel_lobby.list:
        jump motel_receptionist_talk_pinkroom
    motel_recep.name "Pink room?"
    menu:
        "A pink room" if quest_whore.active:
            $ loc_motel_pinkroom.locked=False
            motel_recep.name "Come speak to me when you are done for your pay."
            pc "Thanks."
            if not shop_motel.open:
                motel_recep.name "Got some stuff to sell if you want."
                pc "To sell?"
                motel_recep.name "Yeah."
                $ shop_motel.open = True
                call screen inventory_itemshop_screen(shop_motel, discount = -50, show_locked=True)  
                pc "These prices are through the roof."
                motel_recep.name "Of course they are. Whores and truckers will pay it."
                pc "Right..."
            hide motel_recep with dissolve
            $ walk(loc_motel)
            $ walk(loc_motel_pinkroom)
            if not "first_time" in loc_motel_pinkroom.list:
                jump pinkroom_first_time
            jump travel
        "A blue room" if player.cash >= 30:
            $ motel_book_blue_room()
            motel_recep.name "You have 24 hours, if you want more you pay for more."
            pc "Thanks."
            hide motel_recep with dissolve
            jump travel

        "Cash in pink tickets" if inv.qty(item_pinkticket):
            jump motel_receptionist_talk_sell_tickets
        "Actually, never mind":
            motel_recep.name "Don't waste my time."
            hide motel_recep with dissolve
            jump travel

label motel_receptionist_talk_shop:
    pc "Can I see what you are selling?"
    show motel_recep at right1 with dissolve
    motel_recep.name "Sure."
    call screen inventory_itemshop_screen(shop_motel, discount = -50, show_locked=True)  
    pc "Thanks."
    hide motel_recep with dissolve
    jump travel

label motel_receptionist_talk_sell_tickets:
    motel_recep.name "Sure... Here you go."
    $ player.add_money(item_pinkticket.value * inv.qty(item_pinkticket))
    $ inv.drop(item_pinkticket, inv.qty(item_pinkticket))
    pc "Thanks."
    hide motel_recep with dissolve
    jump travel

label motel_receptionist_talk_first:
    motel_recep.name "Pink room?"
    pc "Huh?"
    motel_recep.name "You want a pink room I take it?"
    pc "Err, no idea what you mean. I was wondering if you needed cleaners?"
    show motel_recep worried
    if c.slutty:
        motel_recep.name "Cleaner? What's a whore want cleaning work for?"
        if player.has_perk(perk_whore):
            $ player.face_worried()
            pc "To make some money without taking a dick in me maybe?"
            motel_recep.name "Whatever. Yeah looking for cleaners."
            motel_recep.name "Between you whores fucking here and the truckers stinking the place up, always need someone to clean up."
            pc "Right... So what do I do?"
            motel_recep.name "Come when you want, dress in the whore cleaners getup and show your arse off more than you clean."
            pc "What?"
            motel_recep.name "Boss wants cleaning girls to wear some stupid maid dress to get the perverts horny."
            motel_recep.name "So flash your arse more than you clean and don't get upset if someone sticks their dick in you at the same time."
            $ player.face_annoyed()
            motel_recep.name "You're clearly used to dicks in you though so shouldn't worry you."
            pc "Ok, so care to explain again without being a cunt?"
            motel_recep.name "Go in back, whore up and clean you dumb fuck. Or piss off, I don't care."
            hide motel_recep with dissolve
            pcm "Right..."
            $ walk(loc_motel)
            pcm "So ignoring the bitch attitude, I can just come when I want and clean up."
            pcm "Sounds like it might be a bit of trouble though."
        else:
            $ player.face_worried()
            pc "I'm not a whore."
            motel_recep.name "You look like one."
            pc "And yet I am not."
            motel_recep.name "..."
            pc "So... Cleaners?"
            motel_recep.name "Yeah, Between the whores fucking here and the truckers stinking the place up, always need someone to clean up."
            pc "So how do I go about it?"
            motel_recep.name "Got a uniform in back you gotta wear that makes you look just as much a whore as you do now."
            motel_recep.name "Bend over, flash your arse and do some cleaning. Get fucked by some pervert now and then."
            pc "Okay, and now a proper answer?"
            motel_recep.name "That was a proper answer. You see what this place is. Clean up in some dumb maid dress the boss insists the cleaners wear and watch your arse."
            motel_recep.name "Means some drunk trucker who cant wait 20 steps to find a whore will try and put his thing in you though."
            motel_recep.name "No complaining to me when you are dragged to the dumpsters and passed around."
            pc "Really selling the job aren't you?"
            motel_recep.name "It's how it is. Don't want some innocent girl walk into this shithole, get arse raped and go off crying."
            pc "Yeah, just leave it to me to get arse raped."
            motel_recep.name "How you're dressed, you don't need any more help so go for it."
            pc "Right. Thanks."
            hide motel_recep with dissolve
            $ walk(loc_motel)
            pcm "So I can just come when I want and clean up."
            pcm "Sounds like it might be a bit of trouble though."
    else:

        motel_recep.name "Ah! Cleaner? Yeah always need some of those."
        pc "So, I can work here?"
        motel_recep.name "You can. Doubt you want to though."
        pc "Why not?"
        motel_recep.name "Boss makes the cleaners wear this whore like maid outfit to clean up."
        $ player.face_worried()
        pc "Err, okay? Most places round here make us dress like whores for work. Whats the difference?"
        motel_recep.name "All these horny and drunk truckers who will try and fuck you as soon as you enter their room to clean."
        motel_recep.name "Or just drag you round the bins and pass you round like a whore."
        pc "Err... Really?"
        motel_recep.name "Yeah..."
        pc "Then why not get the whores to clean up here?"
        motel_recep.name "Don't pay enough for them. So we end up with idiots like us doing it until we end up beaten and ass raped."
        pc "..."
        motel_recep.name "Job's yours if you want. No one else wants it. But I gave you fair warning and suggest you look elsewhere for money."
        pc "Right... Thanks."
        motel_recep.name "Hope I don't see you again."
        hide motel_recep with dissolve
        $ walk(loc_motel)
        pcm "So I can just come when I want and clean up. Sounds like I will be getting myself in trouble if I do though..."
    $ add_to_list(loc_motel_lobby.list, "cleaner_unlocked")
    if not quest_cleaner.active:
        $ log.assign("Cleaner")
    jump travel

label motel_cleaner_first:
    $ add_to_list(loc_motel_lobby.list, "cleaned_first")
    pcm "So have to wear some whore like maid outfit..."
    if wardrobe.qty(item_outfit_20):
        pcm "Already have something similar but I guess I should go and check."
    $ walk(loc_motel_lobby)
    pc "So, this maid dress I am supposed to wear?"
    show motel_recep at right1 with dissolve
    motel_recep.name "Your funeral..."
    $ shop_motel.open = True
    call screen inventory_itemshop_screen(shop_motel, discount = -50, show_locked=True)  
    pc "These prices are through the roof."
    motel_recep.name "Of course they are. Whores and truckers will pay it."
    pc "And why is the dress so expensive?"
    motel_recep.name "Whores buy it to wear for the person fucking them."
    pc "..."
    pc "Thanks..."

    if wardrobe.qty(item_outfit_20):
        motel_recep.name "Change in the room through there."
        hide motel_recep with dissolve
        jump action_clean_start
    else:
        hide motel_recep with dissolve
        $ walk(loc_motel)
        pcm "That dress costs a fortune. Is it even worth it for cleaning?"
        jump travel

label action_clean_event_motel_flyeroffer:
    $ show_cleaning_image()
    "[rlist.clean_area_dialogue]"
    $ add_to_list(quest_flyers.list, "motel_offer")
    motel_recep.name "Next time come and speak to me about flyering. Avoid you getting ass raped by these perverts."
    if quest_flyers.active:
        pc "Okay."
    else:
        $ renpy.scene()
        show motel_recep at right1
        with dissolve
        pc "Flyering?"
        motel_recep.name "Walk around the area with bits of paper showing our prices and services."
        pc "Ah, right. Okay."
        $ log.assign("Flyering")
        $ diary_jobs_flyers_func("motel")
        hide motel_recep with dissolve
    jump action_clean_event_picker

label motel_receptionist_talk_flyerstart:
    show motel_recep at right1 with dissolve
    pc "Err, so this flyer stuff?"
    motel_recep.name "Take these, head around the area and hand them out. Simple."
    pc "Right, okay."
    hide motel_recep with dissolve
    return

label motel_receptionist_talk_pinkroom:
    $ add_to_list(loc_motel_lobby.list, "pink_room_asked")
    motel_recep.name "Pink room?"
    pc "A pink room?"
    motel_recep.name "Whores go in the pink room."
    pc "And if I'm not a whore?"
    motel_recep.name "Then pay for a blue room."
    pc "Okay..."
    pc "Whats the deal with pink rooms?"
    motel_recep.name "Pink rooms are free. You go in and get ready, perverts come in and fuck you. They pay here fixed price for half an hour."
    motel_recep.name "When you're done, come and collect your cut."
    pc "Right..."
    motel_recep.name "So..."
    jump motel_receptionist_talk

label motel_room_kickedout:
    "*KNOCK* *KNOCK*"
    motel_recep.name "Times up! Time to leave!"
    pc "Right, okay."
    $ walk(loc_motel)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
