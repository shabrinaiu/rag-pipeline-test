class LLMGenerator:
    """
    Abstract base class for large language model (LLM) generators.
    Subclasses should implement the generate method for specific LLMs.
    """

    def __init__(self, name, description):
        """
        Initialize the LLMGenerator with a name and description.

        :param name: The name of the LLM generator.
        :param description: A brief description of the LLM generator.
        """
        self.name = name
        self.description = description

    def generate(self, *args, **kwargs):
        """
        Generate a response using the LLM.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def __str__(self):
        """
        Return a string representation of the LLMGenerator.

        :return: A string in the format "name - description".
        """
        return f"{self.name} - {self.description}"
