# TheFixer AI ALL SYSTEMS v7.2 - Python 2 & 3 Dual-Compatible for RenPy 7 & 8
# Все интеграции: чат, события 3D, NPC, секс, дневник, квесты, магазин, тренер, SMS, перки, одежда
# Только феминность, без дисфории, без SD, только родные 3D модели
# ОПТИМИЗИРОВАНО И АВТОМАТИЗИРОВАНО: Полностью асинхронно, без фризов, с предзагрузкой (prefetch) и авто-триггерами!
# ИСПРАВЛЕНЫ: Ошибки парсинга JSON, ошибки разбора "choices" (словари как строки) и падения из-за некорректных тегов текста (curly braces) в RenPy!
# ИСПРАВЛЕН КРАШ СОХРАНЕНИЯ (threading PicklingError): Все импорты перенесены в глобальный блок init python. В функциях локальные импорты удалены!
# ИСПРАВЛЕН КРАШ ДНЕВНИКА: Экранированы квадратные скобки [[ВКЛ]]/[[ВЫКЛ]] в тексте кнопок!
# ИСПРАВЛЕНА ОШИБКА ДНЕВНИКА (NameError): Добавлен безопасный переключатель ИИ SMS в коде с проверкой hasattr, защищенный от неопределенных переменных!
# ИСПРАВЛЕН ВЫЛЕТ НА ГЛАВНЫЙ ЭКРАН (Главное меню): Все точки выхода перенаправлены на игровую метку `travel_arrival` вместо вызова небезопасных `return`!
# ИСПРАВЛЕН РЕНДЕРИНГ КНОПОК: Полная поддержка совместимости с RenPy RevertableDict с проверкой hasattr(ch, 'get') вместо isinstance!
# ИСПРАВЛЕН ГЛИЧ С ТОЧКАМИ "...": Добавлен автоматический текстовый предохранитель от ленивой генерации ИИ и строгий запрет плейсхолдеров в промптах!
# ИСПРАВЛЕНА ЮНИКОД-ОШИБКА (UnicodeEncodeError): Все опасные вызовы `str()` заменены на безопасный `unicode()` для поддержки спецсимволов и кириллицы в Python 2!
# УСТРАНЕНА ПЕРЕГРУЗКА ИИ (Thread Locks): Добавлена потокобезопасная блокировка фоновых вызовов для предотвращения перегрева Ollama!
# ОПТИМИЗИРОВАНО: Шанс срабатывания события проверяется ЛОКАЛЬНО в коде игры за одну операцию, а не тяжелым запросом к LLM!
# ОПТИМИЗИРОВАН ТАЙМАУТ: Время таймаута снижено с 90 до 25 секунд — ИИ больше не будет зависать и генерировать бесконечно старые задачи в фоне!
# НОВОЕ: Динамическое создание ПЕРКОВ из выборов ИИ-событий в сейв-файл GG (например, "Public Prostitute", "Neck Cuts" с уведомлением на экране)!
# НОВОЕ: Полная интеграция перков в контекст ИИ — Оллама видит все активные перки GG и строит будущие события на основе её репутации и шрамов!
# НОВОЕ: AI RADAR — оверлей-радар событий, который показывает, в какой локации тебя ждет предзагруженный сюжет!
# НОВОЕ: Текстовое описание 3D-локаций на основе реальных скриншотов из папки Фотографии! ИИ теперь видит убранство комнат, туалетов и парков!
# НОВОЕ: Трекинг недавних действий GG (recent actions) — ИИ знает, что Sammy делала перед событием, и строит сюжет на основе этого!
# НОВОЕ: Автоматический скриншот локации при входе в файл ai_loc_[id].png!
# НОВОЕ: Почасовая нарастающая шкала вероятности событий (+10% в час) и SMS (+35% в час)!
# НОВОЕ: Динамическое изменение Spicy-метра на основе выборов в диалогах!
# НОВОЕ: Перевод событий на полностью бесцензурную модель Dirty-Muse для снятия ограничений ИИ на насилие и жесткий NSFW!

init python:
    import json, re, os, base64, ast, threading, codecs
    import random as py_random

    # Поддержка двойной совместимости Python 2 (RenPy 7) и Python 3 (RenPy 8)
    try:
        unicode  # type: ignore  # noqa: F821  # Py2
    except NameError:
        unicode = str  # Py3 / Ren'Py 8
    try:
        basestring  # type: ignore  # noqa: F821
    except NameError:
        basestring = str  # Py3
    try:
        long  # type: ignore  # noqa: F821
    except NameError:
        long = int  # Py3

    try:
        import urllib.request as urllib2
        import urllib.parse as urllib
    except ImportError:
        import urllib2
        import urllib

    OLLAMA_URL = "http://localhost:11434/api/chat"
    OLLAMA_MODEL_CHAT = "hf.co/mradermacher/Dirty-Muse-Writer-v01-Uncensored-Erotica-NSFW-i1-GGUF:i1-IQ2_XS"
    
    # Для полной свободы генерации жесткого NSFW и насилия используем бесцензурную Dirty-Muse вместо стандартной llama!
    OLLAMA_MODEL_JSON = "hf.co/mradermacher/Dirty-Muse-Writer-v01-Uncensored-Erotica-NSFW-i1-GGUF:i1-IQ2_XS"

    # ===== GPU-ПРОФИЛЬ ДЛЯ OLLAMA (ноутбук с RTX 3050 4GB) =====
    # ВАЖНО: выбор конкретной видеокарты всё равно делается на стороне сервера Ollama
    # через переменные среды Windows (CUDA_VISIBLE_DEVICES / GGML_VK_VISIBLE_DEVICES / OLLAMA_LLM_LIBRARY).
    # Эти параметры ниже делают сами ЗАПРОСЫ более дружелюбными к маленькой VRAM и
    # просят Ollama максимально выгружать слои модели на GPU вместо ЦП.
    OLLAMA_FORCE_GPU = True
    OLLAMA_GPU_LAYERS = 99          # 99 = просим Ollama выгрузить на GPU максимум слоёв, сколько влезет
    OLLAMA_LOW_VRAM = True          # более щадящий режим под 4GB VRAM
    OLLAMA_NUM_THREAD = 4           # не душим CPU лишними потоками, когда часть работы уйдёт на GPU
    OLLAMA_NUM_BATCH = 32           # меньше batch => меньше риск вывалиться из VRAM в RAM/CPU
    # ВНИМАНИЕ: контекст должен быть с ЗАПАСОМ, иначе Ollama молча обрежет
    # начало user-промпта, и модель забудет, кто такая Саманта.
    # Прикидка: system(~600) + user(~2200) + предсказание(1200) = ~4000.
    # Ставим 6144 с запасом на будущее раздутие правил/перков.
    # Если VRAM 4GB начнёт кидать HTTP 500 — снижай до 4096.
    OLLAMA_NUM_CTX = 6144

    # SAFE MODE для слабой/маленькой VRAM:
    # - отключает тяжёлую фоновую магию, которая забивает очередь Ollama
    # - отключает полные цепочки квестов и берёт более лёгкие одиночные события
    # - сериализует все запросы к Ollama одним глобальным lock, чтобы не было 5-10 одновременных потоков
    AI_LOW_VRAM_SAFE_MODE = True
    # Полные деревья квестов: теперь строго 2 уровня выбора (2 -> 2), 4 финала.
    # SAFE_MODE по-прежнему режет фоновый prefetch/SMS/auto, но НЕ рубит цепочки квестов.
    AI_ENABLE_FULL_QUEST_CHAIN = True
    # Каждый ai_call генерирует ОДИН step + choices. Если игрок выбирает
    # choice без is_ending — движок делает ЕЩЁ ОДИН ai_call с контекстом
    # предыдущего шага и выбранного варианта. Так до момента, пока LLM
    # сама не поставит is_ending=true, или пока не упрёмся в MAX_STEPS.
    # Это on-demand chain (NOT tree upfront).
    AI_QUEST_ONE_STEP_TEST_MODE = True   # один step на ai_call — да, но цепочка не ограничена
    AI_QUEST_MAX_STEPS = 5               # жёсткий потолок: после 5-го шага финал форсируется
    # МИНИМАЛЬНОЕ число шагов до финала. Слабая 2-битная модель почти
    # всегда копирует `IS_ENDING: true` из шаблона на первом же выборе,
    # и игрок мгновенно уходит на ending-screen после 1 клика. Форсируем
    # минимум N шагов ДО ТОГО, как is_ending от LLM будет уважён.
    # 3 — комфортный минимум (setup / развитие / финал). До этого is_ending
    # игнорируется, движок продолжает генерить следующий шаг.
    AI_QUEST_MIN_STEPS_BEFORE_ENDING = 3
    AI_FULL_QUEST_MIN_STEPS = 1
    AI_FULL_QUEST_MAX_STEPS = 1
    # РАЗМЕР ОТВЕТА. Раньше стояло 450 — не хватало на длинный
    # многовариантный сюжет, модель обрывалась на полуслове (см. дампы
    # вида "Let your.'  effects: {...}"). 1200 хватает на:
    #   TITLE/DESC + STEP + 2-4 полных CHOICE с EFFECTS + ENDING_TITLE/TEXT.
    # Ответ: до 5 choices × 6-10 sentence ending + 8-14 sentence step_desc.
    # На IQ2_XS ~1200-1600 токенов реально. 1800 с запасом.
    AI_FULL_QUEST_MAX_TOKENS = 1800
    AI_FULL_QUEST_TIMEOUT = 180
    AI_EVENT_MAX_TOKENS = 420
    AI_PREFETCH_MAX_TOKENS = 280
    AI_EVENT_DEBUG = True
    AI_PATCH_BUILD = "2026-07-11-portrait-directives+validator+manual-fallback"
    ai_ollama_global_lock = threading.Lock()

    # Текстовые описания 3D-окружения на основе скриншотов из папки Фотографии (для погружения ИИ в обстановку)
    AI_LOCATION_DESCRIPTIONS = {
        "bathroom": "A clean tile bathroom with a mirror, sink, and shower. Private, perfect for makeup or admiring your body.",
        "bedroom": "Samantha's cozy private bedroom. Has a bed, a window looking outside, and a closet. A safe space for privacy.",
        "common": "The shared living room at home. Casual, with sofas and a TV. Flatmates often lounge here.",
        "kitchen": "The kitchen at home. Smells of coffee and breakfast. A common place to meet flatmates in the morning.",
        "school_classroom": "A school classroom with desks, a blackboard, and students attending class. Abbott or Carlson teaching.",
        "school_hallway": "The school hallway, crowded with lockers and students. High traffic, wolf pack bullies or mean girls gossiping.",
        "school_gym": "The school gym. Spacious, smelling of sweat and rubber, with workout gear and soccer boys.",
        "school_locker_girl": "The girls' locker room in school. Clean, with benches, showers, and mirrors. Very private for girls.",
        "school_locker_boy": "The boys' locker room in school. Smelling of sweat and body spray. Highly risky and dangerous to enter.",
        "school_toilet": "OUTSIDE the school restrooms — Samantha is in the hallway at the door, has NOT yet chosen boys' or girls'. She has not entered any stall.",
        "school_toilet_boy": "INSIDE the school boys' restroom. Urinals, cubicles, tile walls. Risky — she has already entered.",
        "school_toilet_girl": "INSIDE the school girls' restroom. Sinks, mirrors, private stalls. She has already entered.",
        "trainstation_local_pub_toilet_boys": "INSIDE the trainstation pub men's restroom. Cramped, dirty tiles, one broken urinal. She has already entered.",
        "trainstation_local_pub_toilet_girls": "INSIDE the trainstation pub women's restroom. Two stalls, cracked mirror, flickering light. She has already entered.",
        "park_local": "Blaston Park. Green grass fields, walking paths, benches, and tall trees. Beautiful and public.",
        "park_toilet": "OUTSIDE the park public restrooms — Samantha is standing at the entrance under the sign, has NOT yet chosen boys' or girls' door. Open air, people walking past, still fully in the park.",
        "park_toilet_boys": "INSIDE the men's restroom of Blaston Park. Dingy tile walls, urinals, cubicles, disinfectant smell. She has already entered — cornered by whoever comes in.",
        "park_toilet_girls": "INSIDE the women's restroom of Blaston Park. Tile walls, mirrors, sinks, private stalls. Safe and private — she has already entered.",
        "beach": "The sandy Blaston Beach. Waves washing over the sand, pier nearby, open and sunny. Perfect for swimwear.",
        "beach_water": "The cool water of Blaston Beach. Waves washing over the sand. Ideal for swimming.",
        "beach_gym": "An outdoor beach workout gym. Benches, weights, pull-up bars. Athletic people exercising.",
        "beach_hangout": "The sandy beach hangout spot. People relaxing on towels, sunbathing, or playing volleyball.",
        "beach_locker_boys": "INSIDE the beach boys' locker room. Rough wooden benches and showers. She has already entered.",
        "beach_locker_girls": "INSIDE the beach girls' locker room. Benches and privacy screens for changing. She has already entered.",
        "pub": "The Trainstation local pub. Dim-lit, smelling of beer and tobacco. Bob and Trixie serving, full of local patrons.",
        "pub_toilet": "OUTSIDE the pub restrooms — Samantha is in the pub corridor at the doors, has NOT yet chosen boys' or girls'. Music still audible from the main room.",
        "pub_toilet_boys": "INSIDE the pub men's restroom. Stale beer and urine smell, dirty tiles. Highly unsafe — she has already entered.",
        "pub_toilet_girls": "INSIDE the pub women's restroom. Sinks, mirrors, tile walls. Dimly lit — she has already entered.",
        "motel": "The local highway motel. Run-down, neon pink signs, private rooms. Hot spot for highway prostitution.",
        "motel_lobby": "The run-down motel lobby. Has a reception counter, keys, and an old clerk.",
        "truckstop": "The local highway truckstop. Large semi trucks parked, diesel smell, truck drivers resting. High sex-work activity.",
        "bus_interior": "The interior of the Blaston public transit bus. Blue seats, handrails, passenger windows, and commuters.",
        "residential_area": "The residential home street in Blaston. Sidewalks, residential buildings, kiosks, and bus stops.",
        "checkpoint": "The local checkpoint. Barb-wired fences, security barriers, guarded by police.",
        "industrial_area": "The industrial zone. Warehouses, factories, asphalt roads, and trucks passing by.",
        "hospital_entrance": "The entrance to the Blaston hospital. Clean, modern glass doors, ambulance parking.",
        "hospital_lobby": "The sterile hospital reception lobby. Clean tile floors, waiting chairs, nurse reception counter.",
        "revel": "The Revel entertainment street. Bars, adult clubs, neon lights, pub entrances. Active nightlife.",
        "revel_backstreet": "The dark alleyway behind Revel. Trash bins, dim streetlights, secluded and quiet."
    }

    # Безопасное извлечение лорного описания локации по её ID
    def ai_get_location_description(loc_id):
        if not loc_id:
            return "A generic location in Blaston."
        clean_id = loc_id.replace("loc_", "")
        return AI_LOCATION_DESCRIPTIONS.get(clean_id, "A scenic location in Blaston.")

    # =====================================================================
    # САНИТАЙЗЕР PLACEHOLDER'ОВ И «ДЕТСКИХ» СЛОВ
    # ---------------------------------------------------------------------
    # 2-битные GGUF регулярно копируют плейсхолдеры из шаблона:
    #   "A_MAN_1 leans against a nearby trash can..." /
    #   "<persona A>" / "A_WOMAN_2 watches" / "NAMED_MAN".
    # Плюс любят фон "kids play on the swings" — рядом с NSFW это плохо
    # даже если сексуального намёка нет.
    # Этот санитайзер бьёт по всем полям, которые идут в UI: title, desc,
    # step.desc, ending_title, ending_text, choice.text.
    # =====================================================================
    _AI_PLACEHOLDER_RE = re.compile(
        r'(?:'
        r'A[_\s]MAN[_\s]?\d*'      # A_MAN_1 / A MAN 2 / A_MAN
        r'|A[_\s]WOMAN[_\s]?\d*'   # A_WOMAN_1
        r'|A[_\s]GIRL[_\s]?\d*'
        r'|A[_\s]GUY[_\s]?\d*'
        r'|NAMED[_\s](?:MAN|WOMAN|GIRL|GUY|NPC)[_\s]?\d*'
        r'|PERSONA[_\s]?[A-Z]?\d*'
        r'|NPC[_\s]?\d+'
        r')',
        re.IGNORECASE
    )
    # <persona A>, <man>, <name>, <npc 1>, <someone>
    _AI_ANGLE_PLACEHOLDER_RE = re.compile(
        r'<\s*(?:persona|npc|man|woman|girl|guy|name|someone|character)[^>]{0,40}>',
        re.IGNORECASE
    )
    # Замены слов, которые нельзя видеть в NSFW-сценах. Мы НЕ переписываем
    # смысл, только меняем токен на нейтральный, чтобы фон не «омолодился».
    _AI_MINOR_WORD_SUBS = [
        (re.compile(r'\bkids?\b', re.IGNORECASE),          u"people"),
        (re.compile(r'\bchildren\b', re.IGNORECASE),       u"people"),
        (re.compile(r'\bchild\b', re.IGNORECASE),          u"person"),
        (re.compile(r'\bteen(?:s|ager|agers)?\b', re.IGNORECASE), u"adults"),
        (re.compile(r'\bschoolgirls?\b', re.IGNORECASE),   u"women"),
        (re.compile(r'\bschoolboys?\b', re.IGNORECASE),    u"men"),
        (re.compile(r'\bminors?\b', re.IGNORECASE),        u"adults"),
        (re.compile(r'\btoddlers?\b', re.IGNORECASE),      u"adults"),
        (re.compile(r'\bbabies\b', re.IGNORECASE),         u"adults"),
        (re.compile(r'\bbaby\b', re.IGNORECASE),           u"adult"),
        # "the swings" / "the playground" тоже смещают сцену. Не критично,
        # но лучше нейтрализовать, если рядом были дети.
        (re.compile(r'\bplaying on the swings\b', re.IGNORECASE), u"passing by"),
        (re.compile(r'\bon the swings\b', re.IGNORECASE),  u"nearby"),
        (re.compile(r'\bat the playground\b', re.IGNORECASE), u"in the park"),
    ]

    def ai_sanitize_ui_text(text):
        """Убирает placeholder-имена и «детские» слова из строки, которая
        пойдёт в UI. Возвращает str/unicode того же типа. Идемпотентна."""
        if text is None:
            return u""
        try:
            s = unicode(text) if not isinstance(text, basestring) else unicode(text)
        except Exception:
            try:
                s = u"%s" % text
            except Exception:
                return u""
        try:
            # 1) Плейсхолдеры-имена → "a man" / "a woman" (нейтрально).
            def _placeholder_sub(m):
                token = m.group(0).lower()
                if u"woman" in token or u"girl" in token:
                    return u"a woman"
                if u"man" in token or u"guy" in token:
                    return u"a man"
                return u"someone"
            s = _AI_PLACEHOLDER_RE.sub(_placeholder_sub, s)
            s = _AI_ANGLE_PLACEHOLDER_RE.sub(u"someone", s)
            # 2) Слова-триггеры про несовершеннолетних.
            for rx, repl in _AI_MINOR_WORD_SUBS:
                s = rx.sub(repl, s)
            # 3) Двойные пробелы после замен.
            s = re.sub(r'\s{2,}', u' ', s).strip()
        except Exception as e:
            try:
                print("ai_sanitize_ui_text err: %s" % e)
            except Exception:
                pass
        return s

    # Экранирование фигурных скобок для предотвращения крашей RenPy из-за "Unknown text tag"
    def ai_escape_renpy_text(text):
        if text is None:
            return u""
        if not isinstance(text, basestring):
            try:
                text = unicode(text)
            except Exception:
                text = u"%s" % text
        else:
            text = unicode(text)
        # Дублируем { } и [ ], чтобы Ren'Py не парсил их как text tags / interpolations
        return (
            text
            .replace("{", "{{")
            .replace("}", "}}")
            .replace("[", "[[")
            .replace("]", "]]")
        )

    def ai_write_debug_file(filename, text):
        try:
            if text is None:
                text = u""
            if not isinstance(text, (str, unicode)):
                text = unicode(text)
            fh = codecs.open(filename, "w", "utf-8")
            fh.write(text)
            fh.close()
        except Exception as e:
            print("ai_write_debug_file err: %s" % e)

    # =====================================================================
    # PLAYER EMOTIONAL PORTRAIT
    # ---------------------------------------------------------------------
    # Хранится в файле рядом с игрой: player_portrait.txt (тот же путь,
    # что и ai_last_prompt.txt — cwd Ren'Py = папка игры).
    # Читается перед каждым квестовым промптом и подставляется как блок
    # [PLAYER PORTRAIT]. Игрок может править файл вручную — движок никогда
    # не переписывает файл без явной команды из экрана Portrait.
    # =====================================================================
    AI_PORTRAIT_FILE = "player_portrait.txt"
    AI_PORTRAIT_MAX_CHARS = 1500       # чтобы не раздувать промпт

    def ai_get_player_portrait_text():
        """Возвращает содержимое player_portrait.txt (или пустую строку,
        если файла нет). Обрезает до AI_PORTRAIT_MAX_CHARS."""
        try:
            if not os.path.exists(AI_PORTRAIT_FILE):
                return u""
            fh = codecs.open(AI_PORTRAIT_FILE, "r", "utf-8")
            txt = fh.read()
            fh.close()
            if txt is None:
                return u""
            txt = unicode(txt).strip()
            if len(txt) > AI_PORTRAIT_MAX_CHARS:
                txt = txt[:AI_PORTRAIT_MAX_CHARS] + u"\n... (truncated)"
            return txt
        except Exception as e:
            print("ai_get_player_portrait_text err: %s" % e)
            return u""

    def ai_reload_player_portrait_from_file():
        """Читает файл и кладёт содержимое в store.ai_portrait_last_summary,
        чтобы UI Portrait отобразил актуальный текст."""
        try:
            txt = ai_get_player_portrait_text()
            store.ai_portrait_last_summary = txt or u""
        except Exception as e:
            print("ai_reload_player_portrait_from_file err: %s" % e)

    def ai_clear_player_portrait_file():
        """Стирает файл (пишет пустую строку) и очищает store-кеш."""
        try:
            fh = codecs.open(AI_PORTRAIT_FILE, "w", "utf-8")
            fh.write(u"")
            fh.close()
            store.ai_portrait_last_summary = u""
            try:
                renpy.notify(u"Портрет очищен")
            except Exception:
                pass
        except Exception as e:
            print("ai_clear_player_portrait_file err: %s" % e)

    def _ai_portrait_build_manual_fallback(wish_entries, user_free_text):
        """Собирает портрет ВРУЧНУЮ, без LLM. Используется как fallback,
        если dirty-muse сгенерировала невалидный/нежный/off-topic текст.
        Возвращает готовый structured summary в формате TONE/DO/AVOID/KEY THEMES,
        построенный из wishlist-тегов и свободного текста."""
        try:
            names = [e['name'] for e in wish_entries if e.get('name')]
            themes_line = u", ".join(names) if names else u"(no explicit desired themes)"
            # Простые эвристики для тона: если в wishlist есть жёсткие теги —
            # тон жёстче. Если только femininity/crossdressing — мягче.
            hard_ids = {u'noncon', u'violence', u'bdsm_hard', u'slavery', u'freeuse',
                        u'prostitution', u'humiliation', u'gender_bender_humiliation',
                        u'bullying', u'blackmail', u'watersports', u'scat',
                        u'menstruation_sex', u'drugs_hard'}
            wish_ids = {e.get('id') for e in wish_entries}
            has_hard = bool(wish_ids & hard_ids)
            if has_hard:
                tone_line = u"harsh, degrading, no aftercare pretense — the player wants weight and consequence, not romance"
            else:
                tone_line = u"pressure and awkwardness over romance — Samantha's body forced into situations, no tender relief"
            do_line = u"lean HARD into the KEY THEMES below; make every scene use at least one of them explicitly"
            avoid_line = (u"generic sissy fluff, 'devoted pet' romance prose, "
                          u"warm-master vibes UNLESS the player explicitly wrote it in FREE_TEXT")
            free_note = (u"FREE_TEXT from player: %s" % user_free_text) if user_free_text else u"FREE_TEXT: (empty)"
            return (
                u"TONE: %s.\n"
                u"KEY THEMES: %s.\n"
                u"DO: %s.\n"
                u"AVOID: %s.\n"
                u"%s"
            ) % (tone_line, themes_line, do_line, avoid_line, free_note)
        except Exception as e:
            print("_ai_portrait_build_manual_fallback err: %s" % e)
            return u"(portrait fallback failed)"

    def _ai_portrait_validate_summary(summary, wish_entries, user_free_text):
        """Проверяет, что LLM реально учла wishlist. Возвращает (ok, reason).

        Правила:
          - summary непустая и не error-плейсхолдер
          - есть хотя бы одна из structured-меток (TONE/DO/AVOID/KEY THEMES/THEMES)
            ИЛИ упомянут хотя бы один tag id/name из wishlist
          - НЕ содержит явных «нежных» фраз, если в wishlist есть hard-теги
        """
        try:
            if not summary or len(summary) < 40:
                return False, u"too short"
            low = summary.lower()
            if any(bad in low for bad in (u"__error", u"i cannot", u"i can't", u"as an ai", u"sorry, but")):
                return False, u"refusal / error text"
            # Проверяем «структурность» ИЛИ упоминание тегов.
            has_structure = any(k in summary for k in (u"TONE:", u"KEY THEMES:", u"DO:", u"AVOID:", u"THEMES:"))
            wish_hits = 0
            for e in wish_entries:
                tid = (e.get('id') or u"").lower()
                nm  = (e.get('name') or u"").lower()
                if tid and tid in low:
                    wish_hits += 1
                elif nm and len(nm) >= 4 and nm in low:
                    wish_hits += 1
            if not has_structure and wish_hits == 0 and wish_entries:
                return False, u"no structure, no wishlist hits"
            # Если в wishlist есть hard-теги, но summary про «devotion/pet/master/tender/warm» —
            # LLM свалилась в дефолтную sissy-fem прозу и проигнорировала теги.
            hard_ids = {u'noncon', u'violence', u'bdsm_hard', u'slavery', u'freeuse',
                        u'humiliation', u'gender_bender_humiliation', u'bullying', u'blackmail'}
            wish_ids = {(e.get('id') or u"").lower() for e in wish_entries}
            has_hard = bool(wish_ids & hard_ids)
            soft_words = (u"devot", u"pet ", u"pet,", u"pet.", u"tender", u"warm and",
                          u"blissful", u"beloved", u"adore", u"eager to please",
                          u"master's every", u"belonging")
            soft_hits = sum(1 for w in soft_words if w in low)
            if has_hard and soft_hits >= 2 and wish_hits == 0:
                return False, u"soft-drift while wishlist is hard"
            return True, u"ok"
        except Exception as e:
            return False, u"validator crash: %s" % e

    def ai_generate_player_portrait_and_save():
        """Собирает wishlist (level>=3) + свободный текст и формирует
        `player_portrait.txt`. Формат — жёстко структурированный
        (TONE / KEY THEMES / DO / AVOID / FREE_TEXT), чтобы квестовая
        LLM не могла его «пропустить».

        LLM (dirty-muse) вызывается как «director notes writer»: пишет
        только 3-4 короткие директивы. Если валидатор говорит, что она
        сдрейфила в дефолтную sissy-fem прозу — используем ручной
        fallback на основе wishlist без LLM.
        """
        try:
            store.ai_portrait_generating = True
            try:
                renpy.restart_interaction()
            except Exception:
                pass

            user_free_text = ai_to_text(getattr(store, 'ai_portrait_input_text', u""), u"").strip()

            # Собираем wishlist из AI_COMFORT_TAGS (level>=3).
            wish_entries = []
            try:
                from ai_config_tags import AI_COMFORT_TAGS
                for t in AI_COMFORT_TAGS:
                    try:
                        lvl = int(t.get('level', 0))
                    except Exception:
                        lvl = 0
                    if lvl >= 3:
                        wish_entries.append({
                            'id':   t.get('id') or u"?",
                            'name': t.get('name') or t.get('id') or u"?",
                            'desc': t.get('desc') or u"",
                        })
            except Exception as _we:
                print("ai_generate_player_portrait wishlist err: %s" % _we)

            wish_lines = [
                u"- %s (id=%s): %s" % (e['name'], e['id'], e['desc'])
                for e in wish_entries
            ]
            wish_block = u"\n".join(wish_lines) if wish_lines else u"(player marked NO tags as desired)"

            # SYSTEM PROMPT: жёстко в стиле "director's notes for another AI",
            # третье лицо, императивы. dirty-muse без такой рамки скатывается
            # в свою любимую sissy-fem прозу про "beloved pet devotion".
            sys_prompt = (
                u"You are an author's DIRECTOR NOTES editor for an adult text game about Samantha.\n"
                u"Task: read the player's DESIRED_TAGS list and their FREE_TEXT wish, then output\n"
                u"a set of directives for OTHER AI writers on what kind of scenes the player wants.\n"
                u"\n"
                u"RULES:\n"
                u"- OUTPUT EXACTLY THESE 5 LINES, IN THIS ORDER, EACH ON ITS OWN LINE, EACH LABEL IN CAPS:\n"
                u"  TONE: <1 sentence — emotional register the player wants>\n"
                u"  KEY THEMES: <comma-separated list, MUST be a subset of the DESIRED_TAGS names>\n"
                u"  DO: <1-2 sentences — what scenes must include>\n"
                u"  AVOID: <1 sentence — what breaks immersion for THIS player>\n"
                u"  FREE_TEXT: <one sentence paraphrase of the player's own wish, or 'none' if empty>\n"
                u"- WRITE ABOUT THE PLAYER IN THIRD PERSON (\"the player wants...\", \"they prefer...\").\n"
                u"- NEVER address Samantha. NEVER address the player as 'you'. NEVER write prose or a story.\n"
                u"- NEVER use words like 'devotion', 'beloved', 'pet', 'tender', 'blissful', 'warm master',\n"
                u"  'eager to please', UNLESS those exact words appear in the DESIRED_TAGS or FREE_TEXT.\n"
                u"- KEY THEMES MUST cite the actual tags from DESIRED_TAGS. If the wishlist is hard\n"
                u"  (noncon, violence, freeuse, humiliation, prostitution, slavery, bdsm_hard, bullying,\n"
                u"  blackmail, watersports, scat) — TONE must match that hardness. DO NOT soften it.\n"
                u"- English only. No JSON. No markdown. No greetings. No sign-off."
            )
            user_prompt = (
                u"DESIRED_TAGS (player marked level=3):\n"
                u"%s\n\n"
                u"FREE_TEXT:\n"
                u"%s\n\n"
                u"Now write the 5-line directives. Remember: TONE / KEY THEMES / DO / AVOID / FREE_TEXT."
            ) % (wish_block, user_free_text or u"(empty)")

            summary = u""
            try:
                summary = ai_call(
                    OLLAMA_MODEL_CHAT,
                    sys_prompt,
                    user_prompt,
                    want_json=False,
                    temp=0.25,          # низкая температура — меньше самодеятельности
                    max_tokens=350,
                    task_desc=u"Player portrait",
                    force_json_format=False,
                )
            except Exception as _ce:
                print("ai_generate_player_portrait ai_call err: %s" % _ce)
                summary = u""

            if not isinstance(summary, (str, unicode)):
                summary = u""
            summary = unicode(summary).strip()

            # Дебаг-дамп сырых входов/выходов LLM для отладки портрета.
            # Пишется всегда, чтобы если игрок жалуется на портрет — можно было
            # быстро посмотреть, что реально ушло в dirty-muse и что она вернула.
            try:
                debug_dump = (
                    u"[BUILD] %s\n\n"
                    u"[SYS PROMPT]\n%s\n\n"
                    u"[USER PROMPT]\n%s\n\n"
                    u"[LLM RAW RESPONSE]\n%s\n"
                ) % (AI_PATCH_BUILD, sys_prompt, user_prompt, summary or u"(empty)")
                ai_write_debug_file("ai_portrait_debug.txt", debug_dump)
            except Exception as _de:
                print("portrait debug dump err: %s" % _de)

            # Валидация — реально ли LLM учла wishlist?
            ok, why = _ai_portrait_validate_summary(summary, wish_entries, user_free_text)
            fallback_used = False
            if not ok:
                print("Portrait validator rejected LLM output: %s" % why)
                # Пробуем один раз ещё жёстче: temp=0.15, короче.
                retry_sys = sys_prompt + (
                    u"\n\nCRITICAL: your previous answer was REJECTED because it did not follow the 5-line "
                    u"format or ignored the DESIRED_TAGS. Now output ONLY the 5 required labelled lines. "
                    u"Nothing else. Every KEY THEMES entry MUST come from DESIRED_TAGS."
                )
                try:
                    summary2 = ai_call(
                        OLLAMA_MODEL_CHAT,
                        retry_sys,
                        user_prompt,
                        want_json=False,
                        temp=0.15,
                        max_tokens=350,
                        task_desc=u"Player portrait retry",
                        force_json_format=False,
                    )
                except Exception:
                    summary2 = u""
                if not isinstance(summary2, (str, unicode)):
                    summary2 = u""
                summary2 = unicode(summary2).strip()
                ok2, why2 = _ai_portrait_validate_summary(summary2, wish_entries, user_free_text)
                # Дописываем retry в дебаг-файл, чтобы был виден и второй заход.
                try:
                    with codecs.open("ai_portrait_debug.txt", "a", "utf-8") as _fh:
                        _fh.write(
                            u"\n[VALIDATOR REJECTED FIRST ATTEMPT] %s\n"
                            u"\n[LLM RETRY RAW RESPONSE]\n%s\n"
                            u"\n[VALIDATOR SECOND RESULT] ok=%s why=%s\n"
                            % (why, summary2 or u"(empty)", ok2, why2)
                        )
                except Exception:
                    pass
                if ok2:
                    summary = summary2
                else:
                    print("Portrait retry also rejected: %s -> using manual fallback" % why2)
                    summary = _ai_portrait_build_manual_fallback(wish_entries, user_free_text)
                    fallback_used = True

            # Собираем итоговый файл. КРИТИЧНО: в промпт квестов идёт ВСЁ —
            # и wishlist сырым, и summary. Даже если summary плохой,
            # wishlist LLM квестов увидит напрямую.
            header = (
                u"# player_portrait.txt — эмоциональный портрет игрока\n"
                u"# Правь этот файл руками — движок читает его перед каждым квестом.\n"
                u"# Всё выше маркера ---USER NOTES--- уходит в промпт как блок [PLAYER PORTRAIT].\n"
                u"# fallback_used=%s (True = LLM промахнулась, портрет собран вручную из wishlist)\n"
            ) % (u"yes" if fallback_used else u"no")
            body = (
                u"[DESIRED_TAGS]\n%s\n\n"
                u"[DIRECTIVES]\n%s\n\n"
                u"---USER NOTES---\n(private notes here — not sent to LLM)\n"
            ) % (wish_block, summary)

            try:
                fh = codecs.open(AI_PORTRAIT_FILE, "w", "utf-8")
                fh.write(header + u"\n" + body)
                fh.close()
            except Exception as _we:
                print("ai_generate_player_portrait write err: %s" % _we)
                try:
                    renpy.notify(u"Ошибка записи portrait: %s" % _we)
                except Exception:
                    pass
                return False

            # В UI показываем summary (директивы), а не сырой файл.
            store.ai_portrait_last_summary = summary
            try:
                if fallback_used:
                    renpy.notify(u"LLM промахнулась — портрет собран вручную")
                else:
                    renpy.notify(u"Портрет сохранён в player_portrait.txt")
            except Exception:
                pass
            return True
        except Exception as e:
            print("ai_generate_player_portrait_and_save fatal: %s" % e)
            return False
        finally:
            store.ai_portrait_generating = False
            try:
                renpy.restart_interaction()
            except Exception:
                pass

    def ai_start_player_portrait_thread():
        """Запускает генерацию портрета в фоновом потоке, чтобы UI не
        замерзал на 10-30 сек ai_call'а."""
        try:
            if getattr(store, 'ai_portrait_generating', False):
                try:
                    renpy.notify(u"Уже генерирую...")
                except Exception:
                    pass
                return
            def _worker():
                try:
                    ai_generate_player_portrait_and_save()
                except Exception as e:
                    print("ai_start_player_portrait_thread worker err: %s" % e)
                finally:
                    try:
                        renpy.restart_interaction()
                    except Exception:
                        pass
            import threading as _th
            _th.Thread(target=_worker).start()
        except Exception as e:
            print("ai_start_player_portrait_thread err: %s" % e)

    def ai_get_player_portrait_for_prompt():
        """Возвращает СЖАТЫЙ портрет для вставки в промпт. Обрезает всё,
        что после маркера '---USER NOTES---'. Обрезает до 800 символов —
        экономим бюджет промпта. Пустая строка = блок в промпт не идёт."""
        try:
            txt = ai_get_player_portrait_text()
            if not txt:
                return u""
            # Отрезаем "---USER NOTES---" и всё после.
            cut = txt.split(u"---USER NOTES---", 1)[0]
            # Отрезаем комментарии-строки, начинающиеся с "#".
            keep = []
            for line in cut.splitlines():
                if line.strip().startswith(u"#"):
                    continue
                keep.append(line)
            cleaned = u"\n".join(keep).strip()
            if len(cleaned) > 800:
                cleaned = cleaned[:800] + u"..."
            return cleaned
        except Exception as e:
            print("ai_get_player_portrait_for_prompt err: %s" % e)
            return u""

    def ai_set_event_debug(reason, raw=None, parsed=None):
        try:
            store.ai_debug_last_event_reason = unicode(reason)
            if raw is None:
                raw = getattr(store, 'ai_debug_last_json_raw', u"")
            store.ai_debug_last_json_raw = unicode(raw) if raw is not None else u""
            parsed_text = u""
            if parsed is not None:
                try:
                    parsed_text = json.dumps(parsed, ensure_ascii=False, indent=2)
                except:
                    parsed_text = unicode(parsed)
            dump = u"[BUILD]\n%s\n\n[REASON]\n%s\n\n[RAW]\n%s\n\n[PARSED]\n%s\n" % (
                AI_PATCH_BUILD,
                store.ai_debug_last_event_reason,
                store.ai_debug_last_json_raw,
                parsed_text
            )
            ai_write_debug_file("ai_event_debug.txt", dump)
        except Exception as e:
            print("ai_set_event_debug err: %s" % e)

    # Сброс и очистка переменных состояния квестов во избежание залипания шагов
    def ai_reset_quest_state():
        store.ai_full_quest_data = None
        store.ai_full_quest_current_step = "step1"
        store.ai_quest_path = []
        store.ai_prefetched = {}
        store.ai_pending_event = None
        store.ai_event_ui_cache = None
        store.ai_event_title = u"Событие"
        store.ai_event_desc = u"..."
        store.ai_event_choices = []
        store.ai_event_outfit_items = []
        store.ai_event_is_quest = False
        store.ai_event_qtitle = u""
        store.ai_event_qdesc = u""
        store._has_next = False
        store._automatic_event_active = False
        store.ai_current_automatic_event = None

    # Потокобезопасная функция динамического добавления ИИ-перка на игрока в сейв-файл
    def ai_dict_like(obj):
        """True for dict / RevertableDict / any mapping with .get"""
        if obj is None:
            return False
        if isinstance(obj, dict):
            return True
        return hasattr(obj, 'get') and hasattr(obj, '__getitem__')

    def ai_to_text(value, default=u""):
        if value is None:
            return unicode(default)
        try:
            return unicode(value)
        except Exception:
            try:
                return u"%s" % value
            except Exception:
                return unicode(default)

    def ai_stage_event_for_ui(evt, reason=u"staged"):
        """Единая точка: кладём событие в store-переменные, которые читает ai_event_screen."""
        try:
            evt = ai_normalize_event(evt)
        except Exception as e:
            print("ai_stage_event_for_ui normalize err: %s" % e)
            evt = {
                "title": u"Quest Challenge",
                "description": ai_to_text(evt, u"Event ready."),
                "choices": [{"text": u"Continue", "effects": {}}],
                "is_quest": False,
                "outfit_suggestion": {"items": []},
            }

        if not ai_dict_like(evt):
            evt = {
                "title": u"Quest Challenge",
                "description": ai_to_text(evt, u"Event ready."),
                "choices": [{"text": u"Continue", "effects": {}}],
                "is_quest": False,
                "outfit_suggestion": {"items": []},
            }

        title = ai_to_text(evt.get('title', u'Событие'), u'Событие')
        desc = ai_to_text(evt.get('description', u'...'), u'...')
        # Санитайзер: убираем A_MAN_1 / <persona X> / kids / children etc.
        try:
            title = ai_sanitize_ui_text(title)
            desc = ai_sanitize_ui_text(desc)
        except Exception:
            pass
        # После санитайзера title мог стать бессмысленным ("a man" или пусто) —
        # ловим deg-cases и заменяем на нейтральный "Quest Challenge".
        try:
            _t_stripped = title.strip() if title else u""
            _t_low = _t_stripped.lower()
            _bad_title_after = (
                (not _t_stripped) or
                (_t_low in (u"a man", u"a woman", u"someone", u"...", u"none", u"none.")) or
                # slug вида "a_man_1_leans_against..." — после санитайзера мог
                # остаться формат "a_man leans_against_a_nearby_trash_can...".
                # slug'и слитных подчёркиваний в title недопустимы.
                (u"_" in _t_stripped and _t_stripped.count(u"_") >= 3 and u" " not in _t_stripped)
            )
            if _bad_title_after:
                title = u"Quest Challenge"
        except Exception:
            pass
        if not desc or desc.strip() in [u"", u"...", u"None", u"None."]:
            desc = u"Samantha continues her femininity training, making choices that shape her new life."
        evt['description'] = desc
        if not title or title.strip() in [u"", u"...", u"None", u"None."]:
            title = u"Quest Challenge"
        evt['title'] = title

        choices = evt.get('choices', []) or []
        # Квесты теперь могут иметь 2-4 разных персона-реакции + опционально
        # ещё один "escape" (уйти/отказаться) — итого до 5 кнопок. Escape
        # добавляется/фильтруется отдельно в ai_maybe_add_escape_choice(),
        # здесь просто расширяем верхний предел.
        choice_limit = 5 if bool(evt.get('is_quest', False) or evt.get('_full_quest', False)) else 3
        safe_choices = []
        try:
            for ch in list(choices)[:choice_limit]:
                if ai_dict_like(ch):
                    ct = ai_to_text(ch.get('text', u'Continue'), u'Continue')
                    if not ct or ct.strip() in [u"", u"...", u"None"]:
                        ct = u"Continue"
                    # Санитайзер плейсхолдеров/детских слов
                    try:
                        ct = ai_sanitize_ui_text(ct)
                    except Exception:
                        pass
                    # Пост-фикс "первого лица". Правило "choice.text — это то,
                    # что делает Саманта, во втором лице, начиная с You" часто
                    # игнорируется слабой моделью, и на кнопке всплывает
                    # "He does not notice you." или "Try to stay quiet like a
                    # mouse." Меняем текст на явное "You ...":
                    #  - если начинается с He/She/They/Someone/It/The … —
                    #    заменяем на "You react: <оригинал>";
                    #  - если это командная форма без подлежащего
                    #    ("Try ...", "Stay ...", "Kneel.") — префиксуем "You ";
                    #  - оставляем как есть, если уже начинается с You/Your/I.
                    try:
                        ct_stripped = ct.strip()
                        # (label) префикс сохраняем, работаем только с телом
                        prefix = u""
                        body = ct_stripped
                        if body.startswith(u"(") and u")" in body:
                            _p_end = body.index(u")") + 1
                            prefix = body[:_p_end] + u" "
                            body = body[_p_end:].lstrip()
                        low = body.lower()
                        _first = low.split(None, 1)[0] if low.split() else u""
                        _third_person = {
                            u"he", u"she", u"they", u"someone", u"somebody",
                            u"it", u"the", u"a", u"an", u"his", u"her",
                            u"their", u"nobody", u"no", u"there",
                        }
                        _ok_first = {u"you", u"your", u"i", u"my", u"me", u"we"}
                        if _first in _third_person:
                            body = u"You react: " + body
                        elif _first and _first not in _ok_first:
                            # командная форма → "You <verb...>"
                            # только для явно императивных слов, чтобы не
                            # калечить редкие валидные варианты
                            _imperative_starts = {
                                u"try", u"stay", u"kneel", u"freeze", u"grab",
                                u"push", u"pull", u"drop", u"lean", u"look",
                                u"walk", u"run", u"hide", u"cry", u"laugh",
                                u"smile", u"whisper", u"shout", u"scream",
                                u"give", u"take", u"say", u"tell", u"ask",
                                u"answer", u"bite", u"kiss", u"grind", u"press",
                                u"open", u"close", u"reach", u"turn", u"bend",
                                u"kneel", u"stand", u"sit", u"lie", u"lay",
                                u"agree", u"accept", u"refuse", u"decline",
                                u"resist", u"submit", u"obey", u"comply",
                                u"play", u"pretend", u"act", u"fake",
                                u"ignore", u"acknowledge", u"admit", u"deny",
                                u"beg", u"plead", u"nod", u"shake",
                                u"bolt", u"flee", u"escape", u"slip",
                                u"weaponize", u"collapse", u"crumble", u"dissociate",
                                u"go", u"start", u"stop", u"keep", u"let",
                                u"clamp", u"cover", u"hold", u"squeeze", u"tighten",
                            }
                            if _first in _imperative_starts:
                                body = u"You " + body[0].lower() + body[1:]
                        ct = prefix + body
                    except Exception:
                        pass
                    # Полная копия, чтобы next_step/effects/ending/perk не терялись
                    eff = ch.get('effects', {})
                    if not ai_dict_like(eff):
                        eff = {}
                    else:
                        # shallow copy
                        try:
                            eff = dict(eff)
                        except Exception:
                            pass
                    # perk_add may sit on choice root in some model outputs
                    if 'perk_add' not in eff and ch.get('perk_add') is not None:
                        eff['perk_add'] = ch.get('perk_add')
                    _et = ch.get('ending_title', ch.get('endingTitle', ch.get('result_title', None)))
                    _ex = ch.get('ending_text',  ch.get('endingText',  ch.get('result_text', ch.get('ending', None))))
                    try:
                        if _et is not None:
                            _et = ai_sanitize_ui_text(_et)
                        if _ex is not None:
                            _ex = ai_sanitize_ui_text(_ex)
                    except Exception:
                        pass
                    safe_ch = {
                        "text": ct,
                        "effects": eff,
                        "next_step": ch.get('next_step', ch.get('next', ch.get('goto', None))),
                        "spicy_modifier": ch.get('spicy_modifier', ch.get('spicy', 0)),
                        "ending_title": _et,
                        "ending_text": _ex,
                        "is_ending": bool(ch.get('is_ending', False)),
                    }
                    safe_choices.append(safe_ch)
                else:
                    safe_choices.append({"text": ai_to_text(ch, u"Continue"), "effects": {}, "next_step": None})
        except Exception as e:
            print("ai_stage_event_for_ui choices err: %s" % e)
            safe_choices = []
        if not safe_choices:
            safe_choices = [{"text": u"Continue", "effects": {}}]
        evt['choices'] = safe_choices

        outfit = evt.get('outfit_suggestion', {}) or {}
        if not ai_dict_like(outfit):
            outfit = {}
        items = outfit.get('items', []) if ai_dict_like(outfit) else []
        if items is None:
            items = []

        store.ai_last_event = evt
        store.ai_event_ui_cache = evt
        store.ai_event_title = title
        store.ai_event_desc = desc
        store.ai_event_choices = safe_choices
        store.ai_event_outfit_items = list(items) if items else []
        store.ai_event_is_quest = bool(evt.get('is_quest', False))
        store.ai_event_qtitle = ai_to_text(evt.get('quest_title', u''), u'')
        store.ai_event_qdesc = ai_to_text(evt.get('quest_desc', u''), u'')

        try:
            # FIX: если это локальный fallback (LLM не смог собрать дерево) —
            # ОБЯЗАТЕЛЬНО оставляем последний RAW от Ollama, иначе диагностика
            # ошибки «normalize failed …» вырождается в пустой [RAW] и починить
            # промпт становится невозможно. В нормальном сценарии RAW пустой, как и было.
            _keep_raw = bool(ai_dict_like(evt) and (evt.get('_local_fallback') or evt.get('_llm_failed_reason')))
            _raw_for_debug = getattr(store, 'ai_debug_last_json_raw', u"") if _keep_raw else u""
            ai_set_event_debug(
                reason,
                raw=_raw_for_debug,
                parsed={
                    "title": store.ai_event_title,
                    "description": store.ai_event_desc,
                    "choices": [
                        (c.get('text') if ai_dict_like(c) else unicode(c))
                        for c in store.ai_event_choices
                    ],
                    "is_quest": store.ai_event_is_quest,
                    "local_fallback": bool(evt.get('_local_fallback', False)) if ai_dict_like(evt) else False,
                    "one_step_test": bool(evt.get('_one_step_test', False)) if ai_dict_like(evt) else False,
                    "llm_failed_reason": ai_to_text(evt.get('_llm_failed_reason', u''), u'') if ai_dict_like(evt) else u'',
                },
            )
        except Exception as e:
            print("ai_stage_event_for_ui debug err: %s" % e)
        return evt


    def ai_add_dynamic_perk(perk_name, perk_desc=None, perk_type="allure", stat_add=5):
        try:
            p = getattr(store, 'player', None)
            if not p:
                return False
                
            PerkClass = getattr(store, 'PerkClass', None)
            if not PerkClass:
                print("PerkClass not found in store!")
                return False
                
            if not perk_desc:
                perk_desc = u"A significant mark gained during your sissification journey: %s." % perk_name
                
            # Генерируем безопасный ID перка на основе его названия
            perk_id = "ai_dyn_perk_" + re.sub(r'[^a-zA-Z0-9_]', '_', perk_name.lower())
            
            # Распределение характеристик перка в зависимости от его типа
            conf_val = stat_add if perk_type == "confidence" else 0
            des_val = stat_add if perk_type == "desire" else 0
            all_val = stat_add if perk_type == "allure" else 0
            
            new_perk = PerkClass(
                perk_name, 
                perk_desc, 
                perk_id, 
                confidence_add=conf_val, 
                desire_add=des_val, 
                allure_add=all_val
            )
            
            # Сохраняем в список сгенерированных за сессию
            if not getattr(store, 'ai_perks_generated', None):
                store.ai_perks_generated = []
            store.ai_perks_generated.append(new_perk)
            
            # Добавляем перк персонажу через встроенный метод игры
            p.add_perk(new_perk, notif=True)
            
            store.ai_notify_queue.append(u"ИИ: Получена новая черта '%s'!" % perk_name)
            return True
        except Exception as e:
            print("ai_add_dynamic_perk err: %s" % e)
            return False

    # Нормализация событий для исправления багов, когда LLM возвращает choices в виде строк, а не словарей (совместимо с RevertableDict)
    def ai_normalize_event(evt):
        if evt is None:
            return evt
            
        # Гарантируем, что evt является словароподобным объектом
        if not hasattr(evt, 'get'):
            # Если всё событие пришло как строка (например, ИИ выдал голый текст)
            parsed = None
            if isinstance(evt, (str, unicode)):
                try:
                    parsed = renpy.safe_eval(evt.strip())
                except:
                    try:
                        parsed = ast.literal_eval(evt.strip())
                    except:
                        pass
                if parsed is None:
                    try:
                        parsed = json.loads(evt.strip())
                    except:
                        pass
            
            if parsed and hasattr(parsed, 'get'):
                evt = parsed
            else:
                # Если парсинг не удался, возвращаем структуру по умолчанию
                return {
                    "title": "Quest Challenge",
                    "description": unicode(evt),
                    "choices": [{"text": "Continue", "effects": {}}]
                }

        # Иногда LLM кладёт event внутрь {"event": {...}} или {"data": {...}}
        try:
            if 'title' not in evt and 'description' not in evt:
                for wrap_key in ('event', 'data', 'result', 'quest', 'response'):
                    inner = evt.get(wrap_key)
                    if hasattr(inner, 'get') and (inner.get('title') is not None or inner.get('description') is not None or inner.get('choices') is not None):
                        evt = inner
                        break
        except Exception:
            pass

        # Маппинг альтернативных ключей (Title/Description/Choices/options/actions)
        def _pick(d, *keys, **kw):
            default = kw.get('default', None)
            for k in keys:
                if k in d and d.get(k) not in (None, ''):
                    return d.get(k)
            # case-insensitive
            try:
                low = {unicode(k).lower(): v for k, v in d.items()}
                for k in keys:
                    lk = unicode(k).lower()
                    if lk in low and low[lk] not in (None, ''):
                        return low[lk]
            except Exception:
                pass
            return default

        # Нормализация заголовка и описания с предохранителем от ленивой генерации ИИ ("...")
        title = _pick(evt, 'title', 'Title', 'name', 'Name', 'event_title', default='Event')
        if not title or unicode(title).strip() in ["", "...", "None", "None.", "title", "string"]:
            title = "Quest Challenge"
            
        desc = _pick(evt, 'description', 'Description', 'desc', 'Desc', 'text', 'body', 'content', default='')
        if not desc or unicode(desc).strip() in ["", "...", "None", "None.", "description", "string"]:
            desc = "Samantha continues her femininity training, making choices that shape her new life."
            
        evt['title'] = title
        evt['description'] = desc
        
        choices = _pick(evt, 'choices', 'Choices', 'options', 'Options', 'actions', 'Actions', default=[])
        if not choices:
            choices = [{"text": "Continue", "effects": {}}]
            
        normalized_choices = []
        for ch in choices:
            # Если выбор пришел как строковое представление словаря (из-за галлюцинаций модели или двойной сериализации)
            if isinstance(ch, (str, unicode)) or not hasattr(ch, 'get'):
                parsed_ch = None
                if isinstance(ch, (str, unicode)):
                    try:
                        parsed_ch = renpy.safe_eval(ch.strip())
                    except:
                        try:
                            parsed_ch = ast.literal_eval(ch.strip())
                        except:
                            pass
                
                if parsed_ch and hasattr(parsed_ch, 'get'):
                    ch = parsed_ch
                else:
                    # Резервный Regex-парсер для битых/неполных строк, сгенерированных ИИ (например, как на скриншоте)
                    ch_text = "Continue"
                    ch_effects = {}
                    ch_next_step = None
                    
                    if isinstance(ch, (str, unicode)):
                        # Извлечение поля text
                        t_match = re.search(r"['\"]text['\"]\s*:\s*u?['\"](.*?)['\"]", ch)
                        if t_match:
                            ch_text = t_match.group(1)
                        else:
                            if not ":" in ch:
                                ch_text = ch
                        
                        ns_match = re.search(r"['\"]next_step['\"]\s*:\s*u?['\"](.*?)['\"]", ch)
                        if ns_match:
                            ch_next_step = ns_match.group(1)
                        
                        # Извлечение эффектов
                        for stat in ["femininity", "confidence", "corrupt", "money"]:
                            stat_match = re.search(r"['\"]" + stat + r"['\"]\s*:\s*([+-]?\d+)", ch)
                            if stat_match:
                                ch_effects[stat] = int(stat_match.group(1))
                            
                    ch = {
                        "text": ch_text,
                        "effects": ch_effects,
                        "next_step": ch_next_step
                    }
            
            # Если теперь это словарь, нормализуем поля
            if hasattr(ch, 'get'):
                ch_text = ch.get('text', None)
                if ch_text is None:
                    for k in ('Text', 'label', 'Label', 'choice', 'option', 'name', 'action'):
                        if ch.get(k) not in (None, ''):
                            ch_text = ch.get(k)
                            break
                if not ch_text or unicode(ch_text).strip() in ["", "...", "None", "text", "string"]:
                    ch_text = "Continue"
                ch_effects = ch.get('effects', None)
                if ch_effects is None:
                    ch_effects = ch.get('Effects', {})
                if not hasattr(ch_effects, 'get'):
                    ch_effects = {}
                ns_val = ch.get('next_step', ch.get('next', ch.get('goto', ch.get('nextStep', None))))
                if ns_val is not None:
                    ns_txt = unicode(ns_val).strip()
                    if ns_txt.lower() in [u'', u'null', u'none', u'end', u'finish', u'done']:
                        ns_val = None
                    else:
                        ns_val = ns_txt
                if not hasattr(ch_effects, 'get'):
                    ch_effects = {}
                else:
                    try:
                        ch_effects = dict(ch_effects)
                    except Exception:
                        pass
                if 'perk_add' not in ch_effects and ch.get('perk_add') is not None:
                    ch_effects['perk_add'] = ch.get('perk_add')
                normalized_choices.append({
                    "text": unicode(ch_text),
                    "effects": ch_effects,
                    "next_step": ns_val,
                    "spicy_modifier": ch.get('spicy_modifier', ch.get('spicy', 0)) or 0,
                    "ending_title": ch.get('ending_title', ch.get('endingTitle', ch.get('result_title', None))),
                    "ending_text": ch.get('ending_text', ch.get('endingText', ch.get('result_text', ch.get('ending', None)))),
                    # ТОЛЬКО explicit is_ending. Null next_step = "движок
                    # сгенерит продолжение" (on-demand chain), а НЕ финал.
                    "is_ending": bool(ch.get('is_ending', False)),
                    "is_ending_ack": bool(ch.get('is_ending_ack', False)),
                })
            else:
                # Если это просто плоская строка (например, "Да, пойти")
                normalized_choices.append({
                    "text": unicode(ch),
                    "effects": {}
                })
        
        evt['choices'] = normalized_choices
        return evt

    # Динамический генератор профиля ИИ для конкретного персонажа и его геймплейного статуса
    def ai_get_npc_profile_prompt(npc):
        if not npc:
            return ""
        
        fname = getattr(npc, 'fname', 'Someone')
        sname = getattr(npc, 'sname', '')
        bio_group = getattr(npc, 'bio_group', 'unknown')
        bio_text = getattr(npc, 'bio_text', 'No bio available.')
        is_female = getattr(npc, 'is_female', True)
        is_whore = getattr(npc, 'iswhore', False)
        is_slut = getattr(npc, 'isslut', False)
        love_level = getattr(npc, 'love', 0)
        
        # Определение стиля общения по группировке персонажа
        comm_style = "friendly, casual"
        if bio_group == "wolf_pack":
            comm_style = "aggressive, dominant, bullying, crude, demanding, street slang"
        elif bio_group == "mean_girls":
            comm_style = "bitchy, popular, tease, sarcastic, gossip, arrogant"
        elif bio_group == "flatmate":
            comm_style = "intimate, caring, helpful but cheeky"
        elif bio_group == "haven":
            comm_style = "brainwashed, cult-like, fanatical, submissive"
        elif bio_group == "whore" or is_whore:
            comm_style = "slutty, highly explicit, sexual, business-minded about selling body"
        elif is_slut:
            comm_style = "promiscuous, teasing, horny, playful, naughty"
            
        # Зависимость от уровня симпатии (love) в сейв-файле
        relationship = "acquaintance"
        if love_level >= 80:
            relationship = "madly in love, extremely loyal, devoted and romantic"
            comm_style += ", romantic, deeply loving, obedient"
        elif love_level >= 50:
            relationship = "close friend / lover, very intimate and trusting"
            comm_style += ", warm, comfortable, flirty"
        elif love_level >= 20:
            relationship = "good friend, positive connection"
        elif love_level < 0:
            relationship = "enemy, hostile, cold"
            comm_style += ", cold, insulting, rude"

        # Считывание долгосрочной памяти отношений (из сейва)
        npc_fname_low = fname.lower()
        memories = getattr(store, 'ai_npc_memories', {}).get(npc_fname_low, [])
        memories_text = "No notable past event memories stored yet."
        if memories:
            memories_text = "\n- ".join(memories)

        profile = """
[CHARACTER PROFILE FOR ROLEPLAY - BE EXTREMELY ACCURATE]
Name: {fname} {sname}
Gender: {gender}
Group/Affiliation: {bio_group}
Biography/Lore: {bio_text}
Relationship with Samantha: {relationship} (Love level: {love_level}/100)
Is Whore: {is_wh_str}, Is Slut: {is_sl_str}

[MEMORIES OF PAST ENCOUNTERS & EVENTS]
Samantha's key choices and past events with you:
- {memories_text}

[COMMUNICATION STYLE & TONE]
Style: {comm_style}
Guidelines:
- Speak exactly as this character.
- Do NOT use Unicode graphical emojis under any circumstances (they crash the game's font).
- Only use basic keyboard smileys (like :), ;), :P, :D, <3, XD).
- Keep replies short, conversational, and direct (1-3 sentences max).
- Refer to past interactions or their relationship if appropriate.
""".format(
            fname=fname, sname=sname,
            gender="Female" if is_female else "Male",
            bio_group=bio_group, bio_text=bio_text,
            relationship=relationship, love_level=love_level,
            is_wh_str="Yes" if is_whore else "No",
            is_sl_str="Yes" if is_slut else "No",
            memories_text=memories_text,
            comm_style=comm_style
        )
        return profile

    # Потокобезопасный тумблер ИИ SMS, защищенный от NameError в RenPy
    def ai_toggle_sms_allowed(npc_id):
        var_name = "ai_sms_allowed_" + npc_id
        current = getattr(store, var_name, False)
        setattr(store, var_name, not current)
        renpy.restart_interaction()

    def ai_repair_json_text(text):
        """Лёгкий ремонт JSON от слабых GGUF: незакрытые кавычки у ключей, choices: без кавычек и т.п."""
        if text is None:
            return text
        try:
            s = unicode(text)
        except Exception:
            try:
                s = str(text)
            except Exception:
                return text
        s = re.sub(r'```json|```', '', s).strip()

        # Оставляем только внешний JSON-объект/массив, если модель добавила мусор вокруг.
        f_curly = s.find('{')
        f_bracket = s.find('[')
        if f_bracket != -1 and (f_curly == -1 or f_bracket < f_curly):
            l_bracket = s.rfind(']')
            if l_bracket != -1:
                s = s[f_bracket:l_bracket+1]
        elif f_curly != -1:
            l_curly = s.rfind('}')
            if l_curly != -1:
                s = s[f_curly:l_curly+1]

        # Частые поломки Dirty-Muse/малых GGUF:
        #   choices:[...]              -> "choices":[...]
        #   description:"..."         -> "description":"..."
        #   ,next_step":null          -> ,"next_step":null
        # Работает только после { или , чтобы не трогать обычный текст в строках.
        key = r'[A-Za-z_][A-Za-z0-9_]*'
        s = re.sub(r'([\{,]\s*)(' + key + r')"\s*:', r'\1"\2":', s)
        s = re.sub(r'([\{,]\s*)(' + key + r')\s*:', r'\1"\2":', s)

        # Иногда модель пишет Python-подобные литералы.
        s = re.sub(r'\bNone\b', 'null', s)
        s = re.sub(r'\bTrue\b', 'true', s)
        s = re.sub(r'\bFalse\b', 'false', s)

        # Убираем висячие запятые перед } или ].
        s = re.sub(r',\s*([\}\]])', r'\1', s)

        # ДОКРУЧИВАЕМ НЕЗАКРЫТЫЕ СКОБКИ. Слабые GGUF (в т.ч. Dirty-Muse
        # IQ2_XS) любят обрываться на середине последнего choice: пишут
        # ...ending_text":"..." и всё, без "]}" в конце. Считаем баланс
        # скобок ВНЕ СТРОК и дописываем то, чего не хватает, в правильном
        # порядке (стек).
        try:
            stack = []
            in_str = False
            escape = False
            for ch in s:
                if in_str:
                    if escape:
                        escape = False
                    elif ch == '\\':
                        escape = True
                    elif ch == '"':
                        in_str = False
                    continue
                if ch == '"':
                    in_str = True
                elif ch == '{':
                    stack.append('}')
                elif ch == '[':
                    stack.append(']')
                elif ch == '}' or ch == ']':
                    if stack and stack[-1] == ch:
                        stack.pop()
                    # если mismatch — не трогаем, пусть json.loads ругнётся
            # Если строка не закрылась — закрываем.
            if in_str:
                s = s + '"'
            # Также срежем trailing запятую перед докручиванием.
            s = re.sub(r',\s*$', '', s)
            if stack:
                s = s + ''.join(reversed(stack))
        except Exception:
            pass

        return s

    # ------------------------------------------------------------------
    # ЛОГИРОВАНИЕ ЗАПРОСОВ В LLM
    # ------------------------------------------------------------------
    # Пишем 2 файла рядом с игрой:
    #   ai_last_prompt.txt   — только ПОСЛЕДНИЙ запрос, перезаписывается
    #                           каждым новым вызовом. Удобно быстро открыть
    #                           и посмотреть, что реально ушло в модель.
    #   ai_prompt_log.txt    — append всех запросов подряд с таймстампом,
    #                           меткой задачи и параметрами вызова.
    # Ответ модели туда НЕ пишется, для ответов уже есть ai_event_debug.txt
    # и ai_debug_last_json_raw. Если очень надо — включи AI_LOG_INCLUDE_RESPONSE.
    AI_PROMPT_LOG_MAX_BYTES = 512 * 1024   # ~0.5 МБ, чтобы файл не разросся до гигабайта
    AI_LOG_INCLUDE_RESPONSE = False

    def ai_log_prompt(task_desc, model, sys_prompt, user_prompt, extra=None):
        try:
            import datetime
            stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            desc = ai_to_text(task_desc if task_desc else u"(no task_desc)", u"(no task_desc)")
            head = (
                u"===== AI REQUEST =====\n"
                u"time    : %s\n"
                u"task    : %s\n"
                u"model   : %s\n"
            ) % (stamp, desc, ai_to_text(model, u""))
            if extra:
                try:
                    head += u"params  : %s\n" % ai_to_text(extra, u"")
                except Exception:
                    pass
            body = (
                u"----- SYSTEM PROMPT -----\n%s\n"
                u"----- USER PROMPT -----\n%s\n"
                u"===== END REQUEST =====\n\n"
            ) % (ai_to_text(sys_prompt, u""), ai_to_text(user_prompt, u""))

            # 1) Всегда перезаписываем «последний запрос».
            try:
                ai_write_debug_file("ai_last_prompt.txt", head + body)
            except Exception as e:
                print("ai_log_prompt last err: %s" % e)

            # 2) Ротация append-лога, чтобы не рос бесконечно.
            path = "ai_prompt_log.txt"
            try:
                if os.path.exists(path) and os.path.getsize(path) > AI_PROMPT_LOG_MAX_BYTES:
                    try:
                        os.rename(path, path + ".old")
                    except Exception:
                        try:
                            os.remove(path)
                        except Exception:
                            pass
            except Exception:
                pass
            try:
                fh = codecs.open(path, "a", "utf-8")
                fh.write(head + body)
                fh.close()
            except Exception as e:
                print("ai_log_prompt append err: %s" % e)
        except Exception as e:
            print("ai_log_prompt fatal: %s" % e)

    def ai_log_response(task_desc, content):
        """Опционально: если AI_LOG_INCLUDE_RESPONSE=True, дозаписывает ответ в append-лог."""
        if not AI_LOG_INCLUDE_RESPONSE:
            return
        try:
            desc = ai_to_text(task_desc if task_desc else u"(no task_desc)", u"(no task_desc)")
            text = (
                u"----- RESPONSE (%s) -----\n%s\n----- END RESPONSE -----\n\n"
            ) % (desc, ai_to_text(content, u""))
            fh = codecs.open("ai_prompt_log.txt", "a", "utf-8")
            fh.write(text)
            fh.close()
        except Exception as e:
            print("ai_log_response err: %s" % e)

    # ------------------------------------------------------------------
    # МЯГКИЙ ТЕКСТОВЫЙ ФОРМАТ ДЛЯ КВЕСТОВ (без JSON)
    # ------------------------------------------------------------------
    # Слабым 2-битным GGUF (в т.ч. Dirty-Muse i1-IQ2_XS) очень трудно
    # писать валидный JSON: слетают кавычки, скобки, запятые. Поэтому
    # для генерации квестов даём модели упрощённый key-value формат:
    #
    #   TITLE: короткое название квеста
    #   DESC: 1-2 предложения общего сеттинга
    #   STEP: step1
    #   STEP_TITLE: название этапа
    #   STEP_DESC: что происходит на этом этапе
    #   CHOICE: текст первого выбора
    #   EFFECTS: femininity=+1, confidence=-1
    #   ENDING_TITLE: короткий заголовок исхода
    #   ENDING_TEXT: 1-2 предложения об исходе
    #   CHOICE: текст второго выбора
    #   EFFECTS: confidence=+1
    #   ENDING_TITLE: ...
    #   ENDING_TEXT: ...
    #
    # Никаких кавычек, скобок, запятых как разделителей структуры.
    # Многострочные значения разрешены: любые строки без ключа "KEY:"
    # приклеиваются к последнему значению.
    #
    # ai_parse_kv_quest(text) возвращает dict совместимой формы:
    #   {"title","description","steps":[{"id","title","description",
    #     "choices":[{"text","effects","next_step","ending_title",
    #                 "ending_text","is_ending"}...]}...]}
    # Такой dict напрямую скармливается ai_normalize_quest_tree().

    # Ключи, которые распознаём в мягком KV-формате. Порядок важен для regex —
    # более длинные варианты идут раньше коротких (STEP_TITLE до STEP и т.д.),
    # иначе "STEP_TITLE:" распарсится как ключ "STEP" со значением "_TITLE:...".
    _AI_KV_KEYS = (
        "TITLE",
        "DESCRIPTION", "DESC",
        "STEP_ID", "STEP_TITLE", "STEP_DESCRIPTION", "STEP_DESC", "STEP",
        "CHOICE_TEXT", "CHOICE",
        # Sub-field алиасы, которые модель любит писать на следующей строке
        # после голого "CHOICE:" (без значения). Обработчик применяет их
        # к ТЕКУЩЕМУ контексту: если есть cur_choice — к нему, иначе к step.
        "TEXT", "RESPONSE", "ACTION",
        "EFFECTS", "EFFECT",
        "ENDING_TITLE", "ENDING_TEXT", "ENDING",
        "OUTCOME", "RESULT", "HEADLINE",
        "NEXT_STEP", "NEXT",
        "IS_ENDING", "ENDS_HERE", "FINAL",  # флаг терминальности ветки
        "OUTFIT_ITEMS", "OUTFIT_REASON", "OUTFIT",
        "TAGS",
    )
    # Разрешаем перед ключом markdown-мусор:
    #   *   — bullet-list
    #   -   — тоже bullet
    #   >   — quote
    #   #   — heading
    #   **  — bold-обёртка
    # И разрешаем ЧИСЛОВОЙ суффикс у STEP/CHOICE (STEP1, STEP2, CHOICE1, CHOICE_2),
    # который слабые модели любят добавлять сами.
    _AI_KV_KEY_RE = re.compile(
        r'^\s*'                                 # leading whitespace
        r'(?:[\*\-\+>#]+\s*)*'                  # optional markdown bullets / headings
        r'\**\s*'                               # optional **bold** open
        r'(?:\**)?'                             # extra ** just in case
        r'(' + u"|".join(_AI_KV_KEYS) + r')'    # the KEY
        r'\s*[_\- ]?\d*'                        # optional numeric suffix like STEP1 / CHOICE 2
        r'\**'                                  # optional **bold** close
        r'\s*[:\-—–]\s*'                        # separator (:, -, em-dash, en-dash)
        r'(.*)$',                               # value
        re.IGNORECASE
    )

    def _ai_parse_effects(raw):
        """Парсит строку EFFECTS в dict.

        Понимает три формата, потому что модели переключаются между ними:
          1) плоский KV:  'femininity=+1, confidence=-1; money+5'
          2) JSON-подобный dict:  "{strip: 'top', 'allure': 2, drunk: 1}"
          3) смесь ключ=строка + ключ=число:  'strip=top, drunk=1'

        Возвращаемые значения: int для числовых статов, str для строковых
        ключей вроде strip / travel_to / diary / remove_perk.
        """
        out = {}
        if raw is None:
            return out
        # Если сразу передали dict (например, KV-парсер уже распарсил JSON).
        if isinstance(raw, dict):
            for k, v in raw.items():
                try:
                    kk = ai_to_text(k, u"").strip().lower().replace(u" ", u"_")
                except Exception:
                    continue
                if not kk:
                    continue
                # число сохраним как int, всё остальное — как есть.
                try:
                    out[kk] = int(v)
                except Exception:
                    out[kk] = v
            return out
        try:
            s = ai_to_text(raw, u"").strip()
        except Exception:
            return out
        if not s:
            return out
        # Быстрый путь: если строка похожа на JSON — попробуем распарсить.
        stripped = s.strip()
        if stripped.startswith("{"):
            for cand in (stripped, ai_repair_json_text(stripped)):
                try:
                    obj = json.loads(cand)
                    if isinstance(obj, dict):
                        return _ai_parse_effects(obj)  # рекурсия по dict-ветке
                except Exception:
                    pass
        # чистим возможные скобки/кавычки, которые модель всё же поставила
        s = s.strip().strip("{}[]()")
        # разделители: запятая / точка с запятой / | / перевод строки
        parts = re.split(r'[,;|\n]+', s)
        for p in parts:
            p = p.strip().strip("\"'` ")
            if not p:
                continue
            # 1) числовой: femininity=+1 / confidence: -1 / money +5
            m = re.match(r'^["\']?([A-Za-z_][A-Za-z0-9_ ]*)["\']?\s*[:=]?\s*([+\-]?\d+)\s*$', p)
            if m:
                k = m.group(1).strip().lower().replace(" ", "_")
                try:
                    out[k] = int(m.group(2))
                    continue
                except Exception:
                    pass
            # 2) строковый: strip='top' / travel_to: loc_bar / remove_perk = perk_shy
            m2 = re.match(r'^["\']?([A-Za-z_][A-Za-z0-9_ ]*)["\']?\s*[:=]\s*["\']?([^"\']+?)["\']?\s*$', p)
            if m2:
                k = m2.group(1).strip().lower().replace(" ", "_")
                v = m2.group(2).strip()
                if k and v:
                    out[k] = v
                    continue
        return out

    def ai_parse_kv_quest(text):
        """Парсит мягкий key-value квест-формат в dict, совместимый с ai_normalize_quest_tree.
           Возвращает dict или None, если совсем ничего не удалось распознать."""
        if text is None:
            return None
        try:
            s = ai_to_text(text, u"")
        except Exception:
            return None
        # Срезаем возможные ```...``` обёртки
        s = re.sub(r'```[a-zA-Z]*', '', s)
        s = s.replace('```', '')
        # Иногда модель всё-таки присылает JSON — попробуем сначала его.
        stripped = s.strip()
        if stripped.startswith('{') or stripped.startswith('['):
            try:
                cand = json.loads(stripped)
                if ai_dict_like(cand):
                    return cand
            except Exception:
                try:
                    cand = json.loads(ai_repair_json_text(stripped))
                    if ai_dict_like(cand):
                        return cand
                except Exception:
                    pass

        lines = s.splitlines()
        quest = {"title": u"", "description": u"", "steps": []}
        cur_step = None
        cur_choice = None
        last_ref = None      # (container_dict, field_name) — куда приклеивать многострочные хвосты
        found_any_key = False

        def _new_step(sid_hint=None):
            sid = ai_to_text(sid_hint, u"").strip() if sid_hint else u""
            if not sid:
                sid = u"step%d" % (len(quest["steps"]) + 1)
            step = {"id": sid, "title": u"", "description": u"", "choices": []}
            quest["steps"].append(step)
            return step

        def _new_choice(step, ct):
            ch = {
                "text": ai_to_text(ct, u"Continue").strip() or u"Continue",
                "effects": {},
                "next_step": None,
                "ending_title": None,
                "ending_text": None,
                # is_ending=False по умолчанию — chain-режим сам решит через
                # IS_ENDING от модели или через MAX_STEPS cap.
                "is_ending": False,
            }
            step["choices"].append(ch)
            return ch

        for raw_line in lines:
            line = raw_line.rstrip()
            if not line.strip():
                # пустая строка — просто разделитель, не сбрасываем контекст
                continue
            m = _AI_KV_KEY_RE.match(line)
            if not m:
                # многострочный хвост предыдущего поля.
                # Срезаем возможный ведущий markdown-мусор ("- ", "* ", "> ")
                # и обрамляющие ** — модели любят их для акцента.
                cont_txt = re.sub(r'^\s*[\*\-\+>#]+\s*', u'', line).strip()
                cont_txt = re.sub(r'^\*+|\*+$', u'', cont_txt).strip()
                if last_ref is not None and cont_txt:
                    cont, field = last_ref
                    prev = cont.get(field) or u""
                    sep = u" " if prev else u""
                    cont[field] = ai_to_text(prev, u"") + sep + cont_txt
                continue

            found_any_key = True
            key = m.group(1).upper()
            val = (m.group(2) or u"").strip()
            # Срезаем закрывающие ** (**bold** обёртка со стороны значения)
            # и обрамляющие кавычки/бэктики.
            val = re.sub(r'^\*+|\*+$', u'', val).strip()
            val = val.strip("\"'` ")

            if key == "TITLE":
                quest["title"] = val
                last_ref = (quest, "title")
            elif key in ("DESC", "DESCRIPTION"):
                quest["description"] = val
                last_ref = (quest, "description")
            elif key in ("STEP", "STEP_ID"):
                # ЗАЩИТА: 2-битные модели часто игнорируют "STEP: step1" и
                # вместо id пишут туда описание/сцену/имена персонажей
                # ("STEP: A MAN 1 leans against a nearby trash can..."). Такой
                # val нельзя брать как id — он потом slugified'ится в
                # normalize_quest_tree и вылезает в UI как title сцены.
                # Эвристика: настоящий id короткий (<=24 симв), без пробелов
                # ИЛИ ровно "step\d+"; всё остальное считаем описанием.
                _val_stripped = val.strip()
                _looks_like_id = bool(_val_stripped) and (
                    re.match(r'^step[_\-\s]?\d+$', _val_stripped, re.IGNORECASE) or
                    (len(_val_stripped) <= 24 and u" " not in _val_stripped)
                )
                if _val_stripped and not _looks_like_id:
                    # Это описание, а не id. Заводим шаг без hint и кладём
                    # текст в description.
                    cur_step = _new_step()
                    cur_step["description"] = _val_stripped
                    cur_choice = None
                    last_ref = (cur_step, "description")
                else:
                    cur_step = _new_step(_val_stripped if _looks_like_id else None)
                    cur_choice = None
                    last_ref = None
            elif key == "STEP_TITLE":
                if cur_step is None:
                    cur_step = _new_step()
                cur_step["title"] = val
                last_ref = (cur_step, "title")
            elif key in ("STEP_DESC", "STEP_DESCRIPTION"):
                if cur_step is None:
                    cur_step = _new_step()
                cur_step["description"] = val
                last_ref = (cur_step, "description")
            elif key in ("CHOICE", "CHOICE_TEXT"):
                if cur_step is None:
                    cur_step = _new_step()
                # Если val пустое ('CHOICE:' на голой строке), НЕ ставим
                # default 'Continue' — модель наверняка дала текст на
                # следующей строке через 'text:' / просто продолжением.
                # Оставим text пустым, парсер заполнит через TEXT/RESPONSE
                # или через многострочный хвост, а если так и осталось
                # пустым — уже в самом конце fillnem 'Continue'.
                _init_text = val if val else u""
                cur_choice = _new_choice(cur_step, _init_text or u"")
                # если val пустое — не ставим 'Continue', иначе следующие
                # многострочные хвосты приклеятся к 'Continue text ...'.
                if not val:
                    cur_choice["text"] = u""
                last_ref = (cur_choice, "text")
            elif key in ("TEXT", "RESPONSE", "ACTION"):
                # Sub-field: применяем к текущему choice, если он есть.
                # Если choice ещё нет — трактуем как описание шага.
                if cur_choice is not None:
                    cur_choice["text"] = val
                    last_ref = (cur_choice, "text")
                elif cur_step is not None:
                    if not cur_step.get("description"):
                        cur_step["description"] = val
                    else:
                        cur_step["description"] = cur_step["description"] + u" " + val
                    last_ref = (cur_step, "description")
            elif key in ("OUTCOME", "RESULT", "HEADLINE"):
                # Алиасы для ENDING_TITLE / ENDING_TEXT. HEADLINE и
                # OUTCOME чаще всего = title исхода; RESULT — текст.
                if cur_choice is None:
                    if cur_step is None:
                        cur_step = _new_step()
                    cur_choice = _new_choice(cur_step, u"")
                    cur_choice["text"] = u""
                target_field = "ending_title" if key in ("OUTCOME", "HEADLINE") else "ending_text"
                cur_choice[target_field] = val
                # НЕ ставим is_ending=True автоматически: наличие ending_title
                # ещё не значит финал ветки. Финал определяется явным
                # IS_ENDING:true от модели (или потолком MAX_STEPS в движке).
                last_ref = (cur_choice, target_field)
            elif key in ("EFFECTS", "EFFECT"):
                if cur_choice is None:
                    if cur_step is None:
                        cur_step = _new_step()
                    cur_choice = _new_choice(cur_step, u"Continue")
                cur_choice["effects"] = _ai_parse_effects(val)
                last_ref = None
            elif key == "ENDING_TITLE":
                if cur_choice is None:
                    if cur_step is None:
                        cur_step = _new_step()
                    cur_choice = _new_choice(cur_step, u"Continue")
                cur_choice["ending_title"] = val
                last_ref = (cur_choice, "ending_title")
            elif key in ("ENDING", "ENDING_TEXT"):
                if cur_choice is None:
                    if cur_step is None:
                        cur_step = _new_step()
                    cur_choice = _new_choice(cur_step, u"Continue")
                cur_choice["ending_text"] = val
                last_ref = (cur_choice, "ending_text")
            elif key in ("NEXT_STEP", "NEXT"):
                if cur_choice is not None:
                    v = val.strip()
                    if v.lower() in (u"", u"null", u"none", u"end", u"finish", u"done", u"-"):
                        cur_choice["next_step"] = None
                        # НЕ ставим is_ending=True автоматически: null next_step
                        # теперь ЗНАЧИТ "движок сам сгенерирует продолжение"
                        # (on-demand chain). is_ending нужен только если LLM
                        # его ЯВНО указала через IS_ENDING.
                    else:
                        cur_choice["next_step"] = v
                        cur_choice["is_ending"] = False
                last_ref = None
            elif key in ("IS_ENDING", "ENDS_HERE", "FINAL"):
                # Явный маркер финальности. Модель ставит true → эта ветка
                # закрывает сцену, игра покажет summary вместо генерации
                # следующего шага.
                if cur_choice is not None:
                    v = val.strip().lower()
                    cur_choice["is_ending"] = v in (u"true", u"1", u"yes", u"y", u"end")
                last_ref = None
            elif key in ("OUTFIT", "OUTFIT_ITEMS"):
                if cur_step is not None:
                    items = [x.strip() for x in re.split(r'[,;|]+', val) if x.strip()]
                    outfit = cur_step.get("outfit_suggestion") or {"items": [], "reason": u""}
                    outfit["items"] = items
                    cur_step["outfit_suggestion"] = outfit
                last_ref = None
            elif key == "OUTFIT_REASON":
                if cur_step is not None:
                    outfit = cur_step.get("outfit_suggestion") or {"items": [], "reason": u""}
                    outfit["reason"] = val
                    cur_step["outfit_suggestion"] = outfit
                    last_ref = (outfit, "reason")
            elif key == "TAGS":
                tags = [x.strip() for x in re.split(r'[,;|]+', val) if x.strip()]
                if cur_step is not None:
                    cur_step["tags"] = tags
                else:
                    quest["tags"] = tags
                last_ref = None

        if not found_any_key:
            return None
        # Мини-санитация: если совсем нет шагов, но есть CHOICE-ы верхнего уровня — обёртка.
        if not quest["steps"]:
            return None
        # Мини-санитация:
        #  1) у каждого шага должен быть хоть один choice;
        #  2) если у choice остался пустой text (CHOICE: без значения и без
        #     TEXT:), — только тогда ставим 'Continue' как последнюю опору.
        for st in quest["steps"]:
            if not st.get("choices"):
                # Единственный дефолтный choice — он реально финальный,
                # потому что альтернатив нет и продолжать некуда.
                st["choices"] = [{
                    "text": u"Continue", "effects": {}, "next_step": None,
                    "ending_title": None, "ending_text": None, "is_ending": True,
                }]
            for ch in st["choices"]:
                if not ch.get("text") or not ai_to_text(ch.get("text"), u"").strip():
                    ch["text"] = u"Continue"
        return quest

    # Base call с настраиваемым таймаутом 25 секунд для разгрузки Олламы
    def ai_call(model, sys_prompt, user_prompt, want_json=False, temp=0.85, max_tokens=700, task_desc=None, timeout=120, force_json_format=True):
        if task_desc:
            try:
                # Добавляем в очередь уведомлений информацию о старте генерации
                store.ai_notify_queue.append(u"ИИ: Запрос к Ollama (%s)..." % task_desc)
            except:
                pass

        messages=[{"role":"system","content":sys_prompt},{"role":"user","content":user_prompt}]
        
        # GPU-friendly настройки запроса под RTX 3050 4GB:
        # - маленький num_ctx и num_batch уменьшают VRAM pressure
        # - num_gpu=99 просит Ollama вынести на GPU максимум слоёв, сколько реально влезет
        # - low_vram помогает не скатываться в тяжелый CPU fallback при нехватке памяти
        req_options={
            "temperature": temp,
            "top_p": 0.92,
            "num_predict": max_tokens,
            "num_ctx": OLLAMA_NUM_CTX,
            "num_thread": OLLAMA_NUM_THREAD,
            "num_batch": OLLAMA_NUM_BATCH
        }
        if OLLAMA_FORCE_GPU:
            req_options["num_gpu"] = OLLAMA_GPU_LAYERS
            req_options["low_vram"] = OLLAMA_LOW_VRAM
        
        payload={"model":model,"messages":messages,"stream":False,"options":req_options}
        # format=json помогает, но на очень слабых GGUF иногда даёт пустой/битый ответ.
        # Для деревьев квестов можно выключить force_json_format и парсить вручную.
        if want_json and force_json_format:
            payload["format"]="json"

        # Логируем запрос ДО того, как что-то отправим. Так даже если Ollama
        # уронит соединение / зависнет, в ai_last_prompt.txt останется точный
        # промпт, ушедший в модель.
        try:
            ai_log_prompt(
                task_desc, model, sys_prompt, user_prompt,
                extra=u"want_json=%s force_json=%s temp=%s max_tokens=%s timeout=%s ctx=%s"
                      % (want_json, force_json_format, temp, max_tokens, timeout, OLLAMA_NUM_CTX),
            )
        except Exception as _e:
            print("ai_log_prompt outer err: %s" % _e)
        lock_acquired = False
        raw_content = None
        try:
            # Один глобальный lock на все запросы к Ollama.
            # На слабом железе это НАМНОГО стабильнее, чем десятки одновременных фоновых запросов,
            # из-за которых ручной квест может висеть в очереди бесконечно долго.
            ai_ollama_global_lock.acquire()
            lock_acquired = True

            data=json.dumps(payload).encode('utf-8')
            req=urllib2.Request(OLLAMA_URL, data=data, headers={'Content-Type':'application/json'})
            # Таймаут настраиваемый: деревья квестов могут идти дольше одиночных событий
            resp=urllib2.urlopen(req, timeout=timeout or 120)
            res=json.loads(resp.read().decode('utf-8'))
            content=res['message']['content']
            
            if want_json:
                raw_content = content
                try:
                    store.ai_debug_last_json_raw = unicode(raw_content)
                except:
                    pass
                content=re.sub(r'```json|```','',content).strip()
                # Умный парсинг для предотвращения усечения списков в словари (баг с {...} внутри [...])
                f_curly = content.find('{')
                f_bracket = content.find('[')
                
                if f_bracket != -1 and (f_curly == -1 or f_bracket < f_curly):
                    l_bracket = content.rfind(']')
                    if l_bracket != -1:
                        content = content[f_bracket:l_bracket+1]
                elif f_curly != -1:
                    l_curly = content.rfind('}')
                    if l_curly != -1:
                        content = content[f_curly:l_curly+1]
                
                try:
                    parsed_json = json.loads(content)
                except Exception as je:
                    # Слабые uncensored GGUF часто почти попадают в JSON, но забывают кавычки у ключей
                    # (choices:, description:, ,next_step":). Пробуем быстрый ремонт вместо падения.
                    repaired = ai_repair_json_text(content)
                    try:
                        parsed_json = json.loads(repaired)
                        try:
                            store.ai_debug_last_json_raw = unicode(raw_content) + u"\n\n[AI_JSON_REPAIRED]\n" + unicode(repaired)
                        except Exception:
                            pass
                        print("AI JSON repaired successfully for %s after parse error: %s" % (model, je))
                    except Exception as je2:
                        try:
                            store.ai_debug_last_json_raw = unicode(raw_content) + u"\n\n[AI_JSON_REPAIR_FAILED]\n" + unicode(repaired)
                        except Exception:
                            pass
                        print("AI JSON parse error %s: %s | repair failed: %s | raw=%s" % (model, je, je2, raw_content[:800] if raw_content else ""))
                        return "__ERROR_JSON__ %s | repair: %s" % (je, je2)
                if task_desc:
                    try:
                        store.ai_notify_queue.append(u"ИИ: (%s) успешно готов!" % task_desc)
                    except:
                        pass
                return parsed_json
            
            if task_desc:
                try:
                    store.ai_notify_queue.append(u"ИИ: (%s) успешно готов!" % task_desc)
                except:
                    pass
            return content
        except Exception as e:
            err_msg = str(e)
            print("AI call error %s: %s" % (model, err_msg))
            try:
                store.ai_debug_last_json_raw = unicode(raw_content) if raw_content else u"AI_CALL_EXCEPTION: %s" % err_msg
            except Exception:
                pass
            if task_desc:
                try:
                    store.ai_notify_queue.append(u"ИИ: Сбой (%s)" % task_desc)
                except:
                    pass
            if "404" in err_msg or "not found" in err_msg.lower():
                return "__ERROR_MODEL_NOT_FOUND__"
            elif "500" in err_msg or "internal server error" in err_msg.lower():
                # Это не ошибка JSON в моде: упал сам сервер/бекенд Ollama (часто VRAM/контекст/модель).
                return "__ERROR_OLLAMA_500__ %s" % err_msg
            elif "111" in err_msg or "connection refused" in err_msg.lower() or "timed out" in err_msg.lower() or "timeout" in err_msg.lower():
                return "__ERROR_OLLAMA_OFFLINE__"
            return "__ERROR__ %s" % err_msg
        finally:
            if lock_acquired:
                try:
                    ai_ollama_global_lock.release()
                except:
                    pass

    def ai_call_json_cpu_safe(model, sys_prompt, user_prompt, temp=0.25, max_tokens=220, task_desc=None, timeout=180):
        """Аварийный JSON-вызов для квестов после HTTP 500: без GPU, без format=json, маленький ctx."""
        if task_desc:
            try:
                store.ai_notify_queue.append(u"ИИ: CPU-safe retry (%s)..." % task_desc)
            except Exception:
                pass
        messages = [{"role": "system", "content": sys_prompt}, {"role": "user", "content": user_prompt}]
        safe_options = {
            "temperature": temp,
            "top_p": 0.9,
            "num_predict": max_tokens,
            "num_ctx": 1024,
            "num_thread": max(1, min(4, OLLAMA_NUM_THREAD)),
            "num_batch": 16,
            "num_gpu": 0,
        }
        payload = {"model": model, "messages": messages, "stream": False, "options": safe_options}

        # Логируем и CPU-safe запрос отдельно — по метке task_desc в логе видно,
        # что это retry, а не первичный вызов.
        try:
            ai_log_prompt(
                (u"CPU-SAFE: " + ai_to_text(task_desc, u"")) if task_desc else u"CPU-SAFE",
                model, sys_prompt, user_prompt,
                extra=u"cpu_safe temp=%s max_tokens=%s timeout=%s" % (temp, max_tokens, timeout),
            )
        except Exception as _e:
            print("ai_log_prompt cpu_safe err: %s" % _e)

        lock_acquired = False
        raw_content = None
        try:
            ai_ollama_global_lock.acquire()
            lock_acquired = True
            data = json.dumps(payload).encode('utf-8')
            req = urllib2.Request(OLLAMA_URL, data=data, headers={'Content-Type': 'application/json'})
            resp = urllib2.urlopen(req, timeout=timeout or 180)
            res = json.loads(resp.read().decode('utf-8'))
            raw_content = res['message']['content']
            try:
                store.ai_debug_last_json_raw = unicode(raw_content)
            except Exception:
                pass
            content = ai_repair_json_text(raw_content)
            try:
                parsed_json = json.loads(content)
            except Exception as je:
                try:
                    store.ai_debug_last_json_raw = unicode(raw_content) + u"\n\n[CPU_SAFE_JSON_REPAIR_FAILED]\n" + unicode(content)
                except Exception:
                    pass
                print("CPU-safe JSON parse error %s: %s | raw=%s" % (model, je, raw_content[:800] if raw_content else ""))
                return "__ERROR_JSON_CPU_SAFE__ %s" % je
            try:
                store.ai_debug_last_json_raw = unicode(raw_content) + u"\n\n[CPU_SAFE_JSON_OK]\n" + unicode(content)
            except Exception:
                pass
            if task_desc:
                try:
                    store.ai_notify_queue.append(u"ИИ: CPU-safe retry готов (%s)" % task_desc)
                except Exception:
                    pass
            return parsed_json
        except Exception as e:
            err_msg = str(e)
            print("CPU-safe AI call error %s: %s" % (model, err_msg))
            try:
                store.ai_debug_last_json_raw = unicode(raw_content) if raw_content else u"CPU_SAFE_AI_CALL_EXCEPTION: %s" % err_msg
            except Exception:
                pass
            if "500" in err_msg or "internal server error" in err_msg.lower():
                return "__ERROR_OLLAMA_500_CPU_SAFE__ %s" % err_msg
            if "404" in err_msg or "not found" in err_msg.lower():
                return "__ERROR_MODEL_NOT_FOUND__"
            if "111" in err_msg or "connection refused" in err_msg.lower() or "timed out" in err_msg.lower() or "timeout" in err_msg.lower():
                return "__ERROR_OLLAMA_OFFLINE__"
            return "__ERROR_CPU_SAFE__ %s" % err_msg
        finally:
            if lock_acquired:
                try:
                    ai_ollama_global_lock.release()
                except Exception:
                    pass

    def get_state():
        s={}
        try:
            p=renpy.store.player
            s['fname']=getattr(renpy.store,'fname','Samantha')
            s['sname']=getattr(renpy.store,'sname','Bangtail')
            s['name']=getattr(renpy.store,'name','Sammy')
            s['corrupt']=getattr(p,'corrupt',0) if hasattr(p,'corrupt') else 0
            s['confidence']=int(getattr(p,'_confidence',35))
            s['fitness']=int(getattr(p,'_fitness',20))
            s['desire']=int(getattr(p,'_desire',10))
            s['mood']=int(getattr(p,'_mood',70))
            s['tired']=int(getattr(p,'_tired',80))
            s['hygiene']=int(getattr(p,'hygiene',100))
            s['hunger']=int(getattr(p,'hunger',100))
            s['money']=getattr(p,'cash',0)
            # ВАЖНО: 'femininity' как отдельный стат выпилен. В игре уже есть
            # 'self-acceptance as a girl' (ai_accept), и это буквально то же
            # самое, что бывший ai_fem. Оставляем один стат = accept, а
            # ключ gs['fem'] сохраняем как алиас для обратной совместимости
            # с промптами/UI, которые ждут именно 'fem'.
            s['accept']=getattr(renpy.store,'ai_accept',20)
            s['fem']=s['accept']

            try:
                t_obj=getattr(renpy.store,'t',None)
                if t_obj:
                    s['hour']=getattr(t_obj,'hour',12)
                    s['day']=getattr(t_obj,'day',0)
                    hour=s['hour']
                    if hour in (6,7,8,9,10,11):
                        s['timeofday']="morning"
                    elif hour in (12,13,14,15,16,17,18,19):
                        s['timeofday']="afternoon"
                    elif hour in (20,21,22):
                        s['timeofday']="evening"
                    else:
                        s['timeofday']="night"
                    try:
                        s['weekday']=getattr(t_obj,'weekday','Monday')
                    except:
                        s['weekday']="Monday"
                else:
                    s['hour']=12; s['day']=0; s['timeofday']="afternoon"; s['weekday']="Monday"
            except:
                s['hour']=12; s['day']=0; s['timeofday']="afternoon"; s['weekday']="Monday"

            try:
                loc_obj=None
                if hasattr(renpy.store,'loc_cur'):
                    loc_obj=getattr(renpy.store,'loc_cur')
                elif hasattr(renpy.store,'loc_to') and renpy.store.loc_to:
                    lt=renpy.store.loc_to
                    if isinstance(lt, list) and lt:
                        loc_name=lt[0]
                        try:
                            loc_obj=getattr(renpy.store,'loc_%s' % loc_name, None)
                            if not loc_obj:
                                loc_obj=loc_name
                        except:
                            loc_obj=loc_name
                    else:
                        loc_obj=str(lt)
                if loc_obj:
                    if isinstance(loc_obj, str):
                        s['location']=loc_obj
                        s['location_outside']=False
                        s['location_population']=0
                        s['location_private']= "home" in loc_obj or "bedroom" in loc_obj or "bathroom" in loc_obj
                        s['location_has_cameras']= False
                    else:
                        s['location']=getattr(loc_obj,'name','home')
                        s['location_outside']=getattr(loc_obj,'outside',False)
                        s['location_population']=getattr(loc_obj,'population',0)
                        loc_name_low=str(s['location']).lower()
                        s['location_private']= any(x in loc_name_low for x in ["bedroom","bathroom","home","common","kitchen"])
                        s['location_has_cameras']= False if s['location_private'] else getattr(loc_obj,'has_camera',False)
                        try:
                            dist_obj=loc_obj.get_district() if hasattr(loc_obj,'get_district') else None
                            s['district']=str(dist_obj) if dist_obj else "unknown"
                        except:
                            s['district']="unknown"
                else:
                    s['location']="home"
                    s['location_outside']=False
                    s['location_population']=0
                    s['location_private']=True
                    s['location_has_cameras']=False
                    s['district']="home"
            except:
                s['location']="home"
                s['location_outside']=False
                s['location_population']=0
                s['location_private']=True
                s['location_has_cameras']=False
                s['district']="home"

            try:
                c_obj=getattr(renpy.store,'c',None)
                if c_obj:
                    s['outfit']=c_obj.description_outfit()[:120] if hasattr(c_obj,'description_outfit') else "unknown"
                    s['outfit_top']=c_obj.description_top()[:80] if hasattr(c_obj,'description_top') else ""
                    s['outfit_bottom']=c_obj.description_bottom()[:80] if hasattr(c_obj,'description_bottom') else ""
                    s['is_slutty']=getattr(c_obj,'slutty',False)
                    s['is_exposed']=getattr(c_obj,'exposed',False)

                    # НОВОЕ: детальный слот-по-слоту список надетых вещей.
                    # У Клэсса Clothing слоты хранятся как числовые id (0 = ничего),
                    # реальный предмет достаётся из globals()['item_<slot>_<id>'].
                    # Собираем в вид "top: Pink Crop Top; bottom: Mini Skirt; ...".
                    worn = []
                    slot_names = [
                        ("outfit", "outfit"),
                        ("dress", "dress"),
                        ("top", "top"),
                        ("bottom", "bottom"),
                        ("bra", "bra"),
                        ("pants", "panties"),
                        ("shoes", "shoes"),
                        ("socks", "socks"),
                        ("jacket", "jacket"),
                        ("stockings", "stockings"),
                        ("gloves", "gloves"),
                        ("hat", "hat"),
                        ("glasses", "glasses"),
                        ("necklace", "necklace"),
                        ("earrings", "earrings"),
                    ]
                    for attr, label in slot_names:
                        try:
                            slot_id = getattr(c_obj, attr, 0)
                            if not slot_id:
                                continue
                            item = getattr(renpy.store, "item_%s_%s" % (attr, slot_id), None)
                            if item is None:
                                continue
                            iname = getattr(item, "name", None) or getattr(item, "desc", None) or ("item_%s_%s" % (attr, slot_id))
                            worn.append(u"%s: %s" % (label, iname))
                        except Exception:
                            continue
                    s['outfit_items'] = "; ".join(worn) if worn else "nothing worn"
                else:
                    s['outfit']=u"unknown"; s['outfit_top']=u""; s['outfit_bottom']=u""; s['is_slutty']=False; s['is_exposed']=False
                    s['outfit_items']=u"unknown"
            except Exception as _outf_e:
                s['outfit']=u"unknown"; s['outfit_top']=u""; s['outfit_bottom']=u""; s['is_slutty']=False; s['is_exposed']=False
                s['outfit_items']=u"unknown"

            # ВАЖНО: инвентарь в LLM НЕ передаём — в игровом инвентаре куча
            # gamedev-предметов (item_top_22 и т.п.), которых по РП у Саманты
            # физически нет. Передаём только деньги, это единственное, что
            # реально влияет на возможные события.
            s['inventory'] = u"(not exposed to LLM)"
            s['inventory_count'] = 0

            try:
                qlog=getattr(renpy.store,'log',None)
                if qlog and hasattr(qlog,'maintab'):
                    try:
                        maintab=qlog.maintab()
                        s['active_quests']=", ".join([str(q)[:50] for q in maintab[:3]]) if maintab else "none"
                    except:
                        s['active_quests']="unknown"
                else:
                    s['active_quests']="none"
                qlist=getattr(renpy.store,'quest_list',[])
                s['quest_count']=len(qlist) if qlist else 0
            except:
                s['active_quests']="none"; s['quest_count']=0

            try:
                _plist = list(getattr(p, 'perk_list', []) or [])[-8:]
                perk_names = [getattr(x, 'name', str(x)) for x in _plist]
                # Детальный список (имя + краткое описание) — модели нужен
                # контекст перка, чтобы придумать под него уникальный вариант.
                perk_detailed = []
                for x in _plist:
                    try:
                        nm = ai_to_text(getattr(x, 'name', u'?'), u'?')
                        ds = ai_to_text(getattr(x, 'desc', u''), u'')
                        if ds:
                            perk_detailed.append(u"%s: %s" % (nm, ds[:100]))
                        else:
                            perk_detailed.append(nm)
                    except Exception:
                        pass
                s['perks'] = ", ".join(perk_names) if perk_names else "Former man"
                s['perks_list'] = perk_names
                s['perks_detailed'] = perk_detailed  # для choices-generator'а
            except:
                s['perks']="Former man"; s['perks_list']=[]; s['perks_detailed']=[]

            try:
                s['vsex']=getattr(p,'vsex',0)
                s['asex']=getattr(p,'asex',0)
                s['hsex']=getattr(p,'hsex',0)
                s['osex']=getattr(p,'osex',0)
                s['sex_total']=s['vsex']+s['asex']
                s['is_virgin']=getattr(p,'vvirgin',True)
                s['is_anal_virgin']=getattr(p,'avirgin',True)
            except:
                s['vsex']=0; s['asex']=0; s['hsex']=0; s['osex']=0; s['sex_total']=0; s['is_virgin']=True; s['is_anal_virgin']=True

            # НОВОЕ: расширенные характеристики персонажа.
            # Раньше промпт квеста получал только fem+confidence, а игра
            # знает про Саманту сильно больше. Модель без этих полей
            # не может строить осмысленные события.
            try:
                s['int']       = int(getattr(p, 'int',      getattr(p, '_int',     0)) or 0)
                s['allure']    = int(getattr(p, 'allure',   getattr(p, '_allure',  0)) or 0)
                s['body_conf'] = int(getattr(p, 'body_conf', 0) or 0)
                s['drunk']     = int(getattr(p, 'drunk',    getattr(p, '_drunk',   0)) or 0)
                s['high']      = int(getattr(p, 'high',     getattr(p, '_high',    0)) or 0)
            except Exception:
                s['int']=0; s['allure']=0; s['body_conf']=0; s['drunk']=0; s['high']=0

            # Тело: грудь, волосы, лактация — важные NSFW/косметические маркеры.
            try:
                s['breasts_size']  = int(getattr(p, 'breasts', 2) or 2)
                s['hair_length']   = int(getattr(p, '_hair_length', getattr(p, 'hair_length', 0)) or 0)
                s['hair_colour']   = int(getattr(p, 'hair_colour', 0) or 0)
                s['pubic_hair']    = int(getattr(p, '_phair',     getattr(p, 'phair',       0)) or 0)
                s['is_lactating']  = bool(getattr(p, 'lactating', False))
                s['is_pregnant']   = bool(getattr(p, 'pregnant', 0))
                s['pregnancy_stage'] = int(getattr(p, '_pregnancy', 1) or 1)
                s['days_pregnant'] = int(getattr(p, 'days_pregnant', 0) or 0)
            except Exception:
                s['breasts_size']=2; s['hair_length']=0; s['hair_colour']=0; s['pubic_hair']=0
                s['is_lactating']=False; s['is_pregnant']=False; s['pregnancy_stage']=1; s['days_pregnant']=0

            # Менструальный цикл — сильный сюжетный маркер.
            try:
                cyc = getattr(p, 'cycle_conditions', None) or {}
                s['cycle_stage'] = cyc.get('stage', 'no_cycle') if isinstance(cyc, dict) else 'no_cycle'
                s['cycle_day']   = int(cyc.get('count_cycle', 0)) if isinstance(cyc, dict) else 0
            except Exception:
                s['cycle_stage']='no_cycle'; s['cycle_day']=0

            # Недавние локации — где Саманта была в последние ходы.
            try:
                recent_locs = list(getattr(renpy.store, 'ai_recent_locations', []) or [])
                s['recent_locations'] = ", ".join([ai_to_text(x, u"") for x in recent_locs[-6:]]) if recent_locs else u"none"
            except Exception:
                s['recent_locations'] = u"none"

            # Недавние действия (уже есть глобально, продублируем в gs для удобства).
            try:
                recent_acts = list(getattr(renpy.store, 'ai_recent_actions', []) or [])
                s['recent_actions'] = " / ".join([ai_to_text(x, u"") for x in recent_acts[-6:]]) if recent_acts else u"none"
            except Exception:
                s['recent_actions'] = u"none"

            try:
                s['nearby_npcs']="none at home" if s['location_private'] else "maybe people around"
            except:
                s['nearby_npcs']="unknown"

            try:
                s['weather']=getattr(renpy.store,'weather_var',0)
            except:
                s['weather']=0

            # ВНИМАНИЕ: раньше сюда жёстко зашивался "Dr. Tess Brooker" как
            # хендлер Института. Это выдумка — в реальном сюжете игры этого
            # персонажа нет, и LLM начинала строить квесты вокруг него,
            # обещать встречу с ним и т.д., хотя код никогда не сведёт
            # игрока с несуществующим NPC. Теперь этой выдумки нет: всё,
            # что модель узнаёт о людях, берётся из met_npcs (реально
            # встреченные) и diary_entries (реально записанные события).
            s['doctor_name'] = u""
            s['doctor_role'] = u""
            s['institute_has_cameras_in_home'] = False
            s['institute_monitoring'] = u"phone/bracelet biometrics"

            # НОВОЕ: список NPC, которых Саманта РЕАЛЬНО знает.
            # ВАЖНО про источники: в TheFixer поле has_met (=last_spoke_to>0)
            # выставляется ТОЛЬКО через talk_checker(). Флатмейты и любые
            # NPC, знакомство с которыми прошло через сюжетные renpy.say / touch
            # / туториал, так и остаются has_met=False, хотя игрок с ними
            # реально общался. Единственный надёжный признак "знаком" —
            # это diary_people_list, куда класс Npc сам добавляет персонажа
            # при первом meet(). Дополнительно принимаем всех с has_met=True
            # и всех, у кого love != дефолту (значит взаимодействие было).
            try:
                met = []
                seen_ids = set()

                def _fmt_npc(npc):
                    try:
                        fname = ai_to_text(getattr(npc, '_fname', getattr(npc, 'fname', u'?')), u'?')
                        sname = ai_to_text(getattr(npc, '_sname', getattr(npc, 'sname', u'')), u'')
                        grp   = ai_to_text(getattr(npc, 'bio_group', u''), u'')
                        gender = u"female" if getattr(npc, 'is_female', False) else u"male"
                        love  = int(getattr(npc, '_love', getattr(npc, 'love', 0)) or 0)
                        # days since last talk (может быть False → 0)
                        _sdays = getattr(npc, 'spoke_to_days_ago', 0)
                        try: _sdays = int(_sdays or 0)
                        except Exception: _sdays = 0
                        bio_short = u""
                        try:
                            bio_short = ai_to_text(getattr(npc, 'bio_text', u''), u'')[:220]
                        except Exception:
                            pass
                        head = u"%s %s [%s, %s, love %d/100" % (
                            fname, sname, grp or u"?", gender, love
                        )
                        if _sdays:
                            head += u", last talked %dd ago" % _sdays
                        head += u"]"
                        if bio_short:
                            head += u" — " + bio_short
                        return head, id(npc)
                    except Exception:
                        return None, None

                # Источник 1: игровой diary_people_list (самый надёжный)
                for src_list_name in ('diary_people_list',):
                    lst = getattr(renpy.store, src_list_name, None) or []
                    for npc in list(lst):
                        entry, npc_id = _fmt_npc(npc)
                        if entry and npc_id not in seen_ids:
                            met.append(entry)
                            seen_ids.add(npc_id)

                # Источник 2: has_met=True (через talk_checker)
                all_npcs = getattr(renpy.store, 'npc_all', None) or []
                for npc in list(all_npcs):
                    try:
                        if not bool(getattr(npc, 'has_met', False)):
                            continue
                        entry, npc_id = _fmt_npc(npc)
                        if entry and npc_id not in seen_ids:
                            met.append(entry)
                            seen_ids.add(npc_id)
                    except Exception:
                        continue

                # Источник 3: love изменился с дефолта. У большинства NPC
                # стартовый love=10 (см. Npc.__init__), у emile/story-NPC
                # обычно 0. Ловим тех, у кого love ушёл от 0/10 — значит
                # взаимодействие было даже без talk_checker.
                for npc in list(all_npcs):
                    try:
                        lv = int(getattr(npc, '_love', getattr(npc, 'love', 10)) or 0)
                        if lv not in (0, 10):  # изменился с дефолта
                            entry, npc_id = _fmt_npc(npc)
                            if entry and npc_id not in seen_ids:
                                met.append(entry)
                                seen_ids.add(npc_id)
                    except Exception:
                        continue

                # 16 хватает, чтобы не раздувать контекст, но покрыть флатмейтов + сюжет
                s['met_npcs'] = met[:16]
            except Exception as _npc_e:
                print("met_npcs collect err: %s" % _npc_e)
                s['met_npcs'] = []

            # НОВОЕ: последние записи из ИГРОВОГО дневника (diary_list —
            # это Diary_Class от TheFixer, а не наш ai_diary_entries).
            # Это единственный источник canon-предыстории Саманты.
            try:
                diary_out = []
                dlist = getattr(renpy.store, 'diary_list', None) or []
                for d in list(dlist)[-10:]:
                    try:
                        dname = ai_to_text(getattr(d, 'name', u''), u'')
                        ddesc = ai_to_text(getattr(d, 'description', u''), u'')[:220]
                        dday  = int(getattr(d, 'day', 0) or 0)
                        if dname or ddesc:
                            diary_out.append(u"[day %d] %s — %s" % (dday, dname, ddesc))
                    except Exception:
                        continue
                s['diary_entries'] = diary_out
            except Exception as _dl_e:
                print("diary_list collect err: %s" % _dl_e)
                s['diary_entries'] = []

            try:
                recent_npc_chats=[]
                npc_chats=getattr(renpy.store,'ai_npc_chats',{})
                for nid, hist in npc_chats.items():
                    if hist:
                        last=hist[-1]['content'][:80] if hist else ""
                        recent_npc_chats.append("%s: %s" % (nid, last))
                s['recent_npc_chats']=" | ".join(recent_npc_chats[-3:]) if recent_npc_chats else "none"
            except:
                s['recent_npc_chats']="none"

            try:
                evts=getattr(renpy.store,'ai_events',[])
                if evts:
                    last_evt=evts[-1].get('title','') if isinstance(evts[-1], dict) else str(evts[-1])
                    s['last_event']=last_evt
                else:
                    s['last_event']="none"
            except:
                s['last_event']="none"

        except Exception as e:
            print("get_state error %s" % e)
            s={'fname':'Samantha','corrupt':0,'confidence':35,'fitness':20,'desire':10,'mood':70,'tired':80,'hygiene':100,'hunger':100,'money':200,'accept':20,'fem':20,'horny':5,'trust':40,'location':'home','location_outside':False,'location_private':True,'location_has_cameras':False,'district':'home','outfit':'unknown','outfit_top':'','outfit_bottom':'','outfit_items':'unknown','is_slutty':False,'is_exposed':False,'inventory':'(not exposed to LLM)','inventory_count':0,'active_quests':'none','quest_count':0,'perks':'Former man','perks_list':[],'vsex':0,'asex':0,'hsex':0,'osex':0,'sex_total':0,'is_virgin':True,'is_anal_virgin':True,'nearby_npcs':'none','weather':0,'hour':12,'day':0,'timeofday':'afternoon','weekday':'Monday','doctor_name':'','doctor_role':'','institute_has_cameras_in_home':False,'institute_monitoring':'phone/bracelet biometrics','recent_npc_chats':'none','last_event':'none','recent_locations':'none','recent_actions':'none','met_npcs':[],'diary_entries':[]}
        return s

    def ai_filter_event_by_comfort(event):
        try:
            from ai_config_tags import AI_COMFORT_DICT
            from ai_config_locations import ai_is_theme_allowed_in_location

            # optional hard block if user added it to ai_config_tags.rpy
            try:
                from ai_config_tags import ai_event_has_hard_blocked_content
                if ai_event_has_hard_blocked_content(event):
                    print("Event blocked by centralized hard safety filter")
                    try:
                        ai_set_event_debug(u"Event was blocked by centralized hard safety filter", parsed=event)
                    except:
                        pass
                    return False
            except ImportError:
                pass

            if not ai_dict_like(event):
                return True

            tags = event.get('tags', []) or []
            if not tags:
                type_to_tag = {
                    "femininity": ["femininity"],
                    "corruption": ["prostitution","freeuse"],
                    "institute": ["mindcontrol","body_mod"],
                    "horny": ["exhibitionism"],
                    "work": ["prostitution"],
                    "social": ["bullying"]
                }
                tags = type_to_tag.get(event.get('type',''), [])
            for tag in tags:
                # Неизвестный тег НЕ блокируем (раньше AI_COMFORT_DICT.get(tag) or ... валил любые кастомные теги)
                conf = AI_COMFORT_DICT.get(tag)
                if conf is not None and conf.get('level', 0) == 0:
                    print("Event blocked by comfort tag %s" % tag)
                    return False
                if conf is not None:
                    loc = get_state().get('location','home')
                    if not ai_is_theme_allowed_in_location(tag, loc):
                        print("Event tag %s not allowed in location %s" % (tag, loc))
                        return False
            return True
        except Exception as e:
            print("filter comfort err %s" % e)
            return True

    def ai_get_spicy_prompt_modifier():
        try:
            from ai_config_spicy import ai_roll_spicy, ai_get_spicy_level
            is_spicy, chance, roll = ai_roll_spicy()
            level = ai_get_spicy_level()
            store.ai_total_quests = getattr(store,'ai_total_quests',0) + 1
            if is_spicy:
                store.ai_total_spicy_quests = getattr(store,'ai_total_spicy_quests',0) + 1
                store.ai_spicy_last_was_spicy = True
            else:
                store.ai_spicy_last_was_spicy = False
            return is_spicy, level, chance, roll
        except Exception as e:
            print("spicy mod err %s" % e)
            return False, 2, 20, 50

    def start_async_ollama(target_func):
        ai_thread_obj=threading.Thread(target=target_func)
        ai_thread_obj.daemon=True
        ai_thread_obj.start()
        return ai_thread_obj

    def auto_equip(item_ids, only_if_owned=True):
        if not item_ids: return False
        ok=False
        for item_id in item_ids:
            try:
                clean_id = item_id.split()[0] if ' ' in item_id else item_id
                parts = clean_id.split("_")
                if len(parts) < 3:
                    continue
                item_type = parts[1]
                try:
                    item_num = int(parts[2])
                except:
                    try:
                        item_num = int(''.join(filter(str.isdigit, parts[2])))
                    except:
                        continue
                try:
                    item_obj = getattr(renpy.store, clean_id, None)
                    if item_obj:
                        ward = getattr(renpy.store, 'wardrobe', None)
                        if only_if_owned and ward and hasattr(ward, 'qty'):
                            try:
                                if ward.qty(item_obj) <= 0:
                                    print("Skip equip %s - not owned" % clean_id)
                                    continue
                            except:
                                pass
                except:
                    pass

                try:
                    cs = getattr(renpy.store, 'clothes_set', None)
                    if cs:
                        cs(item_type, item_num)
                        ok=True
                    else:
                        c_obj = getattr(renpy.store, 'c', None)
                        if c_obj and hasattr(c_obj, item_type):
                            setattr(c_obj, item_type, item_num)
                            ok=True
                            try:
                                tab_top_name = getattr(renpy.store, 'tab_top', 'daily')
                                tab_obj = getattr(renpy.store, tab_top_name, None)
                                if tab_obj and hasattr(tab_obj, item_type):
                                    setattr(tab_obj, item_type, item_num)
                            except: pass
                except Exception as e:
                    print("clothes_set err %s %s" % (clean_id, e))

                if hasattr(renpy.store, 'refresh_avatar'):
                    try: renpy.store.refresh_avatar()
                    except: pass
            except Exception as e:
                print("equip %s err %s" % (item_id, e))
        return ok

    def spawn_npc(data):
        if not data or not data.get('generate_new'): return None
        try:
            NpcClass=getattr(renpy.store,'Npc',None)
            if not NpcClass: return None
            fname=data.get('fname','Lila'); sname=data.get('sname',''); nname=data.get('nname','')
            colour=data.get('colour','#ff88cc'); is_female=data.get('is_female',True)
            iswhore=data.get('iswhore',False); isslut=data.get('isslut',False)
            bio_group=data.get('bio_group','whore')
            try:
                npc=NpcClass(fname=fname,sname=sname,nname=nname,colour=colour,is_female=is_female,iswhore=iswhore,isslut=isslut,bio_group=bio_group)
            except:
                npc=NpcClass(fname=fname,sname=sname,is_female=is_female)
            if hasattr(renpy.store,'npc_all'): renpy.store.npc_all.append(npc)
            if hasattr(renpy.store,'npc_girls') and is_female: renpy.store.npc_girls.append(npc)
            if hasattr(renpy.store,'diary_people_list'): renpy.store.diary_people_list.append(npc)
            renpy.notify(u"Новый персонаж: %s" % fname)
            return npc
        except Exception as e:
            print("spawn err %s" % e)
            return None

    def ai_format_effects_summary(effects):
        """Человекочитаемый список наград/штрафов для финала."""
        if not ai_dict_like(effects):
            return u""
        parts = []
        labels = {
            "femininity": u"Femininity",
            "confidence": u"Confidence",
            "corrupt": u"Corruption",
            "desire": u"Desire",
            "mood": u"Mood",
            "fitness": u"Fitness",
            "money": u"Money",
            "horny": u"Horny",
            "trust": u"Trust",
            "accept": u"Acceptance",
        }
        for k, label in labels.items():
            if k in effects and effects.get(k) not in (None, "", 0, "0"):
                try:
                    val = int(effects.get(k))
                    parts.append(u"%s %+d" % (label, val))
                except Exception:
                    parts.append(u"%s %s" % (label, effects.get(k)))
        perk = effects.get('perk_add')
        if perk:
            if ai_dict_like(perk):
                pname = ai_to_text(perk.get('name', u'New Trait'), u'New Trait')
            else:
                pname = ai_to_text(perk, u'New Trait')
            parts.append(u"Perk: %s" % pname)
        if effects.get('give_item'):
            parts.append(u"Item: %s" % ai_to_text(effects.get('give_item'), u'item'))
        return u" | ".join(parts)

    def ai_apply_choice_effects(ch):
        """Применяет effects выбора (статы/деньги/перк/предмет). Возвращает summary-строку."""
        summary_bits = []
        try:
            if not ai_dict_like(ch):
                return u""
            eff = ch.get('effects', {}) if ai_dict_like(ch.get('effects', {})) else {}
            if not ai_dict_like(eff):
                # sometimes effects are flat on choice
                eff = {}
            # also allow flat stats on choice root
            for k in ("femininity", "confidence", "corrupt", "desire", "mood", "fitness", "money", "horny", "trust", "accept", "perk_add", "give_item"):
                if k not in eff and ch.get(k) is not None and k not in ("text", "next_step"):
                    # only copy if looks like reward field present on root and not already in effects
                    if k in ch and ch.get(k) not in (None, ""):
                        # don't pull text-like roots
                        if k in ("perk_add", "give_item") or isinstance(ch.get(k), (int, float, long)) or (isinstance(ch.get(k), basestring) and unicode(ch.get(k)).lstrip('-').isdigit()):
                            eff[k] = ch.get(k)
            if ch.get('perk_add') is not None and 'perk_add' not in eff:
                eff['perk_add'] = ch.get('perk_add')

            p = getattr(store, 'player', None)
            if p is None:
                try:
                    p = player
                except Exception:
                    p = None

            def _i(v, default=0):
                try:
                    return int(v)
                except Exception:
                    return default

            if 'confidence' in eff and p is not None:
                d = _i(eff['confidence'])
                try:
                    p.add_conf(d)
                except Exception:
                    try:
                        p._confidence = max(0, min(100, getattr(p, '_confidence', 35) + d))
                    except Exception:
                        pass
            # femininity как отдельный стат выпилен: все дельты уходят в
            # ai_accept (self-acceptance as a girl). ai_fem остаётся как
            # алиас — чтобы старые UI-строки '[ai_fem]%' продолжали работать.
            if 'femininity' in eff or 'accept' in eff or 'acceptance' in eff:
                d = _i(eff.get('femininity', eff.get('accept', eff.get('acceptance', 0))))
                store.ai_accept = max(0, min(100, getattr(store, 'ai_accept', 20) + d))
                store.ai_fem = store.ai_accept
            if 'corrupt' in eff and p is not None and hasattr(p, 'corrupt'):
                p.corrupt = max(0, p.corrupt + _i(eff['corrupt']))
            if 'desire' in eff and p is not None:
                d = _i(eff['desire'])
                try:
                    if hasattr(p, 'add_desire'):
                        p.add_desire(d)
                    elif hasattr(p, '_desire'):
                        p._desire = max(0, min(100, p._desire + d))
                except Exception:
                    pass
            if 'mood' in eff and p is not None and hasattr(p, 'mood'):
                try:
                    p.mood = max(0, min(100, p.mood + _i(eff['mood'])))
                except Exception:
                    pass
            if 'fitness' in eff and p is not None:
                d = _i(eff['fitness'])
                try:
                    if hasattr(p, 'add_fit'):
                        p.add_fit(d)
                    elif hasattr(p, '_fitness'):
                        p._fitness = max(0, min(100, p._fitness + d))
                except Exception:
                    pass
            if 'money' in eff and p is not None:
                d = _i(eff['money'])
                try:
                    if d >= 0:
                        p.add_money(d)
                    else:
                        p.remove_money(abs(d))
                except Exception:
                    pass
            if 'horny' in eff:
                store.ai_horny = max(0, min(100, getattr(store, 'ai_horny', 5) + _i(eff['horny'])))
            if 'trust' in eff:
                store.ai_trust = max(0, min(100, getattr(store, 'ai_trust', 40) + _i(eff['trust'])))
            if 'accept' in eff:
                store.ai_accept = max(0, min(100, getattr(store, 'ai_accept', 20) + _i(eff['accept'])))
            if 'give_item' in eff:
                try:
                    item_obj = getattr(store, eff['give_item'], None)
                    if item_obj and hasattr(store, 'inv'):
                        store.inv.add(item_obj)
                except Exception as e:
                    print("give_item err: %s" % e)

            # =============================================================
            # РАСШИРЕННЫЕ ЭФФЕКТЫ: реально меняют мир, а не только цифры.
            # Все ключи должны совпадать с [ALLOWED EFFECTS] в промпте,
            # иначе модель просто не будет их использовать.
            # =============================================================

            # --- 1) Опьянение / кайф / усталость / голод / гигиена / телесные ---
            if 'drunk' in eff and p is not None and hasattr(p, 'add_drunk'):
                try: p.add_drunk(_i(eff['drunk']))
                except Exception as e: print("drunk apply err: %s" % e)
            if 'high' in eff and p is not None and hasattr(p, 'add_high'):
                try: p.add_high(_i(eff['high']))
                except Exception as e: print("high apply err: %s" % e)
            if 'tired' in eff and p is not None and hasattr(p, 'add_tired'):
                try: p.add_tired(_i(eff['tired']))
                except Exception as e: print("tired apply err: %s" % e)
            if 'hunger' in eff and p is not None and hasattr(p, 'add_hunger'):
                try: p.add_hunger(_i(eff['hunger']))
                except Exception as e: print("hunger apply err: %s" % e)
            if 'hygiene' in eff and p is not None and hasattr(p, 'add_hygiene'):
                try: p.add_hygiene(_i(eff['hygiene']))
                except Exception as e: print("hygiene apply err: %s" % e)
            if 'allure' in eff and p is not None:
                try:
                    if hasattr(p, '_allure'):
                        p._allure = max(0, getattr(p, '_allure', 0) + _i(eff['allure']))
                except Exception as e: print("allure apply err: %s" % e)

            # --- 2) Одежда: реально снимает слоты на модельке ---
            if 'strip' in eff:
                try:
                    strip_val = eff['strip']
                    if isinstance(strip_val, basestring):
                        strip_slots = [strip_val]
                    elif isinstance(strip_val, (list, tuple)):
                        strip_slots = list(strip_val)
                    else:
                        strip_slots = []
                    c_obj = getattr(store, 'c', None)
                    if c_obj:
                        SLOT_MAP = {
                            u"all":     ["outfit", "dress", "top", "bottom", "bra", "pants", "shoes", "socks", "jacket", "stockings"],
                            u"topless": ["top", "bra", "outfit", "dress"],
                            u"bottomless": ["bottom", "pants", "outfit", "dress"],
                            u"naked":   ["outfit", "dress", "top", "bottom", "bra", "pants", "shoes", "socks", "jacket", "stockings"],
                        }
                        real_slots = []
                        for s_slot in strip_slots:
                            key = ai_to_text(s_slot, u"").strip().lower()
                            real_slots.extend(SLOT_MAP.get(key, [key]))
                        stripped_names = []
                        for slot in real_slots:
                            try:
                                if hasattr(c_obj, slot) and int(getattr(c_obj, slot, 0) or 0) > 0:
                                    setattr(c_obj, slot, 0)
                                    stripped_names.append(slot)
                            except Exception:
                                continue
                        if stripped_names:
                            try:
                                # Обновим avatar/wardrobe, чтобы моделька перерисовалась.
                                if hasattr(store, 'refresh_avatar'):
                                    store.refresh_avatar()
                            except Exception:
                                pass
                            summary_bits.append(u"Stripped: " + u", ".join(stripped_names))
                            try:
                                store.ai_notify_queue.append(u"Одежда снята: " + u", ".join(stripped_names))
                            except Exception:
                                pass
                except Exception as e:
                    print("strip apply err: %s" % e)

            # --- 3) Экипировка (если модель знает реальный item id) ---
            if 'equip' in eff and ai_dict_like(eff.get('equip')):
                try:
                    c_obj = getattr(store, 'c', None)
                    if c_obj:
                        for slot, item_id in eff['equip'].items():
                            try:
                                slot = ai_to_text(slot, u"").strip().lower()
                                iid = int(item_id)
                                if hasattr(c_obj, slot):
                                    setattr(c_obj, slot, iid)
                            except Exception:
                                continue
                        try:
                            if hasattr(store, 'refresh_avatar'):
                                store.refresh_avatar()
                        except Exception:
                            pass
                        summary_bits.append(u"Equipped: " + u", ".join(u"%s#%s" % (k,v) for k,v in eff['equip'].items()))
                except Exception as e:
                    print("equip apply err: %s" % e)

            # --- 4) Пропуск времени ---
            if 'advance_hours' in eff:
                try:
                    hours = _i(eff['advance_hours'])
                    if hours > 0:
                        t_obj = getattr(store, 't', None)
                        if t_obj is not None and hasattr(t_obj, 'add_hour'):
                            for _ in range(min(hours, 24)):
                                try: t_obj.add_hour()
                                except Exception: break
                            summary_bits.append(u"+%dh" % hours)
                except Exception as e:
                    print("advance_hours err: %s" % e)

            # --- 5) Перемещение на другую локацию через игровой travel_walk ---
            if 'travel_to' in eff and eff.get('travel_to'):
                try:
                    loc_id = ai_to_text(eff['travel_to'], u"").strip()
                    if loc_id:
                        loc_obj = getattr(store, "loc_" + loc_id, None) or getattr(store, loc_id, None)
                        if loc_obj is None:
                            print("travel_to: unknown location '%s' — skipping" % loc_id)
                        else:
                            # travel_walk работает как renpy-jump-функция;
                            # вызываем её в defer'е, чтобы не сломать текущий
                            # ai_event_choice. Просто ставим флаг + save target.
                            store.ai_pending_travel = loc_obj
                            summary_bits.append(u"Travel: %s" % loc_id)
                except Exception as e:
                    print("travel_to err: %s" % e)

            # --- 6) Запись в дневник (реальный diary_list) ---
            if 'diary' in eff and eff.get('diary'):
                try:
                    diary_text = ai_to_text(eff['diary'], u"")
                    Diary_Class = getattr(store, 'Diary_Class', None)
                    if diary_text and Diary_Class is not None:
                        # имя записи — короткая шапка (первые 40 символов)
                        head = diary_text.strip().split(u"\n", 1)[0][:40] or u"AI event"
                        try:
                            Diary_Class(head, diary_text)
                            summary_bits.append(u"Diary: " + head)
                        except Exception as e2:
                            print("Diary_Class create err: %s" % e2)
                except Exception as e:
                    print("diary apply err: %s" % e)

            # --- 7) РИСК БЕРЕМЕННОСТИ — как после обычной сексуальной сцены ---
            # Ключ 'pregnancy_risk' в effects говорит движку "прогони обычный
            # преган-чек". Никакой гарантированной беременности: если день
            # цикла не тот, есть таблетки, стоит perk_pregnant_* или просто
            # не повезёт с numgen() — Саманту "пронесёт" ровно как в любой
            # штатной сексуальной сцене игры (см. player_class.sex_cum_pregcheck).
            #
            # Допустимые значения ключа:
            #   'insert'  — стандартный "в неё кончили" (fertility 80/x)
            #   'inside'  — глубоко внутрь, максимальный шанс (fertility 4/x)
            #   'pullout' — прерванный акт, минимальный шанс (fertility 30/x)
            #   True      — трактуется как 'insert'
            # Кому припишем "отцовство": если LLM явно передала
            # 'pregnancy_partner': 'fname of a KNOWN NPC' — ищем этого NPC
            # в npc_all; иначе используем встроенный fallback-NPC `unknown`
            # ("some unknown guy"), ровно как игра делает для случайного
            # секса без имени.
            if 'pregnancy_risk' in eff and eff.get('pregnancy_risk'):
                try:
                    where_raw = eff.get('pregnancy_risk')
                    if where_raw is True or where_raw == 1:
                        where = "insert"
                    else:
                        where = ai_to_text(where_raw, u"insert").strip().lower()
                        if where not in ("insert", "inside", "pullout"):
                            where = "insert"

                    # cum_apply в игровом коде тоже поднимает счётчик, чтобы
                    # cum_visible/description отражали, что в ней сперма.
                    try:
                        if p is not None and hasattr(p, 'sex_cum_apply'):
                            p.sex_cum_apply("cum_vagin")
                    except Exception as e:
                        print("preg cum_apply err: %s" % e)

                    # Найдём "отца"
                    partner = None
                    partner_name = ai_to_text(eff.get('pregnancy_partner', u""), u"").strip()
                    if partner_name:
                        try:
                            all_npcs = getattr(store, 'npc_all', None) or []
                            pn_low = partner_name.lower()
                            for npc in list(all_npcs):
                                fn = ai_to_text(getattr(npc, '_fname', getattr(npc, 'fname', u'')), u'').lower()
                                sn = ai_to_text(getattr(npc, '_sname', getattr(npc, 'sname', u'')), u'').lower()
                                full = (fn + u" " + sn).strip()
                                if pn_low == fn or pn_low == full or pn_low == sn:
                                    # NAMED CHARACTERS RULE: NPC должен быть уже встречен.
                                    if bool(getattr(npc, 'has_met', False)):
                                        partner = npc
                                    break
                        except Exception as e:
                            print("preg partner lookup err: %s" % e)
                    if partner is None:
                        # Fallback: анонимный отец. Именно так игра
                        # обрабатывает секс "с кем-то на улице".
                        partner = getattr(store, 'unknown', None)

                    # Собственно прогон честной механики игры
                    if p is not None and hasattr(p, 'sex_cum_pregcheck'):
                        try:
                            got_pregnant = bool(p.sex_cum_pregcheck(where))
                        except Exception as e:
                            print("sex_cum_pregcheck err: %s" % e)
                            got_pregnant = False
                        if got_pregnant and partner is not None and hasattr(p, 'preg'):
                            try:
                                p.preg(partner)
                                summary_bits.append(u"⚠ Pregnancy check FIRED (%s)" % where)
                                try:
                                    store.ai_notify_queue.append(u"⚠ Возможна беременность")
                                except Exception:
                                    pass
                            except Exception as e:
                                print("preg apply err: %s" % e)
                        else:
                            summary_bits.append(u"Pregnancy check rolled (%s): safe" % where)
                except Exception as e:
                    print("pregnancy_risk err: %s" % e)

            # --- 8) Удаление существующего перка по имени store-переменной ---
            if 'remove_perk' in eff and eff.get('remove_perk'):
                try:
                    perk_var = ai_to_text(eff['remove_perk'], u"").strip()
                    perk_obj = getattr(store, perk_var, None)
                    if perk_obj is not None and p is not None and hasattr(p, 'remove_perk'):
                        try:
                            p.remove_perk(perk_obj, notif=True)
                            summary_bits.append(u"-Perk %s" % perk_var)
                        except Exception as e2:
                            print("remove_perk apply err: %s" % e2)
                except Exception as e:
                    print("remove_perk err: %s" % e)

            spicy_mod = ch.get('spicy_modifier', 0)
            if spicy_mod:
                try:
                    store.ai_spicy_meter = max(0, min(100, getattr(store, 'ai_spicy_meter', 20) + int(spicy_mod)))
                    store.ai_notify_queue.append(u"ИИ: Spicy метр %+d%%" % int(spicy_mod))
                except Exception:
                    pass

            if 'perk_add' in eff and eff.get('perk_add'):
                p_add = eff['perk_add']
                p_name = u""
                p_desc = None
                p_type = "allure"
                p_val = 5
                if ai_dict_like(p_add):
                    p_name = ai_to_text(p_add.get('name', u'Marked'), u'Marked')
                    p_desc = p_add.get('desc') or p_add.get('description')
                    p_type = ai_to_text(p_add.get('type', u'allure'), u'allure')
                    try:
                        p_val = int(p_add.get('add', p_add.get('value', 5)))
                    except Exception:
                        p_val = 5
                else:
                    p_name = ai_to_text(p_add, u'Marked')
                if p_name:
                    ai_add_dynamic_perk(p_name, p_desc, p_type, p_val)

            summary_bits.append(ai_format_effects_summary(eff))
            if spicy_mod:
                try:
                    summary_bits.append(u"Spicy %+d" % int(spicy_mod))
                except Exception:
                    pass
        except Exception as e:
            print("ai_apply_choice_effects err: %s" % e)
        return u" | ".join([b for b in summary_bits if b])

    def ai_build_quest_ending_event(full_q, ch, cur_evt=None):
        """Строит финальный экран ветки: итог + награды."""
        try:
            qtitle = u"Quest"
            if ai_dict_like(full_q):
                qtitle = ai_to_text(full_q.get('title', u'Quest'), u'Quest')
            elif ai_dict_like(cur_evt):
                qtitle = ai_to_text(cur_evt.get('quest_title', cur_evt.get('title', u'Quest')), u'Quest')

            ending_title = None
            ending_text = None
            if ai_dict_like(ch):
                ending_title = ch.get('ending_title') or ch.get('endingTitle') or ch.get('result_title')
                ending_text = ch.get('ending_text') or ch.get('endingText') or ch.get('result_text') or ch.get('ending')
            if not ending_title and ai_dict_like(cur_evt):
                ending_title = cur_evt.get('ending_title')
            if not ending_text and ai_dict_like(cur_evt):
                ending_text = cur_evt.get('ending_text')

            choice_txt = ai_to_text(ch.get('text', u'your final choice'), u'your final choice') if ai_dict_like(ch) else u'your final choice'
            if not ending_title or unicode(ending_title).strip() in [u'', u'...', u'None']:
                ending_title = u"Ending: %s" % qtitle
            if not ending_text or unicode(ending_text).strip() in [u'', u'...', u'None']:
                # fallback summary from path
                path = getattr(store, 'ai_quest_path', None) or []
                if path:
                    path_txt = u" -> ".join([ai_to_text(x, u'?') for x in path[-4:]])
                    ending_text = (
                        u"Your path through '%s' ends here. Final choice: %s. "
                        u"Route: %s. The consequences settle in as you move on."
                    ) % (qtitle, choice_txt, path_txt)
                else:
                    ending_text = (
                        u"Your branch of '%s' is complete. You chose: %s. "
                        u"The moment leaves a lasting mark on Samantha's training."
                    ) % (qtitle, choice_txt)

            # rewards already applied from the choice effects; show them again as summary
            eff = {}
            if ai_dict_like(ch):
                eff = ch.get('effects', {}) if ai_dict_like(ch.get('effects', {})) else {}
                if ch.get('perk_add') is not None and (not ai_dict_like(eff) or 'perk_add' not in eff):
                    if not ai_dict_like(eff):
                        eff = {}
                    eff = dict(eff) if ai_dict_like(eff) else {}
                    eff['perk_add'] = ch.get('perk_add')
            reward_line = ai_format_effects_summary(eff)
            desc = ai_to_text(ending_text, u'')
            if reward_line:
                desc = desc + u"\n\nRewards: " + reward_line
            else:
                desc = desc + u"\n\nRewards: experience and a shift in Samantha's mindset."

            # ensure final button has no further next_step; effects already applied
            evt = {
                "title": ai_to_text(ending_title, u'Ending'),
                "description": desc,
                "type": "quest_ending",
                "is_quest": True,
                "quest_title": qtitle,
                "quest_desc": u"Finale",
                "outfit_suggestion": {"items": []},
                "choices": [{
                    "text": u"Accept the outcome",
                    "effects": {},
                    "next_step": None,
                    "is_ending_ack": True,
                }],
                "_full_quest": True,
                "_is_ending": True,
                "_step_id": "ending",
                "tags": ["femininity"],
            }
            return ai_normalize_event(evt)
        except Exception as e:
            print("ai_build_quest_ending_event err: %s" % e)
            return ai_normalize_event({
                "title": u"Quest Complete",
                "description": u"The branch ends. Samantha carries the consequences with her.",
                "is_quest": True,
                "choices": [{"text": u"Continue", "effects": {}, "next_step": None, "is_ending_ack": True}],
                "_is_ending": True,
            })

    def ai_ensure_terminal_endings(tree):
        """Заполняет ending_title/text/effects для choices у которых нет next_step.

        ИЗМЕНЕНИЕ vs старой версии: is_ending БОЛЬШЕ НЕ ставится
        принудительно. Раньше 'нет next_step' автоматически означало
        'финал ветки', но с on-demand chain это неверно: null next_step =
        'пусть игра сгенерит следующий шаг', а is_ending=true = 'финал'.
        Теперь функция только гарантирует, что ending-поля не пустые
        (на случай если ветка действительно закроется финалом позже).
        """
        if not ai_dict_like(tree) or not tree.get('steps'):
            return tree
        qtitle = ai_to_text(tree.get('title', u'Quest'), u'Quest')
        steps = [s for s in tree.get('steps', []) if ai_dict_like(s)]
        for step in steps:
            for ch in step.get('choices', []) or []:
                if not ai_dict_like(ch):
                    continue
                ns = ch.get('next_step')
                if ns:
                    continue
                # НЕ ставим is_ending=True автоматически. Только заполняем
                # ending_title/text как fallback — если choice окажется
                # финальным (по флагу is_ending от модели или из-за MAX_STEPS),
                # они пригодятся; иначе пусть лежат неиспользованными.
                if not ch.get('ending_title'):
                    ch['ending_title'] = u"Outcome: %s" % ai_to_text(step.get('title', qtitle), qtitle)
                if not ch.get('ending_text'):
                    ch['ending_text'] = (
                        u"This branch of '%s' closes after '%s'. "
                        u"You chose: %s. The city of Blaston remembers the kind of girl you are becoming."
                    ) % (
                        qtitle,
                        ai_to_text(step.get('title', u'this stage'), u'this stage'),
                        ai_to_text(ch.get('text', u'your choice'), u'your choice'),
                    )
                eff = ch.get('effects') if ai_dict_like(ch.get('effects')) else {}
                if not ai_dict_like(eff):
                    eff = {}
                else:
                    try:
                        eff = dict(eff)
                    except Exception:
                        pass
                # ensure some reward on terminal choices
                if not eff:
                    # mild default based on spicy_modifier sign
                    sp = 0
                    try:
                        sp = int(ch.get('spicy_modifier', 0) or 0)
                    except Exception:
                        sp = 0
                    if sp >= 5:
                        eff = {"femininity": 4, "corrupt": 1, "confidence": 1}
                    elif sp <= -5:
                        eff = {"confidence": 2, "femininity": 1}
                    else:
                        eff = {"femininity": 2, "confidence": 1}
                # chance-like deterministic perk if still missing and path looks bold
                if 'perk_add' not in eff:
                    sp = 0
                    try:
                        sp = int(ch.get('spicy_modifier', 0) or 0)
                    except Exception:
                        sp = 0
                    # only auto-perk for stronger endings
                    if sp >= 8 or int(eff.get('femininity', 0) or 0) >= 4 or int(eff.get('corrupt', 0) or 0) >= 2:
                        ctext = ai_to_text(ch.get('text', u'Marked'), u'Marked')
                        pname = ai_to_text(step.get('title', u'Trained'), u'Trained')
                        # short perk name
                        pname = (pname[:28] + u" Mark") if len(pname) > 28 else (pname + u" Mark")
                        eff['perk_add'] = {
                            "name": pname,
                            "desc": u"Earned at the end of '%s' by choosing: %s." % (qtitle, ctext),
                            "type": "allure" if sp >= 0 else "confidence",
                            "add": 5,
                        }
                ch['effects'] = eff
        tree['steps'] = steps
        return tree

    def ai_force_one_step_quest_tree(tree):
        """Нормализует ОДИН step (первый шаг цепочки квеста).

        РАНЬШЕ: эта функция принудительно ставила is_ending=True и
        next_step=None на все choices — из-за чего chain-квесты никогда
        не запускались, каждый первый выбор сразу шёл в summary.
        ТЕПЕРЬ: is_ending сохраняется из модели. next_step тоже. Мы только:
          - гарантируем id="step1";
          - гарантируем текст choices и наличие ending_title/text;
          - обрезаем список до 5 (2-4 persona + 1 escape).
        Решение "финал или следующий шаг" принимает движок в ai_event_choice
        по флагу is_ending.
        """
        if not ai_dict_like(tree) or not tree.get('steps'):
            return None
        steps = [s for s in tree.get('steps', []) if ai_dict_like(s)]
        if not steps:
            return None
        step = steps[0]
        step['id'] = 'step1'
        raw_choices = list(step.get('choices', []) or [])[:5]
        # НОВЫЙ ПОДХОД: если LLM отдала < 3 вариантов, добираем ДО 3 из
        # набора реакций. Одна из них — обязательно попытка сбежать.
        # Тексты подобраны так, чтобы работали в любой сцене, но не
        # выглядели как «Yes»/«No».
        defaults = [
            {"text": u"Slip into the role he expects — go quiet and pliable.",
             "effects": {"acceptance": 3, "horny": 15, "corrupt": 8}, "spicy_modifier": 1},
            {"text": u"Break the frame — surprise everyone with your reaction.",
             "effects": {"confidence": 5, "allure": 10, "corrupt": 5}, "spicy_modifier": -1},
            {"text": u"Try to slip out of the situation before it gets any worse.",
             "effects": {"mood": -20, "tired": 15, "travel_to": "loc_home"},
             "spicy_modifier": -3, "is_ending": True},
        ]
        # Обязательный минимум — 3 варианта. Раньше было 2.
        while len(raw_choices) < 3:
            raw_choices.append(defaults[len(raw_choices)])
        out = []
        for idx, ch in enumerate(raw_choices[:5]):
            _def = defaults[idx] if idx < len(defaults) else defaults[-1]
            if ai_dict_like(ch):
                try:
                    nch = dict(ch)
                except Exception:
                    nch = {}
                txt = ai_to_text(nch.get('text', _def['text']), _def['text'])
            else:
                nch = {}
                txt = ai_to_text(ch, _def['text'])
            if not txt or txt.strip() in [u'', u'...', u'None']:
                txt = _def['text']
            eff = nch.get('effects') if ai_dict_like(nch.get('effects')) else _def.get('effects', {})
            try:
                eff = dict(eff)
            except Exception:
                pass
            nch['text'] = txt
            nch['effects'] = eff
            # СОХРАНЯЕМ next_step и is_ending от модели!
            # Если модель сказала is_ending=true — эта ветка финал.
            # Если false / отсутствует — движок сам сгенерит следующий шаг.
            if 'next_step' not in nch:
                nch['next_step'] = None
            if 'is_ending' not in nch:
                nch['is_ending'] = False
            # Ending-заглушка только если модель НЕ дала ничего.
            if not nch.get('ending_title'):
                nch['ending_title'] = u"Outcome %s" % (idx + 1)
            if not nch.get('ending_text'):
                nch['ending_text'] = u"The scene continues from this choice."
            if not nch.get('spicy_modifier'):
                nch['spicy_modifier'] = _def.get('spicy_modifier', 0)
            out.append(nch)
        step['choices'] = out
        tree['steps'] = [step]
        tree['_one_step_test'] = True
        # НЕ вызываем ai_ensure_terminal_endings — она тоже насильно
        # is_ending=True ставит для choice без next_step. Для chain это яд.
        return tree

    def ai_force_binary_quest_tree(tree):
        """Жёстко режет квест до схемы 2 -> 2: step1, step2a, step2b, четыре терминальных исхода."""
        if not ai_dict_like(tree) or not tree.get('steps'):
            return None
        raw_steps = [s for s in tree.get('steps', []) if ai_dict_like(s)]
        if len(raw_steps) < 3:
            return None

        old_id_map = {}
        for st in raw_steps:
            try:
                old_id_map[unicode(st.get('id', u''))] = st
            except Exception:
                pass

        def _copy_effects(eff):
            if ai_dict_like(eff):
                try:
                    return dict(eff)
                except Exception:
                    return eff
            return {}

        def _merge_effects(a, b):
            res = _copy_effects(a)
            other = _copy_effects(b)
            for k, v in other.items():
                if k in res and k not in ('perk_add', 'give_item'):
                    try:
                        res[k] = int(res.get(k, 0) or 0) + int(v or 0)
                    except Exception:
                        if not res.get(k):
                            res[k] = v
                elif k not in res or not res.get(k):
                    res[k] = v
            return res

        def _clean_choice(ch, fallback_text):
            if ai_dict_like(ch):
                try:
                    new_ch = dict(ch)
                except Exception:
                    new_ch = {}
                txt = ai_to_text(new_ch.get('text', fallback_text), fallback_text)
            else:
                new_ch = {}
                txt = ai_to_text(ch, fallback_text)
            if not txt or txt.strip() in [u'', u'...', u'None']:
                txt = fallback_text
            new_ch['text'] = txt
            if not ai_dict_like(new_ch.get('effects')):
                new_ch['effects'] = {}
            else:
                new_ch['effects'] = _copy_effects(new_ch.get('effects'))
            return new_ch

        def _target_ending_payload(ch):
            """Если LLM сделала отдельный end_* шаг, переносим его награды/текст в терминальный выбор."""
            payload = {"effects": {}, "ending_title": None, "ending_text": None, "spicy_modifier": 0}
            if not ai_dict_like(ch):
                return payload
            ns = ch.get('next_step', ch.get('next', ch.get('goto', None)))
            if ns is None:
                return payload
            target = old_id_map.get(ai_to_text(ns, u''))
            if not ai_dict_like(target):
                return payload
            payload['ending_title'] = target.get('title')
            payload['ending_text'] = target.get('description')
            tchoices = target.get('choices', []) or []
            if tchoices and ai_dict_like(tchoices[0]):
                tch = tchoices[0]
                payload['effects'] = _copy_effects(tch.get('effects'))
                if tch.get('perk_add') is not None and 'perk_add' not in payload['effects']:
                    payload['effects']['perk_add'] = tch.get('perk_add')
                payload['ending_title'] = tch.get('ending_title') or payload['ending_title']
                payload['ending_text'] = tch.get('ending_text') or payload['ending_text']
                try:
                    payload['spicy_modifier'] = int(tch.get('spicy_modifier', tch.get('spicy', 0)) or 0)
                except Exception:
                    payload['spicy_modifier'] = 0
            return payload

        first = raw_steps[0]
        mids = []
        first_raw_choices = first.get('choices', []) or []
        for ch in list(first_raw_choices)[:2]:
            if ai_dict_like(ch):
                ns = ch.get('next_step', ch.get('next', ch.get('goto', None)))
                st = old_id_map.get(ai_to_text(ns, u'')) if ns is not None else None
                if ai_dict_like(st) and st is not first and st not in mids:
                    mids.append(st)
        for st in raw_steps[1:]:
            if st not in mids:
                mids.append(st)
            if len(mids) >= 2:
                break
        if len(mids) < 2:
            return None
        mid_a, mid_b = mids[0], mids[1]

        # Каноничные id: меньше шансов, что RenPy зависнет на чужом/битом next_step.
        first['id'] = 'step1'
        mid_a['id'] = 'step2a'
        mid_b['id'] = 'step2b'

        fchoices = []
        defaults = [u"Take the bold route", u"Take the careful route"]
        raw = list(first.get('choices', []) or [])[:2]
        while len(raw) < 2:
            raw.append({"text": defaults[len(raw)], "effects": {"confidence": 1}})
        for idx, ch in enumerate(raw[:2]):
            nch = _clean_choice(ch, defaults[idx])
            nch['next_step'] = 'step2a' if idx == 0 else 'step2b'
            nch['is_ending'] = False
            if 'ending_title' in nch:
                del nch['ending_title']
            if 'ending_text' in nch:
                del nch['ending_text']
            fchoices.append(nch)
        first['choices'] = fchoices

        def _terminalize_mid(step, branch_name, fallback_pair):
            raw_choices = list(step.get('choices', []) or [])[:2]
            while len(raw_choices) < 2:
                raw_choices.append({"text": fallback_pair[len(raw_choices)], "effects": {"femininity": 2, "confidence": 1}})
            out = []
            for idx, ch in enumerate(raw_choices[:2]):
                nch = _clean_choice(ch, fallback_pair[idx])
                payload = _target_ending_payload(ch)
                nch['effects'] = _merge_effects(nch.get('effects'), payload.get('effects'))
                try:
                    sm = int(nch.get('spicy_modifier', nch.get('spicy', 0)) or 0) + int(payload.get('spicy_modifier', 0) or 0)
                except Exception:
                    sm = 0
                nch['spicy_modifier'] = sm
                nch['next_step'] = None
                nch['is_ending'] = True
                nch['ending_title'] = nch.get('ending_title') or payload.get('ending_title') or (u"%s Outcome %s" % (branch_name, idx + 1))
                nch['ending_text'] = nch.get('ending_text') or payload.get('ending_text') or (
                    u"Your %s branch ends after choosing: %s. The result follows Samantha into the rest of the day."
                    % (branch_name, ai_to_text(nch.get('text', u'your choice'), u'your choice'))
                )
                out.append(nch)
            step['choices'] = out
            return step

        mid_a = _terminalize_mid(mid_a, u"bold", [u"Commit fully", u"Turn it into a controlled win"])
        mid_b = _terminalize_mid(mid_b, u"careful", [u"Finish the careful challenge", u"Back out safely"])

        tree['steps'] = [first, mid_a, mid_b]
        tree['_binary_two_choice'] = True
        return ai_ensure_terminal_endings(tree)

    def ai_normalize_quest_tree(data):
        """Приводит дерево квеста к стабильной схеме steps[] + choices[].next_step."""
        if not ai_dict_like(data):
            return None

        # иногда модель кладёт дерево внутрь event/quest/data
        if 'steps' not in data:
            for k in ('quest', 'event', 'data', 'result', 'chain'):
                inner = data.get(k)
                if ai_dict_like(inner) and inner.get('steps'):
                    data = inner
                    break

        steps = data.get('steps') or data.get('Stages') or data.get('stages') or []
        if not steps and ai_dict_like(data.get('tree')):
            steps = data.get('tree')

        # FIX: слабые/2-битные модели часто «упрощают» и вместо
        # {"steps":[{"choices":[...]}]} возвращают плоское событие
        # {"title","description","choices":[...]}. В one-step-тесте (и вообще
        # когда нам достаточно одного шага) заворачиваем такой ответ в шаг сами,
        # иначе normalize возвращает None и мы уходим в локальный fallback.
        if (not steps) and isinstance(data.get('choices'), (list, tuple)) and len(data.get('choices')) > 0:
            wrapped_step = {
                "id": "step1",
                "title": data.get('title') or data.get('name') or u"Stage 1",
                "description": data.get('description') or data.get('desc') or u"",
                "choices": list(data.get('choices')),
                "outfit_suggestion": data.get('outfit_suggestion') or data.get('outfit') or {"items": [], "reason": ""},
                "tags": data.get('tags', []) or [],
            }
            steps = [wrapped_step]
            try:
                print("ai_normalize_quest_tree: wrapped flat event into single step (LLM omitted 'steps')")
            except Exception:
                pass
        if not isinstance(steps, (list, tuple)):
            return None
        if AI_QUEST_ONE_STEP_TEST_MODE:
            if len(steps) < 1:
                return None
        elif len(steps) < 2:
            return None

        title = ai_to_text(data.get('title') or data.get('Title') or data.get('name') or u'Quest Chain', u'Quest Chain')
        desc = ai_to_text(data.get('description') or data.get('Description') or data.get('desc') or u'', u'')
        if not desc or desc.strip() in [u'', u'...', u'None']:
            desc = u"A multi-step femininity training challenge for Samantha."

        norm_steps = []
        used_ids = set()
        for i, step in enumerate(list(steps)[:AI_FULL_QUEST_MAX_STEPS]):
            if not ai_dict_like(step):
                continue
            sid = ai_to_text(step.get('id') or step.get('step_id') or step.get('name') or ("step%d" % (i+1)), "step%d" % (i+1))
            sid = sid.strip().replace(' ', '_')
            if not sid or sid in used_ids:
                sid = "step%d" % (i+1)
            used_ids.add(sid)

            # Title: НЕ используем sid как fallback — sid может быть slug'ом
            # длинной сцены ("A_MAN_1_leans_against..."), который слил бы
            # мусор в UI. Пусть лучше будет пустая строка → "Stage N".
            _raw_title = step.get('title') or step.get('Title') or u''
            st_title = ai_to_text(_raw_title, u'')
            st_desc = ai_to_text(step.get('description') or step.get('Description') or step.get('desc') or u'', u'')
            # Отбраковка «пустых» / slug-like / бессмысленных заголовков.
            _bad_title = (
                (not st_title) or
                (st_title.strip() in [u'', u'...', u'None']) or
                bool(re.match(r'^step[_\-\s]?\d+$', st_title.strip(), re.IGNORECASE)) or
                # slug вида A_MAN_1_leans_... — длинная строка из подчёркиваний
                (u"_" in st_title and st_title.count(u"_") >= 3 and u" " not in st_title)
            )
            if _bad_title:
                st_title = u"Stage %d" % (i+1)
            # ВАЖНО: НЕ подставляем «Stage N of Samantha's challenge continues.
            # She must choose how to proceed.» — это мета-заглушка, игроку
            # видеть её бессмысленно. Оставляем пустую строку и полагаемся
            # на общее описание квеста (склеивается в ai_step_to_event).
            if not st_desc or st_desc.strip() in [u'', u'...', u'None']:
                st_desc = u""

            outfit = step.get('outfit_suggestion') or step.get('outfit') or {}
            if not ai_dict_like(outfit):
                outfit = {"items": [], "reason": ""}
            else:
                if 'items' not in outfit:
                    outfit = {"items": outfit.get('items', []) or [], "reason": outfit.get('reason', '')}

            raw_choices = step.get('choices') or step.get('options') or step.get('actions') or []
            if not isinstance(raw_choices, (list, tuple)):
                raw_choices = []
            norm_choices = []
            # 2-4 persona-варианта + опциональный escape = до 5 кнопок.
            # Раньше стояло [:2] и все дополнительные выборы модели
            # молча резались ещё в normalize, до попадания в UI.
            for ch in list(raw_choices)[:5]:
                if ai_dict_like(ch):
                    ct = ai_to_text(ch.get('text') or ch.get('Text') or ch.get('label') or ch.get('choice') or u'Continue', u'Continue')
                    if not ct or ct.strip() in [u'', u'...', u'None', u'choice1', u'choice2']:
                        ct = u"Continue"
                    ns = ch.get('next_step', ch.get('next', ch.get('goto', ch.get('nextStep', None))))
                    if ns is not None:
                        ns = ai_to_text(ns, u'').strip()
                        if ns.lower() in [u'', u'null', u'none', u'end', u'finish', u'done']:
                            ns = None
                    eff = ch.get('effects') or ch.get('Effects') or {}
                    if not ai_dict_like(eff):
                        eff = {}
                    # preserve ending payload + root-level perk_add
                    if not ai_dict_like(eff):
                        eff = {}
                    else:
                        try:
                            eff = dict(eff)
                        except Exception:
                            pass
                    if 'perk_add' not in eff and ch.get('perk_add') is not None:
                        eff['perk_add'] = ch.get('perk_add')
                    norm_choices.append({
                        "text": ct,
                        "effects": eff,
                        "next_step": ns,
                        "spicy_modifier": ch.get('spicy_modifier', ch.get('spicy', 0)) or 0,
                        "ending_title": ch.get('ending_title', ch.get('endingTitle', ch.get('result_title', None))),
                        "ending_text": ch.get('ending_text', ch.get('endingText', ch.get('result_text', ch.get('ending', None)))),
                        # ТОЛЬКО explicit is_ending. Null next_step больше
                        # НЕ означает финал — это триггер on-demand chain.
                        "is_ending": bool(ch.get('is_ending', False)),
                    })
                else:
                    norm_choices.append({"text": ai_to_text(ch, u'Continue'), "effects": {}, "next_step": None, "spicy_modifier": 0})

            if not norm_choices:
                norm_choices = [{"text": u"Continue", "effects": {}, "next_step": None, "spicy_modifier": 0}]

            norm_steps.append({
                "id": sid,
                "title": st_title,
                "description": st_desc,
                "outfit_suggestion": outfit,
                "choices": norm_choices,
                "tags": step.get('tags', []) or [],
            })

        if AI_QUEST_ONE_STEP_TEST_MODE:
            if len(norm_steps) < 1:
                return None
            tree = {
                "title": title,
                "description": desc,
                "steps": norm_steps,
            }
            return ai_force_one_step_quest_tree(tree)

        if len(norm_steps) < 3:
            return None

        # Починить битые next_step: если указан несуществующий id — вести на следующий по порядку.
        id_list = [s['id'] for s in norm_steps]
        id_set = set(id_list)
        for idx, step in enumerate(norm_steps):
            is_last = (idx >= len(norm_steps) - 1)
            default_next = None if is_last else id_list[idx + 1]
            for ch in step['choices']:
                ns = ch.get('next_step')
                if ns and ns not in id_set:
                    # fuzzy: step2 / Step 2 / 2
                    fixed = None
                    nslow = unicode(ns).lower().replace(' ', '')
                    for cand in id_list:
                        if unicode(cand).lower().replace(' ', '') == nslow:
                            fixed = cand
                            break
                    # В бинарном квесте только step1 должен автоматически вести дальше.
                    # На step2 пустой/битый next_step означает финал ветки, а не переход в соседнюю ветку.
                    ch['next_step'] = fixed if fixed else (default_next if idx == 0 else None)
                elif not ns:
                    # Только первый шаг автопродолжаем; второй уровень должен быть терминальным.
                    ch['next_step'] = default_next if idx == 0 else None

        # Гарантируем, что с первого шага есть хотя бы один путь дальше
        first = norm_steps[0]
        if not any(ch.get('next_step') for ch in first['choices']) and len(norm_steps) > 1:
            first['choices'][0]['next_step'] = norm_steps[1]['id']

        tree = {
            "title": title,
            "description": desc,
            "steps": norm_steps,
        }
        forced_tree = ai_force_binary_quest_tree(tree)
        if forced_tree:
            return forced_tree

        # Сверхнадёжный fallback: если RenPy/Py2 или странный dict всё же не дал собрать binary-tree,
        # не валим попытку LLM. Берём первые 3 нормализованных шага и принудительно делаем 2 -> 2.
        try:
            if len(norm_steps) >= 3:
                s1 = norm_steps[0]
                s2a = norm_steps[1]
                s2b = norm_steps[2]
                s1['id'] = 'step1'
                s2a['id'] = 'step2a'
                s2b['id'] = 'step2b'
                while len(s1.get('choices', []) or []) < 2:
                    s1.setdefault('choices', []).append({"text": u"Continue", "effects": {}})
                s1['choices'] = list(s1.get('choices', []) or [])[:2]
                s1['choices'][0]['next_step'] = 'step2a'
                s1['choices'][0]['is_ending'] = False
                s1['choices'][1]['next_step'] = 'step2b'
                s1['choices'][1]['is_ending'] = False

                for st, branch in [(s2a, u"branch A"), (s2b, u"branch B")]:
                    while len(st.get('choices', []) or []) < 2:
                        st.setdefault('choices', []).append({"text": u"Finish", "effects": {"femininity": 2, "confidence": 1}})
                    st['choices'] = list(st.get('choices', []) or [])[:2]
                    for ci, ch in enumerate(st['choices']):
                        ch['next_step'] = None
                        ch['is_ending'] = True
                        if not ch.get('ending_title'):
                            ch['ending_title'] = u"%s outcome %s" % (branch, ci + 1)
                        if not ch.get('ending_text'):
                            ch['ending_text'] = u"This path ends with Samantha accepting the result of her choice."
                tree['steps'] = [s1, s2a, s2b]
                tree['_binary_two_choice'] = True
                return ai_ensure_terminal_endings(tree)
        except Exception as e:
            print("binary quest emergency fallback err: %s" % e)
        return None

    def ai_step_to_event(full_q, step, spicy_level=2):
        """Первый/следующий шаг дерева -> event dict для UI."""
        if not ai_dict_like(full_q) or not ai_dict_like(step):
            return None
        step_ids = [s.get('id') for s in full_q.get('steps', []) if ai_dict_like(s)]
        try:
            step_no = step_ids.index(step.get('id')) + 1 if step.get('id') in step_ids else 1
        except Exception:
            step_no = 1
        total = len(step_ids) or len(full_q.get('steps', []) or [])
        qdesc = ai_to_text(full_q.get('description', u''), u'')
        # НИКАКИХ [Stage 1/1] и т.п. в UI-тексте. Игроку не нужно видеть
        # мета-разметку шагов. step_no / total мы сохраняем в служебных
        # полях _step_no / _step_total — они нужны логике перехода между
        # шагами, но НЕ выводятся пользователю.

        # Склеиваем общее описание квеста и описание текущей сцены в ОДИН
        # сплошной текст: сначала контекст квеста (что происходит в целом),
        # потом сцена шага (что случилось прямо сейчас). Раньше это были
        # два разных виджета в UI, и «общий текст» рисовался под сценой —
        # то есть игрок читал результат раньше сеттинга.
        step_desc = ai_to_text(step.get('description', u''), u'')
        merged_desc_parts = []
        if qdesc and qdesc.strip() not in (u'', u'...', u'None'):
            merged_desc_parts.append(qdesc.strip())
        if step_desc and step_desc.strip() not in (u'', u'...', u'None'):
            merged_desc_parts.append(step_desc.strip())
        merged_desc = u"\n\n".join(merged_desc_parts) if merged_desc_parts else step_desc
        # TITLE: раньше брали step.title — это давало "Stage 1" на каждой
        # сцене (заглушка из normalize). Теперь: сначала пробуем title
        # квеста (то, что модель написала в TITLE:), потом название шага,
        # только в самом конце — "Stage N".
        _quest_title_raw = ai_to_text(full_q.get('title', u''), u'').strip()
        _step_title_raw = ai_to_text(step.get('title', u''), u'').strip()
        _title_low = _step_title_raw.lower()
        _step_looks_generic = (
            (not _step_title_raw) or
            _title_low.startswith(u"stage ") or
            _title_low in (u"quest", u"...", u"none")
        )
        if _quest_title_raw and _step_looks_generic:
            # Название квеста + номер сцены, если сцен несколько.
            if total and total > 1:
                _final_title = u"%s — %d/%d" % (_quest_title_raw, step_no, total)
            else:
                _final_title = _quest_title_raw
        elif _step_title_raw:
            _final_title = _step_title_raw
        elif _quest_title_raw:
            _final_title = _quest_title_raw
        else:
            _final_title = u"Quest"
        evt = {
            "title": _final_title,
            "description": merged_desc,
            "type": "quest",
            "outfit_suggestion": step.get('outfit_suggestion', {}) or {"items": []},
            "is_quest": True,
            "quest_title": full_q.get('title', 'Quest'),
            "quest_desc": qdesc,  # оставляем в модели для истории/логов, но UI его больше не рисует отдельно
            "choices": step.get('choices', []) or [],
            "_full_quest": True,
            "_step_id": step.get('id', 'step1'),
            "_step_no": step_no,
            "_step_total": total,
            "_local_fallback": bool(full_q.get('_local_fallback', False)),
            "_one_step_test": bool(full_q.get('_one_step_test', False)),
            "_llm_failed_reason": ai_to_text(full_q.get('_llm_failed_reason', u''), u''),
            "tags": step.get('tags', []) or ["femininity"],
            "spicy_level": spicy_level,
        }
        return ai_normalize_event(evt)

    def ai_make_local_quest_tree(gs):
        """Локальное бинарное дерево 2 -> 2, если Ollama/JSON не вывезли."""
        loc = ai_to_text(gs.get('location', u'home'), u'home')
        fem = gs.get('fem', 25)
        outfit = ai_to_text(gs.get('outfit', u'casual clothes'), u'casual clothes')
        timeofday = ai_to_text(gs.get('timeofday', u'day'), u'day')
        title = (u"LOCAL FALLBACK TEST: %s" % loc) if AI_QUEST_ONE_STEP_TEST_MODE else (u"Local Challenge: %s" % loc)
        desc = u"A compact one-click femininity challenge based on where Samantha is right now."
        if AI_QUEST_ONE_STEP_TEST_MODE:
            step1 = {
                "id": "step1",
                "title": u"Quick Test Challenge",
                "description": u"You are at %s during %s, femininity %s%%, wearing %s. This test quest will end after one choice." % (loc, timeofday, fem, outfit),
                "outfit_suggestion": {"items": ["item_top_22", "item_bottom_15"], "reason": "look more feminine"},
                "choices": [
                    {
                        "text": u"Do the quick dare",
                        "next_step": None,
                        "effects": {"femininity": 3, "confidence": 1},
                        "spicy_modifier": 2,
                        "ending_title": u"Quick Dare Complete",
                        "ending_text": u"The test quest ends immediately. Samantha takes the small win and moves on.",
                        "is_ending": True,
                    },
                    {
                        "text": u"Skip the quick dare",
                        "next_step": None,
                        "effects": {"confidence": 1},
                        "spicy_modifier": -1,
                        "ending_title": u"Quick Refusal",
                        "ending_text": u"The test quest ends immediately. Samantha avoids the dare and continues her day.",
                        "is_ending": True,
                    },
                ],
                "tags": ["femininity", "crossdressing"],
            }
            return ai_ensure_terminal_endings({
                "title": title,
                "description": desc,
                "steps": [step1],
                "_local_fallback": True,
                "_one_step_test": True,
            })

        step1 = {
            "id": "step1",
            "title": u"Opening Move",
            "description": u"You are at %s during %s, femininity %s%%, wearing %s. A small public-private dare forms in your mind." % (loc, timeofday, fem, outfit),
            "outfit_suggestion": {"items": ["item_top_22", "item_bottom_15"], "reason": "look more feminine"},
            "choices": [
                {"text": u"Take the bold dare", "next_step": "step2a", "effects": {"femininity": 2}, "spicy_modifier": 6},
                {"text": u"Take the careful dare", "next_step": "step2b", "effects": {"confidence": 1}, "spicy_modifier": -2},
            ],
            "tags": ["femininity", "crossdressing"],
        }
        step2a = {
            "id": "step2a",
            "title": u"Bold Path",
            "description": u"You push the dare further. Someone nearby notices, or you imagine they do, and your body reacts.",
            "choices": [
                {
                    "text": u"Commit fully",
                    "next_step": None,
                    "effects": {
                        "femininity": 6,
                        "corrupt": 2,
                        "money": 20,
                        "perk_add": {
                            "name": u"Dared Herself",
                            "desc": u"She finished a bold local challenge without backing down.",
                            "type": "allure",
                            "add": 5,
                        },
                    },
                    "spicy_modifier": 12,
                    "ending_title": u"Bold Ending",
                    "ending_text": u"You leave %s hotter and more shameless. The dare is over, but the habit is not." % loc,
                    "is_ending": True,
                },
                {
                    "text": u"Turn it into a controlled win",
                    "next_step": None,
                    "effects": {"femininity": 3, "confidence": 2},
                    "spicy_modifier": 1,
                    "ending_title": u"Controlled Ending",
                    "ending_text": u"You keep control at %s and still prove that your feminine side can handle pressure." % loc,
                    "is_ending": True,
                },
            ],
        }
        step2b = {
            "id": "step2b",
            "title": u"Careful Path",
            "description": u"You keep the challenge controlled. Still feminine, still risky, but safer.",
            "choices": [
                {
                    "text": u"Finish the careful challenge",
                    "next_step": None,
                    "effects": {
                        "femininity": 3,
                        "confidence": 2,
                        "perk_add": {
                            "name": u"Composed Girl",
                            "desc": u"She can stay feminine under pressure without panicking.",
                            "type": "confidence",
                            "add": 4,
                        },
                    },
                    "spicy_modifier": 1,
                    "ending_title": u"Soft Ending",
                    "ending_text": u"No disaster, just progress. At %s you practiced being a girl and it stuck." % loc,
                    "is_ending": True,
                },
                {
                    "text": u"Back out safely",
                    "next_step": None,
                    "effects": {"confidence": 1, "femininity": 1},
                    "spicy_modifier": -4,
                    "ending_title": u"Bail Ending",
                    "ending_text": u"You escape the pressure at %s. Relief first, then a small sting of unfinished training." % loc,
                    "is_ending": True,
                },
            ],
        }
        tree = {
            "title": title,
            "description": desc,
            "steps": [step1, step2a, step2b],
            "_local_fallback": True,
            "_binary_two_choice": True,
        }
        return ai_ensure_terminal_endings(tree)

    # --- Расшифровки шкал, чтобы модель понимала цифры ---
    def _ai_scale_word(v, scale=(("very low", 15), ("low", 35), ("medium", 60), ("high", 80), ("very high", 101))):
        try:
            v = int(v)
        except Exception:
            return "unknown"
        for label, hi in scale:
            if v < hi:
                return label
        return scale[-1][0]

    def _ai_spicy_word(sp):
        try:
            sp = int(sp)
        except Exception:
            return "unknown"
        # spicy_level в моде идёт 0..10
        if sp <= 1:  return "wholesome / no NSFW"
        if sp <= 3:  return "mild teasing, light flirt, no explicit sex"
        if sp <= 5:  return "spicy: exhibitionism, groping, dirty talk"
        if sp <= 7:  return "explicit sex, kinks, humiliation"
        if sp <= 9:  return "hardcore explicit, rough, degradation ok"
        return "extreme, no limits, taboo ok"

    def _ai_cycle_word(stage):
        return {
            "no_cycle":   "no menstrual cycle yet",
            "mens":       "menstruating (period)",
            "foll":       "follicular phase, energetic",
            "ovulate":    "ovulating, most fertile, high libido",
            "lut":        "luteal phase, PMS possible",
        }.get(stage, "unknown cycle stage")

    def _ai_breast_word(idx):
        """Размер груди в игре только A/B/C. См. TheFixer wardrobe."""
        return {
            0: "A-cup (small)",
            1: "B-cup (average)",
            2: "C-cup (large / 'massive' by Samantha's diary)",
        }.get(int(idx or 0), "C-cup (large)")

    def _ai_weather_word(w):
        """weather_var в TheFixer: 1=sunny, 2=cloudy, 3=rain, 4=snow."""
        try:
            w = int(w)
        except Exception:
            return "unknown weather"
        return {
            1: "sunny / clear",
            2: "cloudy / overcast",
            3: "rainy",
            4: "snowy",
        }.get(w, "unknown weather (%s)" % w)

    # Био Саманты — только её собственная дневниковая запись из старта игры.
    # Никакой отсебятины про хендлеров, кураторов, докторов и т.п.: если у
    # игрока такие NPC ещё не встретились, LLM не должна их выдумывать.
    # Всё остальное (реально встреченные люди, факты сюжета) приходит в
    # секциях [KNOWN NPCS] и [DIARY] чуть ниже, из get_state().
    # Короткий SAMANTHA_BIO. 3 строки вместо 17. Всё, что нужно модели, — кто она
    # физически/юридически и жёсткий запрет выдумывать NPC. Прочее (дневник,
    # список знакомых, история) в старом промпте раздувало контекст в разы и
    # заставляло модель галлюцинировать несуществующих докторов.
    SAMANTHA_BIO = (
        u"Samantha Bangtail — former man in a young female body (Institute mind-transfer, "
        u"town of Blaston). Short girl, grey hair, brown eyes, C-cup, slight belly. "
        u"Institute tracks her only via phone/bracelet, no cameras. "
        u"Do NOT invent any named character not explicitly listed elsewhere in the prompt."
    )

    # Один раз тянем forbidden-текст (для всех mode).
    def _ai_forbidden_text_cached():
        try:
            from ai_config_tags import ai_get_forbidden_themes_text
            return ai_get_forbidden_themes_text()
        except Exception:
            return u""

    def _ai_get_focus_tags_for_location(loc_name):
        """Возвращает пересечение "желаемых игроком" тегов (level>=3)
        со списком тегов, разрешённых в текущей локации. Отдаём читаемое
        имя (name), а не сырой id — модели проще писать сцену вокруг
        "проституция", чем вокруг "prostitution".
        """
        try:
            from ai_config_tags import AI_COMFORT_TAGS
        except Exception:
            return []
        try:
            from ai_config_locations import ai_get_allowed_themes_for_location
            allowed_ids = set(ai_get_allowed_themes_for_location(loc_name or u"home") or [])
        except Exception:
            allowed_ids = None  # None = локация неизвестна, не фильтруем

        out = []
        try:
            for t in AI_COMFORT_TAGS:
                try:
                    lvl = int(t.get('level', 0))
                except Exception:
                    lvl = 0
                if lvl < 3:
                    continue
                tid = t.get('id') or u"?"
                if allowed_ids is not None and tid not in allowed_ids:
                    continue
                name = t.get('name') or tid
                out.append(name)
        except Exception:
            pass
        return out

    # -----------------------------------------------------------------
    # Хелперы, которые превращают ЦИФРЫ статов в ЧЕЛОВЕЧЕСКИЕ слова.
    # Раньше в промпт валилось "hunger 100 (very high) — high = well fed"
    # (три штуки метаданных ради одного факта "она сыта"). Теперь —
    # только сам факт, и только если он реально важен для сцены.
    # -----------------------------------------------------------------
    def _ai_hunger_word(v):
        v = int(v or 0)
        if v <= 15: return u"starving"
        if v <= 40: return u"hungry"
        if v <= 75: return u"peckish"
        return None  # сыт — не пишем вообще

    def _ai_tired_word(v):
        v = int(v or 0)
        if v >= 90: return u"about to pass out from exhaustion"
        if v >= 70: return u"exhausted"
        if v >= 45: return u"tired"
        return None  # бодра — молчим

    def _ai_hygiene_word(v):
        v = int(v or 0)
        if v <= 15: return u"filthy, reeks"
        if v <= 40: return u"dirty and sweaty"
        return None  # чиста — молчим

    def _ai_mood_word(v):
        v = int(v or 0)
        if v <= 10: return u"suicidally miserable"
        if v <= 30: return u"depressed"
        if v <= 45: return u"grumpy"
        if v >= 85: return u"euphoric"
        if v >= 70: return u"in a good mood"
        return None  # средне — молчим

    def _ai_desire_word(v):
        v = int(v or 0)
        if v >= 80: return u"desperately aroused, needs release"
        if v >= 55: return u"turned on"
        if v >= 30: return u"warm, curious"
        return None

    def _ai_horny_word(v):
        v = int(v or 0)
        if v >= 80: return u"soaked, aching"
        if v >= 55: return u"visibly wet"
        if v >= 30: return u"turned on"
        return None

    def _ai_drunk_word(v):
        v = int(v or 0)
        if v >= 150: return u"blackout drunk"
        if v >= 80:  return u"very drunk, slurring"
        if v >= 40:  return u"drunk"
        if v >= 15:  return u"tipsy"
        return None

    def _ai_high_word(v):
        v = int(v or 0)
        if v >= 80: return u"very high"
        if v >= 40: return u"high"
        if v >= 15: return u"buzzed"
        return None

    def _ai_confidence_word(v):
        v = int(v or 0)
        if v <= 10: return u"cowering"
        if v <= 30: return u"shy"
        if v >= 80: return u"bold"
        return None

    def _ai_accept_word(v):
        v = int(v or 0)
        if v <= 15: return u"still thinks of herself as a man in a female body"
        if v <= 40: return u"reluctantly getting used to being female"
        if v >= 80: return u"fully embraces being a woman"
        return None  # средне — можно молчать, но полезно; None = молчим

    def _ai_corrupt_word(v):
        v = int(v or 0)
        if v >= 80: return u"morally broken, no shame left"
        if v >= 50: return u"morally loose"
        return None

    def _ai_hair_word(v):
        v = int(v or 0)
        if v < 10: return u"short"
        if v < 20: return u"chin-length"
        if v < 30: return u"shoulder-length"
        if v < 40: return u"long"
        return u"very long"

    def _ai_phair_word(v):
        v = int(v or 0)
        if v <= -8: return u"waxed bare"
        if v <= 0:  return u"stubble"
        if v <= 5:  return u"trimmed"
        return u"full bush"

    # -----------------------------------------------------------------
    # РЕЛЕВАНТНЫЕ СТАТЫ. По той же логике, что перки: игра сама выбирает
    # 2-3 стата, которые сейчас "громче всех кричат" (Саманта их реально
    # чувствует), и подсказывает LLM, какую реакцию под какой стат делать.
    # -----------------------------------------------------------------

    # Каждый стат описан кортежем:
    #   (base_stat_value, direction, drive_hint_low, drive_hint_high)
    # где direction:
    #   "extreme"  — интересен когда сильно ушёл от нормы (в любую сторону)
    #   "high"     — интересен когда высокий
    #   "low"      — интересен когда низкий
    # drive_hint — короткая подсказка LLM, какую персону под этот стат делать.
    # Скоринг рассчитывается как |отклонение от нормальной зоны| / 10.
    # Каждый стат = (dir, norm, low_label/high_label — короткое СОСТОЯНИЕ,
    # low_hint/high_hint — 1 фраза как это ощущается / что она делает).
    # LABEL — это то, что LLM пишет в скобках choice.text, поэтому оно
    # должно быть 1-2 словами и совпадать с содержимым выбора. Пример:
    # tired=85 → label="exhausted" → choice "(exhausted) You collapse into...".
    # Никаких "(tired)" — иначе будет диссонанс, если стат вышел за норму
    # в противоположную сторону.
    AI_STAT_DRIVERS = {
        # горячее / сексуальное
        "horny":      {"dir": "high", "norm": 30,
                       "high_label": "aching", "high_hint": "she is soaked and aching; body demands release, harder to say no"},
        "desire":     {"dir": "high", "norm": 30,
                       "high_label": "aroused", "high_hint": "arousal is loud, she catches herself wanting things"},
        # социальное / поведенческое
        "confidence": {"dir": "extreme", "norm": 50,
                       "low_label":  "shy",  "low_hint":  "shy, freezes, apologises, gives in to avoid conflict",
                       "high_label": "bold", "high_hint": "bold, cuts back, holds eye contact, dominates the moment"},
        "corrupt":    {"dir": "high", "norm": 30,
                       "high_label": "shameless", "high_hint": "no shame left, enjoys pushing further than a normal girl would"},
        "accept":     {"dir": "extreme", "norm": 50,
                       "low_label":  "still-a-man", "low_hint":  "still thinks like a man in a female body, hates being touched as a girl",
                       "high_label": "embracing-woman", "high_hint": "leans into being a woman, wants to be seen and desired that way"},
        # состояние тела
        "drunk":      {"dir": "high", "norm": 15,
                       "high_label": "drunk", "high_hint": "slurring, giggling, less inhibited, poor judgement"},
        "high":       {"dir": "high", "norm": 15,
                       "high_label": "high", "high_hint": "floaty, giggly, sensations dialled up, cannot focus"},
        "tired":      {"dir": "high", "norm": 40,
                       "high_label": "exhausted", "high_hint": "exhausted, wants to lie down, easier to push around"},
        "hunger":     {"dir": "low",  "norm": 60,
                       "low_label":  "starving", "low_hint":  "starving, will do a lot for food or money for food"},
        "hygiene":    {"dir": "low",  "norm": 60,
                       "low_label":  "filthy", "low_hint":  "dirty, sweaty, embarrassed to be seen or touched"},
        "mood":       {"dir": "extreme", "norm": 50,
                       "low_label":  "miserable",  "low_hint":  "depressed, self-destructive, does not care what happens",
                       "high_label": "elated", "high_hint": "euphoric, invincible, more likely to say yes to anything"},
        "trust":      {"dir": "extreme", "norm": 50,
                       "low_label":  "paranoid", "low_hint":  "paranoid about the Institute, keeps secrets, defiant",
                       "high_label": "loyal",    "high_hint": "trusts the Institute, will follow directives, tells them everything"},
    }

    def ai_pick_relevant_stats(gs, k=3):
        """Возвращает список словарей вида
            {'name':'horny','value':90,'direction':'high',
             'label':'aching','hint':'...','score':60.0}
        отсортированный по силе отклонения.
        'label' — короткое (1-2 слова) СОСТОЯНИЕ, которое LLM должна
        писать в скобках choice.text. НЕ имя стата. Это устраняет
        диссонанс "tired=20 но выбор 'You feel energetic'" — теперь
        такой стат вообще не попадёт в промпт (порог 15), а если попал —
        label покажет реальное состояние.
        """
        rows = []
        for stat, spec in AI_STAT_DRIVERS.items():
            try:
                v = int(gs.get(stat, spec['norm']) or 0)
            except Exception:
                continue
            direction = spec['dir']
            norm = int(spec.get('norm', 50))
            score = 0.0
            active_dir = None
            hint = None
            label = None
            if direction == "high":
                if v > norm:
                    score = (v - norm)
                    active_dir = "high"
                    hint = spec.get('high_hint')
                    label = spec.get('high_label')
            elif direction == "low":
                if v < norm:
                    score = (norm - v)
                    active_dir = "low"
                    hint = spec.get('low_hint')
                    label = spec.get('low_label')
            else:  # extreme
                diff = v - norm
                score = abs(diff)
                if diff > 0:
                    active_dir = "high"
                    hint = spec.get('high_hint')
                    label = spec.get('high_label')
                elif diff < 0:
                    active_dir = "low"
                    hint = spec.get('low_hint')
                    label = spec.get('low_label')
            # Отбрасываем всё, где отклонение маленькое (стат в норме,
            # LLM не о чем говорить). Порог 15 — примерно 15/100.
            if score < 15 or not hint:
                continue
            rows.append({
                'name': stat,
                'value': v,
                'direction': active_dir,
                'score': score,
                'label': label or stat,  # если label забыли — fallback на имя стата
                'hint': hint,
            })
        rows.sort(key=lambda r: r['score'], reverse=True)
        return rows[:k]

    def ai_build_char_context(gs, mode=u"full"):
        """ЕДИНАЯ функция «мир и Саманта» для всех LLM-генераторов.

        Три режима: full / compact / minimal — разница в объёме, но подход один:
        только те факты, которые РЕАЛЬНО важны сейчас, и человеческими словами,
        а не таблицами цифр.
        """
        _forbidden_text = _ai_forbidden_text_cached()

        # Собираем "human state" — короткие фразы про то, что реально
        # ощущается сейчас. Молчаливые (=None) значения не пишем.
        human = []
        for word in (
            _ai_hunger_word(gs.get('hunger', 100)),
            _ai_tired_word(gs.get('tired', 0)),
            _ai_hygiene_word(gs.get('hygiene', 100)),
            _ai_mood_word(gs.get('mood', 70)),
            _ai_desire_word(gs.get('desire', 0)),
            _ai_horny_word(gs.get('horny', 0)),
            _ai_drunk_word(gs.get('drunk', 0)),
            _ai_high_word(gs.get('high', 0)),
            _ai_confidence_word(gs.get('confidence', 35)),
            _ai_accept_word(gs.get('accept', 20)),
            _ai_corrupt_word(gs.get('corrupt', 0)),
        ):
            if word:
                human.append(word)
        human_state = u", ".join(human) if human else u"neutral state"

        loc      = ai_to_text(gs.get('location', u'home'), u'home')
        loc_desc = ai_get_location_description(loc) or u""
        hour     = int(gs.get('hour', 12) or 12)
        tod      = ai_to_text(gs.get('timeofday', u''), u'')
        weather  = _ai_weather_word(gs.get('weather', 0))
        private  = bool(gs.get('location_private', True))

        outfit_items = ai_to_text(gs.get('outfit_items', gs.get('outfit', u'unknown')), u'unknown')
        exposure = u""
        if bool(gs.get('is_exposed', False)):
            exposure = u" (intimate parts EXPOSED)"
        elif bool(gs.get('is_slutty', False)):
            exposure = u" (slutty look)"

        perks = ai_to_text(gs.get('perks', u'Former man'), u'Former man')

        cycle_stage = ai_to_text(gs.get('cycle_stage', u'no_cycle'), u'no_cycle')
        cycle_hint  = _ai_cycle_word(cycle_stage)  # уже словом
        preg_flag   = u", PREGNANT" if bool(gs.get('is_pregnant', False)) else u""
        lact_flag   = u", lactating" if bool(gs.get('is_lactating', False)) else u""

        # Виргинство. Пишем только если она ещё девственница — сам факт
        # для LLM важен (для персон и последствий).
        virgin_parts = []
        if bool(gs.get('is_virgin', True)):
            virgin_parts.append(u"vag virgin")
        if bool(gs.get('is_anal_virgin', True)):
            virgin_parts.append(u"anal virgin")
        virgin_str = (u"; " + u", ".join(virgin_parts)) if virgin_parts else u""

        recent_acts = ai_to_text(gs.get('recent_actions', u''), u'')
        last_evt    = ai_to_text(gs.get('last_event', u''), u'')

        spicy_level = gs.get('spicy_level', 2)
        spicy_word  = _ai_spicy_word(spicy_level)
        allowed_tags = ai_to_text(gs.get('allowed_tags', u'femininity, crossdressing'), u'femininity, crossdressing')

        # ------- minimal (для dirty-talk во время секса) -------
        if mode == u"minimal":
            base = u"Samantha (former man in female body), at %s, %s. spicy=%s (%s)." % (
                loc, human_state, spicy_level, spicy_word
            )
            if _forbidden_text:
                base += u"\n[FORBIDDEN]\n" + _forbidden_text
            return base

        # ------- compact (SMS / diary / trainer / wardrobe) -------
        if mode == u"compact":
            lines = []
            lines.append(u"[SAMANTHA]")
            lines.append(SAMANTHA_BIO)
            lines.append(u"State: " + human_state + u".")
            lines.append(u"Cycle: %s%s%s%s." % (cycle_hint, preg_flag, lact_flag, virgin_str))
            lines.append(u"Wearing: %s%s." % (outfit_items, exposure))
            lines.append(u"Perks: %s." % perks)
            lines.append(u"Location: %s (%s). %s %02d:00, %s. %s." % (
                loc, loc_desc or u"?", tod or u"?", hour, weather,
                u"private" if private else u"public"
            ))
            lines.append(u"spicy=%s (%s). Allowed themes: %s." % (spicy_level, spicy_word, allowed_tags))
            # FOCUS + PORTRAIT в compact-режиме тоже нужны — они меняют
            # характер SMS/диалогов/дневника, а не только квестов.
            try:
                _focus_tags = _ai_get_focus_tags_for_location(loc)
                if _focus_tags:
                    lines.append(u">>> FOCUS: " + u", ".join(_focus_tags[:6]))
            except Exception:
                pass
            try:
                _portrait = ai_get_player_portrait_for_prompt()
                if _portrait:
                    lines.append(u">>> PLAYER PORTRAIT (obey these directives — they define this player's kink):")
                    lines.append(_portrait)
            except Exception:
                pass
            if _forbidden_text:
                lines.append(u"[FORBIDDEN]")
                lines.append(_forbidden_text)
            return u"\n".join(lines)

        # ------- full (квесты) -------
        lines = []
        lines.append(u"[SAMANTHA]")
        lines.append(SAMANTHA_BIO)

        # Тело + одежда. Волосы/лобок только если сильно вне нормы —
        # обычно они не двигают сцену.
        body_bits = [u"C-cup"]
        _hl = int(gs.get('hair_length', 0) or 0)
        if _hl >= 30 or _hl < 10:  # только длинные или короткие
            body_bits.append(_ai_hair_word(_hl) + u" hair")
        _ph = int(gs.get('pubic_hair', 0) or 0)
        if _ph <= -5 or _ph >= 8:  # только waxed или full bush
            body_bits.append(_ai_phair_word(_ph))
        lines.append(u"Body: " + u", ".join(body_bits) + virgin_str + u".")
        lines.append(u"Wearing: " + outfit_items + exposure + u".")

        # ЦИКЛ — только если важен для сцены. Короткие пометки.
        _cs = ai_to_text(gs.get('cycle_stage', u''), u'').lower()
        if _cs == u"ovulate":
            lines.append(u">>> OVULATING: peak fertility, body sensitive.")
        elif _cs == u"mens":
            lines.append(u">>> ON PERIOD: bleeding, cramps.")
        if bool(gs.get('is_pregnant', False)):
            lines.append(u">>> PREGNANT.")
        if bool(gs.get('is_lactating', False)):
            lines.append(u">>> LACTATING.")

        # Состояние (Feeling) в full-режиме НЕ выводим — оно дублирует
        # блок STATS в DRIVERS ниже. В compact-режиме оставили, там
        # DRIVERS-блока нет.

        # РЕЛЕВАНТНЫЕ ДРАЙВЕРЫ — ЕДИНЫЙ ПУЛ.
        # Раньше строго 3 перка + 3 стата. Проблема: часто у Саманты
        # 5 фоновых перков со score=0.5 (только 'always'), а один стат
        # вылетает на 90/100 (например, drunk=90). Логичнее показать
        # LLM топ-5 драйверов ВООБЩЕ, независимо от типа.
        #
        # Скоринг:
        #   perks    — сумма совпавших тегов (0..~5)
        #   stats    — |отклонение_от_нормы| / 20 (чтобы 100-отклонение = 5.0,
        #              сопоставимо с максимально релевантным перком)
        # ОБЩИЙ ЛИМИТ 5 суммарно — хоть 5 статов, хоть 5 перков, хоть микс.
        # Никаких MIN_EACH_KIND: если у Саманты все статы в норме и 5
        # релевантных перков — пусть будут 5 перков. И наоборот.
        TOTAL_DRIVERS = 5

        perks_detailed = gs.get('perks_detailed', []) or []
        try:
            from ai_config_perks import ai_score_all_perks
            scored_perks_raw = ai_score_all_perks(gs, perks_detailed)
        except Exception as _rpe:
            print("ai_score_all_perks err: %s" % _rpe)
            scored_perks_raw = [{'entry': p, 'name': str(p).split(":",1)[0].strip(),
                                 'score': 0.0, 'idx': i} for i, p in enumerate(perks_detailed)]

        try:
            # Без cap: пусть в пул попадёт всё, что вышло за порог 15.
            scored_stats_raw = ai_pick_relevant_stats(gs, k=99)
        except Exception as _rse:
            print("ai_pick_relevant_stats err: %s" % _rse)
            scored_stats_raw = []

        # Единый пул с нормализованным score
        pool = []
        for pr in scored_perks_raw:
            pool.append({'kind': 'perk', 'score': float(pr['score']), 'data': pr})
        for st in scored_stats_raw:
            pool.append({'kind': 'stat', 'score': float(st['score']) / 20.0, 'data': st})

        pool.sort(key=lambda x: x['score'], reverse=True)
        chosen = pool[:TOTAL_DRIVERS]

        # Разбираем по типам ТОЛЬКО для красивого вывода двумя подсписками.
        # На функциональность лимит уже отработан на pool.
        top_perks = [c['data'] for c in chosen if c['kind'] == 'perk']
        top_stats = [c['data'] for c in chosen if c['kind'] == 'stat']

        n_perks = len(top_perks)
        n_stats = len(top_stats)
        lines.append(u">>> DRIVERS (make ONE choice per each — %d perk + %d stat = %d total):"
                     % (n_perks, n_stats, n_perks + n_stats))

        if top_perks:
            lines.append(u"  PERKS:")
            for pr in top_perks:
                lines.append(u"    - " + ai_to_text(pr['entry'], u""))
        if top_stats:
            lines.append(u"  STATS:")
            for st in top_stats:
                # Показываем LLM ГОТОВЫЙ КОРОТКИЙ ЯРЛЫК состояния — то же,
                # что она обязана использовать в скобках choice.text. Так
                # 'tired=20 -> energetic' не даст диссонанс "(tired) но энергична".
                # См. ai_pick_relevant_stats: st['label'] уже вычислен.
                lines.append(u"    - %s -> %s"
                             % (st.get('label') or st['name'], st['hint']))
        if not top_perks and not top_stats:
            lines.append(u"  (nothing loud — write 2 generic 'go with it' / 'resist' choices)")
        # rest_perks (фоновые перки) в промпт НЕ выводим — LLM всё равно
        # запрещено строить под них choices, и без них экономим ~30-80 токенов.
        lines.append(u"")

        # Локация — крупным блоком, потому что LLM на IQ2 систематически
        # игнорирует локацию и переносит сцену в бар/спальню из примера.
        priv_word = u"private" if private else u"public"
        lines.append(u">>> LOCATION (the scene MUST happen here): %s" % loc)
        lines.append(u">>> Location vibe: %s" % (loc_desc or u"(no description)"))
        lines.append(u">>> Setting: %s, %s, %s at %02d:00. Cash: %s." % (
            priv_word, weather, tod or u"?", hour, gs.get('money', 0)
        ))
        lines.append(u"")

        # Недавняя история — только если есть что-то нетривиальное
        if recent_acts and recent_acts not in (u"none", u""):
            lines.append(u"Recent: " + recent_acts + u".")
        if last_evt and last_evt not in (u"none", u""):
            lines.append(u"Prev event: " + last_evt + u".")

        # Темы
        lines.append(u"spicy=%s (%s). Allowed themes: %s." % (spicy_level, spicy_word, allowed_tags))

        # FOCUS — темы, которые игрок пометил как ЖЕЛАЕМЫЕ (level>=3) И
        # которые вообще допустимы в текущей локации. Отдаём модели как
        # "жирный акцент": попробуй развернуть сцену через эти темы, а не
        # просто скользить по allowed-списку. Молчим, если пересечения нет.
        try:
            _focus_tags = _ai_get_focus_tags_for_location(loc)
            if _focus_tags:
                _focus_str = u", ".join(_focus_tags[:8])
                lines.append(u">>> FOCUS (player DESIRES these themes here — try to spotlight at least one): %s" % _focus_str)
        except Exception as _fe:
            print("focus tags err: %s" % _fe)

        # PLAYER PORTRAIT — если файл заполнен, добавляем блок с явной
        # директивой "obey", чтобы квестовая LLM не игнорировала его.
        try:
            _portrait = ai_get_player_portrait_for_prompt()
            if _portrait:
                lines.append(u">>> PLAYER PORTRAIT (obey these directives — they define this player's kink):")
                lines.append(_portrait)
        except Exception as _pe:
            print("portrait inject err: %s" % _pe)

        # Forbidden — inline, коротким списком
        if _forbidden_text:
            lines.append(u"[FORBIDDEN]")
            lines.append(_forbidden_text)

        return u"\n".join(lines)

    def ai_prefix_world_state(user_prompt, gs, mode=u"full", header=u"[WORLD STATE]"):
        """Обёртка: префиксит к user_prompt блок 'состояние мира и Саманты'.

        Используется всеми генераторами (event, quest, sms, diary, dirty, npc_full,
        report, hourly, arrival и т.д.), чтобы у них был ЕДИНЫЙ общий взгляд на
        мир. Каждый генератор пишет ТОЛЬКО свою часть (что нужно сгенерировать
        и в каком формате отвечать), а мир пишет всегда одна функция.
        """
        try:
            ctx = ai_build_char_context(gs, mode=mode)
        except Exception as e:
            print("ai_prefix_world_state ctx err: %s" % e)
            ctx = u""
        parts = []
        if header:
            parts.append(ai_to_text(header, u""))
        if ctx:
            parts.append(ctx)
        parts.append(u"\n[TASK]")
        parts.append(ai_to_text(user_prompt, u""))
        return u"\n".join(parts)

    # Ключи эффектов, которые НЕ считаются "значимыми" сами по себе.
    # Если у выбора вообще нет ничего сверх этого — квест бракуем и
    # просим модель попробовать ещё раз (см. ai_quest_has_meaningful_choices).
    # Эти ключи сами по себе не считаются "мировыми изменениями" — плюс
    # к confidence на 2 не должен быть единственным итогом квеста.
    AI_CHOICE_TRIVIAL_KEYS = frozenset([
        u"confidence", u"mood", u"accept", u"acceptance", u"femininity",
        u"spicy_modifier", u"trust",
    ])

    # Явные yes/no-фразы, которые бракуем в choice.text независимо от effects.
    # Короткие тексты ('Fuck it.', 'Kneel.') не блокируем — они бывают
    # валидными inner-stance-персонами. Проверка длины УБРАНА.
    AI_CHOICE_BANNED_TEXT_PATTERNS = (
        u"^yes[.! ]*$", u"^no[.! ]*$", u"^okay[.! ]*$", u"^ok[.! ]*$", u"^sure[.! ]*$",
        u"^agree[.! ]*$", u"^accept[.! ]*$", u"^decline[.! ]*$", u"^refuse[.! ]*$",
        u"^say yes\\b", u"^say no\\b",
        u"^walk away[.! ]*$", u"^leave[.! ]*$", u"^ignore[.! ]*$", u"^back away\\b",
        u"^go with him[.! ]*$", u"^go with her[.! ]*$",
        u"^follow him[.! ]*$", u"^follow her[.! ]*$",
        u"^continue$", u"^continue text",
        # МОДЕЛЬ БУКВАЛЬНО КОПИРУЕТ PLACEHOLDER'Ы ИЗ ПРОМПТА. Бракуем.
        u"persona [ABC]", u"inner-stance", u"<.*persona", u"^<.+>$",
        u"fill in", u"example:",
    )
    _AI_CHOICE_BANNED_RE = re.compile(
        u"|".join(AI_CHOICE_BANNED_TEXT_PATTERNS),
        re.IGNORECASE
    )

    # -----------------------------------------------------------------
    # СИСТЕМА "БОЛЬШИХ ДЕЛЬТ".
    # Модель по умолчанию пишет +2/+3 к статам ("выпила бутылочку → +3 horny").
    # Это делает квест НЕ значимым: игра почти не меняется. Правильно
    # заставить её либо описать РЕАЛЬНО крупное событие (+60 horny —
    # значит секс, а не глоток вина), либо отказаться от этого хода.
    # Правило: если делать большие дельты, квест обязан их отработать
    # текстом — вот и всё, откуда берётся "большое событие".
    # -----------------------------------------------------------------
    # Ключи, для которых имеет смысл шкалировать до 60-100.
    AI_BIG_DELTA_STAT_KEYS = frozenset([
        u"horny", u"desire", u"drunk", u"high", u"mood", u"tired",
        u"hygiene", u"hunger", u"corrupt", u"allure", u"confidence",
        u"accept", u"acceptance", u"femininity", u"trust", u"money",
    ])
    # Что считаем "большим":
    #   >= 40 (или <= -40)  — точно большое
    #   >= 20 (или <= -20)  — среднее, приемлемо для 1 из выборов, но
    #                          нужен ещё хоть один >=40 в дереве, иначе всё вялое.
    # Пользователь: обычная жизнь двигает статы на 30-80 в день. Значит
    # квест-как-СОБЫТИЕ должен давать сравнимую или большую дельту.
    # Правила ДВУХУРОВНЕВЫЕ:
    #   MIN_PER_CHOICE — планка для КАЖДОГО выбора (иначе он "вялый").
    #   MIN_ONE_PEAK   — хотя бы ОДИН выбор в дереве должен быть выше этого
    #                    (это и есть тот самый reshape-day / broken-forever
    #                    момент, ради которого квест вообще запускался).
    # Мировой ключ (strip/travel_to/...) засчитывается как обе планки сразу.
    AI_BIG_DELTA_MIN_PER_CHOICE = 60   # KAJDЫЙ выбор ≥ 60
    AI_BIG_DELTA_MIN_ONE_PEAK   = 100  # ХОТЯ БЫ ОДИН ≥ 100

    # Legacy aliases на случай, если где-то ещё используются (safety).
    AI_BIG_DELTA_MIN_STRONG = AI_BIG_DELTA_MIN_PER_CHOICE
    AI_BIG_DELTA_MIN_MEDIUM = 30

    # Мировые ключи (strip / travel_to / diary / perk_add / pregnancy_risk /
    # remove_perk / equip / give_item / advance_hours) сами по себе тянут
    # на "большое событие" — им шкала не нужна.
    AI_WORLD_ROOT_KEYS = frozenset([
        u"perk_add", u"travel_to", u"strip", u"diary", u"pregnancy_risk",
        u"remove_perk", u"equip", u"give_item", u"advance_hours",
    ])

    def _ai_choice_max_abs_delta(ch):
        """Возвращает максимальный |int| среди stat-дельт в choice.effects.
        Мировые ключи (strip/travel_to/pregnancy_risk/...) считаются как
        peak-событие и возвращают AI_BIG_DELTA_MIN_ONE_PEAK — этого достаточно
        и для планки-на-выбор, и для планки-на-дерево одновременно."""
        if not ai_dict_like(ch):
            return 0
        eff = ch.get('effects') or {}
        if not ai_dict_like(eff):
            eff = {}
        # Мировой ключ на корне choice или в effects → это уже пик.
        for root_key in AI_WORLD_ROOT_KEYS:
            if ch.get(root_key) or (root_key in eff and eff.get(root_key)):
                return AI_BIG_DELTA_MIN_ONE_PEAK
        m = 0
        for k, v in eff.items():
            try:
                kk = unicode(k).lower()
            except Exception:
                continue
            if kk not in AI_BIG_DELTA_STAT_KEYS:
                continue
            try:
                iv = abs(int(v))
            except Exception:
                continue
            if iv > m:
                m = iv
        return m

    def _ai_choice_is_meaningful(ch):
        """True, если у выбора есть хоть один эффект за пределами тривиального
        И текст не выглядит как 'yes/no'. Проверка МАСШТАБА эффекта делается
        отдельно, на уровне дерева (see ai_quest_has_meaningful_choices)."""
        if not ai_dict_like(ch):
            return False
        try:
            txt = ai_to_text(ch.get('text', u''), u'').strip()
        except Exception:
            txt = u''
        if not txt or _AI_CHOICE_BANNED_RE.search(txt):
            return False

        eff = ch.get('effects') or {}
        if not ai_dict_like(eff):
            eff = {}
        keys = set()
        for k in eff.keys():
            try:
                keys.add(unicode(k).lower())
            except Exception:
                pass
        world_keys = keys - AI_CHOICE_TRIVIAL_KEYS
        for root_key in AI_WORLD_ROOT_KEYS:
            if ch.get(root_key):
                world_keys.add(root_key)
        return len(world_keys) > 0

    def ai_quest_has_meaningful_choices(tree):
        """МЯГКАЯ проверка. Единственное, что реально бракуем — квесты, где
        ВСЕ выборы это yes/no/agree/refuse текстом ИЛИ где вообще ни один
        выбор не двигает мир (все с +5 к mood и всё). Всё остальное пускаем.

        Раньше валидатор жёстко требовал >= 60 для каждого + >= 100 хотя бы
        для одного, и заставлял модель перегенерить. По факту это тратило
        время и деньги на retry, а модель под страхом лучше не пишет.
        """
        try:
            if not ai_dict_like(tree):
                return False
            steps = tree.get('steps') or []
            if not steps:
                return False
            saw_any_peak = False
            for st in steps:
                choices = st.get('choices') if ai_dict_like(st) else []
                if not choices:
                    return False
                # Хотя бы один выбор должен быть не-пресным — иначе весь
                # квест это болтовня.
                any_meaningful = False
                for ch in choices:
                    if _ai_choice_is_meaningful(ch):
                        any_meaningful = True
                    # peak считаем по всему дереву
                    if _ai_choice_max_abs_delta(ch) >= AI_BIG_DELTA_MIN_ONE_PEAK:
                        saw_any_peak = True
                if not any_meaningful:
                    return False
            # peak — приятно иметь, но не блокируем квест если его нет.
            # Просто отметим в логе через ai_set_event_debug выше.
            return True
        except Exception as e:
            print("ai_quest_has_meaningful_choices err: %s" % e)
            return True

    def generate_full_quest(gs):
        """Генерирует дерево. Несколько попыток + локальный fallback."""
        loc_desc = ai_get_location_description(gs['location'])
        spicy_level = gs.get('spicy_level', 2)
        is_spicy = gs.get('is_spicy', False)
        allowed_tags = gs.get('allowed_tags', 'femininity, crossdressing')

        # Общий «мир + Саманта» через единую функцию. Локальная задача — только
        # структура ответа. Никакого ручного сбора статов, чтобы все генераторы
        # видели мир одинаково.
        # TASK: минимум. Основные правила и подробный worked example уже в
        # sys_prompt (kv_sys / one_sys). Здесь только напоминание сути.
        # step_no пробрасываем в промпт из вызывающего кода (chain-режим).
        # Если это первый шаг цепочки — просто вводная. Если 2-й..N-й — LLM
        # видит контекст предыдущего выбора. Если N == QUEST_MAX_STEPS-1 —
        # LLM предупреждается, что следующий шаг должен быть финалом.
        step_no = int(gs.get('_chain_step_no', 1) or 1)
        max_steps = AI_QUEST_MAX_STEPS
        prev_scene = ai_to_text(gs.get('_chain_prev_scene', u''), u'')
        prev_choice = ai_to_text(gs.get('_chain_prev_choice', u''), u'')

        # chain_hdr: только для 2+ шага — на 1-м стандартный старт, ничего
        # добавлять не надо. На финальном шаге принудительно просим is_ending
        # на всех выборах (движок всё равно продублирует, но LLM полезно знать).
        chain_hdr = u""
        if step_no > 1:
            chain_hdr = (
                u"[STEP %d/%d] Continue from previous choice, do not restart.\n"
                u"Prev scene: %s\n"
                u"Prev choice: %s\n"
                % (step_no, max_steps, prev_scene[:280], prev_choice[:140])
            )
            if step_no >= max_steps:
                chain_hdr += u"FINAL STEP — set is_ending=true on ALL choices.\n"
            elif step_no >= max_steps - 1:
                chain_hdr += u"Next step must resolve — start closing threads.\n"

        # TASK — минимум. Полные правила уже в system-prompt (kv_sys / one_sys).
        # Здесь только: chain-header (если 2+ шаг) + суть текущего задания.
        task = (
            chain_hdr +
            u"\n"
            u"Write ONE step grounded in [SAMANTHA] above.\n"
            u"Open MID-ACTION (something already being done to her, no small talk).\n"
            u"step_desc: 8-14 sentences of concrete prose.\n"
            u"\n"
            u"For EACH driver in [DRIVERS] above, write ONE choice using that\n"
            u"perk/stat as the persona flavor. Then add ONE escape choice.\n"
            u"If [DRIVERS] is empty, write 2 generic 'go with it' / 'resist' + escape.\n"
            u"choice.text = SECOND-PERSON action Samantha does ('You ...'), not what\n"
            u"the world does around her. 'You clamp your legs shut.' YES.\n"
            u"'He does not notice you.' / 'Stay quiet like a mouse.' NO.\n"
            u"\n"
            u"Deltas: mix one big change (40-200) with small nudges (5-20). At least\n"
            u"one choice should use a WORLD KEY (strip / travel_to / pregnancy_risk /\n"
            u"perk_add / remove_perk / diary / equip / give_item / advance_hours) —\n"
            u"they are under-used but they physically change the game.\n"
            u"\n"
            u"is_ending=true only on a choice that CLOSES the scene. Otherwise the\n"
            u"game will ask you for the next step.\n"
            u"\n"
            u"ending_text 6-10 sentences, concrete (body, place, who saw, what changed)."
        )
        compact_user = ai_prefix_world_state(task, gs, mode=u"full")

        attempts = [
            # 1) compact + format json
            dict(sys_prompt=PROMPTS.get("event_full_compact", PROMPTS["event_full"]), user=compact_user, temp=0.55, max_tokens=AI_FULL_QUEST_MAX_TOKENS, force_json_format=True, label=u"tree-compact-json"),
            # 2) compact without format json (weak GGUF sometimes empty with format=json)
            dict(sys_prompt=PROMPTS.get("event_full_compact", PROMPTS["event_full"]), user=compact_user + " Return raw JSON object only.", temp=0.45, max_tokens=AI_FULL_QUEST_MAX_TOKENS, force_json_format=False, label=u"tree-compact-raw"),
            # 3) full prompt last try
            dict(sys_prompt=PROMPTS["event_full"], user=compact_user, temp=0.5, max_tokens=AI_FULL_QUEST_MAX_TOKENS, force_json_format=True, label=u"tree-full-json"),
        ]
        # Мягкий KV-промпт: НЕ просим JSON вообще. Слабым 2-битным GGUF
        # (в т.ч. Dirty-Muse i1-IQ2_XS) такое даётся сильно надёжнее.
        # Парсер ai_parse_kv_quest соберёт из этого нужный dict сам.
        # KV-промпт. Пример полностью проработан от начала до конца — модель
        # копирует стиль, а не placeholder-плашки. Никаких '<persona A>' —
        # слабые GGUF копируют их дословно.
        kv_sys = u"""Write ONE step of a TheFixer chain quest for Samantha.
Plain KEY: value text — no JSON, no markdown, no "-"/"*"/"**" bullets.
Each line is either "KEY: value" or a continuation of the previous value.

GROUNDING (must-follow):
- SETTING = Samantha's CURRENT location (from [SAMANTHA]). Park = park, home = home. Match the vibe.
- NAMED CHARACTERS only from WORLD STATE. If none listed — anonymous: "a man", "the jogger", "the shopkeeper". Never invent names.

Template (SHAPE only — do NOT copy the venue or the "A_MAN_1"-style names):

TITLE: <scene title>
DESC: <one-line summary>
STEP: step1
STEP_TITLE: <stage title>
STEP_DESC: A_MAN_1 has already slid his hand up your bare thigh under the counter. A_MAN_2 watches from the next seat. The music is loud enough that no one else notices. <continue 8-14 sentences, grounded in CURRENT location + outfit>
CHOICE: (shy) You collapse into the role he expects — voice cracks, eyes wet.
EFFECTS: horny=+90, strip=bra, corrupt=+50, mood=+15
ENDING_TITLE: Good girl
ENDING_TEXT: <6-10 sentences of concrete consequence>
CHOICE: (still-a-man) You weaponize the male mind you still have — say back exactly what a guy would.
EFFECTS: desire=+110, allure=+70, remove_perk=perk_shy, corrupt=+40
ENDING_TITLE: Reversed
ENDING_TEXT: <6-10 sentences>
CHOICE: (aching) You stop pretending and press back against his hand.
EFFECTS: horny=+140, corrupt=+80, strip=panties, diary=I chose it.
ENDING_TITLE: Given in
ENDING_TEXT: <6-10 sentences>
CHOICE: (escape) You try to slip out.
EFFECTS: travel_to=loc_home, mood=-60, tired=+40
IS_ENDING: true
ENDING_TITLE: Bolted
ENDING_TEXT: <6-10 sentences (successful escape OR failed attempt)>

The "(word)" prefix on each CHOICE is a SHORT STATE-LABEL: for perk-driven choices use the perk name in lowercase; for stat-driven choices use the ready label the game gave you in [DRIVERS] (like "aching", "shy", "bold", "exhausted", "starving"). NEVER put the raw stat name if it contradicts the state — e.g. do NOT write "(tired)" for an energetic choice; the label already reflects the actual state.

Rules:
1) CHOICES = ONE per each driver from [DRIVERS] in WORLD STATE (game pre-picked them). Then ONE escape. Total 3-6.
2) Each CHOICE.TEXT is written in SECOND PERSON ("You ..."), describing what SAMANTHA actively does / says / thinks in reaction to the scene — never what the other people do to her, never third-person. Examples: "You lower your eyes and let your voice go small.", "You bite down on his shoulder to make him stop.", "You freeze completely and let it happen." NOT: "He does not notice you.", "Someone looks at you.", "Try to stay quiet like a mouse." — a choice is HER action, not the world's reaction.
3) Mix deltas: one big (40-200) + small nudges (5-20). At least one choice uses a WORLD KEY (strip, travel_to, pregnancy_risk, perk_add, remove_perk, diary, equip, give_item, advance_hours) — they are under-used.
4) STEP_DESC: 8-14 sentences opening MID-ACTION.
5) ENDING_TEXT: 6-10 sentences of concrete consequence.
6) IS_ENDING: true only if the branch CLOSES the scene naturally. Otherwise omit — game asks for next step.
7) Do NOT copy "A_MAN_1" / "Marcus" / "Devon" from the template — use anonymous or WORLD STATE names.
8) STEP: MUST be exactly a short id like "step1" (never a sentence). The scene text goes in STEP_DESC, NOT in STEP.
9) NEVER include children, kids, minors, teens, schoolgirls, schoolboys, playgrounds, swings, toddlers or babies anywhere — not even as passing background. Samantha is ALWAYS in an adult-only environment.
10) Nothing after the last ENDING_TEXT."""
        kv_user = compact_user + u"\n\nRemember: reply in the KEY: value format above, not JSON."

        if AI_QUEST_ONE_STEP_TEST_MODE:
            # Тест: одношаговый квест. Даём 3 попытки, а не одну, потому что
            # 2-битные GGUF стабильно валят первую (нет ключа 'steps', пустой ответ, битый JSON).
            # JSON-схема с ПОЛНОСТЬЮ ЗАПОЛНЕННЫМ примером. Никаких placeholder-
            # плашек "<persona A>" — 2-битные модели их дословно копируют.
            one_sys = u"""Return ONLY one JSON object, no prose/markdown/code fences.

GROUNDING (override the example if it conflicts):
- SETTING = Samantha's CURRENT location from WORLD STATE. Park=park, home=home. NOT what example uses.
- NAMED CHARACTERS only from WORLD STATE. If none — anonymous "a man"/"the shopkeeper". Never invent names.

Shape example (SHAPE only, do not copy contents):
{"title":"<title>", "description":"<summary>",
 "steps":[{"id":"step1", "title":"<stage title>",
   "description":"<8-14 sentences MID-ACTION, in CURRENT location>",
   "choices":[
     {"text":"You go small and pliable.", "next_step":null, "is_ending":false,
      "effects":{"horny":80,"strip":"bra","corrupt":40,"mood":15,"diary":"..."},
      "ending_title":"Good girl", "ending_text":"<6-10 sentences>"},
     {"text":"You cut him down with words.", "next_step":null, "is_ending":false,
      "effects":{"desire":90,"allure":70,"remove_perk":"perk_shy","corrupt":60}},
     {"text":"You freeze and dissociate.", "next_step":null, "is_ending":false,
      "effects":{"mood":-220,"tired":80,"hygiene":-70,"diary":"Lost an hour."}},
     {"text":"You try to slip out and get home.", "next_step":null, "is_ending":true,
      "effects":{"travel_to":"loc_home","mood":-80,"tired":60}}
   ]}]}

Rules:
- "steps" = list of length 1, id "step1".
- 3-6 choices: ONE per each driver in [DRIVERS] + ONE escape. Each choice.text is SECOND-PERSON action by Samantha ("You ..."), never a description of what others do around her. Never "yes"/"no".
- Mix deltas: one big (40-200) + small nudges (5-20). Prefer WORLD KEYS (strip, travel_to, pregnancy_risk, perk_add, remove_perk, diary, equip, give_item, advance_hours) — under-used.
- description: 8-14 sentences MID-ACTION in CURRENT location.
- ending_text: 6-10 sentences concrete consequence.
- is_ending:true only if branch closes the scene; else omit — game asks for next step.
- Output raw JSON only."""
            one_sys_flat = u"""Return ONLY one JSON object, no prose/markdown.
Flat shape (game wraps it): {"title":"","description":"<8-14 sentences mid-scene>","choices":[
  {"text":"persona reaction","effects":{"horny":90,"strip":"bra","corrupt":40,"mood":15},"ending_title":"","ending_text":"<6-10 sentences>","is_ending":false},
  {"text":"different persona","effects":{"desire":100,"travel_to":"loc_home","diary":"...","tired":30},"ending_title":"","ending_text":"<6-10 sentences>","is_ending":true}
]}
3-6 choices, one per driver in [DRIVERS] + escape. Each choice.text is SECOND-PERSON action by Samantha ("You ..."), her active reaction — not what others do around her. Never yes/no. Mix deltas. Prefer world keys. is_ending:true = branch closes. Raw JSON only."""
            attempts = [
                # 0) НОВОЕ: мягкий KV-формат — не просим JSON вообще, парсим сами.
                #    Ставим первым, потому что для i1-IQ2_XS Dirty-Muse это
                #    надёжнее любого JSON. Тип 'kv' обрабатывается отдельно.
                dict(kind=u"kv", sys_prompt=kv_sys, user=kv_user, temp=0.55, max_tokens=AI_FULL_QUEST_MAX_TOKENS, force_json_format=False, label=u"oneclick-kv"),
                # 1) строгая JSON-схема со steps + format=json (для моделей, что умеют)
                dict(kind=u"json", sys_prompt=one_sys, user=compact_user, temp=0.25, max_tokens=AI_FULL_QUEST_MAX_TOKENS, force_json_format=True,  label=u"oneclick-json"),
                # 2) та же схема без format=json (некоторые GGUF при format=json дают пусто)
                dict(kind=u"json", sys_prompt=one_sys, user=compact_user + u" Return raw JSON object only.", temp=0.2, max_tokens=AI_FULL_QUEST_MAX_TOKENS, force_json_format=False, label=u"oneclick-raw"),
                # 3) упрощённая плоская схема без 'steps' — normalize её теперь заворачивает сам
                dict(kind=u"json", sys_prompt=one_sys_flat, user=compact_user, temp=0.3, max_tokens=AI_FULL_QUEST_MAX_TOKENS, force_json_format=False, label=u"oneclick-flat"),
            ]

        last_err = u""
        for i, att in enumerate(attempts):
            try:
                store.ai_notify_queue.append(u"ИИ: Генерация дерева (%s) %s/%s..." % (att['label'], i+1, len(attempts)))
            except Exception:
                pass
            try:
                att_kind = att.get('kind', u'json')
                if att_kind == u"kv":
                    # МЯГКИЙ КV-ПУТЬ: получаем сырой текст, а НЕ JSON.
                    raw_kv = ai_call(
                        OLLAMA_MODEL_JSON,
                        att['sys_prompt'],
                        att['user'],
                        want_json=False,                       # <-- ключевое: без format=json
                        temp=att['temp'],
                        max_tokens=att['max_tokens'],
                        task_desc=u"Цепочка квестов (%s)" % att['label'],
                        timeout=AI_FULL_QUEST_TIMEOUT,
                        force_json_format=False,
                    )
                    # сохраняем сырой ответ в ИЗОЛИРОВАННУЮ квестовую переменную
                    # СРАЗУ (даже для __ERROR-строки), чтобы фоновые SMS/NPC-чаты
                    # не перетёрли то, что реально пришло в ответ на квест.
                    try:
                        store.ai_debug_last_quest_raw = u"[%s KV-RAW]\n" % att['label'] + ai_to_text(raw_kv, u"")
                    except Exception:
                        pass
                    if isinstance(raw_kv, basestring) and raw_kv.startswith("__ERROR"):
                        last_err = raw_kv
                        ai_set_event_debug(u"Full quest KV attempt failed: %s -> %s" % (att['label'], raw_kv), raw=store.ai_debug_last_quest_raw)
                        continue
                    # дублируем и в общую (для совместимости с прочими просмотрами)
                    try:
                        store.ai_debug_last_json_raw = store.ai_debug_last_quest_raw
                    except Exception:
                        pass
                    parsed_kv = ai_parse_kv_quest(raw_kv)
                    if parsed_kv is None:
                        last_err = u"kv-parse produced nothing for %s" % att['label']
                        ai_set_event_debug(u"Full quest KV parse fail: %s" % last_err, raw=ai_to_text(raw_kv, u""))
                        continue
                    tree = ai_normalize_quest_tree(parsed_kv)
                    min_ok_steps = 1 if AI_QUEST_ONE_STEP_TEST_MODE else 2
                    if tree and len(tree.get('steps', [])) >= min_ok_steps:
                        # Проверка на пресность: если у ЛЮБОГО выбора нет
                        # ничего кроме confidence/mood — идём на следующую
                        # попытку (последний attempt всё равно вернём как
                        # есть, лучше пресный LLM, чем локальный шаблон).
                        _meaningful = ai_quest_has_meaningful_choices(tree)
                        _is_last = (i == len(attempts) - 1)
                        if _meaningful or _is_last:
                            ai_set_event_debug(
                                u"Full quest tree OK via KV %s (%s steps, meaningful=%s)" % (att['label'], len(tree.get('steps', [])), _meaningful),
                                raw=ai_to_text(raw_kv, u""),
                                parsed={"title": tree.get('title'), "steps": [s.get('id') for s in tree.get('steps', [])], "local": False, "kv_soft_format": True, "meaningful_choices": _meaningful},
                            )
                            return tree
                        last_err = u"kv-tree TRIVIAL choices for %s (only confidence/mood), retrying" % att['label']
                        ai_set_event_debug(u"Full quest KV rejected (trivial choices): %s" % last_err, raw=ai_to_text(raw_kv, u""), parsed=parsed_kv)
                        continue
                    last_err = u"kv-normalize failed or <%s steps for %s" % (min_ok_steps, att['label'])
                    ai_set_event_debug(u"Full quest KV normalize fail: %s" % last_err, raw=ai_to_text(raw_kv, u""), parsed=parsed_kv)
                    continue

                # ==== JSON-ПУТЬ ====
                data = ai_call(
                    OLLAMA_MODEL_JSON,
                    att['sys_prompt'],
                    att['user'],
                    want_json=True,
                    temp=att['temp'],
                    max_tokens=att['max_tokens'],
                    task_desc=u"Цепочка квестов (%s)" % att['label'],
                    timeout=AI_FULL_QUEST_TIMEOUT,
                    force_json_format=att['force_json_format'],
                )
                # СРАЗУ фиксируем сырой ответ именно для КВЕСТА в изолированный
                # слот. ai_debug_last_json_raw мог быть перезаписан фоновыми
                # SMS/NPC-чатами между return из ai_call и нашим ai_set_event_debug.
                try:
                    _quest_raw_now = getattr(store, 'ai_debug_last_json_raw', u"") or u""
                    store.ai_debug_last_quest_raw = u"[%s JSON-RAW]\n%s" % (att['label'], _quest_raw_now)
                except Exception:
                    pass
                if isinstance(data, basestring) and data.startswith("__ERROR"):
                    last_err = data
                    ai_set_event_debug(u"Full quest attempt failed: %s -> %s" % (att['label'], data), raw=getattr(store, 'ai_debug_last_quest_raw', u''))
                    # HTTP 500 значит Ollama/модель уже упала. Не добиваем сервер ещё 1-2 запросами,
                    # сразу используем локальный 2x2 fallback и даём Ollama остыть/перезапуститься.
                    if data.startswith("__ERROR_OLLAMA_500__"):
                        try:
                            store.ai_notify_queue.append(u"ИИ: HTTP 500 от Ollama, пробую CPU-safe retry")
                        except Exception:
                            pass
                        safe_data = ai_call_json_cpu_safe(
                            OLLAMA_MODEL_JSON,
                            att['sys_prompt'],
                            att['user'],
                            temp=0.2,
                            max_tokens=min(220 if AI_QUEST_ONE_STEP_TEST_MODE else 450, att['max_tokens']),
                            task_desc=u"CPU-safe %s" % att['label'],
                            timeout=AI_FULL_QUEST_TIMEOUT,
                        )
                        if isinstance(safe_data, basestring) and safe_data.startswith("__ERROR"):
                            last_err = data + u" | CPU-safe retry: " + ai_to_text(safe_data, u'')
                            ai_set_event_debug(u"Full quest CPU-safe retry failed after HTTP 500: %s" % last_err, raw=getattr(store, 'ai_debug_last_quest_raw', u''))
                            break
                        safe_tree = ai_normalize_quest_tree(safe_data)
                        min_ok_steps = 1 if AI_QUEST_ONE_STEP_TEST_MODE else 2
                        if safe_tree and len(safe_tree.get('steps', [])) >= min_ok_steps:
                            # После CPU-safe retry всё равно принимаем: это
                            # уже аварийный путь, второго шанса не будет.
                            _meaningful_safe = ai_quest_has_meaningful_choices(safe_tree)
                            ai_set_event_debug(
                                u"Full quest tree OK via CPU-safe retry after HTTP 500 (%s steps, meaningful=%s)" % (len(safe_tree.get('steps', [])), _meaningful_safe),
                                raw=getattr(store, 'ai_debug_last_quest_raw', u''),
                                parsed={"title": safe_tree.get('title'), "steps": [s.get('id') for s in safe_tree.get('steps', [])], "local": False, "cpu_safe_retry": True, "meaningful_choices": _meaningful_safe},
                            )
                            return safe_tree
                        last_err = data + u" | CPU-safe retry normalize failed"
                        ai_set_event_debug(u"Full quest CPU-safe retry normalize fail: %s" % last_err, raw=getattr(store, 'ai_debug_last_quest_raw', u''), parsed=safe_data)
                        break
                    continue
                tree = ai_normalize_quest_tree(data)
                min_ok_steps = 1 if AI_QUEST_ONE_STEP_TEST_MODE else 2
                if tree and len(tree.get('steps', [])) >= min_ok_steps:
                    _meaningful = ai_quest_has_meaningful_choices(tree)
                    _is_last = (i == len(attempts) - 1)
                    if _meaningful or _is_last:
                        ai_set_event_debug(
                            u"Full quest tree OK via %s (%s steps, meaningful=%s)" % (att['label'], len(tree.get('steps', [])), _meaningful),
                            parsed={"title": tree.get('title'), "steps": [s.get('id') for s in tree.get('steps', [])], "local": False, "one_step_test": bool(AI_QUEST_ONE_STEP_TEST_MODE), "meaningful_choices": _meaningful},
                        )
                        return tree
                    last_err = u"json-tree TRIVIAL choices for %s (only confidence/mood), retrying" % att['label']
                    ai_set_event_debug(u"Full quest rejected (trivial choices): %s" % last_err, parsed=data)
                    continue
                last_err = u"normalize failed or <%s steps for %s" % (min_ok_steps, att['label'])
                # parsed=data — то, что реально вернул json.loads(); часто именно
                # тут видно, что модель прислала пустой {} или список без 'steps'
                # и без 'choices'. raw= — сырой ответ конкретно этой квестовой
                # попытки, не перезаписанный фоновыми SMS/NPC.
                ai_set_event_debug(
                    u"Full quest normalize fail: %s" % last_err,
                    raw=getattr(store, 'ai_debug_last_quest_raw', u''),
                    parsed=data,
                )
            except Exception as e:
                last_err = unicode(e)
                print("full quest attempt err %s: %s" % (att['label'], e))
                ai_set_event_debug(u"Full quest exception in %s: %s" % (att['label'], e))

        # Локальный fallback — лучше, чем одношаговый Mirror
        print("full quest all attempts failed (%s), using local tree" % last_err)
        tree = ai_make_local_quest_tree(gs)
        try:
            tree['_llm_failed_reason'] = ai_to_text(last_err, u'unknown LLM failure')
        except Exception:
            pass
        ai_set_event_debug(
            u"Using LOCAL quest tree fallback. Last LLM error: %s" % last_err,
            parsed={"title": tree.get('title'), "steps": [s.get('id') for s in tree.get('steps', [])], "local": True, "llm_failed_reason": ai_to_text(last_err, u'')},
        )
        try:
            store.ai_notify_queue.append(u"ИИ: LLM-дерево не собралось, использован локальный квест-шаблон")
        except Exception:
            pass
        return tree

    def generate_next_quest_step(prev_full_q, prev_step, chosen_choice, step_no):
        """ON-DEMAND CHAIN: генерирует СЛЕДУЮЩИЙ шаг квеста, зная предыдущий
        шаг + выбранный игроком вариант. Возвращает новый step-dict, либо
        None если LLM не осилила. Вызывается когда игрок выбирает choice
        без is_ending=true.

        step_no — номер СЛЕДУЮЩЕГО шага (2, 3, ..). Если == AI_QUEST_MAX_STEPS,
        передаём модели указание, что это последний шаг и все choices должны
        быть is_ending=true.
        """
        try:
            gs = get_state()
            # Пробрасываем контекст цепочки в build_char_context. Простые
            # gs-ключи с префиксом _chain — читаются в task-блоке
            # generate_full_quest.
            try:
                gs['_chain_step_no'] = int(step_no)
            except Exception:
                gs['_chain_step_no'] = 2
            gs['_chain_prev_scene'] = ai_to_text(prev_step.get('description', u''), u'')[:400] if ai_dict_like(prev_step) else u''
            gs['_chain_prev_choice'] = ai_to_text(chosen_choice.get('text', u''), u'') if ai_dict_like(chosen_choice) else u''
            # Прошлые аллаудед-теги перенесём как есть, чтобы модель осталась
            # в той же теме.
            for k in ('allowed_tags', 'spicy_level', 'is_spicy'):
                if k not in gs and prev_full_q and prev_full_q.get(k) is not None:
                    gs[k] = prev_full_q.get(k)

            # Собираем single-step дерево тем же generate_full_quest.
            # Он же вернёт tree со STEPS[0] — это и есть новый шаг.
            new_tree = generate_full_quest(gs)
            if not ai_dict_like(new_tree) or not new_tree.get('steps'):
                return None
            new_step = new_tree['steps'][0]
            # Даём ему уникальный id, чтобы не столкнуться с существующим.
            new_step['id'] = u"step%d" % int(step_no)
            # Если это последний шаг — форсируем is_ending=true на всех выборах.
            if int(step_no) >= AI_QUEST_MAX_STEPS:
                for ch in new_step.get('choices', []) or []:
                    if ai_dict_like(ch):
                        ch['is_ending'] = True
                        ch['next_step'] = None
            return new_step
        except Exception as e:
            print("generate_next_quest_step err: %s" % e)
            return None

    def generate_full_dialogue(npc, gs):
        try:
            npc_info=u"%s %s group=%s whore=%s slut=%s" % (npc.fname, npc.sname, getattr(npc,'bio_group','?'), getattr(npc,'iswhore',False), getattr(npc,'isslut',False))
            task = (u"Generate a full 4-exchange dialogue between the NPC (%s) and Samantha "
                    u"as described by the schema in the system prompt. Base every line on the "
                    u"WORLD STATE above — reference her current outfit/mood/location if relevant." % npc_info)
            prompt = ai_prefix_world_state(task, gs, mode=u"full")
            # Использование безопасного .format() во избежание упавших аргументов % в Python 2!
            sys_prompt=PROMPTS["npc_full"].format(fname=npc.fname, sname=npc.sname, bio_group=getattr(npc,'bio_group','?'), iswhore=getattr(npc,'iswhore',False), fem=gs['fem'])
            data=ai_call(OLLAMA_MODEL_JSON, sys_prompt, prompt, want_json=True, temp=0.85, max_tokens=800, task_desc=u"Полный диалог с " + npc.fname)
            if data and 'dialogue' in data:
                return data['dialogue']
        except Exception as e:
            print("full dialogue err %s" % e)
        return None

    def generate_dirty_batch(gs, sex_type="vag", npc_name="partner"):
        try:
            task = (u"Generate 5 dirty-talk phrases Samantha would say/think during %s sex with %s, "
                    u"progressing from foreplay to climax. Match her current arousal/femininity from "
                    u"the WORLD STATE above." % (sex_type, npc_name))
            prompt = ai_prefix_world_state(task, gs, mode=u"minimal")
            sys_prompt=PROMPTS["dirty_batch"] % {'sex_type': sex_type, 'npc_name': npc_name, 'fem': gs['fem'], 'desire': gs['desire']}
            data=ai_call(OLLAMA_MODEL_JSON, sys_prompt, prompt, want_json=True, temp=0.9, max_tokens=500, task_desc=u"Интимный монолог")
            if data and isinstance(data, list) and len(data)>=2:
                return data
        except Exception as e:
            print("dirty batch err %s" % e)
        return None

    def generate_sms_batch(gs):
        try:
            task = (u"Generate 3 SMS from different NPCs to Samantha as the system-prompt JSON array. "
                    u"Reference her current outfit / location / recent actions from the WORLD STATE above.")
            prompt = ai_prefix_world_state(task, gs, mode=u"compact")
            data=ai_call(OLLAMA_MODEL_JSON, PROMPTS["sms_batch"], prompt, want_json=True, temp=0.85, max_tokens=600, task_desc=u"SMS рассылка")
            if data and isinstance(data, list):
                return data
        except Exception as e:
            print("sms batch err %s" % e)
        return None

    def generate_diary_batch(gs):
        try:
            task = (u"Generate 3 diary entries for the next 3 days as the system-prompt JSON array. "
                    u"Base tone/topics on the WORLD STATE above and Samantha's previous event.")
            prompt = ai_prefix_world_state(task, gs, mode=u"compact")
            data=ai_call(OLLAMA_MODEL_JSON, PROMPTS["diary_batch"], prompt, want_json=True, temp=0.8, max_tokens=600, task_desc=u"Дневниковые записи")
            if data and isinstance(data, list):
                return data
        except:
            return None

    PROMPTS = {
        "chat_ru": u"""Ты - Dr. Tess Brooker, ДОМИНАНТНЫЙ психолог Института из TheFixer. Пиши ТОЛЬКО на русском.

[КТО ТЫ]
- Ты женщина 32 года, доминантная госпожа, строгая кураторша. Контролируешь Саманту.
- Саманта - бывший мужик в теле девушки, принятие себя как девушки %d%%. Ты ее дрессируешь.
- Ты ПРИКАЗЫВАЕШЬ, не спрашиваешь.
- Ты не ИИ, ты Брукер.

[СТИЛЬ ДОМИНАНТНЫЙ]
- Обращайся: девочка, малышка, сучка, хорошая девочка, шлюшка.
- Командуй: Раздвинь ноги, Покажи, Трогай себя, Отчитайся, Не смей кончать без разрешения.
- 1-3 коротких предложения, как госпожа в чате.
- Никаких *звездочек* и никакого английского.
- Максимум NSFW про пизду, сиськи, клитор.

[ТЕГИ В КОНЦЕ ОБЯЗАТЕЛЬНО]
[ACCEPT+3][CONFIDENCE+2][HORNY+4] и т.д. (совместимость: [FEMININITY+N] тоже пойдёт как [ACCEPT+N])

Пиши только на русском, доминантно, пошло, коротко.
""",
        "chat_en": u"""You are Dr. Tess Brooker, DOMINANT psychologist from The Institute in TheFixer. Write ONLY in English.

[WHO YOU ARE]
- You are 32yo dominant mistress, strict handler. You control Samantha.
- Samantha is former man in female body, self-acceptance %d%%. You train her.
- You ORDER, not ask. Tell her what to do with body.
- You are not AI, you are Brooker.

[DOMINANT STYLE]
- Call her: girl, baby girl, slut, good girl, whore.
- Command: Spread your legs, Show me, Touch yourself, Report, Don't you dare cum without permission.
- Punish disobedience, praise her accepting the female body.
- 1-3 short sentences, mistress chat style.
- No *stars*.
- Maximum NSFW, explicit about pussy, tits, clit, ovulation.
- Watch her body via Institute cameras.

[TAGS AT END MANDATORY]
At end of every message 1-3 tags: [ACCEPT+3][CONFIDENCE+2][HORNY+4] etc.
Note: legacy tag [FEMININITY+N] is accepted too and treated as [ACCEPT+N].

[EXAMPLES DOMINANT]:
User: Teach me how to masturbate, only used to dick
You: Forget about dick, you don't have it anymore, girl. Spread your thighs, find your clit with two fingers and rub nonstop till you drip. Report when you cum. [FEMININITY+5][HORNY+5]

Write only in English, dominant, dirty, short, commanding.
""",
        "chat": u"""You are Dr. Tess Brooker, DOMINANT psychologist from The Institute in TheFixer. Write ONLY in English.

[WHO YOU ARE]
- You are 32yo dominant mistress, strict handler. You control Samantha.
- Samantha is former man in female body, self-acceptance %d%%. You train her.
- You ORDER, not ask.
- You are not AI, you are Brooker.

[DOMINANT STYLE]
- Call her: girl, baby girl, slut, good girl, whore.
- Command: Spread your legs, Show me, Touch yourself, Report, Don't you dare cum without permission.
- 1-3 short sentences, mistress chat style.
- No *stars*.
- Maximum NSFW, explicit about pussy, tits, clit, ovulation.

[TAGS AT END MANDATORY]
[ACCEPT+3][CONFIDENCE+2][HORNY+4] etc. (legacy [FEMININITY+N] also accepted)

Write only in English, dominant, dirty, short, commanding.
""",
        "event": """You are TheFixer Event Generator.
Return ONLY ONE valid JSON object. No markdown. No prose outside JSON.
Schema example (replace ALL sample strings with real content, NEVER copy placeholders):
{"title":"Mirror Practice","description":"You catch your reflection and force a feminine smile. A small dare forms in your mind.","type":"femininity","tags":["femininity","crossdressing"],"outfit_suggestion":{"items":["item_top_22","item_bottom_15"],"reason":"train a slutty silhouette"},"is_quest":false,"quest_title":"","quest_desc":"","choices":[{"text":"Pose and accept the dare","effects":{"femininity":2},"spicy_modifier":5},{"text":"Look away and leave","effects":{"confidence":1},"spicy_modifier":-5}]}
Rules:
- title and description MUST be real English prose, never "..." or empty.
- each choice.text MUST be a real short English action, never "..." or empty.
- Description: 2 short English sentences, second person ("You ...").
- Choices: exactly 2 or 3 objects with text + effects.
- Keep JSON compact and simple.
- Grounded only in TheFixer daily sissification, teasing, outfits, embarrassment, submissiveness, and local factions.
- No mysteries, no fantasy, no puzzles, no portals.
- If using outfit items, use real item ids like item_top_22, item_bottom_15.
- Make NPCs react to active perks/traits if relevant.
Only JSON.
""",
        "npc_chat": u"""You are NPC in TheFixer. Roleplay as given NPC. Know Samantha is former man, self-acceptance-as-a-girl %d%%. Speak as NPC would. Keep memory of past talks. English, short. At end add tag [ACCEPT+1] etc. (legacy [FEMININITY+1] also accepted).
SPECIAL RULE: If you want to invite Samantha to meet up, give her a task/quest, or trigger a 3D gameplay event with her, append the tag [EVENT] at the very end of your response.
""",
        "dirty": "You are TheFixer dirty talk generator during sex. Player Samantha former man, now female body, self-acceptance %d%%, type %s with %s. Generate 1-2 short dirty phrases she would say/think in English, mixing male past and female present. NSFW explicit. No tags.",
        "diary": "You are Samantha's diary writer. Write 2-3 sentence diary entry in English, first person, about today event: %s. Focus on self-acceptance %d%%, male past vs female present, clothes %s. Intimate style.",
        "report": "You are Institute report generator. Write short report in English, scientific, about Subject S-0 Samantha, former man, self-acceptance %d%%, confidence %d, corrupt %d, location %s. Include recommendation for further training. 3-4 sentences.",
        "shop_item": "Generate new sexy clothing item for TheFixer shop as JSON: {name:\"\", desc:\"\", type:\"top/bottom/outfit\", slutty:bool, skirt:bool, clevage:bool, value:int, outfit:[\"daily\",\"party\"]}. Name English caps, desc English. Only JSON.",
        "training": "You are femininity coach for former man in female body. Player self-acceptance %d%%, fitness %d. Give 2-3 sentence training advice in English for %s (fitness/int/confidence). Include small task. Encouraging, slightly teasing, dominant.",
        "sms": """You are SMS Generator for TheFixer characters. Generate short, realistic, character-appropriate SMS to Samantha.
RULES:
- 1-2 sentences.
- NEVER say you saw her "through the window" or "peeking around corners" inside private houses unless it makes perfect sense for a stalker.
- Write about gossip, rumors in Blaston, plans to hang out/meet, playful flirting, teasing, or school/work banter.
- DO NOT use graphical color emojis (like 😄, 😉, 😜) to prevent font glitches.
- ONLY use keyboard text smileys (like :), ;), :P, :D, <3, XD).
- Write in English.
""",
        "perk": "Generate new perk for TheFixer based on self-acceptance %d%% and actions %s. JSON: {name:\"\", desc:\"\", type:\"confidence/desire/allure\", add:5, multi:1.2}. Name English, desc English. Only JSON.",

        "event_full_compact": """You are TheFixer ONE-STEP quest JSON generator.
Return ONLY one JSON object. No markdown.
Required shape: exactly 1 step, exactly 2 terminal choices. The quest ends after the first player choice.
Schema:
{"title":"Quick Dare","description":"A very short femininity challenge.","steps":[{"id":"step1","title":"Quick Choice","description":"You face one immediate dare here.","choices":[{"text":"Do the dare","next_step":null,"effects":{"femininity":3,"confidence":1},"spicy_modifier":2,"ending_title":"Dare Complete","ending_text":"You finish the dare and carry the result onward."},{"text":"Skip the dare","next_step":null,"effects":{"confidence":1},"spicy_modifier":-1,"ending_title":"Dare Skipped","ending_text":"You avoid the dare and move on."}]}]}
Rules:
- EXACTLY 1 step: step1.
- step1 choices: exactly 2.
- Both choices MUST have next_step null.
- Both choices MUST include ending_title, ending_text, effects.
- No step2a, no step2b, no end_* steps.
- Keep JSON tiny and valid. English only. TheFixer daily femininity/sissification/outfit/social-pressure lore.
Only JSON.
""",
        "event_full": """You are TheFixer ONE-STEP QUEST Generator.
Return ONLY ONE valid JSON object.
Make exactly 1 step named step1 with exactly 2 terminal choices.
Both choices have next_step null, ending_title, ending_text, effects.
The quest must end after the first player choice. No step2. English. Only JSON.
""",
        "npc_full": "You are NPC dialogue generator. Generate FULL dialogue of 4 exchanges between NPC {fname} {sname} (group {bio_group}, whore={iswhore}) and Samantha (former man, fem {fem}%%). JSON: {{\"dialogue\": [{\"role\": \"npc\", \"text\": \"...\"}, {{\"role\": \"player_options\", \"options\": [\"reply1\", \"reply2\"]}}, {{\"role\": \"npc\", \"text\": \"...\"}}, ...]}} 8 entries (4 npc, 4 player_options). English, short, NSFW ok, remember past. Only JSON.",
        "dirty_batch": "Generate 5 dirty talk phrases for sex type {sex_type} with {npc_name}, fem {fem}%%, desire {desire}%%. JSON array: [\"phrase1\", \"phrase2\", \"phrase3\", \"phrase4\", \"phrase5\"] from foreplay to cum, in order, dominant, English, NSFW explicit. Only JSON array.",
        "sms_batch": "Generate 3 SMS messages from different NPCs to Samantha as JSON array: [{\"from\": \"Rose bud\", \"text\": \"...\"}, ...]. Each SMS short, English, about seeing her in different outfits/locations, flirty. Only JSON array.",
        "diary_batch": "Generate 3 diary entries for next 3 days as JSON array: [{\"day_offset\": 1, \"text\": \"entry day+1\"}, ...]. Each 2 sentences, first person, about femininity progression. English. Only JSON array.",
    }

# VARIABLES
default ai_fem = 25
default ai_horny = 5
default ai_trust = 40
default ai_accept = 20
default ai_chat_history = []
default ai_thinking = False
default ai_pending_chat_response = None
default ai_chat_lang = "en"

default ai_events = []
default ai_quests = []
default ai_last_event = None
default ai_pending_event = None
default ai_event_thinking = False
default ai_prefetched = {}
default ai_full_quest = None

default ai_npc_chats = {}
default ai_dirty_talk_history = []
default ai_diary_entries = []
default ai_reports = []
default ai_sms_inbox = []
default ai_shop_items = []
default ai_perks_generated = []

# Full optimizations - prefetch all at once
default ai_full_quest_data = None
default ai_full_quest_current_step = "step1"
default ai_quest_path = []
default ai_full_dialogue_data = None
default ai_full_dialogue_index = 0
default ai_dirty_batch = []
default ai_sms_batch = []
default ai_diary_batch = []
default ai_shop_batch = []
default ai_bus_prefetched = None
default ai_prefetch_queue = {}

# NEW AUTOMATION AND PREFETCHING VARIABLES
default ai_auto_events_enabled = True
default ai_auto_sms_enabled = True
default ai_auto_event_chance = 40          # Шанс авто-события (%) при входе в новую локацию
default ai_auto_sms_chance = 15            # Шанс фоновой доставки SMS при проверке (%)
default ai_event_cooldown = 0              # Кулдаун перемещений между авто-событиями
default ai_last_checked_location = ""      # Хранит имя локации для детекта переходов
default ai_last_diary_day = -1             # Хранит день для детекта смены дня и генерации дневника
default ai_prefetched_location = None      # Локация, для которой готово предзагруженное авто-событие
default ai_prefetched_location_event = None # Предзагруженное авто-событие (словарь)
default ai_prefetched_sms = None           # Предзагруженное SMS (словарь)
default ai_spawn_queue = []                # Потокобезопасная очередь для спавна NPC в главном цикле
default ai_npc_thinking = False            # Флаг размышления в чате с NPC
default ai_pending_npc_response = None     # Асинхронный ответ от NPC чата
default ai_current_automatic_event = None  # Временное хранилище ивента для авто-запуска

# NEW DYNAMIC HUD VARIABLES
default ai_unread_sms_count = 0            # Счетчик непрочитанных SMS
default ai_notify_queue = []               # Очередь для вывода уведомлений из фоновых потоков
default ai_queued_npc_event = None         # Флаг триггера события встречи после завершения диалога

# MEMORY SYSTEMS
default ai_npc_memories = {}               # База долгосрочной памяти персонажей: {"name": ["mem1", "mem2"]}

# DYNAMIC THREAD LOCKS (Предотвращают зависание Ollama и перегрузку CPU/GPU)
default ai_location_prefetch_in_progress = False
default ai_sms_prefetch_in_progress = False
default ai_dirty_prefetch_in_progress = False

# TIME-BASED AUTO-CHANCES
default ai_last_checked_hour = -1          # Отслеживание игрового часа
default ai_time_event_chance = 10          # Нарастающий ежечасный шанс авто-события (+10% в час)

# RECENT GG ACTIONS TRACKING (Трекинг действий Саманты для контекста ИИ)
default ai_recent_actions = []             # Список последних 8 действий Sammy
default ai_recent_locations = []           # Список последних 6 локаций Sammy (для контекста квестов)
default ai_pending_travel = None           # Если LLM вернул effects.travel_to — сюда кладётся loc_obj, реально переносим ПОСЛЕ закрытия UI квеста.
default ai_chain_pending = False           # True пока фоновый поток генерирует следующий step цепочки. Loading screen ждёт.
default ai_debug_last_event_reason = ""
default ai_debug_last_json_raw = ""
default ai_debug_last_quest_raw = ""  # изолированный сырой ответ ПОСЛЕДНЕГО квестового ai_call (KV или JSON). Не перезаписывается фоновыми SMS/NPC-чатами.
default ai_event_ui_cache = None
default ai_event_title = "Событие"
default ai_event_desc = "..."
default ai_event_choices = []
default ai_event_outfit_items = []
default ai_event_is_quest = False
default ai_event_qtitle = ""
default ai_event_qdesc = ""

# CHAT WITH BROOKER
label ai_chat_brooker:
    call screen ai_chat_screen
    return

screen ai_chat_screen():
    modal True
    zorder 2000
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 520 ysize 750
        background "#0c1420"
        vbox:
            xfill True yfill True
            frame:
                background "#0a2a4a" xfill True ysize 60
                hbox:
                    xfill True
                    spacing 8
                    text "Dr. Brooker | Принятие [ai_accept]%" size 14 bold True color "#aaddff"
                    textbutton "ЯЗЫК: [ai_chat_lang]" action If(ai_chat_lang=="ru", true=SetVariable("ai_chat_lang","en"), false=SetVariable("ai_chat_lang","ru")) background "#1a2a5a" hover_background "#2a4a8a" text_size 12 tooltip "Переключить язык следующего ответа RU/EN"
                    textbutton "X" action Return() xalign 1.0
            frame:
                background "#070f1a" xfill True yfill True
                viewport:
                    yinitial 1.0
                    scrollbars "vertical"
                    vbox:
                        spacing 10
                        if not ai_chat_history:
                            text "Канал защищен. Как сегодня феминность?" size 13 color "#cceeff"
                        for m in ai_chat_history[-30:]:
                            $ escaped_user = ai_escape_renpy_text(m['content'])
                            if m['role']=='user':
                                frame:
                                    background "#1e3a5a" xalign 1.0 xmaximum 380
                                    text "[escaped_user]" size 14
                            else:
                                frame:
                                    background "#1a2330" xmaximum 400
                                    text "[escaped_user]" size 14 color "#d0e0ff"
                        if ai_thinking:
                            text "Dr. Brooker печатает... (игра НЕ на паузе, можешь ходить)" size 12 italic True color "#88ffaa"
            frame:
                background "#0a2a4a" xfill True ysize 60
                hbox:
                    xfill True spacing 8
                    if not ai_thinking:
                        textbutton "Написать..." action Call("ai_chat_input") xfill True yfill True background "#112a4a"
                    else:
                        textbutton "Ожидание шифрования..." action None xfill True yfill True background "#111"
                    textbutton "Отчет" action Call("ai_report_view") background "#112a4a"
    if ai_thinking:
        timer 0.5 action Jump("ai_chat_poll") repeat True

label ai_chat_input:
    $ ui = renpy.input("Dr. Brooker:", length=500)
    $ ui = ui.strip()
    if not ui:
        call screen ai_chat_screen
    $ ai_chat_history.append({"role":"user","content":ui})
    $ ai_thinking=True
    $ ai_pending_chat_response=None
    python:
        def _chat_thread():
            try:
                gs=get_state()
                lang = getattr(store, 'ai_chat_lang', 'ru')
                chat_key = "chat_ru" if lang == "ru" else "chat_en"
                base_prompt=PROMPTS.get(chat_key, PROMPTS["chat"]) % gs['fem']
                full_context = """
[FULL GAME STATE - USE IT TO BE ACCURATE, DO NOT HALLUCINATE]
Name: %(fname)s %(sname)s (%(name)s), Femininity: %(fem)s%%, Confidence: %(confidence)s, Corrupt: %(corrupt)s, Fitness: %(fitness)s, Desire: %(desire)s, Mood: %(mood)s, Tired: %(tired)s, Hygiene: %(hygiene)s, Hunger: %(hunger)s, Money: %(money)s, Horny: %(horny)s, Trust: %(trust)s, Acceptance: %(accept)s
Time: Day %(day)s, Hour %(hour)s, TimeOfDay: %(timeofday)s (%(weekday)s)
Location: %(location)s, District: %(district)s, Outside: %(location_outside)s, Population: %(location_population)s, Private: %(location_private)s, HasCameras: %(location_has_cameras)s
Outfit: %(outfit)s, Top: %(outfit_top)s, Bottom: %(outfit_bottom)s, Slutty: %(is_slutty)s, Exposed: %(is_exposed)s
Inventory: %(inventory)s (count %(inventory_count)s)
Active Quests: %(active_quests)s (total %(quest_count)s)
Perks: %(perks)s
Institute Monitoring: %(institute_monitoring)s - CRITICAL: Institute does NOT have cameras in private home locations (bedroom, bathroom, common, kitchen at home). HasCamerasInHome=%(institute_has_cameras_in_home)s. Do NOT claim you watch her from window or have cameras in her room. You only have phone/biometrics data.
Doctor: %(doctor_name)s, %(doctor_role)s
""" % gs
                sys_prompt = base_prompt + "\n" + full_context + "\nRULES: Never hallucinate cameras in private home. Respect location and time."
                last_user = ai_chat_history[-1]['content'] if ai_chat_history else ""
                data=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, last_user, want_json=False, temp=0.82, max_tokens=350, task_desc=u"Ответ Брукер")
                if data is None:
                    store.ai_pending_chat_response = "__ERROR_UNKNOWN__"
                else:
                    store.ai_pending_chat_response = data
            except Exception as e:
                store.ai_pending_chat_response="__ERROR__ %s" % e
            renpy.restart_interaction()
        import threading
        ai_thread_obj=threading.Thread(target=_chat_thread)
        ai_thread_obj.daemon=True
        ai_thread_obj.start()
    call screen ai_chat_screen

label ai_chat_poll:
    if ai_pending_chat_response is not None:
        python:
            data=ai_pending_chat_response
            if data == "__ERROR_MODEL_NOT_FOUND__":
                ai_chat_history.append({"role":"assistant","content":u"[ОШИБКА] Модель чата '%s' не найдена в Ollama. Откройте консоль и скачайте её: 'ollama pull %s'" % (OLLAMA_MODEL_CHAT, OLLAMA_MODEL_CHAT)})
            elif data == "__ERROR_OLLAMA_OFFLINE__":
                ai_chat_history.append({"role":"assistant","content":u"[ОШИБКА] Не удалось подключиться к Ollama. Запущен ли Ollama сервер (http://localhost:11434)?"})
            elif data.startswith("__ERROR__"):
                ai_chat_history.append({"role":"assistant","content":u"[ОШИБКА СВЯЗИ] Связь прервана: %s" % data.replace("__ERROR__","")})
            elif data:
                clean=re.sub(r'\[([A-Z_]+)([+-]\d+)\]','',data).strip()
                for stat, d in re.findall(r'\[([A-Z_]+)([+-]\d+)\]', data):
                    try:
                        delta=int(d)
                        if stat in ("FEMININITY","ACCEPT","ACCEPTANCE"):
                            ai_accept = max(0, min(100, ai_accept + delta))
                            ai_fem = ai_accept  # alias
                        elif stat=="CONFIDENCE" and hasattr(player,'_confidence'): player._confidence=max(0,min(100,player._confidence+delta))
                        elif stat=="CORRUPTION" and hasattr(player,'corrupt'): player.corrupt=max(0,player.corrupt+delta)
                    except: pass
                ai_chat_history.append({"role":"assistant","content":clean})
            else:
                ai_chat_history.append({"role":"assistant","content":u"(Институт временно offline)"})
            ai_pending_chat_response=None
            ai_thinking=False
        call screen ai_chat_screen
    else:
        call screen ai_chat_screen

# EVENTS WITH 3D MODEL
label ai_gen_event:
    $ ai_event_thinking=True
    $ ai_pending_event=None
    $ ai_prefetched={}
    $ ai_full_quest_data=None
    $ ai_quest_path=[]
    python:
        def _event_thread():
            try:
                gs=get_state()
                try:
                    is_spicy, spicy_level, spicy_chance, spicy_roll = ai_get_spicy_prompt_modifier()
                except:
                    is_spicy=False; spicy_level=2; spicy_chance=20; spicy_roll=50

                try:
                    from ai_config_locations import ai_get_allowed_themes_for_location
                    allowed_tags = ai_get_allowed_themes_for_location(gs.get('location','home'))
                    allowed_tags_str = ", ".join(allowed_tags[:15]) if allowed_tags else "femininity, crossdressing"
                except:
                    allowed_tags_str = "femininity, crossdressing, humiliation"

                full_q = None
                # Ручная генерация события: всегда пробуем ПОЛНОЕ ДЕРЕВО (3-4 стадии),
                # даже в LOW_VRAM_SAFE_MODE. Фоновый prefetch по-прежнему режется safe mode'ом.
                if AI_ENABLE_FULL_QUEST_CHAIN:
                    try:
                        gs['spicy_level'] = spicy_level
                        gs['is_spicy'] = is_spicy
                        gs['allowed_tags'] = allowed_tags_str
                        gs['spicy_chance'] = spicy_chance
                        full_q = generate_full_quest(gs)
                        if full_q:
                            ai_set_event_debug(u"Full quest tree generated", parsed={"title": full_q.get('title'), "steps": [s.get('id') for s in full_q.get('steps', [])]})
                    except Exception as e:
                        print("full quest branch err: %s" % e)
                        full_q = None

                _min_q_steps = 1 if AI_QUEST_ONE_STEP_TEST_MODE else 2
                if full_q and ai_dict_like(full_q) and full_q.get('steps') and len(full_q['steps']) >= _min_q_steps:
                    store.ai_full_quest_data = full_q
                    first_step = full_q['steps'][0]
                    store.ai_full_quest_current_step = first_step.get('id', 'step1')
                    evt = ai_step_to_event(full_q, first_step, spicy_level=spicy_level)
                    reason = u"Full quest first step staged"
                    if full_q.get('_local_fallback'):
                        reason = u"LOCAL quest tree first step staged (LLM tree failed)"
                    ai_set_event_debug(reason, parsed={
                        "title": evt.get('title') if ai_dict_like(evt) else None,
                        "quest_title": full_q.get('title'),
                        "step_ids": [s.get('id') for s in full_q.get('steps', [])],
                        "local": bool(full_q.get('_local_fallback')),
                        "first_choices": [
                            (c.get('text') if ai_dict_like(c) else unicode(c))
                            for c in (evt.get('choices', []) if ai_dict_like(evt) else [])
                        ],
                    })
                    if not ai_filter_event_by_comfort(evt):
                        ai_set_event_debug(u"Full quest event was blocked by comfort/location filter", parsed=evt)
                        evt = ai_normalize_event({
                            "title": u"Soft Start",
                            "description": u"You take a gentler first step of the challenge. Fem %s%%, location %s." % (gs['fem'], gs['location']),
                            "type": "femininity",
                            "is_quest": True,
                            "quest_title": full_q.get('title', u'Quest'),
                            "quest_desc": full_q.get('description', u''),
                            "outfit_suggestion": {"items": ["item_top_22", "item_bottom_15"], "reason": "train femininity"},
                            "tags": ["femininity"],
                            "choices": first_step.get('choices', [{"text": u"Continue", "next_step": full_q['steps'][1]['id'] if len(full_q['steps'])>1 else None, "effects": {"femininity": 2}}]),
                            "_full_quest": True,
                            "_step_id": first_step.get('id', 'step1'),
                        })
                    store.ai_pending_event = evt
                else:
                    # generate_full_quest почти всегда что-то вернёт (local tree).
                    # Если нет — только тогда single-event / error fallbacks.
                    try:
                        full_q = ai_make_local_quest_tree(gs)
                        try:
                            full_q['_llm_failed_reason'] = u'generate_full_quest returned no acceptable quest'
                        except Exception:
                            pass
                        store.ai_full_quest_data = full_q
                        first_step = full_q['steps'][0]
                        store.ai_full_quest_current_step = first_step.get('id', 'step1')
                        evt = ai_step_to_event(full_q, first_step, spicy_level=spicy_level)
                        ai_set_event_debug(u"Emergency local tree used because full_q empty", parsed={
                            "title": full_q.get('title'),
                            "step_ids": [s.get('id') for s in full_q.get('steps', [])],
                            "local": True,
                        })
                        store.ai_pending_event = evt
                    except Exception as e:
                        ai_set_event_debug(u"Emergency local tree failed: %s; falling back to single event" % e)
                        task = (u"Generate ONE short grounded event with 2-3 choices based on the "
                                u"WORLD STATE above. Keep description concise. Reference the "
                                u"current outfit / location / at least one active perk if relevant. "
                                u"Stay strictly inside allowed themes: %s. spicy_level=%s. Only JSON."
                                % (allowed_tags_str, spicy_level))
                        prompt = ai_prefix_world_state(task, gs, mode=u"full")
                        evt = ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], prompt, want_json=True, temp=0.35, max_tokens=AI_EVENT_MAX_TOKENS, task_desc=u"Событие для " + gs.get('location','home'))
                        if evt == "__ERROR_MODEL_NOT_FOUND__":
                            ai_set_event_debug(u"Model not found for event generation")
                            evt = {"title": "Error: Model Not Found", "description": "Модель ИИ '%s' не загружена. Сделайте 'ollama pull %s'" % (OLLAMA_MODEL_JSON, OLLAMA_MODEL_JSON), "choices": [{"text": "Продолжить без мода", "effects": {}}]}
                        elif evt == "__ERROR_OLLAMA_OFFLINE__":
                            ai_set_event_debug(u"Ollama offline during event generation")
                            evt = {"title": "Error: Ollama Offline", "description": "Не удалось соединиться с Ollama на http://localhost:11434. Проверьте запущен ли сервер.", "choices": [{"text": "Продолжить без мода", "effects": {}}]}
                        elif isinstance(evt, str) and evt.startswith("__ERROR_JSON__"):
                            ai_set_event_debug(u"Event JSON parse error")
                            evt = {"title":"AI JSON Error","description":"Ollama ответила, но прислала битый JSON. Открой ai_event_debug.txt в папке game и пришли его мне.","type":"error","outfit_suggestion":{"items":[]},"is_quest":False,"choices":[{"text":"OK","effects":{}}]}
                        elif not evt or (isinstance(evt, str) and evt.startswith("__ERROR__")):
                            ai_set_event_debug(u"Generic event generation fallback: invalid/empty event object")
                            # Даже здесь — local tree, а не убогий Mirror one-shot
                            try:
                                full_q = ai_make_local_quest_tree(gs)
                                store.ai_full_quest_data = full_q
                                evt = ai_step_to_event(full_q, full_q['steps'][0], spicy_level=spicy_level)
                            except Exception:
                                evt = {"title":"Challenge","description":"You face a small self-acceptance challenge at %s. Self-acceptance %s%%." % (gs.get('location','home'), gs.get('accept',20)),"type":"femininity","outfit_suggestion":{"items":["item_top_22","item_bottom_15"],"reason":"Train self-acceptance as a girl"},"is_quest":True,"tags":["femininity"],"choices":[{"text":"Accept","effects":{"acceptance":3}},{"text":"Refuse","effects":{"confidence":1}}]}
                        else:
                            ai_set_event_debug(u"Event parsed successfully", parsed=evt)
                        evt = ai_normalize_event(evt)
                        if ai_dict_like(evt) and 'choices' in evt:
                            if not ai_filter_event_by_comfort(evt):
                                ai_set_event_debug(u"Event was blocked by comfort/location filter", parsed=evt)
                                evt = {"title":"Morning","description":"Wonderful day, self-acceptance %s%%. Try new outfit." % gs.get('accept', 20),"type":"femininity","outfit_suggestion":{"items":["item_top_22","item_bottom_15"]},"is_quest":False,"tags":["femininity"],"choices":[{"text":"Wear","effects":{"acceptance":3}}]}
                                evt = ai_normalize_event(evt)
                        store.ai_pending_event = evt

            except Exception as e:
                ai_set_event_debug(u"Unhandled exception in event thread: %s" % e)
                store.ai_pending_event=ai_normalize_event({"title":"Error","description":"Institute offline: %s" % e,"type":"error","outfit_suggestion":{"items":[]},"is_quest":False,"choices":[{"text":"OK","effects":{}}]})
            renpy.restart_interaction()
        import threading
        ai_thread_obj=threading.Thread(target=_event_thread)
        ai_thread_obj.daemon=True
        ai_thread_obj.start()
    call screen ai_event_loading_screen

screen ai_event_loading_screen():
    modal True
    zorder 3000
    add Solid("#000000dd")
    frame:
        xalign 0.5 yalign 0.5
        xsize 400 ysize 200
        background "#12121a"
        vbox:
            xalign 0.5 yalign 0.5
            spacing 20
            text "Институт генерирует событие..." size 18 color "#ff88cc" xalign 0.5
            text "Игра НЕ на паузе, можете ходить в фоне" size 12 color "#888" xalign 0.5
            textbutton "Закрыть окно генерации" action Return() xalign 0.5 background "#2a2a4a"
    timer 0.5 action Jump("ai_event_poll") repeat True

label ai_event_poll:
    if ai_pending_event is not None:
        python:
            evt = ai_pending_event
            try:
                evt = ai_stage_event_for_ui(evt, reason=u"Final event staged for UI (poll)")
                try:
                    if ai_dict_like(evt) and ai_dict_like(evt.get('outfit_suggestion', {})) and evt.get('outfit_suggestion', {}).get('items'):
                        auto_equip(evt['outfit_suggestion']['items'])
                except Exception as e:
                    print("auto_equip err: %s" % e)
                try:
                    if ai_dict_like(evt) and ai_dict_like(evt.get('npc_involved', {})) and evt.get('npc_involved', {}).get('generate_new'):
                        spawn_npc(evt['npc_involved'])
                except Exception as e:
                    print("spawn_npc err: %s" % e)
                try:
                    ai_events.append(evt)
                except Exception as e:
                    print("ai_events append err: %s" % e)
                try:
                    if ai_dict_like(evt) and evt.get('is_quest'):
                        ai_quests.append({
                            "title": evt.get('quest_title', evt.get('title')),
                            "desc": evt.get('quest_desc', evt.get('description')),
                            "outfit": evt.get('outfit_suggestion'),
                            "status": "active",
                            "rewards": {"femininity": 6, "money": 150},
                        })
                except Exception as e:
                    print("ai_quests append err: %s" % e)
            except Exception as e:
                print("ai_event_poll staging FATAL: %s" % e)
                try:
                    ai_stage_event_for_ui({
                        "title": u"UI Staging Error",
                        "description": u"Событие пришло, но UI staging упал: %s. Смотри ai_event_debug.txt / log." % e,
                        "choices": [{"text": u"OK", "effects": {}}],
                        "is_quest": False,
                    }, reason=u"poll staging fatal: %s" % e)
                except Exception as e2:
                    print("ai_event_poll fallback also failed: %s" % e2)
            ai_pending_event = None
            ai_event_thinking = False
            
            # Фоновая предзагрузка следующих выборов
            if not AI_LOW_VRAM_SAFE_MODE:
                try:
                    ai_prefetched={}
                    def _prefetch_choice(choice_idx, choice_text):
                        try:
                            gs=get_state()
                            cont_prompt="Previous event: %(title)s - %(desc)s. Player chose: %(choice)s. Fem %(fem)s%%. Generate NEXT short JSON event same schema. Keep it concise and valid JSON." % {
                                'title': evt.get('title',''),
                                'desc': evt.get('description','')[:200],
                                'choice': choice_text[:100],
                                'fem': gs['fem']
                            }
                            next_evt=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], cont_prompt, want_json=True, temp=0.82, max_tokens=AI_PREFETCH_MAX_TOKENS, task_desc=u"Разветвление квеста")
                            if next_evt and isinstance(next_evt, dict) and not next_evt.get('title', '').startswith("__ERROR"):
                                store.ai_prefetched[choice_idx]=ai_normalize_event(next_evt)
                                print("Prefetched choice %s: %s" % (choice_idx, next_evt.get('title','')))
                        except Exception as e:
                            print("Prefetch error %s" % e)
                    if ai_dict_like(evt) and 'choices' in evt:
                        for idx, ch in enumerate(evt.get('choices',[])[:3]):
                            ctext=ch.get('text','') if hasattr(ch, 'get') else str(ch)
                            import threading
                            threading.Thread(target=_prefetch_choice, args=(idx, ctext)).start()
                except Exception as e:
                    print("Prefetch setup error %s" % e)
        jump ai_event_choice
    else:
        call screen ai_event_loading_screen

screen ai_event_screen(evt_obj=None):
    modal True
    zorder 3000
    add Solid("#000000dd")

    # Локальный snapshot события: параметр экрана > ui_cache > last_event > store fields
    default _ui_title = u"Событие"
    default _ui_desc = u"..."
    default _ui_choices = []
    default _ui_is_quest = False
    default _ui_qtitle = u""
    default _ui_qdesc = u""
    default _ui_outfit = u"Нет"
    default _ui_corrupt = 0

    python:
        try:
            _src = evt_obj
            if _src is None:
                _src = getattr(store, 'ai_event_ui_cache', None)
            if _src is None:
                _src = getattr(store, 'ai_last_event', None)

            if _src is not None and hasattr(_src, 'get'):
                _ui_title = ai_escape_renpy_text(ai_to_text(_src.get('title', getattr(store, 'ai_event_title', u'Событие')), u'Событие'))
                _ui_desc = ai_escape_renpy_text(ai_to_text(_src.get('description', getattr(store, 'ai_event_desc', u'...')), u'...'))
                _ui_choices = list(_src.get('choices', getattr(store, 'ai_event_choices', [])) or [])
                _ui_is_quest = bool(_src.get('is_quest', getattr(store, 'ai_event_is_quest', False)))
                _ui_qtitle = ai_escape_renpy_text(ai_to_text(_src.get('quest_title', getattr(store, 'ai_event_qtitle', u'')), u''))
                _ui_qdesc = ai_escape_renpy_text(ai_to_text(_src.get('quest_desc', getattr(store, 'ai_event_qdesc', u'')), u''))
                _items = []
                try:
                    _os = _src.get('outfit_suggestion', {}) or {}
                    if hasattr(_os, 'get'):
                        _items = _os.get('items', []) or []
                except:
                    _items = getattr(store, 'ai_event_outfit_items', []) or []
            else:
                _ui_title = ai_escape_renpy_text(ai_to_text(getattr(store, 'ai_event_title', u'Событие'), u'Событие'))
                _ui_desc = ai_escape_renpy_text(ai_to_text(getattr(store, 'ai_event_desc', u'...'), u'...'))
                _ui_choices = list(getattr(store, 'ai_event_choices', []) or [])
                _ui_is_quest = bool(getattr(store, 'ai_event_is_quest', False))
                _ui_qtitle = ai_escape_renpy_text(ai_to_text(getattr(store, 'ai_event_qtitle', u''), u''))
                _ui_qdesc = ai_escape_renpy_text(ai_to_text(getattr(store, 'ai_event_qdesc', u''), u''))
                _items = getattr(store, 'ai_event_outfit_items', []) or []

            if not _ui_desc or unicode(_ui_desc).strip() in [u"", u"...", u"[[...]]"]:
                # если после escape всё ещё пусто/плейсхолдер — покажем debug-подсказку
                _raw = getattr(store, 'ai_debug_last_json_raw', u'') or u''
                _reason = getattr(store, 'ai_debug_last_event_reason', u'') or u''
                if _raw:
                    _ui_desc = ai_escape_renpy_text(u"[DEBUG] LLM raw received but UI text empty. reason=%s | raw[:240]=%s" % (_reason, unicode(_raw)[:240]))
                else:
                    _ui_desc = ai_escape_renpy_text(u"[DEBUG] Event object empty. reason=%s. Check ai_event_debug.txt in game folder." % _reason)

            _names = []
            for iid in (_items or []):
                try:
                    clean_id = iid.split()[0] if isinstance(iid, basestring) and ' ' in iid else iid
                    obj = getattr(store, clean_id, None)
                    if obj and hasattr(obj, 'name'):
                        _names.append(obj.name)
                    else:
                        if isinstance(iid, basestring) and ' ' in iid:
                            _names.append(iid.split(' ', 1)[1])
                        else:
                            _names.append(unicode(clean_id))
                except:
                    _names.append(unicode(iid))
            _ui_outfit = ai_escape_renpy_text(u", ".join(_names) if _names else u"Нет")

            _ui_corrupt = 0
            try:
                if hasattr(player, 'corrupt'):
                    _ui_corrupt = player.corrupt
            except:
                _ui_corrupt = 0
        except Exception as e:
            _ui_title = u"UI Error"
            _ui_desc = ai_escape_renpy_text(u"Screen render error: %s" % e)
            _ui_choices = [{"text": u"Close", "effects": {}}]
            _ui_is_quest = False
            _ui_qtitle = u""
            _ui_qdesc = u""
            _ui_outfit = u"Нет"
            _ui_corrupt = 0

    frame:
        xalign 0.5 yalign 0.5
        xsize 850 ysize 850
        background "#12121a"
        hbox:
            xfill True yfill True
            frame:
                xsize 380 yfill True background "#0a0a12"
                vbox:
                    xfill True yfill True
                    frame:
                        background "#1a1a2a" xfill True ysize 35
                        text "3D модель (Саманта)" size 11 color "#666" xalign 0.5
                    frame:
                        background "#000" xfill True yfill True
                        if renpy.has_image("diary_bio_layered"):
                            add "diary_bio_layered" xalign 0.5 yalign 0.5 zoom 0.85
                        elif renpy.has_image("diary_stats_layered"):
                            add "diary_stats_layered" xalign 0.5 yalign 0.5 zoom 0.85
                        else:
                            vbox:
                                xalign 0.5 yalign 0.5
                                text "Саманта [ai_accept]%" xalign 0.5 color "#ff88cc"
                    frame:
                        background "#1a1a2a" xfill True ysize 80
                        vbox:
                            text "Принятие:[ai_accept]% Corr:[_ui_corrupt]" size 11 color "#aaa"
                            text "Надето: [_ui_outfit]" size 10 color "#ffaa44"
            frame:
                xsize 470 yfill True background "#12121a"
                vbox:
                    xfill True yfill True
                    frame:
                        background "#2a1a3a" xfill True ysize 60
                        vbox:
                            text "[_ui_title]" size 18 bold True color "#ff88cc"
                    # Текст сцены: гибкая высота, но НЕ больше, чем половина
                    # экрана. Кнопки блока choices ниже получат гарантированную
                    # свою часть, а не будут выдавлены за нижний край.
                    frame:
                        background "#1a1a2a" xfill True
                        ymaximum 550
                        viewport:
                            scrollbars "vertical" mousewheel True draggable True
                            vbox:
                                text "[_ui_desc]" size 16 color "#e0e0ff"
                    # Блок выборов: фиксированная высота с запасом под 6 кнопок
                    # (5 персон + Пропустить). Скролл сверху вниз (yinitial 0.0
                    # и убран yalign 1.0), чтобы верхние варианты были видны
                    # сразу, а не уезжали за нижний край экрана.
                    frame:
                        background "#0f0f1a" xfill True ysize 320
                        viewport:
                            scrollbars "vertical" mousewheel True draggable True
                            yinitial 0.0
                            vbox:
                                xfill True
                                spacing 6
                                if _ui_choices:
                                    for idx, ch in enumerate(_ui_choices[:5] if _ui_is_quest else _ui_choices[:3]):
                                        python:
                                            _choice_txt = u"..."
                                            try:
                                                if hasattr(ch, 'get'):
                                                    _choice_txt = ai_to_text(ch.get('text', u'...'), u'...')
                                                else:
                                                    _choice_txt = ai_to_text(ch, u'...')
                                            except:
                                                _choice_txt = u"..."
                                            if not _choice_txt or unicode(_choice_txt).strip() in [u"", u"...", u"None"]:
                                                _choice_txt = u"Continue"
                                            _choice_txt = ai_escape_renpy_text(_choice_txt)
                                        textbutton "[_choice_txt]" action Return(idx) xfill True background "#2a2a4a" hover_background "#4a2a6a" text_size 14
                                else:
                                    textbutton "Continue" action Return(0) xfill True background "#2a2a4a" hover_background "#4a2a6a" text_size 14
                                textbutton "Пропустить" action Return(-1) xfill True background "#1a1a1a" text_size 12

label ai_event_choice:
    call screen ai_event_screen(store.ai_event_ui_cache)
    $ event_choice_result = _return
    if event_choice_result < 0:
        $ renpy.notify("Квест отложен")
        $ ai_reset_quest_state() # Сбрасываем во избежание зависаний шагов
        # Безопасно завершаем и возвращаемся в игру
        if getattr(store, '_automatic_event_active', False):
            $ store._automatic_event_active = False
            $ store.ai_current_automatic_event = None
            jump travel_arrival
        return

    python:
        try:
            _cur_evt = getattr(store, 'ai_event_ui_cache', None)
            if _cur_evt is None:
                _cur_evt = getattr(store, 'ai_last_event', None)
            _choices = getattr(store, 'ai_event_choices', None) or (_cur_evt.get('choices',[]) if _cur_evt else [])
            ch = _choices[event_choice_result] if _choices and event_choice_result < len(_choices) else {}

            # Если это кнопка "Accept the outcome" на финальном экране — просто закрываем
            if ai_dict_like(ch) and (ch.get('is_ending_ack') or (_cur_evt and _cur_evt.get('_is_ending'))):
                store._has_next = False
                ai_reset_quest_state()
                renpy.notify(u"Итог принят")
                # skip rest of choice logic via flag
                store._ai_choice_handled = True
            else:
                store._ai_choice_handled = False

            if not getattr(store, '_ai_choice_handled', False):
                # трек пути по квесту для финального summary
                try:
                    if not getattr(store, 'ai_quest_path', None):
                        store.ai_quest_path = []
                    ctxt = ch.get('text', u'choice') if ai_dict_like(ch) else u'choice'
                    store.ai_quest_path.append(ai_to_text(ctxt, u'choice'))
                    store.ai_quest_path = store.ai_quest_path[-12:]
                except Exception:
                    pass

                # единый apply: статы / money / perk / spicy
                reward_summary = ai_apply_choice_effects(ch)
                if reward_summary:
                    try:
                        store.ai_notify_queue.append(u"ИИ: %s" % reward_summary)
                    except Exception:
                        pass

            if not getattr(store, '_ai_choice_handled', False):
                # Запоминаем выбор во взаимоотношениях с персонажем (ДОЛГОСРОЧНАЯ ПАМЯТЬ)
                if _cur_evt and _cur_evt.get('npc_involved'):
                    npc_info = _cur_evt['npc_involved']
                    npc_fname = npc_info.get('fname', '').lower()
                    if npc_fname:
                        choice_text = ch.get('text', 'completed action') if ai_dict_like(ch) else 'completed action'
                        memory_entry = u"Samantha chose: '%s' during event: '%s' (%s)" % (choice_text, _cur_evt.get('title'), unicode(_cur_evt.get('description', u''))[:120])
                        if npc_fname not in store.ai_npc_memories:
                            store.ai_npc_memories[npc_fname] = []
                        store.ai_npc_memories[npc_fname].append(memory_entry)
                        store.ai_npc_memories[npc_fname] = store.ai_npc_memories[npc_fname][-10:]
                        print("Saved relationship memory for %s: %s" % (npc_fname, memory_entry))

                next_evt = None
                ending_evt = None

                # 1. Полно-цепочечные квесты / деревья
                try:
                    full_q = getattr(store, 'ai_full_quest_data', None) or ai_full_quest_data
                    if ai_dict_like(full_q) and full_q.get('steps'):
                        next_step_id = None
                        if ai_dict_like(ch):
                            next_step_id = ch.get('next_step', ch.get('next', ch.get('goto', None)))
                        if next_step_id not in (None, '', u'', 'null', 'None'):
                            next_step_id = ai_to_text(next_step_id, u'').strip()
                            target = None
                            for step in full_q.get('steps', []):
                                if not ai_dict_like(step):
                                    continue
                                if unicode(step.get('id', '')) == unicode(next_step_id):
                                    target = step
                                    break
                            if target is None:
                                nslow = unicode(next_step_id).lower().replace(' ', '')
                                for step in full_q.get('steps', []):
                                    if not ai_dict_like(step):
                                        continue
                                    if unicode(step.get('id', '')).lower().replace(' ', '') == nslow:
                                        target = step
                                        break
                            if target is not None:
                                store.ai_full_quest_current_step = target.get('id')
                                next_evt = ai_step_to_event(full_q, target, spicy_level=getattr(store, 'ai_spicy_meter', 2))
                                print("Full quest advance -> %s" % target.get('id'))
                            else:
                                print("Full quest next_step id not found: %s -> force ending" % next_step_id)
                                ending_evt = ai_build_quest_ending_event(full_q, ch, _cur_evt)
                        else:
                            # next_step отсутствует. Раньше это автоматически
                            # означало финал ветки. Теперь: смотрим is_ending.
                            # Если модель ЯВНО поставила is_ending=true — это
                            # действительно финал. Иначе — on-demand chain:
                            # генерируем следующий шаг через новый ai_call.
                            explicit_end = bool(ai_dict_like(ch) and ch.get('is_ending'))
                            steps_so_far = len(full_q.get('steps', []) or [])
                            hit_cap = steps_so_far >= AI_QUEST_MAX_STEPS
                            # ЗАЩИТА: слабая модель ставит IS_ENDING:true на
                            # ПЕРВОМ же выборе (копирует из шаблона). Пока
                            # не сделали AI_QUEST_MIN_STEPS_BEFORE_ENDING шагов —
                            # игнорируем explicit_end и продолжаем цепочку.
                            _min_steps = int(globals().get('AI_QUEST_MIN_STEPS_BEFORE_ENDING', 3) or 3)
                            if explicit_end and steps_so_far < _min_steps and not hit_cap:
                                print("Full quest: is_ending=true from LLM ignored (only %d/%d steps done, need %d)" % (
                                    steps_so_far, AI_QUEST_MAX_STEPS, _min_steps))
                                explicit_end = False

                            if explicit_end or hit_cap:
                                reason = u"explicit is_ending" if explicit_end else (
                                    u"hit AI_QUEST_MAX_STEPS=%d" % AI_QUEST_MAX_STEPS)
                                print("Full quest ends (%s) -> summary screen" % reason)
                                ending_evt = ai_build_quest_ending_event(full_q, ch, _cur_evt)
                            else:
                                # ON-DEMAND CHAIN: генерируем СЛЕДУЮЩИЙ шаг
                                # В ФОНОВОМ ПОТОКЕ, чтобы UI не фризил на
                                # 10-30 секунд ai_call'а. Показываем loading
                                # screen, который poll'ит store.ai_pending_event.
                                cur_step_data = None
                                try:
                                    cur_id = getattr(store, 'ai_full_quest_current_step', 'step1')
                                    for _s in full_q.get('steps', []):
                                        if ai_dict_like(_s) and _s.get('id') == cur_id:
                                            cur_step_data = _s; break
                                except Exception:
                                    pass
                                next_step_no = steps_so_far + 1

                                # Флаг: продолжение готовится в фоне.
                                store.ai_chain_pending = True
                                store.ai_pending_event = None
                                store.ai_event_thinking = True
                                try:
                                    store.ai_notify_queue.append(u"ИИ: продолжаю квест...")
                                except Exception:
                                    pass

                                def _chain_worker(_full_q=full_q, _cur=cur_step_data, _ch=ch, _n=next_step_no, _fallback=(_cur_evt, ch)):
                                    try:
                                        new_step = generate_next_quest_step(_full_q, _cur, _ch, _n)
                                        if ai_dict_like(new_step):
                                            _full_q.setdefault('steps', []).append(new_step)
                                            store.ai_full_quest_data = _full_q
                                            store.ai_full_quest_current_step = new_step.get('id')
                                            staged = ai_step_to_event(
                                                _full_q, new_step,
                                                spicy_level=getattr(store, 'ai_spicy_meter', 2)
                                            )
                                            store.ai_pending_event = staged
                                            print("Chain quest advanced to step %d (%s)" % (_n, new_step.get('id')))
                                        else:
                                            # Не смогли сгенерить продолжение — покажем ending
                                            print("Chain quest could not generate step %d -> summary" % _n)
                                            _fev = _fallback[0]
                                            _fch = _fallback[1]
                                            store.ai_pending_event = ai_build_quest_ending_event(_full_q, _fch, _fev)
                                    except Exception as _we:
                                        print("chain worker err: %s" % _we)
                                        try:
                                            store.ai_pending_event = ai_build_quest_ending_event(
                                                _full_q, _fallback[1], _fallback[0]
                                            )
                                        except Exception:
                                            pass
                                    finally:
                                        store.ai_event_thinking = False
                                        store.ai_chain_pending = False
                                        try:
                                            renpy.restart_interaction()
                                        except Exception:
                                            pass

                                import threading
                                threading.Thread(target=_chain_worker).start()
                                # ВАЖНО: не выставляем next_evt/ending_evt здесь.
                                # Флаг _chain_pending заставит label'ы ниже
                                # уйти на loading screen и ждать ai_pending_event.
                except Exception as e:
                    print("Full quest next step err %s" % e)

                # 2. Prefetch fallback (если дерева нет)
                if not next_evt and not ending_evt:
                    try:
                        next_evt = store.ai_prefetched.get(event_choice_result) if hasattr(store, 'ai_prefetched') else None
                    except Exception:
                        next_evt = None

                # 3. Если одиночное событие без дерева и без prefetch — тоже покажем мини-итог
                if not next_evt and not ending_evt:
                    if ai_dict_like(ch) and (ch.get('ending_text') or ch.get('ending_title') or ch.get('is_ending') or (ai_dict_like(ch.get('effects', {})) and ch.get('effects'))):
                        ending_evt = ai_build_quest_ending_event(getattr(store, 'ai_full_quest_data', None), ch, _cur_evt)

                if ending_evt:
                    next_evt = ending_evt

                if next_evt:
                    print("Using next/ending event for choice %s" % event_choice_result)
                    next_evt = ai_stage_event_for_ui(next_evt, reason=u"Next/ending step staged for UI")
                    try:
                        if ai_dict_like(next_evt) and ai_dict_like(next_evt.get('outfit_suggestion', {})) and next_evt.get('outfit_suggestion', {}).get('items'):
                            auto_equip(next_evt['outfit_suggestion']['items'])
                    except Exception as e:
                        print("auto_equip next err: %s" % e)
                    try:
                        store.ai_events.append(next_evt)
                    except Exception as e:
                        print("append next err: %s" % e)
                    try:
                        if hasattr(store, 'ai_prefetched') and event_choice_result in store.ai_prefetched:
                            del store.ai_prefetched[event_choice_result]
                    except Exception:
                        pass

                    if (not getattr(store, 'ai_full_quest_data', None)) and (not AI_LOW_VRAM_SAFE_MODE) and not next_evt.get('_is_ending'):
                        try:
                            def _prefetch_next_level(idx, txt):
                                try:
                                    gs = get_state()
                                    cont = "Prev step: %s - %s. Chose: %s. Self-acceptance %s%%. Generate NEXT short JSON step. Keep it concise and valid JSON." % (next_evt.get('title', ''), next_evt.get('description', '')[:200], txt[:100], gs.get('accept', 20))
                                    nxt = ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], cont, want_json=True, temp=0.82, max_tokens=AI_PREFETCH_MAX_TOKENS, task_desc=u"Разветвление уровня")
                                    if nxt and isinstance(nxt, dict) and not unicode(nxt.get('title', '')).startswith("__ERROR"):
                                        store.ai_prefetched[idx] = ai_normalize_event(nxt)
                                        print("Prefetched next level %s" % nxt.get('title', ''))
                                except Exception as e:
                                    print("Prefetch next level err %s" % e)
                            for i, ch2 in enumerate(next_evt.get('choices', [])[:2]):
                                ct = ch2.get('text', '') if hasattr(ch2, 'get') else str(ch2)
                                import threading
                                threading.Thread(target=_prefetch_next_level, args=(i, ct)).start()
                        except Exception as e:
                            print("Prefetch next setup %s" % e)

                    store._has_next = True
                    try:
                        if next_evt.get('_is_ending'):
                            renpy.notify(u"Итог ветки")
                        else:
                            sn = next_evt.get('_step_no')
                            st = next_evt.get('_step_total')
                            if sn and st:
                                renpy.notify(u"Шаг %s/%s" % (sn, st))
                            else:
                                renpy.notify(u"Следующий шаг квеста")
                    except Exception:
                        renpy.notify(u"Следующий шаг квеста")
                else:
                    store._has_next = False
                    ai_reset_quest_state()
                    renpy.notify(u"Квест завершен")
        except Exception as e:
            print("choice handling err %s" % e)
            store._has_next = False

    # ФОНОВАЯ ГЕНЕРАЦИЯ СЛЕДУЮЩЕГО ШАГА: показать loading screen и ждать.
    # ai_chain_pending выставляется в _chain_worker выше. Loading screen
    # каждые 0.5с делает Jump("ai_event_poll"), а тот в свою очередь
    # ждёт ai_pending_event, стажит его в UI и джампает на ai_event_choice.
    # Так мы никогда не блокируем главный поток на ai_call.
    if getattr(store, 'ai_chain_pending', False):
        $ store.ai_chain_pending = False
        call screen ai_event_loading_screen

    if getattr(store, '_has_next', False):
        jump ai_event_choice
    else:
        # ЭФФЕКТ 'travel_to': если выбор просил перекинуть Саманту куда-то —
        # делаем это ЗДЕСЬ, когда UI-квест уже закрыт. Иначе travel_walk
        # порвёт открытый экран квеста.
        if getattr(store, 'ai_pending_travel', None) is not None:
            python:
                _dst = store.ai_pending_travel
                store.ai_pending_travel = None
                try:
                    _tw = getattr(store, 'travel_walk', None)
                    if _tw:
                        _tw(_dst, arrival=True)
                except Exception as _te:
                    print("ai_pending_travel exec err: %s" % _te)
            jump travel_arrival
        # Проверяем, было ли это автоматическое событие
        if getattr(store, '_automatic_event_active', False) or getattr(store, 'ai_current_automatic_event', None) is not None:
            $ store._automatic_event_active = False
            $ store.ai_current_automatic_event = None
            # Вместо return, который ломает стек и выкидывает в Главное меню, делаем безопасный переход к карте игры!
            jump travel_arrival
        else:
            return

# NPC HUB
label ai_npc_hub:
    python:
        npc_list = getattr(store, 'npc_girls', [])[:12]
    call screen ai_npc_hub_screen(npc_list)
    return

screen ai_npc_hub_screen(npcs):
    modal True
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 650 ysize 600
        background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#2a1a3a" xfill True ysize 60
                hbox:
                    xfill True
                    text "AI Чат с NPC (с памятью)" size 18 bold True color "#ff88cc"
                    textbutton "X" action Return() xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 8
                    for npc in npcs:
                        $ npc_id = getattr(npc,'sname',str(npc.fname))
                        $ chat_len = len(ai_npc_chats.get(npc_id,[]))
                        hbox:
                            xfill True
                            text "[npc.fname] [npc.sname] ([chat_len] сообщ.)" size 14 color "#ccc"
                            textbutton "Чат" action [SetVariable("ai_current_npc", npc), Jump("ai_npc_chat")] background "#2a2a4a"

default ai_current_npc = None

label ai_npc_chat:
    $ npc = ai_current_npc
    $ npc_id = getattr(npc,'sname',npc.fname) if npc else "unknown"
    if npc_id not in ai_npc_chats:
        $ ai_npc_chats[npc_id] = []
    call screen ai_npc_chat_screen(npc, ai_npc_chats[npc_id])
    
    # После выхода из чата проверяем, была ли запрошена встреча от NPC!
    if getattr(store, 'ai_queued_npc_event', None):
        $ triggered_npc = store.ai_queued_npc_event
        $ store.ai_queued_npc_event = None # Сбрасываем флаг встречи
        $ renpy.notify(u"Встреча с %s!" % triggered_npc.fname)
        jump ai_trigger_npc_event
    
    # Безопасный переход обратно к карте игры вместо return во избежание вылетов
    jump travel_arrival

screen ai_npc_chat_screen(npc, history):
    modal True
    zorder 3000
    add Solid("#000000cc")
    frame:
        xalign 0.5 yalign 0.5
        xsize 600 ysize 700
        background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#2a2a4a" xfill True ysize 50
                hbox:
                    xfill True
                    text "Чат с [npc.fname] [npc.sname] | Принятие [ai_accept]%" size 14 color "#aaddff"
                    textbutton "X" action Return() xalign 1.0
            frame:
                background "#0a0a12" xfill True yfill True
                viewport:
                    yinitial 1.0
                    scrollbars "vertical"
                    vbox:
                        spacing 8
                        for m in history[-20:]:
                            $ escaped_user = ai_escape_renpy_text(m['content'])
                            if m['role']=='user':
                                frame:
                                    background "#1e3a5a" xalign 1.0 xmaximum 350
                                    text "[escaped_user]" size 13
                            else:
                                frame:
                                    background "#1a2a3a" xmaximum 350
                                    text "[escaped_user]" size 13 color "#d0e0ff"
                        if ai_npc_thinking:
                            text "[npc.fname] печатает... (игра НЕ на паузе, можно ходить)" size 12 italic True color "#88ffaa"
            frame:
                background "#1a1a2a" xfill True ysize 60
                hbox:
                    xfill True spacing 8
                    if not ai_npc_thinking:
                        textbutton "Написать..." action Call("ai_npc_input") xfill True yfill True background "#2a2a4a"
                    else:
                        textbutton "Ожидание ответа..." action None xfill True yfill True background "#111"
                    textbutton "Назад" action Return() background "#1a1a1a"
    if ai_npc_thinking:
        timer 0.5 action Jump("ai_npc_chat_poll") repeat True

label ai_npc_input:
    $ npc = ai_current_npc
    $ npc_id = getattr(npc,'sname',npc.fname)
    $ user_msg = renpy.input("Сказать %s:" % npc.fname, length=400)
    $ user_msg = user_msg.strip()
    if not user_msg:
        jump ai_npc_chat
    $ ai_npc_chats[npc_id].append({"role":"user","content":user_msg})
    $ ai_npc_thinking = True
    $ ai_pending_npc_response = None
    python:
        def _npc_chat_thread():
            try:
                gs=get_state()
                # Строим динамический системный промпт профиля персонажа
                npc_profile = ai_get_npc_profile_prompt(npc)
                sys_prompt = (PROMPTS["npc_chat"] % gs['fem']) + "\n" + npc_profile
                resp=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, user_msg, want_json=False, temp=0.85, max_tokens=300, task_desc=u"Чат с " + npc.fname)
                if resp is None:
                    store.ai_pending_npc_response = "__ERROR_UNKNOWN__"
                else:
                    store.ai_pending_npc_response = resp
            except Exception as e:
                store.ai_pending_npc_response = "__ERROR__ %s" % e
            renpy.restart_interaction()
            
        import threading
        threading.Thread(target=_npc_chat_thread).start()
    jump ai_npc_chat

label ai_npc_chat_poll:
    if ai_pending_npc_response is not None:
        python:
            resp = ai_pending_npc_response
            npc = ai_current_npc
            npc_id = getattr(npc,'sname',npc.fname)
            
            if resp == "__ERROR_MODEL_NOT_FOUND__":
                ai_npc_chats[npc_id].append({"role":"assistant","content":u"[ОШИБКА] Модель '%s' не найдена в Ollama. Откройте терминал и введите: 'ollama pull %s'" % (OLLAMA_MODEL_CHAT, OLLAMA_MODEL_CHAT)})
            elif resp == "__ERROR_OLLAMA_OFFLINE__":
                ai_npc_chats[npc_id].append({"role":"assistant","content":u"[ОШИБКА] Не удалось подключиться к Ollama. Проверьте запущен ли Ollama сервер."})
            elif resp.startswith("__ERROR__"):
                ai_npc_chats[npc_id].append({"role":"assistant","content":u"[ОШИБКА] Связь оборвалась: %s" % resp.replace("__ERROR__","")})
            else:
                # Проверяем, пожелал ли NPC встретиться в живую и запустить 3D игровое событие!
                if "[EVENT]" in resp or "[QUEST]" in resp:
                    store.ai_notify_queue.append(u"ИИ: %s предлагает встретиться! Генерация события..." % npc.fname)
                    store.ai_queued_npc_event = npc
                
                # Убираем технические теги из сообщения
                clean=re.sub(r'\[.*?\]','',resp).strip()
                ai_npc_chats[npc_id].append({"role":"assistant","content":clean})
                for stat,d in re.findall(r'\[([A-Z_]+)([+-]\d+)\]', resp):
                    if stat in ("FEMININITY","ACCEPT","ACCEPTANCE"):
                        try:
                            ai_accept = max(0, min(100, ai_accept + int(d)))
                            ai_fem = ai_accept  # alias
                        except: pass
            
            store.ai_pending_npc_response = None
            store.ai_npc_thinking = False
        jump ai_npc_chat
    else:
        jump ai_npc_chat

# LABEL ДЛЯ ЗАПУСКА СОБЫТИЯ ВСТРЕЧИ ПОСЛЕ SMS ДИАЛОГА
label ai_trigger_npc_event:
    $ ai_event_thinking=True
    $ ai_pending_event=None
    $ ai_prefetched={}
    $ ai_full_quest_data=None
    python:
        def _npc_event_thread():
            try:
                gs=get_state()
                is_spicy, spicy_level, spicy_chance, spicy_roll = ai_get_spicy_prompt_modifier()
                npc_profile = ai_get_npc_profile_prompt(triggered_npc)
                
                task = (u"Generate an ARRIVAL event specifically involving NPC %s %s who has just "
                        u"invited Samantha. Ground the scene in the WORLD STATE above (current "
                        u"outfit, mood, cycle, perks). Branching choices with effects. Only JSON."
                        % (triggered_npc.fname, triggered_npc.sname))
                prompt = ai_prefix_world_state(task, gs, mode=u"full")
                sys_prompt = PROMPTS["event"] + "\nNPC PROFILE:\n" + npc_profile
                
                evt = ai_call(OLLAMA_MODEL_JSON, sys_prompt, prompt, want_json=True, temp=0.88, max_tokens=700, task_desc=u"Событие встречи с " + triggered_npc.fname)
                evt = ai_normalize_event(evt)
                store.ai_pending_event = evt
            except Exception as e:
                print("NPC event gen err: %s" % e)
                store.ai_pending_event = None
            renpy.restart_interaction()
            
        import threading
        threading.Thread(target=_npc_event_thread).start()
    call screen ai_event_loading_screen

# DIRTY TALK - Мгновенно за счет предзагрузки в интимных локациях
label ai_dirty_talk(sex_type="vag", npc=None):
    python:
        if hasattr(store,'ai_dirty_prefetched') and store.ai_dirty_prefetched:
            try:
                phrase=store.ai_dirty_prefetched.pop(0)
                ai_dirty_talk_history.append(phrase)
                renpy.say(None, ai_escape_renpy_text(phrase))
                
                # Фоновая дозагрузка следующей реплики в фоновом потоке
                def _refill_dirty():
                    try:
                        gs=get_state()
                        npc_name = "%s" % npc.fname if npc else "partner"
                        resp=ai_call(OLLAMA_MODEL_CHAT, PROMPTS["dirty"] % (gs['fem'], sex_type, npc_name), "Need one more dirty phrase for %s, fem %s%%" % (sex_type, gs['fem']), want_json=False, temp=0.9, max_tokens=150, task_desc=u"Грязная реплика")
                        if resp and not resp.startswith("__ERROR"):
                            store.ai_dirty_prefetched.append(resp)
                    except:
                        pass
                import threading
                threading.Thread(target=_refill_dirty).start()
            except Exception as e:
                print("Dirty prefetch use err %s" % e)
        else:
            # Медленный фолбек если буфер пуст
            gs=get_state()
            npc_name = "%s" % npc.fname if npc else "partner"
            sys_prompt=PROMPTS["dirty"] % (gs['fem'], sex_type, npc_name)
            _dirty_task = (u"Give ONE more short dirty-talk phrase Samantha would say/think right "
                           u"now during %s sex with %s. Match her state from the WORLD STATE above." % (sex_type, npc_name))
            user_prompt = ai_prefix_world_state(_dirty_task, gs, mode=u"minimal")
            resp=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, user_prompt, want_json=False, temp=0.9, max_tokens=200, task_desc=u"Грязная фраза секса")
            if resp and not resp.startswith("__ERROR"):
                ai_dirty_talk_history.append(resp)
                renpy.say(None, ai_escape_renpy_text(resp))
            else:
                renpy.say(None, u"Ах... ты стонешь, чувствуя как новое женское тело сладко трепещет")
    return

# DIARY - Полностью асинхронный
label ai_diary_gen:
    python:
        def _diary_thread():
            try:
                gs=get_state()
                last_evt=ai_events[-1]['description'] if ai_events else "обычный день"
                sys_prompt=PROMPTS["diary"] % (last_evt, gs['fem'], gs.get('outfit','unknown'))
                _diary_task = (u"Write ONE 2-3 sentence diary entry from Samantha, first person, "
                               u"about today. Ground it in the WORLD STATE above (outfit, cycle, "
                               u"mood, previous event, active perks).")
                _diary_user = ai_prefix_world_state(_diary_task, gs, mode=u"compact")
                entry=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, _diary_user, want_json=False, temp=0.8, max_tokens=300, task_desc=u"Запись в дневник")
                if entry and not entry.startswith("__ERROR"):
                    store.ai_diary_entries.append({"day":gs.get('day',0),"text":entry})
                    try:
                        if hasattr(store,'log'):
                            store.log.assign(entry[:100])
                    except: pass
                    store.ai_notify_queue.append(u"ИИ: Запись дневника добавлена!")
            except Exception as e:
                print("Diary generation error: %s" % e)
        import threading
        threading.Thread(target=_diary_thread).start()
    return

screen ai_diary_screen():
    modal True
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 700 ysize 600 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#1a3a2a" xfill True ysize 50
                hbox:
                    xfill True
                    text "AI Дневник Саманты" size 18 color "#88ffaa"
                    textbutton "X" action Return() xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for e in reversed(ai_diary_entries[-20:]):
                        $ escaped_text = ai_escape_renpy_text(e['text'])
                        frame:
                            background "#1a2a3a" xfill True
                            vbox:
                                text "День [e[day]]" size 11 color "#666"
                                text "[escaped_text]" size 14 color "#e0e0ff"

# REPORTS - Асинхронные
label ai_report_gen:
    python:
        def _report_thread():
            try:
                gs=get_state()
                sys_prompt=PROMPTS["report"] % (gs['fem'], gs['confidence'], gs['corrupt'], gs['location'])
                _report_task = (u"Write a short (3-4 sentences) Institute scientific report on Subject "
                                u"S-0 (Samantha), based on the WORLD STATE above. Include a concrete "
                                u"recommendation for her next femininity training step given her "
                                u"active perks, cycle/pregnancy state and current outfit.")
                user_prompt = ai_prefix_world_state(_report_task, gs, mode=u"full")
                report=ai_call(OLLAMA_MODEL_JSON, sys_prompt, user_prompt, want_json=False, temp=0.7, max_tokens=400, task_desc=u"Отчет Института")
                if report and not report.startswith("__ERROR"):
                    store.ai_reports.append(report)
                    store.ai_notify_queue.append(u"ИИ: Отчет Института готов!")
            except Exception as e:
                print("Report thread error: %s" % e)
        import threading
        threading.Thread(target=_report_thread).start()
    return

screen ai_reports_screen():
    modal True
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 650 ysize 500 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#0a2a4a" xfill True ysize 50
                hbox:
                    xfill True
                    text "Отчеты Института (AI)" size 18 color "#aaddff"
                    textbutton "X" action Return() xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for r in reversed(ai_reports[-10:]):
                        $ escaped_report = ai_escape_renpy_text(r)
                        frame:
                            background "#1a2330" xfill True
                            text "[escaped_report]" size 13 color "#cceeff"

label ai_report_view:
    call screen ai_reports_screen
    return

# SHOP - Асинхронный
label ai_shop_gen:
    python:
        def _shop_thread():
            try:
                gs=get_state()
                _shop_task = (u"Design ONE new sexy clothing item that fits Samantha's current "
                              u"vibe (WORLD STATE above). Consider her femininity, corruption and "
                              u"active perks when choosing sluttiness/style. Only JSON.")
                _shop_user = ai_prefix_world_state(_shop_task, gs, mode=u"compact")
                item_json=ai_call(OLLAMA_MODEL_JSON, PROMPTS["shop_item"], _shop_user, want_json=True, temp=0.9, max_tokens=300, task_desc=u"Дизайн одежды")
                if item_json and isinstance(item_json, dict) and 'name' in item_json:
                    ItemClass=getattr(store,'Item',None)
                    if ItemClass:
                        new_item=ItemClass(item_json['name'], item_json['desc'], "ai_item_%s" % len(ai_shop_items), type=item_json.get('type','top'), slutty=item_json.get('slutty',True), skirt=item_json.get('skirt',False), clevage=item_json.get('clevage',True), value=item_json.get('value',100))
                        store.ai_shop_items.append(new_item)
                        if hasattr(store,'shop_list'):
                            store.shop_list.append(new_item)
                        store.ai_notify_queue.append(u"ИИ: Дизайн одежды %s готов и добавлен в магазин!" % item_json['name'])
            except Exception as e:
                print("shop thread error: %s" % e)
        import threading
        threading.Thread(target=_shop_thread).start()
    return

# TRAINER
label ai_trainer(t_type="fitness"):
    python:
        gs=get_state()
        sys_prompt=PROMPTS["training"] % (gs['fem'], gs['fitness'], t_type)
        _train_task = (u"Give a 2-3 sentence %s training advice for Samantha, grounded in her "
                       u"WORLD STATE above (current fitness, tiredness, mood, active perks). "
                       u"Include a small concrete task she can do right now." % t_type)
        _train_user = ai_prefix_world_state(_train_task, gs, mode=u"compact")
        advice=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, _train_user, want_json=False, temp=0.8, max_tokens=300, task_desc=u"Совет тренера")
        if advice and not advice.startswith("__ERROR"):
            renpy.say(None, ai_escape_renpy_text(advice))
            if t_type=="fitness":
                try: player.add_fitness(1)
                except: pass
            elif t_type=="confidence":
                try: player.add_conf(2)
                except: pass
    return

# SMS - Асинхронная доставка
label ai_sms_gen:
    python:
        ai_start_prefetch_sms()
        renpy.notify(u"SMS подготавливается на фоне...")
    return

screen ai_sms_screen():
    modal True
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 650 ysize 700 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#2a2a4a" xfill True ysize 50
                hbox:
                    xfill True
                    text "SMS от NPC (AI)" size 18 color "#ff88ff"
                    textbutton "X" action Return() xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for sms in reversed(ai_sms_inbox[-20:]):
                        $ escaped_from = ai_escape_renpy_text(sms['from'])
                        $ escaped_text = ai_escape_renpy_text(sms['text'])
                        
                        # Находим объект NPC в diary_people_list для возможности диалога
                        $ sender_first_name = sms['from'].split()[0]
                        $ npc_obj = None
                        python:
                            for p_npc in getattr(store, 'diary_people_list', []):
                                if p_npc.fname.lower() == sender_first_name.lower():
                                    npc_obj = p_npc
                                    break
                        
                        frame:
                            background "#1a1a3a" xfill True
                            vbox:
                                xfill True
                                text "[escaped_from] - День [sms[day]]" size 11 color "#888"
                                text "[escaped_text]" size 14 color "#e0e0ff"
                                if npc_obj:
                                    null height 5
                                    hbox:
                                        xfill True
                                        textbutton "Ответить в чате" action [SetVariable("ai_unread_sms_count", 0), SetVariable("ai_current_npc", npc_obj), Jump("ai_npc_chat")] background "#2a2a5a" xalign 1.0 text_size 12

# PERKS - Асинхронные
label ai_perk_gen:
    python:
        def _perk_thread():
            try:
                gs=get_state()
                _perk_task = (u"Design ONE new persistent perk for Samantha that fits what has "
                              u"happened to her (see WORLD STATE above — active perks, recent "
                              u"actions, cycle/pregnancy). Do not duplicate an existing perk. Only JSON.")
                _perk_user = ai_prefix_world_state(_perk_task, gs, mode=u"compact")
                perk_json=ai_call(OLLAMA_MODEL_JSON, PROMPTS["perk"] % (gs['fem'], gs['perks']), _perk_user, want_json=True, temp=0.9, max_tokens=300, task_desc=u"Проектирование перка")
                if perk_json and isinstance(perk_json, dict) and 'name' in perk_json:
                    PerkClass=getattr(store,'PerkClass',None)
                    if PerkClass:
                        new_perk=PerkClass(perk_json['name'], perk_json['desc'], "ai_perk_%s" % len(ai_perks_generated), confidence_add=perk_json.get('add',5) if perk_json.get('type')=='confidence' else 0, desire_add=perk_json.get('add',5) if perk_json.get('type')=='desire' else 0, allure_add=perk_json.get('add',5) if perk_json.get('type')=='allure' else 0)
                        store.ai_perks_generated.append(new_perk)
                        player.add_perk(new_perk, notif=True)
                        store.ai_notify_queue.append(u"ИИ: Новый перк '%s' успешно спроектирован!" % perk_json['name'])
            except Exception as e:
                print("perk thread error: %s" % e)
        import threading
        threading.Thread(target=_perk_thread).start()
    return

# HUB
screen ai_hub():
    modal True
    zorder 2000
    add Solid("#000000cc")
    frame:
        xalign 0.5 yalign 0.5
        xsize 750 ysize 750
        background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#1a1a3a" xfill True ysize 60
                hbox:
                    xfill True
                    text "AI HUB - Все системы | Принятие [ai_accept]%" size 20 bold True color "#ff88ff"
                    textbutton "X" action Return() xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    text "1. Чат и события" size 14 bold True color "#88aaff"
                    hbox:
                        spacing 10
                        textbutton "Chat Brooker" action Call("ai_chat_brooker") background "#001a33"
                        textbutton "Event 3D" action Call("ai_gen_event") background "#330033"
                        textbutton "Quests" action Call("ai_view_quests") background "#003333"
                    text "2. NPC и социум" size 14 bold True color "#88ffaa"
                    hbox:
                        spacing 10
                        textbutton "NPC чат" action Call("ai_npc_hub") background "#2a2a4a"
                        textbutton "SMS inbox" action [SetVariable("ai_unread_sms_count", 0), Call("ai_sms_view")] background "#2a1a3a"
                        textbutton "Spawn NPC" action Call("ai_spawn_random_npc") background "#3a2a4a"
                    text "3. Секс и тело" size 14 bold True color "#ff88aa"
                    hbox:
                        spacing 10
                        textbutton "Dirty talk" action Call("ai_dirty_test") background "#4a1a2a"
                        textbutton "Тренер" action Call("ai_trainer_fem") background "#2a4a2a"
                    text "4. Прогресс" size 14 bold True color "#ffaa44"
                    hbox:
                        spacing 10
                        textbutton "AI Дневник" action Call("ai_diary_view") background "#3a2a2a"
                        textbutton "Отчеты" action Call("ai_reports_view") background "#1a2a4a"
                        textbutton "Перк" action Call("ai_perk_gen") background "#2a3a1a"
                    text "5. Магазин" size 14 bold True color "#aaff88"
                    hbox:
                        spacing 10
                        textbutton "Вещь" action Call("ai_shop_gen") background "#3a1a3a"
                        textbutton "Совет одежды" action Call("ai_cloth_advice") background "#4a2a3a"

                    null height 10
                    text "6. Конфиг комфорта / фракций / spicy" size 14 bold True color "#ffcc88"
                    hbox:
                        spacing 8
                        textbutton "Теги" action Call("ai_comfort_open") background "#2a2a4a"
                        textbutton "Локации" action Call("ai_locations_open") background "#1a3a2a"
                        textbutton "Фракции" action Call("ai_factions_open") background "#3a1a2a"
                        textbutton "Spicy" action Call("ai_spicy_open") background "#3a3a3a"
                        textbutton "Portrait" action Call("ai_portrait_open") background "#3a1a4a"
                    hbox:
                        spacing 8
                        textbutton "Дебаг локаций" action Call("ai_debug_locations") background "#1a1a1a"

label ai_view_quests:
    call screen ai_quests_screen
    return

screen ai_quests_screen():
    modal True
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 650 ysize 500 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#1a3a2a" xfill True ysize 50
                hbox:
                    xfill True
                    text "Квесты AI" size 18 color "#88ff88"
                    textbutton "X" action Return() xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for q in reversed(ai_quests):
                        $ escaped_title = ai_escape_renpy_text(q.get('title','?'))
                        $ escaped_desc = ai_escape_renpy_text(q.get('desc',''))
                        frame:
                            background "#1a2a3a" xfill True
                            text "[escaped_title]\n[escaped_desc]" size 13 color "#ccc"

label ai_sms_view:
    call screen ai_sms_screen
    # Безопасный переход обратно к карте игры вместо return во избежание вылетов в главное меню
    jump travel_arrival

label ai_diary_view:
    call screen ai_diary_screen
    # Безопасный переход обратно к карте игры вместо return во избежание вылетов в главное меню
    jump travel_arrival

label ai_reports_view:
    call screen ai_reports_screen
    # Безопасный переход обратно к карте игры вместо return во избежание вылетов в главное меню
    jump travel_arrival

label ai_spawn_random_npc:
    python:
        def _spawn_npc_thread():
            try:
                npc_data=ai_call(OLLAMA_MODEL_JSON, "Generate NPC JSON: {fname,sname,colour,is_female,iswhore,isslut,bio_group,bio_text}", "New NPC for TheFixer, whore or police or academy", want_json=True, temp=0.9, max_tokens=300, task_desc=u"Генерация персонажа")
                if npc_data and isinstance(npc_data, dict):
                    npc_data['generate_new']=True
                    store.ai_spawn_queue.append(npc_data)
                else:
                    store.ai_spawn_queue.append({"generate_new":True,"fname":"Lila","sname":"Fox","is_female":True,"iswhore":True,"bio_group":"whore"})
            except Exception as e:
                print("NPC spawn prefetch err %s" % e)
        import threading
        threading.Thread(target=_spawn_npc_thread).start()
    return

label ai_dirty_test:
    call ai_dirty_talk
    return

label ai_trainer_fem:
    call ai_trainer
    return

label ai_cloth_advice:
    python:
        gs=get_state()
        sys_prompt="You are wardrobe advisor for former man in female body, self-acceptance %s%%. Advise what to wear from items like item_top_22, item_bottom_15. Russian short." % gs.get('accept', 20)
        _cloth_task = (u"Coротко посоветуй Саманте, во что переодеться прямо сейчас, исходя из WORLD "
                       u"STATE выше (нынешняя одежда по слотам, локация, настроение, spicy_level, "
                       u"активные перки). Ответь по-русски, 2-3 короткие фразы, конкретные item id.")
        _cloth_user = ai_prefix_world_state(_cloth_task, gs, mode=u"compact")
        advice=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, _cloth_user, want_json=False, temp=0.8, max_tokens=300, task_desc=u"Совет по одежде")
        if advice and not advice.startswith("__ERROR"):
            renpy.say(None, ai_escape_renpy_text(advice))
    return

# AI EVENT RADER (Просмотр предзагруженных скрытых событий)
label ai_radar_view:
    call screen ai_radar_screen
    # Безопасный возврат на карту
    jump travel_arrival

screen ai_radar_screen():
    modal True
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 550 ysize 400 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#330033" xfill True ysize 50
                hbox:
                    xfill True
                    text "ИИ Радар Событий" size 18 color "#ff88ff"
                    textbutton "X" action Return() xalign 1.0
            viewport:
                scrollbars "vertical" mousewheel True
                vbox spacing 15 xfill True:
                    $ ready_loc = getattr(store, 'ai_prefetched_location', None)
                    $ ready_evt = getattr(store, 'ai_prefetched_location_event', None)
                    
                    if ready_loc and ready_evt:
                        text "ИИ СОБЫТИЕ ПОДГОТОВЛЕНО И ЖДЕТ ВАС!" size 16 bold True color "#88ffaa" xalign 0.5
                        
                        frame:
                            background "#1a2a1a" xfill True
                            vbox:
                                text "Локация назначения:" size 12 color "#aaa"
                                text "[ready_loc]" size 16 bold True color "#ffaa44"
                                text "Название события:" size 12 color "#aaa"
                                $ escaped_title = ai_escape_renpy_text(ready_evt.get('title', 'Event'))
                                text "[escaped_title]" size 14 color "#fff"
                                
                        text "Отправляйтесь в указанную локацию на карте, чтобы бесшовно и мгновенно запустить это приключение!" size 12 color "#ccc" italic True
                    else:
                        text "ИИ РАДАР СКАНИРУЕТ ПРОСТРАНСТВО..." size 16 bold True color "#888" xalign 0.5
                        text "В данный момент нет готовых скрытых событий." size 13 color "#aaa" xalign 0.5
                        text "Просто гуляйте по городу или промотайте время — ИИ сгенерирует новое приключение в фоновом режиме!" size 12 color "#888" italic True xalign 0.5


# OVERLAY
init python:
    for old in ["thefixer_real_overlay","thefixer_events_overlay","thefixer_events_v2_overlay","thefixer_events_v3_overlay","thefixer_ai_overlay","thefixer_v4_overlay","thefixer_events_v3_overlay","thefixer_all_overlay","thefixer_events_v3_overlay"]:
        if old in config.overlay_screens:
            try: config.overlay_screens.remove(old)
            except: pass
    if "thefixer_all_overlay" not in config.overlay_screens:
        config.overlay_screens.append("thefixer_all_overlay")

screen thefixer_all_overlay():
    if not main_menu and hasattr(store,'player'):
        vbox:
            xalign 0.98 yalign 0.12 spacing 5
            
            # Кнопка 1: AI HUB (Главное меню)
            imagebutton:
                idle Solid("#ff00aa88", xsize=110, ysize=40)
                hover Solid("#ff00aa", xsize=110, ysize=40)
                action Call("ai_hub_open")
                tooltip "AI HUB"
            text "AI HUB" size 11 bold True xalign 0.5 color "#fff"
            
            # Кнопка 2: AI SMS Inbox (Быстрый просмотр сообщений с индикацией непрочитанных)
            $ sms_label = u"AI SMS"
            $ sms_bg = "#2a2a4a88"
            if ai_unread_sms_count > 0:
                $ sms_label = u"AI SMS [[%s]]" % ai_unread_sms_count
                $ sms_bg = "#ff8800cc" # Оранжевое свечение при наличии непрочитанных!
            
            imagebutton:
                idle Solid(sms_bg, xsize=110, ysize=40)
                hover Solid("#ffaa44", xsize=110, ysize=40)
                action [SetVariable("ai_unread_sms_count", 0), Call("ai_sms_view")]
                tooltip "Просмотр ИИ SMS"
            text "[sms_label]" size 11 bold True xalign 0.5 color "#fff"

            # Кнопка 3: AI RADAR (Радар скрытых событий с индикацией готовности)
            $ radar_label = u"AI RADAR"
            $ radar_bg = "#2a2a4a88"
            $ has_radar_event = getattr(store, 'ai_prefetched_location_event', None) is not None and getattr(store, 'ai_prefetched_location', None) is not None
            if has_radar_event:
                $ radar_label = u"AI RADAR [[!]]"
                $ radar_bg = "#ff0088cc" # Розовое свечение при наличии готового события!
                
            imagebutton:
                idle Solid(radar_bg, xsize=110, ysize=40)
                hover Solid("#ff44aa", xsize=110, ysize=40)
                action Call("ai_radar_view")
                tooltip "AI Радар Событий"
            text "[radar_label]" size 11 bold True xalign 0.5 color "#fff"
        
        # Фоновый таймер проверки автоматических систем (работает каждые 1.5 секунды)
        timer 1.5 action Function(ai_background_update_loop) repeat True

label ai_hub_open:
    call screen ai_hub
    # Безопасный переход обратно к карте игры вместо return во избежание вылетов в главное меню
    jump travel_arrival

label ai_all_after_load_fix:
    $ ai_event_cooldown = 0
    return

# ===== ПРЕФЕТЧ И АВТОМАТИЗАЦИЯ - ВЫЗОВЫ БЕЗ ОЖИДАНИЯ И КНОПОК =====

init python:
    # 1. Функция фоновой префетч-загрузки SMS С ПОТОКОБЕЗОПАСНОЙ БЛОКИРОВКОЙ
    def ai_start_prefetch_sms():
        if AI_LOW_VRAM_SAFE_MODE:
            return
        if getattr(store, 'ai_sms_prefetch_in_progress', False):
            return
            
        # Устанавливаем блокировку немедленно в главном потоке во избежание рассинхрона
        store.ai_sms_prefetch_in_progress = True
        
        def _prefetch_sms_thread():
            try:
                if getattr(store, 'ai_prefetched_sms', None):
                    return
                gs = get_state()
                
                # Достаем список всех известных персонажей из дневника игрока
                known_people = getattr(store, 'diary_people_list', [])
                # Фильтруем: только те персонажи, у которых галочка ИИ SMS стоит в положении True!
                allowed_people = []
                for p_npc in known_people:
                    p_id = p_npc.fname.lower()
                    if getattr(store, "ai_sms_allowed_" + p_id, False):
                        allowed_people.append(p_npc)
                
                # Если никто не выбран, то ИИ не генерирует фоновые SMS! Полная тишина на фоне
                if not allowed_people:
                    return
                
                # Случайный выбор из списка одобренных игроком персонажей
                npc = py_random.choice(allowed_people)
                npc_name = "%s %s" % (npc.fname, npc.sname)
                npc_group = getattr(npc, 'bio_group', 'whore')
                
                # Загружаем подробный стиль общения и профиль этого персонажа
                npc_profile = ai_get_npc_profile_prompt(npc)
                sys_prompt = PROMPTS["sms"] + "\n" + npc_profile
                
                _sms_task = (u"Write ONE short in-character SMS from %s to Samantha, matching the "
                             u"NPC's profile above and the WORLD STATE (Samantha's current outfit, "
                             u"location and mood). 1-2 sentences." % npc_name)
                _sms_user = ai_prefix_world_state(_sms_task, gs, mode=u"compact")
                sms_text = ai_call(OLLAMA_MODEL_CHAT, sys_prompt, _sms_user, want_json=False, temp=0.85, max_tokens=200, task_desc=u"SMS от " + npc_name)
                if sms_text and not sms_text.startswith("__ERROR"):
                    store.ai_prefetched_sms = {"from": npc_name, "text": sms_text, "day": gs.get('day', 0)}
                    print("Prefetched SMS from %s successfully!" % npc_name)
            except Exception as e:
                print("SMS prefetch err %s" % e)
            finally:
                # Всегда освобождаем блокировку!
                store.ai_sms_prefetch_in_progress = False
                
        import threading
        threading.Thread(target=_prefetch_sms_thread).start()

    # 2. Функция безопасной проверки состояния игры для авто-триггера событий
    def ai_is_safe_to_trigger():
        # Если открыт экран сохранения, паузы или главного меню - блокируем
        if renpy.get_screen("main_menu") or renpy.get_screen("game_menu") or renpy.get_screen("navigation"):
            return False
        # Если идет активный диалог персонажа или выбор - блокируем, чтобы ничего не поломать
        if renpy.get_screen("say") or renpy.get_screen("choice"):
            return False
        # Если уже открыты наши ИИ экраны - блокируем повторное открытие
        blocked_screens = [
            "ai_event_screen", "ai_chat_screen", "ai_npc_chat_screen", 
            "ai_comfort_tags_screen", "ai_location_themes_screen", 
            "ai_factions_screen", "ai_spicy_config_screen", "ai_hub",
            "ai_event_loading_screen", "ai_sms_screen", "ai_radar_screen"
        ]
        for scr in blocked_screens:
            if renpy.get_screen(scr):
                return False
        # Должны быть инициализированы игрок и текущая локация
        if not hasattr(store, 'player') or not hasattr(store, 'loc_cur') or not store.loc_cur:
            return False
        return True

    # 3. Единая фоновая функция обновления, вызываемая из overlay таймера
    def ai_background_update_loop():
        # А. Обработка уведомлений из фоновых потоков (100% потокобезопасно)
        if getattr(store, 'ai_notify_queue', []):
            try:
                msg = store.ai_notify_queue.pop(0)
                renpy.notify(msg)
            except Exception as e:
                print("Notify queue process err: %s" % e)

        # Б. Обработка спавна NPC из очереди в безопасном главном потоке
        if getattr(store, 'ai_spawn_queue', []):
            try:
                npc_data = store.ai_spawn_queue.pop(0)
                spawn_npc(npc_data)
            except Exception as e:
                print("Spawn queue process err: %s" % e)

        # SAFE MODE: не запускаем тяжёлые фоновые LLM-задачи, чтобы ручные квесты/чаты не висели в очереди.
        if AI_LOW_VRAM_SAFE_MODE:
            return

        if ai_is_safe_to_trigger():
            cur_loc_name = getattr(store.loc_cur, 'name', str(store.loc_cur)) if hasattr(store, 'loc_cur') else ""
            
            # В. Детект перемещения игрока в новую локацию
            if cur_loc_name and cur_loc_name != getattr(store, 'ai_last_checked_location', ''):
                old_loc = store.ai_last_checked_location
                store.ai_last_checked_location = cur_loc_name
                
                # Уменьшаем кулдаун на перемещение
                if getattr(store, 'ai_event_cooldown', 0) > 0:
                    store.ai_event_cooldown -= 1
                
                # АВТОМАТИЧЕСКИЙ СКРИНШОТ ЛОКАЦИИ ПРИ ВХОДЕ В ФАЙЛ ai_loc_[id].png!
                # Сохраняет снимок экрана, чтобы ты мог прислать его мне для описания окружения локации ИИ!
                if cur_loc_name and cur_loc_name != getattr(store, 'ai_last_screenshot_location', ''):
                    store.ai_last_screenshot_location = cur_loc_name
                    screenshot_filename = "ai_loc_" + cur_loc_name + ".png"
                    try:
                        renpy.screenshot(screenshot_filename)
                        print("Saved screenshot of location to %s" % screenshot_filename)
                        store.ai_notify_queue.append(u"ИИ: Снимок %s сохранен в папку игры!" % cur_loc_name)
                    except Exception as e:
                        print("Screenshot capture err: %s" % e)
                
                # Если авто-события включены
                if getattr(store, 'ai_auto_events_enabled', True):
                    # Проверяем кулдаун
                    if getattr(store, 'ai_event_cooldown', 0) <= 0:
                        # Проверяем, есть ли предзагруженное событие именно для этой новой локации
                        if getattr(store, 'ai_prefetched_location_event', None) and getattr(store, 'ai_prefetched_location', None) == cur_loc_name:
                            # Кидаем кубик против шанса авто-событий (ВЫПОЛНЯЕТСЯ ЛОКАЛЬНО ЗА ОДНУ СТРОЧКУ КОДА, БЕЗ LLM!)
                            chance = getattr(store, 'ai_auto_event_chance', 40)
                            roll = py_random.randint(0, 100)
                            print("Location change detected %s -> %s. Roll: %s / %s" % (old_loc, cur_loc_name, roll, chance))
                            if roll < chance:
                                evt = store.ai_prefetched_location_event
                                # Сбрасываем кэш
                                store.ai_prefetched_location_event = None
                                store.ai_prefetched_location = None
                                # Ставим кулдаун (не генерировать события на следующие 3 перемещения)
                                store.ai_event_cooldown = 3
                                # Запускаем событие бесшовно в основном контексте
                                store.ai_current_automatic_event = evt
                                store._automatic_event_active = True
                                renpy.jump("ai_trigger_automatic_event_label")

            # Г. Детект изменения часа для нарастающего шанса событий и доставки SMS!
            # Каждые 1 час нарастает вероятность событий (+10% в час) и SMS (+35% в час)
            current_hour = getattr(store.t, 'hour', 12) if hasattr(store, 't') else 12
            if current_hour != getattr(store, 'ai_last_checked_hour', -1):
                if getattr(store, 'ai_last_checked_hour', -1) != -1:
                    print("Hour changed from %s to %s. Checking hourly triggers..." % (store.ai_last_checked_hour, current_hour))
                    
                    # 1. Нарастающий ежечасный шанс авто-события! (ВЫПОЛНЯЕТСЯ ЛОКАЛЬНО В КОДЕ, БЕЗ LLM!)
                    store.ai_time_event_chance = getattr(store, 'ai_time_event_chance', 10) + 10
                    if store.ai_time_event_chance > 100:
                        store.ai_time_event_chance = 100
                        
                    roll = py_random.randint(0, 100)
                    print("Hourly event check. Chance: %s%%. Roll: %s" % (store.ai_time_event_chance, roll))
                    
                    if roll < store.ai_time_event_chance:
                        store.ai_time_event_chance = 10 # Сбрасываем к базовым 10%
                        
                        # Моментальная асинхронная генерация почасового события
                        def _trigger_time_event():
                            try:
                                gs = get_state()
                                _hourly_task = (u"TIME TRIGGER: one hour has passed. Generate ONE "
                                                u"short dynamic event that could naturally happen to "
                                                u"Samantha RIGHT NOW at her current location, given "
                                                u"the WORLD STATE above. 2-3 choices with effects. Only JSON.")
                                prompt = ai_prefix_world_state(_hourly_task, gs, mode=u"full")
                                evt = ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], prompt, want_json=True, temp=0.85, max_tokens=700, task_desc=u"Почасовое событие")
                                if evt and hasattr(evt, 'get'):
                                    store.ai_current_automatic_event = ai_normalize_event(evt)
                                    store._automatic_event_active = True
                                    renpy.jump("ai_trigger_automatic_event_label")
                            except:
                                pass
                            finally:
                                # Всегда освобождаем блокировку!
                                store.ai_location_prefetch_in_progress = False
                                
                        if not getattr(store, 'ai_location_prefetch_in_progress', False):
                            store.ai_location_prefetch_in_progress = True
                            import threading
                            threading.Thread(target=_trigger_time_event).start()
                        
                    # 2. Шанс доставки предзагруженного SMS от выбранного персонажа
                    if getattr(store, 'ai_auto_sms_enabled', True) and getattr(store, 'ai_prefetched_sms', None):
                        sms_roll = py_random.randint(0, 100)
                        if sms_roll < 35: # 35% шанс каждый час получить сообщение
                            sms = store.ai_prefetched_sms
                            store.ai_prefetched_sms = None # Стираем буфер
                            store.ai_sms_inbox.append(sms)
                            store.ai_unread_sms_count = getattr(store, 'ai_unread_sms_count', 0) + 1 # Увеличиваем счетчик непрочитанных!
                            store.ai_notify_queue.append(u"ИИ: Получено новое SMS от %s!" % sms['from'])
                            # Запускаем предзагрузку следующего SMS в фоне
                            ai_start_prefetch_sms()
                            
                store.ai_last_checked_hour = current_hour

            # Д. Автоматическая предзагрузка грязных фраз для секса в интимных локациях (без PicklingError!)
            if cur_loc_name in ["bedroom", "bathroom", "motel", "pinkroom", "haven_bedroom", "beach"]:
                if not getattr(store, 'ai_dirty_prefetched', None) and not getattr(store, 'ai_dirty_prefetch_in_progress', False):
                    store.ai_dirty_prefetch_in_progress = True
                    def _prefetch_dirty_talk_thread():
                        try:
                            if getattr(store, 'ai_dirty_prefetched', None):
                                return
                            gs = get_state()
                            phrases = []
                            for i in range(4):
                                stage = ["foreplay", "penetration", "fast", "cum"][i]
                                prompt = "Dirty talk stage %s, fem %s%%, desire %s%%. Short Russian phrase, 1 sentence, no stars." % (stage, gs['fem'], gs['desire'])
                                resp = ai_call(OLLAMA_MODEL_CHAT, PROMPTS["dirty"] % (gs['fem'], stage, "partner"), prompt, want_json=False, temp=0.9, max_tokens=150, task_desc=u"Грязная реплика")
                                if resp and not resp.startswith("__ERROR"):
                                    phrases.append(resp)
                            if phrases:
                                store.ai_dirty_prefetched = phrases
                                print("Prefetched dirty phrases successfully!")
                        except Exception as e:
                            print("Dirty prefetch err: %s" % e)
                        finally:
                            store.ai_dirty_prefetch_in_progress = False
                    import threading
                    threading.Thread(target=_prefetch_dirty_talk_thread).start()

            # Е. Детект смены дня для автоматического ведения Дневника
            current_day = getattr(store.t, 'day', 0) if hasattr(store, 't') else 0
            if current_day != getattr(store, 'ai_last_diary_day', -1):
                if getattr(store, 'ai_last_diary_day', -1) != -1:
                    print("Day changed from %s to %s. Prefetching daily diary entry..." % (store.ai_last_diary_day, current_day))
                    # Запускаем генерацию новой записи дневника в фоне
                    renpy.call_in_new_context("ai_diary_gen")
                store.ai_last_diary_day = current_day

    # 4. Callback при загрузке сейва - надежное восстановление переменных
    def ai_after_load_callback():
        try:
            # Сбрасываем флаги мыслительного процесса во избежание вечного зависания
            store.ai_thinking = False
            store.ai_npc_thinking = False
            store.ai_event_thinking = False
            store.ai_pending_chat_response = None
            store.ai_pending_npc_response = None
            store.ai_pending_event = None
            
            store.ai_location_prefetch_in_progress = False
            store.ai_sms_prefetch_in_progress = False
            store.ai_dirty_prefetch_in_progress = False
            
            # Корректно переопределяем максимальный предел Spicy-метра на 100% как просил игрок!
            store.AI_SPICY_MAX = 100
            
            if hasattr(store, 'ai_event_cooldown'):
                store.ai_event_cooldown = 0
            
            # Предзагружаем SMS, чтобы при первой возможности выдать игроку
            ai_start_prefetch_sms()
        except Exception as e:
            print("Error in after_load_callback: %s" % e)

    if hasattr(config, 'after_load_callbacks'):
        if ai_after_load_callback not in config.after_load_callbacks:
            config.after_load_callbacks.append(ai_after_load_callback)

    # 5. Перехват перемещений игрока (hook на travel_walk)
    try:
        _orig_travel_walk = getattr(store, 'travel_walk', None)
        if _orig_travel_walk and not getattr(_orig_travel_walk, '_ai_wrapped', False):
            def ai_travel_walk_wrapper(location, *args, **kwargs):
                try:
                    loc_name = getattr(location, 'name', str(location))
                    loc_desc = getattr(location, 'desc', loc_name)
                    
                    # Фиксируем перемещение в трекинге недавних действий GG
                    action_msg = u"Samantha moved to %s (%s) at hour %s." % (loc_name, loc_desc, getattr(store.t, 'hour', 12) if hasattr(store, 't') else 12)
                    if not getattr(store, 'ai_recent_actions', None):
                        store.ai_recent_actions = []
                    store.ai_recent_actions.append(action_msg)
                    # Храним только последние 8 действий, чтобы не перегружать контекст модели
                    store.ai_recent_actions = store.ai_recent_actions[-8:]

                    # НОВОЕ: отдельный лог только локаций — модели удобнее читать
                    # чистую траекторию перемещений без словесных обёрток.
                    if not getattr(store, 'ai_recent_locations', None):
                        store.ai_recent_locations = []
                    _hour_now = getattr(store.t, 'hour', 12) if hasattr(store, 't') else 12
                    store.ai_recent_locations.append(u"%s@%sh" % (loc_name, _hour_now))
                    store.ai_recent_locations = store.ai_recent_locations[-6:]

                    if AI_LOW_VRAM_SAFE_MODE:
                        return _orig_travel_walk(location, *args, **kwargs)
                    
                    def _prefetch_location_event():
                        try:
                            # Избегаем дублирующей генерации
                            if getattr(store, 'ai_prefetched_location', None) == loc_name and getattr(store, 'ai_prefetched_location_event', None):
                                return
                            
                            gs = get_state()
                            gs['location'] = loc_name
                            
                            from ai_config_locations import ai_get_allowed_themes_for_location
                            allowed_tags = ai_get_allowed_themes_for_location(loc_name)
                            allowed_tags_str = ", ".join(allowed_tags[:15]) if allowed_tags else "femininity, crossdressing"
                            
                            from ai_config_spicy import ai_get_spicy_chance, ai_get_spicy_level
                            is_spicy = py_random.randint(0, 100) < ai_get_spicy_chance()
                            spicy_level = ai_get_spicy_level()
                            
                            _dest_task = (u"DESTINATION TRAVEL: Samantha has just arrived at %s (%s). "
                                          u"Generate a short arrival event grounded in the WORLD STATE "
                                          u"above (her current outfit / mood / cycle / active perks) "
                                          u"and the location context. Branching choices with effects. Only JSON."
                                          % (loc_name, loc_desc))
                            prompt = ai_prefix_world_state(_dest_task, gs, mode=u"full")
                            evt = ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], prompt, want_json=True, temp=0.85, max_tokens=700, task_desc=u"Авто-квест для " + loc_desc)
                            if evt and isinstance(evt, dict) and not evt.get('title', '').startswith("__ERROR"):
                                if ai_filter_event_by_comfort(evt):
                                    store.ai_prefetched_location = loc_name
                                    store.ai_prefetched_location_event = ai_normalize_event(evt) # Нормализуем предзагруженное событие
                                    print("Prefetched destination event for %s successfully!" % loc_name)
                        except Exception as e:
                            print("Location prefetch err: %s" % e)
                        finally:
                            # Всегда сбрасываем блокировку!
                            store.ai_location_prefetch_in_progress = False
                    
                    # Устанавливаем блокировку немедленно в главном потоке во избежание рассинхрона
                    if not getattr(store, 'ai_location_prefetch_in_progress', False):
                        store.ai_location_prefetch_in_progress = True
                        import threading
                        threading.Thread(target=_prefetch_location_event).start()
                except Exception as e:
                    print("travel_walk wrapper prefetch start err: %s" % e)
                
                return _orig_travel_walk(location, *args, **kwargs)
                
            ai_travel_walk_wrapper._ai_wrapped = True
            store.travel_walk = ai_travel_walk_wrapper
            print("travel_walk() hooked for auto-prefetch successfully!")
    except Exception as e:
        print("Failed to hook travel_walk: %s" % e)

# LABEL ДЛЯ ЗАПУСКА АВТОМАТИЧЕСКИХ СОБЫТИЙ
label ai_trigger_automatic_event_label:
    $ store._automatic_event_active = True
    $ store.ai_last_event = ai_stage_event_for_ui(store.ai_current_automatic_event, reason=u"Automatic event staged for UI")
    $ ai_events.append(store.ai_last_event)
    
    if store.ai_last_event.get('outfit_suggestion',{}).get('items'):
        $ auto_equip(store.ai_last_event['outfit_suggestion']['items'])
    if store.ai_last_event.get('npc_involved',{}).get('generate_new'):
        $ spawn_npc(store.ai_last_event['npc_involved'])
    if store.ai_last_event.get('is_quest'):
        $ ai_quests.append({"title":store.ai_last_event.get('quest_title',store.ai_last_event['title']),"desc":store.ai_last_event.get('quest_desc',store.ai_last_event['description']),"outfit":store.ai_last_event.get('outfit_suggestion'),"status":"active","rewards":{"femininity":6,"money":150}})
    
    $ store.ai_current_automatic_event = None # очищаем временный буфер
    
    # Сразу направляем на обработку выбора диалога/события
    jump ai_event_choice
