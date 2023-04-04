let arr : number[] = [1, 2];
let x = 1, y = 2, ctrl = 0, sum = 0;

while(ctrl < 4000000){
    ctrl = x + y;
    x = y;
    y = ctrl;
    arr.push(ctrl);
}

for(const ndx in arr) (arr[ndx] % 2 == 0) ? sum += arr[ndx] : sum += 0;
console.log(sum);