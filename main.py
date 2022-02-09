# Hash Code 2022 Practice Round
# Problem: https://codingcompetitions.withgoogle.com/hashcode/round/00000000008f5ca9/00000000008f6f33
# Title: "One Pizza"
# Description:
# You are opening a small pizzeria. In fact, your pizzeria is so small that you
# decided to offer only one type of pizza. Now you need to decide what ingredients to include (peppers? tomatoes? both?).
# Everyone has their own pizza preferences. Each of your potential clients has some ingredients they like,
# and maybe some ingredients they dislike. Each client will come to your pizzeria if both conditions are true:
# 1. all the ingredients they like are on the pizza, and
# 2. none of the ingredients they dislike are on the pizza.
# Each client is OK with additional ingredients they neither like or dislike being present on the pizza.
# Your task is to choose which ingredients to put on your only pizza type, to maximize the number of clients that
# will visit your pizzeria.
# Input:
# The first line contains one integer 1≤C≤10^5 - the number of potential clients.
# The following 2×C lines describe the clients’ preferences in the following format:
# First line contains integer 1≤L≤5, followed by L names of ingredients a client likes, delimited by spaces.
# Second line contains integer 0≤D≤5, followed by D names of ingredients a client dislikes, delimited by spaces.
# Each ingredient name consists of between 1 and 15 ASCII characters. Each character is one of the lowercase letters (a-z) or a digit (0-9).
#
# Output:
# The submission should consist of one line consisting of a single number 0≤N followed by a list of N ingredients
# to put on the only pizza available in the pizzeria, separated by spaces.
# The list of ingredients should contain only the ingredients mentioned by at least one client, without duplicates.
#
# Scoring:
# The score of a submission is the number of clients that will visit your pizzeria.
# A client will come to your pizzeria if all the ingredients they like are on the pizza and
# none of the ingredients they dislike are on the pizza.
import tqdm.auto as tqdm


# Define solution function

def solve(clients):
    """
    Solve problem.
    """
    # Initialize solution.
    solution = []

    # Make a list of all ingredients.
    ingredients = []
    for client in clients:
        ingredients.extend(client[1])
        ingredients.extend(client[2])
    ingredients = list(set(ingredients))

    # From the list of ingredients, remove those that are disliked and add them to a saperate list.
    disliked = set()
    for ingredient in ingredients:
        for client in clients:
            if ingredient in client[2]:
                disliked.add(ingredient)

    # Remove disliked ingredients from the list of ingredients if they are present.
    for ingredient in disliked:
        if ingredient in ingredients:
            ingredients.remove(ingredient)

    # Add ingredients to solution.
    for ingredient in ingredients:
        solution.append(ingredient)

    # Evaluate current solution.
    current_score = 0
    for client in clients:
        # If client likes all ingredients and dislikes no ingredients, add one to score.
        if set(client[1]).issubset(set(solution)) and set(client[2]).isdisjoint(set(solution)):
            current_score += 1

    best_solution = solution
    best_score = current_score

    # for each ingredient in the list of disliked ingredients.
    for ingredient in tqdm.tqdm(disliked):

        # add the ingredient to the solution
        solution.append(ingredient)

        # calculate the score of the solution
        score = 0
        for client in clients:
            # If client likes all ingredients and dislikes no ingredients, add one to score.
            if set(client[1]).issubset(set(solution)) and set(client[2]).isdisjoint(set(solution)):
                score += 1

        # if the score is better or equal to the best score, update the best solution and score.
        if score >= best_score:
            best_solution = solution
            best_score = score
        # if the score is not better than the best score, remove the ingredient from the solution
        else:
            solution.remove(ingredient)

    # # Loop over clients.
    # for client in clients:
    #     # Get client preferences.
    #     likes = client[1]
    #     dislikes = client[2]
    #     # Loop over likes.
    #     for like in likes:
    #         # If like is not in solution.
    #         if like not in solution:
    #             # Append like to solution.
    #             solution.append(like)
    #
    #     # Loop over dislikes.
    #     for dislike in dislikes:
    #         # If dislike is in solution.
    #         if dislike in solution:
    #             # Remove dislike from solution.
    #             solution.remove(dislike)

    # Return solution.
    return best_solution


def main():
    """
    Main function.
    """

    # Input file paths.
    a_an_example = "input/a_an_example.in.txt"
    b_basic = "input/b_basic.in.txt"
    c_coarse = "input/c_coarse.in.txt"
    d_difficult = "input/d_difficult.in.txt"
    e_elaborate = "input/e_elaborate.in.txt"

    # for each input file.
    for input_file in [a_an_example, b_basic, c_coarse, d_difficult, e_elaborate]:

        # Read input file.
        with open(input_file, "r") as f:
            # Read number of clients.
            n_clients = int(f.readline())
            # Read clients preferences.
            clients = []
            # Each client has two lines.
            for i in range(n_clients):
                # Get client likes.
                likes = f.readline().split()[1:]
                # Get client dislikes.
                dislikes = f.readline().split()[1:]
                # Append client preferences to clients.
                clients.append([i, likes, dislikes])

        # Solve problem.
        solution = solve(clients)

        # Write solution to output file.
        with open("output/{}.out.txt".format(input_file.split("/")[1].split(".")[0]), "w") as f:
            # Write number of ingredients.
            f.write(str(len(solution)) + " ")
            # Write ingredients.
            f.write(" ".join(solution))

        # Evaluate solution.
        with open("output/{}.out.txt".format(input_file.split("/")[1].split(".")[0]), "r") as f:
            # Read ingredients.
            ingredients = f.readline().split()[1:]
            # Initialize score.
            score = 0
            # Loop over clients.
            for client in clients:
                # Get client likes.
                likes = client[1]
                # Get client dislikes.
                dislikes = client[2]

                # If all likes are in solution and none of the dislikes are in solution.
                if all(like in ingredients for like in likes) and not any(
                        dislike in ingredients for dislike in dislikes):
                    # Increment score.
                    score += 1

            # Print score.
            print(score)


if __name__ == '__main__':
    main()
