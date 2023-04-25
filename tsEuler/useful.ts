// disjoint set union class for faster graph manipulation
export class DisjointSetUnion {
    dsu : Array<number>;
    size : Array<number>;

    constructor(n : number){
        this.dsu = Array.from(Array<number>(n).keys());
        this.size = new Array<number>(n).fill(1);
    }

    find = (n : number) : number => {
        if(this.dsu[n] === n) return n;
        return this.dsu[n] = this.find(this.dsu[n]);
    }

    union = (n1 : number, n2 : number) => {
        const n1Parent = this.find(n1);
        const n2Parent = this.find(n2);
        if(n1Parent == n2Parent){
            return;
        }
        if(this.size[n1Parent] >= this.size[n2Parent]){
            this.size[n1Parent] += this.size[n2Parent];
            this.dsu[n2Parent] = n1Parent;
        }else{
            this.size[n2Parent] += this.size[n1Parent];
            this.dsu[n1Parent] = n2Parent;
        }
    }
    
    sameset = (n1 : number, n2 : number) : boolean => {
        return this.find(n1) === this.find(n2);
    }
}

// memoize function w/ one parameter of type P and return value of type R; big useful
export const memoize = <P,R>(fn: (param: P) => R) : ((param: P) => R) => {
    const cache = new Map<P, R>();
    return (p : P) => {return(!cache.has(p) ? cache.set(p, fn(p)).get(p)! : cache.get(p)!);};
}