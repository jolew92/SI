import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;

import static java.util.Collections.*;

public class Main {

    protected static String graphFileName = "le450 25c.txt";
    protected static double crossProbability = 0.75;
    protected static double mutationProbability = 0.001;
    protected static double parentMutationProbability = 0.05;
    protected static int colors = 25;
    protected static int populationSize = 100;
    protected static int generations = 1000;

    public static void main(String[] args) throws FileNotFoundException {
        Graph g = new Graph();
        g.loadFromFile(graphFileName);
        PrintWriter save = new PrintWriter("output9.txt");
        GeneticAlgorithm ga = new GeneticAlgorithm(g, colors);
        List<Integer[]> population = ga.init(populationSize);
        for(int i=0; i<generations && ga.getBest()!=0; i++) {
            List<Integer[]> new_population = new ArrayList<Integer[]>();
            List<Integer> results = ga.fitnessAll(population);
            int min = min(results);
            double avg = average(results);
            int max = max(results);
            System.out.print("Best: " + min);
            System.out.print(" Avg: " +avg);
            System.out.println(" Worst: " + max);
            save.println(min + ";" + avg + ";" + max);
            while(populationSize>new_population.size()) {
                //Collections.shuffle(population);
                List<Integer[]> new_subjects = ga.crossover(ga.selection(population), ga.selection(population), crossProbability);
                if(!ga.getCrossed()) {
                    new_subjects = ga.mutation(new_subjects, parentMutationProbability);
                    new_population.add(new_subjects.get(0));
                    new_population.add(new_subjects.get(1));
                }
                else {
                    new_subjects = ga.mutation(new_subjects, mutationProbability);
                    new_population.add(new_subjects.get(0));
                    new_population.add(new_subjects.get(1));
                }
            }
            population = new_population;
        }
        save.close();
    }

    private static double average(List<Integer> ls) {
        double avg = 0.0;
        for (int i = 0; i < ls.size(); i++)  {
            avg += ls.get(i) ;
        }
        return avg/ls.size();
    }
}