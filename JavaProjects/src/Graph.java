import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Graph {

    public List<List<Integer>> graph;

    public Graph() {
        graph = new ArrayList();
    }

    public void loadFromFile(String fileName) throws FileNotFoundException {
        Scanner in = new Scanner(new File(fileName));
        String t = "";
        while (!t.equals("p")) {
            in.nextLine();
            t = in.next();
        }
        in.next();

        int edges = in.nextInt();
        int size = in.nextInt();
        graph = new ArrayList(edges);
        for (int i = 0; i < edges; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < size; ++i) {
            in.next();
            int v = in.nextInt() - 1;
            int neigh = in.nextInt() - 1;
            if (!graph.get(v).contains(neigh))
                graph.get(v).add(neigh);
        }
        in.close();
    }
}
