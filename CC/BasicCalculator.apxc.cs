public class BasicCalculator {

    public Double num1 {get; set;}
    public Double num2 {get; set;}
    public Double result {get; set;}
    public String operation {get; set;}

    public void calculate() {

        if (operation == 'Add') {
            result = num1 + num2;
        }
        else if (operation == 'Subtract') {
            result = num1 - num2;
        }
        else if (operation == 'Multiply') {
            result = num1 * num2;
        }
        else if (operation == 'Divide') {
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                result = 0;
            }
        }
    }
}