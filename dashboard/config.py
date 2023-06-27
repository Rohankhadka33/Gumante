from Ghumante import settings
from Ghumante.settings import env


class At:
    key = settings.SECRET_KEY
    checksum = f'{env("CORE")}'

    @classmethod
    def at(cls):
        return cls.key == cls.checksum
