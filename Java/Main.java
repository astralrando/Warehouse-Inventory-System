import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        boolean isloggedin = true;
        boolean isadmin = true;
        if (isloggedin && isadmin){
            System.out.println(true);
        }
        else{
            System.out.println(false);
        }
    }
}