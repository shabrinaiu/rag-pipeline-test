from typing import Dict, Any, Optional

class Document:
    """
    Data transfer object representing a text document and its metadata.
    Used throughout the pipeline for consistent data handling.
    """
    def __init__(self, page_content: str, metadata: Optional[Dict[str, Any]] = None):
        self.page_content = page_content
        self.metadata = metadata if metadata is not None else {}

    def __repr__(self):
        return f"Document(page_content={self.page_content[:30]}..., metadata={self.metadata})"