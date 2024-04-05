class EmailValidator:

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        parts = email.split("@")
        if len(parts) != 2:
            return False

        name, rest = parts
        mail_parts = rest.split(".")
        if len(mail_parts) != 2:
            return False

        mail, domains = mail_parts
        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domains)



mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))