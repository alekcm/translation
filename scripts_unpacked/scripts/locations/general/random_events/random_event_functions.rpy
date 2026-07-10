init python:

    def trigger_hucow():
        amount = sum([c.bra == 13, c.pants==16, c.socks==20, c.gloves==6, c.hat==10, acc.choker==5])
        if amount >= 4:
            return amount * 10
        return 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
