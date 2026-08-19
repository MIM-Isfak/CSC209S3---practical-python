seq1 = "GAT"
seq2 = "GCT"

m = len(seq1)
n = len(seq2)

score_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

gap_penalty = -2

for i in range(1,m+1):
    score_matrix[i][0] = score_matrix[i-1][0] + gap_penalty

for j in range(1,n+1):
    score_matrix[0][j] = score_matrix[0][j-1] + gap_penalty
    
Microsoft Windows [Version 10.0.26200.8655]
(c) Microsoft Corporation. All rights reserved.

C:\Users\dcsuser\Documents\2023csc044\csc209s3>my_env\Scripts\activate

(my_env) C:\Users\dcsuser\Documents\2023csc044\csc209s3>python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> lst = [0 for_in range(3)]
  File "<python-input-0>", line 1
    lst = [0 for_in range(3)]
           ^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> lst = [0 for _ in range(3)]
>>> lst
[0, 0, 0]
>>> for i in range(3):
...     print("Hello")
...
Hello
Hello
Hello
>>> lst = []
>>> for i in range(3):
...     lst.append(0)
...
>>> print(lst)
[0, 0, 0]
>>> for i in range(3):
...     lst.append([0,0,0],[0,0,0])
...
Traceback (most recent call last):
  File "<python-input-7>", line 2, in <module>
    lst.append([0,0,0],[0,0,0])
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^
TypeError: list.append() takes exactly one argument (2 given)
>>> for i in range(3):
...     lst.append([0,0,0])
...
>>> lst
[0, 0, 0, [0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> [[0,0,0] for _ in range(3)]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> [[0 for _ in range(3)] for _ in range(3)]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> [[0 for _ in range(5)] for _ in range(3)]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
>>> seq1="GAT"
>>> seq2="GCT"
>>> m = len(seq1)
>>> n = len(seq2)
>>> score_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
>>> score_matrix
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
>>> lst[0][0]
Traceback (most recent call last):
  File "<python-input-19>", line 1, in <module>
    lst[0][0]
    ~~~~~~^^^
TypeError: 'int' object is not subscriptable
>>>
>>> lst = [[0 for _ in range(5)] for _ in range(3)]
>>> lst
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
>>> lst[0][0]
0
>>> score_matrix[i][j]
Traceback (most recent call last):
  File "<python-input-24>", line 1, in <module>
    score_matrix[i][j]
                    ^
NameError: name 'j' is not defined
>>> score_matrix[1][0] = -2
>>> score_matrix[2][0] = -4
>>> print("hello")
hello
