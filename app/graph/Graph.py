import utils

from inspect import *
class _Constraint:
	"""
	A constraint is an abstraction of a requirement on an object (Entity).

	It has a satisfaction clause, representing the conditions on the entity that cause the constraint to be satisfied.
	Whenever the the constraint is broken or satisfied, a response is triggered.

	Must be linked to an entity to be of any use.
	"""

	def __init__(self, identifier, clause, callback=None):
		"""
		Constraint constructor

		:param str identifier: constraint identifier type
		:param clause: function that takes an Entity as a parameter and returns a Boolean True if the constraint
				is satisfied, False otherwise
		:param callback: function that gets called every time the constraint CHANGES state
				(i.e. broken -> satisfied, satisfied -> broken)

		:return: None
		"""

		utils.assert_params([identifier, clause, callback], [str, callable, callable])

		self._value_changed = callback
		self.identifier = identifier
		self._satisfied = False
		self.clause = clause
		self.entity = None

	@property
	def satisfied(self):
		return self._satisfied

	@satisfied.setter
	def satisfied(self, value):
		utils.assert_type(value, bool)

		if self._satisfied != value:
			self._satisfied = value

			if self._value_changed is not None:
				self._value_changed(self._satisfied)

	def satisfy(self):
		"""
		Set the constraint to "satisfied" calls callback function if previously broken.

		:return: None
		"""

		self.satisfied = True

	def fail(self):
		"""
		Set the constraint to "broken" calls callback function if previously satisfied.
		:return None
		"""

		self.satisfied = False

	def check(self):
		"""
		Checks the constraint for satisfaction (and sets the constraint to that value).
			Requires constraint to have been linked to an entity.

		:return: None
		:raises: TypeError if constraint has not been linked to en entity.
		"""

		if self.entity is None:
			raise Warning("Constraint cannot be checked if it has not been linked to an Entity")

		self.satisfied = self.clause(self.entity)

	def link_to(self, entity):
		"""
		Link the constraint to an Entity. Required in order to check the constraint. If already linked to an entity,
			does nothing.

		:param _Entity entity: entity to link constraint to
		:return: None
		"""

		utils.assert_type(entity, _Entity)

		if self.entity is None:
			self.entity = entity

	def unlink(self):
		self.entity.remove_constraint(self)
		self.entity = None


class _Entity:
	"""
	An entity is an abstraction of an object that
		(1) has pre-determined, type-specific properties
		(2) can be constrained. These constraints are on the properties mentioned above.

	Can be modified/observed via attributes ==> entity.name = "Bob" ; n = entity.name
	Can be modified via bracket notation ==> entity["name"] = "Bob" ; n = entity["name"]

	However, can only access/set attributes that are defined in the attribute_map that the Entity is initialized with.
	Additionally, attributes "property
	"""

	def __init__(self, identifier, attribute_map):
		"""
		Entity constructor creates an entity of type type with no constraints and no properties.

		:param str identifier: identifier of entity i.e. "subject", "person", "dog"
		:param dict attribute_map: dict<str, obj> map of entity properties (i.e. "name", "age") to their expected type
									(i.e. str, Map)

		:return: _Entity object with no constraints

		self.constraints: Array<_Constraint> - contains all Constraints linked to Entity
		"""

		utils.assert_params([identifier, attribute_map], [str, dict])

		object.__setattr__(self, "identifier", identifier)
		object.__setattr__(self, "attribute_map", attribute_map)
		object.__setattr__(self, "constraints", [])

	def __getitem__(self, item):
		utils.assert_type(item, str)
		return self.__getattribute__(item)

	def __setitem__(self, key, value):
		utils.assert_type(key, str)
		self.__setattr__(key, value)

	def __setattr__(self, key, value):
		protected = ["constraints", "identifier", "attribute_map"]
		if key in protected:
			raise AttributeError("Cannot modify " + key + " attribute of an Entity object")

		if key not in self.attribute_map:
			raise AttributeError("Entity of type " + self.identifier + " does not have attribute \"" + key + "\"")

		expected_type = self.attribute_map[key]

		if type(value) != expected_type:
			raise TypeError(
				"Attribute \"" + key + "\" is of type " + str(expected_type) + ", not of type" + str(type(value)) + ".")

		object.__setattr__(self, key, value)

	def __getattr__(self, item):
		utils.assert_type(item, str)

		if item not in self.attribute_map:
			raise AttributeError("Entity of type \"" + self.identifier + "\" does not have attribute \"" + item + "\"")

		return self.__dict__[item]


	def add_constraint(self, constraint):
		"""
		Add constraint to entity

		:param _Constraint constraint:
		:return: None
		"""
		utils.assert_type(constraint, _Constraint)

		self.constraints.append(constraint)
		constraint.check()

	def remove_constraint(self, constraint):
		"""
		Remove constraint from entity

		:param _Constraint constraint:
		:return: None
		"""
		utils.assert_type(constraint, _Constraint)

		if constraint in self.constraints:
			self.constraints.remove(constraint)


class Factory:
	"""
	Creates Constraint and Entity objects. In order to create Entity/Constraint objects, they must be registered via
	register_entity and register_constraint methods, respectively.
	"""

	def __init__(self):
		"""
		Factory constructor.
		"""

		self._entity_map = {}
		self._constraint_map = {}
		self._constraint_clauses = {}

	def register_entity(self, identifier, attribute_map):
		"""
		Register an identifier - attribute map pair for use in creating entities.

		:param str identifier: unique identifier describing entity type i.e. "class", "person", "subject"
		:param dict attribute_map: dictionary whose keys are names of entity properties (i.e. "name", "age"), and whose
			values are the expected type (i.e. str, int, dict) of that attribute. Note: to denote a first-class
			function as a type, use the "callable" keyword.
		:return: None
		"""

		utils.assert_params([identifier, attribute_map], [str, dict])

		if identifier not in self._entity_map:
			self._entity_map[identifier] = attribute_map

	def register_constraint(self, identifier, entity_type, clause):
		"""
		Register an identifier - attribute map pair for use in creating entities.
		:param identifier: unique identifier describing constraint type
		:param entity_type: identifier of entity constraint is to be linked to; must have been registered
		:return: None
		:raises: AssertionError if entity_type is not registered
		"""

		utils.assert_params([identifier, entity_type, clause], [str, str, callable])

		if entity_type not in self._entity_map:
			raise AssertionError("Entity type \"" + entity_type + "\" is not registered")

		if identifier not in self._constraint_map:
			self._constraint_map[identifier] = entity_type
			self._constraint_clauses[identifier] = clause

	def create_entity(self, identifier, obj=None):
		"""
		Factory method for creating Entity objects.

		:param str identifier: identifier of Entity to create
		:param obj: object or dict; if object, uses object properties to populate entity properties;
			if dict, uses key-value pairs
		:return: Entity object of type identifier
		:raises: AttributeError if entity type is not registered.
		"""

		utils.assert_type(identifier, str)

		if identifier in self._entity_map:
			entity = _Entity(identifier, self._entity_map[identifier])

			if obj is not None:
				if type(obj) != dict:
					obj = obj.__dict__

				for p in obj:
					entity[p] = obj[p]

			return entity


		raise AttributeError("Entity type \"" + identifier + "\" is not registered.")

	def create_constraint(self, identifier, callback=None, *args):
		"""
		Factory method for creating Constraint objects.

		:param str identifier: identifier of Constraint to create
		:param clause: function that takes an Entity object and returns a bool if the constraint is satisfied,
			false otherwise
		:param callback: function to be called when the constraint changes state; takes a boolean representing the
			constraint state (True -> satisfied, False -> not)
		:return: Constraint object of type identifier
		:raises: AttributeError if constraint type is not registered.
		"""

		print(args)
		if callback is None:
			utils.assert_type(identifier, str)
		else:
			utils.assert_params([identifier, callback], [str, callable])

		if identifier in self._constraint_map:
			clause = self._constraint_clauses[identifier]

			if utils.is_nested_clause(clause):
				print("nested")
				utils.assert_num_params(self._constraint_clauses[identifier], *args)
				clause = clause(*args)

			print(clause)

			return _Constraint(identifier, clause, callback)

		raise AttributeError("Constraint type \"" + identifier + "\" is not registered.")

	def link(self, a, b):
		"""
		Links a constraint to an entity.

		:param a: constraint or entity object
		:param b: constraint or entity object; must be of different type than a
		:return: None
		:raises: AttributeError if type of entity is not the registered "companion" type of the given constraint type.
		"""

		constraint = a if type(a) == _Constraint else b
		entity = a if constraint is b else b

		utils.assert_params([constraint, entity], [_Constraint, _Entity])

		if self._constraint_map[constraint.identifier] != entity.identifier:
			raise AttributeError(
				"Constraint of type \"" + constraint.identifier + "\" can only be linked to Entity of type \"" +
				self._constraint_map[constraint.identifier] + "\". Tried to link to Entity of type \"" +
				entity.identifier + "\".")

		constraint.link_to(entity)
		entity.add_constraint(constraint)

		constraint.check()


class Graph:

	def __init__(self, name, factory=None):
		"""
		Graph constructor.

		:param str name: name of graph
		:param Factory factory: factory to use in creating Entity and Constraint objects
		:return: Empty Graph object.
		"""

		self.name = name
		self._entities = set()
		self._constraints = set()
		self.factory = factory if factory is not None else Factory()

	@property
	def entities(self):
		return self._entities

	@entities.setter
	def entities(self, value):
		raise NotImplementedError("Cannot reassign entities of graph")

	@property
	def constraints(self):
		return self._constraints

	@constraints.setter
	def constraints(self, value):
		raise NotImplementedError("Cannot reassign constraints of graph")

	def add(self, obj):
		"""
		Add a constraint or entity to the graph. If already added, does nothing. If obj is a Constraint, also adds its
		linked Entity to the graph. If obj is an Entity, also adds all of its constraints to graph.

		:param obj: Constraint or Entity object to add.
		:return: None
		:raises: AssertionError is obj is of Constraint type and it is unlinked.
		"""

		if type(obj) == _Entity:
			self._entities.add(obj)

			for constraint in obj.constraints:
				self.add(constraint)

		if type(obj) == _Constraint:
			self._constraints.add(obj)

			if obj.entity is None:
				raise AssertionError("Cannot add unlinked constraint to graph.")

			self._entities.add(obj.entity)

	def remove(self, obj, keep=False):
		"""
		Remove a constraint or entity from graph.

		:param obj: Constraint or Entity object to remove from graph. If obj is an Entity, removes all of its
			constraints from graph as well.
		:param bool keep: If obj is Constraint and keep is True, then removing the obj from the graph will NOT unlink
			obj from its Entity.

		:return: None
		"""

		if type(obj) == _Entity:
			self._entities.remove(obj)

			for constraint in obj.constraints:
				self.remove(constraint)

		if type(obj) == _Constraint:
			self._constraints.remove(obj)

			if not keep:
				obj.unlink()


	def __contains__(self, item):
		if type(item) == _Entity:
			return item in self._entities

		if type(item) == _Constraint:
			return item in self._constraints

	def __str__(self):
		return self.name + "\n\t" + \
			str(len(self._entities)) + " entities\n\t" + \
			str(len(self._constraints)) + " constraints."

	def register_entity(self, identifier, attribute_map):
		self.factory.register_entity(identifier, attribute_map)

	def register_constraint(self, identifier, entity_type, clause):
		self.factory.register_constraint(identifier, entity_type, clause)

	def create_entity(self, identifier, obj=None):
		entity = self.factory.create_entity(identifier, obj)
		self.add(entity)

		return entity

	def create_constraint(self, identifier, *args, callback=None, link_to=None):
		print(args)
		constraint = self.factory.create_constraint(identifier, callback, *args)

		if link_to is not None:
			self.factory.link(link_to, constraint)
			self.add(constraint)

		return constraint


	def register_class(self, c):
		obj = getattr_static(c, "entity_map", None)

		if obj is None:
			raise AttributeError("To register class, make sure to implement 'entity_map' staticmethod")

		entity_map = obj if type(obj) is dict else obj()

		print(entity_map)
		self.register_entity(c.__name__, entity_map)