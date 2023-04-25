const dsu = Array.from(Array<number>(1000000).keys());
const pmNum = 524287;
let numConnected = 0;
let numSuccessful = 0;

const find = (n : number) : number => {
    if(dsu[n] === n){
        return n;
    }
    return dsu[n] = find(dsu[n]);
}

const union = (n1 : number, n2 : number) => {
    const n1u = find(n1);
    const n2u = find(n2);
    if(n1u !== n2u){
        dsu[n2u] = n1u;
    }
}

const sameset = (n1 : number, n2 : number) : boolean => {
    return find(n1) === find(n2);
}

const memoize = <P,R>(fn: (param: P) => R): ((param: P) => R) => {
    const cache = new Map<P, R>();
    return (p : P) => {return(!cache.has(p) ? cache.set(p, fn(p)).get(p)! : cache.get(p)!);};
}

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
        
    }
    i++;
}
