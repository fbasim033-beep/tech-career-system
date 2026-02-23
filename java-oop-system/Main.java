// Tech Career OOP System
// Author: Fatima

class Job {
    String title;
    double salary;

    Job(String title, double salary) {
        this.title = title;
        this.salary = salary;
    }

    void displayJob() {
        System.out.println("Job Title: " + title);
        System.out.println("Salary: " + salary);
        System.out.println("---------------------");
    }
}

public class Main {
    public static void main(String[] args) {

        Job job1 = new Job("Python Developer", 1200);
        Job job2 = new Job("Java Developer", 1100);
        Job job3 = new Job("Medical Physicist", 1500);

        System.out.println("=== Tech Career OOP System ===");

        job1.displayJob();
        job2.displayJob();
        job3.displayJob();
    }
}
