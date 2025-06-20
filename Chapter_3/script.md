# IN THIS CHAPTER:
  - you learn recursion
  - base case and recursive case , which D&C uses
<hr>

>[!NOTE]
> it is generally recommended to execute the examples in this chapter.

recursive functions call themselves over and over again until something stops them, or they don't.
*recursive case is when the function calls itself*
*the base case is when the function doesn't call itself again, so it doesn't get into an infinite loop.*
**Every time you make a function call, yuour computer saves the values for all the variables  for that call in memory like this.**
***When you call a function from another function, the calling function is paused in a partially completed state.***

**A stack has 2 operations: push n pop**

in a recrusive function, ***each call function has its own copy of the variables.***

**if the recursive functions gets too big, the memory overloads and we get "a stack overflow"**
