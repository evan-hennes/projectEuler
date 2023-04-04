var n = 600851475143;
var sieve = function (num) {
    var nList = new Array();
    for (var i = 2; i < num; i++) {
        nList.push(i);
    }
    var p = 2;
    while (Math.pow(p, 2) < num + 1) {
        for (var i = Math.pow(p, 2); i < num; i += p) {
            if (i % p == 0 && nList.includes(i)) {
                nList.splice(nList.indexOf(i), 1);
            }
        }
        p++;
    }
    return nList;
};
console.log(sieve(n));
