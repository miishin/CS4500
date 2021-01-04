import java.util.*;

public class XYes {
    ArrayList<String> args;
    boolean limit;
    boolean removed;

    XYes(String[] args) {
        this.args = new ArrayList<String>();
        this.args.addAll(Arrays.asList(args));
        limit = false;
        removed = false;
    }

    public void run() {
        String result;

        this.limit = this.limit();

        result = this.getLine();


        if (limit) {
            for (int i = 0; i < 20; i++) {
                System.out.println(result);
            }
        } else {
            while (true) {
                System.out.println(result);
            }
        }
    }

    public boolean limit() {
        if (this.args.size() == 0) {
            return false;
        } else {
            return this.args.get(0) == "-limit";
        }
    }

    public String getLine() {
        if (this.args.size() == 0) {
            return "hello world";
        } else {
            if (this.limit) {
                if (!(this.removed)) {
                    this.args.remove(0);
                    this.removed = true;
                }
            }

            if (this.args.size() == 0) {
                return "hello world";
            } else {
                return String.join(" ", this.args);
            }
        }
    }
}