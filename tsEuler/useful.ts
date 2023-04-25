//disjoint set union class for faster graph manipulation
export class DisjointSetUnion {
    dsu : Array<number>;
    //size : Array<number>;

    constructor(n : number){
        this.dsu = Array.from(Array<number>(n).keys());
        //this.size = new Array<number>(n).fill(1);
    }

    find = (n : number) : number => {
        if(this.dsu[n] === n) return n;
        return this.dsu[n] = this.find(this.dsu[n]);
    }

    union = (n1 : number, n2 : number) => {
        n1 = this.find(n1);
        n2 = this.find(n2);
        //if(this.size[n1] > this.size[n2]) [this.dsu[n1], this.dsu[n2]] = [this.dsu[n2], this.dsu[n1]];
        if(n1 == n2) return;
        //this.size[n1] += this.size[n2];
        this.dsu[n2] = n1;
    }
    
    sameset = (n1 : number, n2 : number) : boolean => {
        return this.find(n1) === this.find(n2);
    }
}

//memoize function w/ one parameter of type P and return value of type R; big useful
export const memoize = <P,R>(fn: (param: P) => R) : ((param: P) => R) => {
    const cache = new Map<P, R>();
    return (p : P) => {return(!cache.has(p) ? cache.set(p, fn(p)).get(p)! : cache.get(p)!);};
}