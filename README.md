# Linked List String

In this assignment, you will write iterative and recursive methods that operate on a linked list representation of a string. We started the `LLString` class in the lessons and practice exercises this week. Now, it's your turn to add functionality to it.

## Starter Code

You are given the file `llstring.py`, which includes the implementation of `LLString` class that we started in the lessons this week. Each `LLString` object contains both a `head` pointer to the beginning of the linked list, as well as a `tail` pointer to the end of the linked list. It also contains the following methods:

* Constructors (`__init__`) for creating a linked list, including from a string
* An `append()` method, which appends a new node to the end of the list
* A `print()` method, which prints the contents of the list
* A `to_string()` method, which returns a string version of the `LLString`

***You should not change any of the existing methods in the `LLString` class.*** Doing so may hinder our ability to test your code.

You may wish to refer back to the lessons or practice exercises to see example implementations of other `LLString` methods.

## Steps to Complete

Implement the following six methods. As you do so, keep the following guidelines in mind:

* For some methods, you may be required to implement the solution either iteratively or recursively. Solutions that don't implement the method using the described technique will receive only partial credit.
* You should *not* change any of the method signatures (names or parameters), and in particular, you should not add any optional or default parameters.
* If you need to add a recursive helper function, you should create a new method using the double underscore convention. For example, if the given method to implement is `print()` and you need a recursive helper method, you should name the recursive method `__print()`.
* For each method, you should consider all possible edge cases, including (but not limited to): if the list is empty and if the list has one node. Be sure to test your methods with as many cases as possible. More information about testing is below.
* You may only use programming concepts and constructs covered in this course and previous Kibo courses. In particular, you may not use built-in library functions that have not been discussed, or inner (nested) Python functions for your recursive methods.
* For full credit, you should not call the `to_string()` method and operate on the resulting string (this requires `O(n)` extra space). Instead, you should do all of your operations on the linked list itself.

1. Implement the `find(c)` method using iteration. `find(c)` finds and returns the index of the first occurrence of the character `c` in the linked list.

    Sample inputs and outputs:

    | `LLString` | Method Call | Expected Output |
    |------------|-------------|-----------------|
    | `'hello'`  | `find('l')` | 2               |
    | `'hello'`  | `find('o')` | 4               |
    | `'hello'`  | `find('x')` | -1              |

2. Implement the `to_upper_case()` method using recursion. `to_upper_case()` converts each character of the existing list to upper case.

    * For the purposes of this method, you may assume that each character in the string is a Latin alphabet character.
    * Some characters may already be upper case.
    * You should not create any new nodes for this method. Any changes to the list should be made *in-place* -- i.e., on the given linked list itself.
    * You can use the built-in Python function `upper()` to convert a lowercase character to an uppercase character.

    Sample inputs and outputs:

    | `LLString` | Expected Output |
    |------------|-----------------|
    | `'hello'`  | `'HELLO'`       |
    | `''`       | `''`            |
    | `'hElLo'`  | `'HELLO'`       |

3. Implement the `replace(old, new)` method using either iteration or recursion. This method should replace each occurrence of the character `old` with the character `new`.

    For example, if the list represents the string `'banana'`, then `replace('a', 'o')` should modify the list so that it represents the string `'bonono'`.

    Notes:

    * The linked list may or may not contain the character `old`. If it does not, your method should not change the list.
    * You may use either iteration or recursion.

    Sample inputs and outputs:

    | `LLString`  | Method Call         | Expected Output |
    |-------------|---------------------|-----------------|
    | `'banana'`  | `replace('a', 'o')` | `'bonono'`      |
    | `'banana'`  | `replace('y', 'o')` | `'banana'`      |
    | `''`        | `replace('a', 'e')` | `''`            |

4. Implement the `copy()` method using either iteration or recursion. `copy()` should create and return a copy of the `LLString` object. In other words, it should create a new `LLString` object, and populate it with new nodes that hold all of the characters that are in the `LLString` object that was used to call the method (`self`).

    Notes:

    * As a part of this function, you will need to create a new linked list -- something like `new_list = LLString()`.
    * You can make use of any of the existing `LLString` constructors and methods, if needed.
    * You may use either iteration or recursion.
    * If the calling `LLString` is empty (has no nodes), the copy should be empty as well.

5. Implement the `trim()` method using either iteration or recursion. `trim()` should trim any space characters from the beginning or end of the `LLString` by deleting nodes from the list. However, any spaces in the middle of the string should be preserved.

    For example, if the linked list represents the string `'   hello  '`, then `trim()` should modify the list so that it is only `'hello'`. Similarly, for `' hello     world'`, `trim()` should return `'hello     world'`.

    Sample inputs and outputs:

    | `LLString`          | Expected Output    |
    |---------------------|--------------------|
    | `'   hello  '`      | `'hello'`          |
    | `'  hello    world'`| `'hello    world'` |
    | `''`                | `''`               |

6. Implement the `find_nth(n, c)` function using recursion. `find_nth(n, c)` should return the index of the `n`th occurrence of the character `c` in the `LLString`.

    Sample inputs and outputs:

    | `LLString`  | Method Call         | Expected Output |
    |-------------|---------------------|-----------------|
    | `'banana'`  | `find_nth(2, 'a')`  | 3               |
    | `'banana'`  | `find_nth(1, 'b')`  | 0               |
    | `'banana'`  | `find_nth(4, 'a')`  | -1              |
    | `''`        | `find_nth(1, 'e')`  | -1              |
    | `'banana'`  | `find_nth(0, 'a')`  | -1              |
    | `'banana'`  | `find_nth(-1, 'a')` | -1              |

## Testing

In `test_llstring.py`, there are unit tests for each of the six methods described above. However, these tests are not exhaustive, and you should add your own tests to ensure the correctness of your code.

When you upload your submission to Gradescope, you will see the results for some tests, but there may be other edge cases we test during grading that you are not able to see when you submit. So be sure to test thoroughly!
