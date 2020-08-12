#TODO
class detail
https://docs.python.org/3/reference/datamodel.html?highlight=__new__#object.__new__

metaclass,..
https://docs.python.org/3/reference/datamodel.html#metaclasses
https://pyvideo.org/pycon-us-2016/dustin-ingram-what-is-and-what-can-be-an-exploration-from-type-to-metaclasses-pycon-2016.html
https://pyvideo.org/kiwi-pycon-2019/im-so-meta-even-this-acronym.html
__build_class__
https://www.youtube.com/watch?v=cKPlPJyQrt4&t=2211s

yield from generator
coroutine
http://dabeaz.com/coroutines/
https://docs.python.org/3/reference/expressions.html#yieldexpr


hashable
https://docs.python.org/3/reference/datamodel.html#object.__hash__

print to sys.stderr

virtual subclassing

abc

weakref

logging

unit test

strftime strptime
datetime https://realpython.com/python-datetime/

string formatting format

import, packages (notes.py 159)
https://docs.python.org/3/reference/datamodel.html modules section

files. read one line, read all, read binary


type hint + type check

https://docs.python.org/3/howto/index.html


# python cookbook (beazly), python essential references
# fluent python Luciano Ramalho

https://medium.com/instamojo-matters/become-a-pdb-power-user-e3fc4e2774b2g

https://pyvideo.org/index.html


# exercises
"""
https://www.hackerrank.com/dashboard
http://www.practicepython.org/
https://www.codewars.com?language=python
https://edabit.com/challenges/python3
https://py.checkio.org/
http://www.pythonchallenge.com/
https://codechalleng.es/
""" 


# https://gto76.github.io/python-cheatsheet/

# pythontutor.com to viuzalize execution


the term protocol coming from smalltalk is also used in python. 
It means a set of methods with a certain signature (+ contract  on behaviour)

# venv
python -m venv venv
. venv/bin/activate

## ipython within a  venv
pip install ikernel
ipython kernel install --user --name=<projectname>

# linux, install packages in local user
pip --user package_name
(alternative : sudo the package)
requires adding:  
PATH=$PATH:/home/tburette/.local/bin

dir()
help()
vars()

running a file is a two step process
1) import (top to bottom, create the module)
2) run
decorators are run at step 1


##############################################################################
# function

callable() determines if can be called as a function
    eg.: function, method, class, object with __call__

can read from a global/nonlocal variable
need to use global/nonlocal to write to it
a write anywhere to a variable means the variable is local (unless global/nonlocal is used)
a variable shadowing a variable : a local scope variable with the same name as a variable in an outer scope


## parameters
function parameters:  
def f(pos_only, /, pos_or_key, *, kw_only, **kwargs)
def f(pos_only, /, pos_or_key, *args, kw_only, **kwargs)
types of parameters:
positional-or-keyword (with eventually a default value)
def f(a)
def f(a=1)
def f(..., /, a, *, ...)

positional-only
def f(pos, /)

keyword-only
def f(*args, kw_only) # *args same role as *. Can't have both
def f(*, kw_only)

variable positional
def f(*args)
variable keyword
def f(**kwargs) # nothing after
they are filled with everything that didn't fit in the variables


/ syntax new in 3.8
origin : cpython sometimes working with positional parameter
that was put in the python documentation as id(obj ,/)
it became a language feature

default values
a=1
parameters (except for variable) can also have default value
the default values are stored in __defaults__ of the function

parameter with default value != keyword parameter:
# a is a pos-or-keyword with a default
# b is a keyword-only with no default
def foo(a=0, *, b): 
    pass

## calling and arguments
keyword argument
argument with an identifier
foo(a=1)

positional arguments
no name
foo(1)

# unpacking arguments, flatten, aka _splat_ :
def right(y, x):
    ...
pos=(2, 0)
right(*pos)

def foo(x, y):
    ...
d={'x'=1, 'y'=2}
foo(**d)


# positional argument and chaining
## zero one or more
def foo(*elements, ...):
    for e in elements:
        ...
foo()
foo(1)
foo(1, 2)


## arguments are list
def foo(elements, *other_elements, ...):
    all_elements = chain(elements, *other_elements)
    for e in all_elements:
        ...

#how python assigns the arguments to the parameters
1) each parameter is a slot to be filled with a value
2) take every positional argument and 
   put it in a positional/pos-or-keyword paremeter slot (left to right)
   (error if too many)
3) for every keyword argument : set the slot of the corresponding name
    (error if already filled)
4) if unfilled slots whose argument have a default value
5) error if unfilled slots
6) if extra
    and *args **kwargs : fill those
    and no * ** : error


all parameters must have a value, 
no extra unless *args or **kwargs



##############################################################################
# Functional

map is a class
map is lazy

use list comprehension when there is more than just a function and a sequence

as many arguments passed to the function as there are sequences
map(single_arg, seq)
map(two_args, seq, seq2)
map(three_args, seq, seq2, seq3)

filter
is a class
is lazy
filter(predicate, sequence)
filter(None, sequence)
    return elements that are true

prefer list comprehension
[x for x in sequence if predicate(x)]

reduce
aggregate function
fold left

from functools import reduce
reduce(lambda a, b: a+b, [1, 2, 3], 0)
reduce(new_state, events, initial_state)

from itertools import chain
chain(*list_of_list) # flatten

recursion
no tail call optimisation in CPython
import sys
sys.getrecursionlimit()
sys.setrecursionlimit(100)



##############################################################################
#misc

#range
iterable not iterator (can use multiple times)
can use indexing, slicing in and len:
    range(10)[::-1]
    range(10)[-2]
    x in range(10)
    len(range(10)


# nested list comprehension
[.. for x in .. for y in ..]
equivalent to
for x in ..:
    for y in ..:
        ..
BUT
[ [.. for y in ..] for x in ..]
equivalent to
for x in..:
    for y in.. # and this, returns a single list


# condition
chaining
a < b == c
like doing a < b and b == c
no (direct) comparison between a and c

comparing sequence in lexicographical order
(1, 2, 3) < (1, 2, 4)
works recursively
[1, (2, 3)] < [1, (3, 3)]


# packing
(zero, (f,*irst),*rest)= ['zero', 'First', 'rest', 'here']
assert zero == 'zero' 
    and f=='F' 
    and irst = ['i', 'r', 's', 't'] 
    and rest = ['rest', 'here']

seq=range(10)
[*seq, 10, *reversed(seq)]
[*seq[1:], seq[0]] # shift rotate left



# Type hinting
Intro : https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
Static type checker : mypy
import typing



# list
modify list (in place)
sequence[::] = [value for value in sequence if value != x]
generally better to create a copy

list_.count(elem)

enumerate(..., starting_at)

# set
set()
frozenset()


# str

("a"
"single"
"string")

s.swapcase()
s.count(...)
s.ljust(width, fillchar) s.center s.rjust

# dict
mydict.get('key', 'default value')

... Ellipsis

##############################################################################
#documentation

# docstring
# https://github.com/google/styleguide/blob/gh-pages/pyguide.md
# becomes the __doc__ attribute of the object
def foo(arg1, arg2):
    """Summary in one line ended with a dot.
    
    More detailed description
    goes
    here.
    
    Args:
        arg1: description
            here.
        *arg2: variable length argument
    
    Returns:
        Description here.
    
    Yields:
        Instead of Returns for generators
    
    Raises:
        IOError: decription here
    """

class Class():
    """Summary here.
    
    Longer description here
    
    Attributes:
        xxx: description
        yyy: description
    """


# linter
(big names : flake8 and pylint)
pip install flake8

flake8 .

ignore error (space after # is important)
whole file
    # flake8: noqa
one line
    # noqa


black will automatically format the text


##############################################################################
# module, package, dependencies

# module
import x as y
from x import y as z

don't forget to comment the module """ """

## import
See https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html    

## search path
when importing : 
* search builtin modules
  sys.builtin_module_names
* in sys.path
  sys.path will contain:
      directory of the input script (or current dir if repl)
      PYTHONPATH
      defaults

pkgutil.iter_modules(path_or_none)
    list all modules importable from path (if no args)
    or modules available in given path(s)

dir(module) names defined by a module
    without a parameter : same as locals()
    assert dir() == locals()

__builtins__ = 
    import builtins
    assert __builtins__ == builtins
    not to be mixed up with the sys.builtin_module_names


## packages
A folder that can contain modules.
Is itself a module
(namespace package = package without __init__, after the import the namespace package is just a package, the only difference is the find/__path__ setting)

if there is a variable in __init__ with the same name as a module:
    with from .. import .. : will references the variable
    with import ........   : will reference the module (full name to access)


__all__ in __init__.py
    useful in __init__ of package only
    optional
    change what is imported when using import * (vars and modules)
    can speed things up if the directory contains a lot of files
    specify the public API. If present it is a sign that public has been thought about for this module --> should have _vars set and be importable with import *

if __all__ is not defined on a package, doing from .... import * will only but in the global variables the modules that have already been loaded!
The behaviour of import * depends on previous imports
    
absolute import : 
    from package.blah import foo
    "there is nothing wrong with using from Package import specific_submodule! In fact, this is the recommended notation"
    PEP8: "Relative imports for intra-package imports are highly discouraged. "
relative import:
    from . import echo
    from .. import formats
    from ..filters import equalizer
    relative imports do not work when a module is run from the console (__name__ == '__main__'). (Because relative imports are based on the __name__ (__path__?) of the current module)


__pycache__
one set of file per version of PYTHONPATH
does not speed up execution, only speeds up the loading


import builtins VS sys


##############################################################################
#string



f''
{x:_^5}
{x!r} {x!s} repr str


[symbole de padding][alignement][signe][largeur][groupage][.précision][type]
:< ^ > = align

+ - " " sign

8 minimal width

_ , grouping

.2 precision for float, truncating for string

type:
:x hexa
:X uppercase
:o octal
:b binary

# formattage : 
# https://he-arc.github.io/livre-python/fstrings/index.html
# https://pyformat.info/

''.format()
'{} {}'.format(1, 2)
'{0} {1}'.format(1, 2)
'{x}'.format(x=1)
'{0[0]}'.format([1]) 
'{a} {b}'.format(**{'a': 1, 'b': 2})
'{var1}'.format(**vars())


pprint.pformat like pprint but returns a string instead of printing



##############################################################################
#  Files
open('x', 'r+') read/write
open('x', 'a')  append
open('x', 'rb') binary mode
with open(...) as f:
    ....


##############################################################################
# Exceptions
list exceptions:
[b for b in dir(__builtin__) if 'Error' in b or 'Exception' in b]
hierarchy?
See file:///home/tburette/dev/python/python-3.7.2rc1-docs-html/library/exceptions.html#exception-hierarchy
BaseException
    SystemExit
    KeyboardInterrupt
    Exception
        ArithmeticError
            ZeroDivisionError
            OverflowError
            FloatingPointError  
        SyntaxError
        ImportError
        AssertionError
        NameError               does_not_exist
        AttributeError          var.does_not_exist
        TypeError
        ValueError
        LookupError
            IndexError
            KeyError
        StopIteration


try:
    pass
except (RuntimeError, TypeError): #can be a base of the exception
    pass
except FooException:
    pass
except:
    pass # wildcard (bad)
else:
    pass # no exception raised
    # useful to prevent an exception in the else code to be accidentally caught in an except
finally:
    pass # always executed
    # can cancel the exception with a break or a return
    # overrides a return in the try

## finally 
break/return can swallow an exception
def test_except():
    """will return 0"""
    try:
        2/0 # or return 0
    finally:
        return 0 # or break

finally can not run in the case of a generator function:
def foo():
    try:
        yield 0
    finally:
        # if yield is performed and execution is not resumed
        # finally won't be run.
        # it can be run when the GC collects the generator object
        print('')


raise X()
or
raise X (shorthand)

raise  
    to re-raise

re raise exception
try:
    ...
except ...:
    raise # nothing else!



## exception argument (= value)
the exception object contains an .args field containing all the args.
try:
    raise NameError(arg1, arg2, arg3)
except NameError as inst:
    inst.args # = (arg1, arg2, arg3)

print(an_exception) str(exc) #will print args

(Custom) subclass can change its content
class TestError(Exception):
    def __init__(self, args):
        super().__init__()# don't pass anything. .args will be empty

by default args is set even if init does nothing
    def __init__(self, args):
        pass
this is because __new__ sets args



## custom exception
End with Error
must be derived (directly or indirectly) from Exception (technically BaseException but it is not recommanded)
If multiples exceptions for a module : create a base exception class for the module to b inherited by all (actual) module exceptions

class MyErro(Exception):
    pass

class MyError(Exception):
    def __init__(self, message, other_data):
        super().__init__(message)# exc.args will only have message in it
        self.other_data = other_data

can inherit from multiples exceptions : can catch any class in an except:
class MissingSchema(RequestionException, ValueError)

## Traceback
__traceback__
The stack

## chaining

__context__
implicit exception context
__context__ is the exception that was being handled when the current exception was raised
always automatically set when raise a new exception in an except or finally
if raise .. from xx is used 
    __context__ is still the handled exception (and NOT xx) even though it is 
    xx that will be printed in the traceback
"During handling of the above exception, another exception occurred:"
meaning : during an exception handling, I failed and got another exception

to mask/replace manually __context__:
__cause__
explicit exception context
__cause__ is the exception that was manually set as the exception causing this one
Overrides context in the traceback. __context__ still set but not shown
It is set manually through the use of
    raise xxx from cause_exception
"The above exception was the direct cause of the following exception"
meaning : during an exception handling, I converted the exception in somthing else but here is the underlying error

    raise xxx from None
still fill __context__ but the context exception will not be displayed in tracebacks, only xxx.
Tracebacks will only show xxx starting from here and not the __context__

## str repr
str(exc) only prints the args
repr(exc) prints ExceptionName(args)

## logging
logging.exception("...")
logging.info("...", exc_info=True)




##############################################################################
# class OO


# Scope and namespace
https://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html
There are four namespaces :

namespaces (searched in order) : 
L local           locals()
E enclosed (zero, one or more)     (nonlocal )
G module globals  globals()       (global )
B builtin                         (__builtin__)

locals()
globals()

By default can read from outer scope but write only to local one (and shadows the outer one). To write : must use nonlocal, global

consequence : import xxx inside a function only has an effect inside the function. xxx will be a new attribute of the function scope

can declare a global xxx for a name that does not exist yet in the global scope and by writing a value to it, creating it in the global scope

CANNOT declare a nonlocal xxx for a name that does not exist in an enclosing scope (because : which enclosed namespace to choose where to put the new variable?)

loops use existing scope and leave their variables behind
x=1
for x in range(5):
    pass
assert x == 4
BUT list comprehension do not:
x=1
[x for x in range(9)]
assert x == 1

python has no (local) variable declaration
to decide what x corresponds to (which namespace) : 
    if there is a write in the function then it is assumed 
    to be a local variable (unless there is a nonlocal/global statement)
x = 0
def inc():
    x += 1 #UnboundLocalError
inc()

x = 0
def inc():
    print(x) #UnboundLocalError
    if False:
        x = 1 
inc()

# closure
a function with open binding (free variables) that have been closed by the lexical environment resulting in a closed expression
a function + an environment. Env =  list of bindings between (free) variable names and a certain data coming from the lexical environment
(this is lexical scope, there is another way : dynamic scope where the binding is performed during call by looking at the call environment )
a function with free variable only becomes a closure when it has been evaluated and the binding have been made

classic trap:
def functions_maker(n):
    # within the lambda x is a free variable
    # a closure is created  with the binding to x
    # but x is the same variable for all the iterations of the loop
    # hence the value of x in every lambda is the final value
    return [ lambda val: x*val for x in range(n)]



# Class

There is a namespace (scope) for a class
Creation of a class : The code indented inside the class definition is executed just like a module, in the context of the class namespace.

'data attributes' means instance variables
'method attribute' means method of instances
'class attribute' means class level attribute (variable)


self is the same object as the one returned from the constructor
__dict__ on the instance contains the namespace (???)
inst.method is not Class.method (bound method vs a function)
inst.method() ~= Class.method(inst) (thanks to descriptor)
a new instance method object (bound method) is created each time 
the method attribute is accessed   my_obj.method

when getting/setting/deleting an attribute, the attribute of an object is 
    first searched  in the instance's __dict__ then in the class, superclass,...
    (not strictly true : if there is a descriptor in the class it will use it instead of looking in the object's __dict__)

assert inst.method.__self__ is inst
assert inst.method.__func__ is inst.__class__.method

In a method, MUST use self.x or ClassName.x to access attribute
otherwise x will be considered a local or global variable (like in any function)

When a non-data attribute of an instance is referenced, the instance’s class is searched:
class Foo:
    x=1
    def foo(self):
        print(self.x) # 1
That is how obj.method() works (method is in the scope of the class, not obj)


Can use class like a dict:
    class Foo:
        pass
    f = Foo()
    f.x = ..
    f.y = ...

So we can have objects of the same class with different attributes (bad idea!)

can use duck typing. E.g.: pass an object with a read method


id(obj) of an object. Unique (among objects alive), doesn't change

type(obj) type of object (itself an object)
type(inst) is inst.__class__
also used to create new classes type(name, bases, dict_)
type is also the (default) metaclass


## init
multiple init ?
- use (named) arguments
- provide alternative arguments
  @classmethod
  from_xxx(cls, ...):
    ...
    # cls and not ClassName in case this class is subclassed
    return cls(...) # !!! 

## inheritance

Calling the parent
    super().method_name(arguments)
    is equal to BaseClassName.method_name(self, arguments)

isinstance(obj, type)
issubclass(type, other_type)


super().field_or_method
used to be : super(SubClass, self)

### multiple inheritance

find attribute (mro) : 
    a class appear before its parents, the parents appear in order of declaration
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

## private
_
convention _ is private

__
name mangling us useful to prevent clash in name (parent member will not collide with child)
Ensures that self.__foo() will call our foo and foo of a subclass
(technically the child can override and users can call...)
__spam --> _ClassName__spam
this affects getattr, setattr, delattr

if we want a method that can be overriden by subclass
but we want to use our definition only internally even if there is a subclass:
    class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable) # will always use our version

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

    def something(self):
        self.__update() # calls our
        self.update() # calls subclass version (if exists)

## dunder
https://docs.python.org/3/reference/datamodel.html#special-method-names



### __iter__, __next__
for, in,...  call __iter__
to be an iterable: 
    has __iter__()
    the object returned by __iter__ has a __next__
to be an iterator:
    has a __next__ that returns value until it (always) raise StopIterator 
    has an __iter__ which returns self

GOTCHA 0
iterator : only one pass and then it is exhausted (forever)

GOTCHA 1
iterable : depending on implementation an iterable may only be iterated once
typically the case with self-iterator (has an iter that returns self and next is implementd)
eg.: Foo has an __iter__ that return self with __next__ that store iteration advance in self
x = Foo()
for _ in range(2):
    for y in x: # will only run the first time :(
        print(y)

__iter__ and no __next__ -> good indication that it can be iterated upon multiple times

better to have iterator returning new iterable each time if possible (eg. with a generator method)
exception : io.StringIO because it emulates a file (file EOF : don't start over)

Using a generator as the __iter__ implementation:
class Fib:
    def __init__(self):
        # bad ! better to keep variables (prev, cur) local to __iter__ so that
        # iter can be called multiple times, multiple uses at the same time
        self.prev = 0
        self.cur = 1
    
    # since it is a generator function, when called it returns
    # a generator that can be iterated upon with __next__
    def __iter__(self):
        while True:
            yield self.prev + self.cur
            (self.prev, self.cur) = (self.cur, self.prev + self.cur)

GOTCHA 2
object change while being iterated upon

GOTCHA 3
can't reverse, can't slice, 

GOTCHA 4
can't get len()
always True

GOTCHA 5
must be careful weither we accept an iterator *or* an iterable
# no problem
def twice ( seq ):
    for x in seq :
        yield x
        yield x

def every_other(gen):
    for x in gen: #1
        yield x
        # will fail if gen is an iterable (no __next__ in protocol)
        # and no access to the iterator created at #1
        next(gen) 

## property
class C:
    def getx:pass
    def setx:pass
    def delx:pass

    prop = property(getx, setx, delx)

class C:
    ...
    @property # trick : only the first (getx) arg will be passed!
    def x(self):
        pass # getter

    @x.setter
    def x(self, value):
        ...
    @x.deleter
    def x(self):
        ... 

## class method
class level function
useful for custom constructor (from_xxx)
class C:
    @classmethod
    def method(cls):
        pass

C().method()
C.method()

## static method
function that happens to be attached in a class
why? this is where people will look for code. "Put related code in the toolbox"
class C:
    @staticmethod
    def method():
        pass

C().method()
C.method()

## __slots__
a string, iterable (of strings)
instead of dict, pointer for attributes
__dict__ __weakref__ won't be created
slots attributes implemented using descriptors
saves memory
side effect : can't add attributes
if a superclass has no __slots__ : there wil be a __dict__
if a subclass has no __slots__ and it is instanciated : there wil be a __dict__


## Python class gotchas
# from Luciano Ramalho - Pythonic Objects: idiomatic OOP in Python - PyCon 2019
# https://www.youtube.com/watch?v=mUu_4k6a5-I&feature=youtu.be
class Foo:
    def __init__(self, passengers):
        #bad : from now on, a change inside this object impacts 
        # passengers of the caller and vice-versa
        self.passengers = passengers
        #better, no hidden dependency
        self.passengers = list(passengers)

    class_attribute = 0
    def ...(self):
        #change a class attribute?
        #error, will set a variable in the self object
        self.class_attribute = 1
        #ok
        Foo.class_atribute = 1

class A:
    a=10
    def foo(self):
        # read the value from the class attribute 
        # but set in the self object!
        # reason : read from class (since 'a' not in the object) 
        #          but write locally
        # That is why when we want to write to a class attribute
        # we must use Class.Class_attribute and not self
        self.a += 1
a = A()
a.foo()
A.a, a.a # (10, 11) !

native types do not always call method of subclass when inherited
(non virtual methds)
?

## metaclass
a class is an object, the type of that object is a metaclass
a class is a callable that returns objects
the metaclass is callable and returns the class. 
The class block is syntactic sugar for calling the metaclass (after executing the class block to fill the bindings)
using the class syntax, metaclass let you make stuff that are not class
    enum.Enum, django model, the value 7, ...

when inheriting from a class : superclass might actually be using a metaclass
type is the default metaclass of classes

if possible use class decorator instead

#can define metaclass as function or class
def my_metaclass(name, bases, d):
    return 7

class Xxx("hello", "world", metaclass=abc.ABCMeta):
    foo='bar'
assert Xxx == 7
# name = 'Xxx'
# bases = ('hello', 'world')
# d = {'foo': 'bar', '__module__': '__main__', '__qualname__': 'JustSeven', '__metaclass__': <function my_metaclass at 0x7f7926bb8290>}

class Meta(type):
    def __new__(cls, name, bases, dict_):
        return super().__new__(cls, name, bases, dict_)
    def __init__(cls, name, bases, dict_):
        cls.attr = 100
    pass

class Xxx(metaclass=Meta):
    pass

## dynamic/manual class creation


def __init__(self, numerator, denumerator):    
def __mul__(self, other):
def print_fraction(self):

attributes = {
    '__init__' : __init__,
    '__mul__': __mul__,
    'print_fraction':print_fraction}

Fraction = type('Fraction', (object,), attributes)

f = Fraction(2, 3)
f.print_fraction()

Use of dynamic class creation :
create a class allowing operations defined in a json describing remote calls

# Decorators
It's a form of higher order programming
same idea as the gof decorator pattern

import functools
def decorator(func):
    # wraps: make the decorated function look like the original
    # copy dunders : name, doc, annotation, module, qualname, dict (?)
    # adds a __wrapped__
    @functools.wraps(func)
    def decorator_wrapper(*args, **kwargs)
        return func(*args, **kwargs)
    return decorator_wrapper

@decorator
def foo():
    pass

A decorator can
    return the original function (example decorator).
    prevent the execution of the function.
    return a new function that uses the original function

A decorator can work on the methods of a class
class C:
    @time
    def __init__(self,...):
        pass


running a file is a two step process
1) import (top to bottom, create the module)
2) run
decorators are run at step 1 (and not at first call or something like that)
decorator is executed during the import phase


A decorator can work on a class itself
(alternative to mess with metaclass)

def cls_decorator(cls):
    #...
    return cls

@cls_decorator
class Foo:
    pass

Decorator with argument
The job of the outer function is to simply return a decorator function 
(ie. a function that takes a function and returns one)
the value returned by the expression after the @ (@xxx @xxx())
must be a function that takes one param : a function, and returns a function
def repeat(num_times):
    def decorator_repeat(func):
        def repeat_wrapper(*args, **kwargs):
            for _ in num_times:
                value = func(*args, **kwargs)
            return value
        return repeat_wrapper
    return decorator_repeat

#decorator with or without argument
#if used with no args : func will be given, otherwise it is None
def repeat(func=None, times=2):
    #a decorator function 
    def repeat_decorator(func):
        @functools.wraps(func)
        def repeat_wrapper(*args, **kwargs):
            for _ in range(times):
                ret = func(*args, **kwargs)
            return ret
        return repeat_wrapper
    
    if func is None:
        #decorator with arguments
        return repeat_decorator
    else:
        #decorator with no argument
        return repeat_decorator(func)
@repeat
@repeat(times=2)


Class as decorator
useful to hold state in  the decorator
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)  

class CountCallsWithArgs:
    def __init__(self, options):
        self.options = options
        self.num_calls = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sel.num_calls += 1
            print(f"Call {self.num_calls} of {func.__name__!r}")
            return func(*args, **kwargs)

advantage can change behaviour during RuntimeError
class limit...
@limit(size=10)
...
later on:
limit.size = 2

inconvenient : may not work for methods
class X:
    # actually decorated the (unbound) function
    The __call__ of the class decorator will not pass self
    @class_decorator 
    def method(self):
        pass
can fix by implemening the __get__ of the descriptor protocol:
def __get__ ( self, obj_self, objtype ):
    return functools.partial(self.__call__, obj_self)

a decorator can be defined in a module, use globals/code/data from that module
and be used in another module
-> when called the decorator function can modify data/call in its home module

Builtin decorators:
@property
@classmethod
@staticmethod
@functools.wraps
@functools.singledispatch
@functools.total_ordering
@functools.lru_cache


Use of decorator :
registration decorator (put the decorated function in a registry)
temporarily redirect sys.Stdout to capture print()
access control





## Descriptors
# https://nbviewer.jupyter.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb
# https://docs.python.org/3/howto/descriptor.html
Repeating same code across properties? descriptor is a good idea
a class with __get__ __set__ __delete__
set a (class-level) attribute of a class to an instance of that class
class Foo:
    attr = ADescriptor()
result : get/set/del to that attribute will go through the dunder of the descriptor instance instead of directly to the data attribute of the dict
without a __set__, __get__, __delete__ will never be called
__set_name__ to know when descriptor associated with a class

!the descriptor is class level : it is shared by all the instances
if we want value for each instance : store it in the instance or in a dict in the descriptor

# simple, pass storage field name manually
class NonBlank:
    def __init__(self, storage_name):
        # could use instance.__dict__ to avoid the underscore
        self.storage_name = '_' + storage_name

    def __get__(self, instance, owner):
        # ...
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value == '':
            raise ValueError()
        setattr(instance, self.storage_name, value)

class Foo:
    name = NonBlank('name') # duplication of name :(

#different version 
# + doesn't require to duplicate the name of the attribute:
# - the name of the field in the objects that will actually contain the value
#   will be obfuscated : my_object.NonBlank_0
class NonBlank:
    field_count = 0
    def __init__(self):
        self.storage_name = self.__class + '_' + self.__class__.field_count
        field_count += 1
    
    def __get__(self, instance, owner):
        if instance is None:
            # instance is none when accessing through the class : Foo.name
            return self
        else:
            return getattr(instance, self.storage_name)

# class decorator version
# + no duplication and readable attribute
# - must remember to put the decorator
class NonBlank:
    def __set__(self, instance, value):
        # no init, self.storage_name set for us by the decorator
        setattr(instance, self.storage_name, value)

def named_fields(cls):
    for name, attr in cls.__dict__.items():
        if isinstance(attr, NonBlank):
            attr.storage_name = name
    return cls

@named_fields
class Foo:
    name = NonBlank()

# metaclass version
# https://youtu.be/81S01c9zytE?t=9682
# django uses this and does not even require the metaclass=... business in Foo
# because the classes will inherit from something
class NonBlank:
    ...

class ModelMeta(type):
    def __init__(cls, name, bases, dic):
        super.__init__(name, bases, dic)

        for name, attr in dic.items():
            if isinstance(attr, NonBlank):
                attr.storage_name = name

class Foo(metaclass=ModelMeta):
    ...

# best version
# python 3.6+ version
class Desc:
    def __get__(self, instance, owner=None):
        return instance.__dict__[self.storage_name]
    
    def __set__(self, instance, value):
        if value == '':
            raise ValueError
        instance.__dict__[self.storage_name] = value
        
    def __set_name__(self, owner, name):
        self.storage_name = name

two type of descriptor
- data descriptor
  defines set or delete
  if an object has an entry with the name of the descriptor in its dict
     -> will NOT override the descriptor

- non-data descriptor
  only defines get
  if an object has an entry with the name of the descriptor in its dict
     -> will override the descriptor
    
class Foo:
    a = Descriptor(42)
    
f = Foo()
f.__dict__['a'] = -1
f.a # 42 if data desc, -1 if non-data desc


can have a decorator implemented as a decriptor

class defaultedmethod:
    def __init__(self, fn):
        # called when the decorator is created
        self.fn = fn
    # called when the decorated function is called
    def __get__(self, obj, cls):
        if obj is None:
            # called through the class (NamePrinter.print_name())
            return partial(self.fn, cls())
        # called through an object
        # we don't call the function directly but its __get__!
        return self.fn.__get__(obj, cls)

class NamePrinter:
    ...
    @defaultedmethod
    def print_name(self):
        print(self.xxx)



(Built-in) usage:
-super()
-static/class methods
-attributes when using __slots__
-methods
 Bound method.
 Used to transform function into method
 injects self

-prevents repetition (non negativity written once)
-lazy?
-proxying?



# namedtuple

## straight tuple
instance = ('Mr. x', 222)

## named tuple
from collections import namedtuple
Employee = collections.namedtuple('Employee', 'name id')

## typed version of namedtuple (since 3.6)
from typing import NamedTuple
class Employee(NamedTuple):
    # if type defined
    # technically a class level attribute but actually defines an instance attribute
    # just like descriptors
    name: str
    int: int = 0 # default value (must be after fields without default value)
    # no type defined
    # class level attribute
    glob = -1

    def foo(self): # can have methods
        pass

## dataclass (since 3.7)
# https://realpython.com/python-data-classes/
from dataclasses import dataclass, field
from typing import Any, List


@dataclass(
    #showing default values
    init=True,
    repr=True,
    eq=True, #tuple comparison of members, must be same type
    order=False, # lt, le, gt, ge tuple comparison
    # Never overrides an explicitely defined hash (error)
    # true : always try to add __hash__
    # false : will add __hash__ only if safe
    # if eq and frozen are true : __hash__ will be added
    # if eq and no frozen : __hash__ = None
    # if eq false : superclass __hash__ will be used (based on id)
    unsafe_hash=False, 
    frozen=False) #dataclases are mutable by default!
class Foo:
    # typing mandatory (for the field to be part of the data class)
    # but can use Any. Not enforced at runtime
    an_any: Any
    a_list: List = field(
        # default='default',
        default_factory=lambda: "default",
        init=True,
        repr=True,
        compare=True,
        hash=True,  # use value of compare by default
        metadata={"whatever": "I want"},
    )
    # needs a type to be considered as a field (instance var)
    # can put Any
    an_str: str = "default value"

    def method(self):
        return f"{self.an_str} {self.an_any}"



# generator function
use yield in a function. Function has a flag to mark it as a gneratr
when called : does not run but returns an iterator object
Supports iteration because the returned object supports __iter__ and __next__ (with StopIteration,..) 

Why this feature?
    Allows functions that can be called iteratively 
    without the potentially complex state keeping that iterative calls brings
    (or returning all the elements at once)

good alternative to a list comprehension that has become too complex
[yyy for xxx ] # something very complex here
def a_name():
    for xxx:
        yield yyy

return signals that the iterator is exhausted (same as if control flows off the end of the function) 
it will raise StopIteration from now on and won't execute code anymore
return xxx --> do not use, xxx ignored

Like all iterator, they are not reusable
g = a_name()
[x for x in g] # works
[x for x in g] # empty

can slice with itertools.islice


yield from ...
delegates the work of yielding to a subgenerator/an iterable
like : for x in subgenerator(): yield x
BUT also:
data sent  to the generator : (generator.send(xxx)) 
is sent to the subgenerator : x = yield xxx
like a coroutine except that the generator doesn't choose who runs next (only returns to the caller)


# generator expression
shortened syntax of generator
like list comprehension but lazy and returns an iterator
(... for ... in ...)

no need for parenthesis inside function IF it is the only argument
sum(x**2 for x in range(5)) # ok
sum(x**2 for x in range(5), 0) # SyntaxError

can pass it wherever a sequence is expected

# Unit test
Libraries :
unittest built-in, looks like frameworks in other languages
pytest  more compact test
nose    compatible with unittest tests

python -m unittest (equivalent yo python -m unittest)

import unittest
class BlahTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_foo(self):
        self.assertEqual(1, 1, "c")


# Logging
Logger      called by the code to record
LogRecord   an event being logged
Handler     Does something with a LogRecord (stdout, file,...)
Formatter   specify format of the output

import logging

logging using the default logger (named root):
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()

# can be used only once
# must be called before any logging is done
logging.basicConfig()


# custom logger
logging.getLogger(__name__)

# configure from file
# allows changing the config at startup without changing the code
import logging
import logging.config

logging.config.fileConfig(fname='logging.conf')




# Dunder
class A:
    def __new__(cls, *args, **kwargs):
        # returns a new instance
        # use cases : singleton, sublcassing an immutable type
        # IF return an instance/subclass of cls : __init__ will be called
        # useful to subclass immutable type (can't use init on immutable : even in init can't modify!)
        # is a static method : special cased, no @ needed. 
        # (NOT a class method. No wrapper likr in class method : obj.__new__ is obj.__new__)
        return super().__new__(cls)

    def __init__(self, other, *args, **kwargs):
        # not a constructor but an initializer because 
        # the object is already created when this method is called
        # if not present __init__ of superclass will be called automatically
        self.other = other
        pass

    def __del__(self):
        # finalizer
        # Must call del of super _if_ the superclass has a del
        # super().__del__(self)
        # `del obj`, decrements the reference count
        # __del__ call is not (necessarily) immediate (other ref exist, circular reference)
        # gotchas:
        # - may not be called for objects that still exist at exit
        # - if called during interpreter shutdown:global variables may have been deleted/set to None.
        # - exceptions are ignored (printed to sys.stderr)
        pass

    def __repr__(self):
        # either an expression that can create the object :Foo(...)
        # or information within <ClassName ...>
        return f"A({self.other})" 

    def __str__(self):
        # if doesn't exists : use __repr__
        return repr(self)
        return "human representaton of the object"

    def __format__(self, format_spec):
        # called by format()
        pass

    # can return something else than True, False, python will bool() if needed (should avoid in general)
    #
    # return NotImplemented if can't compare. 
    #   Python will try with reflection __le__(self, other) --> __ge__(other, self). 
    #   Will raise TypeError if nothing can compare (eq, ne are exceptions : they fall back to identity comparison)
    # operations can use the 'reflection' :
    #   a<b -> b>a
    #   a<=b -> b>=a
    #   a==b -> b==a 
    #   a!=b -> b==a
    #   i.e.: if a<b is not defined, python will try b>a
    #
    # ONLY for ne : can use 'not __eq__' if the __ne__ does not exist: 
    #   a!=b -> not a==b
    #
    # @functools.total_ordering to auto implement all from just < and ==  
    def __lt__(self, other):pass
    def __le__(self, other):pass
    def __eq__(self, other):pass
        # sets __hash__ to None
        # think whether __hash__ is needed
    def __ne__(self, other):pass
        # by default : calls and inverts result of __eq__
    #def __gt__(self, other):pass
    #def __ge__(self, other):pass

    def __hash__(self):
        # must return integer
        # returned value must not change over time
        # a==b ==> hash(a) == hash(b)
        # exists a default implementation based on id()
        # if NOT defined : cannot be used as key of dict, in set,...
        # if defined __hash__, __eq__ should also be defined
        # Do NOT implement if there is NO implementation of __eq__
        # set to None (or implement __eq__) to make non hashable 
        # DO NOT implement if mutable
        # can have __eq__ without hash 
        #    will automatically set __hash__ to None
        #   (eg mutable object)
        # if redefine __eq__ but not __hash__, in subclass: __hash__ = <superclass>.__hash__
        # classic error: hash of an immutable object can change if the object contains a (reference to a) mutable object
        return 123 # hash((self.x, self.y,...))

    def __bool__(self):
        # default uses len, if no len, True
        return True

    # Attribute access : x.name
    def __getattr_(self, name):
        # Called only when couldn't access name (AttributeError)
        # exist a variant for module
        pass
    def __getattribute__(self,name):
        # Always called (first) whenever an attribute access is performed
        # better to use __getattr__
        # raise AttributeError if no value to return
        # when getting, call superclass to avoid infinite recursion
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        # when setting, call superclass to avoid infinite recursion
        super().__setattr__(name, value)
        pass
    def __delattr__(self, name):
        pass
    def __dir__(self):
        # must return a sequence
        return super().__dir__()

    # Descriptor
    # see descriptor section for details
    # set a class attribute to an object with __get__, __set__ or __delete__
    # class Foo:
        attr = ADescriptor()
    # when accessing attr : will call the __get__ on the descriptor object
    # foo.x --> get/set/del defined inside foo.x.__class__
    # https://stackoverflow.com/questions/25808477/what-are-some-rules-of-thumb-for-deciding-between-get-getattr-and-ge/25808799
    # Used to implement properties, super, bound method,...
    __get__(self, instance, owner=None)
    __set__(self, instance, value)
    __delete__(self, instance)

    # Prevents creation of __dict__ and __weakref__
    # Reserves space for the variables
    # saves space, prevent creation of new attributes
    # warning with inheritance
    # see slots section
    __slots__ = ['a', 'b']

    # Container
    def __len__(self):
        # integer >= 0
        return 0
    def __length_hint__(self):
        # used to presize lists. Optimization
        pass
    def __getitem__(self, key):
        # for self[key]
        # key can be index (integer), any value (mapping) or slice()
        pass
    def __setitem__(self, key, value):
        pass
    def __delitem__(self, key):
        pass
    def __iter__(self):
        # can use generator as an iterator
        pass
    def __next__(self);
        pass
    def __reversed__(self):
        # called by reversed()
        pass
    def __contains__(self):
        # called by in
        pass

    # Numeric types
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    ...
    # called if the left operand does not support the operation
    def __radd__(self, other):
        pass
    def __rsub__(self, other):
        pass
    # in place assignment
    def __iadd__(self, other):
        pass
    def __isub__(self, other):
        pass

    # unary
    def __neg__(self):pass
    def __pos__(self):pass
    def __abs__(self):pass
    def __invert__(self):pass

    # rounding
    def __round__(self[, ndigits]):pass # towards nearest int
    def __trunc__(self):pass # towards zero
    def __floor__(self):pass # towards lower
    def __ceil__(self):pass # towards upper

    # context manager
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback)
        # args None if no exception
        # Do NOT reraise exception
        pass


# inspect module
import inspect
inspect.getsource(...)
# where is it from?
inspect.getmodule(...)


#pybytes learned
# textwrap
    unindent multiline """ """ text as if it was aligned left
    wrap text
        at word boudary or not
    shorten text blahblahblah => bla...
# secrets.choice
    like random but cryptographically secure

#collections.deque has a maxlen to turn it into a bounded buffer

'aA'.swapcase()

# hackerrank learned
itertools.product has two usages

1)take multiple elements from the same list : product(list, repeat=2)
2) combine from multiple lists : product(list1, list2, list3)

can use [...] instead of ..|..|.. in regex

\w inclus \d et _ --> [A-Za-z0-9_]

findall returns the entire matches as strings but
if there is one group () then it returns that group
if there are multiple groups then it returns those groups in a tuple    

findall returns strings

finditer returns match objects

lookahead/lookbehind (?=) (?<=)
to solve problem of not having all the results because of an overlap
re.findall(r'x(aa)x', 'xaaxaax') ==> ['aa']
re.findall(r'x(aa)(?=x)', 'xaaxaax') ==> ['aa', 'aa']

Cannot repeat qualifiers *, +, ?, {m}, ... because of ambiguity
This is incorrect :
'[\da-fA-F]{3}?'
Must add parentheses in that case
'([\da-fA-F]{3})?'

import operator
operator.mul([1], 3)
sorted_c = sorted(c.items(), key=operator.itemgetter(0))


#cheeky
++i # does nothing  
....;

#fun things you should NOT use
fun = object.meth
fun()

class X:
    if ...:
        def x():
            ...
    else:
        def x():
            ...

A_Class.a_function(object_from_different_class)

def fun():
    ...
class X:
    f = fun 

class Foo():
        def foo(self):
            print(1)

f = Foo()

def f():
    print(999)
f.foo = f

f.foo()

#read seen done
https://realpython.com/python-metaclasses/

Intermediate Python Programming 2nd Edition

The 8 things that happen at the '.' between an object and the attributes
Mike Graham - The Life Cycle of a Python Class - PyCon 2016
Kyle Knapp - Dynamic Class Generation in Python
