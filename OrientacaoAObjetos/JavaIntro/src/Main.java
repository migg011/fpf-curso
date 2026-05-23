import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        //Declaração de Tipo de Dados
        byte TypeByte = 12;
        short TypeShort = 42;
        char TypeChar = 'C';
        float TypeFloat = 2.6f;
        double TypeDouble = 3.59;
        int TypeInt = 23971310;
        long TypeLong = 317293711L;
        boolean TypeBoolean = true;

        //Output dos Tipos de Dados
        System.out.println("Byte: " + TypeByte);
        System.out.println("Short: " + TypeShort);
        System.out.println("Char: "+ TypeChar);
        System.out.println("Float: " + TypeFloat);
        System.out.println("Double: " + TypeDouble);
        System.out.println("Int: "+ TypeInt);
        System.out.println("Long: " + TypeLong);
        System.out.println("Boolean: "+ TypeBoolean);

        //abre o scanner
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite sua idade: ");
            int idade = scanner.nextInt();
        System.out.println("Sua idade é: " + idade + " anos");

        System.out.print("Digite seu nome: "); //faz uma pergunta
            String nome = scanner.next(); // ler a variavel que vai pegar o resultado
        System.out.println("Olá " + nome + "!"); //mostra o resultado

        scanner.close(); //fim do scanner

        //Formatação de Strings
        String nome2 = "Miguel";
        double nota = 7.899;

        System.out.printf("Ola, %s, Sua nota é %.2f\n", nome2, nota);

        System.out.println("Valor absoluto de -10: " + Math.abs(-10));
        System.out.println("Maior entre 5 e 9: " + Math.max(5, 9));
        System.out.println("2 elevado a 5: " + Math.pow(2, 5));
        System.out.println("Raiz quadrada de 25: " + Math.sqrt(25));
        System.out.println("Numero Aleatorio:" + Math.random());
        
    }
}