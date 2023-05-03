import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class ConstantProp {

    static boolean isVariable(String s) {
        char ch = s.toCharArray()[0];
        return (ch >= 'a' && ch <= 'z');
    }

    public static void main(String[] args) throws IOException {
        
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        String[] split;
        HashSet<String> dataTypes = new HashSet<>(Arrays.asList("int", "float", "double", "long", "boolean"));
        HashMap<String, String> variables = new HashMap<>();

        File output = new File("output.txt");
        if (output.exists()) {
            output.delete();
        }
        output.createNewFile();

        FileWriter writer = new FileWriter(output);

        String line;
        while (sc.hasNextLine()) {
            line = sc.nextLine();
            split = line.split(" ", -1);
            for (int i = 0; i < split.length; i++) {
                if (variables.get(split[i]) != null) {
                    split[i] = variables.get(split[i]);
                }
                else if (dataTypes.contains(split[i])) {
                    for (int j = i + 1; j < split.length; j++) {
                        if (split[j].equals(",") || split[j].equals(""))
                            continue;
                        if (isVariable(split[j])) {
                            variables.put(split[j], null);
                            if (split[j + 1].equals("="))
                                variables.put(split[j], split[j + 2]);
                                i += 2;
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
        writer.close();
        sc.close();
    }
}
