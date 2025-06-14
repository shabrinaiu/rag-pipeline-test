from transformers import AutoTokenizer, pipeline
import torch
import bitsandbytes, accelerate

from . import LLMGenerator
from utils.config import default_llm_model


class GemmaGenerator(LLMGenerator):
    """
    Google Gemma LLM generator for text generation tasks.
    Uses HuggingFace Transformers pipeline with quantization for efficiency.
    """

    def __init__(self, model_name=default_llm_model):
        super().__init__(
            name="Gemma",
            description="A large language model developed by Google, designed for various natural language processing tasks.",
        )

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Initialize the pipeline
        self.pipeline = pipeline(
            "text-generation",
            model=model_name,
            tokenizer=self.tokenizer,
            model_kwargs={
                "torch_dtype": torch.float16,
                "quantization_config": {"load_in_4bit": True},
            },
        )

    def generate(self, prompt, **kwargs):
        """
        Generate a response from the Gemma LLM given a prompt and optional parameters.
        Handles both list and dict output structures from the pipeline.
        """
        chat_prompt = self.tokenizer.apply_chat_template(
            prompt, tokenize=False, add_generation_prompt=True
        )
        outputs = self.pipeline(
            chat_prompt, max_new_tokens=256, do_sample=True, temperature=0.1
        )
        # Robustly handle output structure
        if (
            isinstance(outputs, list)
            and len(outputs) > 0
            and "generated_text" in outputs[0]
        ):
            generated_text = outputs[0]["generated_text"]
            generated_answer = generated_text[len(chat_prompt) :]
        elif isinstance(outputs, dict) and "generated_text" in outputs:
            generated_text = outputs["generated_text"]
            generated_answer = generated_text[len(chat_prompt) :]
        else:
            generated_answer = str(outputs)
        return generated_answer
