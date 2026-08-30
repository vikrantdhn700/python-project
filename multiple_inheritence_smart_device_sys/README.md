# Smart Device System Using Multiple Inheritance

This project demonstrates Python multiple inheritance by combining camera,
music player, and GPS features in a single `SmartPhone` class.

## Classes and Methods

### Camera

- `take_photo()`
- `record_video()`

### MusicPlayer

- `play_music()`
- `stop_music()`

### GPS

- `current_location()`
- `navigate()`

### SmartPhone

`SmartPhone` inherits from all three feature classes:

```python
class SmartPhone(Camera, MusicPlayer, GPS):
    ...
```

It also stores these properties:

- `brand`
- `model`
- `price`
- `storage`

The program creates three smartphone objects and calls all inherited methods on
each one.

## How Multiple Inheritance Works

Multiple inheritance allows one child class to inherit attributes and methods
from more than one parent class. Here, a `SmartPhone` object can call
`take_photo()` from `Camera`, `play_music()` from `MusicPlayer`, and `navigate()`
from `GPS` without redefining those methods in `SmartPhone`.

When Python looks for a method, it follows the Method Resolution Order (MRO).
For this class, the important search order is:

```text
SmartPhone -> Camera -> MusicPlayer -> GPS -> object
```

This order matters if multiple parent classes define a method with the same
name. Python uses the first matching implementation in the MRO. The parent
classes in this project have distinct method names, so no conflict occurs.

## Run the Program

```bash
python main.py
```

The output displays each smartphone's details and demonstrates its inherited
camera, music, and navigation functionality.
