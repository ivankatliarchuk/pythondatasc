package rank.recursion

import scala.annotation.tailrec

object Fibonacci {


  def fibonacci(x:Int):Int = {

    // Fill Up this function body
    // You can add another function as well, if required
    if (x > 2) {
      fibonacci(x - 1) + fibonacci(x - 2)
    } else {
      x - 1
    }
  }

  def main(args: Array[String]) {
    /** This will handle the input and output**/
    println(fibonacciCase(readInt()))

  }

  def fibonacciCase(x:Int):Int = x match {
    case 0 | 1 => 0
    case 2 => 1
    case _ => fibonacciCase(x-1) + fibonacciCase(x-2)
  }
}
