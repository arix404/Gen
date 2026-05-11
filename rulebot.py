def chatbot():
    print("Customer Support Chatbot")
    print("Ask your queries (type 'bye' to exit)\n")

    while True:
        user = input("You: ").lower()

        
        if "bye" in user:
            print("Bot: Thank you! Have a great day.")
            break

        
        elif any(word in user for word in ["hello", "hi", "hey"]):
            print("Bot: Hello! How can I assist you?")

        elif any(word in user for word in ["product", "item", "available"]):
            print("Bot: We offer clothes, shoes, and accessories.")

        elif any(word in user for word in ["price", "cost", "rate"]):
            print("Bot: Prices start from ₹500.")

        elif any(word in user for word in ["service", "help", "support"]):
            print("Bot: We provide delivery, returns, and customer support.")

        elif any(word in user for word in ["delivery", "shipping"]):
            print("Bot: Delivery takes 3-5 business days.")

        elif any(word in user for word in ["return", "refund"]):
            print("Bot: You can return items within 7 days.")

        else:
            print("Bot: Sorry, I didn't understand. Please try another query.")

chatbot()