let n = 600851475143;

const sieve = (num : number) => {
    let nList = new Set<number>();
    for(let i = 2; i < num; i++){ 
        try{
            nList.add(i);
        } catch {
            console.log(nList.size);
        }
    }
    let p = 2;
    while(p ** 2 < num + 1){
        for(let i = p ** 2; i < num; i += p){
            if(i % p == 0 && nList.has(i)){
                nList.delete(i);
            }
        }
        p++;
    }
    return nList;
};

console.log(sieve(n));