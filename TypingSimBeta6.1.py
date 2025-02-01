import time
import random
from cryptography.fernet import Fernet
pinto = 10
county = 0
times = 0
Head = ("Heads", "Tails")
q = ["Highly effective", "Extremely effective", "Nothing happened", "Very little effect", "Normal effection"]
let = ("A", "B", "C")
port = ("2020", "8080", "7676", "6667")
color = "❗"
while True:
    ans = input("<Typing Simulator>")
    if ans == "var /a":
        print("Welcome Admin. You are now in secure shell!")
    elif ans == "var":
	    print("Var has been enabled. You now have Eli ressistance!")
    elif ans == "Godot" or ans == "./Godot":
        while true:
            anse == input("<GodotShell(1.0)>")
            if anse == "print("")":
                print("One or more args required")
            elif anse == "quit":
                break
    elif ans == "var /b":
        print(random.choice(color))
    elif ans == "ohio":
        print("Skibidi ohio sigma? Are you mewing?")
        time.sleep(3)
        for i in range(1, 100):
            print("Are you mewing?")
            time.sleep(0.01)
    elif ans == "":
        print("Type something in")
    elif ans == "mine /pint":
        while True:
            T = random.choice(let)
            rr = random.choice(port)
            print(f"Mining {T} on port {rr}")
            pinto +=1
            county +=1
            print(pinto)
            if county == 300:
                county = 0
                break
    elif ans == "coin flip":
        while True:
            coinn = input("Heads or Tails?")
            uii = random.choice(Head)
            pino = input("How much pinto?")
            if float(pino) > pinto:
                print("Invalid amount.")
                break
            if uii == coinn:
                print("Ya won!")
                pinto += float(pino)
                print(pinto)
            else:
                print("Nope")
                pinto -= float(pino)
                print(pinto)
    elif ans == "encjournal":
        print("Encypted journal 1.0")
        while True:
            journ = input("Write some stuff securely!")
            key = Fernet.generate_key()
            yik = Fernet(key)
            joun = journ.encode('utf-8')
            writey = yik.encrypt(joun)
            print("This is the encrypted thingy:")
            print(writey)
            
    else:
            print(ans)
