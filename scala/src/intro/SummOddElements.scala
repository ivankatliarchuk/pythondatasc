package intro

import scala.io.Source.stdin

object SummOddElements extends App {

  def f(arr:List[Int]):Int = arr.filter(_ % 2 != 0).sum

  private def displayResult(arr: List[Int]) = println(f(arr).toString)

  displayResult(stdin.getLines.takeWhile(_.nonEmpty).toList.map(_.trim).map(_.toInt))

}
