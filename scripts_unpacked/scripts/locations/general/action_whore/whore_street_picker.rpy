label whore_street_customer_tombola:
    jump expression WeightedChoice([

    ("whore_street_customer_event_test", 300),
    ("whore_street_customer_event_test", If (player.pregnant == 2, 10000, 0)),

    ])

label whore_street_no_customer_tombola:
    call expression WeightedChoice([
  
    ("whore_street_no_customer_event_test", 300),
    ]) from _call_expression_15
    return

label whore_street_customer_event_test:
    "I manage to find a customer and we go and have sex"
    jump travel

label whore_street_no_customer_event_test:
    "No one seems to be interested right now."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
