import java.util.Scanner;
import java.util.LinkedList;

public class PrimeTest {
  public static void main(String[] args) {
    int a, ans;
    Scanner Obj = new Scanner(System.in);
    System.out.println("Type a number: ");
    a = Obj.nextInt();
    boolean prime = true;
    for (i = 0; i < a; i++;) {
      if (a % i == 0) {
        prime = false;
      }
    }
    if (prime == true) {
      System.out.println("Your number is prime!");
    } else {
      System.out.println("Your number is NOT prime!");
    }
  }
}
