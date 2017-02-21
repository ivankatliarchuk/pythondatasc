package rank.intro

object updatestructure extends App {
  // math.abs
  def f(arr: List[Int]): List[Int] = arr.map(_.abs)


  println(f(List(2, -4, 3, -1, 23, 4, 54)))

}
