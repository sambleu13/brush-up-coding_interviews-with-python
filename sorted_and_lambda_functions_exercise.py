animals = [{'type': 'penguin', 'name': 'Stephanie', 'age': 8},
            {'type': 'elephant', 'name': 'Devon', 'age': 3},
            {'type': 'puma', 'name': 'Moe', 'age': 5}
            ]

print(sorted(animals, key=lambda animal: animal['age']))

print(sorted(animals, key=lambda animal: len(animal['type']),reverse=True))
