## Free (Unrestricted) Grammar For Prime Numbers
Code hint: just run 'python free_grammar.py'


#### Grammar
Start: #S#
Non-terminals: S, Q, a, b, +, -, *, o, '
Terminals: #, t
#### Rules:
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
| 2 | 9 |
| 3 | 22 |
| 5 | 85 |
| 7 | 220 |
| 11 | 766 |
| 13 | 1 278 |
| 17 | 2 699 |
| 19 | 3 710 |
| 23 | 6 338 |
| 29 | 12 573 |
| 31 | 15 451 |
| 37 | 26 081 |
| 41 | 34 744 |
| 43 | 40 012 |
| 47 | 51 207 |
| 53 | 73 264 |
| 59 | 99 879 |
| 61 | 112 266 |
| 67 | 147 210 |
| 71 | 173 465 |
| 73 | 190 679 |
| 79 | 238 145 |
