init python:

    def resolver(match):
        expression = match.group(1)
        parts = expression.split(".")
        current = globals()[parts[0]]
        
        for part in parts[1:]:
            
            current = getattr(current, part)
        if parts[-1:] == "name" and not isinstance(current,str):
            current = getattr(current, "name")
        else:
            current = str(current)
        return str(current)

    def resolvePlaceholders(string):
        return re.sub(r"\[([^\]]+)\]", resolver, string)

    def slurCharacter(character, amount):
        if amount <= numgen(0,100):
            return character
        elif character in "aeiou":
            return numgen(1,3) * character
        elif character in "AEIOU":
            return character + character.lower() * numgen(1,2)
        elif character in "s":
            return character + "h" * numgen(1,)
        return character

    def slurWord(word, amount):
        if word.startswith("{"):
            return word
        if word.startswith("["):
            word = globals()[word[1:-1]]
        return "".join([slurCharacter(character, amount) for character in word])

    def slur(string, amount):
        string = resolvePlaceholders(string)
        return " ".join([slurWord(word, amount) for word in string.split(" ")])
        return string

    def bimbofy(string, amount):
        string = resolvePlaceholders(string)
        replacements = [
            [", ", ", like, "],
            ["I'm ", "I'm, like, "],
            ["I really", "I totes"],
            ["totally", "totes"], ["Totally", "Totes"],
            ["girl", "chick"], ["Girl", "Chick"],
            ["kind of", "kinda"], ["Kind of", "Kinda"],
            ["beautiful", "hawt"], ["Beautiful", "Hawt"],
            ["lovely", "adorbs"], ["Lovely", "Adorbs"],
            ["wonderful", "brill"], ["Wonderful", "Brill"],
            ["damn", "oh my god"], ["Damn", "Oh my god"],
            ["darn", "oh my god"], ["Darn", "Oh my god"],
            ["because", "'cos"], ["Because", "'Cos"],
            ["don't know", "dunno"], ["Don't know", "Dunno"],
            ["!", ", like oh my God!!"],
            ["probably", "probs"], ["Probably", "Probs"],
            ["so ", "sooo "], ["So ", "So like, "],
            ["about", "bout"], ["About", "Bout"],
            ["okay", "'kay"], ["Okay", "'Kay"],
        ]
        
        for replacement in replacements:
            if amount < numgen(0,100):
                string = string.replace(replacement[0], replacement[1])
        string = resolvePlaceholders(string)
        return string

    def bambify(string):
        string = resolvePlaceholders(string)
        
        replacements = {
            "shit": "poop",
            "fuck": "eff",
            "cunt": "fanny",
            "arse": "bum",
            "ass": "bum",
            "damn": "darn",
            "hell": "heck",
        }
        
        def replace(match):
            word = match.group(0)
            lower = word.lower()
            replacement = replacements[lower]
            
            
            if word[0].isupper():
                replacement = replacement.capitalize()
            
            return replacement
        
        pattern = r'\b(' + '|'.join(re.escape(k) for k in replacements.keys()) + r')\b'
        string = re.sub(pattern, replace, string, flags=re.IGNORECASE)
        
        string = resolvePlaceholders(string)
        return string

    def dialogue_edit(string):
        if player.has_perk(perk_bambi):
            string = bambify(string)
        if player.has_perk(perk_bimbo):
            string = bimbofy(string, percent_scaler(5, 40, player.int))
        string = slur(string, percent_scaler(40, 150, player.drunk))
        return string
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
