from clozer import QuestionVar
import itertools


tpl = """<span class="{} underline">{{1:{}:~%100%{}~%0%*#{}}}</span>"""


def get_ans(key, properties, kwargs, feedback):
    def fget(obj):
        v = getattr(obj, key)
        if isinstance(v, str):
            t = "SHORTANSWER"
        else:
            t = "NUMERICAL"
            if "decimals" in kwargs:
                decimals = kwargs["decimals"]
                v = round(v, decimals)
                v = "{}:{}".format(v, 2*10**-decimals)
        return tpl.format(" ".join(properties), t, v,feedback)
    fget.__name__ = "{}_ANS".format(key)
    return fget


def AnswerVar(*properties, **kwargs):
    class AnswerVar(QuestionVar):
        def __init__(self, fget):
            super().__init__(fget=fget)
            self._feedback = fget.__doc__

        def __set_name__(self, owner, name):
            super().__set_name__(owner, name)
            attrs = [
                get_ans(self._key, properties, kwargs, self._feedback)
            ]
            for f in attrs:
                prop = QuestionVar(f)
                owner.questionvars += [f.__name__]
                setattr(owner, f.__name__, prop)
    return AnswerVar


AnswerVar.OPTIONAL = "optional"
AnswerVar.DECIMAL = "decimal"
AnswerVar.INTEGER = "integer"
AnswerVar.PROBABILITY = "probability"
