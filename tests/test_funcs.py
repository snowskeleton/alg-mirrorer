from funcs import invert

assert invert("F' R U2 R' U2 R' F2 R U R U' R' F'") == "F L' U2 L U2 L F2 L' U' L' U L F", "with spaces"

assert invert("F'RU2R'U2R'F2RURU'R'F'") == "F L' U2 L U2 L F2 L' U' L' U L F", "without spaces"

assert invert("F 'RU 2R'U 2 R'F 2R UR U'R'F'") == "F L' U2 L U2 L F2 L' U' L' U L F", "mixed spacing"

assert invert("()  ") == "", "input sanitization"

assert invert("F'") == "F", "single-length prime alg"

assert invert("F") != "F", "single-length non-prime alg"


from funcs import clean

assert clean("asdf\r1234'\n()\"", "RLFBUDrlfbudm'23") == "df23'", "character removal"
