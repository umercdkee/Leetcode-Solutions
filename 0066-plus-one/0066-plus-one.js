/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    index = digits.length - 1;
    digits[index] = digits[index] + 1;
    while (digits[index] == 10 & index >= 0){
        digits[index] = 0;
        index-=1;
        digits[index] = digits[index] +1;
    }
    if (index == -1)
        digits.unshift(1);
    return digits;
};