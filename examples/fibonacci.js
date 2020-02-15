/**
 * ### Fibonacci numbers
 * @param {number} n Fibonacci number to calculate
 * @returns {number} nth Fibonacci number
 * @tutorial
 * [WikiBooks](https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Fibonacci_Number_Program)
 */
const fib = n => {
  var i = 1,
    j = 0,
    k,
    t
  for (k = 1; k <= Math.abs(n); k++) {
    t = i + j
    i = j
    j = t
  }
  if (n < 0 && n % 2 === 0) j = -j
  return j
}

console.log(fib(8))
