# ai_config_screens.rpy - Экраны для тегов комфорта, локаций, фракций, spicy - без ошибок синтаксиса

screen ai_comfort_tags_screen():
    modal True
    zorder 3000
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 800 ysize 700
        background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#2a1a3a" xfill True ysize 60
                hbox:
                    xfill True
                    text "Теги комфорта - выбери что ок" size 18 bold True color "#ff88cc"
                    textbutton "X" action Return() xalign 1.0
            frame:
                background "#1a1a2a" xfill True ysize 40
                hbox:
                    spacing 20
                    text "0=запрет 1=мягко 2=разрешить" size 12 color "#888"
                    text "Файл: ai_config_tags.rpy" size 11 color "#666" xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 6
                    for tag in AI_COMFORT_TAGS:
                        python:
                            _tag_name = tag.get('name','')
                            _tag_id = tag.get('id','')
                            _tag_desc = tag.get('desc','')
                            _tag_level = tag.get('level',0)
                            _bg = "#1a2a3a" if _tag_level>0 else "#2a1a1a"
                        frame:
                            background _bg
                            xfill True
                            hbox:
                                xfill True spacing 10
                                vbox:
                                    xsize 400
                                    text "[_tag_name] ([_tag_id])" size 13 bold True
                                    text "[_tag_desc]" size 10 color "#aaa"
                                hbox:
                                    spacing 5
                                    xalign 1.0
                                    for lvl in [0,1,2]:
                                        python:
                                            _btn_bg = "#2a2a4a" if _tag_level!=lvl else "#ff44aa"
                                        textbutton "[lvl]" action [SetDict(tag,'level',lvl), Function(renpy.restart_interaction)] background _btn_bg text_size 12 xsize 30
                    null height 20
                    text "Как добавлять свои теги: открой game/ai_config_tags.rpy и добавь id/name/desc/level" size 11 color "#666"
                    text "Теги фильтруют ивенты. Если запрещен - ивент не покажется." size 11 color "#888"

screen ai_location_themes_screen():
    modal True
    zorder 3000
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 850 ysize 700
        background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#1a3a2a" xfill True ysize 60
                hbox:
                    xfill True
                    vbox:
                        text "Темы по локациям" size 18 bold True color "#88ff88"
                        text "Файл: ai_config_locations.rpy" size 10 color "#aaa"
                    textbutton "X" action Return() xalign 1.0
            frame:
                background "#1a2a4a" xfill True ysize 30
                text "Все локации игры - смотри AI_ALL_LOCATIONS" size 11 color "#888"
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 8
                    for loc in AI_ALL_LOCATIONS:
                        python:
                            try:
                                allowed = ai_get_allowed_themes_for_location(loc)
                                allowed_str = ", ".join(allowed[:8])
                                if len(allowed)>8:
                                    allowed_str += "..."
                                if not allowed:
                                    allowed_str = "все разрешенные глобально"
                            except:
                                allowed_str = "ошибка"
                        frame:
                            background "#1a2a3a"
                            xfill True
                            vbox:
                                text "[loc]" size 12 bold True color "#aaffaa"
                                text "Разрешено: [allowed_str]" size 10 color "#aaa"
                    null height 10
                    text "Чтобы запретить тему в локации: в AI_LOCATION_THEMES[\"beach\"] добавь [\"!violence\"]" size 11 color "#666"

screen ai_factions_screen():
    modal True
    zorder 3000
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 800 ysize 700
        background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#3a1a1a" xfill True ysize 60
                hbox:
                    xfill True
                    text "Фракции Blaston" size 18 bold True color "#ffaaaa"
                    textbutton "X" action Return() xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for fid, fdata in AI_FACTIONS.items():
                        python:
                            try:
                                rep = ai_get_faction_rep(fid)
                            except:
                                rep = fdata.get('reputation',0)
                            _f_name = fdata.get('name','?')
                            _rep_color = "#ffaaaa" if rep<0 else "#aaffaa"
                            _bg = "#2a1a2a" if rep>=0 else "#1a2a2a"
                        frame:
                            background _bg
                            xfill True
                            vbox:
                                hbox:
                                    xfill True
                                    text "[_f_name] (%s)" % fid size 14 bold True color _rep_color
                                    text "Rep: %s" % rep size 12 color "#ffaa44" xalign 1.0
                                text fdata.get('desc','') size 11 color "#ccc"
                                hbox:
                                    spacing 10
                                    textbutton "-10" action Function(ai_add_faction_rep, fid, -10) background "#3a1a1a"
                                    textbutton "+10" action Function(ai_add_faction_rep, fid, 10) background "#1a3a2a"
                    text "Файл: ai_config_factions.rpy - добавляй свои группировки" size 11 color "#666"

screen ai_spicy_config_screen():
    modal True
    zorder 3000
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 600 ysize 500
        background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#3a1a3a" xfill True ysize 60
                hbox:
                    xfill True
                    text "Spicy Meter" size 18 bold True color "#ff88ff"
                    textbutton "X" action Return() xalign 1.0
            frame:
                background "#1a1a2a" xfill True yfill True
                vbox:
                    spacing 15
                    python:
                        try:
                            _chance = ai_get_spicy_chance()
                            _meter = ai_spicy_meter
                            _total = ai_total_quests
                            _spicy = ai_total_spicy_quests
                        except:
                            _chance = 20
                            _meter = 20
                            _total = 0
                            _spicy = 0
                    text "Шанс spicy: [_chance]%%" size 16 bold True color "#ff88cc"
                    text "Метр: [_meter]%%" size 14 color "#aaa"
                    text "Всего квестов: [_total], spicy: [_spicy]" size 12 color "#888"
                    bar:
                        value ai_spicy_meter
                        range 100
                        xsize 500 ysize 20
                        left_bar Solid("#ff44aa")
                        right_bar Solid("#333")
                    hbox:
                        spacing 10
                        textbutton "Сброс 20%" action SetVariable("ai_spicy_meter", 20) background "#2a2a4a"
                        textbutton "+20" action SetVariable("ai_spicy_meter", min(80, ai_spicy_meter+20)) background "#3a2a4a"
                        textbutton "-20" action SetVariable("ai_spicy_meter", max(0, ai_spicy_meter-20)) background "#3a1a1a"
                    text "После спокойного +20 к шансу, после spicy -40. Ночь, высокая фем, коррапт, beach/pub/haven повышают шанс." size 12 color "#aaa"
                    text "Файл: ai_config_spicy.rpy" size 11 color "#666"

# Labels to open config screens
label ai_comfort_open:
    call screen ai_comfort_tags_screen
    return

label ai_locations_open:
    call screen ai_location_themes_screen
    return

label ai_factions_open:
    call screen ai_factions_screen
    return

label ai_spicy_open:
    call screen ai_spicy_config_screen
    return

label ai_debug_locations:
    python:
        try:
            from ai_config_locations import AI_ALL_LOCATIONS
            msg = "Все локации (%s): %s..." % (len(AI_ALL_LOCATIONS), ", ".join(AI_ALL_LOCATIONS[:15]))
            renpy.notify(msg)
            print(msg)
            for loc in AI_ALL_LOCATIONS:
                print(loc)
        except Exception as e:
            renpy.notify("Ошибка дебага: %s" % e)
    return
