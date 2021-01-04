package com.company;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {

        Scanner scanner = new Scanner(System.in);
        JSONArray list = new JSONArray();
        JSONArray rev = new JSONArray();

        ArrayList inputs = new ArrayList();
        String curr = "";
        int openbrac = 0;
        int closebrac = 0;
        while (scanner.hasNextLine()) {
            curr = curr.concat(scanner.nextLine());
        }
        char[] chars = curr.toCharArray();
        curr = "";
        for (Character c : chars) {
            if (c == '{') {
                openbrac++;
            } else if (c == '}') {
                closebrac++;
            }
            if ((openbrac + closebrac) == 0) {
                continue;
            }
            curr = curr.concat(c.toString());
            if (openbrac == closebrac) {
                //System.out.println("CURR: " +curr);
                inputs.add(curr);
                curr = "";
                openbrac = 0;
                closebrac = 0;
            }
        }
        int count = inputs.size();
        String[] reverse = new String[count];
        for (Object value : inputs ) {
            list.add((String)value);
            reverse[count-1] = (String)value;
            count--;
        }
        for (String value : reverse) {
            rev.add(value);
        }
        JSONObject out1 = new JSONObject();
        JSONObject out2 = new JSONObject();

        out1.put("count",list.size());
        out1.put("seq",list);

        out2.put("count",list.size());
        out2.put("seq",rev);
        System.out.println(out1);
        System.out.println(out2);
    }
}
