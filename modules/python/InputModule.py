from utils.python import TypeUtils

def custom_input(input_type: type, input_title: str):
    while True:
        input_ = input(input_title)

        if TypeUtils.get_true_type(type_=input_type, obj=input_) == input_type:
            break

    return input_type(input_)