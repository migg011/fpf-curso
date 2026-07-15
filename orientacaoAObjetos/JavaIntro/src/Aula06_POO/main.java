//package Aula06_POO;
//
//import Aula06_POO.Models.Funcionario;
//import Aula06_POO.Models.Pessoa;
//import Aula06_POO.utils.Impressora;
//
//public class main {
//    public static void main(String[] args) {
//        Pessoa p = new Pessoa("Miguel", 17, "Manaus", 9000);
//        Funcionario f = new Funcionario("Fulano", 90, "Rio Preto", -0);
//        Impressora imp = new Impressora();
//
//        System.out.println("=== testes dentro do mesmo pacote ===");
//        f.mostrarAcessos();
//
//        System.out.println("=== testes em outros pacote (utils)===");
//        imp.imprimir(p);
//
//        System.out.printf("Nome: %s - Idade: %d - Cidade: %s - Salario: %.2f", p.nome, p.idade, p.cidade.p.salario);
//        p.exibirInfoPublica();
//        p.testarPrivadoDentro();
//        p.exibirProtegido();
//        p.exibirPrivado();
//    }
//
//}
