const sortNum = (n : string) => {
    return n.split('').sort().join('');
}

const cube = (n : number) => {
    return n ** 3;
}

const genCubes = (n : number) => {
    const res = new Array<string>();
    for(let i = 1; i <= n; i++){
        res.push(cube(i).toString());
    }
    return res;
}

const checkCubes = (carr : Array<string>) => {
    for(let i = 0; i < carr.length; i++){
        const curr = new Set<string>();
        for(let j = i; j < carr.length; j++){
            if(carr[i].length != carr[j].length){
                break;
            }
            if(sortNum(carr[i]) == sortNum(carr[j])){
                curr.add(carr[i]);
                curr.add(carr[j]);
            }
            if(curr.size == 5){
                return curr;
            }
        }
    }
}

console.log(checkCubes(genCubes(10000)));