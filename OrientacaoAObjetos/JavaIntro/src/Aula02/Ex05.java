package Aula02;
import java.util.Scanner;

public class Ex05 {
    public static void main(String[] args) {
        Scanner  sc = new Scanner(System.in);
        System.out.println("Digite o numero do funcionario");
        String nome = sc.next();
        System.out.println("Quantas horas trabalhadas: ");
        double horasTrabalhadas = sc.nextDouble();
        System.out.println("Recebe quantos p/Hora: ");
        double horasRecebidas = sc.nextDouble();

        sc.close();

        double salario =  horasTrabalhadas * horasRecebidas;

        System.out.printf("Funcionario: %s, Salario: %.2f", nome, salario);
    }
}
