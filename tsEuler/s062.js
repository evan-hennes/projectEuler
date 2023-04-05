var sortNum = function (n) {
    return n.split('').sort().join('');
};
var cube = function (n) {
    return Math.pow(n, 3);
};
var genCubes = function (n) {
    var res = new Array();
    for (var i = 1; i <= n; i++) {
        res.push(cube(i).toString());
    }
    return res;
};
var checkCubes = function (carr) {
    for (var i = 0; i < carr.length; i++) {
        var curr = new Set();
        for (var j = i; j < carr.length; j++) {
            if (carr[i].length != carr[j].length) {
                break;
            }
            if (sortNum(carr[i]) == sortNum(carr[j])) {
                curr.add(carr[i]);
                curr.add(carr[j]);
            }
            if (curr.size == 5) {
                return curr;
            }
        }
    }
};
console.log(checkCubes(genCubes(10000)));
