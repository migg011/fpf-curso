package Aula01;

import java.util.Scanner;

public class Ex02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double preco;
        int quantidade;
        double valorFinal;

        System.out.print("Digite o preço do produto: ");
            preco = scanner.nextDouble();
        System.out.print("Digite o quantidade que vai comprar: ");
            quantidade = scanner.nextInt();

        valorFinal = preco * quantidade;

        System.out.println("o valor final sera de: "+ valorFinal);


        scanner.close();
    }
}
