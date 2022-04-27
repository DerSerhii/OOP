from typing import Tuple, Dict


data_stack: Dict[str, str] = {'ser': 'ser',
                              'der': 'der',
                              }


def valid_input(input_text, separator, text_error, text_example) -> Tuple[str, str]:
    errors = 0
    
    while True:
        try:
            first_input, second_input = map(str, input(input_text).split(separator))
        except ValueError:
            errors += 1
            if errors > 1:
                print(f"You're a fool!!! {errors} times the input is wrong! {text_error}")
            else:
                print(f"Enter the correct data, for example: {text_example}")
        else:
            break

    return first_input, second_input


def get_name() -> Tuple[str, str]:
    input_text = "Enter the first and last name separated by a space \n" \
                 "(if your name has more than one word, use an underscore in it): "
    separator = " "
    text_error = "\nEnter the first and last name separated by a space... two words \n"
    text_example = "Elon Musk, Ludwig van_Beethoven ...\n"
    
    fullname = valid_input(input_text, separator, text_error, text_example)
    first_name = fullname[0].replace('_', ' ').title()
    last_name = fullname[1].replace('_', ' ').title()

    print(f"Very nice to meet you, {first_name} {last_name}\n")

    return first_name, last_name


def push() -> None:
    input_text = "Enter the key and value separated by a colon(:) to add it to the dictionary\n" \
                 "(if your key or value consists of more than one word, use an underscore in it): "
    separator = ":"
    text_error = "\nEnter key and value separated by colon... two words by colon\n"
    text_example = "key:value, key1:value2 ...\n"

    item_dict = valid_input(input_text, separator, text_error, text_example)
    
    if item_dict[0] not in data_stack.keys():
        data_stack[item_dict[0]] = item_dict[1]
        print(f"The value '{item_dict[0]}:{data_stack.get(item_dict[0])}' has been added to the dictionary\n")
    else:
        answer = input("Such key already exists. Overwrite? If yes press 'y' else press any key: ")
        if answer in 'yY':
            data_stack[item_dict[0]] = item_dict[1]
            print(f"The value '{item_dict[0]}:{data_stack.get(item_dict[0])}' has been added to the dictionary\n")
        else:
            print(f"The value '{item_dict[0]}:{data_stack.get(item_dict[0])}' was not added to the dictionary\n")


def pop() -> None:
    errors = 0
    key_dict = None

    while True:
        try:
            key_dict = input("Enter dictionary key to remove item: ")
            data_stack.pop(key_dict)
        except KeyError:
            errors += 1
            if errors < 2:
                print("You need to check the correctness of the specified key, try again... ")
            else:
                answer = input(f"There is no key with name '{key_dict}'."
                               f"Will you try again? If yes press 'y' else press any key ")
                if answer in 'yY':
                    errors = 0
                    continue
                else:
                    break
        else:
            # data_stack.pop(key)
            break


def view_dict():
    dict = data_stack.items()
    
    for i, item in enumerate(dict, start=1):
        print(f"\t{i}.\tkey='{item[0]}' value='{item[1]}'")


FUNC_CONTAINER = {
    "push": push,
    "pop": pop,
    "view": view_dict,
}


if __name__ == "__main__":
    name = get_name()
    action = ""

    while True:
        try:
            for key in FUNC_CONTAINER:
                action += str(key) + ', '
            
            choice = input(f"{name[0]}, choose an action ({action.rstrip(', ')}): ")
            FUNC_CONTAINER[choice.lower()]()
        except KeyError:
            print(f"{action.rstrip(', ').upper()} - only!!!!")
            action = ""
            continue
        except KeyboardInterrupt:
            print("\n\nGoodbye!! Come back to us again")
            break
