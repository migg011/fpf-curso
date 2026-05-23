package Aula01;

import java.util.Scanner;

public class Ex01 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double salarioBase;
        double salarioLiquido;

            System.out.print("Digite seu salario-base: ");
                salarioBase = scanner.nextDouble();
            salarioLiquido = salarioBase + (salarioBase * 0.5) - (salarioBase * 0.7);

        System.out.println(salarioLiquido);
        scanner.close();
    }
}
