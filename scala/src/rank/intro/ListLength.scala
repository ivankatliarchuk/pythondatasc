package rank.intro

import java.util.NoSuchElementException

import scala.io.Source.stdin

object ListLength {

  def main(args: Array[String]) {
    val data = stdin.getLines().takeWhile(_.nonEmpty).toList
    var x:Int = 0
    x = x+1
    print(counter(data, 0))
  }



  def counter(arr:List[String], accumulator: Int):Int = {
    try {
      var headA = arr.head
      if (headA == null) {
        accumulator
      } else {
        counter(arr.tail, accumulator + 1)
      }
    } catch  {
      case _: Throwable => accumulator
    }
  }

  private def displayResult(arr:List[Int]) = println(arr)
 // displayResult(stdin.getLines.takeWhile(_.nonEmpty).toList.map(_.trim).map(_.toInt))
}
