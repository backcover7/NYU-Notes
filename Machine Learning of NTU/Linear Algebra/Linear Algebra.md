

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



Row aspect is intuition

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

![1.png](https://i.loli.net/2020/01/02/u1nd4SQUKyN9sRj.png)

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

Span of S = set of b



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

## RREF

### **RREF v.s. Linear Combination**

Column Correspondence Theorem

A[a1, ..., an] --[RREF]--> R[r1, ..., rn]

If aj is a linear combination of other columns of A, then rj is a linear combination of the corresponding columns of R with the same coefficients

a5 = -a1 + a4 <=> r5 = -r1 + r4



[Before starting]

<u>Intuition</u>: The three elementary row operations will not change the relationship between the columns. 

A --[RREF]--> R

[A b] --[RREF]--> [R b']



The RREF of matrix A is R, then Ax = b and Rx = b will probably not have the same solution.

The RREF of augmented matrix [A b] is [R b'], then Ax = b and Rx = b' will have the same solution.

The RREF of matrix A is R, Ax = 0 and Rx = 0 will have the same solution. Because the we just specified b the previous theory as zero vector. **[Definition of Column Correspondence Theorem]**

Then RREF will let us find the same linear combination relationships in columns between A and R.



Span of rows are the same, spans of columns are different

The relationship between the rows are changed, the relationship between the column are the same.

### **RREF v.s. Independent**

The pivot column(column containing leading entries) are linear independent.

The non-pivot columns are the linear combination of the previous pivot columns.



If a matrix is independent. Each column in RREF(A) is standard vector. RREF matrix looks like the following.
$$
\left[\begin{array}{c}
I \\
O \\
\end{array}\right]\  or \ [I \ *]
$$
More than m vectors in R^m must be dependent.

<u>[Intuition could be referred from the slide]</u>

### **RREF v.s. Rank**

**Rank = #pivot columns = #non-zero rows**

rank <= min(#columns, #rows)

**If rank = min(m, n), then the matrix is full rank.**

If a matrix is linear independent, then rank = n. But if m<n so that rank is less or equal than m. So the matrix is not independent.



If the matrix has solution.

**rank = non-zero row = #basic variables**

**nullity = #columns - rank = #free variables**

### **RREF v.s. Span**

If rank A ≠ rank [A b] -> no solution, because rank is #non-zero row.

Ax = b is consistent for every b <=> RREF[A b] cannot have a zero in the last column <=> RREF[A] cannot have zero row <=>  rank A = #row

So, Ax = b is consistent for every b <=> rank A = #row

**m independent vectors can span R^m => more than m vectors in R^m must be dependent.**



Full rank & rank = #columns

Ax = b has at most one solution; all columns are pivot columns.

Full rank & rank = #row

Ax = b has at least one solution; every row of R contains a pivot position.

## Matrix Multiplication

**Inner product**
$$
C_{m\times p} = A_{m\times n}B_{n\times p}\\
c_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + ... + a_{in}b_{nj}
$$
**Linear Combination of Columns and Rows**
$$
AB = A[b_1\ b_2\ ...\ b_p] = [Ab_1\ Ab_2\ ...\ Ab_p]
$$
**Composition**

Given two functions f and g, the function g(f()) is the composition of g○f

Matrix multiplication is the composition of two linear functions.

**Linear combination of rows**
$$
A = \left[\begin{array}{c}
a^T_1 \\
a^T_2 \\
...\\
a^T_m\\
\end{array}\right],\ 
B = \left[\begin{array}{c}
b^T_1 \\
b^T_2 \\
...\\
b^T_n\\
\end{array}\right]\\
C = \left[\begin{array}{c}
a_{11}b^T_1 + a_{12}b^T_2 + ... + a_{1n}b^T_n\\
a_{21}b^T_1 + a_{22}b^T_2 + ... + a_{2n}b^T_n\\
...\\
a_{m1}b^T_1 + a_{m2}b^T_2 + ... + a_{mn}b^T_n\\
\end{array}\right]
$$
**Summation of Matrices**
$$
A = \left[\begin{array}{c}
a_1 & a_2 & ... & a_n\\
\end{array}\right],\ 
B = \left[\begin{array}{c}
b^T_1 \\
b^T_2 \\
...\\
b^T_n\\
\end{array}\right]\\
C = a_1b^T_1 + a_2b^T_2 + ... + a_nb^T_n
$$
\***Block Multiplication**

1. Partition 
2. Produce

**Properties**

AB ≠ BA



Let A and B be k*x matrices, C be an m\*n martix, and P and Q be n\*p matrices

s(AC) = (sA)C = A(sC)

(A+B)C = AC + BC

C(P+Q) = CP + CQ

IA = A = AI

matrix * O = O

A^1 = A, A^0 = I, A^k = AAA...A(k times)

A(CP) = (AC)P



Let A be k*m matrices, C be an m\*n matrix

(AC)^T = C^T * A^T

**Special Matrix**

* Diagonal Matrix: 只有对角线有值

* Symmetric Matrix: A^T = A
  $$
  AA^T\ and\ A^TA\ are\ sqaure\ and\ symmetric.\\
  (AA^T)^T = A^{TT}A^T = AA^T\\
  (A^TA)^T = A^TA^{TT} = A^TA
  $$
  

## Inverse Matrix

Two function f and g are inverse
$$
f = g^{-1}\\
g = f^{-1}
$$
If B is an inverse of A, then A is an inverse of B
$$
Bv = x\\
Ax = y\\
y = v\\
AB = I\\
$$

$$
Av = x \\
Bx = y\\
y = v\\
BA = I\\
$$

$$
If AB = I \& BA = I,\ then\ A\ and\ B\ are\ inverse\ to\ each\ other\\
B = A^{-1}\\
A = B^{-1}
$$

* A is invertible then A is non-singular, otherwise A is singular.

* Non-square matrix cannot be invertible.

* Not all square matrix is invertible

* Inverse is unique. A and B are inverse to each other, A will not be inverse to any other matrix.

* A and B are inverse to each other, then AB is invertible, too
  $$
  (AB)^{-1} = B^{-1}A^{-1}
  $$
  [Proof]
  $$
  B^{-1}A^{-1}(AB) = B^{-1}(A^{-1}A)B = B^{-1}B =I\\
  (AB)B^{-1}A^{-1} = A(BB^{-1})A^{-1} = AA^{-1} =I\\
  $$

* A1, A2, ..., AK are invertible. The product is invertible, too.

* If A is invertible, A^T is invertible, too.
  $$
  (A^T)^{-1} = (A^{-1})^T
  $$
  

The inverse can be used to solve system of linear equations

Ax = b, if A is invertible
$$
A^{-1}(Ax) = A^{-1}b\\
(A^{-1}A)x = A^{-1}b\\
I_nX = A^{-1}b\\
x = A^{-1}b
$$

##  Invertible

Let A be an n*n matrix. A is invertible if and only if

* The columns of A span R^n
* For every b in R^n, the system Ax = b is consistent
* The rank of A is n
* The columns of A are linear independent
* The only solution to Ax = 0 is the zero vector
* The nullity of A is zero
* The RREF of A is I
* A is a product of elementary matrices
* There exists an n*n matrix B such that BA = I
* There exists an n*n matrix C such that AC = I



If co-domain is smaller than the domain, function f cannot be one-to-one.

If a matrix is m<n, it cannot be one-to-one.

The reverse is not true.

If a matrix A is one-to-one, its columns are independent.



A function f is onto(co-domain = range), then f always has solution.

If co-domain is larger than the domain, f cannot be onto.

If a matrix A is m>n, it cannot be onto.

The reverse is not true.

If a matrix A is onto, rank A = #rows.



**If A is invertible, A must be one-to-one and onto.**

A function is one-to-one and onto, the domain and co-domain must have the same size.

So, if a matrix is squared, then it will be both one-to-one and onto, or either one-to-one and onto.



Let A be an n*n matrix

If A is one-to-one or onto, then A is invertible.

**Onto**

* The columns of A span R^n
* For every b in R^n, the system Ax = b is consistent
* The rank of A is #row

**One-to-one**

* The columns of A are linear independent
* The rank of A is #columns
* The nullity of A is zero
* The only solution to Ax = 0 is the zero vector
* **The RREF of A is I**



**An n*n matrix A is invertible <=> There exists an n\*n matrix B such that BA = I**

**An n*n matrix A is invertible <=> There exists an n\*n matrix B such that AC = I**

## Inverse of Elementary Matrices

1. Interchange
   $$
   \left[\begin{array}{c}
   0 & 1\\
   1 & 0
   \end{array}\right]
   \left[\begin{array}{c}
   a & b\\
   c & d
   \end{array}\right]=
   \left[\begin{array}{c}
   c & d\\
   a & b
   \end{array}\right]
   $$
   
2. Scaling
   $$
   \left[\begin{array}{c}
   1 & 0\\
   0 & k
   \end{array}\right]
   \left[\begin{array}{c}
   a & b\\
   c & d
   \end{array}\right]=
   \left[\begin{array}{c}
   a & b\\
   kc & kd
   \end{array}\right]
   $$
   
3. Adding k times row i to row j
   $$
   \left[\begin{array}{c}
   1 & 0\\
   k & 1
   \end{array}\right]
   \left[\begin{array}{c}
   a & b\\
   c & d
   \end{array}\right]=
   \left[\begin{array}{c}
   a & b\\
   ka+c & kb+d
   \end{array}\right]
   $$

All of the previous matrix is elementary matrix.



EA => exchange the 1st and 2nd rows of A

EI => exchange the 1st and 2nd rows of I & EI = E => exchange the 1st and 2nd rows of I then we get E.

Just do operations on I.



**Inverse of Elementary Matrix**
$$
E = \left[\begin{array}{c}
1 & 0 & 0\\
0 & -4 & 0\\
0 & 0 & 1
\end{array}\right] <=>
E^{-1} = \left[\begin{array}{c}
1 & 0 & 0\\
0 & -\frac{1}{4} & 0\\
0 & 0 & 1
\end{array}\right]
$$
RREF v.s. Elementary Matrix
$$
E_k...E_2E_1A = RREF(A) = R
$$
There exists an invertible m*m matrix P such that PA = R
$$
P = E_k...E_2E_1
$$
A is invertible <=> R = RREF(A) = I <=> A is a product of elementary matrices
$$
E_k...E_2E_1A = I\\
A = E_1^{-1}E_2^{-1}...E_k^{-1}I\\
A = E_1^{-1}E_2^{-1}...E_k^{-1}
$$
**Inverse of General Matrices**

RREF(A) = I if A is invertible.
$$
E_k...E_2E_1A = I\\
E_k...E_2E_1 = A^{-1}
$$
**[R B] = RREF([A I]), R, B, A, I are all n dimension.**

**If R = I, then A is invertible and B = A^{-1}.**

[Proof]
$$
E_k...E_2E_1[A\ I] = [R\ E_k...E_2E_1] = [I\ A^{-1}]
$$
To find A^{-1}C, transform [A C] into its RREF [R C']. C' = A^{-1}C
$$
E_k...E_2E_1[A\ C] = [R\ E_k...E_2E_1C] = [I\ A^{-1}C]
$$

## Subspace

A vector set V is called a subspace if

1. The zero vector 0 belongs to V
2. If u and w belong to V, then u+w belongs to V (Closed under vector addition)
3. If u belongs to V, and c is a scalar, then cu belongs to V (Closed under scalar multiplication)

*2+3 is linear combination; 1 is mean to ignore null set.*
$$
Example\ of\ Subspace:W = \left\{\left[\begin{array}{c}
\omega_1\\
\omega_2\\
\omega_3
\end{array}\right]
\in R^3: 6\omega_1-5\omega_2+4\omega_3=0
\right\}
$$
*{0} is zero subspace



**Subspace v.s. Span**

The span of a vector set is a subspace.

<u>Span <=> Subspace</u>



**Null Space**

The null space of a matrix A is the solution set of Ax = 0. It's denoted as Null A.
$$
Null\ A = \{v \in R^n: Av = 0\}
$$
The solution set of the homogeneous linear equations Av = 0.

Null A is a subspace.

**Column Space and Row Space**

Column space of a matrix A is the span of its columns. It's denoted as Col A.
$$
A \in R^{m\times n} => Col\ A = \{Av: v\in R^n\}
$$
If matrix A represents a function. Col A is the range of the function.

Row space of a matrix A is the span of its rows. It's denoted as Row A.
$$
Row\ A = Col\ A^T
$$
**RREF**

Col A ≠ Col R

Row A = Row R

**Consistent**

* Ax = b have solution
* b is the linear combination of columns of A
* b is in the span of the columns of A
* b is in Col A

## Basis

Let V be a nonzero subspace of R^n, a basis B for V is a <u>linearly independent</u> <u>generation set</u> of V.

**V = Span B & B is independent**

{e1, e2, ..., en} is a basis for R^n		#ei are all standard vector.

*Any two independent vectors form a basis of R^2



The pivot columns of a matrix form a basis for its column space.

**Property**

* S is contained in Span S

  Basis is always in its subspace

* If a finite set S' is contained in Span S, then Span S' is also contained in Span S

  Because Span S is a subspace

* For any vector z, Span S = Span S∪{z} if and only of z belongs to the Span S

**Theorem**

* A basis is the smallest generation set
* A basis is the largest independent vector set in the subspace
* Any two bases for a subspace contain the same number of vectors
  * The number of vectors in a basis for a nonzero subspace V is called dimension of V (dim V)

*dim V: dimension of V

**Reduction Theorem**

There is a basis containing in any generation set S.

**Extension Theorem**

Given an independent vector set S in the subspace, S can be extended to a basis by adding more vectors.



**<u>Generation set --[delete]--> basis <--[add]-- Independent set</u>**



**Confirming that a set is a Basis**

Already know dim V = km, suppose S is a subset of V with k vectors

* If S in independent -> S is basis
* If S is a generation set -> S is basis

## Subspaces associated with a Matrix

**Col Space**

Basis: pivot columns

Dim(Col A) = #pivot columns = rank

<u>Rank A</u>

- Maximum number of independent columns
- #pivot columns
- #non-zero rows
- #basic variables
- Dim(Col A) = Dim(Row A)
- Dimension of the range of A = Dim(Col A^T)

**Null Space**

RREF(A) -> parametric representation -> find the vector values of basic variables -> form basis

Dim(Null A) = #free variables = Nullity A = n - rank A

**Row Space**

Basis: nonzero rows of RREF(A)

Dim(Row A) = #nonzero rows of RREF = rank



rank A = rank A^T

Dim of Range + Dim of Null = Dim of Domain

## Coordinate System

**Different viewpoints**

The same vector is represented differently in different coordinate system.

Different vectors can have the same representation in different coordinate system.



A vector set B can be considered as a coordinate system for R^n if

1. The vector set B spans the R^n
2. The vector set B is independent

**B is a basis of R^n**

B-coordinate vector of v: 
$$
[v]_\beta
$$
Given [v]B, how to find v Cartesian coordinate system
$$
[v]_\beta =
\left[\begin{array}{c}
c_1\\
c_2\\
...\\
c_n
\end{array}\right]
$$

$$
v = c_1u_1 + c_2u_2 + ... + c_nu_n = B[v]_B
$$

Given cartesian, find representation in B-coordinate system
$$
[v]_B = B^{-1}v
$$
*B is invertible

**Let B = {b1, b2, ..., b2} be a basis of R^n. [bi]B = ei**

**Change Coordinates**

e.g. rotate the oval

## Linear Function in Coordinate System

Complex function in cartesian coordinate system may be simpler in another coordinate system.
[T] = B\*[T]B\*B^{-1}
[T]B = B^{-1}\*[T]B\*B

[T]B is similar with [T]B

## Determinant

The determinant of a square matrix is a scalar that provides information about the matrix. 
$$
A =
\left[\begin{array}{c}
a & b\\
c & d
\end{array}\right]
\\det(A) = ad - bc
$$

$$
A =
\left[\begin{array}{c}
a_1 & a_2 & a_3\\
a_4 & a_5 & a_6\\
a_7 & a_8 & a_9
\end{array}\right]
\\det(A) = a_1a_5a_9 + a_2a_6a_7 + a_3a_4a_8 - a_3a_5a_7 -a_2a_4a_9 - a_1a_6a_8
$$

Cofactor Expansion

aij is the entry.

Aij is the submatrix of A obtained by removing the i-th row and j-th column, Aij is size of (n-1)*(n-1)

1. Pick row 1
   $$
   detA = a_{11}c_{11} + a_{12}c_{12} + ... + a_{1n}c_{1n}
   $$

2. Or pick row i
   $$
   detA = a_{i1}c_{i1} + a_{i2}c_{i2} + ... + a_{in}c_{in}
   $$

3. Or pick column j
   $$
   detA = a_{1j}c_{1j} + a_{2j}c_{2j} + ... + a_{nj}c_{nj}
   $$

Cofactor
$$
c_{ij}: (i,j)-cofactor\\
c_{ij} = (-1)^{i+j}detA_{ij}
$$
*tridiagonal matrix & digonal matrix

**Properties**

* det(I) = I
* Exchange rows only reverses the sign of det (do not change absolute value)
* Determinant is "linear" for <u>each row</u>

*Area in 2d and Volume in 3d have the above properties
$$
det\left(\left[\begin{array}{c}
ta & tb\\
c & d
\end{array}\right]\right) =
tdet\left(\left[\begin{array}{c}
a & b\\
c & d
\end{array}\right]\right)
$$

$$
det\left(\left[\begin{array}{c}
a+a' & b+b'\\
c & d
\end{array}\right]\right) =
det\left(\left[\begin{array}{c}
a & b\\
c & d
\end{array}\right]\right) + 
det\left(\left[\begin{array}{c}
a' & b'\\
c & d
\end{array}\right]\right)
$$

$$
det(A+B) \neq detA + detB
$$

Upper triangular matrix

det(U) = det(only triangle) = d1d2...dn*det(I)

**determinants v.s. invertible**

A is invertible <=> det(A) ≠ 0

**Other properties**

det(AB) = det(A)det(B)

det(A^-1) = 1/det(A)

det(A62) = (det(A))^2

det(A^T) = det(A)

**Cramer's Rule**
$$
A^{-1} = \frac{1}{det(A)}C^T
$$

* det(A): scalar
* C: cofactors of A(C has the same size as A, so does C^T)
* C^T is adjugate of A

[Proof]
$$
AC^T = det(A)I_n
$$

## Eigenvalues and Eigenvectors

Eigen: "unique" or "belonging to"

If Av = λv (v is a vector, λ is a scalar), A must be square

- v is an eigenvector of A excluding zero vector
- λ is eigenvalue of A corresponds to v 

T is a linear operator. If T(v) = λv(v is a vector, λ is a scalar)

* v is an eigenvector of T excluding zero vector
* λ is an eigenvalue of T that corresponds to v

**How to find eigenvector(given eigenvalue)?**

An eigenvector of A corresponds to a unique eigenvalue 

An eigenvalue of A has infinitely many eigenvectors

**Eigenspace**

Av - λv = 0

Av - λIv = 0

Eigenspace of λ: Nonzero solution of (A - λI)v = 0 => **Null(A-λI)**-{0}

**Check Eigenvalues**

Check the dimension of eigenspace of λ. If the dimension is 0, eigenspace only contains {0}, it means no eigenvector so λ is not the eigenvalue.

*Check Null(A-λI)

**Looking for Eigenvalues**

A scalar t is an egienvalue of A

<=> Existing v ≠ 0 such that Av = tv

<=> Existing v ≠ 0 such that Av - tv = 0

<=> Existing v ≠ 0 such that (A - tI)v = 0

<=> (A-tI)v = 0 has multiple solution

<=> The columns of (A-tI) are dependent

<=> (A - tI) is not invertible

<=> **det(A - tI) = 0**

Trace(A) = Sum(eigenvalues)

**Characteristic Polynomial**: det(A-tI)

**Characteristic Equation**: det(A-tI)=0

Eigenvalues are the roots of characteristic polynomial or solutions of characteristic equation.



* In general, a matrix A and RREF of A have different characteristic polynomials.

* Similar matrices have the same characteristic polynomials.

  B = P^-1 A P; A = P^-1 B P

* The characteristic polynomial of an n*n matrix is indeed a polynomial with degree n

* An n*n matrix A have less than or equal to neigenvalues

## Diagonalization

An n*n matrix A is called diagonalizable if
$$
A = PDP^-1
$$

* D: n*n diagonal matrix
* P: n*n invertible matrix

*Not all matrices are diagonlizable
$$
A^2 = PD^2P^-1
$$

$$
Ap_i = d_ip_i
$$

pi is an eigenvector of A corresponding to eigenvalue di

There are n eigenvectors that form an invertible matrix => There are n independent eigenvectors => The eigenvectors of A can form a basis for R^n if A is diagonalizable.

A set of eigenvectors that correspond to distinct eigenvalues is linear independent.

## Page Rank

Ax = x

The solution x is in the eigenspace of eigenvalue λ = 1

## Orthogonality

**Dot product**
$$
u\cdot v = u_1\cdot v_1 + u_2\cdot v_2 + ... + u_n\cdot v_n
$$
**u and v are orthogonal if u·v = 0**

* Orthogonal is actually "perpendicular"
* Zero vector is orthogonal to every vector

$$
||v||_p = (\sum_{i=1}^{n}|v_i|^p)^{\frac{1}{p}}\\
||v||_1 = |v_1| + |v_2| + ... + |v_n|\\
||v||_2 = \sqrt{(v_1)^2 + (v_2)^2 + ... + (v_n)^2}\\
||v||_3 = \sqrt[3]{(v_1)^3 + (v_2)^3 + ... + (v_n)^3}\\
||v||_4 = \sqrt[4]{(v_1)^4 + (v_2)^4 + ... + (v_n)^4}
$$

**More about Dot Product**
$$
u\cdot u = ||u||^2\\
u\cdot u = 0\ if\ and\ only\ if\ u = 0\\
u\cdot v = v\cdot u\\
u\cdot (v+w) = u\cdot v + u\cdot w\\
(v+w)\cdot u = v\cdot u + w\cdot u\\
(cu)\cdot v = c(u\cdot v) = u\cdot (cv)\\
||cu|| = |c|||u||\\
Au\cdot v = (Au)^Tv = u^T(A^Tv) = u\cdot A^Tv
$$
**Pythagorean Theorem**

* u and v are orthogonal

$$
||u + v||^2 = ||u||^2 + ||v||^2
$$

* The diagonals of a parallelogram are orthogonal, the parallelogram is a rhombus

**Triangle Inequality**

For any vectors u and v,
$$
||u+v|| \leq ||u|| + ||v||
$$

## Orthogonal Projection

**Orthogonal Complement**

The orthogonal complement of a nonempty vector set S is denoted as S perp.

S perp is the set of vectors that are orthogonal to every vector in S.

$$
S^\perp = \{v:v\cdot u = 0, \forall u \in S\}
$$
e.g.
$$
S = R^n => S^\perp = {0}\\
S = {0} => S^\perp = R^n
$$
**Properties of Orthogonal Complement**

* S perp is always a subspace
* For any nonempty vector set S, span S perp = S perp
* Let W be a subspace, and B be a basis of W => B perp = W perp
* Intersection of S and S perp is zero vector



**For any matrix A**
$$
(Row\ A)^\perp = Null\ A\\
(Col\ A)^\perp = Null\ A^T = Row\ A^T perp
$$


**For any subspace W of R^n,** 
$$
dimW + dimW^\perp = n
$$

$$
u = w + z\\
w \in W\\
z \in W^\perp
$$


**Orthogonal Projection**
$$
u = w + z\\
U_W(u) = w
$$
w in subspace W is closest to vector u

z is always orthogonal to all vectors in W

**Closest Vector Properties**

Among all vectors in subspace W, the vector closest to u is the orthogonal projection of u onW.



Orthogonal projection operator is linear, find the orthogonal projection matrix P

Orthogonal Projection Matrix

Let C be an n*k matrix whose columns form a basis for a subspace W.
$$
P_W = C(C^TC)^{-1}C^T
$$
Let C be a matrix with linearly independent columns. Then C^TC is invertible.

**Solutions of Inconsistent System of Linear Equations**

* Suppose Ax = b is an inconsistent system of linear equations
* b is not in the column space of A
* Find vector z minimizing ||Az-b||

Col A is W, find orthogonal projection of b in W. Az = Pb

![2.png](https://i.loli.net/2020/01/02/m1DZMENvbYX7riw.png)

Error Vector:
$$
e =
\left[\begin{array}{c}
y_1 - (a_0 + a_1x_1)\\
y_2 - (a_0 + a_1x_2)\\
...\\
y_n - (a_0 + a_1x_n)\\
\end{array}\right]
$$
Find a0 and a1 minimizing E
$$
E = ||e||^2\\
E = [y_1 - (a_0 + a_1x_1)]^2 + [y_2 - (a_0 + a_1x_2)]^2 + ... +[y_n - (a_0 + a_1x_n)]^2
$$

$$
e = y - a_0v_1 - a_1v_2\\
y\triangleq
\left[\begin{array}{c}
y_1\\y_2\\...\\y_n
\end{array}\right],
v_1\triangleq
\left[\begin{array}{c}
1\\1\\...\\1
\end{array}\right],
v_2\triangleq
\left[\begin{array}{c}
x_1\\x_2\\...\\x_n
\end{array}\right]
$$

$$
C\triangleq [v_1\ v_2], and\ a =
\left[\begin{array}{c}
a_0\\a_1
\end{array}\right],
$$

$$
E = ||y-(a_0v_1+a_1v_1)||^2 = ||y-Ca||^2
$$

y = Ca is inconsistent.

$$
B = {v_1, v_2}
$$

Ca is the orthogonal projection of y on W = Span B

find a such that Ca = Py
$$
\left[\begin{array}{c}
a_0\\a_1
\end{array}\right] = (C^TC)^{-1}C^Ty
$$

## Orthogonal Basis

**Orthogonal Set**

* A set of vectors is called an orthogonal set of every pair of distinct vectors in the set is orthogonal.
* *By definition, a set with only one vector is an orthogonal set.
* Any orthogonal set of nonzero vectors is linearly independent.

**Orthonormal Set**

A set of vectors is called an orthonormal set if it is an orthogonal set, and the norm of all the vectors is 1.

Orthonormal set is independent.



*A vector that has norm equal to 1 is called a unit vector.



* An orthogonal set is called an orthogonal basis.
* An orthonormal set is called an orthonormal basis.



Orthogonal basis of R^3

Orthonormal basis of R^3
$$
\left[\begin{array}{c}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{array}\right]
$$
Let  S = {v1, v2, ..., vk} be an orthogonal basis for a subspace W, and let u be a vector in W
$$
u = c_1v_1 + c_2v_2 + ... + c_kv_k
$$

$$
c_i = \frac{u\cdot v_i}{||v_i||^2}
$$

If S is an orthonormal basis
$$
c_i = u\cdot v_i
$$
If C in project matrix is orthogonal basis, P = CD^-1C^T



Let {u1, u2, ..., uk} be a basis of a subspace V. Transform {u1, u2, ..., uk} into an orthogonal basis {v1, v2, ..., vk}
$$
v_1 = u_1\\
v_k = u_k - \frac{u_k\cdot v_1}{||v_1||^2} v_1 - \frac{u_k\cdot v_2}{||v_2||^2} v_2 - ... - \frac{u_k\cdot v_k}{||v_{k-1}||^2} v_{k-1}
$$
Span {v1, v2, ..., vi} = Span {u1, u2, ..., ui}

## Orthogonal Matrices & Symmetric Matrices

**Norm-preserving**

A linear operator is norm-preserving if 
$$
||T(u)|| = ||u||\ For\ all\ u
$$
Orthogonal matrix

* An n*n matrix Q is called an orthogonal matrix (or simply orthogonal) if the columns of Q form an <u>orthonormal basis</u> for R 

* Orthogonal operator: standard matrix is an orthogonal matrix. 

**Norm-preserving <=> Orthogonal matrix**

Let P and Q be n*n orthogonal matrices

* detQ = 1 or -1
* PQ is an orthogonal matrix
* Q^-1 is an orthogonal matrix
* Q^T is an orthogonal matrix

Orthogonal operator

T is an orthogonal operator,

* T(u) · T(v) = u · v for all u and v
* ||T(u)|| = ||v|| for all v
* T and U are orthogonal operators, then TU and T^-1 are orthogonal operators.



**The eigenvalues for symmetric matrices are always real.**

A is symmetric <=> P^TAP = D

*P is an orthogonal matrix, D is a diagonal matrix

## SVD

Any m*n matrix A

A = UΣV^T

A m*n

U m*m, orthonormal set, independent

Σ m*n, diagonal, decreasing

V^T n*n, orthonormal set, independent



Rank(AB) = min(Rank(A), Rank(B))

