package templates

object display {

  def f():List[Int] = {List();}
  def displayResult(arr:List[Int]) = println(f().map(_.toString).mkString("\n"))
  displayResult(io.Source.stdin.getLines.toList.map(_.trim).map(_.toInt))



}
