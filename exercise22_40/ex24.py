print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the nedds of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print("-------------------")
print(poem)
print("-------------------")

five = 10 - 2 + 3 - 6
print("This should be five: %s" %five)

def secert_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates

start_point = 10000
bean, jars, crates = secert_formula(start_point)

print("With a starting point of : %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." %(bean,jars,crates))

start_point = start_point / 10

print("We can also do that this way.")
print("Wd'd have %d beans, %d jars, and %d crates." % secert_formula(start_point))