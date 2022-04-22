from dataclasses import replace


proseString = """
Hi Mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place int he world to build a career around them. I'll need to start small-- At First, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME
"""

replacements = [
    ["An occupation", "OCCUPATION"],
    ["A country", "COUNTRY"],
    ["A plural noun", "PLURAL_NOUN"],
    ["A verb, like 'run', 'eat', or 'think'", "VERB"],
    ["An adjective, like 'friendly', 'long', or 'warm'", "ADJECTIVE"],
    # ["A title that someone might have in an organization, like 'manager', 'captian', or 'trainer'", "TITLE"],
    ["A personal item", "PERSONAL_ITEM"],
    ["A holiday", "HOLIDAY"]
]

# newProseString = proseString
# userInput = input("Please provide a holiday")
# newProseString = newProseString.replace("HOLIDAY", userInput)


def prompt_replace(array):
    newProseString = proseString
    for index in range(0, len(array)):
        prompt = "Please provide "
        placeholder = array[index][1]
        userInput = input(prompt + array[index][0] + ": ")
        newProseString = newProseString.replace(placeholder, userInput)
    print(newProseString)


# for index in range(0, len(replacements)):
#     prompt = "Please provide "
#     placeholder = replacements[index][1]
#     print("placeholder ", placeholder)
#     userInput = input(prompt + replacements[index][0] + ": ")
#     newProseString = newProseString.replace(placeholder, userInput)

prompt_replace(replacements)
