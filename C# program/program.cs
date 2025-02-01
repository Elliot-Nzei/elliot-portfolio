using System;

class Program
{
    static void Main()
    {
        Random random = new Random();
        int secretNumber = random.Next(1, 101);
        int guess = 0;
        int attempts = 0;

        Console.WriteLine("Welcome to the Number Guessing Game!");
        Console.WriteLine("I have picked a number between 1 and 100. Try to guess it!");

        while (guess != secretNumber)
        {
            Console.Write("Enter your guess: ");
            string input = Console.ReadLine();
            
            if (int.TryParse(input, out guess))
            {
                attempts++;
                if (guess < secretNumber)
                {
                    Console.WriteLine("Too low! Try again.");
                }
                else if (guess > secretNumber)
                {
                    Console.WriteLine("Too high! Try again.");
                }
                else
                {
                    Console.WriteLine($"Congratulations! You guessed the number {secretNumber} in {attempts} attempts.");
                }
            }
            else
            {
                Console.WriteLine("Invalid input! Please enter a number.");
            }
        }
    }
}
