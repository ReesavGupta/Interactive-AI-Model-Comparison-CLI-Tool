from typing import Dict, Any, Union


def token_summary(response: Dict[str, Any]) -> str:
    """
    Generate a summary of token usage from a model response.
    
    Args:
        response: Dictionary containing model response with token usage info
        
    Returns:
        String summary of token usage
    """
    token_usage = response.get("token_usage") or response.get("tokens")
    
    if token_usage is None:
        return "N/A"
    elif isinstance(token_usage, int):
        return str(token_usage)
    else:
        return str(token_usage)
