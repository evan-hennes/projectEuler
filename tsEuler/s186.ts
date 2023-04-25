import { DisjointSetUnion, memoize } from "./useful.ts";

const dsu = new DisjointSetUnion(1000000);
const pmNum = 524287;
let numConnected = 1;
let numSuccessful = 0;

const lfib = memoize((k : number) : number => {
    if(1 <= k && k <= 55) return (100003 - (200003 * k) + (300007 * (k ** 3))) % 1000000;
    return (lfib(k - 24) + lfib(k - 55)) % 1000000;
});

let i = 1;
while(numConnected / 1000000 < 0.99){
    const caller = lfib((2 * i) - 1);
    const called = lfib(2 * i);
    if(caller === called){
        i++;
        continue; //misdial case; do nothing
    }else{
        numSuccessful++;
        dsu.union(caller, called);
        const size = dsu.size[dsu.find(pmNum)];
        if(size != numConnected){
            numConnected = size;
        }
        if(numConnected / 1000000 >= 0.99){
            break;
        }
    }
    i++;
}
console.log(numSuccessful);