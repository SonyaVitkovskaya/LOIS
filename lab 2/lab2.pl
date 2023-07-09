state(left,left,left,left,_):-
	write('Result in reverse order: '),nl.

state(left,Wolf,Goat,Cabbage,_):-
	write('Try went empty on the right'),nl,
	not(dangerous_state(right,Goat, Cabbage)),
	not(dangerous_state(right,Wolf, Goat)),
	state(right,Wolf,Goat,Cabbage,nothing),
	write('Went empty on the right'),nl.

state(Ride_together,Ride_together,Goat,Cabbage,Last):-
	not(Last=wolf),opposite(Ride_together,Other_side),
	write('Try drove the wolf '),write(Other_side),nl,
	not(dangerous_state(Other_side,Other_side, Goat)),
	not(dangerous_state(Other_side,Cabbage, Goat)),
	state(Other_side,Other_side,Goat,Cabbage,wolf),
	concat('Drove the wolf ', Other_side, String), write(String),nl.

state(Ride_together,Wolf,Ride_together,Cabbage,Last):-
	not(Last=goat),opposite(Ride_together,Other_side),
	write('Try drove the goat '),write(Other_side),nl,
	not(dangerous_state(Other_side,Other_side, Wolf)),
	not(dangerous_state(Other_side,Other_side, Cabbage)),
	state(Other_side, Wolf, Other_side,Cabbage,goat),
	concat('Drove the goat ',Other_side,String), write(String),nl.

state(Ride_together,Wolf,Goat,Ride_together,Last):-
	not(Last=cabbage),opposite(Ride_together,Other_side),
	write('Try drove the cabbage '),write(Other_side),nl,
	not(dangerous_state(Other_side,Other_side, Goat)),
	not(dangerous_state(Other_side,Wolf, Goat)),
	state(Other_side,Wolf,Goat,Other_side,cabbage),
	concat('Drove the cabbage ', Other_side,String), write(String),nl.

dangerous_state(Man,Сomparison_object1, Сomparison_object2):-
	Сomparison_object1=Сomparison_object2,
    not(Сomparison_object2=Man),
    write('danger position'),nl,!.

opposite(left,right).
opposite(right,left).