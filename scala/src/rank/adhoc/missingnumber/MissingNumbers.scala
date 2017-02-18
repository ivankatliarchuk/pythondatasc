package rank.adhoc.missingnumber

import scala.io.StdIn

object MissingNumbers {

  def main(args: Array[String]): Unit = {
    var first = StdIn.readInt
    var dataF = readData()
    var second = StdIn.readInt
    var dataS = readData()

    displayResult(sortedDiff(dataF, dataS))
  }

  private def readData():List[Int] = StdIn.readLine.split(" ").filter(_.nonEmpty).map(_.trim).map(_.toInt).toList
  private def sortedDiff(first: List[Int], second: List[Int]):List[Int] = {
    if (first.length >= second.length) {
      first.diff(second).distinct.sorted
    } else {
      second.diff(first).distinct.sorted
    }
  }
  private def displayResult(arr: List[Int]) = println(arr.mkString(" ").trim)

}

//  l2.diff(l1).sortWith(_ < _).distinct.foreach(k => print(k + " "))
// 3670 3674 3677 3684 3685 3695 3714 3720
