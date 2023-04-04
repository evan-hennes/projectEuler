#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> muls;
    int mulSum = 0;
    for(int i = 0; i < 1000; i++){
        if(i % 3 == 0 || i % 5 == 0){
            muls.push_back(i);
        }
    }
    for(unsigned long int i = 0; i < muls.size(); i++){
        mulSum += muls[i];
    }
    cout << mulSum;

    return 0;
}
