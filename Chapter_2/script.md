# IN THIS CHAPTER:
 -  you'll revise the difference between arrays and lists
 -  sosme stuff abt data types
 -  you'll learn selection sort

tasks and items are stored next to each other in memory (contiguously).

tasks and items can be anywhere in linked lists. **Therefore, linked lists are good at inserts.**

***In linked lists, you don't know the address of the next item. you have to go to the X element to get the address of the Y element. ***

***In arrays, you know the address for every item.***

Indexes are the pos. of the item.

***In linked lists, adresses are stored in memory. They are also called pointers.***

##Runtimes:
  ... | arrays | lists | reason | 
|-----|--------|-------| ------ |
 | READING | O(1) | O(n) | Arrays are next to each other, lists contain addresses and pointers. |
 | INSERTING | O(n) | O(1) | You need to move the whole array to add an element in the middle, however you can insert an element in the middle without any problem in lists. |
 | DELETION | O(n) | O(1) | Same reason as INSERTING. |
