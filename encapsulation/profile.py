class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        characters_long_case = len(value) >= 8
        upper_letter_case = len([l for l in value if l.isupper()]) > 0
        containing_digit_case = len([d for d in value if d.isdigit()]) > 0
        is_valid = characters_long_case and upper_letter_case and containing_digit_case

        if not is_valid:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# #profile_with_invalid_password = Profile('My_username', 'My-password')
# #profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username","Passw0rd")
# print(correct_profile)

import unittest

class Tests(unittest.TestCase):
    def test_invalid_password(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('My_username', 'My-password')
        self.assertEqual(str(ve.exception), "The password must be 8 or more characters"
                                            " with at least 1 digit and 1 uppercase letter.")

    def test_invalid_username(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('Too_long_username', 'Any')
        self.assertEqual(str(ve.exception), "The username must be between 5 and 15 characters.")

    def test_correct_profile(self):
        self.profile = Profile("Username", "Passw0rd")
        self.assertEqual(str(self.profile), 'You have a profile with username: "Username" and password: ********')

if __name__ == "__main__":
    unittest.main()