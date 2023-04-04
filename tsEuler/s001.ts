let mults : number[] = [];
let sum : number = 0;

for(let i = 0; i < 1000; i += 3){
    mults.push(i);
}

for(let j = 0; j < 1000; j += 5){
    if(mults.includes(j)){
        continue;
    } else {
        mults.push(j);
    }
}

for(let n in mults){
    sum += mults[n];
}

console.log(sum);