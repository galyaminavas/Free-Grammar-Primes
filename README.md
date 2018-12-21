## Free (Unrestricted) Grammar For Prime Numbers
Code hint: just run 'python free_grammar.py'


#### Grammar
Axiom: A

Non-terminals: A, S, Q, a, b, +, -, *, o, '

Terminals: #, t

#### Rules:
0. A -> #S#
1. S -> aQ
2. Q -> bQ
3. Q -> b+
4. b+# -> b*#
5. bb* -> b*c
6. ab* -> a*a-
7. aa* -> a*a-
8. #a* -> #a+
9. -a -> a-
10. -b -> b-
11. -c -> b
12. -# -> #
13. +a -> a+
14. +b -> b+
15. +c -> bo
16. oc -> 'c
17. b' -> 'b
18. a' -> a*
19. a+# -> t#
20. at -> tt


---------------------------
| Prime | Derivation length|
| ----- | -----------------|
| 2 | 10 |
| 3 | 23 |
| 5 | 86 |
| 7 | 221 |
| 11 | 767 |
| 13 | 1 279 |
| 17 | 2 700 |
| 19 | 3 711 |
| 23 | 6 339 |
| 29 | 12 574 |
| 31 | 15 452 |
| 37 | 26 082 |
| 41 | 34 745 |
| 43 | 40 013 |
| 47 | 51 208 |
| 53 | 73 265 |
| 59 | 99 880 |
| 61 | 112 267 |
| 67 | 147 211 |
| 71 | 173 466 |
| 73 | 190 680 |
| 79 | 238 146 |
