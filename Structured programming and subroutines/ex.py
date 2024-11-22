# # check the nnumber is prime or not

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# n = int(input("Enter a number: "))

# if is_prime(n):
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")



# def calculate_discount(price, discount_rate):
#     """Calculate the discounted price."""
#     discounted_price = price - (price * discount_rate / 100)
#     return discounted_price

# price = 500
# discount_rate = 10
# final_price = calculate_discount(price, discount_rate)
# print(f"Final Price: {final_price}")



def ask_question(question, correct_answer):
    """Ask a question and return True if the answer is correct."""
    answer = input(question + " ")
    return answer.lower() == correct_answer.lower()

def calculate_score(results):
    """Calculate the total score from the results."""
    return sum(results)

def main():
    """Main procedure to run the quiz."""
    print("Welcome to the Quiz!")   
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 5 + 7?", "12"),
        ("What programming language is this?", "Python")
    ]
    
    results = []
    for question, correct_answer in questions:
        results.append(ask_question(question, correct_answer))
    
    score = calculate_score(results)
    print(f"You got {score}/{len(questions)} questions correct!")

if __name__ == "__main__":
    main()