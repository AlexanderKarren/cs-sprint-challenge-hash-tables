# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions

The idea behind a hashing table is to put in a string and use a complex mathematical operation (usually involving a bitwise operation) to produce a long, unique integer to be used for an index. After the item is in an array, the hashing function can be used to produce the index again for constant access to an item.

2. Collision resolution

Collisions can be avoided through a couple of methods:
- Linked nodes. Using a simple linked list, if a collision occurs, an item can be placed at the same index as another item by pointing the original node to it.
- Automatic resizing (see below)

3. Performance of basic hash table operations

With a larger list, accessing and updating items in a linked list should be done in O(1) time. With more collisions, the performance will be worse, but this issue can be subdued by implementing automatic resizing (see below) which should reduce the amount of linked nodes at one index. Many linked nodes at one index (many collisions) means that the program will need to go into a loop to access values.

4. Load factor

Load factor can be calculated by dividing the number of active elements by the number of open slots (length of the array.) This can be used to provide the program with a threshold for automatic resizing (see below.)

5. Automatic resizing

Automatic resizing is a program implementation that allows the array to be lengthened or shortened and the indices reallocated when the load factor (see above) goes above or below a certain threshold. In theory, the larger a list is, the fewer potential collisions.

6. Various use cases for hash tables

- Hash tables can be used as a cache for performance-heavy recursive operations. If a recursive function is liable to perform the same operations more than once, it’s useful to have the function store results in a hash table for lookup on future iterations.
- Hash tables can be used for AI chains, like Markov, to store words and phrases and the words that follow them to produce a random syntax with a realistic (or, as realistic as it can be) syntax.
- Hash tables can be used to store first appearances of values so that duplicates can be identified in constant time.

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [x] Create a forked copy of this project
- [x] Add your team lead as a collaborator on Github
- [x] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [x] Create a new branch: git checkout -b `<firstName-lastName>`.
- [x] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [x] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [x] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [x] Navigate into each exercise's directory
- [x] Read the instructions for the exercise in the README
- [x] Implement your solution in the `.py` skeleton file
- [x] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [x] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

