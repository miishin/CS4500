import org.junit.jupiter.api.*;

import static org.junit.Assert.*;
import java.io.PrintStream;
import java.io.ByteArrayOutputStream;

/**
 * Test class
 */
public class xyesTest {

  /**
   * Guidance from https://www.baeldung.com/java-testing-system-out-println
   */

  private final PrintStream stdOut = System.out;
  private final ByteArrayOutputStream output = new ByteArrayOutputStream();

  @BeforeEach
  public void setUp() {
    System.setOut(new PrintStream(output));
  }

  @AfterEach
  public void reset() {
    System.setOut(stdOut);
  }

  // Testing

  // Note: There are 2 infinite cases, one where there are no command line arguments and it will print
  // "hello world" infinitely, and the other with an input such as "hi how are you". We have tested
  // these with our executable, and based on the instructor endorsed answer on
  // https://piazza.com/class/kevisd7ggfb502?cid=39, this is the "halting problem" and a test cannot
  // be written for this

  @Test
  public void TestLimitWithArgs(){
    String[] args = new String[]{"-limit", "hi", "hello", "bye"};
    xyes xyes = new xyes(args);
    xyes.echo();
    assertEquals("hi hello bye \nhi hello bye \nhi hello bye \nhi hello bye \nhi hello bye \n" +
                    "hi hello bye \nhi hello bye \nhi hello bye \nhi hello bye \nhi hello bye \nhi hello bye \n" +
                    "hi hello bye \nhi hello bye \nhi hello bye \nhi hello bye \nhi hello bye \n" +
                    "hi hello bye \nhi hello bye \nhi hello bye \nhi hello bye \n", output.toString());
  }

  @Test
  public void TestJustLimitEmpty(){
    String[] args = new String[]{"-limit"};
    xyes xyes = new xyes(args);
    xyes.echo();
    assertEquals("hello world\nhello world\nhello world\nhello world\nhello world\n" +
            "hello world\nhello world\nhello world\nhello world\nhello world\n" +
            "hello world\nhello world\nhello world\nhello world\nhello world\n" +
            "hello world\nhello world\nhello world\nhello world\nhello world\n",
            output.toString());
  }

}