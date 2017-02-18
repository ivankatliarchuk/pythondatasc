package rank.intro

import scala.io.Source.stdin

object FilterArray extends App {

  def f(delim: Int, arr: List[Int]): List[Int] = arr.filter(_ < delim)

  private def displayResult(arr: List[Int]) = println(f(3, arr).map(_.toString).mkString("\n"))

  displayResult(stdin.getLines.takeWhile(_.nonEmpty).toList.map(_.trim).map(_.toInt))

}
