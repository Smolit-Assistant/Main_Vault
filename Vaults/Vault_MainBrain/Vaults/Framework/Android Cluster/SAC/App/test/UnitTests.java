import org.junit.Test;
import static org.junit.Assert.*;

public class CalculatorUnitTest {

    @Test
    public void add_twoNumbers_correctResult() {
        Calculator calculator = new Calculator();
        assertEquals(4, calculator.add(2, 2));
    }

    // Weitere Testmethoden für andere Funktionen von Calculator
}

class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    // Weitere Methoden der Calculator-Klasse
}
