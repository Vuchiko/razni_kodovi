
    var x1 = 10;
    var x2 = 12;
    var x3 = 9.5;
    var x4 = 15;
     
    function compute(x1, x2, x3, x4) {
        var m = (x1 + x2 + x3 + x4)/5.0;
        console.log("m variable is: " + m)
        var n = m*12*m/2.;
        console.log("n variable is: " + n)
        var o = n-0.94;
        console.log("o variable is: " + o)
        return o/518;
    }
     
    // Call the above function with x1, x2, x3, x4
    // What is the result, add here a mean to display
    // the result in the console
    var result = compute(x1, x2, x3, x4);
    console.log(result);
