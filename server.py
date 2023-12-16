import socket 
from threading import Thread
import random


#server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address = "127.0.0.2"
port = 8000
server.bind((ip_address,port))
server.listen()
list_of_clients = []

#quiz question and answer
questions = ["What is the capital of Australia?\n  a. Sydney\n  b. Melbourne\n  c. Canberra\n  d. Perth",
             
             "Who painted the Mona Lisa? \n  a. Vincent van Gogh\n  b. Pablo Picasso\n  c. Leonardo da Vinci\n  d. Michelangelo",

             "What is the largest ocean in the world?\n a. Atlantic Ocean \n   b. Indian Ocean \n   c. Arctic Ocean \n  d. Pacific Ocean",

             "Who wrote the play 'Romeo and Juliet'? \n a William Shakespeare \n b. Jane Austen \n  c. Charles Dickens \n  d. F. Scott Fitzgerald"

]

answers = ["c" , "c" , " d" , "a"]

#function
def clientthread(conn,addr):
     score = 0
     conn.send("Welcome to this Quiz game!".encode('utf-8'))
     conn.send("You will receive a question. the answer to that question should be one of a , b , c , d\n".encode('utf-8'))
     conn.send("GoodLuck!\n\n".encode('utf-8'))
     index, questions , answers = get_random_question_answer(conn)
     while True:
          try:
               message = conn.recv(2048).decode('utf-8')
               if message:
                    if message.lower() == answers:
                         score+=1
                         conn.send(f"Bravo! Your score is{score}\n\n".encode('utf-8'))
                    else:
                         conn.send("Incorrect! Better Luck next time\n\n".encode('utf-8'))     
                    remove_question(index)
                    index, questions, answers = get_random_question_answer(conn)
               else:
                    remove(conn) 
          except:
               continue          


def remove(conn):
    if conn in list_of_clients:
        list_of_clients.remove(conn)


#for getting question and answer
def get_random_question_answer(conn): 
     random_index = random.randint(0,len(questions) - 1)
     random_question = questions[random_index]
     random_answers = answers[random_index]
     conn.send(random.question.encode('utf-8'))
     return random_index, random_question, random_answers


#remove_question() function 
def remove_question(index):
     questions.pop(index)
     answers.pop(index)



#from client
while True:
     conn,addr = server.accept()
     conn.send('NICKNAME').encode('utf-8')
     nm = conn.recv(2048).decode('utf-8')
     list_of_clients.append(conn)
     nicknames.append(nickname)
     print (nickname + "connected!")
     new_thread = Thread(target= clientthread,args=(conn,addr))
     new_thread.start()





# loop for accepting connection
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    new_thread = Thread(target= clientthread,args=(conn,addr))
    new_thread.start()








