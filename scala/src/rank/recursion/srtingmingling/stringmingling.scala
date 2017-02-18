package rank.recursion.srtingmingling

import scala.io.StdIn

object stringmingling {

  def main(args: Array[String]): Unit = {
    var R = StdIn.readLine().split("").toList
    var Q = StdIn.readLine().split("").toList

    R.zip(Q).foreach(f => print(f._1 + f._2))


  }

  def mingled(r:List[String], q:List[String]):String = ""

  println(readLine.zip(readLine).map(e => e._1 + "" + e._2).mkString(""))


}
