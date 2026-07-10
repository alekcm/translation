screen surgery_screen(service=""):
    zorder 0
    $ reset_speaking_char()
    if cheats == 1:
        frame align (0,0.095):
            text "[tab_top_acc] and [tab_left_acc] and [primary_colour] and [secondary_colour]"
    frame anchor (0,0) align (0.3,0.095) xysize (990,900):
        has vbox
        hbox:
            vbox:
                frame padding (0,0) xysize (82,80) background None:
                    add "button_wardrobe_tab_bg"
                    add "button_wardrobe_tab_frame_idle"

                if service == "salon":
                    $ surgery_list = ["eyeliner", "hair_length", "phair", "eyes", "eyeshadow", "lipstick", "blush", "nails"]
                else:
                    $ surgery_list = ["eyeliner", "hair_length", "phair", "eyes", "skin", "skin_effect", "breasts", "nip_size"]
                for i in surgery_list:
                    use acc_screen_left_makeup_button(i)


            vbox:
                vbox:
                    if "hair" in tab_left_acc:
                        use acc_screen_hair_colours()
                    elif tab_left_acc == "eyes":
                        use acc_screen_eyes_colours()
                    elif tab_left_acc in ["skin", "breasts", "skin_effect"]:
                        use acc_screen_skin_colours()
                    elif tab_left_acc in ["nip_size"]:
                        use acc_screen_nips_colours()


                    else:
                        use acc_screen_makeup_colours()

                hbox:
                    vbox:

                        hbox:
                            for i in (1,2,3,4):
                                use acc_screen_item_makeup_eyeliner_button(i)

                        hbox:
                            for i in (1,2,3,4):
                                use acc_screen_item_hair_neck_button(i)
                            for i in (1,2,3,4,5,6):
                                use acc_screen_item_hair_fringe_button(i)

                        hbox:
                            for i in (0,1):
                                use acc_screen_item_hair_p_button(i)

                        hbox:
                            use acc_screen_item_eyes_button()

                        if service == "salon":
                            hbox:
                                use acc_screen_item_makeup_button("eyeshadow")
                            hbox:
                                use acc_screen_item_makeup_button("lipstick")
                            hbox:
                                use acc_screen_item_makeup_button("blush")
                            hbox:
                                use acc_screen_item_makeup_button("nails")

                        if service == "":
                            hbox:
                                use acc_screen_item_skin_button()

                            hbox:
                                for i in (0,1):
                                    use acc_screen_item_freckles_button(i)

                            hbox:
                                for i in (1,2,3):
                                    use acc_screen_item_breastsize_button(i)

                            hbox:
                                for i in (1,2,3):
                                    use acc_screen_item_nips_button(i)




    frame anchor (0.0,0.0) align (0.82,0.095) xysize (330,900):
        has vbox xsize 330 ysize 880
        hbox align (0.5, 1.0):
            use color_picker()

    use surgery_screen_return()

label surgery_screen_cheat:


    call screen surgery_screen() 
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
