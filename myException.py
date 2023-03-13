# class DonationError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self, message)
#
#     def __str__(self):
#         return f"This {self.message} is not a proper donation."
# try:
#     try:
#         donation = int(input("Please enter your amount: "))
#     except ValueError as v:
#         raise DonationError(v)
# except DonationError as de:
#     print(de)

while True:
    match input("Enter (), {}, or [] and I will tell you what they are: "):
        case '[]':
            print("A list is a collection of ordered data: [one, two, three...] and it is mutable.")
        case '()':
            print("A tuple is an ordered collection of data: (one, two, three...) and it is immutable.")
        case '{}':
            print('''A dictionary is an unordered collection of data that stores data in key-value pairs:
    {key1: meaning_one, key2: meaning_two}, Dictionaries are mutable and keys do not allow duplicates. Sets can also be 
    written in curly brackets: {1,2,3,4,5,"hello") A set is an unordered collection. Sets are mutable and have no duplicate elements.''')
        case _:
            print("Invalid Entry. Start over and try again by entering (), or [], or {}...")
            break
