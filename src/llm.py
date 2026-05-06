from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLM:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("🔄 Loading model (ONE TIME)")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "initialized"):
            return

        model_name = "Qwen/Qwen2.5-1.5B-Instruct"

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.initialized = True

    def generate(self, messages):
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        output = self.model.generate(**inputs, max_new_tokens=256)

        output = output[0][len(inputs.input_ids[0]):]

        return self.tokenizer.decode(output, skip_special_tokens=True)