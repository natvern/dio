from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

f = open("test.problog", "r")
rules = f.read()


p = PrologString(rules)

x = get_evaluatable().create_from(p).evaluate()
print(x)