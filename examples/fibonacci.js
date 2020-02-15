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

/**
 * ### Fibonacci sequence
 * @param {number} n Calculate Fibonacci sequence up to this number
 * @returns {array} Fibonacci sequence
 * @tutorial
 * [30 Seconds of Interviews](https://30secondsofinterviews.org/)
 * > Initialize an empty array of length n _(note: I use `n + 1`)_.
 * > Use `Array.prototype.reduce()` to add values into the array, using
 * > the sum of the last two values, except for the first two.
 */
const fib_seq = n =>
  [...Array(n + 1)].reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  )
console.log(fib(8))
console.log(fib_seq(8))
