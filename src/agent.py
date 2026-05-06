class Agent:
    def __init__(self, llm, prompt_system):
        self.llm = llm
        self.prompt_system = prompt_system
        self.memory = []

    def run(self, user_input):
        self.memory.append({"role": "user", "content": user_input})

        messages = [
            {"role": "system", "content": self.prompt_system},
            *self.memory
        ]

        response = self.llm.generate(messages)

        self.memory.append({"role": "assistant", "content": response})

        return response