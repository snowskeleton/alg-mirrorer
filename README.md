# Absstract

Mir is a simple python program reverse the symmetry of a rubik's cube algorithm (e.g., right-handed to left-handed).

# Install

## macOS

* Download package

* * ```git clone https://github.com/snowskeleton/alg-mirrorer.git .```

* * ```cd alg-mirror```

* Set permissoins and install

* * ```chmod +x install.sh```

* * ```./install.sh```

* Aftet it's installed, run it from the terminal like so: ```mir "<ALGORITHM>"```. (Note that the algoritm is double-quoted, not single-quoted.)p

## Other operating systems:
* Simply clone this repo and run the ```main.py``` script directly from your command line, and pass in arguments as noted elsewhere.

**Examples**

* * ```$ mir "R U R' U'"```

* * ```>> L' U' L U```

* * ```$ mir "l' U' L U' L F' L' F L' U2 l"```

* * ```>> r U R' U R' F R F' R U2 r'```

* mir supports input redirection
* * ```$ mir "F R U R' U' R U R' U' F'" > output.txt```

* * ```$ cat output.txt```

* * ```>> F' L' U' L U L' U' L U F```

* You can even go the other way

* * ```$ echo "R' U' F U R U' R' F' R`" | mir```

* * ```>> L U F' U' L' U L F L'```

* Mir can operating on files containing a list of algorithms, treating each newline as the start of an algoritm.

* * ```$ cat input.txt```
* * ```>> R' U' F U R U' R' F' R```
* * ```>> l' U' l L' U' L U l' U l```
* * ```>> R' F R U R U' R2 F' R2 U' R' U R U R'```
* * ```>> F U R U' R' U R U' R' F'```
* * ```>> r U R' U' M2 U R U' R' U' M'```
###
* * ```$ cat input.txt | mir```
* * ```>> L U F' U' L' U L F L'```
* * ```>> r U r' R U R' U' r U' r'```
* * ```>> L F' L' U' L' U L2 F L2 U L U' L' U' L```
* * ```>> F' U' L' U L U' L' U L F```
* * ```>> l' U' L U M2 U' L' U L U M```
