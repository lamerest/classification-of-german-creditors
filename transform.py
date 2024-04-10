


from numpy import NaN, nan
import numpy as np
from pandas import DataFrame

def transform(data: DataFrame):
	prop = 'Housing'
	transform_prop(data, prop, 'rent', 0)
	transform_prop(data, prop, 'own', 1)
	transform_prop(data, prop, 'free', 2)

	prop = 'Sex'
	transform_prop(data, prop, 'male', 0)
	transform_prop(data, prop, 'female', 1)

	prop = 'Saving accounts'
	transform_prop(data, prop, 'NaN', 0)
	transform_prop(data, prop, 'little', 1)
	transform_prop(data, prop, 'moderate', 2)
	transform_prop(data, prop, 'quite rich', 3)
	transform_prop(data, prop, 'rich', 4)

	prop = 'Checking account'
	transform_prop(data, prop, 'NaN', 0)
	transform_prop(data, prop, 'little', 1)
	transform_prop(data, prop, 'moderate', 2)
	transform_prop(data, prop, 'rich', 3)

	prop = 'Purpose'
	transform_prop(data, prop, 'radio/TV', 0)
	transform_prop(data, prop, 'furniture/equipment', 1)
	transform_prop(data, prop, 'car', 2)
	transform_prop(data, prop, 'education', 3)
	transform_prop(data, prop, 'business', 4)
	transform_prop(data, prop, 'repairs', 5)
	transform_prop(data, prop, 'domestic appliances', 6)
	transform_prop(data, prop, 'vacation/others', 7)

	return data

def transform_prop(data: DataFrame, prop, value, new_value):
	if (prop == 'Saving accounts' or prop == 'Checking account') and value == 'NaN':
		data.loc[data[prop].isnull(), prop] = new_value
	else:
		data.loc[data[prop] == value, prop] = new_value
