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

