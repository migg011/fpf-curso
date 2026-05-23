package Aula01;

import java.util.Scanner;

public class Ex03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int leitores;
        int votosBrancos;
        int votosNulos;
        int votosValidos;

        System.out.print("digite o total de leitores");
            leitores = scanner.nextInt();
        System.out.print("digite o numero de votos brancos: ");
            votosBrancos = scanner.nextInt();
        System.out.print("digite o numero de votos nulos: ");
            votosNulos = scanner.nextInt();
        System.out.print("digite o numero de votos validos: ");
            votosValidos = scanner.nextInt();

        System.out.println("Porcentagem do Valores pelo total de Leitores");
        System.out.printf("Brancos: ",  (Double.valueOf((leitores)/votosBrancos)*100.0));
        System.out.printf("Nulos: ",  (Double.valueOf((leitores)/votosNulos)*100.0));
        System.out.printf("Validos: ",  (Double.valueOf((leitores)/votosValidos)*100.0));

        scanner.close();
    }
}
