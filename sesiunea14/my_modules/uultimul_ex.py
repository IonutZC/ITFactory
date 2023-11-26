
def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

# Loop through the letters A to Z


for letter in range(ord("A"), ord("Z") + 1):
    current_letter = chr(letter)
    ordinal_number = ordinal(letter - ord("A") + 1)

    # Generate the content for the file
    content = f"My name is letter {current_letter}.\nI am the {ordinal_number} letter of the alphabet."

    # Create and write to the file
    file_name = f"{current_letter}.txt"
    with open(file_name, "w") as file:
        file.write(content)

    print(f"File '{file_name}' has been created.")
