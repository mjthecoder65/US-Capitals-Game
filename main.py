import random

# Declaring global variables
content_list = [];
wrong_answers = []
counter = 0;

# A function to read local StatesANC.txt file
def file_reader(filename):
    f = open(filename, "r")
    for item in f:
        content_list.append(item.split(","))
# Calling file_reader function
file_reader("StatesANC.txt")

# function to display wrong answers
def display_wrong_answers():
    print("You missed {} question(s)".format(5-counter));
    for item in wrong_answers:
        print(item)

# A function to genearate questions
def question_generator(index):
    global counter # Declare are a global variable
    state_list = content_list[index]
    capital = state_list[3].rstrip('\r\n');
    answer = input("What is the capital of {} ?: ".format(state_list[0]))
    if answer.lower() == capital.lower():
        counter = counter + 1
    else:
        wrong_answers.append(capital + " is the capital of "+state_list[0])
        
# Declaing the main function of the program
def main():
    generated_indexes = [];
    index =  random.randint(0, 49)
    while index not in generated_indexes and len(generated_indexes) < 5:
        generated_indexes.append(index)
        index =  random.randint(0, 49)
    for i in generated_indexes:
        question_generator(i)
    display_wrong_answers()

# Running the program
main()
