
cookbook =[]

def create(recipe):
    cookbook.append(recipe)
    print(f"The recipe {recipe} has been added")

#step 3
def read(index):
    if index < len(cookbook):
        return cookbook[index]
    else:
        return "Please pick an index within the range"

def update(index, recipe):
    if index<len(cookbook):
        cookbook[index] = recipe
        print(cookbook[index])
    else:
        print("Please pick an index within the range")

def destroy(index):
    if index < len(cookbook):
        removed = cookbook.pop(index)
        print(f"The element '{removed}' has been deleted")
    else:
        print("Please pick an index within the range")

def list_all_recipes():
    if cookbook:
        print("Here are all the recipes in the cookbook:")
        for index, recipe in enumerate(cookbook):
            print(f"{index}: {recipe}")
    else:
        print("The cookbook is currently empty.")

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = int(input("Enter the index of the recipe to read: "))
            print(read(index))
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
