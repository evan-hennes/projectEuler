import { memoize } from "./useful.ts";

const startingNums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18];
const zeroes = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17];

const findNums = memoize((nums : Array<number>) : number => {
    let sum = 0;
    if(nums[10] === 0){
        return 1;
    }
    for(let i = 0; i <= 9; i++){
        const curr = [...nums];
        if(curr[i] === 3){
            continue;
        }
        curr[i] = curr[i] + 1;
        curr[10] = curr[10] - 1;
        sum += findNums(curr);
    }
    return sum;
});

console.log(findNums(startingNums) - findNums(zeroes));