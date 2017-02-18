package templates

object readList {

  def f(num:Int,arr:List[Int]):List[Int] = {
    arr.flatMap(e => List.fill(num)(e))
  }

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
