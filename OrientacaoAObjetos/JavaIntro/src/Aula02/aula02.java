package Aula02;

import java.util.Scanner;

public class aula02 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
//        System.out.println("Digite sua idade: ");
//        int idade = sc.nextInt();
//
//        if(idade >= 18){
//            System.out.println("Voce é maior de idade");
//        } else {
//            System.out.println("Voce é menor de idade");
//        }
//
//        System.out.println("Digite sua idade: ");
//        double nota = sc.nextInt();
//
//        if(idade >= 18){
//            System.out.println("Voce é maior de idade");
//        } else {
//            System.out.println("Voce é menor de idade");
//        }
//
//        System.out.println("Digite o numero inteiro: ");
//        int numero = sc.nextInt();
//
//        if (numero % 2 == 0){
//            System.out.printf("%d é par", numero);
//        }  else {
//            System.out.printf("%d é impar", numero);
//        }

//        System.out.println("Digite um numero inteiro: ");
//        int numero2 = sc.nextInt();
//
//        if (numero2 % 2 == 0){
//            System.out.printf("o %d é o dobro de %d", numero2, numero2 / 2);
//        } else {
//            System.out.printf("o %d não é o dobro de qualquer numero", numero2);
//        }

//        System.out.println("digite o valor A: ");
//        int a = sc.nextInt();
//        System.out.println("digite o valor B: ");
//        int b = sc.nextInt();
//
//        if (a % b == 0 || b % a == 0 ){
//            System.out.println("Sao multiplos");
//        } else  {
//            System.out.println("Nao sao multiplos");
//        }
//
//        System.out.println("digite um caracter");
//        char caracter = sc.next().charAt(0);
//
//        if (caracter == 'a' || caracter == 'e' || caracter == 'i' ||caracter == 'o' || caracter == 'u'){
//            System.out.println("É uma vogal");
//        } else {
//            System.out.println("Nao é uma vogal");
//        }
//
//        System.out.println("digite um caracter");
//        char Char = sc.next().charAt(0);
//
//        if (caracter == 'a' || caracter == 'e' || caracter == 'i' ||caracter == 'o' || caracter == 'u'){
//            System.out.println("É uma vogal");
//        } else {
//            System.out.println("Nao é uma vogal");
//        }

//        for (int index = 0; index <= 5; index++){
//            System.out.println("Valor de index: " + index);
//        }

        int numeroIndex;

        System.out.print("Digite um numero positivo (ou 0 para sair): ");
        numeroIndex = sc.nextInt();

        while (numeroIndex != 0) {
            System.out.println("voce digitou: " + numeroIndex);
            System.out.print("Digite outro numero (ou 0 para sair): ");
            numeroIndex = sc.nextInt();
        }

        System.out.println("Programa encerrado!");
        sc.close();


    }
}

