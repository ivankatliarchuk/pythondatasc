package rank.intro

object filterbyindex extends App {

  /*
  list.zipWithIndex.collect {
  case (x,i) if i % 3 == 0 => x
}

2
5
3
4
6
7
9
8
   */

  def f(arr:List[Int]):List[Int] = arr.zipWithIndex.collect {
    case (x,i) if i % 2 != 0 => x
  }
  println(f(List(2, 5, 3, 4, 6, 7, 9, 8)))
}
