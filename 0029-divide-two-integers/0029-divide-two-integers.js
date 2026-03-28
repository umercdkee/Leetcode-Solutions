/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    if (dividend === 0)
        return 0;
    let negative = false;
    if (dividend < 0){
        dividend = - dividend;
        negative = true;
    }
    if (divisor < 0){
        divisor = - divisor;
        if (negative)
            negative = false;
        else
            negative = true;
    }
    let quotient = 0;
    while (dividend >= divisor){
        let subtract = divisor;
        let count = 1;
        while (subtract + subtract <= dividend){
            count += count;
            subtract += subtract
        }
        dividend -= subtract;
        quotient+= count; 
    }
    if (negative)
        quotient = -quotient;
    if (quotient > (2**31 - 1))
        return (2**31 -1)
    return quotient;
};