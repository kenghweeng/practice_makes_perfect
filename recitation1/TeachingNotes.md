Rough Teaching Notes:
1. Introduce myself, give expectations of module, emphasise integrity and how important grit is. Support system is very very strong, don't worry! Remedial, helps.
2. Components, rough weekly flow.
3. Go through questions:
* Concept of `if-elif-else`
   * Understand the equivalence between the usual block and the "one-liner" if-elif-else block: 
   ```
   if expression1:
      statement1
   elif expression2:
      statement2
   else:
      statement3
   ```
   **versus**
   `statement1 if expression1 else (statement2 if expression2 else statement3)`

   For example: `x if x>0 else ("zero" if x==0 else "invalid value")`

   * In-class discussion: What about multiple "ifs", multiple "elifs"?

* Operators:
   * Order of precedence: https://docs.python.org/3/reference/expressions.html#operator-precedence
   * String comparisons: ASCII values! How to confirm: `ord` and `chr` (these 2 functions are out of scope, can don't care)
   * Just need to know "0" < "9" < "A" < "Z" < "a" < "z"

* Code Tracing:
   * Concepts of variables, boolean values
   * Slide 135, 149 important slides!

* Burger functions:
   * Functions: print v.s return
   * How to write functions!
   * How to capture future uses!
   * Empty arguments are possible!
