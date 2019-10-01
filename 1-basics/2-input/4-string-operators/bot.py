print("How many respawns do you require?")
lives = int(input())
print("And your fitness quota?")
energy = int(input())
print("Force field protection variable?")
shield = int(input())
print("""Nice stats bro! Check it.

    Health: """ + ("♥" * lives) + """
    Energy: """ + ("#" * energy) + """
    Shield: """ + ("▲" * shield))