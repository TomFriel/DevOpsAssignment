# mylib.py
import logging

from main import GameFeature

logger = logging.getLogger(__name__)

def do_something():
    #Make logger relevant to project
    game = GameFeature()
    score = game.compute_score(" john ")
    logger.info("Computed score: %s", score)https://github.com/TomFriel/DevOpsAssignment/compare/Autodoc-and-class-split?expand=1