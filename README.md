# AirBnB_clone
This is the infrastructure of the Airbnb project

## BaseModel
- defines all common attributes/methods for other classes
  ### Attributes
	- id: Unique id for each BaseModel.
	- created_at: Current datetime when an instance is created.
	- updated_at: current datetime when an instance is created and it will be updated every time you change your object.
  ### Methods
	- save(): updates the public instance attribute updated_at with the current datetime.
	- to_dict(): returns a dictionary containing all keys/values of __dict__ of the instance.

- The BaseModel will take care of the initialization, serialization and deserialization of the instances.


