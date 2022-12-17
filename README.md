# Workshop "Introduction to Programming with Python" - Take Home Exercise 
Writ an algorithm, that will choose a random number between `1` and `100`, and then allow the user guess the number. With every guess, the algorithm will inform the user whether its chosen number is smaller or greater, until the user guesses right.


**Example Output:**
```python
>>> Please enter a guess: 50
>>> Incorrect, my number is smaller!

>>> Please enter a guess: 25
>>> Incorrect, my number is greater!

>>> Please enter a guess: 33
>>> Congratulations, you found my number!
```

**NOTE**
In Python, to select a random number between `1` and `100`, you can use the following code:
```Python
import random 

random_number = random.randint(1, 100)
```