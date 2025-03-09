from const import EnumConst

from const import constantize_module



SOME_NORMAL_VARS = 12

class Links(str, EnumConst):
    GITHUB = "https://github.com/ra101"
    WEB = "https://ra101.dev/"
    EMAIL = "ping@ra101.dev"


constantize_module(__name__)


__all__ = []