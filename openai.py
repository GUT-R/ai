from rede_neural import RedeNeural

OR = (
    (
        (False, False),
        (False, False)
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
        (False, False)
    ),
    (
        (True, False),
        (False, False)
    ),
    (
        (False, True),
        (False, False)
    ),
    (
        (True, True),
        (False, True)
    ),
)

BUILD_GTA_VI = (
    (
        (False, False, False),
        (False, False),
    ),
    (
        (True, False, False),
        (True, False),
    ),
    (
        (True, False, True),
        (True, False)
    ),
    (
        (True, True, False),
        (True, False),
    ),
    (
        (True, True, True),
        (True, True)
    )
)

ia = RedeNeural((3, 4, 4, 2))
