const mults = new Set<number>();
let sum = 0;

for(let i = 0; i < 1000; i += 3){
    mults.add(i);
}

for(let j = 0; j < 1000; j += 5){
    if(mults.has(j)){
        continue;
    } else {
        mults.add(j);
    }
}

mults.forEach(value => sum += value);
console.log(sum);