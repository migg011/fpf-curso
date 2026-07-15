package Aula07_POO.Modificadores;

public class Circulo extends Forma {
    public double raio;

    public Circulo(double raio){
        this.raio = raio;
    }

    public double calcularArea(){
        return Math.PI*Math.pow(this.raio,2);
    }
}
