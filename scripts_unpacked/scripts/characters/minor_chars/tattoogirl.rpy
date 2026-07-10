init python:
    def salongirl_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        cur_location = loc_shop_tattoo
        
        
        
        
        
        
        
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

layeredimage salongirl:
    at sprite_highlight("salongirl")
    always "salongirl_base"

label shop_tattoo_speak:
    show salongirl at right1 with dissolve
    if not salongirl.has_met:
        salongirl.name "Heya darlin'. Not seen you before."
        pc "No, just poked my head in to see what this place is."
        salongirl.name "It's where I make you beautiful."
        salongirl.name "Makeup, hair, tattoos, jewellery. All the nice things."
        pc "Ah okay. Sounds good."
        salongirl.name "Yup. Cost ya though. Looking amazing ain't cheap."
        pc "Right."
        hide salongirl with dissolve
        jump travel

    salongirl.name "What can I do for you?"
    menu:
        "Jewelry":
            salongirl.name "Sure, here's what I got."
            call screen inventory_itemshop_screen(shop_piercings) 
            salongirl.name "Be safe out there."
            hide salongirl_base with dissolve
            jump travel
        "Makeover - £150":
            if not player.cash >= 150:
                pcm "Hmm, I don't have enough..."
                pc "I'll come back when I have the money."
                salongirl.name "No problem darling."
            else:
                salongirl.name "Lovely. Come here and sit down. I'll make ya look great."
                call screen surgery_screen(service="salon") 
                $ player.spend(150)
                salongirl.name "Wonderful!"
            hide salongirl with dissolve
            jump travel
        "Tattoos":
            jump tattoo_shop

label tattoo_shop:
    salongirl.name "Oooh fun. What did you have in mind?"
    menu:
        "Tattoo a Butterfly on breast - £250" if not tattoo.chest and player.cash >= 250:
            $ temp_var_1 = "butterfly"
            $ player.spend(250)
        "Tattoo a tramp stamp - £250" if not tattoo.ass and player.cash >= 250:
            $ temp_var_1 = "tramp"
            $ player.spend(250)
        "Tattoo \"Whore\" on forehead - £100" if writing.forehead and not "tattoo" in writing.forehead and player.cash >= 100:
            $ temp_var_1 = "whore"
            $ player.spend(100)
        "Tattoo Slut heart on cheek - £100" if writing.face and not "tattoo" in writing.face and player.cash >= 100:
            $ temp_var_1 = "slut"
            $ player.spend(100)
        "Tattoo \"Milk me\" on chest - £100" if writing.chest and not "tattoo" in writing.chest and player.cash >= 100:
            $ temp_var_1 = "milk"
            $ player.spend(100)
        "Tattoo \"Fertile\" on stomach - £100" if writing.belly and not "tattoo" in writing.belly and player.cash >= 100:
            $ temp_var_1 = "fertile"
            $ player.spend(100)
        "Tattoo \"Cum here\" on pubis - £100" if writing.pubic and not "tattoo" in writing.pubic and player.cash >= 100:
            $ temp_var_1 = "cum"
            $ player.spend(100)
        "Tattoo \"Anal queen\" on my ass - £100" if writing.anus and not "tattoo" in writing.anus and player.cash >= 100:
            $ temp_var_1 = "anal"
            $ player.spend(100)
        "Tattoo \"Fuck me\" on my thigh - £100" if writing.lleg and not "tattoo" in writing.lleg and player.cash >= 100:
            $ temp_var_1 = "fuck"
            $ player.spend(100)
        "Tattoo a sex counter on my ass - £100" if writing.ass and not "tattoo" in writing.ass and player.cash >= 100:
            $ temp_var_1 = "counter"
            $ player.spend(100)
        "Never mind":

            salongirl.name "No problem, come back when you have thought it over."
            hide salongirl with dissolve
            jump travel


    salongirl.name "Okay, let's go around back for privacy. Clothes off please."
    pc "Right."
    $ player.uncover()
    $ pc_striptease()
    salongirl.name "Buzz buzz buzz."
    show screen blackout() with dissolve
    pause 0.5
    $ relax(30)
    jump expression "tattoo_shop_" +  temp_var_1

label tattoo_shop_butterfly:
    $ tattoo.chest = 1
    hide screen blackout with dissolve
    show sb_pose_showbreasts with dissolve
    salongirl.name "And we have a lovely little butterfly."
    salongirl.name "That should bring some more attention."
    pc "Thanks."
    salongirl.name "Don't fly away now."
    jump tattoo_shop_end

label tattoo_shop_tramp:
    $ tattoo.ass = 1
    hide screen blackout with dissolve
    show sb_pose_lookback happy smile with dissolve
    salongirl.name "Perfect. Something for people to admire."
    salongirl.name "Should be more fun when you bend over."
    pc "Thanks."
    jump tattoo_shop_end

label tattoo_shop_whore:
    $ writing.add_writing("forehead", "tattoo")
    hide screen blackout with dissolve
    show sb_pose_showbreasts with dissolve
    salongirl.name "And now everyone will know what you really are."
    salongirl.name "Might not get you any more customers though, covers up your pretty face."
    pc "..."
    jump tattoo_shop_end

label tattoo_shop_slut:
    $ writing.add_writing("face", "tattoo")
    hide screen blackout with dissolve
    show sb_pose_showbreasts with dissolve
    salongirl.name "Not sure why you would wan't to advertise this."
    salongirl.name "But something to show everyone you are a slutty slut."
    pc "..."
    jump tattoo_shop_end

label tattoo_shop_milk:
    $ writing.add_writing("chest", "tattoo")
    hide screen blackout with dissolve
    show sb_pose_showbreasts with dissolve
    salongirl.name "Now you can be a genuine cow."
    salongirl.name "Have you met the other cow in the market? You two will get along."
    if player.breasts == 3:
        salongirl.name "With those huge tits people already knew what you were though."
    pc "Moo!"
    jump tattoo_shop_end

label tattoo_shop_fertile:
    $ writing.add_writing("belly", "tattoo")
    hide screen blackout with dissolve
    show sb_mast_stand with dissolve
    if player.pregnant >= 2:
        salongirl.name "A bit late for a sign telling the guys to knock you up, but there is always a next time."
    else:
        salongirl.name "And now all the guys will want to knock you up."
    salongirl.name "I guess that's what you hope for anyway."
    salongirl.name "Didn't think I'd tattoo a girl wanting to get preggo, but crazy is crazy."
    pc "..."
    jump tattoo_shop_end

label tattoo_shop_anal:
    $ writing.add_writing("anus", "tattoo")
    hide screen blackout with dissolve
    show sb_pose_upvag with dissolve
    salongirl.name "Not a bad idea taking it in the ass."
    salongirl.name "But did you really have to put a sign on it saying so?"
    salongirl.name "Doubt anyone is going to listen, or read... Actually they probably will read."
    pc "Hopefully."
    jump tattoo_shop_end

label tattoo_shop_counter:
    $ writing.add_writing("ass", "tattoo")
    hide screen blackout with dissolve
    show sb_pose_upvag with dissolve
    salongirl.name "Right, well. Not sure I would be putting a counter on someone's ass on how many dicks they have had."
    salongirl.name "But whatever, not my business..."
    jump tattoo_shop_end

label tattoo_shop_fuck:
    $ writing.add_writing("lleg", "tattoo")
    hide screen blackout with dissolve
    show sb_pose_upvag with dissolve
    salongirl.name "Not sure the guys need any directions not to fuck you, they are perverts."
    salongirl.name "But I suppose most need at last some directions finding where to put it."
    pc "..."
    salongirl.name "Don't think the arrow is going to stop them from poking and prodding until you do it for them."
    jump tattoo_shop_end

label tattoo_shop_cum:
    $ writing.add_writing("pubic", "tattoo")
    hide screen blackout with dissolve
    show sb_mast_stand with dissolve
    salongirl.name "The guys were going to do this anyway I think, but fun to be a pervert now and then."
    salongirl.name "Not sure I would have got it tattooed myself, but be as you want."
    pc "..."
    jump tattoo_shop_end

label tattoo_shop_end:
    hide sb_pose_lookback
    hide sb_pose_upvag
    hide sb_pose_showbreasts
    hide sb_mast_stand
    with dissolve
    salongirl.name "I'll leave you to get dressed."
    hide salongirl with dissolve
    $ pc_dress_slow()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
