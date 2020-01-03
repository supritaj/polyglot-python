from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/twoSidedPrime/<number>', methods=['GET'])
def home(number):
    if not isinstance(number, int):
        return jsonify(
            input=number,
            error="input is not integer"
        )
    return jsonify(
        input=number,
        isTwoSidedPrime=check_two_sided_prime(int(number))
    )


def left_prime(number):
    temp = number
    length = len(str(number))
    while (length > 1):
        if not is_prime(temp):
            return False
        temp = int(str(temp)[1:])
        length = len(str(temp))
    return True


def right_rime(number):
    while number > 0:
        if not is_prime(number):
            return False
        number = int(number / 10)
    return True


def check_two_sided_prime(number):
    if not is_prime(number):
        return False
    if not left_prime(number):
        return False
    if not right_rime(number):
        return False
    return True


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


app.run()
