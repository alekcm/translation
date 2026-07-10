init python:
    def show_notif_popup(message):
        var = 0
        for i in irange(0,8):
            if not renpy.get_screen("notif_popup_" + str(var)):
                renpy.show_screen("notif_popup_" + str(var), message)
                break
            else:
                var = var + 1

    def diary_people_list_progress(back=False):
        global diary_people_list_var, diary_people_list
        diary_people_list = sorted(diary_people_list, key=lambda person: person.bio_group)
        if not back:
            diary_people_list_var += 1
            if diary_people_list_var > len(diary_people_list):
                diary_people_list_var = 1
        else:
            diary_people_list_var -= 1
            if diary_people_list_var < 1:
                diary_people_list_var = len(diary_people_list)

    def get_diary_people_list_entry():
        global diary_people_list_var
        number = diary_people_list_var - 1
        return diary_people_list[number]

    def get_selected_perk_name_desc():
        if selected_perk and selected_perk in player.perk_list:
            if selected_perk == player.origin_perk:
                return selected_perk.name + " origin", selected_perk.desc
            else:
                return selected_perk.name, selected_perk.desc
        else:
            return "", ""

    def get_selected_perk_timer():
        if selected_perk and selected_perk in player.perk_list and selected_perk.hours:
            return "Lasts for " + str(selected_perk.hours) + If(selected_perk.hours > 1, " hours", " hour")
        if selected_perk and selected_perk in player.perk_list and selected_perk.days:
            return "Lasts for " + str(selected_perk.days) + If(selected_perk.days > 1, " days", " day")
        else:
            return ""

    def get_selected_perk_victim():
        if selected_perk and selected_perk in player.perk_list and selected_perk.victim:
            return "Vulnerable"
        elif selected_perk and selected_perk in player.perk_list and selected_perk.not_victim:
            return "Streetwise"

    def get_selected_perk_stats(stat):
        if selected_perk and selected_perk in player.perk_list:
            text = stat.capitalize() + " "
            if stat == "allure":
                if getattr(selected_perk, stat + "_add"):
                    text = text + "add(" + str(getattr(selected_perk, "allure_add")) + ")"
            elif stat == "fertility":
                if getattr(selected_perk, stat + "_multi"):
                    text = text + "multi(" + str(getattr(selected_perk, "fertility_multi")) + ")"
            else:
                for i in ("min", "max", "add", "multi", "multineg"):
                    if getattr(selected_perk, stat + "_" + i):
                        text = text + i + "(" + str(getattr(selected_perk, stat + "_" + i)) + "), "
            if text == stat.capitalize() + " ":
                return False
            else:
                return text

    def rename_npc(who):
        global tempname, tempname2
        tempname = copy.deepcopy(who)
        tempname2 = who
        renpy.jump("rename_npc")

    def diary_set_seen(tab):
        global new_diary_diary_entry, new_diary_people_entry, new_diary_job_entry
        if tab == 3:
            new_diary_people_entry = False
        if tab == 4:
            new_diary_diary_entry = False
        if tab == 5:
            new_diary_job_entry = False

    def diary_name_title():
        if main_quest_04.active:
            return "The Fixer"
        elif quest_homeless_start.active == 1 or quest_homeless.active == 1:
            return "Homeless girl"
        elif player.has_perk(perk_addict) and quest_whore.sold > 10:
            return "Junkie whore"
        elif player.has_perk(perk_addict):
            return "Junkie"
        elif quest_whore.sold > 10:
            return "Whore"
        elif player.has_perk(perk_exhibitionist):
            return "Flaunter"
        else:
            return "Waif"



label rename_npc:
    menu:
        "Rename [tempname.fullname]":
            $ tempname._fname = renpy.input("First name", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=15)
            $ tempname._fname = tempname._fname.strip()

            if tempname._fname == "":
                $ tempname._fname = tempname2._fname

            $ tempname._sname = renpy.input("Second name", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=15)
            $ tempname._sname = tempname._sname.strip()

            if tempname._sname == "":
                $ tempname._sname = tempname2._sname

            $ tempname._nname = renpy.input("Does [tempname.fname] [tempname.sname] have a nickname?", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=15)
            $ tempname._nname = tempname._nname.strip()


            "Rename [tempname2.diaryname] to [tempname.diaryname]?"
            menu:
                "Yes":
                    $ tempname2._fname = tempname._fname
                    $ tempname2._sname = tempname._sname
                    $ tempname2._nname = tempname._nname
                    $ tempname2.classname = Character(tempname.setname_start, color=tempname._colour, callback=name_callback, cb_name=tempname.setname.lower(), image=If(tempname.bio_image, tempname.bio_image, tempname._fname))
                    jump travel
                "No":
                    jump travel
        "Keep it as [tempname.fname] [tempname.sname]":

            $ NullAction()
    jump travel



default diary_people_list_var = 1
default diary_people_list = []
default stats_screen_tab = 1
default quest_objectives_button = True
default selected_perk = None

define new_diary_diary_entry = True
define new_diary_people_entry = True
define new_diary_job_entry = True

screen qkey




style quest_obj_stat is text:
    size 42
    font "BRLNSB.TTF"
    idle_color '#8888887f'
    hover_color '#e066a3'
    selected_color '#ffffff'
    insensitive_color '#8888887f'

style quest_obj_stat_alt is text:
    size 38
    font "BRLNSB.TTF"
    idle_color '#8888887f'
    hover_color '#e066a3'
    selected_color '#ffffff'
    insensitive_color '#8888887f'

image diary_button_menu_small_idle:
    "diary_button_menu_small_hover"
    matrixcolor TintMatrix("#b23f73")
image diary_button_menu_large_idle:
    "diary_button_menu_large_hover"
    matrixcolor TintMatrix("#b23f73")
image diary_button_icon_next_idle:
    "diary_button_icon_next_hover"
    matrixcolor TintMatrix("#b23f73")
image diary_button_icon_next_left_hover:
    "diary_button_icon_next_hover"
    xzoom -1
image diary_button_icon_next_left_idle:
    "diary_button_icon_next_left_hover"
    matrixcolor TintMatrix("#b23f73")

screen diary_stats_perk_button(perk):
    frame padding (0,0) xysize (82,80) background None:
        if perk == player.origin_perk:
            add "button_wardrobe_tab_y_bg"
        else:
            add "button_wardrobe_tab_bg"
        add perk.image:
            if selected_perk != perk:
                matrixcolor TintMatrix(wardrobe_colour_selected)

        imagebutton auto "button_wardrobe_tab_frame_%s":
            action SetVariable("selected_perk", perk)

screen diary_button(picture, desc, tab, arrow=False):
    if stats_screen_tab == tab:
        $ desc = str.upper(desc)
        frame padding (0,0) xysize (336,84) background None:
            add "diary_button_menu_large_idle"
            text desc anchor (0.5,0.5) align (0.5,0.5) size 60 font "BRLNSB.TTF" yoffset 3
            if arrow:
                imagebutton auto "diary_button_icon_next_%s" anchor (0.5,0.5) align (0.93, 0.5):
                    action Function(diary_people_list_progress)
                imagebutton auto "diary_button_icon_next_left_%s" anchor (0.5,0.5) align (0.07, 0.5):
                    action Function(diary_people_list_progress, back=True)
    else:
        frame padding (0,0) xysize (84,84) background None:
            add "diary_button_icon_" + picture anchor (0.5,0.5) align (0.5,0.5)
            imagebutton auto "diary_button_menu_small_%s":
                action [SetVariable ("stats_screen_tab", tab), Function(diary_set_seen, tab)],
            if (tab == 3 and new_diary_people_entry) or (tab == 4 and new_diary_diary_entry) or (tab == 5 and new_diary_job_entry):
                add "diary_button_icon_newentry"

screen diary_button_close():
    frame padding (0,0) xysize (84,84) background None:
        add "diary_button_icon_return" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "diary_button_menu_small_%s":
            action [ Hide(log.screen()), Show("right_menu"), Show("travel_screen"), Function(player.face_normal)]



screen diary_title(title):
    hbox xysize (950, 50) pos (875,200):
        text title font "BRLNSB.TTF" size 42

screen diary_npc_name(title, who):
    hbox ysize (950) pos (875,200):
        text title font "BRLNSB.TTF" size 42
        textbutton "RENAME" action [Hide(log.screen()), Show("right_menu"), Function(player.face_normal), Function(rename_npc, who)] background None xpadding 0.0 text_size 8


screen qlog():
    default stats_tab = 1
    add "diary_ui_bg"
    hbox anchor (0, 0) pos (875,100) spacing 4:
        use diary_button("bio", name, 1)
        use diary_button("stats", "Stats", 2)
        use diary_button("people", "People", 3, arrow=True)
        use diary_button("diary", "Diary", 4)
        use diary_button("quest", "Questlog", 5)
        use diary_button_close()

    if stats_screen_tab == 1:
        use qlog_bio()
    elif stats_screen_tab == 2:
        use qlog_stats()
    elif stats_screen_tab == 3:
        use qlog_people()
    elif stats_screen_tab == 4:
        use qlog_diary()
    elif stats_screen_tab == 5:
        use qlog_questlog()

    add "diary_ui_frame"

screen qlog_bio():
    add AlphaMask("diary_bio_layered", "diary_ui_frame_alpha_mask") xalign 0.29
    if not fname == name:
        use diary_title(fname + " \"" + name + "\" " + sname + " - " + diary_name_title())
    else:
        use diary_title(fname + " " + sname + " - " + diary_name_title())

    viewport xysize (875, 700) pos (875,275):
        scrollbars "vertical"
        vscrollbar_unscrollable "hide"
        draggable True
        mousewheel True
        has vbox

        if quest_homeless_start.active:
            text "I am [fname] [sname]. After fleeing my home city with my sister [emile.name], We were in a serious car accident and fled some lunatics chasing us." size 24
            text "We were seperated while fleeing and I lost sight of her and ended up in this unknown town all alone." size 24
        else:
            text "I am [fname] [sname]. After fleeing my home city with my sister [emile.name], I was in a fatal accident and was left close to death." size 24
            text "As luck would have it, I was saved by the enigmatic \"Institute\" who put my mind in a new body in an attempt to save my life." size 24
        text "" size 10
        if player.comfort_description():
            text player.comfort_description() size 24
            text "" size 10
        text player.description() size 24
        text "" size 10
        text c.description_outfit() size 24
        text c.description_top() size 24
        if c.description_bottom():
            text c.description_bottom() size 24
        text "" size 10
        text player.description_sex() size 24
        text player.preg_text() size 24
        text player.description_period() size 24
        if player.recovering:
            text "I have recently suffered a serious trauma and am feeling pretty shit about myself. Hopefully it will go away in a few days." size 24

screen qlog_stats():
    add "diary_stats_layered" xalign 0.26
    use diary_title("My personal diary")

    hbox pos (875,275):
        hbox:
            vbox xsize 200:
                text "Handjobs:" size 26
                text "Blowjobs:" size 26
                text "• Swallowed:" size 26
                text "• Facials:" size 26
            vbox xsize 30

            vbox xsize 30:
                text "[player.hsex]" size 26
                text "[player.osex]" size 26
                text "[player.swallow]" size 26
                text "[player.facial]" size 26
            vbox xsize 30
        hbox:
            vbox xsize 200:
                text "Vaginal sex:" size 26
                text "Creampies:" size 26
                text "• Safe:" size 26
                text "• Normal:" size 26
                text "• Risky:" size 26
                text "Anal sex:" size 26
                text "• Anal creampie:" size 26
            vbox xsize 30
            vbox xsize 30:
                text "[player.vsex]" size 26
                text str(player.creamsafe + player.creamdanger + player.creamnormal) size 26
                text "[player.creamsafe]" size 26
                text "[player.creamnormal]" size 26
                text "[player.creamdanger]" size 26
                text "[player.asex]" size 26
                text "[player.creamanal]" size 26
            vbox xsize 30
        hbox:
            vbox xsize 200:
                text "Prostitution:" size 26
                text "• Cash made:" size 26
                if danger_content:
                    text "Raped:" size 26
                text "" size 26
                text "Pregnancies:" size 26
                text "Children:" size 26
                text "• Boys" size 26
                text "• Girls" size 26
            vbox xsize 30
            vbox xsize 30:
                text "[player.sold]" size 26
                text "£[player.soldpricetotal]" size 26
                if danger_content:
                    text "[player.rape]" size 26
                text "" size 26
                text "[player.preg_amount]" size 26
                text "[player.pregbabies]" size 26
                text "--" size 26
                text "--" size 26
            vbox xsize 30

    vbox xysize (420,70) pos (875,620):
        text "Perks" font "BRLNSB.TTF" size 42








    hbox xsize 430 pos (875,700):
        viewport xysize (430, 250):
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            draggable True
            mousewheel True
            has hbox
            box_wrap True
            use diary_stats_perk_button(player.origin_perk)
            for perk in player.perk_list:
                if not perk == player.origin_perk:
                    use diary_stats_perk_button(perk)

    vbox xysize (500,70) pos (1350,620):
        text get_selected_perk_name_desc()[0] font "BRLNSB.TTF" size 42
        text "" size 10
        text get_selected_perk_name_desc()[1] size 24
        text "" size 10
        text get_selected_perk_timer() size 24
        for i in ("desire", "tired", "mood", "confidence", "fitness", "int", "allure", "fertility"):
            if get_selected_perk_stats(i):
                text get_selected_perk_stats(i) size 24
        if get_selected_perk_victim():
            text get_selected_perk_victim() size 24

screen qlog_people():
    add AlphaMask(Transform(get_diary_people_list_entry().bio_image, xzoom=-1, crop=(0,0,450,980)), "diary_ui_frame_alpha_mask"):
        anchor (1.0, 0.0) align (0.45, 0.05) zoom 1.2
        if get_diary_people_list_entry().dead:
            matrixcolor SaturationMatrix(0)

    use diary_npc_name(get_diary_people_list_entry().diaryname, get_diary_people_list_entry())


    vbox xsize 875 pos (875,275):
        text get_diary_people_list_entry().bio_text size 24
        text "" size 24

        if not get_diary_people_list_entry().rape or get_diary_people_list_entry().is_female:
            text get_diary_people_list_entry().love_desc size 24


        if get_diary_people_list_entry()._original_name.lower() + "_here" in globals() and not get_diary_people_list_entry().dead:
            text "Location - " + globals()[get_diary_people_list_entry()._original_name.lower() + "_here"](where=True) size 24
        elif get_diary_people_list_entry().dead and get_diary_people_list_entry().dead_location:
            text get_diary_people_list_entry().dead_location size 24
        else:
            text "Location - Unknown" size 24

        if (get_diary_people_list_entry().love >= 60 or cheats) and get_diary_people_list_entry().is_female:
            if get_diary_people_list_entry().iswhore:
                text "She works as a whore." size 24
            elif get_diary_people_list_entry().isslut:
                text "She is a bit of a slut." size 24

        if not get_diary_people_list_entry().is_female:
            if get_diary_people_list_entry().rape:
                text "The arsehole forced himself on me so he can fuck right off." size 24
            elif get_diary_people_list_entry().sex:
                if get_diary_people_list_entry().sex == 1:
                    text "We have had sex before." size 24
                elif get_diary_people_list_entry().sex < 4:
                    text "We have had sex a few times." size 24
                else:
                    text "We have spent quite a bit of time together having sex." size 24
            elif get_diary_people_list_entry().naughty:
                text "While we haven't had sex, we have fooled around a bit and he has seen me naked." size 24
            elif get_diary_people_list_entry().seen_any:
                if get_diary_people_list_entry().seen_all:
                    text "While we haven't fooled around, he has seen me totally naked." size 24
                elif get_diary_people_list_entry().seen_breasts:
                    text "While we haven't fooled around, he has seen me topless." size 24
                else:
                    text "While we haven't fooled around, he has seen me undressed." size 24
            if not get_diary_people_list_entry().dead:
                text get_diary_people_list_entry().lust_desc size 24
        else:
            if get_diary_people_list_entry().sex_les:
                if get_diary_people_list_entry().sex_les == 1:
                    text "Despite being girls, we have had sex before." size 24
                elif get_diary_people_list_entry().sex_les < 4:
                    text "Despite being girls, we have had sex a few times." size 24
                else:
                    text "We have spent quite a bit of time together having sex." size 24
            elif get_diary_people_list_entry().nosex_les and get_diary_people_list_entry().seen_any:
                text "Despite being girls, we have kind of fooled around and seen each other naked." size 24
            elif get_diary_people_list_entry().nosex_les:
                text "Despite being girls, we have kind of fooled around." size 24
            elif get_diary_people_list_entry().seen_any:
                text "She has seen me undressed. But we are both girls so that doesn't matter..." size 24

        if get_diary_people_list_entry().drunk:
            if get_diary_people_list_entry().is_female:
                if get_diary_people_list_entry().drunk >= 100:
                    text "She is blackout drunk." size 24
                elif get_diary_people_list_entry().drunk >= 75:
                    text "She is piss drunk." size 24
                elif get_diary_people_list_entry().drunk >= 50:
                    text "She is drunk." size 24
                elif get_diary_people_list_entry().drunk >= 25:
                    text "She is kinda tipsy." size 24
                else:
                    text "She has been drinking." size 24
            else:
                if get_diary_people_list_entry().drunk >= 100:
                    text "He is blackout drunk." size 24
                elif get_diary_people_list_entry().drunk >= 75:
                    text "He is piss drunk." size 24
                elif get_diary_people_list_entry().drunk >= 50:
                    text "He is drunk." size 24
                elif get_diary_people_list_entry().drunk >= 25:
                    text "He is kinda tipsy." size 24
                else:
                    text "He has been drinking." size 24



        if get_diary_people_list_entry().vvirgin and not get_diary_people_list_entry().rape:
            text "I had my first time with " + get_diary_people_list_entry().fname size 24
        if get_diary_people_list_entry().is_female and get_diary_people_list_entry().is_pregnant and get_diary_people_list_entry().days_pregnant > (global_pregnancy_length * 0.3):
            if get_diary_people_list_entry().love < 60 and not cheats:
                text "She is currently pregnant." size 24
            elif get_diary_people_list_entry().pregnant_who == lover:
                text "She is currently pregnant with someone she has a one night stand with." size 24
            elif get_diary_people_list_entry().pregnant_who == rapist:
                text "She is carrying the baby of someone who raped her." size 24
            elif get_diary_people_list_entry().pregnant_who == punter:
                text "She is carrying the baby of someone who paid to have sex with her." size 24
            elif get_diary_people_list_entry().pregnant_who == highpayer:
                text "She is carrying the baby of someone who offered far too much money to refuse." size 24
            elif get_diary_people_list_entry().pregnant_who == busgroper:
                text "She is carrying the baby of some bus groper." size 24
            elif get_diary_people_list_entry().pregnant_who == partyman:
                text "She is carrying the child of someone she entertined at the dance party." size 24
            elif get_diary_people_list_entry().pregnant_who == mira_kidnapper:
                text "She is carrying the child of the guy who held her captive." size 24
            else:
                text "She is currently pregnant with " + get_diary_people_list_entry().pregnant_who.setname + "'s child." size 24
        else:
            if get_diary_people_list_entry().preg_current:
                text "I am currently pregnant with his child." size 24

        if get_diary_people_list_entry().dead:
            if get_diary_people_list_entry().dead_message:
                text get_diary_people_list_entry().dead_message size 24
            else:
                text get_diary_people_list_entry().setname + " is dead." size 24

    if get_diary_people_list_entry().is_female:
        hbox pos (875,700):
            hbox:
                vbox:
                    text "Handjobs:" size 24
                    text "Blowjobs:" size 24
                    text "Vaginal sex:" size 24
                    text "Anal sex:" size 24
                vbox:
                    xsize 30
                vbox:
                    if get_diary_people_list_entry().love >= 60 or cheats:
                        text str(get_diary_people_list_entry().hsex) size 24
                        text str(get_diary_people_list_entry().osex) size 24
                        text str(get_diary_people_list_entry().vsex) size 24
                        text str(get_diary_people_list_entry().asex) size 24

                    else:
                        text "???" size 24
                        text "???" size 24
                        text "???" size 24
                        text "???" size 24

                vbox:
                    xsize 30
            hbox:
                vbox:
                    text "Sold herself:" size 24
                    text "Forced:" size 24
                    text "" size 24
                    text "Pregnant:" size 24
                    text "• Babies:" size 24

                vbox:
                    xsize 30
                vbox:
                    if get_diary_people_list_entry().love >= 60 or cheats:
                        text str(get_diary_people_list_entry().sold) size 24
                        text str(get_diary_people_list_entry().rape) size 24
                        text "" size 24
                        text str(get_diary_people_list_entry().preg) size 24
                        text str(get_diary_people_list_entry().pregbabies) size 24
                    else:
                        text "???" size 24
                        text "???" size 24
                        text "" size 24
                        text "???" size 24
                        text "???" size 24


                vbox:
                    xsize 30
    else:
        hbox pos (875,700):
            hbox:
                vbox:
                    text "Handjobs:" size 24
                    text "Blowjobs:" size 24
                    text "• Swallowed:" size 24
                    text "• Facials:" size 24
                    text "• On body:" size 24
                vbox:
                    xsize 30
                vbox:
                    text str(get_diary_people_list_entry().hsex) size 24
                    text str(get_diary_people_list_entry().osex) size 24
                    text str(get_diary_people_list_entry().swallow) size 24
                    text str(get_diary_people_list_entry().facial) size 24
                    text str(get_diary_people_list_entry().buk) size 24
                vbox:
                    xsize 30
            hbox:
                vbox:
                    text "Vaginal sex:" size 24
                    text "Creampies:" size 24
                    text "• Safe:" size 24
                    text "• Normal:" size 24
                    text "• Risky:" size 24
                    text "Anal sex:" size 24
                    text "• Anal creampies:" size 24
                vbox:
                    xsize 30
                vbox:
                    text str(get_diary_people_list_entry().vsex) size 24
                    text str(get_diary_people_list_entry().creamvag) size 24
                    text str(get_diary_people_list_entry().creamsafe) size 24
                    text str(get_diary_people_list_entry().creamnormal) size 24
                    text str(get_diary_people_list_entry().creamdanger) size 24
                    text str(get_diary_people_list_entry().asex) size 24
                    text str(get_diary_people_list_entry().creamanal) size 24
                vbox:
                    xsize 30
            hbox:
                vbox:
                    text "Bought me:" size 24
                    text "• Cash made:" size 24
                    text "Assaulted:" size 24
                    text "Forced:" size 24
                    text "" size 24
                    text "Pregnant:" size 24
                    text "• Babies:" size 24

                vbox:
                    xsize 30
                vbox:
                    text str(get_diary_people_list_entry().sold) size 24
                    text "£{}".format(get_diary_people_list_entry().soldpricetotal) size 24
                    text str(get_diary_people_list_entry().assault) size 24
                    text str(get_diary_people_list_entry().rape) size 24
                    text "" size 24
                    text str(get_diary_people_list_entry().preg) size 24
                    text str(get_diary_people_list_entry().pregbabies) size 24

                vbox:
                    xsize 30

screen qlog_diary():

    $ new_diary_entry = False

    add "diary_diary" xalign 0.26
    use diary_title("My diary")

    viewport xysize (875, 700) pos (875,275):
        scrollbars "vertical"
        vscrollbar_unscrollable "hide"
        draggable True
        mousewheel True
        has vbox xsize 855
        box_reverse True
        for i in diary_list:

            if i.left_pic:
                use qlog_diary_entry_leftimage(i.name, i.date, i.description, i.left_pic)

            elif i.right_pic:
                use qlog_diary_entry_rightimage(i.name, i.date, i.description, i.right_pic)
            else:
                vbox:
                    text i.name size 34 font "BRLNSB.TTF"
                    null height 5
                    text i.date size 18 color "#b1b1b1"
                    null height 10
                    text i.description size 24
                    text "" size 24
                    null height 30

screen qlog_diary_entry_leftimage(name, date, desc, pic):
    vbox:

        hbox xsize 855:
            frame xsize 280 ysize 300 background None:
                add pic rotate numgen(-10,10) anchor ((0.5, 0.5)) align (0.5,0.6)
            frame xsize 575 background None:
                has vbox
                text "" size 24
                text name size 34 font "BRLNSB.TTF"
                text date size 18 color "#b1b1b1"
                text desc size 24
                text "" size 24
        frame ysize 20 background None

screen qlog_diary_entry_rightimage(name, date, desc, pic):
    vbox:

        hbox xsize 855:

            frame xsize 575 background None:
                has vbox
                text "" size 24
                text name size 34 font "BRLNSB.TTF"
                text date size 18 color "#b1b1b1"
                text desc size 24
                text "" size 24
            frame xsize 280 ysize 300 background None:
                add pic rotate numgen(-10,10) anchor ((0.5, 0.5)) align (0.5,0.6)
        frame ysize 20 background None

screen qlog_questlog():
    if log.activeimage():
        add log.activeimage() xalign 0.26

    viewport xysize (250, 400) pos (875,200):
        scrollbars "vertical"
        draggable True
        mousewheel True

        has vbox

        if log.definedtab("Institute"):
            text "MISSIONS" size 30 font "BRLNSB.TTF"
            vbox:
                box_reverse True
                for i in log.maintab():
                    textbutton i.title() action SetField(log, "qvar", i) background None xpadding 0.0 text_size 24

        if log.definedtab("Jobs"):
            text "" size 18
            text "JOBS" size 30 font "BRLNSB.TTF"
            vbox:
                box_reverse True
                for i in log.definedtab("Jobs"):
                    textbutton i.title() action SetField(log, "qvar", i) background None xpadding 0.0 text_size 24
        if log.definedtab("Misc"):
            text "" size 18
            text "TASKS" size 30 font "BRLNSB.TTF"
            vbox:
                box_reverse True
                for i in log.definedtab("Misc"):
                    textbutton i.title() action SetField(log, "qvar", i) background None xpadding 0.0 text_size 24
        if log.definedtab("Completed"):
            text "" size 18
            text "COMPLETE" size 30 font "BRLNSB.TTF"
            vbox:
                box_reverse True
                for i in log.definedtab("Completed"):
                    textbutton i.title() action SetField(log, "qvar", i) background None xpadding 0.0 text_size 24

    vbox xysize (700, 50) pos (1135,200):



        text log.activetitle() font "BRLNSB.TTF" size 42

    vbox xysize (700,300) pos (1135,275):

        text log.activedescription() size 24





    vbox xsize 950 pos (875,620):
        hbox:
            textbutton "Objectives" action SetVariable("quest_objectives_button", True) text_style "quest_obj_stat"
            textbutton "Stats" action SetVariable("quest_objectives_button", False) text_style "quest_obj_stat"

    if quest_objectives_button:
        vbox xsize 950 pos (875,700) spacing 5:

            for i in log.activeprogress():
                hbox xpos 10:
                    add formatgoal(i)[1] yoffset 4
                    text formatgoal(i)[0] size 24 xoffset 10
    else:

        use qlog_questlog_stats(log.active_qstats())

screen qlog_questlog_stats(quest):
    hbox xsize 900 pos (880,700):
        hbox:
            vbox:
                text "Handjobs:" size 24
                text "Blowjobs:" size 24
                text "• Swallowed:" size 24
                text "• Facials:" size 24
                text "• On body:" size 24
            vbox:
                xsize 30
            vbox:
                text str(quest.hsex) size 24
                text str(quest.osex) size 24
                text str(quest.swallow) size 24
                text str(quest.facial) size 24
                text str(quest.buk) size 24
            vbox:
                xsize 30
        hbox:
            vbox:
                text "Vaginal sex:" size 24
                text "Creampies:" size 24
                text "• Safe:" size 24
                text "• Normal:" size 24
                text "• Risky:" size 24
                text "Anal sex:" size 24
                text "• Anal creampies:" size 24
            vbox:
                xsize 30
            vbox:
                text str(quest.vsex) size 24
                text str(quest.creamvag) size 24
                text str(quest.creamsafe) size 24
                text str(quest.creamnormal) size 24
                text str(quest.creamdanger) size 24
                text str(quest.asex) size 24
                text str(quest.creamanal) size 24
            vbox:
                xsize 30
        hbox:
            vbox:
                text "Bought me:" size 24
                text "• Cash made:" size 24
                text "Assaulted:" size 24
                text "Forced:" size 24
                text "" size 24
                text "Pregnant:" size 24
                text "• Babies:" size 24

            vbox:
                xsize 30
            vbox:
                text str(quest.sold) size 24
                text "£{}".format(quest.soldpricetotal) size 24
                text str(quest.assault) size 24
                text str(quest.rape) size 24
                text "" size 24
                text str(quest.preg) size 24
                text str(quest.pregbabies) size 24

            vbox:
                xsize 30

image notification_img:
    align (0.5, 0.25)

    alpha 0.0
    Text(log.message())
    linear 0.5 alpha 1.0
    pause 2.0
    linear 0.5 alpha 0.0











screen notification:
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.20)
        text str.upper(log.message()) size 40 font "BRLNSB.TTF" align (0.5, 0.20)
    timer 3 action Hide ('notification')


screen stat_popup(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.25)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.25)
    timer 3 action Hide ('stat_popup')

screen inv_popup(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.30)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.30)
    timer 3 action Hide ('inv_popup')

screen inv_popup2(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.35)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.35)
    timer 3 action Hide ('inv_popup2')

screen inv_popup3(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.40)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.40)
    timer 3 action Hide ('inv_popup3')



screen notif_popup_0(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.25)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.25)
    timer 3 action Hide ('notif_popup_0')

screen notif_popup_1(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.30)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.30)
    timer 3 action Hide ('notif_popup_1')

screen notif_popup_2(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.35)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.35)
    timer 3 action Hide ('notif_popup_2')

screen notif_popup_3(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.40)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.40)
    timer 3 action Hide ('notif_popup_3')

screen notif_popup_4(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.45)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.45)
    timer 3 action Hide ('notif_popup_4')

screen notif_popup_5(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.50)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.50)
    timer 3 action Hide ('notif_popup_5')

screen notif_popup_6(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.55)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.55)
    timer 3 action Hide ('notif_popup_6')

screen notif_popup_7(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.60)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.60)
    timer 3 action Hide ('notif_popup_7')

screen notif_popup_8(message):
    modal False
    zorder 6
    frame at notification_transform:
        background None
        add "notif_bg" align (0.5, 0.65)
        text str.upper(message) size 40 font "BRLNSB.TTF" align (0.5, 0.65)
    timer 3 action Hide ('notif_popup_8')

init -1:
    transform notification_transform:
        on show:
            align (0.5, 0.25)
            alpha 0

            linear 0.5 alpha 1.0
            pause 2.0
            linear 0.5 alpha 0.0







init python:




    def formatgoal(goal):
        str = ''
        img = ''
        if not goal.hidden():
            if goal.completed():
                img = "ui/quest_icon_full.webp"
                str = "{0}".format(goal.description())
            else:
                img = "ui/quest_icon_empty.webp"
                if goal.fetch():
                    str = "{0}  {1}/{2}".format(goal.description(), goal.have(), goal.need())
                else:
                    str = "{0}".format(goal.description())
        else:
            if goal.required():
                str = "?????"
        
        return (str, img)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
