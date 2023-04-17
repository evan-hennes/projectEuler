const callers = new Array<number>();
const called = new Array<number>();
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

let numConnected = 0;
let numSuccessful = 0;
for(let i = 1; i <= 1000000; i++){
    const caller = lfib(2 * i - 1);
    const called = lfib(2 * i);
    if(caller != called){
        numSuccessful++;
        if(caller == pmNum || called == pmNum){
            numConnected++;
            if(numConnected / numSuccessful == 0.99){
                console.log("donezo");
            }else{
                console.log(numConnected / numSuccessful);
            }
        }else{
            console.log('womp womp');
        }
    }else{
        console.log("alpha cure mom");
    }
}