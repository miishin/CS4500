/**
 * Represents xyes, with method to echo command line arguments
 */
public class xyes {

  public String[] args;

  xyes(String[] args) {
    this.args = args;
  }
  /**
   * Echos command line arguments infinitely, with 2 exceptions, (1) If "-limit" is specified
   * the argument is printed 20 times, (2) and if there are no arguments,
   * it prints "hello world"
   */
  public void echo() {
    int lim = 0;
    int start = 0;
    boolean islim = false;

    if (args.length == 0 || (args.length == 1 && args[0].equals("-limit"))) {
      if (args.length == 1) {
        islim = true;
      }
      while (lim < 20) {
        System.out.println("hello world");
        if (islim) {
          lim++;
        }
      }
      return;
    } else if (args[0].equals("-limit")) {
      start = 1;
      islim = true;
    }
    String output = "";
    for (int i = start; i < args.length; i++) {
      output = output.concat(args[i] + " ");
    }

    while (lim < 20) {
      System.out.println(output);
      if (islim) {
        lim++;
      }
    }
    return;
  }
}



