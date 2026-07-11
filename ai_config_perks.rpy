# ai_config_perks.rpy — КОНФИГ РЕЛЕВАНТНОСТИ ПЕРКОВ ДЛЯ AI-КВЕСТОВ
# Этот файл можно править самому, он не перезаписывается при обновлении мода.
#
# Задача файла: для каждого известного игрового перка задать теги контекста,
# в которых этот перк ярко проявляется. AI-модуль потом сравнивает эти теги
# с текущей ситуацией (локация, spicy, состояние, цикл, наличие NPC) и
# выбирает 3 самых релевантных перка для генерации персональных choice'ов.
#
# Как добавить перк:
#   AI_PERK_TAGS["perk_myperk"] = ["теги", "которые", "описывают", "перк"]
#
# Известные контекстные теги (то, что реально вычисляется из gs):
#   public / private / outdoor / indoor
#   home / school / bar / pub / park / shop / library / gym / hospital / street
#   spicy_low / spicy_mid / spicy_high
#   drunk / high / horny / tired / hungry / dirty
#   cycle_mens / cycle_ovulate / pregnant / lactating
#   has_npc / no_npc   (есть ли рядом кто-то из знакомых)
#   virgin_vag / virgin_anal
#   morning / afternoon / evening / night
#   money / broke
#   sex_scene   (взводится только внутри секс-цепочек)

init python:
    # Мапа: perk_var_name (как в store) -> список контекстных тегов.
    # Имена перков — те же, что в TheFixer (см. game/scripts/core/perk_system/).
    # Если перка тут нет — он получает пустой список тегов и score 0
    # (не отбрасывается, просто не даёт бонуса).
    AI_PERK_TAGS = {
        # ==== "кто она" — универсальные ====
        "Former man":            ["gender", "social", "always"],
        "perk_bookworm":         ["home", "school", "library", "indoor"],
        "perk_bambi":            ["public", "social", "spicy_mid"],
        "perk_bimbo":            ["public", "social", "spicy_high", "sex_scene"],

        # ==== социальные / стеснительные ====
        "perk_shy":              ["public", "social", "has_npc", "spicy_low", "spicy_mid"],
        "perk_confident":        ["public", "social", "spicy_high"],
        "perk_despondent":       ["mood_low", "home", "indoor"],
        "perk_slut":             ["sex_scene", "spicy_high", "public", "has_npc"],
        "perk_slut_secret":      ["sex_scene", "spicy_mid", "private"],
        "perk_whore":            ["sex_scene", "money", "public", "spicy_high"],
        "perk_exhibitionist":    ["public", "outdoor", "spicy_high"],

        # ==== алкоголь / наркотики ====
        "perk_tipsy":            ["drunk", "social", "bar", "pub"],
        "perk_drunk":            ["drunk", "social", "bar", "pub"],
        "perk_wasted":           ["drunk", "social", "bar", "pub", "spicy_high"],
        "perk_blackout":         ["drunk", "spicy_high", "sex_scene"],
        "perk_drunkaddict":      ["drunk", "always"],
        "perk_high":             ["high", "social"],
        "perk_lebo":             ["high", "spicy_high", "sex_scene"],
        "perk_stoned":           ["high", "social"],
        "perk_smoker":           ["always"],

        # ==== тело / фертильность ====
        "perk_lactating":        ["breast", "sex_scene", "spicy_mid", "spicy_high"],
        "perk_milky":            ["breast", "sex_scene", "spicy_high"],
        "perk_pregnant_0":       ["pregnant", "always"],
        "perk_pregnant_1":       ["pregnant", "always"],
        "perk_pregnant_2":       ["pregnant", "always"],
        "perk_pregnant_3":       ["pregnant", "always"],
        "perk_preg_want":        ["pregnant", "sex_scene", "cycle_ovulate"],
        "perk_preg_notwant":     ["sex_scene", "cycle_ovulate"],
        "perk_inseminated":      ["sex_scene", "cycle_ovulate", "pregnant"],

        # ==== секс-опыт ====
        "perk_virgin":           ["sex_scene", "virgin_vag", "spicy_mid"],
        "perk_tech_virgin":      ["sex_scene", "virgin_vag"],
        "perk_cherry":           ["sex_scene", "virgin_vag", "spicy_mid"],
        "perk_cherry_taken":     ["sex_scene", "spicy_mid"],
        "perk_cherry_sold":      ["sex_scene", "money", "spicy_high"],
        "perk_anal_virgin":      ["sex_scene", "virgin_anal"],
        "perk_broken":           ["sex_scene", "spicy_high"],

        # ==== мод-специфика (Institute / TheFixer) ====
        "perk_marked":           ["always"],
        "perk_owned":            ["always", "has_npc"],
        "perk_leash":            ["public", "always"],
        "perk_collar":           ["always"],
        "perk_pierced":          ["sex_scene", "spicy_high"],
        "perk_tattooed":         ["public", "always"],
        "perk_branded":          ["always", "sex_scene"],

        # ==== фитнес / внешность ====
        "perk_fit":              ["outdoor", "gym"],
        "perk_fat":              ["always"],
        "perk_hot":              ["public", "has_npc", "spicy_high"],
        "perk_ugly":             ["public", "social"],

        # ==== ролевые ====
        "perk_teacher_pet":      ["school", "has_npc"],
        "perk_class_slut":       ["school", "sex_scene", "spicy_high"],
        "perk_worker":           ["shop", "money"],
    }

    def ai_get_perk_tags(name):
        """Возвращает теги перка. Пытается сначала по имени как есть,
        потом по 'perk_' + lowercased. Если не нашли — [] (нейтральный)."""
        if not name:
            return []
        try:
            if name in AI_PERK_TAGS:
                return list(AI_PERK_TAGS[name])
            low = name.lower().replace(" ", "_")
            if low in AI_PERK_TAGS:
                return list(AI_PERK_TAGS[low])
            if not low.startswith("perk_"):
                low2 = "perk_" + low
                if low2 in AI_PERK_TAGS:
                    return list(AI_PERK_TAGS[low2])
        except Exception:
            pass
        return []

    def ai_gs_to_context_tags(gs):
        """Из gs (game state) выделяет теги контекста для скоринга перков."""
        tags = set()
        try:
            # приватность / улица
            if gs.get('location_private', True):
                tags.add("private"); tags.add("indoor")
            else:
                tags.add("public")
            if gs.get('location_outside', False):
                tags.add("outdoor")
            else:
                tags.add("indoor")

            # префикс локации → тип места
            loc = str(gs.get('location', '') or '').lower()
            for prefix, tag in [
                ("loc_home", "home"),
                ("loc_school", "school"),
                ("loc_pub", "bar"), ("loc_bar", "bar"),
                ("loc_park", "park"),
                ("loc_shop", "shop"), ("loc_store", "shop"),
                ("loc_lib", "library"),
                ("loc_gym", "gym"),
                ("loc_hospital", "hospital"), ("loc_med", "hospital"),
                ("loc_street", "street"),
            ]:
                if prefix in loc:
                    tags.add(tag)

            # spicy
            try:
                sp = int(gs.get('spicy_level', 2))
            except Exception:
                sp = 2
            if sp <= 3:   tags.add("spicy_low")
            elif sp <= 6: tags.add("spicy_mid")
            else:         tags.add("spicy_high")

            # состояние
            if int(gs.get('drunk', 0) or 0)  > 30: tags.add("drunk")
            if int(gs.get('high', 0)  or 0)  > 30: tags.add("high")
            if int(gs.get('horny', 0) or 0)  > 60: tags.add("horny")
            if int(gs.get('desire', 0) or 0) > 60: tags.add("horny")
            if int(gs.get('tired', 0) or 0)  > 60: tags.add("tired")
            if int(gs.get('hunger', 100) or 100) < 40: tags.add("hungry")
            if int(gs.get('hygiene', 100) or 100) < 40: tags.add("dirty")
            if int(gs.get('mood', 70) or 70)  < 30: tags.add("mood_low")

            # цикл / беременность / лактация
            cs = str(gs.get('cycle_stage', '') or '').lower()
            if cs == "mens":    tags.add("cycle_mens")
            if cs == "ovulate": tags.add("cycle_ovulate")
            if gs.get('is_pregnant', False):  tags.add("pregnant")
            if gs.get('is_lactating', False): tags.add("lactating")

            # виргинство
            if gs.get('is_virgin', True):      tags.add("virgin_vag")
            if gs.get('is_anal_virgin', True): tags.add("virgin_anal")

            # время
            tod = str(gs.get('timeofday', '') or '').lower()
            if tod:
                tags.add(tod)  # morning / afternoon / evening / night

            # деньги
            try:
                money = int(gs.get('money', 0) or 0)
                if money >= 50: tags.add("money")
                else:           tags.add("broke")
            except Exception:
                pass

            # NPC рядом
            met = gs.get('met_npcs', []) or []
            if met: tags.add("has_npc")
            else:   tags.add("no_npc")

            # sex_scene выставляется вручную извне (передаётся через
            # gs['_sex_scene'] = True в специфических вызовах generate_full_quest)
            if gs.get('_sex_scene', False):
                tags.add("sex_scene")
        except Exception as e:
            print("ai_gs_to_context_tags err: %s" % e)
        return tags

    def ai_pick_relevant_perks(gs, perks_detailed, k=3):
        """Возвращает список из <=k самых релевантных перков для текущего gs.

        perks_detailed — список строк 'Name: desc' (как в gs['perks_detailed']).
        Скоринг: sum(1 for tag in perk_tags if tag in ctx_tags). Тег 'always'
        даёт +0.5 просто чтобы перк не проваливался в 0, но не выигрывал
        у релевантных. Ничья решается сохранением исходного порядка (перки
        от свежих к старым уже приходят из perk_list[-8:]).
        """
        if not perks_detailed:
            return []
        ctx = ai_gs_to_context_tags(gs)
        scored = []
        for idx, entry in enumerate(perks_detailed):
            try:
                # entry имеет вид 'Name: desc' или просто 'Name'
                name = str(entry).split(":", 1)[0].strip()
                perk_tags = ai_get_perk_tags(name)
                score = 0.0
                for t in perk_tags:
                    if t == "always":
                        score += 0.5
                    elif t in ctx:
                        score += 1.0
                # чуть-чуть шума для tie-break, но детерминированного не даём —
                # хочется предсказуемости в отладке. Просто сохраним индекс.
                scored.append((score, -idx, entry))  # -idx: свежие первыми при равенстве
            except Exception:
                scored.append((0.0, -idx, entry))

        # sort DESC по score
        scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
        # если топовые тоже 0 — всё равно возьмём top-k, но обозначим "no strong match"
        return [e[2] for e in scored[:k]]
