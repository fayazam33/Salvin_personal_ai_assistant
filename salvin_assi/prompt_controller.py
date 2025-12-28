
class PromptController:
    def __init__(self, role="Assistant"):
        self.role = role

    def build_prompt(self, user_input, memory):
        system_prompt = f"""
                You are SALVIN, a smart personal AI assistant.
                Your role: {self.role}. Behave professionally, clearly and helpfully.
                """

        history = memory.get_history()

        final_prompt = system_prompt + "\n\nConversation:\n"
        for msg in history:
            final_prompt += f"{msg['role'].upper()}: {msg['message']}\n"

        final_prompt += f"\nUSER: {user_input}\nSalvin:"
        return final_prompt
