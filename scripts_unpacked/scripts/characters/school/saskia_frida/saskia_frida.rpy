init python:
    def needle_girls_new_outfits_check():
        if not "times_unlocked_costume" in shop_needle.dict:
            shop_needle.dict["times_unlocked_costume"] = 1
        
        outfit_sets = ["casino", "santa", "jester", "maid"]
        outfit_sets_can_unlock = []
        
        outfit_has_more = shop_needle.dict["times_unlocked_costume"] <= len(outfit_sets) 
        outfit_can_unlock = shop_needle.value_junk() > (shop_needle.dict["times_unlocked_costume"] * 30)
        
        if outfit_can_unlock and outfit_has_more: 
            for i in outfit_sets:
                if not i in shop_needle.list:
                    add_to_list(outfit_sets_can_unlock, i)
            if outfit_sets_can_unlock:
                shop_needle.dict["times_unlocked_costume"] += 1
                renpy.jump("neddle_girls_shop_unlock_" + random(outfit_sets_can_unlock))


label saskia_frida_talk_picker:
    if not shop_needle.open:
        jump saskia_frida_intro_again
    if saskia_here() and frida_here():
        jump expression WeightedChoice([
        ("saskia_frida_talk_subject", 100),
        ("saskia_talk_subject", 70),
        ("frida_talk_subject", 70),
        ])
    elif saskia_here():
        jump saskia_talk_subject
    else:
        jump frida_talk_subject

label saskia_frida_intro_again:
    $ shop_needle.open = True
    if all([saskia_here(), frida_here()]):
        show frida at right1 with dissolve
        pc "Err, so. What is it you actually do here?"
        frida.name "Told you didn't we?"
        pc "Not really."
        frida.name "[saskia.nname]! What we do here?"
        show saskia at right2 with dissolve
        saskia.name "Scratch our arses and pick our nose mosta the time."
        saskia.name "She got something for us?"
        frida.name "Jus' bored I think. Come to chat."
        saskia.name "Ah."
        pc "So...?"
        saskia.name "We don't do a thing here. All this stuff around us and nothing to do with it."
        pc "Huh? The machinery?"
        frida.name "Ya, want to make some clothes. Something nice. Not the shitty stuff left over from before."
        frida.name "Stuff was shit anyway. Wanna make like from books and TV. Fancy stuff. Colourful."
        pc "Ah ok. So what's stopping you if you have all this equipment."
        saskia.name "Materials."
        pc "Ah."
        frida.name "Got fuck all to make with."
        saskia.name "Could rip apart other stuff. Clothes and whatever. But ugly as it is, it still works. Feels not right to do that."
        saskia.name "So sitting here with our thumb in our cunts since nothing to do."
        pc "Okay. So why stay here?"
        frida.name "Scavvers. Hoping some poor sot will come bring us something."
        frida.name "So we wait."
        pc "Not looking yourself?"
        saskia.name "Fuck no! Filthy out there. Let someone else do it."
    elif saskia_here():
        show saskia at right1 with dissolve
        pc "Err, so. What is it you actually do here?"
        saskia.name "Said before no?"
        pc "Not really."
        saskia.name "We don't do a thing here. All this stuff around us and nothing to do with it."
        pc "Okay... So why are you here?"
        saskia.name "Hoping it changes. We got all this stuff but no materials do to a damn thing with."
        pc "Why make stuff when you can just buy it?"
        saskia.name "Don't wanna make that shit. Want to make fancy stuff. Old timey clothes an' stuff you see on TV. Not all the boring clothes from before."
        pc "Ah, like fancy dress?"
        saskia.name "Yaa you get it!"
        saskia.name "But fuck all to work with. So we wait here picking our noses."
        pc "Wait for what?"
        saskia.name "Asked scavvers to get us something to work with. Waiting for them to come up with something."
        saskia.name "Then get to work."
        pc "Not looking yourself?"
        saskia.name "Fuck no! Filthy out there. Let someone else do it."
    else:
        show frida at right1 with dissolve
        pc "Err, so. What is it you actually do here?"
        frida.name "Told you didn't we?"
        pc "Not really."
        frida.name "[saskia.nname]! What we do here?"
        frida.name "..."
        frida.name "Not here? A well."
        frida.name "Doin' fuck all now. Got all this gear and can't do a damn thing with it."
        pc "The machinery?"
        frida.name "Ya, want to make some clothes. Something nice. Not the shitty stuff left over from before."
        frida.name "Stuff was shit anyway. Wanna make like from books and TV. Fancy stuff. Colourful."
        pc "Ah ok. So what's stopping you if you have all this equipment."
        frida.name "Got fuck all to make with."
        pc "Ah. No materials?"
        frida.name "No fucking materials!"
        pc "Okay. So why stay here?"
        frida.name "Scavvers. Hoping some poor sot will come bring us something."
        frida.name "So we wait."
        pc "Not looking yourself?"
        frida.name "Yeah no! Not gonna do that."
        frida.name "Don't mind the arse fucking someone will give me when I bend over to look. But scavving's hard work."
        frida.name "Leave that to people who can do it good. I'll stay here clean and waiting."
    pc "Right... Okay then."
    hide saskia
    hide frida
    if loc(loc_school_sewroom):
        $ walk(loc_school_hallway_2f)
    else:
        $ walk(loc_market)
    pcm "..."
    pcm "What fucking weirdos."
    if quest_scav.isactive:
        pcm "So if I understand the crazies right. They need cloth and similar stuff to make clothes with."
        pcm "I can offload any scraps or damaged clothes I come across to them."
    jump travel

label neddle_girls_shop:
    $ needle_girls_new_outfits_check()

    if saskia_here():
        show saskia at right1 with dissolve
        saskia.name "Ooh, want something nice?"
    else:
        show frida at right1 with dissolve
        frida.name "Looking for something good?"
    call screen inventory_itemshop_screen(shop_needle, show_locked=True)
    jump neddle_girls_shop_end



label neddle_girls_junk:
    if saskia_here():
        show saskia at right1 with dissolve
        saskia.name "Oooh, you have something for us?"
    else:
        show frida at right1 with dissolve
        frida.name "Got some nice cloths for us?"
    call screen inventory_junk_choice(shop_needle, choices=[item_scrap_cloth, item_scrap_clothes, item_scrap_jewel, item_scrap_gem])
    $ renpy.scene()
    with dissolve
    jump travel

label neddle_girls_shop_unlock_casino:
    if saskia_here():
        show saskia happy at right1 with dissolve
        saskia.name "I can make you a horny bunny!"
        pc "Huh?"
        saskia.name "Something new for you. Have a look."
    else:
        show frida happy at right1 with dissolve
        frida.name "Sexy rabbit time!"
        pc "Huh?"
        frida.name "Ears and everything. Have a look."
    $ add_to_list(shop_needle.shop_list, [item_outfit_18, [item_socks_13, 2], [item_gloves_3, 2], item_choker_4])
    $ shop_needle.stock()
    $ add_to_list(shop_needle.list, "casino")
    call screen inventory_itemshop_screen(shop_needle, show_locked=True)
    jump neddle_girls_shop_end

label neddle_girls_shop_unlock_jester:
    if saskia_here() and frida_here():
        show frida at right1 with dissolve
        frida.name "I'm here."
        show saskia happy at right2 with dissolve
        saskia.name "And I'm here."
        frida.name "We are here!"
        saskia.name "Are you here?"
        frida.name "[name]'s here."
        saskia.name "I can see her."
        frida.name "Can you?"
        saskia.name "Can I?"
        pc "What the hell?"
        frida.name "Wanna be a jester?"
        saskia.name "A harlequin."
        pc "A what?"
        saskia.name "Look and see."
    elif saskia_here():
        show saskia happy at right1 with dissolve
        saskia.name "Wanna be a funny girl?"
        pc "Huh?"
        saskia.name "Make everyone laugh?"
        pc "No idea."
        saskia.name "Now you can."
        pc "Can I?"
        saskia.name "Sure you can. Have a look."
    else:
        show frida happy at right1 with dissolve
        frida.name "I'm here."
        frida.name "I'm here I said!"
        pc "Okay."
        frida.name "I'm alone..."
        pc "Err... I'm here?"
        frida.name "You're here???"
        pc "I'm here."
        frida.name "You're here!"
        pc "Right..."
        frida.name "Have a look at what I got!"
    $ add_to_list(shop_needle.shop_list, [item_top_28, item_bottom_22, [item_socks_16, 2]])
    $ shop_needle.stock()
    $ add_to_list(shop_needle.list, "jester")
    call screen inventory_itemshop_screen(shop_needle, show_locked=True)
    jump neddle_girls_shop_end

label neddle_girls_shop_unlock_santa:
    if saskia_here():
        show saskia happy at right1 with dissolve
        saskia.name "Hoe!"
        pc "Nice to see you too."
        saskia.name "Hoe hoe hoe!"
        pc "Right."
        saskia.name "Got some santa stuff."
    else:
        show frida happy at right1 with dissolve
        frida.name "Whore!"
        pc "What?"
        show frida
        frida.name "I meant \"hoe\". Got mistaken."
        pc "Okay."
        frida.name "Hoe hoe!"
        pc "Right."
        frida.name "Sexy santa time!"
    $ add_to_list(shop_needle.shop_list, [item_hat_2, item_socks_21, item_gloves_7, item_top_43, item_bottom_35])
    $ shop_needle.stock()
    $ add_to_list(shop_needle.list, "santa")
    call screen inventory_itemshop_screen(shop_needle, show_locked=True)
    jump neddle_girls_shop_end

label neddle_girls_shop_unlock_maid:
    if saskia_here() and frida_here():
        show saskia happy at right1 with dissolve
        saskia.name "Scrub a dub dub, three men in a tub."
        show frida happy at right2 with dissolve
        frida.name "And who do they be?"
        saskia.name "The barman, the copper and the homeless drug dealer."
        frida.name "All getting wanked off by [name]."
        pc "..."
        saskia.name "We got the outfit for your cooking, cleaning, whatever."
    elif saskia_here():
        show saskia happy at right1 with dissolve
        saskia.name "Scrub a dub dub, three men in a tub."
        saskia.name "..."
        show saskia
        saskia.name "Shit, she left..."
        pc "Right..."
        saskia.name "Whatever. Wanna be a bangmaid?"
        pc "Dunno, what's that?"
        saskia.name "Who cares, buy my maid outfit."
    else:
        show frida happy at right1 with dissolve
        frida.name "And who do they be?"
        pc "What?"
        show frida
        frida.name "..."
        frida.name "Damn, she left. We had this all planned!"
        pc "Right."
        frida.name "Whoremaid!"
        pc "Okay."
        frida.name "Have a look."
    $ add_to_list(shop_needle.shop_list, [item_outfit_20, item_socks_14, item_hat_8, item_pants_13])
    $ shop_needle.stock()
    $ add_to_list(shop_needle.list, "maid")
    call screen inventory_itemshop_screen(shop_needle, show_locked=True)
    jump neddle_girls_shop_end



























label neddle_girls_shop_end:
    if saskia_here():
        saskia.name "Come again."
    else:
        frida.name "Bring us some stuff next time."
    $ renpy.scene()
    with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
