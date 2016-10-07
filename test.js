function Coins(num) {
    var q = Math.trunc(num / 25);
    var r = num % 25;
    var d = Math.trunc(r / 10);
    r = r % 10;
    var n = Math.trunc(r / 5);
    p = r % 5;
    console.log(q, d, n, p)
}

Coins(92)
