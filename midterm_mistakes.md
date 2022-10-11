## Common mistakes made by students:
## General things:
* Somehow decides to cancel code away, despite us being able to mark for some points. It's super wasted.

## Q1 related stuff:
* Forgets that we also mark for workings in Q1.
* Note that we deliberately have a lot of print statements for reasons.

## Q2 related stuff:
* Forgets string slicing takes up O(n) time. A kind of subtle hint wass that if we asked for a better algorithm later on, chances are that Q2A wouldn't have been O(n) already.

## Q3 related stuff:
* To be added.

## Q4 related stuff:
* Tuple addition was often done without the extra brackets. Note the difference between:
```
x = (5,)
tpl = ()
tpl += x
print(tpl) # (5,)

v.s

x = (5,)
tpl = ()
tpl += (x,)
print(tpl) # ((5,),)
```
* Forgets the type of inputs, note that time differencing cannot be done with strings: `get_checkin(record) - get_checkout(record)` can't be done since they were both **strings**.
* Wrongfully initialise the "accumulator" inside the loop instead of outside. Compare these 2 examples:
```
>>> tpl = ()
    for i in range(5):
      tpl += (i,)
  
>>> print(tpl)

v.s 

>>> for i in range(5):
      tpl = ()  # note the placement of tpl inside vs outside of for loop.
      tpl += (i,)
  
>>> print(tpl)
