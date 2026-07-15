package Aula02;

import java.util.Scanner;

public class Ex04 {
    public static void main(String[] args) {
        double nota1;
        double nota2;

        Scanner input = new Scanner(System.in);
        System.out.println("Digite a nota 1: ");
        nota1 = input.nextDouble();
        System.out.println("Digite a nota 2: ");
        nota2 = input.nextDouble();

        input.close();

        double media = ((nota1 * 2) + (nota2 * 3)) / 5;

        System.out.printf("a media das notas é: %.2f", media);
    }
}
