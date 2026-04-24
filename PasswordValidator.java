import java.util.Scanner;
public class PasswordValidator {

    public static boolean checkPassword(String password) {

        boolean upperFind = false;
        boolean digitFind = false;

        if (password.length() < 8) {
            System.out.println("Password is too short");
        return false;
        }

        for(int i = 0; i < password.length(); i++) {

            char presentChar = password.charAt(i);

            if (Character.isUpperCase(presentChar)) {
                upperFind = true;
            }

            if (Character.isDigit(presentChar)) {
                digitFind = true;
            }
        }

      if (!upperFind) {
            System.out.println("Add at least one uppercase letter.");
        }

        if (!digitFind) {
            System.out.println("Include at least one number.");
        }
         return upperFind && digitFind;
    }

    public static void main(String[] args) {
         Scanner input = new Scanner(System.in);
        String paswdInput;

        while (true) {

            System.out.println("\n--- Password Setup ---");
            System.out.println("Rules:");
            System.out.println("• Minimum 8 characters");
            System.out.println("• At least one uppercase letter");
            System.out.println("• At least one number");

            System.out.print("Enter password: ");
            paswdInput = input.nextLine();

            if (checkPassword(paswdInput)) {
                System.out.println("Password saved");
                break;
            } else {
                System.out.println("Please try again\n");
            }
        }

        input.close();
    }
}