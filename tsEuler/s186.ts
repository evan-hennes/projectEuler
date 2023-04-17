const calls = new Map<number, Set<number>>();
const pmNum = 524287;

const memoize = <P,R>(fn: (param: P) => R): ((param: P) => R) => {
    const cache = new Map<P, R>();
    return (p : P) => {
        if(cache.get(p) === undefined){
            cache.set(p, fn(p));
            return cache.get(p)!;
        }else{
            return cache.get(p)!;
        }
    }
}

const lfib = memoize((k : number) : number => {
    if(1 <= k && k <= 55){
        return (100003 - (200003 * k) + (300007 * (k ** 3))) % 1000000;
    }else{
        return (lfib(k - 24) + lfib(k - 55)) % 1000000;
    }
});

const checkConnection = (conn : number, n : number) => {
    
}

let numConnected = 0;
let numSuccessful = 0;
for(let i = 1; i <= 1000000; i++){
    const caller = lfib((2 * i) - 1);
    const called = lfib(2 * i);
    if(caller === called){
        console.log('misdial');
    }else{
        if(calls.has(caller)){
            const arr = calls.get(caller)!.add(called);
            calls.set(caller, arr);
        }else{
            const arr = new Set<number>();
            arr.add(called);
            calls.set(caller, arr);
        }
    }
}
console.log('done');