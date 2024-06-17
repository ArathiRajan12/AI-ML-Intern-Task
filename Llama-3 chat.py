


def generate_llama3_response(user_input):
    # Placeholder function to simulate Llama-3's response generation
    responses = {
        "hello": "Hello there!",
        "how are you?": "I'm just a llama-3, I don't have feelings, but thanks for asking!",
        "tell me a joke": "Why did the llama cross the road? To spit at the rude driver on the other side!",
        "bye": "Goodbye! Have a llama-tastic day!"
    }
    
    # Check if the user's input matches any predefined response
    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "Sorry, I didn't understand that."

def main():
    print("Welcome to Llama-3 Chat!")
    print("You can start chatting. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")  # Prompt user for input
        
        # Process the user's input and generate a response from Llama-3
        response = generate_llama3_response(user_input)
        
        # Display Llama-3's response
        print("Llama-3:", response)
        
        # Check if the user wants to exit the chat
        if user_input.lower() == "bye":
            print("Llama-3 Chat ended.")
            break  # Exit the loop

if __name__ == "__main__":
    main()







