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

BUILD_GTA_VI = (
    (
        (False, False),
        (False, False),
    ),
    (
        (False, True),
        (False, False)
    ),
    (
        (True, False),
        (False, False),
    ),
    (
        (True, True),
        (False, False)
    )
)

ia = RedeNeural((2, 2, 2, 2))
