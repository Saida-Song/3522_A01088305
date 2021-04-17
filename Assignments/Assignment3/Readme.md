# COMP 3522 Assignment 3: Pokedex
This program allows users to query against the [PokeAPI](https://pokeapi.co/). The program will return the 
output in the terminal console, or save the output result to a given text file.  

## Installation
Please have Python3 installed.  
Please have `aiohttp` ,`argparse` and `asyncio` installed by using the following command in the terminal:
`pip install aiohttp`,`pip install argparse`
and `pip install asyncio`.


## Usage
To run the program, users must enter input in the command line. Here is the format:

`python3 pokedex.py {"pokemon" | "ability" | "move"} {--inputfile "filename.txt" | --inputdata "name or id" } 
[--expanded] [--output "outputfile.txt"]`

NOTE: `python3` may not be a recognized command for some. Use `python` instead. 

### Mode
The program will return results for Pokemons, abilities, or moves. Please specify which one in the terminal input using
`"pokemon"`, `"ability"`, or `"move"`.

### Input
The program can query a single input or multiple inputs. Multiple inputs must be in a text file. 
Queries can be made using an ID (integer) or name.

### Expanded
Only the Pokemon queries can be expanded at this moment. Stats, Abilities, and Moves of a Pokemon will be expanded to return
more details if indicated. This parameter is optional. 

### Output
This parameter is optional. If output is not specified, the results will be printed to the console. If an output
file is specified, the results will be saved to that file.

### Results
Here are some sample results for a Pokemon (expanded and not expanded), Ability, and Move:


Non-expanded Pokemon:
```
Name: pikachu
ID: 25
Height: 4
Weight: 60
Types: electric 

Stats:
------
('hp', 35)
('attack', 55)
('defense', 40)
('special-attack', 50)
('special-defense', 50)
('speed', 90)

Abilities:
------
static
lightning-rod

Moves:
------
('mega-punch', 0)
('pay-day', 0)
('thunder-punch', 0)
('slam', 20)
('mega-kick', 0)
('headbutt', 0)
('body-slam', 0)
('take-down', 0)
```

Expanded Pokemon:
```
Name: ivysaur
ID: 2
Height: 10
Weight: 130
Types: grass poison 

Stats:
------
Name: hp
ID: 1
Battle only: False
Move Damage Class: N/A


Name: attack
ID: 2
Battle only: False
Move Damage Class: physical


Abilities:
------
Name: overgrow
ID: 65
Generation: generation-iii
Effect: ['When this Pokémon has 1/3 or less of its HP remaining, its grass-type moves inflict 1.5× as much regular damage.']
Effect(short): ['Strengthens grass moves to inflict 1.5× damage at 1/3 max HP or less.']
Pokemon:
bulbasaur, ivysaur, venusaur, chikorita, bayleef, meganium, treecko, grovyle, sceptile, turtwig, grotle, torterra, snivy, servine, serperior, pansage, simisage, chespin, quilladin, chesnaught, rowlet, dartrix, decidueye, grookey, thwackey, rillaboom, venusaur-gmax, rillaboom-gmax


Name: chlorophyll
ID: 34
Generation: generation-iii
Effect: ["This Pokémon's Speed is doubled during strong sunlight.\n\nThis bonus does not count as a stat modifier."]
Effect(short): ['Doubles Speed during strong sunlight.']
Pokemon:
bulbasaur, ivysaur, venusaur, oddish, gloom, vileplume, bellsprout, weepinbell, victreebel, exeggcute, exeggutor, tangela, bellossom, hoppip, skiploom, jumpluff, sunkern, sunflora, seedot, nuzleaf, shiftry, tropius, cherubi, tangrowth, leafeon, sewaddle, swadloon, leavanny, cottonee, whimsicott, petilil, lilligant, maractus, deerling, sawsbuck, venusaur-gmax


Moves:
------
Name: swords-dance
ID: 14
Generation: generation-i
Accuracy: None
PP: 20
Power: None
Type: normal
Damage class: status
Effect(short): ["Raises the user's Attack by two stages."]


Name: cut
ID: 15
Generation: generation-i
Accuracy: 95
PP: 30
Power: 50
Type: normal
Damage class: physical
Effect(short): ['Inflicts regular damage with no additional effect.']


Name: headbutt
ID: 29
Generation: generation-i
Accuracy: 100
PP: 15
Power: 70
Type: normal
Damage class: physical
Effect(short): ['Has a $effect_chance% chance to make the target flinch.']
```


Ability:
```
Name: stench
ID: 1
Generation: generation-iii
Effect: ["This Pokémon's damaging moves have a 10% chance to make the target flinch with each hit if they do not already cause flinching as a secondary effect.\n\nThis ability does not stack with a held item.\n\nOverworld: The wild encounter rate is halved while this Pokémon is first in the party."]
Effect(short): ['Has a 10% chance of making target Pokémon flinch with each hit.']
Pokemon:
gloom, grimer, muk, stunky, skuntank, trubbish, garbodor, garbodor-gmax
```

Move:
```
Name: karate-chop
ID: 2
Generation: generation-i
Accuracy: 100
PP: 25
Power: 50
Type: fighting
Damage class: physical
Effect(short): ['Has an increased chance for a critical hit.']
```

## Contributors
Authors: 
* Cindy Lu   A01057420   Set 3U
* Saida Song A01088305   Set 3T
