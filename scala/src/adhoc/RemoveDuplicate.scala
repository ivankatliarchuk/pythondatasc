package adhoc

import scala.io.Source.stdin

object RemoveDuplicate {

  def main(args: Array[String]): Unit = {
    displayResult(stdin.getLines.take(1).toList)
  }

  def f(arr: List[String]): Set[String] = arr.toSet
  def displayResult(arr: List[String]) = println(f(arr).mkString("\n"))


}
