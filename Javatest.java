public class Javatest {
	public static void test(Student student){
		student.setAge(100);
	}
	
	public static void main(String[] args) {
		Student student = new Student();
		
		student.setName("ÕÅÈı");
		test(student);
		
		System.out.println(student);
	}
} 

class Student {
	String name;
	int age;
	
	public String getName(){
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	
	public String toString() {
		return "name: " + this.getName() +
			" age: " + this.getAge();
	}
}