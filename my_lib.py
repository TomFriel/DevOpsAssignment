"""Module for my_lib functionality."""

import logging

from game_feature import GameFeature

logger = logging.getLogger(__name__)

def do_something():
    """Perform a sample operation using GameFeature."""
    # Make logger relevant to project
    game = GameFeature()
    score = game.compute_score(" john ")
    logger.info("Computed score: %s", score)