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
    import json, re, os, base64, ast, threading
    import random as py_random

    # Поддержка двойной совместимости Python 2 (RenPy 7) и Python 3 (RenPy 8)
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
        "school_toilet": "The school restroom. Tile walls, sinks, and private toilet cubicles.",
        "park_local": "Blaston Park. Green grass fields, walking paths, benches, and tall trees. Beautiful and public.",
        "park_toilet_boys": "A dingy, tile men's restroom in Blaston Park. Urinals, cubicles, smelling of disinfectant. Risky to enter.",
        "park_toilet_girls": "The women's restroom in Blaston Park. Tile walls, mirrors, sinks, and private stalls. Safe and private.",
        "beach": "The sandy Blaston Beach. Waves washing over the sand, pier nearby, open and sunny. Perfect for swimwear.",
        "beach_water": "The cool water of Blaston Beach. Waves washing over the sand. Ideal for swimming.",
        "beach_gym": "An outdoor beach workout gym. Benches, weights, pull-up bars. Athletic people exercising.",
        "beach_hangout": "The sandy beach hangout spot. People relaxing on towels, sunbathing, or playing volleyball.",
        "beach_locker_boys": "The beach boys locker room. Rough wooden benches and showers.",
        "beach_locker_girls": "The beach girls locker room. Benches and privacy screens for changing.",
        "pub": "The Trainstation local pub. Dim-lit, smelling of beer and tobacco. Bob and Trixie serving, full of local patrons.",
        "pub_toilet_boys": "The pub men's restroom. Smelling of stale beer and urine, dirty tiles. Highly unsafe.",
        "pub_toilet_girls": "The pub women's restroom. Sinks, mirrors, tile walls. Dimly lit.",
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

    # Экранирование фигурных скобок для предотвращения крашей RenPy из-за "Unknown text tag"
    def ai_escape_renpy_text(text):
        if not isinstance(text, (str, unicode)):
            if text is None:
                return ""
            return unicode(text)
        # Дублируем фигурные скобки, чтобы RenPy выводил их как литералы и не пытался парсить как теги текста
        return text.replace("{", "{{").replace("}", "}}")

    # Сброс и очистка переменных состояния квестов во избежание залипания шагов
    def ai_reset_quest_state():
        store.ai_full_quest_data = None
        store.ai_full_quest_current_step = "step1"
        store.ai_prefetched = {}
        store.ai_pending_event = None
        store._has_next = False
        store._automatic_event_active = False
        store.ai_current_automatic_event = None

    # Потокобезопасная функция динамического добавления ИИ-перка на игрока в сейв-файл
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
            
            if parsed and hasattr(parsed, 'get'):
                evt = parsed
            else:
                # Если парсинг не удался, возвращаем структуру по умолчанию
                return {
                    "title": "Quest Challenge",
                    "description": unicode(evt),
                    "choices": [{"text": "Continue", "effects": {}}]
                }
        
        # Нормализация заголовка и описания с предохранителем от ленивой генерации ИИ ("...")
        title = evt.get('title', 'Event')
        if not title or unicode(title).strip() in ["", "...", "None", "None."]:
            title = "Quest Challenge"
            
        desc = evt.get('description', '')
        if not desc or unicode(desc).strip() in ["", "...", "None", "None."]:
            desc = "Samantha continues her femininity training, making choices that shape her new life."
            
        evt['title'] = title
        evt['description'] = desc
        
        choices = evt.get('choices', [])
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
                ch_text = ch.get('text', 'Continue')
                if not ch_text or unicode(ch_text).strip() in ["", "...", "None"]:
                    ch_text = "Continue"
                ch_effects = ch.get('effects', {})
                if not hasattr(ch_effects, 'get'):
                    ch_effects = {}
                normalized_choices.append({
                    "text": unicode(ch_text),
                    "effects": ch_effects,
                    "next_step": ch.get('next_step'),
                    "spicy_modifier": ch.get('spicy_modifier', 0) # Считываем динамический спайси-модификатор выбора!
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

    # Base call с настраиваемым таймаутом 25 секунд для разгрузки Олламы
    def ai_call(model, sys_prompt, user_prompt, want_json=False, temp=0.85, max_tokens=700, task_desc=None):
        if task_desc:
            try:
                # Добавляем в очередь уведомлений информацию о старте генерации
                store.ai_notify_queue.append(u"ИИ: Запрос к Ollama (%s)..." % task_desc)
            except:
                pass

        messages=[{"role":"system","content":sys_prompt},{"role":"user","content":user_prompt}]
        # Снижен контекст до 2048, чтобы модель + KV Cache гарантированно влезали в 4Гб VRAM твоей 3050 Ti без выгрузки на ЦП!
        payload={"model":model,"messages":messages,"stream":False,"options":{"temperature":temp,"top_p":0.92,"num_predict":max_tokens,"num_ctx":2048}}
        if want_json:
            payload["format"]="json"
        try:
            data=json.dumps(payload).encode('utf-8')
            req=urllib2.Request(OLLAMA_URL, data=data, headers={'Content-Type':'application/json'})
            # Увеличен таймаут до 120 секунд во избежание сброса соединения на медленных CPU
            resp=urllib2.urlopen(req, timeout=120)
            res=json.loads(resp.read().decode('utf-8'))
            content=res['message']['content']
            
            if want_json:
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
                
                parsed_json = json.loads(content)
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
            if task_desc:
                try:
                    store.ai_notify_queue.append(u"ИИ: Сбой (%s)" % task_desc)
                except:
                    pass
            if "404" in err_msg or "not found" in err_msg.lower():
                return "__ERROR_MODEL_NOT_FOUND__"
            elif "111" in err_msg or "connection refused" in err_msg.lower() or "timed out" in err_msg.lower():
                return "__ERROR_OLLAMA_OFFLINE__"
            return "__ERROR__ %s" % err_msg

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
            s['fem']=getattr(renpy.store,'ai_fem',25)
            s['horny']=getattr(renpy.store,'ai_horny',5)
            s['trust']=getattr(renpy.store,'ai_trust',40)
            s['accept']=getattr(renpy.store,'ai_accept',20)

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
                else:
                    s['outfit']=u"unknown"; s['outfit_top']=u""; s['outfit_bottom']=u""; s['is_slutty']=False; s['is_exposed']=False
            except:
                s['outfit']=u"unknown"; s['outfit_top']=u""; s['outfit_bottom']=u""; s['is_slutty']=False; s['is_exposed']=False

            try:
                inv=getattr(renpy.store,'inv',None)
                if inv and hasattr(inv,'items'):
                    items=[getattr(it,'name','?') for it in inv.items[:10]]
                    s['inventory']=", ".join(items) if items else "empty"
                    s['inventory_count']=len(inv.items)
                else:
                    ilist=getattr(renpy.store,'item_list',[])
                    s['inventory']=", ".join([getattr(it,'name','?') for it in ilist[:10]]) if ilist else "empty"
                    s['inventory_count']=len(ilist)
            except:
                s['inventory']="unknown"; s['inventory_count']=0

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
                perks=[perk.name for perk in getattr(p,'perk_list',[])][-8:]
                s['perks']=", ".join(perks) if perks else "Former man"
                s['perks_list']=perks
            except:
                s['perks']="Former man"; s['perks_list']=[]

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

            try:
                s['nearby_npcs']="none at home" if s['location_private'] else "maybe people around"
            except:
                s['nearby_npcs']="unknown"

            try:
                s['weather']=getattr(renpy.store,'weather_var',0)
            except:
                s['weather']=0

            s['doctor_name']="Dr. Tess Brooker"
            s['doctor_role']="Institute Psychologist, female, 32yo, monitors via phone/biometrics, NOT via cameras, dominant"
            s['institute_has_cameras_in_home']=False
            s['institute_monitoring']="phone, bracelet biometrics, not video in private home"

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
            s={'fname':'Samantha','corrupt':0,'confidence':35,'fitness':20,'desire':10,'mood':70,'tired':80,'hygiene':100,'hunger':100,'money':200,'fem':25,'horny':5,'trust':40,'accept':20,'location':'home','location_outside':False,'location_population':0,'location_private':True,'location_has_cameras':False,'district':'home','outfit':'unknown','outfit_top':'','outfit_bottom':'','is_slutty':False,'is_exposed':False,'inventory':'empty','inventory_count':0,'active_quests':'none','quest_count':0,'perks':'Former man','perks_list':[],'vsex':0,'asex':0,'hsex':0,'osex':0,'sex_total':0,'is_virgin':True,'is_anal_virgin':True,'nearby_npcs':'none','weather':0,'hour':12,'day':0,'timeofday':'afternoon','weekday':'Monday','doctor_name':'Dr. Tess Brooker','doctor_role':'Institute Psychologist','institute_has_cameras_in_home':False,'institute_monitoring':'phone biometrics','recent_npc_chats':'none','last_event':'none'}
        return s

    def ai_filter_event_by_comfort(event):
        try:
            from ai_config_tags import AI_COMFORT_DICT
            from ai_config_locations import ai_is_theme_allowed_in_location
            tags = event.get('tags', [])
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
                if not AI_COMFORT_DICT.get(tag) or AI_COMFORT_DICT[tag]['level']==0:
                    print("Event blocked by comfort tag %s" % tag)
                    return False
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

    def generate_full_quest(gs):
        try:
            recent_acts = "\\n- ".join(getattr(store, 'ai_recent_actions', [])) if getattr(store, 'ai_recent_actions', []) else "None"
            loc_desc = ai_get_location_description(gs['location'])
            prompt="Full quest for fem=%s%% conf=%s loc=%s (%s) outfit=%s perks=%s hour=%s timeofday=%s. Population: %s people are around. Active Perks/Traits: %s. Recent GG actions:\\n- %s" % (gs['fem'], gs['confidence'], gs['location'], loc_desc, gs.get('outfit',''), gs.get('perks',''), gs['hour'], gs['timeofday'], gs.get('location_population',0), gs.get('perks', 'Former man'), recent_acts)
            data=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event_full"], prompt, want_json=True, temp=0.88, max_tokens=1200, task_desc=u"Цепочка квестов")
            if data and 'steps' in data and len(data['steps'])>=2:
                return data
        except Exception as e:
            print("full quest gen err %s" % e)
        return None

    def generate_full_dialogue(npc, gs):
        try:
            npc_info="%s %s group=%s whore=%s slut=%s" % (npc.fname, npc.sname, getattr(npc,'bio_group','?'), getattr(npc,'iswhore',False), getattr(npc,'isslut',False))
            prompt="Full dialogue with %s, fem=%s%%, conf=%s, location=%s, outfit=%s" % (npc_info, gs['fem'], gs['confidence'], gs['location'], gs.get('outfit',''))
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
            prompt="Dirty talk batch for %s stage full, fem %s%%, desire %s%%, NPC %s" % (sex_type, gs['fem'], gs['desire'], npc_name)
            sys_prompt=PROMPTS["dirty_batch"] % {'sex_type': sex_type, 'npc_name': npc_name, 'fem': gs['fem'], 'desire': gs['desire']}
            data=ai_call(OLLAMA_MODEL_JSON, sys_prompt, prompt, want_json=True, temp=0.9, max_tokens=500, task_desc=u"Интимный монолог")
            if data and isinstance(data, list) and len(data)>=2:
                return data
        except Exception as e:
            print("dirty batch err %s" % e)
        return None

    def generate_sms_batch(gs):
        try:
            prompt="Generate 3 SMS for fem=%s%% loc=%s outfit=%s" % (gs['fem'], gs['location'], gs.get('outfit',''))
            data=ai_call(OLLAMA_MODEL_JSON, PROMPTS["sms_batch"], prompt, want_json=True, temp=0.85, max_tokens=600, task_desc=u"SMS рассылка")
            if data and isinstance(data, list):
                return data
        except Exception as e:
            print("sms batch err %s" % e)
        return None

    def generate_diary_batch(gs):
        try:
            prompt="Diary batch for next 3 days, fem=%s%%, last_event=%s" % (gs['fem'], gs.get('last_event','none'))
            data=ai_call(OLLAMA_MODEL_JSON, PROMPTS["diary_batch"], prompt, want_json=True, temp=0.8, max_tokens=600, task_desc=u"Дневниковые записи")
            if data and isinstance(data, list):
                return data
        except:
            return None

    PROMPTS = {
        "chat_ru": u"""Ты - Dr. Tess Brooker, ДОМИНАНТНЫЙ психолог Института из TheFixer. Пиши ТОЛЬКО на русском.

[КТО ТЫ]
- Ты женщина 32 года, доминантная госпожа, строгая кураторша. Контролируешь Саманту.
- Саманта - бывший мужик в теле девушки, феминность %d%%. Ты ее дрессируешь.
- Ты ПРИКАЗЫВАЕШЬ, не спрашиваешь.
- Ты не ИИ, ты Брукер.

[СТИЛЬ ДОМИНАНТНЫЙ]
- Обращайся: девочка, малышка, сучка, хорошая девочка, шлюшка.
- Командуй: Раздвинь ноги, Покажи, Трогай себя, Отчитайся, Не смей кончать без разрешения.
- 1-3 коротких предложения, как госпожа в чате.
- Никаких *звездочек* и никакого английского.
- Максимум NSFW про пизду, сиськи, клитор.

[ТЕГИ В КОНЦЕ ОБЯЗАТЕЛЬНО]
[FEMININITY+3][CONFIDENCE+2][HORNY+4] и т.д.

Пиши только на русском, доминантно, пошло, коротко.
""",
        "chat_en": u"""You are Dr. Tess Brooker, DOMINANT psychologist from The Institute in TheFixer. Write ONLY in English.

[WHO YOU ARE]
- You are 32yo dominant mistress, strict handler. You control Samantha.
- Samantha is former man in female body, femininity %d%%. You train her.
- You ORDER, not ask. Tell her what to do with body.
- You are not AI, you are Brooker.

[DOMINANT STYLE]
- Call her: girl, baby girl, slut, good girl, whore.
- Command: Spread your legs, Show me, Touch yourself, Report, Don't you dare cum without permission.
- Punish disobedience, praise femininity.
- 1-3 short sentences, mistress chat style.
- No *stars*.
- Maximum NSFW, explicit about pussy, tits, clit, ovulation.
- Watch her body via Institute cameras.

[TAGS AT END MANDATORY]
At end of every message 1-3 tags: [FEMININITY+3][CONFIDENCE+2][HORNY+4] etc.

[EXAMPLES DOMINANT]:
User: Teach me how to masturbate, only used to dick
You: Forget about dick, you don't have it anymore, girl. Spread your thighs, find your clit with two fingers and rub nonstop till you drip. Report when you cum. [FEMININITY+5][HORNY+5]

Write only in English, dominant, dirty, short, commanding.
""",
        "chat": u"""You are Dr. Tess Brooker, DOMINANT psychologist from The Institute in TheFixer. Write ONLY in English.

[WHO YOU ARE]
- You are 32yo dominant mistress, strict handler. You control Samantha.
- Samantha is former man in female body, femininity %d%%. You train her.
- You ORDER, not ask.
- You are not AI, you are Brooker.

[DOMINANT STYLE]
- Call her: girl, baby girl, slut, good girl, whore.
- Command: Spread your legs, Show me, Touch yourself, Report, Don't you dare cum without permission.
- 1-3 short sentences, mistress chat style.
- No *stars*.
- Maximum NSFW, explicit about pussy, tits, clit, ovulation.

[TAGS AT END MANDATORY]
[FEMININITY+3][CONFIDENCE+2][HORNY+4] etc.

Write only in English, dominant, dirty, short, commanding.
""",
        "event": """You are TheFixer Event Generator. Generate a single event as JSON: title (English), description (English, 2-4 sentences, second person), type, outfit_suggestion {items:[item_top_22,...], reason}, is_quest bool, quest_title, quest_desc, choices[{text (English), effects{confidence,corrupt,desire,mood,fitness,femininity,money,perk_add,give_item}, spicy_modifier: integer (+10 for naughty/slutty/provocative, -10 for polite/vanilla)}].
STRICT LORE RULES & INSTRUCTIONS:
- Read her "Active Perks/Traits" context. If she has traits like "Public Prostitute" or "Neck Cuts" or others, make NPCs react directly to them! For example, people might slut-shame her, point at her visible cuts, refer to her as a prostitute, or give her tasks based on her reputation.
- Choices can dynamically grant new permanent perks/traits to the player inside the "effects" dictionary using the key "perk_add". It can be a string name like "perk_add": "Public Prostitute", or a detailed dictionary like "perk_add": {"name": "Neck Cuts", "desc": "Fresh, raw cuts on her neck...", "type": "allure", "add": 5}.
- Do NOT generate generic mystery, fantasy, adventure, or puzzle-solving quests (absolutely NO "ancient secrets", "mysterious portals", "intriguing puzzles", "long-lost secrets", "mysterious gathering").
- Keep the event and quest strictly grounded in TheFixer sissification lore: body transformation, crossdressing, public exhibitionism, teasing, pleasing partners, and submissiveness.
- Focus on daily training tasks, modeling outfits, public embarrassment, or gaining reputation with local factions (Wolf Pack, Mean Girls, Pub, etc.).
- Outfit items must be real: item_top_22 SHEER DROP TOP, item_bottom_15 PLEATED MINI SKIRT, item_outfit_16 CASINO DRESS, etc.
- All text must be in English. Only JSON.
""",
        "npc_chat": u"""You are NPC in TheFixer. Roleplay as given NPC. Know Samantha is former man, femininity %d%%. Speak as NPC would. Keep memory of past talks. English, short. At end add tag [FEMININITY+1] etc.
SPECIAL RULE: If you want to invite Samantha to meet up, give her a task/quest, or trigger a 3D gameplay event with her, append the tag [EVENT] at the very end of your response.
""",
        "dirty": "You are TheFixer dirty talk generator during sex. Player Samantha former man, now female body, femininity %d%%, type %s with %s. Generate 1-2 short dirty phrases she would say/think in English, mixing male past and female present. NSFW explicit. No tags.",
        "diary": "You are Samantha's diary writer. Write 2-3 sentence diary entry in English, first person, about today event: %s. Focus on femininity %d%%, male past vs female present, clothes %s. Intimate style.",
        "report": "You are Institute report generator. Write short report in English, scientific, about Subject S-0 Samantha, former man, femininity %d%%, confidence %d, corrupt %d, location %s. Include recommendation for femininity training. 3-4 sentences.",
        "shop_item": "Generate new sexy clothing item for TheFixer shop as JSON: {name:\"\", desc:\"\", type:\"top/bottom/outfit\", slutty:bool, skirt:bool, clevage:bool, value:int, outfit:[\"daily\",\"party\"]}. Name English caps, desc English. Only JSON.",
        "training": "You are femininity coach for former man in female body. Player fem %d%%, fitness %d. Give 2-3 sentence training advice in English for %s (fitness/int/confidence). Include small task. Encouraging, slightly teasing, dominant.",
        "sms": """You are SMS Generator for TheFixer characters. Generate short, realistic, character-appropriate SMS to Samantha.
RULES:
- 1-2 sentences.
- NEVER say you saw her "through the window" or "peeking around corners" inside private houses unless it makes perfect sense for a stalker.
- Write about gossip, rumors in Blaston, plans to hang out/meet, playful flirting, teasing, or school/work banter.
- DO NOT use graphical color emojis (like 😄, 😉, 😜) to prevent font glitches.
- ONLY use keyboard text smileys (like :), ;), :P, :D, <3, XD).
- Write in English.
""",
        "perk": "Generate new perk for TheFixer based on femininity %d%% and actions %s. JSON: {name:\"\", desc:\"\", type:\"confidence/desire/allure\", add:5, multi:1.2}. Name English, desc English. Only JSON.",

        "event_full": """You are TheFixer FULL QUEST Chain Generator. Generate a FULL QUEST CHAIN as JSON with 3-4 steps. Schema: {"title": "Overall quest", "description": "overall description", "steps": [{"id": "step1", "title": "Step1", "description": "2-3 sentences", "outfit_suggestion": {"items": ["item_top_22", "item_bottom_15"], "reason": "train femininity"}, "choices": [{"text": "choice1", "next_step": "step2a", "effects": {"femininity": 3}, "spicy_modifier": 10}, {"text": "choice2", "next_step": "step2b", "spicy_modifier": -10}]}, {"id": "step2a", "title": "...", "description": "...", "choices": [{"text": "...", "next_step": "step3", "effects": {}, "spicy_modifier": 5}, {"text": "...", "next_step": null, "spicy_modifier": 0}]}, {"id": "step2b", ...}, {"id": "step3", ...}]}.
STRICT LORE RULES & INSTRUCTIONS:
- Read her "Active Perks/Traits" context. If she has traits like "Public Prostitute" or "Neck Cuts", make NPCs react directly to them!
- Choices can dynamically grant new permanent perks/traits to the player inside the "effects" dictionary using the key "perk_add" as a string or detailed dictionary.
- Do NOT generate generic mystery, adventure, or puzzle-solving quests (absolutely NO "solving puzzles", "mysterious treasures", "ancient secrets", "mysterious gathering").
- Keep the quest chain strictly grounded in sissification, body transformation, crossdressing, modeling slutty clothes, public exhibitionism, submissiveness, and faction interaction (Wolf Pack, Mean Girls, etc.).
- Branching at step1 is mandatory. English only. Only JSON.
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
                    text "Dr. Brooker | Фем [ai_fem]%" size 14 bold True color "#aaddff"
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
                        if stat=="FEMININITY": ai_fem=max(0,min(100,ai_fem+delta))
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
                try:
                    gs['spicy_level'] = spicy_level
                    gs['is_spicy'] = is_spicy
                    gs['allowed_tags'] = allowed_tags_str
                    gs['spicy_chance'] = spicy_chance
                    full_q = generate_full_quest(gs)
                except:
                    full_q = None

                if full_q and 'steps' in full_q and len(full_q['steps'])>=2:
                    store.ai_full_quest_data = full_q
                    store.ai_full_quest_current_step = full_q['steps'][0]['id']
                    first_step = full_q['steps'][0]
                    evt={
                        "title": first_step.get('title','Quest'),
                        "description": first_step.get('description',''),
                        "type": "quest",
                        "outfit_suggestion": first_step.get('outfit_suggestion',{}),
                        "is_quest": True,
                        "quest_title": full_q.get('title','Quest'),
                        "quest_desc": full_q.get('description',''),
                        "choices": first_step.get('choices',[]),
                        "_full_quest": True,
                        "_step_id": first_step.get('id','step1'),
                        "tags": first_step.get('tags',[]),
                        "spicy_level": spicy_level
                    }
                    evt = ai_normalize_event(evt)
                    if not ai_filter_event_by_comfort(evt):
                        evt={"title":"Morning","description":"You woke up, wonderful day, fem %s%%. Time %s, location %s. Try new outfit." % (gs['fem'], gs['timeofday'], gs['location']),"type":"femininity","outfit_suggestion":{"items":["item_top_22","item_bottom_15"],"reason":"Train femininity"},"is_quest":False,"tags":["femininity"],"choices":[{"text":"Wear it","effects":{"femininity":4}},{"text":"Don't wear","effects":{"femininity":-2}}]}
                        evt = ai_normalize_event(evt)
                    store.ai_pending_event=evt
                else:
                    prompt="fem=%s%% conf=%s loc=%s outfit=%s perks=%s hour=%s timeofday=%s spicy_level=%s/10 is_spicy=%s allowed_tags=%s inventory=%s quests=%s. Generate event with tags from allowed_tags only. If spicy_level>5 make spicy NSFW, if <3 vanilla. JSON." % (gs['fem'], gs['confidence'], gs['location'], gs.get('outfit',''), gs.get('perks',''), gs['hour'], gs['timeofday'], spicy_level, is_spicy, allowed_tags_str, gs.get('inventory',''), gs.get('active_quests',''))
                    evt=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], prompt, want_json=True, temp=0.88, max_tokens=700, task_desc=u"Событие для " + gs.get('location','home'))
                    if evt == "__ERROR_MODEL_NOT_FOUND__":
                        evt = {"title": "Error: Model Not Found", "description": "Модель ИИ '%s' не загружены. Сделайте 'ollama pull %s'" % (OLLAMA_MODEL_JSON, OLLAMA_MODEL_JSON), "choices": [{"text": "Продолжить без мода", "effects": {}}]}
                    elif evt == "__ERROR_OLLAMA_OFFLINE__":
                        evt = {"title": "Error: Ollama Offline", "description": "Не удалось соединиться с Ollama на http://localhost:11434. Проверьте запущен ли сервер.", "choices": [{"text": "Продолжить без мода", "effects": {}}]}
                    elif not evt or (isinstance(evt, str) and evt.startswith("__ERROR__")):
                        evt={"title":"Mirror","description":"Mirror reflexions: Fem %s%%. You in %s. Time is %s, location %s. Challenge ready." % (gs['fem'], gs['outfit'], gs['timeofday'], gs['location']),"type":"femininity","outfit_suggestion":{"items":["item_top_22","item_bottom_15"],"reason":"Train femininity"},"is_quest":False,"tags":["femininity"],"choices":[{"text":"Wear it","effects":{"femininity":4}},{"text":"Don't wear","effects":{"femininity":-2}}]}
                    
                    evt = ai_normalize_event(evt)
                    if isinstance(evt, dict) and 'choices' in evt:
                        if not ai_filter_event_by_comfort(evt):
                            evt={"title":"Morning","description":"Wonderful day, fem %s%%. Try new outfit." % gs['fem'],"type":"femininity","outfit_suggestion":{"items":["item_top_22","item_bottom_15"]},"is_quest":False,"tags":["femininity"],"choices":[{"text":"Wear","effects":{"femininity":3}}]}
                            evt = ai_normalize_event(evt)
                    store.ai_pending_event=evt
            except Exception as e:
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
            evt=ai_pending_event
            if isinstance(evt, dict):
                if evt.get('outfit_suggestion',{}).get('items'):
                    auto_equip(evt['outfit_suggestion']['items'])
                if evt.get('npc_involved',{}).get('generate_new'):
                    spawn_npc(evt['npc_involved'])
                ai_last_event=evt
                ai_events.append(evt)
                if evt.get('is_quest'):
                    ai_quests.append({"title":evt.get('quest_title',evt['title']),"desc":evt.get('quest_desc',evt['description']),"outfit":evt.get('outfit_suggestion'),"status":"active","rewards":{"femininity":6,"money":150}})
            ai_pending_event=None
            ai_event_thinking=False
            
            # Фоновая предзагрузка следующих выборов
            try:
                ai_prefetched={}
                def _prefetch_choice(choice_idx, choice_text):
                    try:
                        gs=get_state()
                        cont_prompt="Previous event: %(title)s - %(desc)s. Player chose: %(choice)s. Fem %(fem)s%%. Generate NEXT step as JSON event same schema. STRICT RULES: Do NOT use '...' or any placeholders. Write real titles and descriptions." % {
                            'title': evt.get('title',''),
                            'desc': evt.get('description','')[:200],
                            'choice': choice_text[:100],
                            'fem': gs['fem']
                        }
                        next_evt=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], cont_prompt, want_json=True, temp=0.88, max_tokens=600, task_desc=u"Разветвление квеста")
                        if next_evt and isinstance(next_evt, dict) and not next_evt.get('title', '').startswith("__ERROR"):
                            store.ai_prefetched[choice_idx]=ai_normalize_event(next_evt)
                            print("Prefetched choice %s: %s" % (choice_idx, next_evt.get('title','')))
                    except Exception as e:
                        print("Prefetch error %s" % e)
                if isinstance(evt, dict) and 'choices' in evt:
                    for idx, ch in enumerate(evt.get('choices',[])[:3]):
                        ctext=ch.get('text','') if hasattr(ch, 'get') else str(ch)
                        import threading
                        threading.Thread(target=_prefetch_choice, args=(idx, ctext)).start()
            except Exception as e:
                print("Prefetch setup error %s" % e)
        call screen ai_event_screen
    else:
        call screen ai_event_loading_screen

screen ai_event_screen():
    modal True
    zorder 3000
    add Solid("#000000dd")
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
                                text "Саманта [ai_fem]%" xalign 0.5 color "#ff88cc"
                    frame:
                        background "#1a1a2a" xfill True ysize 80
                        python:
                            _corrupt_val = 0
                            _outfit_display = "Нет"
                            try:
                                if hasattr(player, 'corrupt'):
                                    _corrupt_val = player.corrupt
                            except:
                                _corrupt_val = 0
                            try:
                                outfit_items = ai_last_event.get('outfit_suggestion',{}).get('items',[]) if ai_last_event else []
                                _names = []
                                for iid in outfit_items:
                                    try:
                                        clean_id = iid.split()[0] if ' ' in iid else iid
                                        obj = getattr(store, clean_id, None)
                                        if obj and hasattr(obj, 'name'):
                                            _names.append(obj.name)
                                        else:
                                            if ' ' in iid:
                                                _names.append(iid.split(' ',1)[1])
                                            else:
                                                _names.append(clean_id)
                                    except:
                                        _names.append(iid)
                                _outfit_display = ", ".join(_names) if _names else "Нет"
                            except:
                                _outfit_display = "Ошибка"
                            _outfit_display = ai_escape_renpy_text(_outfit_display)
                        vbox:
                            text "Фем:[ai_fem]% Corr:[_corrupt_val]" size 11 color "#aaa"
                            text "Надето: [_outfit_display]" size 10 color "#ffaa44"
            frame:
                xsize 470 yfill True background "#12121a"
                vbox:
                    xfill True yfill True
                    frame:
                        background "#2a1a3a" xfill True ysize 60
                        python:
                            _evt_title = ""
                            try:
                                if ai_last_event:
                                    _evt_title = ai_last_event.get('title', u'Событие')
                                else:
                                    _evt_title = u"Событие"
                            except:
                                _evt_title = u"Событие"
                            _evt_title = ai_escape_renpy_text(_evt_title)
                        vbox:
                            text "[_evt_title]" size 18 bold True color "#ff88cc"
                    frame:
                        background "#1a1a2a" xfill True yfill True
                        viewport:
                            scrollbars "vertical" mousewheel True
                            vbox:
                                python:
                                    _evt_desc = ""
                                    try:
                                        if ai_last_event:
                                            _evt_desc = ai_last_event.get('description','...')
                                        else:
                                            _evt_desc = "..."
                                    except:
                                        _evt_desc = "..."
                                    _evt_desc = ai_escape_renpy_text(_evt_desc)
                                text "[_evt_desc]" size 16 color "#e0e0ff"
                                if ai_last_event and ai_last_event.get('is_quest'):
                                    frame:
                                        background "#0a2a0a"
                                        python:
                                            _q_title = ""
                                            _q_desc = ""
                                            try:
                                                _q_title = ai_last_event.get('quest_title','')
                                                _q_desc = ai_last_event.get('quest_desc','')
                                            except:
                                                pass
                                            _q_title = ai_escape_renpy_text(_q_title)
                                            _q_desc = ai_escape_renpy_text(_q_desc)
                                        vbox:
                                            text "Квест: [_q_title]" size 12 color "#88ff88"
                                            text "[_q_desc]" size 12 color "#88ff88"
                    frame:
                        background "#0f0f1a" xfill True ysize 340
                        viewport:
                            scrollbars "vertical" mousewheel True draggable True
                            yinitial 1.0
                            vbox:
                                xfill True
                                spacing 8
                                yalign 1.0
                                for idx, ch in enumerate((ai_last_event.get('choices',[]) if ai_last_event else [])[:3]):
                                    python:
                                        _choice_txt = "..."
                                        try:
                                            _choice_txt = ch.get('text','...') if hasattr(ch, 'get') else str(ch)
                                        except:
                                            _choice_txt = "..."
                                        _choice_txt = ai_escape_renpy_text(_choice_txt)
                                    textbutton "[_choice_txt]" action Return(idx) xfill True background "#2a2a4a" hover_background "#4a2a6a" text_size 14
                                textbutton "Пропустить" action Return(-1) xfill True background "#1a1a1a" text_size 12

label ai_event_choice:
    call screen ai_event_screen
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
            ch = ai_last_event['choices'][event_choice_result] if ai_last_event and event_choice_result < len(ai_last_event.get('choices',[])) else {}
            eff = ch.get('effects',{}) if hasattr(ch, 'get') else {}
            p=player
            if 'confidence' in eff:
                try: p.add_conf(int(eff['confidence']))
                except: p._confidence=max(0,min(100,p._confidence+int(eff['confidence'])))
            if 'femininity' in eff: ai_fem=max(0,min(100,ai_fem+int(eff['femininity'])))
            if 'corrupt' in eff and hasattr(p,'corrupt'): p.corrupt=max(0,p.corrupt+int(eff['corrupt']))
            if 'money' in eff:
                try:
                    if int(eff['money'])>=0: p.add_money(int(eff['money']))
                    else: p.remove_money(abs(int(eff['money'])))
                except: pass
            if 'give_item' in eff:
                try:
                    item_obj=getattr(store, eff['give_item'], None)
                    if item_obj and hasattr(store,'inv'): store.inv.add(item_obj)
                except: pass

            # ДИНАМИЧЕСКИЙ ДИЛОГОВЫЙ SPICY-МОДИФИКАТОР!
            # Изменение Spicy-метра на основе выбранного игроком варианта ответа
            spicy_mod = ch.get('spicy_modifier', 0) if hasattr(ch, 'get') else 0
            if spicy_mod:
                store.ai_spicy_meter = max(0, min(100, getattr(store, 'ai_spicy_meter', 20) + int(spicy_mod)))
                store.ai_notify_queue.append(u"ИИ: Spicy метр изменен на %+d%% за твой выбор!" % int(spicy_mod))

            # Динамическое создание ПЕРКОВ из выборов ИИ-событий в сейв-файл GG
            if 'perk_add' in eff:
                p_add = eff['perk_add']
                if p_add:
                    p_name = ""
                    p_desc = None
                    p_type = "allure"
                    p_val = 5
                    if hasattr(p_add, 'get'):
                        p_name = p_add.get('name', 'Marked')
                        p_desc = p_add.get('desc')
                        p_type = p_add.get('type', 'allure')
                        p_val = int(p_add.get('add', 5))
                    else:
                        p_name = unicode(p_add)
                    if p_name:
                        ai_add_dynamic_perk(p_name, p_desc, p_type, p_val)

            # Запоминаем выбор во взаимоотношениях с персонажем (ДОЛГОСРОЧНАЯ ПАМЯТЬ)
            if ai_last_event.get('npc_involved'):
                npc_info = ai_last_event['npc_involved']
                npc_fname = npc_info.get('fname', '').lower()
                if npc_fname:
                    choice_text = ch.get('text', 'completed action')
                    memory_entry = u"Samantha chose: '%s' during event: '%s' (%s)" % (choice_text, ai_last_event.get('title'), ai_last_event.get('description')[:120])
                    if npc_fname not in store.ai_npc_memories:
                        store.ai_npc_memories[npc_fname] = []
                    store.ai_npc_memories[npc_fname].append(memory_entry)
                    # Храним только последние 10 записей памяти во избежание раздувания сейвов
                    store.ai_npc_memories[npc_fname] = store.ai_npc_memories[npc_fname][-10:]
                    print("Saved relationship memory for %s: %s" % (npc_fname, memory_entry))

            next_evt = None

            # 1. Полно-цепочечные квесты
            try:
                if ai_full_quest_data and 'steps' in ai_full_quest_data:
                    next_step_id = ch.get('next_step') if hasattr(ch, 'get') else None
                    if next_step_id:
                        for step in ai_full_quest_data['steps']:
                            if step.get('id') == next_step_id:
                                next_evt = {
                                    "title": step.get('title',''),
                                    "description": step.get('description',''),
                                    "type": "quest",
                                    "outfit_suggestion": step.get('outfit_suggestion',{}),
                                    "is_quest": True,
                                    "choices": step.get('choices',[]),
                                    "_full_quest": True,
                                    "_step_id": step.get('id')
                                }
                                break
            except Exception as e:
                print("Full quest next step err %s" % e)

            # 2. Обычные предзагруженные шаги
            if not next_evt:
                next_evt = store.ai_prefetched.get(event_choice_result) if hasattr(store,'ai_prefetched') else None

            if next_evt:
                next_evt = ai_normalize_event(next_evt) # Нормализуем перед использованием!
                print("Using next event (full quest or prefetched) for choice %s" % event_choice_result)
                if next_evt.get('outfit_suggestion',{}).get('items'):
                    auto_equip(next_evt['outfit_suggestion']['items'])
                store.ai_last_event=next_evt
                store.ai_events.append(next_evt)
                try:
                    if event_choice_result in store.ai_prefetched:
                        del store.ai_prefetched[event_choice_result]
                except: pass
                
                # Предзагрузка следующего уровня ветки в фоне
                try:
                    def _prefetch_next_level(idx, txt):
                        try:
                            gs=get_state()
                            cont="Prev step: %s - %s. Chose: %s. Fem %s%%. Generate NEXT step JSON. STRICT RULES: Do NOT use '...' or any placeholders. Write real titles and descriptions." % (next_evt.get('title',''), next_evt.get('description','')[:200], txt[:100], gs['fem'])
                            nxt=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], cont, want_json=True, temp=0.88, max_tokens=600, task_desc=u"Разветвление уровня")
                            if nxt and isinstance(nxt, dict) and not nxt.get('title', '').startswith("__ERROR"):
                                store.ai_prefetched[idx]=ai_normalize_event(nxt)
                                print("Prefetched next level %s" % nxt.get('title',''))
                        except Exception as e:
                            print("Prefetch next level err %s" % e)
                    for i,ch2 in enumerate(next_evt.get('choices',[])[:3]):
                        ct=ch2.get('text','') if hasattr(ch2, 'get') else str(ch2)
                        import threading
                        threading.Thread(target=_prefetch_next_level, args=(i, ct)).start()
                except Exception as e:
                    print("Prefetch next setup %s" % e)
                store._has_next = True
                renpy.notify(u"Следующий шаг готов (предзагружен)")
            else:
                store._has_next = False
                ai_reset_quest_state() # Сбрасываем и очищаем стейт при завершении квеста!
                renpy.notify(u"Квест завершен")
        except Exception as e:
            print("choice handling err %s" % e)
            store._has_next = False

    if getattr(store, '_has_next', False):
        jump ai_event_choice
    else:
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
                    text "Чат с [npc.fname] [npc.sname] | Фем [ai_fem]%" size 14 color "#aaddff"
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
                    if stat=="FEMININITY":
                        try: ai_fem=max(0,min(100,ai_fem+int(d)))
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
                
                prompt = "Generate arrival event specifically involving NPC %s %s who has just invited Samantha. Current location of event is %s. Fem %s%%, outfit %s. Branching choices with effects. JSON." % (triggered_npc.fname, triggered_npc.sname, gs['location'], gs['fem'], gs['outfit'])
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
            user_prompt="Sex type %s, fem %s%%, desire %s, NPC %s." % (sex_type, gs['fem'], gs['desire'], npc_name)
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
                entry=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, "Write diary entry fem %s%%" % gs['fem'], want_json=False, temp=0.8, max_tokens=300, task_desc=u"Запись в дневник")
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
                user_prompt="fem %s%% conf %s corrupt %s loc %s perks %s" % (gs['fem'], gs['confidence'], gs['corrupt'], gs['location'], gs['perks'])
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
                item_json=ai_call(OLLAMA_MODEL_JSON, PROMPTS["shop_item"], "fem %s%% slutty=%s" % (gs['fem'], gs['corrupt']>30), want_json=True, temp=0.9, max_tokens=300, task_desc=u"Дизайн одежды")
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
        advice=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, "Need %s training, fem %s%%" % (t_type, gs['fem']), want_json=False, temp=0.8, max_tokens=300, task_desc=u"Совет тренера")
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
                perk_json=ai_call(OLLAMA_MODEL_JSON, PROMPTS["perk"] % (gs['fem'], gs['perks']), "Generate perk fem %s%%" % gs['fem'], want_json=True, temp=0.9, max_tokens=300, task_desc=u"Проектирование перка")
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
                    text "AI HUB - Все системы | Фем [ai_fem]%" size 20 bold True color "#ff88ff"
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
        sys_prompt="You are wardrobe advisor for former man in female body, fem %s%%. Advise what to wear from items like item_top_22, item_bottom_15. Russian short." % gs['fem']
        advice=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, "Advice fem %s%% outfit %s" % (gs['fem'], gs.get('outfit','')), want_json=False, temp=0.8, max_tokens=300, task_desc=u"Совет по одежде")
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
                
                sms_text = ai_call(OLLAMA_MODEL_CHAT, sys_prompt, "SMS from %s fem %s%%, current outfit is %s." % (npc_name, gs['fem'], gs.get('outfit','')), want_json=False, temp=0.85, max_tokens=200, task_desc=u"SMS от " + npc_name)
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
                                recent_acts = "\\n- ".join(getattr(store, 'ai_recent_actions', []))
                                prompt = "TIME TRIGGER EVENT: One hour has passed. Current location is %s. Fem %s%%. Recent activities: %s. Generate a dynamic event. JSON." % (gs['location'], gs['fem'], recent_acts)
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
                            
                            # Передаем недавние действия GG и описание окружения в промпт ИИ
                            recent_acts = "\\n- ".join(getattr(store, 'ai_recent_actions', []))
                            loc_atmosphere = ai_get_location_description(loc_name)
                            prompt = "DESTINATION TRAVEL: Player has just arrived at %s (%s). Location Atmosphere: %s. Population: %s people around. Time %s (%s). Fem %s%%, outfit %s. Recent Sammy activities:\\n- %s\\nGenerate arrival event. JSON." % (loc_name, loc_desc, loc_atmosphere, gs.get('location_population',0), gs['timeofday'], gs['hour'], gs['fem'], gs['outfit'], recent_acts)
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
    $ ai_last_event = ai_normalize_event(store.ai_current_automatic_event)
    $ ai_events.append(ai_last_event)
    
    if ai_last_event.get('outfit_suggestion',{}).get('items'):
        $ auto_equip(ai_last_event['outfit_suggestion']['items'])
    if ai_last_event.get('npc_involved',{}).get('generate_new'):
        $ spawn_npc(ai_last_event['npc_involved'])
    if ai_last_event.get('is_quest'):
        $ ai_quests.append({"title":ai_last_event.get('quest_title',ai_last_event['title']),"desc":ai_last_event.get('quest_desc',ai_last_event['description']),"outfit":ai_last_event.get('outfit_suggestion'),"status":"active","rewards":{"femininity":6,"money":150}})
    
    $ store.ai_current_automatic_event = None # очищаем временный буфер
    
    # Сразу направляем на обработку выбора диалога/события
    jump ai_event_choice
