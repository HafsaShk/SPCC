import java.util.*;
import java.io.*;

public class CopyProp {
    static boolean isVariable(String s) {
        char ch = s.toCharArray()[0];
        return (ch >= 'a' && ch <= 'z');
    }

    public static void main(String[] args) throws IOException {
        File input = new File("input.txt");
        FileWriter writer = new FileWriter("output.txt");
        Scanner sc = new Scanner(input);
        String line;
        String[] split;
        Map<String, String> map = new LinkedHashMap<>();
        String parent;
        while (sc.hasNextLine()) {
            line = sc.nextLine().trim();
            split = line.split(" ", -1);
            for (int i = 0; i < split.length; i++) {
                if (split[i].equals("=")) {
                    if (split.length == 4 && isVariable(split[i + 1])) {
                        map.put(split[i - 1], split[i + 1]);
                    } else {
                        for (; i < split.length; i++) {
                            if (isVariable(split[i])) {
                                parent = map.get(split[i]);
                                while (parent != null) {
                                    split[i] = parent;
                                    parent = map.get(parent);
                                }
                            }
                        }
                    }
                }
            }

            for (String word : split) {
                writer.flush();
                writer.append(word + " ");
            }
            writer.append("\n");
        }
        sc.close();
        writer.close();
    }
}
