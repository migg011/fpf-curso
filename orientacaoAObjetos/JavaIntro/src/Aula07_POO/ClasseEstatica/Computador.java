package Aula07_POO.ClasseEstatica;

public class Computador {
    private String Marca = "Dell";

    class PlacaMae {
        public void mostrarMarca(){
            System.out.println("Marca: " + Marca);
        }
    }

    static class Fonte {
        public void info(){
            System.out.println("fonte generica");
        }
    }
}
