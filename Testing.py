def test(func, input, expectedOutput):
  output = func(*input)
  if output == expectedOutput:
    print(f"Passing on input: {input}")
  else:
    print(f"Failed on input: {input}")
    print(f"Expected: {expectedOutput}, got: {output}")