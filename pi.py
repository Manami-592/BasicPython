text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
import re

words = re.split('[ \n,.]+', text)

#0入るの除く
words = list(filter(None, words))

lengths = map(len, words)

result = "".join(map(str, lengths))
print(result)
