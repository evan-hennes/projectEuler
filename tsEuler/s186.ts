const calls = new Map<number, Set<number>>();
const pmNum = 524287;
const connections = new Set<number>();
let numConnected = 0;
let numSuccessful = 0;

const memoize = <P,R>(fn: (param: P) => R): ((param: P) => R) => {
    const cache = new Map<P, R>();
    return (p : P) => {return(!cache.has(p) ? cache.set(p, fn(p)).get(p)! : cache.get(p)!);};
}

const lfib = memoize((k : number) : number => {
    if(1 <= k && k <= 55) return (100003 - (200003 * k) + (300007 * (k ** 3))) % 1000000;
    return (lfib(k - 24) + lfib(k - 55)) % 1000000;
});

const checkConnections = (n : number) => {
    return n;
}

let i = 1;
let pmCaller = 0;
while(numConnected / numSuccessful != 0.99){
    const caller = lfib((2 * i) - 1);
    const called = lfib(2 * i);
    if(caller === called){
        console.log('misdial');
    }else{
        numSuccessful++;
        if(calls.has(caller)){
            const arr = calls.get(caller)!.add(called);
            calls.set(caller, arr);
        }else{
            const arr = new Set<number>();
            arr.add(called);
            calls.set(caller, arr);
        }
        if(caller === pmNum || called === pmNum){
            console.log('direct connection');
            pmCaller = caller;
            break;
        }
    }
    i++;
    if(pmCaller != 0){
        console.log(i);
        break;
    }
}
checkConnections(pmCaller);
console.log(connections.size / numSuccessful);