package rank.intro

object LinesReader {


  def main(args: Array[String]): Unit = {
//    var lines = Iterator.continually(stdin.getLines()).takeWhile(line => line.nonEmpty).mkString
    var lines = io.Source.stdin.getLines.takeWhile(_.nonEmpty).map(_.toString).toList
    println(lines)
  }
}
