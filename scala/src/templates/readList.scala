package templates

object readList {

  def f(num:Int,arr:List[Int]):List[Int] = {
    arr.flatMap(e => List.fill(num)(e))
  }

}
