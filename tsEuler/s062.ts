const sortNum = (n : string) => {
    return n.split('').sort().join('');
}

const cube = (n : number) => {
    return n ** 3;
}

const genCubeMap = (n : number) => {
    const cmap = new Map<string, Set<number>>();
    for(let i = 1; i <= n; i++){
        const curr = cube(i);
        const sorted = sortNum(curr.toString());
        if(cmap.has(sorted)){
            cmap.set(sorted, cmap.get(sorted)!.add(curr));
        }else{
            cmap.set(sorted, new Set<number>().add(curr)); 
        }
    }
    cmap.forEach((value : Set<number>) => {
        if(value.size == 5) console.log(Math.min(...value));
    });
}

genCubeMap(10000);