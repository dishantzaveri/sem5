female(dishant).
female(dipti).
female(g1).
female(g2).
male(dhruv).
male(parag).
male(gm1).
male(gm2).
parent(parag,dishant).          
parent(parag,dhruv).
parent(dipti,dishant).
parent(dipti,dhruv).
parent(gm1,parag).
parent(g1,parag).
parent(gm2,dipti).
parent(g2,dipti).
grandparent(X,Y):-parent(X,Z),parent(Z,Y).
grandmother(X,Z):-mother(X,Y),parent(Y,Z).
grandfather(X,Z):-father(X,Y),parent(Y,Z).
mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
haschild(X):- parent(X,_).
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
wife(X,Y):-parent(X,Z),parent(Y,Z),female(X),male(Y).
husband(X,Y):-parent(X,Z),parent(Y,Z),female(Y),male(X).
