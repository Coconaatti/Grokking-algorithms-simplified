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


Sequential access : It is basically reading the elements one by one. *Lists use that only*.

random access : It is basically reading all of the data at once. *Arrays use that*.

***Arrays also use caching, making them even better.***

> [More differences can be found here.](https://statlearner.org/random-access-vs-sequential-access-memory)

 **Linked lists occupy more memory as they store the adresses also. However, this isn't the case with Arrays. They occupy less memory.**

> [!CAUTION]
> ***HOWEVER, if each item is big in an array, then a single lslot is valuable. AND In comparison storing addresses by lists is more efficient (and smol).***\
> *SO, arrays are used more often than lists **except in specific use cases.***

