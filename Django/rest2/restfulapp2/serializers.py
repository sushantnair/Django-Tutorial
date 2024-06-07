from rest_framework import serializers #type: ignore
from .models import Person

# PART A

'''
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # The below statement is used to serialize particular columns of the table
        # fields = ['first_name', 'age']
        # The below statament is used to serialize all columns of the table
        fields = '__all__'
        # The below statement is used to serialize all columns except the ones mentioned
        # exclude = ['middle_name', 'last_name']
'''

# PART B

'''
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # The below statement is used to serialize particular columns of the table
        # fields = ['first_name', 'age']
        # The below statament is used to serialize all columns of the table
        fields = '__all__'
        # The below statement is used to serialize all columns except the ones mentioned
        # exclude = ['middle_name', 'last_name']

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Underage')
        return age
    
    # notice how some characters which carry special meaning, like doublequotes, are mentioned

    def validate_first_name(self, first_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in first_name):
            raise serializers.ValidationError(f'First Name {first_name} has special characters which are not allowed.')
        
    def validate_middle_name(self, middle_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in middle_name):
            raise serializers.ValidationError(f'First Name {middle_name} has special characters which are not allowed.')
        
    def validate_last_name(self, last_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in last_name):
            raise serializers.ValidationError(f'First Name {last_name} has special characters which are not allowed.')
'''

# PART C

'''
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # The below statement is used to serialize particular columns of the table
        # fields = ['first_name', 'age']
        # The below statament is used to serialize all columns of the table
        fields = '__all__'
        # The below statement is used to serialize all columns except the ones mentioned
        # exclude = ['middle_name', 'last_name']
        depth = 1

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Underage')
        return age
    
    # notice how some characters which carry special meaning, like doublequotes, are mentioned

    def validate_first_name(self, first_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in first_name):
            raise serializers.ValidationError(f'First Name {first_name} has special characters which are not allowed.')
        
    def validate_middle_name(self, middle_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in middle_name):
            raise serializers.ValidationError(f'First Name {middle_name} has special characters which are not allowed.')
        
    def validate_last_name(self, last_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in last_name):
            raise serializers.ValidationError(f'First Name {last_name} has special characters which are not allowed.')
'''
        
# PART D

'''
from .models import Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        # To get only course_name and not any other column
        fields = ['course_name']

class PersonSerializer(serializers.ModelSerializer):
    course = CoursesSerializer()
    class Meta:
        model = Person
        # The below statement is used to serialize particular columns of the table
        # fields = ['first_name', 'age']
        # The below statament is used to serialize all columns of the table
        fields = '__all__'
        # The below statement is used to serialize all columns except the ones mentioned
        # exclude = ['middle_name', 'last_name']

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Underage')
        return age
    
    # notice how some characters which carry special meaning, like doublequotes, are mentioned

    def validate_first_name(self, first_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in first_name):
            raise serializers.ValidationError(f'First Name {first_name} has special characters which are not allowed.')
        
    def validate_middle_name(self, middle_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in middle_name):
            raise serializers.ValidationError(f'Middle Name {middle_name} has special characters which are not allowed.')
        
    def validate_last_name(self, last_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in last_name):
            raise serializers.ValidationError(f'Last Name {last_name} has special characters which are not allowed.')
'''

# PART E

'''
from .models import Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        # To get only course_name and not any other column
        fields = ['course_name']

class PersonSerializer(serializers.ModelSerializer):
    course = CoursesSerializer()
    nationality = serializers.SerializerMethodField()

    class Meta:
        model = Person
        # The below statement is used to serialize particular columns of the table
        # fields = ['first_name', 'age']
        # The below statament is used to serialize all columns of the table
        fields = '__all__'
        # The below statement is used to serialize all columns except the ones mentioned
        # exclude = ['middle_name', 'last_name']

    def get_nationality(self, object):
        return "India"

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Underage')
        return age
    
    # notice how some characters which carry special meaning, like doublequotes, are mentioned

    def validate_first_name(self, first_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in first_name):
            raise serializers.ValidationError(f'First Name {first_name} has special characters which are not allowed.')
        
    def validate_middle_name(self, middle_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in middle_name):
            raise serializers.ValidationError(f'Middle Name {middle_name} has special characters which are not allowed.')
        
    def validate_last_name(self, last_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in last_name):
            raise serializers.ValidationError(f'Last Name {last_name} has special characters which are not allowed.')
'''

# PART F

'''
from .models import Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        # To get only course_name and not any other column
        fields = ['course_name']

class PersonSerializer(serializers.ModelSerializer):
    course = CoursesSerializer()
    course_details = serializers.SerializerMethodField()

    class Meta:
        model = Person
        # The below statement is used to serialize particular columns of the table
        # fields = ['first_name', 'age']
        # The below statament is used to serialize all columns of the table
        fields = '__all__'
        # The below statement is used to serialize all columns except the ones mentioned
        # exclude = ['middle_name', 'last_name']

    def get_course_details(self, object):
        course_objectect = Courses.objects.get(id = object.course.id)
        return {'course_domain': course_objectect.course_domain, 'certificate': course_objectect.certificate}

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Underage')
        return age
    
    # notice how some characters which carry special meaning, like doublequotes, are mentioned

    def validate_first_name(self, first_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in first_name):
            raise serializers.ValidationError(f'First Name {first_name} has special characters which are not allowed.')
        
    def validate_middle_name(self, middle_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in middle_name):
            raise serializers.ValidationError(f'Middle Name {middle_name} has special characters which are not allowed.')
        
    def validate_last_name(self, last_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in last_name):
            raise serializers.ValidationError(f'Last Name {last_name} has special characters which are not allowed.')
'''

# PART G

'''
from .models import Courses

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    pword = serializers.CharField()

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        # To get only course_name and not any other column
        fields = ['course_name']

class PersonSerializer(serializers.ModelSerializer):
    course = CoursesSerializer()
    course_details = serializers.SerializerMethodField()

    class Meta:
        model = Person
        # The below statement is used to serialize particular columns of the table
        # fields = ['first_name', 'age']
        # The below statament is used to serialize all columns of the table
        fields = '__all__'
        # The below statement is used to serialize all columns except the ones mentioned
        # exclude = ['middle_name', 'last_name']

    def get_course_details(self, object):
        course_object = Courses.objects.get(id = object.course.id)
        return {'course_domain': course_object.course_domain, 'certificate': course_object.certificate}

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Underage')
        return age
    
    # notice how some characters which carry special meaning, like doublequotes, are mentioned

    def validate_first_name(self, first_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in first_name):
            raise serializers.ValidationError(f'First Name {first_name} has special characters which are not allowed.')
        
    def validate_middle_name(self, middle_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in middle_name):
            raise serializers.ValidationError(f'Middle Name {middle_name} has special characters which are not allowed.')
        
    def validate_last_name(self, last_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in last_name):
            raise serializers.ValidationError(f'Last Name {last_name} has special characters which are not allowed.')
'''

# PART H

from .models import Courses

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    pword = serializers.CharField()

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        # To get only course_name and not any other column
        fields = ['course_name']

class PersonSerializer(serializers.ModelSerializer):
    course = CoursesSerializer()
    course_details = serializers.SerializerMethodField()

    class Meta:
        model = Person
        # The below statement is used to serialize particular columns of the table
        # fields = ['first_name', 'age']
        # The below statament is used to serialize all columns of the table
        fields = '__all__'
        # The below statement is used to serialize all columns except the ones mentioned
        # exclude = ['middle_name', 'last_name']

    def get_course_details(self, object):
        if object.course:
            return {
                'course_code': object.course.course_code,
                'course_domain': object.course.course_domain,
            }
        return None

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Underage')
        return age
    
    # notice how some characters which carry special meaning, like doublequotes, are mentioned

    def validate_first_name(self, first_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in first_name):
            raise serializers.ValidationError(f'First Name {first_name} has special characters which are not allowed.')
        
    def validate_middle_name(self, middle_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in middle_name):
            raise serializers.ValidationError(f'Middle Name {middle_name} has special characters which are not allowed.')
        
    def validate_last_name(self, last_name):
        special_characters = "~`!@#$%^&*()_+-={[}]|:;\"<>,.?/"
        if any(character in special_characters for character in last_name):
            raise serializers.ValidationError(f'Last Name {last_name} has special characters which are not allowed.')
