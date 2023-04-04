var mults = [];
var sum = 0;
for (var i = 0; i < 1000; i += 3) {
    mults.push(i);
}
for (var j = 0; j < 1000; j += 5) {
    if (mults.includes(j)) {
        continue;
    }
    else {
        mults.push(j);
    }
}
for (var n in mults) {
    sum += mults[n];
}
console.log(sum);
