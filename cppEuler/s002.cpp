#include <iostream>
#include <vector>

using namespace std;

int main(){
    int x = 1;
    int y = 2;
    int hek = 0;
    vector<int> hekFrik = {x, y};
    int penisButt = 0;

    while(hek < 4000000){
        hek = x + y;
        x = y;
        y = hek;
        hekFrik.push_back(hek);
    }

    for(int i = 0; i < hekFrik.size(); i++){
        int curr = hekFrik[i];
        if(curr % 2 == 0){
            penisButt += curr;
        }
    }

    cout << penisButt;

    return 0;
}

