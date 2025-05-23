cipher_found = False

def intro():
    global cipher_found
    cipher_found = False
    print("Welcome, traveler, to the Forgotten Cipher.")
    print("You wake up on cold stone, your heart pounding in the silence.")
    print("A rusty door is on your left, and a set of stone steps go down into the dark on your right.")

    
    print("\nWhat do you do?")
    print("1. Open the door")
    print("2. Descend the stairs")
    
    choice = input("> ").strip()
    
    if choice == "1":
        door_scene()
    elif choice == "2":
        stairs_scene()
    else:
        print("\nYou hesitate. The silence grows heavy. Time is slipping past you.")
        ending()

def door_scene():
    print("\nThe door creaks open… and a cold wind hits your face. You step into the dark.")
    print("Ahead is a cold hall covered with ice, filled with statues — knights, scholars, and one empty spot.")
    print("A old cloth hangs ahead, moving gently, and to your right, a broken mirror makes a soft sound.")


    print("\nWhat do you do?")
    print("1. Examine the cloth")
    print("2. Approach the mirror")

    choice = input("> ")

    if choice == "1":
        tapestry_scene()
    elif choice == "2":
        mirror_scene()
    else:
        print("\nYou wait. The statues seem... closer than before.")
        ending()

def tapestry_scene():
    print("\nYou lift the cloth — behind it, a message carved in an old language:")
    print("'Who forgets their name is free from the curse.'")
    print("A strange feeling pulls at your mind. Your own name starts to fade.")


    print("\nWhat do you do?")
    print("1. Speak your name aloud")
    print("2. Remain silent")

    choice = input("> ")

    if choice == "1":
        print("\nYou speak it. The air stills. One statue turns its head toward you.")
        print("You remember... something you were never meant to.")
    elif choice == "2":
        print("\nYou say nothing. The words vanish. The curse remains asleep.")
    else:
        print("\nYour silence speaks louder than words. The floor beneath you cracks slightly.")
    
    ending()

def mirror_scene():
    print("\nYou stand before the mirror. It shows your reflection — but older, with eyes full of regret.")
    print("Your reflection speaks: 'Don’t go further. It doesn’t end where you think.'")

    print("\nWhat do you do?")
    print("1. Touch the mirror")
    print("2. Turn away")

    choice = input("> ")

    if choice == "1":
        print("\nYour hand passes through. Cold. You’re pulled in.")
        print("You now stand *inside* the mirror, watching yourself walk away.")
    elif choice == "2":
        print("\nYou turn. But something inside the mirror follows. Always.")
    else:
        print("\nThe mirror fractures slightly. You see a thousand versions of yourself screaming.")
    
    ending()

def stairs_scene():
    print("\nYou descend the stairs. Each step feeling heavy. Something ancient watching below...")
    print("You reach a cavern. The air is heavy with dust and secrets.")
    print("In the center lies a pedestal with a glowing orb. To the left, a narrow tunnel disappears into darkness.")

    print("\nWhat do you do?")
    print("1. Approach the orb")
    print("2. Enter the tunnel")

    choice = input("> ")

    if choice == "1":
        orb_scene()
    elif choice == "2":
        tunnel_scene()
    else:
        print("\nYou stand frozen. A distant howl answers your silence.")
        ending()

def orb_scene():
    global cipher_found
    print("\nAs you near the orb, symbols flicker across its surface. It's pulsing... alive.")
    print("A voice — or is it a thought? — whispers: 'Speak the cipher or be unmade.'")
    print("But do you remember it...?")

    print("\nWhat do you do?")
    print("1. Touch the orb")
    print("2. Step back")

    choice = input("> ")

    if choice == "1":
        if cipher_found:
            print("\nYour hand meets the orb. You whisper the cipher: ΔX = ΣL - F.")
            print("The orb glows brighter, then vanishes. A warmth spreads through your chest.")
            print("You have restored the missing piece. The curse is undone. The cipher... is whole.")
            print("\n✨ TRUE ENDING UNLOCKED ✨")
        else:
            print("\nYour hand meets the surface. Light floods your mind. You scream.")
            print("You needed something — a piece you missed. The cipher rejects you.")
            print("When you open your eyes, the chamber is gone. You're in a forgotten memory... that isn’t yours.")
    elif choice == "2":
        print("\nYou step back. The orb dims. It is waiting — for another time.")
    else:
        print("\nThe orb pulses impatiently. Time warps... and you collapse, senseless.")
    
    ending()


def tunnel_scene():
    global cipher_found
    print("\nYou enter the tunnel. Walls close in. It smells of damp earth and old bones.")
    print("Something scuttles ahead — too fast to see. Your breath catches.")
    print("You find a cracked journal half-buried in the dust.")

    print("\nWhat do you do?")
    print("1. Read the journal")
    print("2. Ignore it and press on")

    choice = input("> ")

    if choice == "1":
        print("\nYou flip through brittle pages. A cipher is repeated: ΔX = ΣL - F.")
        print("There's a note scribbled beside it: 'Balance what was taken. Find what remains. Speak it at the orb.'")
        cipher_found = True
    elif choice == "2":
        print("\nYou press forward. But the path is watching. And you missed what it wanted to tell you.")
    else:
        print("\nYou freeze. The darkness does not.")
    
    ending()


def ending():
    print("\nEverything begins to blur. The air warps, time collapses.")
    print("Whether orb or tunnel, mirror or name — all led you here.")
    print("You stand in a white room. A figure speaks from behind a veil:")
    print("‘You’ve seen fragments, but the cipher remains broken.’")
    print("‘Next time, perhaps, you’ll find the missing piece.’")
    print("\n\nTHE END. Or the prologue to your next cipher...")


# Start the game
intro()
