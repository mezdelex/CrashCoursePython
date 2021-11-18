"""
Father class module
"""


class Father:
    """
    Father class
    """

    def __init__(self, eyes_color: str, skin_tone: str):
        self._eyes_color = eyes_color
        self._skin_tone = skin_tone

    @property
    def eyes_color(self):
        """
        _eyes_color getter
        Returns:
            str: eyes color
        """
        return self._eyes_color

    @eyes_color.setter
    def eyes_color(self, eyes_color: str):
        self._eyes_color = eyes_color
        return self

    @eyes_color.deleter
    def eyes_color(self):
        del self._eyes_color

    @property
    def skin_tone(self):
        """
        _skin_tone getter
        Returns:
            str: skin tone
        """
        return self._skin_tone

    @skin_tone.setter
    def skin_tone(self, skin_tone: str):
        self._skin_tone = skin_tone

    @skin_tone.deleter
    def skin_tone(self):
        del self._skin_tone
