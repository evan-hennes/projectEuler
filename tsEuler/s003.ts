let n = 600851475143;

const sieve = (lim : number) => {
    let nList = new Array<number>();
    for(let i = 2; i < lim; i++){ 
        try{
            nList.push(i);
        } catch {
            console.log(nList.length);
        }
    }
    let p = 2;
    while(p ** 2 < lim + 1){
        for(let i = p ** 2; i < lim; i += p){
            if(i % p == 0 && nList.includes(i)){
                nList.splice(nList.indexOf(i), 1);
            }
        }
        p++;
    }
    return nList;
};

const segsieve = (num : number) => {
    let limit = Math.floor(Math.sqrt(num)) + 1;
    let primes : Array<number> = sieve(limit);
    let res : Array<number> = primes;
    let low = limit, high = 2 * limit;
    while(low < num){
        if(high >= num){
            high = num;
        }
        let mark = new Array<boolean>(limit + 1).fill(true);
        for(let i = 0; i < primes.length; i++){
            let llim = Math.floor(low/primes[i]) * primes[i];
            if(llim < low){
                llim += primes[i];
            }
            for(let j = llim; j < high; j += primes[i]){
                mark[j - low] = false;
            }
        }
        for(let i = low; i < high; i++){
            if (mark[i - low]){
                res.push(i);
            } 
        }
        low = low + limit, high = high + limit;
    }
    return res;
};

const resultArr : Array<number> = segsieve(n);
const result = resultArr[resultArr.length - 1];
console.log(result)
