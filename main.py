""" Game feature module.
"""

class GameFeature:
    """ 
    Score usernames based on trimmed length.
    Rule: score = 10 × length of the trimmed name
    """

    def compute_score(self, username: str) -> int:
        if not isinstance(username, str):

            """ 
            Examples - GameFeature.compute_score(" alice ") -> 50
            Raises error for non-string inputs
            """
            
            raise TypeError("username must be a string")
        name = username.strip()
        return 0 if name == "" else len(name) * 10
    


