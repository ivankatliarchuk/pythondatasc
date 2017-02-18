package rank.recursion.pascaltriangle


import scala.io.StdIn

object PascTriangle {

  def main(args: Array[String]): Unit = {
    var N  = StdIn.readInt()
    for ( n <- 0 until N) {
      for (r <- 0 to n) {
        var value =
        print(calculate(n, r) + " ")
      }
      println()
    }

  }

  // formula N!/(R!*(N-R)!)
  def calculate(n: Int, r:Int): Int = {
    factorial(n) / (factorial(r) * factorial(n-r))
  }

  def factorial(n: Int): Int = {
    if (n == 0)
      return 1
    else
      return n * factorial(n-1)
  }

}
