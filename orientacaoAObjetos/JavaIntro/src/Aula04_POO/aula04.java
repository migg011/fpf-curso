package Aula04_POO;

import java.util.*;

public class aula04 {
    public static void main(String[] args) {

        // Lista


//        List<String> frutas = new ArrayList<>();
//
//        System.out.println("Lista inicial: "+frutas);
//        frutas.add("Maça");
//        frutas.add("Banana");
//        frutas.add("uva");
//        frutas.add(0, "Morango");
//        System.out.println("Lista apos a adição: "+frutas);
//
//        String segundaFruta = frutas.get(1);
//        System.out.println("A fruta na posição 1 é: "+ segundaFruta);
//
//        System.out.println("Tamanho da lista: "+frutas.size());
//
//        frutas.remove("Morango");
//         frutas.remove(0); //pelo index tmb
//        System.out.println("Lista apos a remoção: "+frutas);
//
//        System.out.println("Percorrendo: ");
//        for (String fruta : frutas) {
//            System.out.print(fruta + " | ");
//        }


        //stack (pilha)


//        Deque<Integer> pilha = new ArrayDeque<>();
//
//        System.out.println("Pilha Inicial: "+ pilha);
//        pilha.push(101);
//        pilha.push(202);
//        pilha.push(303);
//        System.out.println("Pilha Final: "+ pilha);
//
//        //elemento do topo
//        int topo = pilha.peek();
//        System.out.println("o topo da pilha é: "+ topo);
//
//        //pop: remover
//        int removido1 = pilha.pop();
//        int removido2 = pilha.pop();
//
//        System.out.println("Elemento removido 1: "+ removido1);
//        System.out.println("Elemento removido 2: "+ removido2);
//        System.out.println("Pilha apos o pop: "+ pilha);

        // MAPs


//        Map<String, Integer> estoque = new TreeMap<>();
//        estoque.put("Notebook",50);
//        estoque.put("Mouse",100);
//        estoque.put("Teclado",75);
//        estoque.put("Notebook",40);
//        System.out.println("Mapa apos a put e atualizaçãoes: "+ estoque);
//
//        int qntdNotebook = estoque.get("Notebook");
//        System.out.println("Quantiade de notebook: "+qntdNotebook);
//
//        boolean temMouse = estoque.containsKey("Mouse");
//        boolean temMonitor = estoque.containsKey("Monitor");
//
//        System.out.println("Tem mouse? "+ temMouse);
//        System.out.println("Tem monitor? "+ temMonitor);
//
//        System.out.println(" ------------ MAPA DETALHADO ------------");
//        for(String produto: estoque.keySet()){
//            int quantidade = estoque.get(produto);
//            System.out.println(produto + ": " + quantidade + " unidades.");
//        }


        //map com objeto


//        Map<String, Object> dadosUsuarios = new HashMap<>();
//        dadosUsuarios.put("nome", "Lilly");
//        dadosUsuarios.put("idade", 18);
//        dadosUsuarios.put("ativo", true);
//
//        String nome = (String)  dadosUsuarios.get("nome");
//        int idade = (Integer) dadosUsuarios.get("idade");
//        boolean ativo = (Boolean) dadosUsuarios.get("ativo");
//
//        System.out.printf("Nome: %s%nIdade: %d%nAtivo: %b%n", nome, idade, ativo);


        //Exeções (try, except...)


        try {
            Scanner sc = new Scanner(System.in);
            int numerador =  sc.nextInt();
            int denominador = sc.nextInt();

            System.out.println("Iniciando a operação de divisao...");
            System.out.println("Tentando dvidir: "+ numerador + " por " + denominador);

            int resultado =  numerador / denominador;
            System.out.println("Resultado da divisao: " + resultado);
        } catch (ArithmeticException e) {
            System.err.println("\n--- Exceção Capturada ---");
            System.err.println("Erro: nao é possivel dividir por zero.");
            System.err.println("Mensagem: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Ocorreu um eror inesperado: " + e.getMessage());
        } finally {
            System.out.println("\n---Bloco Finally ---");
            System.out.println("Operação de limpeza ou finalização concluida");
            System.out.println("O programa pode continuar normalmente");
        }

    }
}
