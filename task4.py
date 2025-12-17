def chatbot():
    print("Chatbot : Hello! ")

    while True:
       user=input("You :").lower()

       if user == "hello":
           print("Chatbot : Hi!")

       elif user == "how are you":
           print("Chatbot : I'm fine,thanks!")

       elif user == "bye":
           print("Chatbot : Goodbye!")
           break

       else :
           print("Chatbot : Sorry,I donot understand")

chatbot()