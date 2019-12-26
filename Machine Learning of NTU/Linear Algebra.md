Linear Algebra Lecture 2018

 http://speech.ee.ntu.edu.tw/~tlkagk/courses_LA18.html 

## Intro

Input -> System -> Output

Linear system has 2 properties

1. persevering multiplication

   x -> Linear system -> y

   kx -> Linear system -> ky

2. persevering addition

   x1 -> Linear system -> y1

   x2 -> Linear system -> y2

   x1 + x2 -> Linear system -> y2 + y2

#Prediction
$$
y = w_1x_1 + w_2x_2 + w_3x_3
$$


##  System of Linear Equations 

$$
a_{11}x_1 + a_{12}x_2 + ... + a_{1n}x_n = b_1\\
a_{21}x_1 + a_{22}x_2 + ... + a_{2n}x_n = b_2\\
...\\
a_{m1}x_1 + a_{m2}x_2 + ... + a_{mn}x_n = b_m\\
$$

function f(Input in domain) = Output in range in co-domain

Domain	 	定义域

Co-domain	对应域

Range		 	值域

one-to-one	一对一

Onto			   映成（Co-domain = range)

*Derivative & Integral are all linear system



A linear system is described by a system of linear equations

## Vector

A vector **v** is a set of numbers

**Row Vector**
$$
[1 \ 2 \ 3]
$$
**Column Vector**
$$
\left[\begin{array}{c}
1\\
2\\
3\\
\end{array}\right]
$$
The i-th component of vector v refers to vi.

*If a vector only has less than four components we can visualize it.
$$
v_1 = 1, v_2 = 2, v_3 = 3
$$

**Scalar Multiplication**
$$
v =\left[\begin{array}{c}
v_1\\
v_2\\
\end{array}\right] \\
cv = \left[\begin{array}{c}
cv_1\\
cv_2\\
\end{array}\right]
$$
**Vector Addition**
$$
v_1 =\left[\begin{array}{c}
a_1\\
b_1\\
\end{array}\right] \\
v_2 = \left[\begin{array}{c}
a_2\\
b_2\\
\end{array}\right] \\
v_1 + v_2 = \left[\begin{array}{c}
a_1 + a_2\\
b_1 + b_2\\
\end{array}\right]
$$
**Vector Set**

A vector set with 4 elements
$$
\left\{
\left[\begin{array}{c}
1 \\
2 \\
3 \\
\end{array}\right],
\left[\begin{array}{c}
4 \\
5 \\
6 \\
\end{array}\right],
\left[\begin{array}{c}
6 \\
8 \\
9 \\
\end{array}\right],
\left[\begin{array}{c}
9 \\
0 \\
2 \\
\end{array}\right]
\right\}\\
$$
A vector can contain infinite elements
$$
L = \left\{
\left[\begin{array}{c}
x_1 \\
x_2 \\
\end{array}\right]: x_1 + x_2 = 1 \right\}
\\
R^n: We \ denote \ the \ set \ of \ all \ vectors \ with \ n \ entries \ by \ R^n
$$
**Properties of vector**

**u + v = v + u**

**(u + v) + w = u + (v + w)**

There's an element **0** in R^n such that **0 + u = u**

There's an element **u'** in R^n such that **u' + u = 0**

1**u** = **u**

(ab)**u** = a(b**u**)

a(**u + v**) = a**u** + a**v**

(a+b)**u** = a**u** + b**u**

## Matrix

Row first, then column when describe the entry or the matrix

zero matrix: matrix with all zero entries, denote by O

Identity matrix: must be square(左上到右下的对角线为1, 其他为0), denote by I

**Properties**

A + B = B + A

(A + B) + C = A + (B + C)

(st)A = s(tA)

s(A+B) = sA + sB

(s+t)A = sA + tA

**Transpose**

A is an m*n matrix

A^T (transpose of A) is an n*m matrix whose (i,j)-entry is the (j-i)-entry of A
$$
A = 
\left[\begin{array}{c}
6 & 9\\
8 & 0\\
9 & 2\\
\end{array}\right]\\
A^T = 
\left[\begin{array}{c}
6 & 8 & 9\\
9 & 0 & 2\\
\end{array}\right]
$$
(A^T)^T = A

(sA)^T = sA^T

(A + B)^T = A^T + B^T

## Matrix-Vector Product

$$
A = 
\left[\begin{array}{c}
a_{11} & a_{12} & ... & a_{1n}\\
a_{21} & a_{22} & ... & a_{2n}\\
...\\
a_{m1} & a_{m2} & ... & a_{mn}\\
\end{array}\right],
x = 
\left[\begin{array}{c}
x1\\
x2\\
...\\
xn\\
\end{array}\right]\\
Ax = 
\left[\begin{array}{c}
a_{11}x_1 + a_{12}x_2 + ... + a_{1n}x_n\\
a_{21}x_1 + a_{22}x_2 + ... + a_{2n}x_n\\
...\\
a_{m1}x_1 + a_{m2}x_2 + ... + a_{mn}x_n\\
\end{array}\right]
$$

Linear Equations: Ax = b

x -> Linear System(Coefficients are A) -> Ax



Row aspect is tuition

Column aspect:

 Ax = x1[Col 1] + x2[Col2] + ... + xn[Coln]



*size should be matched between matrix and vector

**Properties**

A(u + v) = Au + Av

A(cu) = c(Au) = (cA)u

(A + B)u = Au + Bu

A0 is m*1 zero vector

Ov is also the m*1 zero vector

I_n * v = v



If Aw = Bw for all w in R^n, then A = B

## Having Solution or Not?

![image-20191225185819331](C:\Users\houkc\AppData\Roaming\Typora\typora-user-images\image-20191225185819331.png)

Given A and b, sometimes x exists, and sometimes doesn't.          *Find x

**Consistent**: one or more solutions

**Inconsistent**: no solution



**Linear Combination**

Given a vector set {u1, u2, ..., uk}, find k scalars c1, c2, ..., ck, then get new vector v.
$$
v = c_1u_1 + c_2u_2 + ... + c_ku_k
$$
zero vector is the linear combination of any other vectors

v is the linear combination of the vector set {u1, u2, ..., uk}, {c1, c2, ..., ck} is the solution



Ax = b

Have solution? = Is b the linear combination of column of A? = Do the results come from the linear system? = Can we find any input to generate the specified result through the linear system?

**<u>R^2: u and v are nonzero vectors & u ≠ cv -> u & v are not parallel -> has solution</u>**

<u>**has solution --[no]--> u and v are not parallel**</u>

R^3: u, v and w are independent -> has solution



**Span**

A vector set S = {u1, u2, ..., uk}, Span S is the vector set of all linear combinations of u1, u2, ..., uk.

Span S = {c1u1 + c2u2 + ... + ckuk | for all c1, c2, ..., ck}



Vector set V = Span S

S generates V, it is a kind of description of how to generate a giant set vector V.



Span which do not contain zero vector has infinitely many vectors

Different number of vectors can generate the same space

If there are at least 2 vectors in the set are not parallel and all of the vectors are in R^2, then the span is in the R^2, too.



**if {b is a linear combination of columns of A} & {b is in the span of the columns of A}**

​    #have solution

​    **if {columns of A are independent} or {rank A = n} or {nullity A = 0}**

​        **Unique solution**

​    **else {columns of A are dependent} or {rank A < n} or {nullity A > 0}**

​        **Infinite solution**

**else:**

​    **no solution**

## How Many Solutions?

A set of vector {a1, a2, ..., an} is linear dependent.

If there exist scalars x1, x2, ..., xn, not all zero such that
$$
x_1a_1 + x_2a_2 + ... + x_na_n = 0
$$
A set of vector {a1, a2, ..., an} is linear independent (there will be no zero in the set)
$$
x_1a_1 + x_2a_2 + ... + x_na_n = 0 \\
Only\ if\ x_1 = x_2 = ... = x_n = 0
$$


**Linear Dependent**

Given a vector set, {a1, a2, ..., an}, if there exists any ai that is a linear combination of other vectors.

Once we have solution and meantime the set of vector is linear dependent <=> we have infinite solutions.

**[Proof for homogeneous linear equations]**

*Homogeneous linear equations*

if Ax = 0, then it is homogeneous linear equations.

A homogeneous must have a solution which is zero vector.

<u>Based on the definition</u>

A set of n vectors {a1, a2, ..., an} is linear dependent <=> Ax = 0 have nonzero solution + a zero vector solution => we have more than one solutions => we have infinite solutions

A set of n vectors {a1, a2, ..., an} is linear independent <=> Ax = 0 have only zero solution => we have only one solution

**[Proof for general linear equations]**

<u>Columns of A are dependent -> if Ax = b have solution, it will have infinite solutions</u>

1. We can find non-zero solution u such that Au = 0
2. There exists v such that Av = b

then A(u+v) = b, (u+v) is another solution different to v

<u>If Ax = b have infinite solutions -> Columns of A are dependent</u>

Au = b

Av = b, and u ≠ v

A(u - v) = 0 and u - v ≠ 0  [Definition of dependent]



**Rank and Nullity**

The **rank** is a matrix is defined as the maximum number of linearly independent columns in the matrix.

**nullity** = #columns - **rank**



**if {columns of A are independent} or {rank A = n} or {nullity A = 0}**

​    **if {b is a linear combination of columns of A} & {b is in the span of the columns of A}**

​        **Unique solution**

​    **else**

​        **No solution**

**else**

​    **if {b is a linear combination of columns of A} & {b is in the span of the columns of A}**

​        **Infinite solution**

​    **else**

​        **No solution**

## Solving System of Linear Equations

Two systems of linear equations are equivalent if they have exactly the same solution set.

<u>Three operations</u> of change the origin system of linear equation to another system of linear equation

1. interchange
2. scaling (nonzero scalar)
3. row addition

<u>augmented matrix</u>

augment A to A' = [A | b], then operate on the augmented matrix with the previous 3 operations(elementary row operations) to get A'', A''', ..., R = [R' b'] -> R'x = b' which is reduced row echelon form(RREF).



**Reduced Row Echelon Form(RREF)**

Row Echelon Form

1. Each nonzero row lies above every zero row
2. The leading entries(the first element which is not 0) are in echelon form(like a ladder)

Reduced Row Echelon Form

1. The matrix is in row echelon form
2. The columns containing the leading entries are standard vectors(the elements are zero without the leading entry)



*A matrix could be transformed into multiple REF by row operation, but only one RREF.*



The pivot positions are the positions of leading entries in the origin matrix.

The pivot columns are the columns of each pivot positions.



**REFF v.s. Solutions**

* If RREF looks like [I b'], then it has an unique solution
* If there is at least one free variable, there are infinitely many solutions
* When an augmented matrix contains a row in which the only nonzero entry lies in the last column(in b'), then no solution



**Gaussian Elimination**

Matrix -> Original augmented matrix -> REF -> RREF, Solution√



**Checking Independence**

Ax = 0

augmented matrix = [Ax, 0] -> RREF -> Has at least an nonzero solution? -> dependent/independent?