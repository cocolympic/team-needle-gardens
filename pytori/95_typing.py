from typing import List, Dict, Tuple, Optional

def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

def get_numbers() -> List[int]:
    return [1, 2, 3]

def get_user() -> Dict[str, str]:
    return {"name": "Alice", "role": "admin"}

def get_coords() -> Tuple[float, float]:
    return (35.6, 139.7)

def maybe_str(flag: bool) -> Optional[str]:
    return "yes" if flag else None