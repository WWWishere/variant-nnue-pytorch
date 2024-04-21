RANKS = 8
FILES = 8
SQUARES = RANKS * FILES
KING_SQUARES = 64
PIECE_TYPES = 14
PIECES = 2 * PIECE_TYPES
USE_POCKETS = False
POCKETS = 2 * FILES if USE_POCKETS else 0

PIECE_VALUES = {
  1: 126,
  2: 781,
  3: 825,
  4: 1276,
  5: 2538,
  6: 2050,
  7: 1250,
  8: 770,
  9: 1150,
  10: 1300,
  11: 800,
  12: 950,
  13: 2200,
}