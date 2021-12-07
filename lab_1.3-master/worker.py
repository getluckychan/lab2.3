from main import Money


def main_func():
    first_value = Money()
    first_value.read()
    second_value = Money()
    second_value.read()
    first_value.to_string()
    second_value.to_string()
    print(first_value.to_string() - second_value.to_string())
    print(first_value.to_string() * 1.5)
    first_value.compere(second_value.to_string())
    first_value.increment()
    first_value.decrement()

main_func()