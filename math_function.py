# this is function for square numbers

@app.route('/<int:num>')
def square_number(num):
    return {f'Square number of {num}': num ** 2}
