adjective = input("Input an adjective. ")
adjective2 = input("Input a different adjective. ")
noun = input("Input a noun. ")
noun2 = input("Input a different noun. ")
verb = input("Input a verb ")
verb2 = input("Input a different verb but in the past tense ")
sentence = f"The {adjective} {noun2}, belonged to {noun}. Everybody knows {noun} is {adjective2}. Did I ever tell you about the time a chimpanzee {verb2} ? The Elephant's first reaction was to {verb}."
print(sentence)
funny_or_weird = input("Do you think the sentence was funny or weird? Type 'A' or 'B': ").lower()
if funny_or_weird == "a":
  print("You have a peculiar sense of humour!")
else:
    print("Gosh, lighten up. It was supposed to be funny!")
