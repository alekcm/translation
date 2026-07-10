label random_event_nudevball_mason_catch_park:
    show mason nude at right5 with hpunch
    $ add_to_list(mason.list, "mason_caught_parknude")
    $ player.face_shock()
    pc "Ahhh! Fuck fuck!"
    show mason shock
    mason.name "Shit!"
    show mason at left3 with dissolve
    hide mason with dissolve
    $ player.face_worried()
    pcm "What the hell?"
    pcm "Weird naked man going around."
    pcm "I'm sure he looked familiar..."
    jump travel

label random_event_nudevball_mason_catch_park_convo:
    show mason at right1 with dissolve
    $ add_to_list(mason.list, "mason_caught_parknude_convo")
    mason.name "Miss [sname], can we have a chat."
    $ player.face_shock()
    pc "I knew it was you!"
    mason.name "Err... Yes. I can explain."
    $ player.face_worried()
    pc "Right..."
    mason.name "Maybe I can explain somewhere more private?"
    if player.has_perk([perk_bimbo, perk_slut, perk_party_girl, perk_sucu]):
        $ player.face_happy()
        pc "Oh? I saw your private already and now you want to show it again?"
        mason.name "Right... Okay, out in the open then."
        pc "Yup, get it out in the open for everyone to see."
        $ player.eye = 6
        pc "It was also standing."
        mason.name "Can you not make this more awkward?"
        $ player.eye = 1
        pc "No, I will make it way more awkward. Dingaling your thingy all over. Trying to sneak me alone."
        pc "Pervert coach."
        mason.name "..."
        pc "I'm sure it winked at me."
        hide mason with dissolve
        pcm "Ah, he left."
        pcm "Haha, weirdo."
    else:
        pc "Yeah right. I saw your private already. I'm not going alone with you."
        mason.name "Right... Okay, out in the open then."
        pc "You were all out in the open already. Not my business."
        mason.name "I just hoped I could explain..."
        pc "Explain why you were running around with your thing ready to poke my eye out?"
        pc "Sure, okay. Let's hear it."
        mason.name "..."
        pc "Pervert coach."
        hide mason with dissolve
        pcm "Oh? He left?"
        pcm "Weirdo."
    jump travel

label random_event_nudevball_mason_catch_park_again:
    show mason nude at right1 with hpunch
    $ add_to_list(mason.list, "mason_caught_parknude_again")
    $ add_to_list(loc_beach_hangout.list, "nude_vball")
    $ player.face_shock()
    pc "Ahhh! Fuck!"
    show mason shock
    mason.name "Shit!"
    show mason at left3 with dissolve
    pc "Where are you running off to pervert coach?"
    show mason neutral at right1 with dissolve
    $ player.face_annoyed()
    pc "Again running around with that thing ready to take an eye out."
    mason.name "It's... I can explain..."
    pc "Okay naked man. What are you going to say."
    mason.name "Can I... Maybe get dressed first?"
    if player.has_perk([perk_bimbo, perk_slut, perk_party_girl, perk_sucu], notif=True):
        pc "No! Way more fun like this."
        mason.name "More fun?"
        $ player.eye = 6
        pc "For me anyway."
        mason.name "Errr, okay. If you don't mind then."
        pc "Nope."
        mason.name "Okay. So, err... I kind of..."
        mason.name "Can you look at me?"
        $ player.eye = 1
        pc "Oh? I suppose."
        $ player.eye = 6
        pc "That thing is saying hello."
        mason.name "It is..."
        pc "So what? Pervert like you runs around poking that thing at girls?"
        mason.name "Not quite."
        $ player.eye = 1
        pc "No?"
        mason.name "The idea isn't to get caught."
        pc "Ah. So I caught you twice now."
        mason.name "I didn't expect to bump into one of my students. I was worried it might cause trouble."
        pc "Ah. I could complain you are poking that thingy at me?"
        mason.name "Something like that."
        $ player.eye = 6
        pc "Well, I am not complaining."
        mason.name "No..."
        mason.name "So... Is everything okay?"
        pc "Looks fine to me."
        mason.name "I mean with..."
        show mason happy
        mason.name "Errr..."
        mason.name "..."
        $ player.eye = 1
        pc "What? Getting shy?"
        mason.name "No, kinda of... The opposite..."
        pc "Huh?"
        mason.name "If you want. Come to the beach, we play volleyball there."
        pc "The beach? Wait, the opposite?"
        mason.name "Beach. We play volleyball."
        pc "I know. I have been."
        mason.name "Naked."
        pc "Ah."
        mason.name "Gotta go!"
        hide mason with dissolve
        pcm "I think he was getting way too excited there."
        pcm "Wonder if I will find him wanking in the bushes?"
    else:
        pc "..."
        hide mason with dissolve
        pcm "Damn weird coach."
        pcm "Maybe I should run away..."
        show mason at right1 with dissolve
        mason.name "Err, sorry about that."
        pc "Yeah. So why have I caught my coach running around naked twice now?"
        mason.name "I... Do it for fun..."
        $ player.face_worried()
        pc "Run around naked?"
        mason.name "Yes..."
        pc "Right... This a sex thing?"
        mason.name "No. Yes. It's... A thing..."
        $ player.face_annoyed()
        pc "Right, pervert."
        mason.name "Well, yes. But I didn't mean to scare you. The idea is to not get caught. And if I do I run away."
        mason.name "But I didn't expect to run into someone from the academy."
        pc "Right..."
        mason.name "I tried to explain, but I didn't want to say where people could hear and obviously you didn't want to be alone with me."
        pc "Yeah, might get your thingy out again."
        mason.name "Right. Sorry."
        $ player.face_neutral()
        pc "So what? You go to work, play volleyball then run around naked all night?"
        mason.name "Sometimes..."
        pc "Hope you don't jump out at girls."
        mason.name "No! Nothing like that. Just being naked is the fun."
        pc "Right. Whatever. You do whatever weird stuff you want."
        mason.name "Errm, you will keep it between us?"
        pc "Yeah sure. Your naked secret is safe."
        mason.name "Thank you."
        pc "Mmmm."
        mason.name "If you are interested, we play volleyball at the beach."
        pc "Yeah I know. I have been there."
        mason.name "At night. Naked."
        pc "Ah. Yeah not sure I want to be jumped by a bunch of naked men when I fall over."
        mason.name "Actually I am the only man there. Rest are girls."
        pc "Really?"
        mason.name "Girls wont play if men jump on them. At least most girls... Many girls..."
        pc "So why do they let you play?"
        mason.name "I'm in it for the naked fun, not jumping on people."
        pc "Okay. Well whatever. You do your naked thing."
        mason.name "Be safe."
        hide mason with dissolve
        pcm "Naked volleyball? Really?"
        pcm "Heh, weirdos."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
