
#include <bits/stdc++.h>
using namespace std;
 
bool is_prime(int n){
    if(n==0 || n==1){
        return false;
    }
    for (int i = 2; i*i<=n; ++i)
  {
      /* code */
    if(n%i==0){
        return false;
    }
  }
  return true;
}
int main(void)
{
  int n ;
  cin>>n;
  bool t = is_prime(n);
  if(t){
      cout<<n <<" is the prime number"<<endl; 
  }
  else{
cout<<n <<" is not the prime number"<<endl;
  }

    return 0;
}