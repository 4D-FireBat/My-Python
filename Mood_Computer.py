#Mood Computer
#Demonstartes the elif clause

import random

print("I sense your energy. Your true emotions are coming across my screen.")
print("You are...")

mood = random.randint(1, 3)

if mood == 1:
    # happy
    print( \
    """

        -----------
        |         |
        | 0     0 |
        |   <     |
        |         |
        | .     . |
        |  `...`  |
        |         |
        -----------

                    """)

elif mood ==2:
    #Neutral
    print( \
    """

        -----------
        |         |
        | 0     0 |
        |   <     |
        |         |
        |         |
        | ------- |
        |         |
        -----------

                    """)

elif mood ==3:
    #sad
    print( \
    """

        -----------
        |         |
        | 0     0 |
        |   <     |
        |         |
        |         |
        |   .'.   |
        |  '   '  |
        -----------

                    """)

else:
    print("Illegal mood value! (You must be in a really bad mood).")
    print("...today.")

input("\n\nPress the enter key to exit.")
