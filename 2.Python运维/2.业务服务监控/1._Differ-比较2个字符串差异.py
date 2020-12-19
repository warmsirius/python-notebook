import difflib

text1 = """
a
b
c
d
e
f
g
"""

text2 = """
A
B
C
D
E
F
g
"""

if __name__ == "__main__":
    d = difflib.Differ()
    print("\n".join(d.compare(text1, text2)))
    #
    # - a
    # + A
    #
    # - b
    # + B
    #
    # - c
    # + C
    #
    # - d
    # + D
    #
    # - e
    # + E
    #
    # - f
    # + F
    #
    # g
