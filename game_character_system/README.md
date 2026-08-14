# Game Character System

A small Python project that models game characters and a scripted battle using object-oriented programming. It demonstrates inheritance, method overriding, object interaction, and shared base-class behavior through three playable character types: `Warrior`, `Wizard`, and `Archer`.

## Features

- Defines common character attributes such as name, health, and level.
- Provides specialized warrior, wizard, and archer classes.
- Gives each character type its own attack method.
- Applies damage to another character and prevents health from falling below zero.
- Displays character statistics before and after a scripted battle.
- Requires no third-party dependencies.

## Project Structure

```text
game_character_system/
|-- game_character.py  # Base character class and damage handling
|-- warrior.py         # Warrior class and sword attack
|-- wizard.py          # Wizard class and magic attack
|-- archer.py          # Archer class and bow attack
|-- main.py            # Scripted battle demonstration
`-- README.md
```

## Requirements

- Python 3.8 or later

No package installation is required because the project uses only standard Python functionality.

## Running the Project

1. Open a terminal in the project directory:

   ```powershell
   cd D:\julysuper30\game_character_system
   ```

2. Run the battle simulation:

   ```powershell
   python main.py
   ```

The program prints the initial statistics for all characters, performs one attack by each character, and then prints their updated health.

## How It Works

### Base class: `GameCharacter`

Every character inherits these attributes from `GameCharacter`:

- `name`
- `health`
- `level`

The base class also supplies:

- `take_damage(damage)`: subtracts damage from health and clamps the result to zero.
- `display_info()`: returns a formatted summary of the character's state.

### Character classes

Each subclass adds a `damage` attribute and a specialized attack method:

| Class | Attack method | Description |
|---|---|---|
| `Warrior` | `sword_attack(target)` | Deals sword damage to a target. |
| `Wizard` | `magic_attack(target)` | Deals spell damage to a target. |
| `Archer` | `bow_attack(target)` | Deals bow damage to a target. |

Each class also overrides `display_info()` to include its damage value while reusing the base character information.

## Scripted Battle

`main.py` creates the following characters:

| Character | Class | Health | Level | Damage |
|---|---|---:|---:|---:|
| Dr. Strange | Wizard | 120 | 5 | 20 |
| Thor | Warrior | 150 | 4 | 15 |
| Hawkeye | Archer | 100 | 5 | 18 |

The battle proceeds in this order:

1. Dr. Strange attacks Thor for 20 damage.
2. Thor attacks Hawkeye for 15 damage.
3. Hawkeye attacks Dr. Strange for 18 damage.

Their resulting health values are 102 for Dr. Strange, 130 for Thor, and 85 for Hawkeye.

## Example Output

```text
==================== Character Info ====================
Name: Dr. Strange, Health: 120, Level: 5, Damage: 20
Name: Thor, Health: 150, Level: 4, Damage: 15
Name: Hawkeye, Health: 100, Level: 5, Damage: 18

==================== Battle Start ====================
Thor has 20 damage and now has 130 health.
Dr. Strange casts a spell with 20 damage!
Hawkeye has 15 damage and now has 85 health.
Thor attacks with 15 damage!
Dr. Strange has 18 damage and now has 102 health.
Hawkeye attacks with 18 damage!
```

## Using the Classes

The classes can also be imported into another Python module:

```python
from warrior import Warrior
from wizard import Wizard

warrior = Warrior("Knight", 100, 1, 12)
wizard = Wizard("Mage", 80, 1, 20)

warrior.sword_attack(wizard)
print(wizard.display_info())
```

## Current Limitations

- The battle sequence and character data are hard-coded in `main.py`.
- There is no interactive character selection or turn system.
- Characters can still attack after their health reaches zero.
- Damage values are not validated, so negative damage would increase health.
- The project does not include inventory, defense, abilities, experience, or persistence.
- There are currently no automated tests.

## Possible Enhancements

- Add input validation for health, level, and damage.
- Introduce defense, critical hits, healing, and special abilities.
- Prevent defeated characters from attacking.
- Build an interactive, turn-based battle loop.
- Add character creation and team selection.
- Store and restore character progress.
- Add unit tests for attacks, damage handling, and health limits.

## License

No license has been specified for this project.
