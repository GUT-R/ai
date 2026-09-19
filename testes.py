from rede_neural import RedeNeural

OR = (
    (
        (False, False),
        (True, False)
    ),
    (
        (True, False),
        (False, True)
    ),
    (
        (False, True),
        (False, True)
    ),
    (
        (True, True),
        (False, True)
    ),
)
AND = (
    (
        (False, False),
        (True, False)
    ),
    (
        (True, False),
        (True, False)
    ),
    (
        (False, True),
        (True, False)
    ),
    (
        (True, True),
        (False, True)
    ),
)
ia = RedeNeural((2, 2, 2, 2))
