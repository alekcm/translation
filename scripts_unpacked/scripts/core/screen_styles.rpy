define grope_trans = Move((2, -8), (0, 0), .50)
define penetrate_trans1 = Move((0, 0), (20, 0), 2)
define penetrate_trans2 = Move((20, 0), (0, 0), .2)
define moveinoutdissolve = ComposeTransition(penetrate_trans1, before=penetrate_trans2)

style hover_font_style:
    outlines [(2, "#000000")]


screen choice_text(text_desc):
    frame anchor (0.5, 0.5) xalign (0.5) yalign (0.47) ysize (300):
        background None
        text "[text_desc]" size 24 xalign (0.5)

screen wardrobe_text(text_title, text_desc):

    frame anchor (0.0, 0.0) xalign (0.82) yalign (0.095) xsize 330 padding (12,12,12,12):
        background None
        has vbox
        $ text_title = text_title.upper()
        text "[text_title]" size 26 font "BRLNSB.TTF"
        text "[text_desc]" style "hover_font_style" size 22

screen shop_text(text_title, text_cost, text_desc):
    frame anchor (0.0, 0.0) xalign (0.81) yalign (0.095) xsize 330 ysize (20):
        background None
        text "[text_title]" style "hover_font_style" size 25
    frame anchor (0.0, 0.0) xalign (0.36) yalign (0.135) xsize 330 ysize (20):
        background None
        text "£[text_cost]" style "hover_font_style" size 35
    frame anchor (0.0, 0.0) xalign (0.81) yalign (0.16) xsize 330 ysize (300):
        background None
        text "[text_desc]" style "hover_font_style" size 20

screen shop_desc(text_name, text_desc):
    frame anchor (0.0, 0.0) xalign (0.73) yalign (0.095) xsize (450) ysize (20):
        background None
        text "[text_name]" style "hover_font_style" size 50
    frame anchor (0.0, 0.0) xalign (0.73) yalign (0.2) xsize (450) ysize (300):
        background None
        text "[text_desc]" style "hover_font_style" size 25

screen no_money():
    zorder 100



    frame xalign (0.5) yalign (0.5) at text_hov_fadeout:

        text "Not enough money!" size 50

    timer 3.25 action Hide('no_money')

screen drink():
    zorder 100



    frame pos (325, 268) at icon_fadeout:
        background None

        add "beer"

    timer 1.0 action Hide('drink')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
