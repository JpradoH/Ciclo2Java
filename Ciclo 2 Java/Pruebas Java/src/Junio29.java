import java.util.Scanner;

public class Junio29{
    public static void main(String args []){
        Scanner scanner = new Scanner(System.in);
        int numero = scanner.nextInt();
        int resultado = contadorDigitos(numero);
        System.out.println(resultado);
    }
    public static int contadorDigitos(int numero){
        //1990->4
        int cifras = 4;
        while(numero !=0){
            numero  /= 10;
            cifras++;
        }
        return cifras;
    }
    
}
