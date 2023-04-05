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
            const currSet = cmap.get(sorted)!;
            currSet.add(curr);
            cmap.set(sorted, currSet);
        }else{
            const currSet = new Set<number>();
            currSet.add(curr);
            cmap.set(sorted, currSet); 
        }
    }
    const sets = new Set<Set<number>>();
    cmap.forEach((value : Set<number>) => {
        if(value.size == 5) sets.add(value);
    });
    const mins = new Set<number>();
    sets.forEach((s : Set<number>) => {
        mins.add(Math.min(...s));
    });
    console.log(Math.min(...mins));
}

genCubeMap(10000);