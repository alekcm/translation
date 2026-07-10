# TheFixer AI ALL SYSTEMS v5 - Python2 compatible for RenPy 7.5.3
# Все интеграции: чат, события 3D, NPC, секс, дневник, квесты, магазин, тренер, SMS, перки, одежда
# Только феминность, без дисфории, без SD, только родные 3D модели

init python:
    import json, urllib, urllib2, re, os, base64
    import random as py_random

    OLLAMA_URL = "http://localhost:11434/api/chat"
    OLLAMA_MODEL_CHAT = "hf.co/mradermacher/Dirty-Muse-Writer-v01-Uncensored-Erotica-NSFW-i1-GGUF:i1-IQ3_S"
    OLLAMA_MODEL_JSON = "llama3.2:3b"
    # Для 4Гб VRAM: твоя Dirty-Muse IQ3_S (3.2Гб) уже подходит.
    # Для событий JSON вместо llama3.1 8B (4.7Гб) используй llama3.2:3b (2Гб) или qwen2.5:3b (2Гб) или phi3.5:3.8b (2.3Гб)
    # Если нет llama3.2:3b, сделай: ollama pull llama3.2:3b
    # Альтернативы для 4Гб: gemma2:2b, qwen2.5:1.5b, dolphin-phi:2.7b

    # Базовый вызов без f-строк
    def ai_call(model, sys_prompt, user_prompt, want_json=False, temp=0.85, max_tokens=700):
        messages=[{"role":"system","content":sys_prompt},{"role":"user","content":user_prompt}]
        payload={"model":model,"messages":messages,"stream":False,"options":{"temperature":temp,"top_p":0.92,"num_predict":max_tokens,"num_ctx":4096}}
        if want_json:
            payload["format"]="json"
        try:
            data=json.dumps(payload).encode('utf-8')
            req=urllib2.Request(OLLAMA_URL, data=data, headers={'Content-Type':'application/json'})
            resp=urllib2.urlopen(req, timeout=90)
            res=json.loads(resp.read().decode('utf-8'))
            content=res['message']['content']
            if want_json:
                content=re.sub(r'```json|```','',content).strip()
                f=content.find('{')
                l=content.rfind('}')
                if f!=-1:
                    content=content[f:l+1]
                if content.strip().startswith('['):
                    f2=content.find('['); l2=content.rfind(']')
                    content=content[f2:l2+1]
                return json.loads(content)
            return content
        except Exception as e:
            print("AI call error %s: %s" % (model, e))
            return None

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
                    s['outfit']="unknown"; s['outfit_top']=""; s['outfit_bottom']=""; s['is_slutty']=False; s['is_exposed']=False
            except:
                s['outfit']="unknown"; s['outfit_top']=""; s['outfit_bottom']=""; s['is_slutty']=False; s['is_exposed']=False

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
        # Проверяет разрешены ли теги события по комфорту и локации
        try:
            from ai_config_tags import AI_COMFORT_DICT
            from ai_config_locations import ai_is_theme_allowed_in_location
            # Теги события
            tags = event.get('tags', [])
            # Если тегов нет - пробуем угадать по типу и описанию
            if not tags:
                # Fallback по type
                type_to_tag = {
                    "femininity": ["femininity"],
                    "corruption": ["prostitution","freeuse"],
                    "institute": ["mindcontrol","body_mod"],
                    "horny": ["exhibitionism"],
                    "work": ["prostitution"],
                    "social": ["bullying"]
                }
                tags = type_to_tag.get(event.get('type',''), [])
            # Проверяем каждый тег
            for tag in tags:
                if not AI_COMFORT_DICT.get(tag) or AI_COMFORT_DICT[tag]['level']==0:
                    print("Event blocked by comfort tag %s" % tag)
                    return False
                # Проверяем локацию
                loc = get_state().get('location','home')
                if not ai_is_theme_allowed_in_location(tag, loc):
                    print("Event tag %s not allowed in location %s" % (tag, loc))
                    return False
            return True
        except Exception as e:
            print("filter comfort err %s" % e)
            return True  # в случае ошибки разрешаем

    def ai_get_spicy_prompt_modifier():
        # Кидает кубик и возвращает уровень spicy для промпта
        try:
            from ai_config_spicy import ai_roll_spicy, ai_get_spicy_level
            is_spicy, chance, roll = ai_roll_spicy()
            level = ai_get_spicy_level()
            # Обновляем счетчики
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


    # ===== АСИНХРОННЫЙ ВЫЗОВ (не фризит игру) =====
    # Для 4Гб VRAM используем маленькие модели
    # Chat: твоя Dirty-Muse IQ3_S уже подходит под 4Гб (3.2Гб), можно оставить
    # Events JSON: вместо llama3.1 8B (4.7Гб) лучше llama3.2:3b (2Гб) или qwen2.5:3b
    # Если Ollama тормозит - поставь "llama3.2:3b" или "qwen2.5:3b" или "phi3.5:3.8b"
    def start_async_ollama(target_func):
        # Запускает функцию в отдельном потоке чтобы не фризить RenPy
        import threading
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
                # Проверяем есть ли вещь в гардеробе если only_if_owned
                try:
                    item_obj = getattr(renpy.store, clean_id, None)
                    if item_obj:
                        ward = getattr(renpy.store, 'wardrobe', None)
                        if only_if_owned and ward and hasattr(ward, 'qty'):
                            try:
                                if ward.qty(item_obj) <= 0:
                                    # Нет вещи - не надеваем, только если она выдается по квесту (give_item)
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
            renpy.notify("Новый персонаж: %s" % fname)
            return npc
        except Exception as e:
            print("spawn err %s" % e)
            return None

    # ===== FULL OPTIMIZATIONS - GENERATE ALL AT ONCE FOR SPEED =====
    def generate_full_quest(gs):
        try:
            prompt="Full quest for fem=%s%% conf=%s loc=%s outfit=%s perks=%s hour=%s timeofday=%s" % (gs['fem'], gs['confidence'], gs['location'], gs.get('outfit',''), gs.get('perks',''), gs['hour'], gs['timeofday'])
            data=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event_full"], prompt, want_json=True, temp=0.88, max_tokens=1200)
            if data and 'steps' in data and len(data['steps'])>=2:
                return data
        except Exception as e:
            print("full quest gen err %s" % e)
        return None

    def generate_full_dialogue(npc, gs):
        try:
            npc_info="%s %s group=%s whore=%s slut=%s" % (npc.fname, npc.sname, getattr(npc,'bio_group','?'), getattr(npc,'iswhore',False), getattr(npc,'isslut',False))
            prompt="Full dialogue with %s, fem=%s%%, conf=%s, location=%s, outfit=%s" % (npc_info, gs['fem'], gs['confidence'], gs['location'], gs.get('outfit',''))
            sys_prompt=PROMPTS["npc_full"] % {'fname': npc.fname, 'sname': npc.sname, 'bio_group': getattr(npc,'bio_group','?'), 'iswhore': getattr(npc,'iswhore',False), 'fem': gs['fem']}
            data=ai_call(OLLAMA_MODEL_JSON, sys_prompt, prompt, want_json=True, temp=0.85, max_tokens=800)
            if data and 'dialogue' in data:
                return data['dialogue']
        except Exception as e:
            print("full dialogue err %s" % e)
        return None

    def generate_dirty_batch(gs, sex_type="vag", npc_name="partner"):
        try:
            prompt="Dirty talk batch for %s stage full, fem %s%%, desire %s%%, NPC %s" % (sex_type, gs['fem'], gs['desire'], npc_name)
            sys_prompt=PROMPTS["dirty_batch"] % {'sex_type': sex_type, 'npc_name': npc_name, 'fem': gs['fem'], 'desire': gs['desire']}
            data=ai_call(OLLAMA_MODEL_JSON, sys_prompt, prompt, want_json=True, temp=0.9, max_tokens=500)
            if data and isinstance(data, list) and len(data)>=2:
                return data
        except Exception as e:
            print("dirty batch err %s" % e)
        return None

    def generate_sms_batch(gs):
        try:
            prompt="Generate 3 SMS for fem=%s%% loc=%s outfit=%s" % (gs['fem'], gs['location'], gs.get('outfit',''))
            data=ai_call(OLLAMA_MODEL_JSON, PROMPTS["sms_batch"], prompt, want_json=True, temp=0.85, max_tokens=600)
            if data and isinstance(data, list):
                return data
        except Exception as e:
            print("sms batch err %s" % e)
        return None

    def generate_diary_batch(gs):
        try:
            prompt="Diary batch for next 3 days, fem=%s%%, last_event=%s" % (gs['fem'], gs.get('last_event','none'))
            data=ai_call(OLLAMA_MODEL_JSON, PROMPTS["diary_batch"], prompt, want_json=True, temp=0.8, max_tokens=600)
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
        "event": "You are TheFixer Event Generator. JSON only: title (English), description (English, 2-4 sentences, second person, about new body, femininity), type, outfit_suggestion {items:[item_top_22,...], reason}, is_quest bool, quest_title, quest_desc, choices[{text (English), effects{confidence,corrupt,desire,mood,fitness,femininity,money,perk_add,give_item}}]. Outfit items must be real: item_top_22 SHEER DROP TOP, item_bottom_15 PLEATED MINI SKIRT, item_outfit_16 CASINO DRESS etc. Write everything in English.",
        "npc_chat": "You are NPC in TheFixer. Roleplay as given NPC. Know Samantha is former man, femininity %d%%. Speak as NPC would (slutty, shy, etc). Keep memory of past talks. English, short. At end add tag [FEMININITY+1] etc.",
        "dirty": "You are TheFixer dirty talk generator during sex. Player Samantha former man, now female body, femininity %d%%, type %s with %s. Generate 1-2 short dirty phrases she would say/think in English, mixing male past and female present. NSFW explicit. No tags.",
        "diary": "You are Samantha's diary writer. Write 2-3 sentence diary entry in English, first person, about today event: %s. Focus on femininity %d%%, male past vs female present, clothes %s. Intimate style.",
        "report": "You are Institute report generator. Write short report in English, scientific, about Subject S-0 Samantha, former man, femininity %d%%, confidence %d, corrupt %d, location %s. Include recommendation for femininity training. 3-4 sentences.",
        "shop_item": "Generate new sexy clothing item for TheFixer shop as JSON: {name:\"\", desc:\"\", type:\"top/bottom/outfit\", slutty:bool, skirt:bool, clevage:bool, value:int, outfit:[\"daily\",\"party\"]}. Name English caps, desc English. Only JSON.",
        "training": "You are femininity coach for former man in female body. Player fem %d%%, fitness %d. Give 2-3 sentence training advice in English for %s (fitness/int/confidence). Include small task. Encouraging, slightly teasing, dominant.",
        "sms": "Generate SMS from NPC %s (%s) to Samantha, former man. SMS short, English, about seeing her in %s wearing %s. Could be flirty, slut-shaming, or friendly. 1-2 sentences.",
        "perk": "Generate new perk for TheFixer based on femininity %d%% and actions %s. JSON: {name:\"\", desc:\"\", type:\"confidence/desire/allure\", add:5, multi:1.2}. Name English, desc English. Only JSON.",

        "event_full": "You are TheFixer FULL QUEST Generator. Generate FULL QUEST CHAIN as JSON with 3-4 steps, not just one event. Schema: {\"title\": \"Overall quest\", \"description\": \"overall\", \"steps\": [{\"id\": \"step1\", \"title\": \"Step1\", \"description\": \"2-3 sentences\", \"outfit_suggestion\": {\"items\": [\"item_top_22\", \"item_bottom_15\"], \"reason\": \"train femininity\"}, \"choices\": [{\"text\": \"choice1\", \"next_step\": \"step2a\", \"effects\": {\"femininity\": 3}}, {\"text\": \"choice2\", \"next_step\": \"step2b\"}]}, {\"id\": \"step2a\", \"title\": \"...\", \"description\": \"...\", \"choices\": [{\"text\": \"...\", \"next_step\": \"step3\", \"effects\": {}}, {\"text\": \"...\", \"next_step\": null}]}, {\"id\": \"step2b\", ...}, {\"id\": \"step3\", ...}]}. Rules: 3-4 steps, branching at step1 into 2 branches, each branch 1-2 more steps, outfit per step, English, Only JSON.",
        "npc_full": "You are NPC dialogue generator. Generate FULL dialogue of 4 exchanges between NPC {fname} {sname} (group {bio_group}, whore={iswhore}) and Samantha (former man, fem {fem}%%). JSON: {\"dialogue\": [{\"role\": \"npc\", \"text\": \"...\"}, {\"role\": \"player_options\", \"options\": [\"reply1\", \"reply2\"]}, {\"role\": \"npc\", \"text\": \"...\"}, ...]} 8 entries (4 npc, 4 player_options). English, short, NSFW ok, remember past. Only JSON.",
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
default ai_chat_lang = "en"  # en - основной теперь английский как просил

default ai_events = []
default ai_quests = []
default ai_last_event = None
default ai_pending_event = None
default ai_event_thinking = False
default ai_prefetched = {}  # {choice_idx: event} - предзагрузка на 1 шаг вперед
default ai_full_quest = None  # если LLM сгенерил сразу весь квест

default ai_npc_chats = {}
default ai_dirty_talk_history = []
default ai_diary_entries = []
default ai_reports = []
default ai_sms_inbox = []
default ai_shop_items = []
default ai_perks_generated = []

# NEW: Full optimizations - prefetch all at once
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

# CHAT WITH BROOKER
label ai_chat_brooker:
    call screen ai_chat_screen
    return

screen ai_chat_screen():
    modal True
    # tag menu removed to avoid main menu conflict
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
                            if m['role']=='user':
                                frame:
                                    background "#1e3a5a" xalign 1.0 xmaximum 380
                                    text m['content'] size 14
                            else:
                                frame:
                                    background "#1a2330" xmaximum 400
                                    text m['content'] size 14 color "#d0e0ff"
                        if ai_thinking:
                            text "Dr. Brooker печатает... (игра НЕ на паузе, можешь ходить)" size 12 italic True color "#88ffaa"
            frame:
                background "#0a2a4a" xfill True ysize 60
                hbox:
                    xfill True spacing 8
                    textbutton "Написать..." action Call("ai_chat_input") xfill True yfill True background "#112a4a"
                    textbutton "Отчет" action Call("ai_report_view") background "#112a4a"
    # Таймер проверяет пришел ли ответ из потока
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
        # АСИНХРОННЫЙ вызов - не фризит игру
        def _chat_thread():
            try:
                gs=get_state()
                # Выбор языка
                lang = getattr(store, 'ai_chat_lang', 'ru')
                chat_key = "chat_ru" if lang == "ru" else "chat_en"
                base_prompt=PROMPTS.get(chat_key, PROMPTS["chat"]) % gs['fem']
                # ПОЛНЫЙ КОНТЕКСТ чтобы не было галлюцинаций про камеры и ночные лучи утром
                full_context = """
[FULL GAME STATE - USE IT TO BE ACCURATE, DO NOT HALLUCINATE]
Name: %(fname)s %(sname)s (%(name)s), Femininity: %(fem)s%%, Confidence: %(confidence)s, Corrupt: %(corrupt)s, Fitness: %(fitness)s, Desire: %(desire)s, Mood: %(mood)s, Tired: %(tired)s, Hygiene: %(hygiene)s, Hunger: %(hunger)s, Money: %(money)s, Horny: %(horny)s, Trust: %(trust)s, Acceptance: %(accept)s
Time: Day %(day)s, Hour %(hour)s, TimeOfDay: %(timeofday)s (%(weekday)s) - IMPORTANT: If timeofday is morning (6-11), DO NOT talk about night lights, night, moon. If afternoon, don't talk about night. Respect current time. Current hour %(hour)s.
Location: %(location)s, District: %(district)s, Outside: %(location_outside)s, Population: %(location_population)s, Private: %(location_private)s, HasCameras: %(location_has_cameras)s
Outfit: %(outfit)s, Top: %(outfit_top)s, Bottom: %(outfit_bottom)s, Slutty: %(is_slutty)s, Exposed: %(is_exposed)s
Inventory: %(inventory)s (count %(inventory_count)s)
Active Quests: %(active_quests)s (total %(quest_count)s)
Perks: %(perks)s
Sex History: vsex=%(vsex)s asex=%(asex)s hsex=%(hsex)s osex=%(osex)s total=%(sex_total)s virgin=%(is_virgin)s anal_virgin=%(is_anal_virgin)s
Weather: %(weather)s, Nearby NPCs: %(nearby_npcs)s
Recent NPC chats: %(recent_npc_chats)s
Last AI Event: %(last_event)s
Institute Monitoring: %(institute_monitoring)s - CRITICAL: Institute does NOT have cameras in private home locations (bedroom, bathroom, common, kitchen at home). HasCamerasInHome=%(institute_has_cameras_in_home)s. Do NOT claim you watch her from window or have cameras in her room. You only have phone/biometrics data.
Doctor: %(doctor_name)s, %(doctor_role)s
""" % gs
                sys_prompt = base_prompt + "\n" + full_context + "\nRULES: Never hallucinate cameras in private home. Never talk about night when it's morning. Respect location and time."
                # Берем последний ввод пользователя из истории
                last_user = ""
                try:
                    last_user = ai_chat_history[-1]['content'] if ai_chat_history else ""
                except:
                    last_user = ""
                data=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, last_user, want_json=False, temp=0.82, max_tokens=350)
                store.ai_pending_chat_response=data
            except Exception as e:
                store.ai_pending_chat_response="__ERROR__ %s" % e
            # Не трогаем ai_thinking здесь, пусть poll его снимет
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
            if data and "__ERROR__" not in data:
                clean=re.sub(r'\[([A-Z_]+)([+-]\d+)\]','',data).strip()
                for stat, d in re.findall(r'\[([A-Z_]+)([+-]\d+)\]', data):
                    try:
                        delta=int(d)
                        if stat=="FEMININITY": ai_fem=max(0,min(100,ai_fem+delta))
                        elif stat=="CONFIDENCE" and hasattr(player,'_confidence'): player._confidence=max(0,min(100,player._confidence+delta))
                        elif stat=="CORRUPTION" and hasattr(player,'corrupt'): player.corrupt=max(0,player.corrupt+delta)
                    except: pass
                ai_chat_history.append({"role":"assistant","content":clean})
            elif data:
                ai_chat_history.append({"role":"assistant","content":data})
            else:
                ai_chat_history.append({"role":"assistant","content":"(Институт offline)"})
            ai_pending_chat_response=None
            ai_thinking=False
        call screen ai_chat_screen
    else:
        call screen ai_chat_screen

# EVENTS WITH 3D MODEL - ASYNC - FULL QUEST AT ONCE (оптимизация)
label ai_gen_event:
    $ ai_event_thinking=True
    $ ai_pending_event=None
    $ ai_prefetched={}
    $ ai_full_quest_data=None
    python:
        def _event_thread():
            try:
                gs=get_state()
                # Spicy dice
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

                # Full quest first
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
                    if not ai_filter_event_by_comfort(evt):
                        evt={"title":"Morning","description":"You woke up, wonderful day, fem %s%%. Time %s, location %s. Try new outfit." % (gs['fem'], gs['timeofday'], gs['location']),"type":"femininity","outfit_suggestion":{"items":["item_top_22","item_bottom_15"],"reason":"Train femininity"},"is_quest":False,"tags":["femininity"],"choices":[{"text":"Wear it","effects":{"femininity":4}},{"text":"Don't wear","effects":{"femininity":-2}}]}
                    store.ai_pending_event=evt
                else:
                    prompt="fem=%s%% conf=%s loc=%s outfit=%s perks=%s hour=%s timeofday=%s spicy_level=%s/10 is_spicy=%s allowed_tags=%s inventory=%s quests=%s. Generate event with tags from allowed_tags only. If spicy_level>5 make spicy NSFW, if <3 vanilla. JSON." % (gs['fem'], gs['confidence'], gs['location'], gs.get('outfit',''), gs.get('perks',''), gs['hour'], gs['timeofday'], spicy_level, is_spicy, allowed_tags_str, gs.get('inventory',''), gs.get('active_quests',''))
                    evt=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], prompt, want_json=True, temp=0.88, max_tokens=700)
                    if not evt:
                        evt={"title":"Mirror","description":"Fem %s%%. You in %s. Time is %s, location %s. Spicy %s/10." % (gs['fem'], gs['outfit'], gs['timeofday'], gs['location'], spicy_level),"type":"femininity","outfit_suggestion":{"items":["item_top_22","item_bottom_15"],"reason":"Train femininity"},"is_quest":False,"tags":["femininity"],"choices":[{"text":"Wear it","effects":{"femininity":4}},{"text":"Don't wear","effects":{"femininity":-2}}]}
                    if not ai_filter_event_by_comfort(evt):
                        evt={"title":"Morning","description":"Wonderful day, fem %s%%. Try new outfit." % gs['fem'],"type":"femininity","outfit_suggestion":{"items":["item_top_22","item_bottom_15"]},"is_quest":False,"tags":["femininity"],"choices":[{"text":"Wear","effects":{"femininity":3}}]}
                    store.ai_pending_event=evt
            except Exception as e:
                store.ai_pending_event={"title":"Error","description":"Institute offline: %s" % e,"type":"error","outfit_suggestion":{"items":[]},"is_quest":False,"choices":[{"text":"OK","effects":{}}]}
            renpy.restart_interaction()
        import threading
        ai_thread_obj=threading.Thread(target=_event_thread)
        ai_thread_obj.daemon=True
        ai_thread_obj.start()
    call screen ai_event_loading_screen

screen ai_event_loading_screen():
    modal True
    # tag menu removed to avoid main menu conflict
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
            text "Игра НЕ на паузе, можешь закрыть это окно и ходить" size 12 color "#888" xalign 0.5
            text "Фем [ai_fem]% - 3D модель уже готова" size 11 color "#666" xalign 0.5
            textbutton "Закрыть и ждать в фоне" action Return() xalign 0.5 background "#2a2a4a"
    timer 0.5 action Jump("ai_event_poll") repeat True

label ai_event_poll:
    if ai_pending_event is not None:
        python:
            evt=ai_pending_event
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
            # ПРЕДЗАГРУЗКА на 1 шаг вперед - генерим следующие события для каждого выбора в фоне
            try:
                ai_prefetched={}
                def _prefetch_choice(choice_idx, choice_text):
                    try:
                        gs=get_state()
                        # Промпт для продолжения квеста
                        cont_prompt="Previous event: %(title)s - %(desc)s. Player chose: %(choice)s. Fem %(fem)s%%. Generate NEXT step as JSON event same schema. Continue story." % {
                            'title': evt.get('title',''),
                            'desc': evt.get('description','')[:200],
                            'choice': choice_text[:100],
                            'fem': gs['fem']
                        }
                        next_evt=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], cont_prompt, want_json=True, temp=0.88, max_tokens=600)
                        if next_evt:
                            store.ai_prefetched[choice_idx]=next_evt
                            print("Prefetched choice %s: %s" % (choice_idx, next_evt.get('title','')))
                    except Exception as e:
                        print("Prefetch error %s" % e)
                # Запускаем для каждого выбора
                for idx, ch in enumerate(evt.get('choices',[])[:3]):
                    ctext=ch.get('text','') if isinstance(ch, dict) else str(ch)
                    # Запускаем в отдельном потоке
                    import threading
                    ai_thread_obj=threading.Thread(target=_prefetch_choice, args=(idx, ctext))
                    ai_thread_obj.daemon=True
                    ai_thread_obj.start()
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
            # Левая часть - 3D модель из игры (только она, без голой в середине)
            frame:
                xsize 380 yfill True background "#0a0a12"
                vbox:
                    xfill True yfill True
                    frame:
                        background "#1a1a2a" xfill True ysize 35
                        text "3D модель (игра)" size 11 color "#666" xalign 0.5
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
                        vbox:
                            text "Фем:[ai_fem]% Corr:[_corrupt_val]" size 11 color "#aaa"
                            text "Надето: [_outfit_display]" size 10 color "#ffaa44"
                            text "Только из гардероба" size 9 color "#666" italic True
            # Правая часть - описание и выборы
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
                                    _evt_title = ai_last_event.get('title','Событие')
                                else:
                                    _evt_title = "Событие"
                            except:
                                _evt_title = "Событие"
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
                                        vbox:
                                            text "Квест: [_q_title]" size 12 color "#88ff88"
                                            text "[_q_desc]" size 12 color "#88ff88"
                    # ПОДНЯТЫЕ КНОПКИ - расширяются вверх, не вылезают за экран
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
                                            _choice_txt = ch.get('text','...') if isinstance(ch, dict) else str(ch)
                                        except:
                                            _choice_txt = "..."
                                    textbutton "[_choice_txt]" action Return(idx) xfill True background "#2a2a4a" hover_background "#4a2a6a" text_size 14
                                textbutton "Пропустить" action Return(-1) xfill True background "#1a1a1a" text_size 12




label ai_event_choice:
    call screen ai_event_screen
    $ event_choice_result = _return
    if event_choice_result < 0:
        $ renpy.notify("Квест отложен")
        return

    python:
        try:
            # Применяем эффекты текущего выбора
            ch = ai_last_event['choices'][event_choice_result] if ai_last_event and event_choice_result < len(ai_last_event.get('choices',[])) else {}
            eff = ch.get('effects',{}) if isinstance(ch, dict) else {}
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

            next_evt = None

            # 1. Пытаемся найти следующий шаг в ПОЛНОМ квесте (сгенерированном за 1 запрос)
            try:
                if ai_full_quest_data and 'steps' in ai_full_quest_data:
                    next_step_id = ch.get('next_step') if isinstance(ch, dict) else None
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

            # 2. Если нет полного квеста - проверяем предзагруженный ивент (1 шаг вперед)
            if not next_evt:
                next_evt = store.ai_prefetched.get(event_choice_result) if hasattr(store,'ai_prefetched') else None

            if next_evt:
                print("Using next event (full quest or prefetched) for choice %s" % event_choice_result)
                if next_evt.get('outfit_suggestion',{}).get('items'):
                    auto_equip(next_evt['outfit_suggestion']['items'])
                store.ai_last_event=next_evt
                store.ai_events.append(next_evt)
                # Чистим использованный префетч
                try:
                    if event_choice_result in store.ai_prefetched:
                        del store.ai_prefetched[event_choice_result]
                except: pass
                # Запускаем предзагрузку для нового шага (еще 1 шаг вперед)
                try:
                    def _prefetch_next_level(idx, txt):
                        try:
                            gs=get_state()
                            cont="Prev step: %s - %s. Chose: %s. Fem %s%%. Generate NEXT step JSON." % (next_evt.get('title',''), next_evt.get('description','')[:200], txt[:100], gs['fem'])
                            nxt=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], cont, want_json=True, temp=0.88, max_tokens=600)
                            if nxt:
                                store.ai_prefetched[idx]=nxt
                                print("Prefetched next level %s" % nxt.get('title',''))
                        except Exception as e:
                            print("Prefetch next level err %s" % e)
                    import threading
                    for i,ch2 in enumerate(next_evt.get('choices',[])[:3]):
                        ct=ch2.get('text','') if isinstance(ch2, dict) else str(ch2)
                        ai_thread_obj=threading.Thread(target=_prefetch_next_level, args=(i, ct))
                        ai_thread_obj.daemon=True
                        ai_thread_obj.start()
                except Exception as e:
                    print("Prefetch next setup %s" % e)
                store._has_next = True
                renpy.notify("Следующий шаг готов (предзагружен)")
            else:
                # Нет следующего шага - квест закончился
                store._has_next = False
                renpy.notify("Квест завершен")
        except Exception as e:
            print("choice handling err %s" % e)
            store._has_next = False

    # Если есть следующий шаг - сразу показываем его без вылета в меню
    if getattr(store, '_has_next', False):
        jump ai_event_choice
    else:
        return
        if event_choice_result>=0 and getattr(store, '_prefetched_used', False):
            jump ai_event_choice
    return

# NPC HUB
label ai_npc_hub:
    python:
        npc_list = getattr(store, 'npc_girls', [])[:12]
    call screen ai_npc_hub_screen(npc_list)
    return

screen ai_npc_hub_screen(npcs):
    modal True
    # tag menu removed to avoid main menu conflict
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
                text "AI Чат с NPC (с памятью)" size 18 bold True color "#ff88cc"
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 8
                    for npc in npcs:
                        $ npc_id = getattr(npc,'sname',str(npc.fname))
                        $ chat_len = len(ai_npc_chats.get(npc_id,[]))
                        hbox:
                            xfill True
                            text "[npc.fname] [npc.sname] ([chat_len])" size 14 color "#ccc"
                            textbutton "Чат" action [SetVariable("ai_current_npc", npc), Jump("ai_npc_chat")] background "#2a2a4a"

default ai_current_npc = None

label ai_npc_chat:
    $ npc = ai_current_npc
    $ npc_id = getattr(npc,'sname',npc.fname) if npc else "unknown"
    if npc_id not in ai_npc_chats:
        $ ai_npc_chats[npc_id] = []
    call screen ai_npc_chat_screen(npc, ai_npc_chats[npc_id])
    return

screen ai_npc_chat_screen(npc, history):
    modal True
    # tag menu removed to avoid main menu conflict
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
                text "Чат с [npc.fname] [npc.sname] | Фем [ai_fem]%" size 14 color "#aaddff"
            frame:
                background "#0a0a12" xfill True yfill True
                viewport:
                    yinitial 1.0
                    scrollbars "vertical"
                    vbox:
                        spacing 8
                        for m in history[-20:]:
                            if m['role']=='user':
                                frame:
                                    background "#1e3a5a" xalign 1.0 xmaximum 350
                                    text m['content'] size 13
                            else:
                                frame:
                                    background "#1a2a3a" xmaximum 350
                                    text m['content'] size 13 color "#d0e0ff"
            frame:
                background "#1a1a2a" xfill True ysize 60
                hbox:
                    xfill True spacing 8
                    textbutton "Написать..." action Call("ai_npc_input") xfill True background "#2a2a4a"
                    textbutton "Назад" action Return() background "#1a1a1a"

label ai_npc_input:
    $ npc = ai_current_npc
    $ npc_id = getattr(npc,'sname',npc.fname)
    $ user_msg = renpy.input("Сказать %s:" % npc.fname, length=400)
    $ user_msg = user_msg.strip()
    if not user_msg:
        jump ai_npc_chat
    $ ai_npc_chats[npc_id].append({"role":"user","content":user_msg})
    python:
        gs=get_state()
        npc_desc="%s %s, group %s, whore=%s" % (npc.fname, npc.sname, getattr(npc,'bio_group','?'), getattr(npc,'iswhore',False))
        sys_prompt=PROMPTS["npc_chat"] % gs['fem']
        sys_prompt=sys_prompt + "\nNPC: %s\nPlayer fem %s%%" % (npc_desc, gs['fem'])
        resp=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, user_msg, want_json=False, temp=0.85, max_tokens=300)
        if resp:
            clean=re.sub(r'\[.*?\]','',resp).strip()
            ai_npc_chats[npc_id].append({"role":"assistant","content":clean})
            for stat,d in re.findall(r'\[([A-Z_]+)([+-]\d+)\]', resp):
                if stat=="FEMININITY":
                    try: ai_fem=max(0,min(100,ai_fem+int(d)))
                    except: pass
    jump ai_npc_chat

# DIRTY TALK - теперь с предзагрузкой
label ai_dirty_talk(sex_type="vag", npc=None):
    python:
        # Если есть предзагруженные фразы - используем их мгновенно без ожидания LLM
        if hasattr(store,'ai_dirty_prefetched') and store.ai_dirty_prefetched:
            try:
                phrase=store.ai_dirty_prefetched.pop(0)
                ai_dirty_talk_history.append(phrase)
                renpy.say(None, phrase)
                # Тут же запускаем догрузку следующей фразы в фоне
                def _refill_dirty():
                    try:
                        gs=get_state()
                        npc_name = "%s" % npc.fname if npc else "partner"
                        resp=ai_call(OLLAMA_MODEL_CHAT, PROMPTS["dirty"] % (gs['fem'], sex_type, npc_name), "Need one more dirty phrase for %s, fem %s%%" % (sex_type, gs['fem']), want_json=False, temp=0.9, max_tokens=150)
                        if resp:
                            store.ai_dirty_prefetched.append(resp)
                    except:
                        pass
                import threading
                threading.Thread(target=_refill_dirty).start()
                # Выходим, уже показали фразу без ожидания
            except Exception as e:
                print("Dirty prefetch use err %s" % e)
        else:
            # Фолбек - старое поведение если предзагруженных нет
            gs=get_state()
            npc_name = "%s" % npc.fname if npc else "partner"
            sys_prompt=PROMPTS["dirty"] % (gs['fem'], sex_type, npc_name)
            user_prompt="Sex type %s, fem %s%%, desire %s, NPC %s. Generate dirty talk." % (sex_type, gs['fem'], gs['desire'], npc_name)
            resp=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, user_prompt, want_json=False, temp=0.9, max_tokens=200)
            if resp:
                ai_dirty_talk_history.append(resp)
                renpy.say(None, resp)
            else:
                renpy.say(None, "Ах... ты стонешь, чувствуя как новое тело реагирует")
    return

# DIARY
label ai_diary_gen:
    python:
        gs=get_state()
        last_evt=ai_events[-1]['description'] if ai_events else "обычный день"
        sys_prompt=PROMPTS["diary"] % (last_evt, gs['fem'], gs.get('outfit','unknown'))
        entry=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, "Write diary entry fem %s%%" % gs['fem'], want_json=False, temp=0.8, max_tokens=300)
        if entry:
            ai_diary_entries.append({"day":gs.get('day',0),"text":entry})
            try:
                if hasattr(store,'log'):
                    store.log.assign(entry[:100])
            except: pass
            renpy.notify("Дневник обновлен AI")
    return

screen ai_diary_screen():
    modal True
    # tag menu removed to avoid main menu conflict
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 700 ysize 600 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#1a3a2a" xfill True ysize 50
                text "AI Дневник Саманты" size 18 color "#88ffaa"
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for e in reversed(ai_diary_entries[-20:]):
                        frame:
                            background "#1a2a3a" xfill True
                            vbox:
                                text "День %s" % e['day'] size 11 color "#666"
                                text e['text'] size 14 color "#e0e0ff"

# REPORTS
label ai_report_gen:
    python:
        gs=get_state()
        sys_prompt=PROMPTS["report"] % (gs['fem'], gs['confidence'], gs['corrupt'], gs['location'])
        user_prompt="fem %s%% conf %s corrupt %s loc %s perks %s" % (gs['fem'], gs['confidence'], gs['corrupt'], gs['location'], gs['perks'])
        report=ai_call(OLLAMA_MODEL_JSON, sys_prompt, user_prompt, want_json=False, temp=0.7, max_tokens=400)
        if report:
            ai_reports.append(report)
    return

screen ai_reports_screen():
    modal True
    # tag menu removed to avoid main menu conflict
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 650 ysize 500 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#0a2a4a" xfill True ysize 50
                text "Отчеты Института (AI)" size 18 color "#aaddff"
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for r in reversed(ai_reports[-10:]):
                        frame:
                            background "#1a2330" xfill True
                            text r size 13 color "#cceeff"

label ai_report_view:
    call screen ai_reports_screen
    return

# SHOP
label ai_shop_gen:
    python:
        gs=get_state()
        item_json=ai_call(OLLAMA_MODEL_JSON, PROMPTS["shop_item"], "fem %s%% slutty=%s" % (gs['fem'], gs['corrupt']>30), want_json=True, temp=0.9, max_tokens=300)
        if item_json and 'name' in item_json:
            try:
                ItemClass=getattr(store,'Item',None)
                if ItemClass:
                    new_item=ItemClass(item_json['name'], item_json['desc'], "ai_item_%s" % len(ai_shop_items), type=item_json.get('type','top'), slutty=item_json.get('slutty',True), skirt=item_json.get('skirt',False), clevage=item_json.get('clevage',True), value=item_json.get('value',100))
                    ai_shop_items.append(new_item)
                    if hasattr(store,'shop_list'):
                        store.shop_list.append(new_item)
                    renpy.notify("Новая вещь: %s" % item_json['name'])
            except Exception as e:
                print("shop gen err %s" % e)
    return

# TRAINER
label ai_trainer(t_type="fitness"):
    python:
        gs=get_state()
        sys_prompt=PROMPTS["training"] % (gs['fem'], gs['fitness'], t_type)
        advice=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, "Need %s training, fem %s%%" % (t_type, gs['fem']), want_json=False, temp=0.8, max_tokens=300)
        if advice:
            renpy.say(None, advice)
            if t_type=="fitness":
                try: player.add_fitness(1)
                except: pass
            elif t_type=="confidence":
                try: player.add_conf(2)
                except: pass
    return

# SMS
label ai_sms_gen:
    python:
        gs=get_state()
        try:
            npc_list=getattr(store,'npc_girls',[])
            npc=py_random.choice(npc_list) if npc_list else None
            npc_name="%s %s" % (npc.fname, npc.sname) if npc else "Rose bud"
            npc_group=getattr(npc,'bio_group','whore') if npc else "whore"
        except:
            npc_name="Rose bud"; npc_group="whore"
        sys_prompt=PROMPTS["sms"] % (npc_name, npc_group, gs['location'], gs.get('outfit',''))
        sms=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, "SMS from %s fem %s%%" % (npc_name, gs['fem']), want_json=False, temp=0.85, max_tokens=200)
        if sms:
            ai_sms_inbox.append({"from":npc_name,"text":sms,"day":gs.get('day',0)})
            renpy.notify("SMS от %s" % npc_name)
    return

screen ai_sms_screen():
    modal True
    # tag menu removed to avoid main menu conflict
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 500 ysize 600 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#2a2a4a" xfill True ysize 50
                text "SMS от NPC (AI)" size 18 color "#ff88ff"
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for sms in reversed(ai_sms_inbox[-20:]):
                        frame:
                            background "#1a1a3a" xfill True
                            vbox:
                                text "%s - День %s" % (sms['from'], sms['day']) size 11 color "#888"
                                text sms['text'] size 14 color "#e0e0ff"

# PERKS
label ai_perk_gen:
    python:
        gs=get_state()
        perk_json=ai_call(OLLAMA_MODEL_JSON, PROMPTS["perk"] % (gs['fem'], gs['perks']), "Generate perk fem %s%%" % gs['fem'], want_json=True, temp=0.9, max_tokens=300)
        if perk_json and 'name' in perk_json:
            try:
                PerkClass=getattr(store,'PerkClass',None)
                if PerkClass:
                    new_perk=PerkClass(perk_json['name'], perk_json['desc'], "ai_perk_%s" % len(ai_perks_generated), confidence_add=perk_json.get('add',5) if perk_json.get('type')=='confidence' else 0, desire_add=perk_json.get('add',5) if perk_json.get('type')=='desire' else 0, allure_add=perk_json.get('add',5) if perk_json.get('type')=='allure' else 0)
                    ai_perks_generated.append(new_perk)
                    player.add_perk(new_perk, notif=True)
            except Exception as e:
                print("perk gen %s" % e)
    return

# HUB
screen ai_hub():
    modal True
    # tag menu removed to avoid main menu conflict
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
                text "AI HUB - Все системы | Фем [ai_fem]%" size 20 bold True color "#ff88ff"
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
                        textbutton "SMS inbox" action Call("ai_sms_view") background "#2a1a3a"
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
                        textbutton "Spicy" action Call("ai_spicy_open") background "#3a1a3a"
                    hbox:
                        spacing 8
                        textbutton "Дебаг локаций" action Call("ai_debug_locations") background "#1a1a1a"

label ai_view_quests:
    call screen ai_quests_screen
    return

screen ai_quests_screen():
    modal True
    # tag menu removed to avoid main menu conflict
    zorder 2500
    add Solid("#000000bb")
    frame:
        xalign 0.5 yalign 0.5
        xsize 650 ysize 500 background "#12121a"
        vbox:
            xfill True yfill True
            frame:
                background "#1a3a2a" xfill True ysize 50
                text "Квесты AI" size 18 color "#88ff88"
            viewport:
                scrollbars "vertical" mousewheel True
                vbox:
                    spacing 10
                    for q in reversed(ai_quests):
                        frame:
                            background "#1a2a3a" xfill True
                            text "%s\n%s" % (q.get('title','?'), q.get('desc','')) size 13 color "#ccc"

label ai_sms_view:
    call screen ai_sms_screen
    return

label ai_diary_view:
    call screen ai_diary_screen
    return

label ai_reports_view:
    call screen ai_reports_screen
    return

label ai_spawn_random_npc:
    python:
        npc_data=ai_call(OLLAMA_MODEL_JSON, "Generate NPC JSON: {fname,sname,colour,is_female,iswhore,isslut,bio_group,bio_text}", "New NPC for TheFixer, whore or police or academy", want_json=True, temp=0.9, max_tokens=300)
        if npc_data:
            npc_data['generate_new']=True
            spawn_npc(npc_data)
        else:
            spawn_npc({"generate_new":True,"fname":"Lila","sname":"Fox","is_female":True,"iswhore":True,"bio_group":"whore"})
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
        advice=ai_call(OLLAMA_MODEL_CHAT, sys_prompt, "Advice fem %s%% outfit %s" % (gs['fem'], gs.get('outfit','')), want_json=False, temp=0.8, max_tokens=300)
        if advice:
            renpy.say(None, advice)
    return






# OVERLAY









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
            imagebutton:
                idle Solid("#ff00aa88", xsize=90, ysize=40)
                hover Solid("#ff00aa", xsize=90, ysize=40)
                action Call("ai_hub_open")
                tooltip "AI HUB"
            text "AI HUB" size 11 bold True xalign 0.5 color "#fff"

label ai_hub_open:
    call screen ai_hub
    return

label ai_all_after_load_fix:
    # Фикс конфликта с родным after_load.rpyc TheFixer - переименовано
    $ ai_event_cooldown = 0
    return

# ===== ПРЕФЕТЧ ОПТИМИЗАЦИИ - ПИШЕМ ЗАРАНЕЕ =====
# 1. Автобус: генерим событие для точки назначения пока едешь в автобусе
# 2. Секс: генерим грязные фразы когда секс еще только планируется
# 3. Диалоги: генерим сразу весь диалог а не по 1 реплике
# 4. SMS: генерим заранее и показываем когда время придет

default ai_prefetched_bus = None
default ai_dirty_prefetched = []  # список фраз грязного разговора предзагруженных
default ai_dialogue_prefetched = {}  # {npc_id: full_dialogue_tree}

init python:
    def ai_after_load_callback():
        try:
            if hasattr(store, 'ai_event_cooldown'):
                store.ai_event_cooldown = 0
        except:
            pass
    if hasattr(config, 'after_load_callbacks'):
        config.after_load_callbacks.append(ai_after_load_callback)

    # Хук на walk() - когда игрок едет в автобусе, начинаем генерить событие для места куда едет
    try:
        _orig_walk = getattr(store, 'walk', None)
        if _orig_walk:
            def ai_walk_wrapper(dest, *args, **kwargs):
                # Предзагрузка события для dest пока в автобусе
                try:
                    dest_name = str(dest[0]) if isinstance(dest, list) and dest else str(dest)
                    def _prefetch_bus():
                        try:
                            gs=get_state()
                            # Притворяемся что уже в dest
                            gs['location']=dest_name
                            prompt="BUS TRAVEL: Player currently in bus traveling to %s. Time %s (%s). Fem %s%%, outfit %s. Generate arrival event for %s that will happen RIGHT WHEN BUS ARRIVES, not after. Player is still in bus now, so event should be about bus ride ending or arriving. JSON." % (dest_name, gs['timeofday'], gs['hour'], gs['fem'], gs['outfit'], dest_name)
                            evt=ai_call(OLLAMA_MODEL_JSON, PROMPTS["event"], prompt, want_json=True, temp=0.85, max_tokens=600)
                            if evt:
                                store.ai_prefetched_bus=evt
                                print("Prefetched bus arrival event for %s" % dest_name)
                        except Exception as e:
                            print("Bus prefetch err %s" % e)
                    import threading
                    threading.Thread(target=_prefetch_bus).start()
                except Exception as e:
                    print("walk wrapper err %s" % e)
                return _orig_walk(dest, *args, **kwargs)
            store.walk = ai_walk_wrapper
            print("Hooked walk() for bus prefetch")
    except Exception as e:
        print("Failed to hook walk %s" % e)

    # Хук на секс - генерим грязный разговор заранее когда секс планируется
    try:
        p = getattr(store, 'player', None)
        if p:
            for sex_method_name in ['sex_vag','sex_anal','sex_oral','sex_hand','sex_cum']:
                orig = getattr(p, sex_method_name, None)
                if orig:
                    def make_wrapper(orig_func, mname):
                        def wrapper(*args, **kwargs):
                            # Предзагрузка грязных фраз когда секс только планируется
                            try:
                                def _prefetch_dirty():
                                    try:
                                        gs=get_state()
                                        phrases=[]
                                        for i in range(4):  # 4 фразы на весь секс - начало, середина, кульминация, конец
                                            stage = ["foreplay","penetration","fast","cum"][i] if i<4 else "foreplay"
                                            prompt="Dirty talk for %s stage %s, fem %s%%, desire %s%%, NPC %s. Short Russian phrase, 1 sentence, no stars." % (mname, stage, gs['fem'], gs['desire'], str(args[0])[:50] if args else "partner")
                                            resp=ai_call(OLLAMA_MODEL_CHAT, PROMPTS["dirty"] % (gs['fem'], stage, "partner"), prompt, want_json=False, temp=0.9, max_tokens=150)
                                            if resp:
                                                phrases.append(resp)
                                        store.ai_dirty_prefetched=phrases
                                        print("Prefetched %s dirty phrases: %s" % (mname, len(phrases)))
                                    except Exception as e:
                                        print("Dirty prefetch err %s" % e)
                                import threading
                                threading.Thread(target=_prefetch_dirty).start()
                            except:
                                pass
                            return orig_func(*args, **kwargs)
                        return wrapper
                    setattr(p, sex_method_name, make_wrapper(orig, sex_method_name))
            print("Hooked sex methods for dirty talk prefetch")
    except Exception as e:
        print("Failed to hook sex %s" % e)

    # Хук на NPC чат - генерим сразу весь диалог (3-4 реплики) а не по 1
    # Будет в ai_npc_input - генерим 1 ответ, но также предзагружаем 2 следующих возможных ответа

default ai_prefetched_bus_event_shown = False

label ai_bus_check:
    # Проверяет есть ли предзагруженный ивент для автобуса и показывает его сразу при выходе из автобуса
    if ai_prefetched_bus:
        $ ai_last_event = ai_prefetched_bus
        $ ai_events.append(ai_last_event)
        $ ai_prefetched_bus = None
        call screen ai_event_screen
        return
    return
