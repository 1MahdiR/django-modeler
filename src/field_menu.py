#
# Clients for building fields
# By Ray (__mr__)
#
# The value that user enters won't get validated!
# such as empty strings, alnum(), etc.
#

from model_builder import *
from static_data.prompts import *
from static_data.model_builder_statics import DJANGO_ON_DELETE_ACTIONS
from menu_module import show_on_delete_actions
from utility import validate_name

def BigIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = BigIntegerField_Builder(name,default,blank,null,unique)

	return field

def BooleanField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = BooleanField_Builder(name,default,blank,null,unique)

	return field

def CharField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(32))

	if not max_length:
		max_length = 32
	elif not max_length.isdigit() or '.' in max_length:
		raise ValueError("Invalid input!")

	if int(max_length) < 1:
		raise ValueError("Invalid input!")

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = CharField_Builder(name,max_length,default,blank,null,unique)

	return field

def DateField_client(name):

	default = input(ENTER_DEFAULT_NOW_DATE_PROMPT)
	if default.lower() == 'y':
		default = 'timezone.now'
	else:
		default = ''

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = DateField_Builder(name,default,blank,null,unique)

	return field

def DateTimeField_client(name):

	default = input(ENTER_DEFAULT_NOW_DATE_PROMPT)
	if default.lower() == 'y':
		default = 'timezone.now'
	else:
		default = ''

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = DateTimeField_Builder(name,default,blank,null,unique)

	return field

def DecimalField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	max_digits = input(ENTER_MAX_DIGIT_PROMPT.format(10))
	if not max_digits:
		max_digits = 10

	decimal_places = input(ENTER_DECIMAL_PLACES_PROMPT.format(3))
	if not decimal_places:
		decimal_places = 3

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = DecimalField_Builder(name,max_digits,decimal_places,default,blank,null,unique)

	return field

def EmailField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(254))

	if not max_length:
		max_length = 254
	elif not max_length.isdigit() or '.' in max_length:
		raise ValueError("Invalid input!")

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = EmailField_Builder(name,max_length,default,blank,null,unique)

	return field

def FileField_client(name):

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(100))

	if not max_length:
		max_length = 100
	elif not max_length.isdigit() or '.' in max_length:
		raise ValueError("Invalid input!")

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = FileField_Builder(name,max_length,blank,null,unique)

	return field

def FloatField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = FloatField_Builder(name,default,blank,null,unique)

	return field

def ImageField_client(name):

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(100))

	if not max_length:
		max_length = 100
	elif not max_length.isdigit() or '.' in max_length:
		raise ValueError("Invalid input!")

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = ImageField_Builder(name,max_length,blank,null,unique)

	return field

def IntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = IntegerField_Builder(name,default,blank,null,unique)

	return field

def PositiveBigIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = PositiveBigIntegerField_Builder(name,default,blank,null,unique)

	return field

def PositiveIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = PositiveIntegerField_Builder(name,default,blank,null,unique)

	return field

def PositiveSmallIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = PositiveSmallIntegerField_Builder(name,default,blank,null,unique)

	return field

def SlugField_client(name):

	unicode = input(ENTER_UNICODE_ALLOWED_PROMPT)
	if unicode.lower == 'y':
		unicode = True
	else:
		unicode = False

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = SlugField_Builder(name,unicode,default,blank,null,unique)

	return field

def SmallIntegerField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = SmallIntegerField_Builder(name,default,blank,null,unique)

	return field

def TextField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = TextField_Builder(name,default,blank,null,unique)

	return field

def TimeField_client(name):

	default = input(ENTER_DEFAULT_NOW_DATE_PROMPT)
	if default.lower() == 'y':
		default = 'timezone.now'
	else:
		default = ''

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = TimeField_Builder(name,default,blank,null,unique)

	return field

def URLField_client(name):

	default = input(ENTER_DEFAULT_VALUE_PROMPT)

	max_length = input(ENTER_MAX_LENGTH_PROMPT.format(200))

	if not max_length:
		max_length = 200
	elif not max_length.isdigit() or '.' in max_length:
		raise ValueError("Invalid input!")

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = URLField_Builder(name,max_length,default,blank,null,unique)

	return field

def UUIDField_client(name):

	default = input(ENTER_DEFAULT_UUID_PROMPT)
	if default.lower() == 'y':
		default = 'uuid.uuid4'
	else:
		default = ''

	primary_key = input(ENTER_UUID_PRIMARY_KEY_PROMPT)
	if primary_key.lower() == 'y':
		primary_key = True
	else:
		primary_key = False

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	unique = input(ENTER_UNIQUE_VALUE_PROMPT)
	if unique.lower() == 'y':
		unique = True
	else:
		unique = False

	field = UUIDField_Builder(name,primary_key,default,blank,null,unique)

	return field

def ForeignKey_client(name):

	to = input(ENTER_TO_PROMPT)
	if not to:
		raise ValueError("Reference key should match Python3 naming conventions!")

	key = to.split('.')
	app_name = ""
	model = ""
	key_length = len(key)

	if key_length > 2:
		raise ValueError("Invalid input!")
	elif key_length == 2:
		app_name, model = key
		if not (validate_name(model) and validate_name(app_name)):
			raise ValueError("Reference key should match Python3 naming conventions!")
	else:
		model = key[0]
		if not validate_name(model):
			raise ValueError("Reference key should match Python3 naming conventions!")

	show_on_delete_actions()
	on_delete = input(ENTER_FOREIGN_KEY_ON_DELETE_PROMPT)
	if not (on_delete and on_delete.isdigit() and (0 > int(on_delete) or 5 > int(on_delete))):
		raise IndexError("Wrong input for index on delete actions!\nAborted!\n")
	else:
		on_delete = DJANGO_ON_DELETE_ACTIONS[int(on_delete)]

	related_name = input(ENTER_RELATED_NAME_PROMPT)
	if not related_name.strip():
		related_name = None

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	field = ForeignKeyField_Builder(name,model,app_name,on_delete,related_name,blank,null)

	return field

def OneToOneField_client(name):

	to = input(ENTER_TO_PROMPT)
	if not to:
		raise ValueError("Reference key should match Python3 naming conventions!")

	key = to.split('.')
	app_name = ""
	model = ""
	key_length = len(key)

	if key_length > 2:
		raise ValueError("Invalid input!")
	elif key_length == 2:
		app_name, model = key
		if not (validate_name(model) and validate_name(app_name)):
			raise ValueError("Reference key should match Python3 naming conventions!")
	else:
		model = key[0]
		if not validate_name(model):
			raise ValueError("Reference key should match Python3 naming conventions!")

	show_on_delete_actions()
	on_delete = input(ENTER_FOREIGN_KEY_ON_DELETE_PROMPT)
	if not (on_delete and on_delete.isdigit() and (0 > int(on_delete) or 5 > int(on_delete))):
		return
	else:
		on_delete = DJANGO_ON_DELETE_ACTIONS[int(on_delete)]

	related_name = input(ENTER_RELATED_NAME_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	field = OneToOneField_Builder(name,to,on_delete,blank,null)

	return field

def ManyToManyField_client(name):

	to = input(ENTER_TO_PROMPT)
	if not to:
		raise ValueError("Reference key should match Python3 naming conventions!")

	key = to.split('.')
	app_name = ""
	model = ""
	key_length = len(key)

	if key_length > 2:
		raise ValueError("Invalid input!")
	elif key_length == 2:
		app_name, model = key
		if not (validate_name(model) and validate_name(app_name)):
			raise ValueError("Reference key should match Python3 naming conventions!")
	else:
		model = key[0]
		if not validate_name(model):
			raise ValueError("Reference key should match Python3 naming conventions!")

	related_name = input(ENTER_RELATED_NAME_PROMPT)

	blank = input(ENTER_BLANK_VALUE_PROMPT)
	if blank.lower() == 'y':
		blank = True
	else:
		blank = False

	null = input(ENTER_NULL_VALUE_PROMPT)
	if null.lower() == 'y':
		null = True
	else:
		null = False

	field = ManyToManyField_Builder(name,to,blank,null)

	return field
