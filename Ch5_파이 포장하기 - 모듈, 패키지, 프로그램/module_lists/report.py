def get_description():  # 바로 아래에 docstring이 있음"
    """Return random weather, just like the pros"""

    from random import choice
    possibilities = ["rain", "snow", "sleet", "fog", "sun", "who knows"]

    return choice(possibilities)
