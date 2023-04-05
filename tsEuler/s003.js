var n = 600851475143;
var sieve = function (lim) {
    var nList = new Array();
    for (var i = 2; i < lim; i++) {
        try {
            nList.push(i);
        }
        catch (_a) {
            console.log(nList.length);
        }
    }
    var p = 2;
    while (Math.pow(p, 2) < lim + 1) {
        for (var i = Math.pow(p, 2); i < lim; i += p) {
            if (i % p == 0 && nList.includes(i)) {
                nList.splice(nList.indexOf(i), 1);
            }
        }
        p++;
    }
    return nList;
};
var segsieve = function (num) {
    var limit = Math.floor(Math.sqrt(num)) + 1;
    var primes = sieve(limit);
    var res = primes;
    var low = limit, high = 2 * limit;
    while (low < num) {
        if (high >= num) {
            high = num;
        }
        var mark = new Array(limit + 1).fill(true);
        for (var i = 0; i < primes.length; i++) {
            var llim = Math.floor(low / primes[i]) * primes[i];
            if (llim < low) {
                llim += primes[i];
            }
            for (var j = llim; j < high; j += primes[i]) {
                mark[j - low] = false;
            }
        }
        for (var i = low; i < high; i++) {
            if (mark[i - low]) {
                res.push(i);
            }
        }
        low = low + limit, high = high + limit;
    }
    return res;
};
var resultArr = segsieve(n);
var result = resultArr[resultArr.length - 1];
console.log(result);
