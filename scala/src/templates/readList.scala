package templates

import scala.io.Source.stdin

object readList {

  def f(num:Int,arr:List[Int]):List[Int] = {
    arr.flatMap(e => List.fill(num)(e))
  }
  //def displayResult(arr:List[Int]) = println(f(arr(0).toInt,arr.drop(1)).map(_.toString).mkString("\n"))
 // displayResult(stdin.getLines.takeWhile(_.nonEmpty).toList.map(_.trim).map(_.toInt))

}



object readArray {
  def main(args: Array[String]): Unit = {
    val sc = new java.util.Scanner (System.in)
    var n = sc.nextInt()
    var k = sc.nextInt()
    var a = new Array[Int](n)
    for(a_i <- 0 until  n-1) {
      a(a_i) = sc.nextInt()
    }
  }
}
