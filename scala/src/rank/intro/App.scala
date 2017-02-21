package rank.intro


object App {
  def main(args: Array[String]) {
    var d = io.Source.stdin.getLines().takeWhile(_.nonEmpty).map(_.toInt).sum
    println(d)
  }
}
