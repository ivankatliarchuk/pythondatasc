package rank.recursion

import scala.annotation.tailrec

/**
  * In this challenge, we learn how to compute GCD using the Euclidean algorithm
  * GCD greatest common denominator.
  *
  * Sample return values:
  * GCD(1,5) = 1
  * GCD(10,100) = 10
  * GCD(22,131) = 1
  *1701 3768 = 3
  */
object GcdCopute {

  def gcd(x: Int, y: Int): Int = {
    // You only need to fill up this function
    // To return the value of the GCD of x and y
    recursive(x, y)

  }
  // 1701 3768
  @tailrec
  def recursive(f: Int, s: Int): Int = {
    // exit the recursive call
    if (s == 0) {
      f
    }
    else {
      recursive(s, f % s)
    }
  }


  /** This part handles the input/output. Do not change or modify it **/
  def acceptInputAndComputeGCD(pair: List[Int]) = {
    println(gcd(pair.head, pair.reverse.head))
  }

  def main(args: Array[String]) {
    /** The part relates to the input/output. Do not change or modify it **/
    acceptInputAndComputeGCD(readLine().trim().split(" ").map(_.toInt).toList)

  }

}
