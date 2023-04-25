import { DisjointSetUnion, memoize } from "./useful.ts";

const dsu = new DisjointSetUnion(1000000);
const pmNum = 524287;
let numConnected = 0;
let numSuccessful = 0;

const lfib = memoize((k : number) : number => {
    if(1 <= k && k <= 55) return (100003 - (200003 * k) + (300007 * (k ** 3))) % 1000000;
    return (lfib(k - 24) + lfib(k - 55)) % 1000000;
});

let i = 1;
while(numConnected / numSuccessful != 0.99){
    const caller = lfib((2 * i) - 1);
    const called = lfib(2 * i);
    if(caller === called){
        console.log('misdial');
    }else{
        numSuccessful++;
        dsu.union(caller, called);
        if(i > 7000000){
            break;
        }
    }
    i++;
}
console.log(dsu.dsu);
//console.log(dsu.size);