# Transformation-of-2D---Geometric-Objects
An ​interactive python program ​interactive python program ​to applytransformations (both linear and non - linear) to an object and plot it using ​matplotlib.matplotlib.
The program supports the following objects:-A Disc (of radius ​r​r​ centered at ​(a,b)​(a,b)​ )
                                           -A polygon (vertices of which are specified by lists ​X​X​ and ​Y​Y​)
Input
The first contains the word ​‘disc​‘disc​’ or ​‘polygon​‘polygon​’ denoting the figure you have to use.If the word is ‘​disc’​disc’​, the next line contains three space-separated integers ​a b r ​a b r ​as specifiedabove.If the word is ​‘polygon​‘polygon​’, the next ​two lines ​two lines ​contain space separated lists ​X[]​X[]​ and ​Y[]​Y[]​ of equallength, denoting the x-y co-ordinates of the vertices of the polygon.The next few lines contain a single query each, denoting the transformation you have to perform.
Each query will be of the form:--S x y : ​S x y : ​scale the object by a factor of ​x​x​ along the x-axis, and ​y​y​ along the y-axis.--R theta : ​R theta : ​rotate the object by angle theta(in degrees, 0 <= theta <= 360) in thecounter-clockwise​counter-clockwise​ direction about the origin.--T dx dy : ​T dx dy : ​translate the object by ​dx​dx​ units along the x-axis, and by ​dy ​dy ​units along the y-axis.Each transformation has to be performed on the shape obtained as a result of all the previoustransformations, ie the effect of the transformations should be cumulative.The final line of the input contains the word ​‘quit​‘quit​’, denoting that no further transformations arerequired and you should exit the program.

Output
Input object plots according to the input specifications.For each transformation:-
prints the new resulting parameters(​a b r​a b r​ for disc and ​x[] y[]​x[] y[]​ for polygon) of the object in theformat specified in the input.
-updates the plot to show the new object position
