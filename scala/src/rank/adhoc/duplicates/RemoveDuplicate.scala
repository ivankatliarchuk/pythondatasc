package rank.adhoc.duplicates


import scala.collection.mutable.ArrayBuffer
import scala.io.Source.stdin

object RemoveDuplicate {

  def main(args: Array[String]): Unit = {
    var data = stdin.getLines.take(1).mkString.split("")
    //data.foreach(println)
    val cash = ArrayBuffer[String]()
    data.foreach(ch => {
      if (!cash.contains(ch)) {
        cash += ch
      }
    })
    displayResult(cash)

//    str.distinct
    /**
      * var str=Console.readLine()
        println(str.distinct)
    }
      */
  }

  private def f(arr: List[String]): List[String] = arr.map(f => f)
      .filter(_ != ())
    .toList

  private def displayResult(arr: ArrayBuffer[String]) = println(arr.mkString)

}
