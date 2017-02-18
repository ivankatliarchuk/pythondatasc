package rank.intro

object ArrayNCreate extends App {

  def f(num:Int) : List[Int] = List.fill(num){2}
  def r(num:Int) : List[Int] = List.range(0, num)

  print(r(readInt()))

}
