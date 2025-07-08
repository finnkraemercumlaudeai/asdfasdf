def subfunction(name: str | None) -> str:
    """
    Given an optional name, return the same greeting
    you had in your test function.
    """
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, world!"
