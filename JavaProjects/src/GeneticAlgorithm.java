import java.util.ArrayList;
import java.util.List;

public class GeneticAlgorithm {

    private Graph graph;
    private int colors;
    private boolean crossed;
    private int best = -1;

    public GeneticAlgorithm(Graph graph, int colors) {
        this.graph = graph;
        this.colors = colors;
    }

    public List<Integer[]> init(int size) {
        List<Integer[]> temp = new ArrayList<Integer[]>();
        for (int i = 0; i < size; i++) {
            Integer[] t = new Integer[graph.graph.size()];
            for (int j = 0; j < t.length; j++) {
                t[j] = (int) Math.floor(Math.random() * colors);
            }
            temp.add(t);
        }
        return temp;
    }

    public int fitnessSubject(Integer[] subject) {
        int conflicts = 0;
        for (int i = 0; i < subject.length; ++i) {
            int currentColor = subject[i];
            List<Integer> current = graph.graph.get(i);
            for (int j = 0; j < current.size(); j++) {
                if (subject[current.get(j)] == currentColor) {
                    conflicts++;
                }
            }
        }
        return conflicts;
    }

    public List<Integer> fitnessAll(List<Integer[]> population) {
        List<Integer>  temp = new ArrayList<Integer>();
        for (Integer[] subject : population) {
            int current = fitnessSubject(subject);
                temp.add(current);
            if(current<best || best==-1)
                best = current;
        }
        return temp;
    }

    public Integer[] selection(List<Integer[]> population) {
        int best=-1;
        int bestIndex = 0;
        for(int i=0; i<5; i++) {
            int subjectIndex = (int) Math.floor(Math.random() * population.size());
            int current = fitnessSubject(population.get(subjectIndex));
            if(current<best || best==-1) {
                best = current;
                bestIndex = subjectIndex;
            }
        }
        return population.get(bestIndex);
    }

    public List<Integer[]> crossover(Integer[] parent1, Integer[] parent2, double crossoverProbability) {
        List<Integer[]> children = new ArrayList<Integer[]>();
        Integer[] child1 = new Integer[parent1.length];
        Integer[] child2 = new Integer[parent1.length];
        if(Math.random() < crossoverProbability) {
            int split = (int) Math.floor(Math.random() * parent1.length);
            for (int i = 0; i < split; i++) {
                child1[i] = parent1[i];
                child2[i] = parent2[i];
            }
            for (int i = split; i < parent1.length; i++) {
                child1[i] = parent2[i];
                child2[i] = parent1[i];
            }
            children.add(child1);
            children.add(child2);
            crossed = true;
        }
        else {
            children.add(parent1);
            children.add(parent2);
            crossed = false;
        }
        return children;
    }

    public List<Integer[]> mutation(List<Integer[]> population, double mutationProbability) {
        for (Integer[] subject : population) {
            for (int i = 0; i < subject.length; i++) {
                if (Math.random() < mutationProbability) {
                    subject[i] = (int) Math.floor(Math.random() * colors);
                }
            }
        }
        return population;
    }

    public boolean getCrossed() {
        return crossed;
    }

    public int getBest() {
        return best;
    }
}