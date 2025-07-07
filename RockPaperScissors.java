import java.util.Scanner;
import java.util.Random;

public class RockPaperScissors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        String[] options = {"rock", "paper", "scissors"};

        System.out.println("Welcome to Rock, Paper, Scissors!");
        System.out.print("Enter your move (rock, paper, or scissors): ");
        String userMove = scanner.nextLine().toLowerCase();

        // Validate input
        if (!userMove.equals("rock") && !userMove.equals("paper") && !userMove.equals("scissors")) {
            System.out.println("Invalid move! Please enter rock, paper, or scissors.");
            return;
        }

        int computerIndex = random.nextInt(3);
        String computerMove = options[computerIndex];

        System.out.println("Computer chose: " + computerMove);

        if (userMove.equals(computerMove)) {
            System.out.println("It's a tie!");
        } else if (
            (userMove.equals("rock") && computerMove.equals("scissors")) ||
            (userMove.equals("paper") && computerMove.equals("rock")) ||
            (userMove.equals("scissors") && computerMove.equals("paper"))
        ) {
            System.out.println("You win!");
        } else {
            System.out.println("Computer wins!");
        }

        scanner.close();
    }
}
