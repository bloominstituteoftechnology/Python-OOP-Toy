# Python - Intro to
 * learning Python is like learning a new language. We know what we want to talk about, but we just don't know how to express it in the new language. It's taking concepts that we already know, but expressing them in the new language's context.

# Programming Paradigm
* big three: Procedural Programming, Object-Oriented Programming and Functional Programming

* What is a programming paradigm? 
    - a "way" of programming
    - a way of thinking about how you are going to write code to process data.
    - certain languages tend to follow one paradigm or another

## Types of programming paradigms
* Imperative programming
    - Control flow in imperative programming is explicit: commands show how the computation takes place, step by step. Each step affects the global state of the computation.
```
    result = []
    i = 0
start:
    numPeople = length(people)
    if i >= numPeople goto finished
    p = people[i]
    nameLength = length(p.name)
    if nameLength <= 5 goto nextOne
    upperName = toUpper(p.name)
    addToList(result, upperName)
nextOne:
    i = i + 1
    goto start
finished:
    return sort(result)
```

* Structured Programming
    - Structured programming is a kind of imperative programming where control flow is defined by nested loops, conditionals, and subroutines, rather than via gotos. Variables are generally local to blocks (have lexical scope).
```
result = [];
for i = 0; i < length(people); i++ {
    p = people[i];
    if length(p.name)) > 5 {
        addToList(result, toUpper(p.name));
    }
}
return sort(result);
```

## Object Oriented Programming

OOP is based on the sending of messages to objects. Objects respond to messages by performing operations, generally called methods. Messages can have arguments. A society of objects, each with their own local memory and own set of operations has a different feel than the monolithic processor and single shared memory feel of non object oriented languages.

One of the more visible aspects of the more pure-ish OO languages is that conditionals and loops become messages themselves, whose arguments are often blocks of executable code. In a Smalltalk-like syntax:
```
result := List new.
people each: [:p |
  p name length greaterThan: 5 ifTrue: [result add (p name upper)]
]
result sort.
^result
```
This can be shortened to:

```
^people filter: [:p | p name length greaterThan: 5] 
 map: [:p | p name upper] sort
```
Many popular languages that call themselves OO languages (e.g., Java, C++), really just take some elements of OOP and mix them in to imperative-looking code. In the following, we can see that length and toUpper are methods rather than top-level functions, but the for and if are back to being control structures:
```
result = []
for p in people {
    if p.name.length > 5 {
        result.add(p.name.toUpper);
    }
}
return result.sort;
```
The first object oriented language was Simula-67; Smalltalk followed soon after as the first “pure” object-oriented language. Many languages designed from the 1980s to the present have labeled themselves object-oriented, notably C++, CLOS (object system of Common Lisp), Eiffel, Modula-3, Ada 95, Java, C#, Ruby.

## Functional Programming
In functional programming, control flow is expressed by combining function calls, rather than by assigning values to variables.




