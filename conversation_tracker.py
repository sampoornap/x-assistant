history = []

class ConversationHistory:
    def __init__(self, max_history=5):
        self.max_history = max_history

    def add_interaction(self, user_query, assistant_response):
        # Add new interaction to history
        history.append({
            "user": user_query,
            "assistant": assistant_response
        })
        # Limit the history size to avoid too much context being passed
        # print("History is ", history)
        if len(history) > self.max_history:
            history.pop(0)  # Remove oldest interaction

    def get_conversation_history(self):
        # Format conversation history for sending to the language model
        formatted_history = ""
        for turn in history:
            formatted_history += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"
        return formatted_history

    def clear_history(self):
        history = []
