import random
import time

def slowprint(text, delay=2):
    """Function for slow-printing to create atmosphere"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay / 100)
    print()  # Newline at the end

def introduction():
    """The game's introduction"""
    slowprint("Welcome to your Soylent-Infused Adventure in Ohio... Albeit, you're just a number now.")
    slowprint("You've been living in a world where 'eating the bugs' is considered gourmet, and 'owning nothing' is a lifestyle choice.")
    slowprint("Corporate overlords love you. You love the government. Or at least, you're told to.")
    slowprint("It's time to make a decision... or so you've been told.")
    input("Press Enter to continue your journey...")

def encounter_corp_agent():
    """Encounter with a corporate agent"""
    slowprint("You stumble into a sleek corporate building, the walls shine with pristine white. A figure stands in front of you. It's a Corp Agent.")
    slowprint("'Welcome to Still Prime. How can I help you today?'")
    slowprint("1. Accept Soylent ration.")
    slowprint("2. Decline Soylent and ask about 'Still Water'.")
    choice = input("What will you do? (1 or 2): ")

    if choice == '1':
        slowprint("'Excellent. Here is your Soylent. It's protein-packed... and peer-reviewed.'")
        slowprint("You drink it. It's strangely satisfying. Your body feels the slowburn.")
        slowprint("You feel closer to 'being happy.'")
    elif choice == '2':
        slowprint("'Ah, you prefer 'Still Water,' don't you? Well, that's a choice. Howeverbeit, we have something better. You VILL experience the future, or whatever.'")
        slowprint("The Corp Agent hands you a strange, glowing bottle. You take it reluctantly, feeling oddly compelled to drink it.")
        slowprint("You feel 'genetically superior.' The system has spoken.")

def exploration():
    """Exploration phase where user makes decisions"""
    slowprint("You're now free to explore this post-4th industrial revolution world. There’s a lot to take in.")
    slowprint("You notice a 'Hyperkorea' banner in the distance. You also hear some 808 phonk beats blasting from a nearby alley.")
    slowprint("1. Head to the Hyperkorea district.")
    slowprint("2. Investigate the 808 Phonk crashout alley.")
    slowprint("3. Go for a walk and think about your life choices.")
    choice = input("What will you do? (1, 2, or 3): ")

    if choice == '1':
        slowprint("You arrive in Hyperkorea. The neon lights flicker, and you're overwhelmed with 'sigma' energy. Everyone's rizzing each other.")
        slowprint("There's an odd sense of 'belonging,' but also an undercurrent of something more sinister.")
        slowprint("'Remember,' a voice calls, 'it's all part of the Soyence.'")
    elif choice == '2':
        slowprint("You walk into the alley and immediately feel the bass. It's like the world itself is shaking to the 808 phonk rhythm.")
        slowprint("Suddenly, a figure steps out. It's Baby Gronk, the mascot of post-society, ready to challenge you.")
        slowprint("'Wanna battle? Let’s see who’s got more rizz,' Baby Gronk says.")
        slowprint("You have to decide: engage in a phonk battle or try to leave this strange place.")
    elif choice == '3':
        slowprint("You sit on a bench, wondering about 'still prime' and 'balkan rage.' You feel oddly calm in a world that’s anything but.")
        slowprint("You start contemplating the meaning of 'owning nothing and being happy.' Is it really possible?")
        slowprint("An agent approaches you with a 'Goyslop' container, reminding you to be 'evidence-based.'")

def random_event():
    """Random event that might happen during the game"""
    events = [
        "WARNING: may randomly start talking about Fortnite being bad and Minecraft being good.",
        "You feel the urge to engage in Baby Monkey Torture, but you suppress the thought.",
        "A small doggo trots by, looking suspiciously like a chonker. Is it following you?"
    ]
    slowprint(random.choice(events))

def game():
    """Main game loop"""
    introduction()
    encounter_corp_agent()
    exploration()
    random_event()
    slowprint("Erm... well that just happened!")
    slowprint("You’re now deep within this strange world, but the choices are yours.")
    slowprint("Remember: you VILL have to make decisions. Or whatever.")
    
# Start the game
game()
