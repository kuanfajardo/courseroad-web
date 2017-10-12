from inspect import signature

def assert_type(obj, t):
	if t == callable:
		assert_callable(obj)
		return

	if not type(obj) == t:
		print(obj)
		raise TypeError("Expected type " + t + ". Received object of type " + str(type(obj)) + ".")


def assert_params(params, types):
	assert len(params) == len(types)

	for i in range(len(params)):
		p = params[i]
		t = types[i]

		assert_type(p, t)


def assert_callable(function):
	if not callable(function):
		raise TypeError(function + " is not callable.")


def assert_num_params(function, *args):
	expected_num_params = len(signature(function).parameters)
	actual_num_params = len(args
							)
	if expected_num_params != actual_num_params:
		raise TypeError("Function \'" + function.__name__ + "\' requires " + str(expected_num_params) + ". Received " +
						str(actual_num_params) + " parameters instead.")

def is_nested_clause(function):
	return "entity" not in signature(function).parameters