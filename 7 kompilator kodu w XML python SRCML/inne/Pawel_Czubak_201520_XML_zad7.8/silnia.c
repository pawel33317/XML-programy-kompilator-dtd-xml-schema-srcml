#include <iostream>
using namespace std;


int main() {
	int n = 5;
    int silnia = 1;
  	while(n > 1){
    	silnia = silnia * n;
    	n = n-1;
	}
	cout<<"wynik: "<<silnia<<endl;
  	return 0;
}




