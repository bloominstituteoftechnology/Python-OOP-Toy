# Overview
“Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which may contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods. A feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated (objects have a notion of "this" or "self"). In OOP, computer programs are designed by making them out of objects that interact with one another.[1][2]” --Wikipedia

In English, this means that in OOP, code is organized in logical and self contained parts that contain within them everything needed to create, store, and manipulate one very specific element of the program.  When this element is needed, a copy of it is initialized according to the instructions within.  This is called an object.  

As with all things programming, the specific vocabulary varies from language to language, or even programmer to programmer.  Some Python vocabulary:

Class:  The top level organization structure in OOP.  This contains all of the instructions and storage for the operations of this part of the program.  A class should be self contained and all variables within the class should only be modified by methods within the class.

Method:  A function that belongs to a specific class.

Constructor:  A special method, defined with __init__() that is used to instantiate an object of this class.

Inheritance:  Perhaps the most important concept in OOP, a class may inherit from another class.  This gives the child class all of the variables and methods found in the parent class, or classes, automatically.  

Override:  If a child class needs to function slightly differently than objects of the parent class, this can be done by giving the child class a method with the same name as one found in the parent.  This method will override the one defined in the parent class.  Often, this is done to add child specific functionality to the method before calling the parent version of the method using super().foo().  This is commonly done with the __init__() method.

Self: In Python, a class refers to class-level variables and methods with the keyword `self`.  These have scope across the entire class.  Variables may also be declared normally and will have scope limited to the block of code they are declared within.

# Python OOP Toy
This project will demonstrate the core concepts of OOP by using a library called pygame to create a toy similar to early screensavers.  

To run, use: `python src/draw.py`

## In-class Demo
Your instructor will demonstrate the above concepts by extending the `Block` class

## Project Work
Fill out the stubs in `ball.py` to extend the functionality of the `ball` class.

## Stretch Goals
Implement simple physics to enable balls to bounce off of one another, or off of blocks.  This will be HARD.  If you get it ‘sort of working’ in any form, consider yourself to have accomplished an impressive feat!
