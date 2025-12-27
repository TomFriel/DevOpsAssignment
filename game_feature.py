""" Game feature module.
    Score usernames based on trimmed length.
    Rule: score = 10 × length of the trimmed name
"""

class GameFeature:
    """Class to compute game feature scores based on usernames."""

    def compute_score(self, username: str) -> int:

        """ 
        Examples - GameFeature.compute_score(" alice ") -> 50
        Raises error for non-string inputs
        """
        if not isinstance(username, str):

            raise TypeError("username must be a string")
        name = username.strip()
        return 0 if name == "" else len(name) * 10
    


