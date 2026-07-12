# ai_config_screens.rpy - Экраны для тегов комфорта, локаций, фракций, spicy - с управлением автоматизацией

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
                    text "0=запрет 1=мягко 2=разрешить 3=ЖЕЛАЕМО (упор)" size 12 color "#888"
                    text "После настройки level=3 открой кнопку «Portrait» в HUB." size 11 color "#666" xalign 1.0
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
                            # Цвет фона: level=3 (желаемо) — розовый, 1-2 — синий, 0 — тёмно-красный.
                            if _tag_level >= 3:
                                _bg = "#3a1a3a"
                            elif _tag_level > 0:
                                _bg = "#1a2a3a"
                            else:
                                _bg = "#2a1a1a"
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
                                    for lvl in [0,1,2,3]:
                                        python:
                                            # Активная кнопка розовая; для 3 (желаемо) — ярко-жёлтая, чтобы отличать от «просто разрешить».
                                            if _tag_level == lvl and lvl == 3:
                                                _btn_bg = "#ffaa22"
                                            elif _tag_level == lvl:
                                                _btn_bg = "#ff44aa"
                                            else:
                                                _btn_bg = "#2a2a4a"
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
        xsize 620 ysize 680
        background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#3a1a3a" xfill True ysize 60
                hbox:
                    xfill True
                    text "Настройки Spicy и Автоматизации ИИ" size 18 bold True color "#ff88ff"
                    textbutton "X" action Return() xalign 1.0
            frame:
                background "#1a1a2a" xfill True yfill True
                viewport:
                    scrollbars "vertical" mousewheel True
                    vbox:
                        spacing 15
                        xfill True
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
                        
                        text "Шанс Spicy NSFW: [_chance]%%" size 16 bold True color "#ff88cc"
                        text "Текущий накопительный метр: [_meter]%%" size 12 color "#aaa"
                        text "Всего квестов: [_total], из них spicy: [_spicy]" size 11 color "#888"
                        
                        bar:
                            value ai_spicy_meter
                            range 100
                            xsize 500 ysize 15
                            left_bar Solid("#ff44aa")
                            right_bar Solid("#333")
                        
                        hbox:
                            spacing 10
                            textbutton "Сброс 20%" action SetVariable("ai_spicy_meter", 20) background "#2a2a4a"
                            textbutton "+20" action SetVariable("ai_spicy_meter", min(80, ai_spicy_meter+20)) background "#3a2a4a"
                            textbutton "-20" action SetVariable("ai_spicy_meter", max(0, ai_spicy_meter-20)) background "#3a1a1a"
                        
                        text "После спокойного +20 к шансу, после spicy -40. Ночь, высокая фем, коррапт, пляж/бар повышают шанс." size 11 color "#aaa"
                        
                        # Новая секция настроек автоматизации
                        null height 10
                        frame:
                            background "#221a35" xfill True ysize 3
                        null height 5
                        
                        text "Автоматизация Систем ИИ (Без дебаг кнопок)" size 15 bold True color "#88ffaa"
                        
                        hbox:
                            spacing 15
                            text "Автоматические события:" size 13 color "#ccc"
                            textbutton "[ai_auto_events_enabled]" action ToggleVariable("ai_auto_events_enabled") background "#2a2a4a"
                        
                        hbox:
                            spacing 15
                            text "Шанс авто-событий при переходе:" size 13 color "#ccc"
                            textbutton "-5%" action SetVariable("ai_auto_event_chance", max(5, ai_auto_event_chance-5)) background "#3a1a1a"
                            text "[ai_auto_event_chance]%" size 13 bold True color "#ffaa44"
                            textbutton "+5%" action SetVariable("ai_auto_event_chance", min(95, ai_auto_event_chance+5)) background "#1a3a2a"
                        
                        hbox:
                            spacing 15
                            text "Автоматические SMS:" size 13 color "#ccc"
                            textbutton "[ai_auto_sms_enabled]" action ToggleVariable("ai_auto_sms_enabled") background "#2a2a4a"
                        
                        text "События и SMS генерируются заранее в фоновом потоке Ollama и срабатывают мгновенно и бесшовно во время игры, сохраняя полное погружение!" size 11 color "#888" italic True
                        text "Файл настроек: ai_config_spicy.rpy" size 11 color "#666"

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

# =====================================================================
# PLAYER EMOTIONAL PORTRAIT
# ---------------------------------------------------------------------
# Экран для формирования «эмоционального портрета» игрока. Игрок:
#   1) в ai_comfort_tags_screen ставит level=3 у тем, которые для него
#      ЖЕЛАЕМЫ (не просто разрешены).
#   2) на этом экране пишет свободным текстом «чего я хочу от игры»
#      (стилистику, кинки, эмоциональный тон, любимые фетиши, табу и т.д.).
#   3) жмёт «Сформировать портрет» — уходит LLM-запрос, ответ пишется в
#      player_portrait.txt в корне игры (config.basedir).
# После этого КАЖДЫЙ квестовый промпт получает этот портрет отдельной
# строкой [PLAYER PORTRAIT] в контексте. Пользователь может открыть файл
# в блокноте и править вручную — движок читает файл заново перед каждым
# квестом.
# =====================================================================

default ai_portrait_input_text = ""
default ai_portrait_last_summary = ""
default ai_portrait_generating = False

screen ai_portrait_screen():
    modal True
    zorder 3000
    add Solid("#000000cc")
    frame:
        xalign 0.5 yalign 0.5
        xsize 900 ysize 660
        background "#12121a"
        vbox:
            xfill True yfill True spacing 6
            frame:
                background "#3a1a4a" xfill True ysize 60
                hbox:
                    xfill True
                    vbox:
                        text "Эмоциональный портрет игрока" size 18 bold True color "#ff88cc"
                        text "Файл: player_portrait.txt (в папке игры) — можно править руками" size 10 color "#ddb"
                    textbutton "X" action Return() xalign 1.0

            # Секция 1: список «желаемых» (level=3) тегов
            frame:
                background "#1a1a2a" xfill True ysize 130
                vbox:
                    spacing 4
                    text "Твои ЖЕЛАЕМЫЕ темы (level=3):" size 13 bold True color "#ffaa22"
                    python:
                        try:
                            _wish = [t for t in AI_COMFORT_TAGS if int(t.get('level',0)) >= 3]
                            _wish_names = [t.get('name', t.get('id','?')) for t in _wish]
                            _wish_line_raw = u", ".join(_wish_names) if _wish_names else u"(ни одного — поставь 3 в списке тегов)"
                            _wish_line = ai_escape_renpy_text(_wish_line_raw)
                        except Exception as _e:
                            _wish_line = u"(ошибка чтения тегов)"
                    text "[_wish_line]" size 11 color "#ddd"

            # Секция 2: свободный текст
            # В Ren'Py 7.5.x у input НЕТ multiline — пришлось делать
            # однострочный ввод с большой длиной. Для длинного/многострочного
            # портрета проще открыть player_portrait.txt в блокноте.
            frame:
                background "#1a1a2a" xfill True ysize 150
                vbox:
                    spacing 4
                    text "Опиши своими словами, чего ты хочешь от игры:" size 13 bold True color "#88ff88"
                    text "Тон, стилистика, любимые кинки, эмоциональные акценты, желаемые последствия, табу." size 10 color "#888"
                    text "(Enter = подтвердить. Для длинного текста удобнее править player_portrait.txt в блокноте.)" size 9 color "#666"
                    frame:
                        background "#0a0a14" xsize 830 ysize 60
                        input:
                            value VariableInputValue("ai_portrait_input_text")
                            length 800
                            xsize 810
                            color "#fff"
                            size 13

            # Секция 3: кнопки
            hbox:
                spacing 15 xalign 0.5
                textbutton "Сформировать портрет" action Function(ai_start_player_portrait_thread) background "#3a2a5a" text_size 14 sensitive (not ai_portrait_generating)
                textbutton "Загрузить из файла" action [Function(ai_reload_player_portrait_from_file), Function(renpy.restart_interaction)] background "#2a3a4a" text_size 13
                textbutton "Очистить" action [SetVariable("ai_portrait_input_text", ""), SetVariable("ai_portrait_last_summary", ""), Function(ai_clear_player_portrait_file)] background "#3a1a1a" text_size 13

            if ai_portrait_generating:
                text "⏳ Генерирую портрет… может занять 10-30 сек." size 12 color "#ffaa44" xalign 0.5

            # Секция 4: последний summary
            frame:
                background "#0f1225" xfill True yfill True
                viewport:
                    scrollbars "vertical" mousewheel True
                    vbox:
                        spacing 4
                        text "Текущий портрет (что уходит в промпт квестов):" size 12 bold True color "#88ccff"
                        python:
                            try:
                                _portrait_display = ai_escape_renpy_text(ai_portrait_last_summary) if ai_portrait_last_summary else u"(пусто — нажми «Сформировать» или отредактируй файл вручную)"
                            except Exception:
                                _portrait_display = u"(ошибка отображения)"
                        text "[_portrait_display]" size 12 color "#ddd" xsize 830

label ai_portrait_open:
    python:
        # При открытии загружаем последний сохранённый портрет из файла.
        try:
            ai_reload_player_portrait_from_file()
        except Exception as e:
            print("ai_portrait_open reload err: %s" % e)
    call screen ai_portrait_screen
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
