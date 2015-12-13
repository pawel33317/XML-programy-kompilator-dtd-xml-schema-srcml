Program filozofy;
var	widelec:array[0..4] of binary_semaphore;
	lokaj: semaphore
	i: integer;
procedurę filozof(i:integer)
begin
	repeat
		mysl;
		wait(lokaj)lokaj;
		wait(widelec[i]);
		wait(widelec[(i+1)mod 5]);
		jedz;
		signal(widelec[i]);
		signal(widelec[(i+1)mod 5]);
		signal lokaj;
	forever
end
