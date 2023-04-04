var mults = new Set();
var sum = 0;
for (var i = 0; i < 1000; i += 3) {
    mults.add(i);
}
for (var j = 0; j < 1000; j += 5) {
    if (mults.has(j)) {
        continue;
    }
    else {
        mults.add(j);
    }
}
mults.forEach(function (value) { return sum += value; });
console.log(sum);
