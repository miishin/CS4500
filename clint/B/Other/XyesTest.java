
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
import java.time.Duration;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class XyesTest {

    //stdout capture from
    //https://www.baeldung.com/java-testing-system-out-println

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

    String[] blank = {};
    String[] onlyLimit = {"-limit"};
    String[] limitHelloWorld = {"-limit", "hello", "world"};
    String[] singleLimit = {"-limit", "a"};
    String[] limitLimitInput = {"-limit", "-limit"};
    String[] multipleLimit = {"-limit", "1", "2", "x"};
    String[] infinite = {"go", "forever"};


    // Test that ./xyes 1 2 x
    // Will return the right concatenated string
    @Test
    public void testGetLine() {
        XYes x = new XYes(multipleLimit);
        assertEquals("1 2 x", x.getLine());
    }

    // Test that ./xyes -limit
    // Will return the concatenated string "hello world"
    @Test
    public void testGetLine2() {
        XYes x = new XYes(onlyLimit);
        assertEquals("hello world", x.getLine());
    }

    // Test that ./xyes
    // With no args returns "hello world"
    @Test
    public void testGetLine3() {
        XYes x = new XYes(blank);
        assertEquals("hello world", x.getLine());
    }

    // Test that with ./xyes -limit -limit
    // the -limit is recognized
    @Test
    public void testLimit() {
        XYes x = new XYes(limitLimitInput);
        assertTrue(x.limit());
    }

    // Test that when -limit is not specified
    // that it isn't flagged
    @Test
    public void testLimit2() {
        XYes x = new XYes(infinite);
        assertFalse(x.limit());
    }

    // Test for input ./xyes -limit
    // Only -limit as command argument
    @Test
    public void testLimitedInput() {
        XYes x = new XYes(onlyLimit);
        x.run();
        assertEquals("hello world\nhello world\nhello world\nhello world\n"
        + "hello world\nhello world\nhello world\nhello world\nhello world\nhello world\n"
        + "hello world\nhello world\nhello world\nhello world\nhello world\nhello world\n"
        + "hello world\nhello world\nhello world\nhello world", output.toString().trim());
    }

    // Test for input ./xyes -limit hello world
    //
    @Test
    public void testLimitHelloWorldInput() {
        XYes x = new XYes(limitHelloWorld);
        x.run();
        assertEquals("hello world\nhello world\nhello world\nhello world\n"
        + "hello world\nhello world\nhello world\nhello world\nhello world\nhello world\n"
        + "hello world\nhello world\nhello world\nhello world\nhello world\nhello world\n"
        + "hello world\nhello world\nhello world\nhello world", output.toString().trim());
    }


    // Test ./xyes -limit -limit to see
    // if flag is recognized if appears elsewhere
    @Test
    public void testLimitedInputLimit() {
        XYes x = new XYes(limitLimitInput);
        x.run();
        assertEquals("-limit\n-limit\n-limit\n-limit\n-limit\n-limit\n-limit\n-limit" +
                "\n-limit\n-limit\n-limit\n-limit\n-limit\n-limit\n-limit\n-limit\n-limit" +
                "\n-limit\n-limit\n-limit", output.toString().trim());
    }

    // Test for ./xyes -limit a
    // -limit and only one other string
    @Test
    public void testSingleLimitedInput() {
        XYes x = new XYes(singleLimit);
        x.run();
        assertEquals("a\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na", output.toString().trim());
    }

    // Test for ./xyes -limit 1 2 x

    @Test
    public void testMultipleLimitInput() {
        XYes x = new XYes(multipleLimit);
        x.run();
        assertEquals("1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n"
        + "1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x\n1 2 x",
                output.toString().trim());
    }

    // Test for ./xyes go forever
    // but timeout after 0.1 seconds

    // If we test for 0.1 seconds, then 1, then 2 seconds,
    // We can see it outputting more and more
    // But this also doesn't show that the output is infinite.
    // But it does show that it's outputting more than 20,
    // And if our code only runs 20 or infinite (while (true))
    // Then it should be infinite
    @Test
    public void testInfiniteShort() {
        XYes x = new XYes(infinite);
        assertTimeoutPreemptively(Duration.ofMillis(100), () -> {
            x.run();
        });
    }

    // Test for ./xyes go forever
    // but timeout after 1 second
    @Test
    public void testInfiniteMedium() {
        XYes x = new XYes(infinite);
        assertTimeoutPreemptively(Duration.ofSeconds(1), () -> {
            x.run();
        });
    }

    // Test for ./xyes go forever
    // but timeout after 2 seconds
    @Test
    public void testInfiniteLong() {
        XYes x = new XYes(infinite);
        assertTimeoutPreemptively(Duration.ofSeconds(2), () -> {
            x.run();
        });
    }
}
