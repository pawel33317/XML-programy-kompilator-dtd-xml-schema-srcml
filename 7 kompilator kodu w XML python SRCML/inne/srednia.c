#include <iostream>
using namespace std;

int main() {
	int t[] = {2,3,4,3,2,3,4,5,6,4,3};
	int tlen = 11;
	int i = 0;
	double wynik = 0;
	while (i < tlen){
		wynik = wynik + t[i];
		i=i+1;
	}
	wynik = wynik / tlen;
	cout << wynik;

}




