from mesa.agent import Agent
from mesa.model import Model
from mesa.space import MultiGrid


class WealthAgent(Agent):
    """
    An agent which can accumulate and distribute wealth.

    Attributes:
        wealth (int): The agent's current wealth.
    """

    def __init__(self, model: Model, initial_wealth=1):
        super().__init__(model)
        self.wealth = initial_wealth

    def move(self):
        """
        Move the agent's position on the model's grid.

        Should be overridden by subclasses.
        """
        if hasattr(self.model, "grid") and isinstance(self.model.grid, MultiGrid):
            possible_moves = self.model.grid.get_neighborhood(
                self.pos,
                moore=True,
                include_center=False,
            )
            new_pos = self.random.choice(possible_moves)
            self.model.grid.move_agent(self, new_pos)

    def give_wealth(self, amount: int, to: "WealthAgent"):
        """
        Give some units of wealth to another agent.

        Parameters:
            amount (int): The amount of wealth units to be given
            to (WealthAgent): The agent who will receive the wealth
        """
        # Yes, this can go negative. I want to use that to simulate debt.
        self.wealth -= amount
        to.receive_wealth(amount)

    def receive_wealth(self, amount: int):
        """
        Receive some units of wealth.

        Parameters:
             amount (int): The amount of wealth units to be received
        """
        self.wealth += amount

    def step(self):
        """
        Actions taken by the agent each step of the simulation.

        Should be overridden by subclasses.
        """
        self.move()
