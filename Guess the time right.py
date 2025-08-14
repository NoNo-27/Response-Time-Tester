   
import time
import random

while True:
    print ("\nwelcome to the Best Response time Tester!".upper())
    time.sleep(1)

    # Get user's name
    while True:
        user_name = input ("\nTo begin enter enter your name: ".upper()).strip()
        if all(char.isalpha() or char.isspace() for char in user_name):
            print("\nWelome", user_name, "to the best Response time Tester ever created! " ) 
            break
        else:
            print("Please enter  a word that contains only letters.")

    # Get the number of rounds to play
    while True:
        try:
            num_rounds = int(input("\nHow many rounds would you like to play " + user_name + "? "))
            if num_rounds < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please enter a Positive Integer.")
            
    # Explain the game to the user

    print ("\nNow on you will be asked to press enter after random time, to check your reaction time, for", num_rounds, "round", "\nALL THE BEST", "\nPress enter when Ready!".upper())
    input ()
    
    # Define a function to calculate the rating based on the difference between the target and the response time
    def calculate_rating(difference):
        if difference <= 0.25:
            return "Excellent!"
        elif difference > 0.25 and difference <= 0.5:
            return "Great!"
        elif difference > 0.5 and difference <= 1:
            return "Good!"
        elif difference > 1 and difference <= 2:
            return "OK!"
        else:
            return "Miss!"
        
    # Initialize lists to store the targets, responses, and differences
    targets = []   
    responses = []      
    differences = []

    # Play the game for the given number of rounds
    for i in range(1, num_rounds+1):

        print(f"\nRound {i} of {num_rounds}.")
        print("You ready!")

        duration = 3
        for i in range(duration, 0, -1):
            print(i)
            time.sleep(1)
            
    # Get a random target time
        target = random.randint(2, 8) 
        targets.append(target)

    # Instruct the user to press Enter after the target time has elapsed
        print(f"Press Enter in {target} seconds.")

    # Record the response time and calculate the difference from the target time
        start_time = time.time()
        input()
        response = round(time.time() - start_time, 2)

    # Calculate the rating for the response time
        difference = abs(response - target)
        differences.append(difference)
        if difference == 0:
            rating = "Spot on!"
        else:
            rating = calculate_rating(difference)

    # Record the response and rating
        responses.append(response)

    # Print the response time and rating for the round
        print(f"Response time: {response}s")
        if rating == "Spot on!":
            print(rating)
        else:
            print(f"Rating: {rating} ({'early' if response < target else 'late'})")

    # Print testing complete message
    print("\nTesting complete! Press Enter to see a breakdown of your results.")
    input()

    # Print a breakdown of the user's results
    print("Round\tTarget\tResponse\tDifference")
    for i in range(num_rounds):
        print(f"{i+1}\t{targets[i]}\t{responses[i]}s\t\t{differences[i]:.2f}s {'(early)' if responses[i] < targets[i] else '(late)'}")
        
    time.sleep(1)
    print ("\nYour Overall rating!")

    # Calculate and print overall rating
    total_difference = sum(differences)
    average_difference = total_difference / num_rounds
    overall_rating = calculate_rating(average_difference)
    print(f"\nYou usually respond {'early' if average_difference < 0 else 'late'}.")
    print(f"Overall rating: {overall_rating}")

    time.sleep (1)
    answer = input("\nDo you want to continue? (y/n)")

    if answer == "n":
        break
