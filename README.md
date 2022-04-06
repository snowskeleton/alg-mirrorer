**Absstract**

Mir is a simple python program reverse the symmetry of a rubik's cube algorithm (e.g., right-handed to left-handed).


**Install** (macOS)

* Download package

* * ```git clone https://github.com/snowskeleton/alg-mirrorer.git .```

* * ```cd alg-mirror```

* Set permissoins and install

* *```chmod +x install.sh```

* *```./install.sh```

* Aftet it's installed, run it from the terminal like so: ```mir "<ALGORITHM>"```. (Note that the algoritm is double-quoted, not single-quoted.)

**Examples**

* *```$ mir "R U R' U'"```

* *```>> L' U' L U```

* *```$ mir "l' U' L U' L F' L' F L' U2 l"```

* *```>> r U R' U R' F R F' R U2 r'```

* mir supports input redirection
* *```$ mir "F R U R' U' R U R' U' F'" > output.txt```

* *```$ cat output.txt```

* *```>> F' L' U' L U L' U' L U F```

* You can even go the other way

* *```$ cat input.txt```

* *```>> "R' U' F U R U' R' F' R"```

* *```$ cat input.txt | mir```

* *```>> L U F' U' L' U L F L'```
