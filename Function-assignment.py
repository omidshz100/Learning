def namingSystem(firstName, lastName, age):
    """
    This function takes a first name, last name, and age as input and returns a  dictonary
    """
    # Create a dictionary to store the person's information
    person_info = {
        "first_name": firstName,
        "last_name": lastName,
        "age": age
    }
    return person_info
# Example usage
person = namingSystem("John", "Doe", 30)
print(person)
# Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 30}
# The function takes three arguments: firstName, lastName, and age.