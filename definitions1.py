class Agent():
    """
        Implements the interface for an agent
    """
    def __init__(self,env):
        """
        Constructor for the agent class
        Args:
            env: a reference to an environment
        """
        self.env = env

    def act(self):
        """
        Defines the agent action

        Raises:
            NotImplementedError:If the method is not implemented or not overidden.
        """
        raise NotImplementedError('act')

class Environment:
    """
    Implements the interface for an Environment
    """
    def initial_percepts(self):
        """
        Returns the environment initial percepts
        Raises:
            NotImplementedError: If the method is not implemented or not overidden.
        """
        raise NotImplementedError('initial_percepts')

    def signal(self,action):
        """
        Returns the environment initial percepts
        Raises:
            NotImplementedError: If the method is not implemented or not overidden.
        """
        raise NotImplementedError('signal')