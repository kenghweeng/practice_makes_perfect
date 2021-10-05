## Common mkistakes made by students:
1. Somehow decides to cancel code away, despite us being able to mark for some points. It's super wasted.
2. Forgets string slicing takes up O(n) time.
3. Forgets that we also mark for workings in Q1.
4. Tuple addition is often done without the extra brackets. Note the difference between:
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
