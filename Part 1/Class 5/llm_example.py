import random
import time

def generate_text(prompt, temperature):
    print(f"--- Starting AI Generation ---")
    print(f"Prompt: '{prompt}'")
    print(f"Temperature set to: {temperature}\n")

    # STEP 1: Tokenization
    # We chop the user's sentence into a list of words (tokens).
    tokens = prompt.split()
    print(f"[Step 1] Tokenized prompt: {tokens}\n")

    # STEP 5: The Autoregressive Loop
    # The model generates one word at a time, over and over, until it stops.
    while True:
        
        # STEP 2: Attention
        # The model looks at the entire sequence generated so far to understand context.
        current_context = " ".join(tokens)
        print(f"[Step 2] Attention reading context: '{current_context}'")

        # STEP 3: The Great Prediction Game (Probabilities)
        # Based on the last word, the model calculates what should come next.
        # (We are using mock probabilities here to represent the neural network's math).
        if tokens[-1] == "the":
            probabilities = {"mat": 0.82, "couch": 0.12, "Roomba": 0.05, "moon": 0.01}
        elif tokens[-1] == "Roomba":
            probabilities = {"and": 0.60, "rode": 0.30, "<STOP>": 0.10}
        elif tokens[-1] == "mat":
            probabilities = {"and": 0.50, "softly": 0.20, "<STOP>": 0.30}
        else:
            # If it doesn't know what to do next, it decides to end the sentence.
            probabilities = {"<STOP>": 1.0} 

        print(f"[Step 3] Calculated probabilities: {probabilities}")

        # STEP 4: Rolling the Dice (Temperature)
        # Temperature decides if we play it safe or get creative.
        if temperature < 0.5:
            # Low temperature = strict. We just pick the mathematically highest number.
            next_token = max(probabilities, key=probabilities.get)
            print(f"[Step 4] Low temperature picked the safest bet: '{next_token}'")
        else:
            # High temperature = creative. We roll a weighted dice.
            # (In this simple code, we'll just randomly pick from the available options).
            next_token = random.choice(list(probabilities.keys()))
            print(f"[Step 4] High temperature rolled the dice and got: '{next_token}'")

        # STEP 6: Knowing When to Stop
        # If the dice lands on the invisible <STOP> token, we break the loop!
        if next_token == "<STOP>":
            print(f"[Step 6] Generated <STOP> token. Putting the pen down.")
            break

        # If it's not a stop token, glue it to our list and loop again!
        tokens.append(next_token)
        print(f"[Step 5] Appended '{next_token}'. Looping again...\n")
        
        # A small pause so students can watch the loop happen in real-time
        time.sleep(1.5) 

    # The Final Result
    final_sentence = " ".join(tokens)
    print(f"\n--- Final Output: '{final_sentence}' ---")


# --- RUNNING THE CODE ---
# Let's test it with a creative (high) temperature!
generate_text(prompt="The cat sat on the", temperature=0.9)
