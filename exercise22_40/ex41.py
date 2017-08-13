""""
def outer_function():
    global a
    a =20
    def inner_function():
        global a
        a = 30
        print("inner a = ",a)

    inner_function()
    print("outer a = ",a)

a = 10
outer_function()
print("a = ",a)
"""

"""
class ComplexNumber:
    def __init__(self, r= 0, i =0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

c1 = ComplexNumber(2,3)
c1.getData()

c2 = ComplexNumber(5)
c2.attr = 10
print((c2.real, c2.imag, c2.attr))
"""
"""
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input("Enter side" + str(i+1)+":")) for i in range(self.n)]

    def dispSide(self):
        for i in range(self.n):
            print("Side", i+1, "is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle is %0.2f"%area)

t = Triangle()

t.inputSides()
t.dispSide()
t.findArea()
"""
"""
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        #return "({0},{2})".format(self.x,self.y)
        return "({0},{1})".format(self.x,self.y)

p1 = Point(2,3)
print(p1)
"""

"""
class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",\
"I don't want to get sued",\
"So I'll stop right there"])   

bulls_on_parade = Song(["They rally around the family",\
"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
"""

import random
from urllib import request
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has-a function named *** thats takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instant of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***' ":
        "From *** get the *** attribute and set it to '***'. "
}

PHRASE_FIRST = False

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

for word in request.urlopen(WORD_URL).readlines():
    word = str(word,encoding = 'utf-8')
    WORDS.append(word.strip())


def convert(snippet,phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(','.join(random.sample(WORDS,param_names)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%",word,1)
        for word in other_names:
            result = result.replace("***",word,1)
        for word in param_names:
            result = result.replace("@@@",word,1)
        results.append(result)
    return results

try:
    while True:
        snippets = PHRASES.keys()
        #random.shuffle(snippets)

        for snippet in snippets:
            pharse = PHRASES[snippet]
            question, answer = convert(snippet,pharse)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)
            input(">")
            print("ANSWER: %s\n\n"%answer)
except  EOFError:
    print("\bBye")








