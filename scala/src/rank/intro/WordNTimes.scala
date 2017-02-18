package rank.intro
import scala.io.StdIn

object WordNTimes extends App {
  private def f(n: Int) = {
    for (i <- 1 to n )
      println("Hello World")

  }

  var n = StdIn.readInt
  f(n)
}



