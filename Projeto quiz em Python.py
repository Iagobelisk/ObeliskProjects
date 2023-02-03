def new_game(): # função que inicia o quiz.

    guesses = []          # list
    correct_guesses = 0   # variable
    questions_num = 1     # variable

    for key in questions:
        print("---------------------------")
        print(key)
        for i in options[questions_num-1]: # mostra as opções (options) de questões usando o value das respostas corretas [questions_num-1].
            print(i)

        guess = input("Digite (A, B ,C ou D): ") # entrar com as opções A, B, C ou D.
        guess = guess.upper()
        guesses.append(guess) # acrescenta o input (guess) à lista (guesses).

        correct_guesses += check_answer(questions.get(key),guess)  # irá pegar as respostas (guess) e adicionar à check_answer.
        questions_num += 1

    display_score(correct_guesses, guesses) # call display_score() function.

def check_answer(answer, guess):  # irá checar as respostas (guess) e armazenar os resultados: CORRECT e WRONG à variável (guesses).

    if answer == guess:
        print("CORRETO!")
        return 1
    else:
        print("ERRADO!")
        return 0

def display_score(correct_guesses, guesses): # irá mostrar os resultados e a porcentagem de acerto.

    print("---------------------------")
    print("RESULTADO")
    print("---------------------------")

    print("Respostas: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")  # pega as respostas certas de questions e mostra no resultado.
    print()

    print("Palpites: ", end="")
    for i in guesses:
        print(i, end=" ")                 # pega as respostas de guesses e mostra no resultado.
    print()

    score = int((correct_guesses/len(questions)) * 100)  # calcula a porcentagem de acerto das questões.
    print("Sua pontuação é: "+str(score)+"%")              # mostra a porcentagem.

def play_again():   # irá perguntar se quer jogar novamente.

    response = input("Quer jogar de novo? (sim ou não): ")
    response = response.upper()

    if response == "SIM":
        return True
    else:
        return False

# Dictionary
questions = {
    "Quem criou a linguaguem Python?: ": "A",
    "Que ano Python foi criado?: ": "B",
    "Python é uma linguagem orientada à objetos?: ": "B",
    "A terra é redonda?: ": "A",
    "Qual o número de pi? ": "C"
}
# 2D LIST
options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Não", "B. Sim", "C. Um dia será", "D. Já foi"],
    ["A. Verdadeiro", "B. Falso", "C. As vezes", "D. O que é Terra?"],
    ["A. 3", "B. 10", "C. 3.14", "D. 3.13"]]

# call new_game() function
new_game()

# enquanto a função play_again() == TRUE, chama a função new_game() novamente.
while play_again():
    new_game()

print("Até a próxima!")