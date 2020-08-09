# 2020-04-30
## git and Testing
This is an attempt to create a *proper* remote repository.
### What I want to achieve with this repository
---
- learn about git repositories. 
- learn about GitHub
- learn to use Markdown and commands such as...
``` 
git init
git status 
git commit (-m)
git push
```
### Testing your code
---
#### ```assert``` statement.
---
- ```assert``` statement is either ```True``` or ```False``` 
- usage: ```assert myfunction(args) == result```
- It is not always possible to distinguish between errors in function or results. 
#### Python frameworks 
---
- unittest (comes with the standard library)
- nose (obsolete)
- pytest (most popular one, per instructor)
#### C++ frameworks 
---
- Boost::test
- google_test
- Catch2
#### Implementation of pytest in python
---
```
def test_something():
    assert myfunction(args) == result
def test_something_else():
    assert myfunction(diff_args) == diff_result
```
- Then, the test is done by calling pytest in terminal as follows: ```pytest your_script.py```
- Dots past the name represent number of tests. Failed test is shown by an 'F'.
- Exceptions: Need to import pytest to script and ```with pytest.raises(expected exception like ZeroDivisionError): 
    myfunction(args)```
Script2.py in this repository is an example of such testing framework. 
---
- Tests can be in another file but in same directory. If all tests are defined in a separate file, the required parts need to be *imported* to the test script. For example, ```from script2 import divide``` as seen above.
- Therefore, it allows a higher degree of automation. Collecting similar kinds of tests in separate files in the same directory.
#### Best practices
---
- Arrange: Establish a database connection; Create file
- Act: Actually call the function/class/method that is tested. Try to keep tests small, and with simpler logic. 
- Assert: assert results.

# 2020-05-28
## CLI:
+ Command line argument parsing: ```argparse``` or ```click``` 
+ ```__name__``` returns name of script that is being executed, or the name of the module that is imported (which depends on the filename of the module script). 
+ See ```script.py``` for more information and hands-on example. 
---
### Click usage: 
- ```@click.command()``` initiates click and responds when script.py is called with ```--help```
- ```@click.argument(arg)``` allows user to provide command line argument and assigns to variable name ```arg``` as specified in this example. It is a positional argument while calling from command line.
- ```@click.argument(arg,type='vartype')``` takes care of type casting if necessary, and provides error message if invalid type casting is attempted. 
- Negative arguments can be passed on commandline using ```--``` before the particular argument. 
- Can be used instead of raising errors in the script, API link is given below, example usage can be seen in ```setup.py```
- To make the argument an option, ```@click.option()``` is used. It allows more verbose passage in CLI. However, they are not required, and the default value would be ```None``` or 0. This is rectified by specifying as ```@click.option("--arg",required=True)```
- ```@click.option("--arg",help="Description of the argument")``` helps in providing better description of arg in help. 
---
### Relevant links
- Click: https://click.palletsprojects.com/en/7.x/
- Argparse tutorial: https://docs.python.org/3/howto/argparse.html
- Argparse documentation: https://docs.python.org/3/library/argparse.html#module-argparse
- More on ```__name__```: https://www.tutorialspoint.com/name-a-special-variable-in-python
- Types in Click: https://click.palletsprojects.com/en/7.x/api/#types 
- Dave Forgac - Writing Command Line Applications that Click - PyCon 2019 - YouTube: https://www.youtube.com/watch?v=Sv7rRGTaMHE

# 2020-06-04

## PYTHON PACKAGES - PyGeo

A Python package for three-dimensional geometry. Usually, a python package is a directory. All the code should be in directory known as ```src```
**Implemented here: GOAL: Write a function for floating point equality check**
- First thing, writing of directory structure. Essentially, create a new directory with the name of the package. This directory file will have following files:
    - ```__init__.py``` - Tells it is a package, and executes it whenever imported. 
    - Other modules
- To make a package installable, one needs to create a ```setup.py``` file. These evolve rapidly, be on the lookout. This method is a bit older. 
    - This file imports ```setup, find_packages``` from ```setuptools``` package. Syntax can be seen in the file present. 
    - This allows user to install via pip, using the command ```pip install -e .```. Specifying -e specifies that this package will be editable, and forces an update whenever the source code is changed, eliminating need to run ```pip upgrade```. 
- This can be used to create a file consisting specifically of tests. 


- Variables are configurable by the user. Using ```mypackage.my_method()``` calls the method, whereas ```mypackage.my_variable``` accesses the variable, which can then be given a new value. Especially useful in case of floating point errors. 

- Other modules can be declared as dependencies and make the custom package import them as well. ```setup.py``` will then include ```install_requires```. ```install_requires``` forces the install of dependencies, so include only absolutely necessary packages. 

- For optional packages, ```extras_require``` argument to setup function, which is a dictionary. For example, see ```setup.py```. In this case, however, ```pip install -e .[dictionary_key_specified]``` must be used to check installation and request a package. This distinguishes usage between users and developers of a package. 

### Implementing the tests
This is directly related to the goal specified above. The structure recommends a ```tests``` directory alongside on the same level as ```src```. 

- Try emulating the bug reported. 

### Test Driven Development 
- Naming convention: *UnitOfWork_StateUnderTest_ExpectedBehavior*
- For example: ```test__unit_of_work__state_under_test__expected_behaviour()```
- Unit of work: Function, or class, or whatever is being tested. Most of the tests are unit tests, so the name of the function is given. 
- Could be under a file structure as follows: test_unit_of_work.py -> test__state_under_test__expected_behavior()
- Example: ```def test__give_two_equal_numbers__return_true():```

### Additional structuring
- Code can be structured into different files within the src directory, which would require usage of file name while importing, i.e. ```from module.file_name import function```. For example, in this module, ```from pygeo.comparisons import are_equal```
- This can be avoided by adding ```from .file_name import function``` in ```__init__.py```. In the case described above, it hence becomes, ```from .comparisons import are_equal``` which makes the function available in the ```__init__.py```. 
- Something inside init can be called a package, and something in a .py file in the same directory is called a module. 
- To ensure python imports the right module '.' is used, this is known as relative importing. '..' is the level above. 

# 02.07.2020 - OOP setup
- Refer to ```src/pygeo/models.py``` for an example. 
- To define a class, we use the keyword class followed by the name of it, always have a docstring. Usage: ```class Point:```. 
- ```isinstance(object,class)``` is a function that returns True or False if the given object is an instance of the specified class or not. 
- A method is a function that is attached to a class, which always takes a parameter called ```self``` as the first argument. 
- The first method in a class is usually ```__init__()```, to initialize an object of this class. It is passed implicitly. ```self``` in itself is an object of the class, which must be passed. 
- ```__repr__(self)``` is a method to initialize the representation of the object of the class being defined. This is called internally when user executes ```print(object)``` command. This method can construct a string which will be returned. 
- ```__sub__()``` and ```__rsub__()``` are two special methods in classes. ```__rsub()__``` takes right side argument as self instead of left one. Python tries both, starting with ```__sub__()```. This can be forced by using an if condtion checking the instances and using ```return NotImplemented```.

### Misc info
- To avoid round-off error or floating point error, use ```Sum-number<tolerance``` instead of ```sum == number```

- Something ```is [True, False, None]``` is used instead of ```== [True,False,None]```.

### Relevant Links
- ```gitignore``` repository of python: https://github.com/github/gitignore/blob/master/Python.gitignore
- src directory layout - https://blog.ionelmc.ro/2017/09/25/rehashing-the-src-layout/
- Packaging a python library - https://blog.ionelmc.ro/2014/05/25/python-packaging/
- Test Driven Development - https://en.wikipedia.org/wiki/Test-driven_development
-  Test Driven Development: By Example (A Kent Beck Signature Book) - https://www.goodreads.com/book/show/387190.Test_Driven_Development
- Osherove:
    - Naming standards for unit tests - https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html
    - Test naming conventions with unit of work - https://osherove.com/blog/2012/5/15/test-naming-conventions-with-unit-of-work.html
- Pytest: Good Integration Practices - https://docs.pytest.org/en/latest/goodpractices.html