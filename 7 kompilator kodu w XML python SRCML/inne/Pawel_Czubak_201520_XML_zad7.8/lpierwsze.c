#include<iostream>
#include<cstdlib>
using namespace std;

bool czy_pierwsza(int n)
{
  if(n<2)
    return false;

  int i = 2;
  int ii = 0;
  int z=0;
  
  ii=i*i;
  
  while(ii<=n){
  	z=n%i;
    if(z==0)
      return false;
    i = i + 1;
	ii = i * i;
  }
  return true;
}

int main()
{
  int n = 100;
  int i = 0;
  
  while(i <= n){
  	if(czy_pierwsza(i) == true){
  		cout<<"Liczba "<<i<<" jest pierwsza"<<endl;
	}
	i = i + 1;
  }
  return 0;
}