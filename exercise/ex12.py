age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print ("So, you're %r old, %r tall and %r heavy." % (
age, height, weight))

# study drill
"""
python -m pydoc input
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
"""




