package Java_playground;
public class playground {
    public class Tutor{
        public String name;
        public int age;
        public String subject;
        public Tutor(String name, int age, String subject){
            this.name = name;
            this.age = age;
            this.subject = subject;
        }
        public void printTutor(){
            System.out.println("Name: " + this.name);
            System.out.println("Age: " + this.age);
            System.out.println("Subject: " + this.subject);
        }
    }
    public static void main(String[] args) {
        System.out.println("Hello World");
        int num = 5;
        System.out.println(num);
        for(int i = 0; i < 6; i++){
            System.out.println(i);
        }

    }
}
