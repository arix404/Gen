def chatbot():
    print("Welcome to Customer Support Bot!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        
        if "bye" in user:
            print("Bot: Thank you! Visit again.")
            break

        
        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you?")

        
        elif "product" in user:
            print("Bot: We offer clothes, shoes, and accessories.")

        
        elif "price" in user or "cost" in user:
            print("Bot: Prices start from ₹500 depending on product.")

        
        elif "service" in user:
            print("Bot: We provide delivery, returns, and support services.")

        
        elif "delivery" in user:
            print("Bot: Delivery takes 3-5 business days.")

        
        elif "return" in user:
            print("Bot: You can return products within 7 days.")

        
        else:
            print("Bot: Sorry, I didn’t understand. Please ask about product, price, or service.")

chatbot()