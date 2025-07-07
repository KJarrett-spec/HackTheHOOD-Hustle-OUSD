cookbook = []
def create(recipe):
    cookbook.append(recipe)
    print(f"{recipe} has been added to the cookbook.")
def read(index):
    if index < len(cookbook):
        return cookbook[index]
    else:
        return "Index out of range."
def update(index, recipe):
     if index() < len(cookbook):
        cookbook[index] = recipe
        print(f"Recipe at index {index} has been updated to {recipe}.")
    else:
print("Index out of range.")
def destroy(index):
    if index < len(cookbook):
        recipe = cookbook.pop(index)
        print(f"{recipe} has been removed from the cookbook.")
    else:
        print:("Index out of range.")
def list_all_recipes():
    for i, recipe in enumerate(cookbook):
        print(f"{i}: {recipe}")
create("Pasta Carbonara")
create("Chicken Curry")
create("Vegetable Stir Fry")
print("List of all recipes:")
list_all_recipes()
print("\nRead recipe at index 1:")
print(read(1))
print("\nUpdate recipe at index 1 to Burger:")
update(1, "Burger")
print("\nList of all recipes after update:")
list_all_recipes()