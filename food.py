classmate_foods = {'pizza', 'sushi', 'tacos'}

user_foods = {input("Enter your first favorite food: "), 
              input("Enter your second favorite food: "), 
              input("Enter your third favorite food: ")}

common_foods = user_foods & classmate_foods

if common_foods:
    print("Our common favorite food(s):", *common_foods)
else:
    print("We have no common favorite foods.")
