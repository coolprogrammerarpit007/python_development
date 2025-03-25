# Compare Instance Methods vs Class Methods vs Static Methods
# If you’re here for a quick reminder of how the three method types differ from one another, then consider the following overview that compares them:

# Instance methods use a self parameter pointing to an instance of the class. They can access and modify instance state through self and class state through self.__class__. These are the most common methods in Python classes.

# Class methods use a cls parameter pointing to the class itself. They can modify class-level state through cls, but they can’t modify individual instance state.

# Static methods don’t take self or cls parameters. They can’t modify instance or class state directly, and you’ll mainly use them for organizational purposes and namespacing.

class DemoClass:
    def instance_method(self):
        return ("Instance method called",self)
    
    @classmethod
    def class_method(cls):
        return ("class method called",cls)
    
    @staticmethod
    def static_method():
        return ("Static Method is called!")