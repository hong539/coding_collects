import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()