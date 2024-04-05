from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class ISender(IContent):

    def format(self):
        return "I'm" + " " + self.text


class IReceiver(IContent):
    def format(self):
        return "I'm" + " " + self.text


class MyMl(IContent):
    def format(self):
        return "\n".join(['<myML>', self.text, '</myML>'])


class HTML(IContent):
    def format(self):
        return "\n".join(['<html>', self.text, '</html>'])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: ISender):
        self.__sender = sender.format()

    def set_receiver(self, receiver: IReceiver):
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):

        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


# email = Email('IM', 'MyML')
# email.set_sender(ISender('qmal'))
# email.set_receiver(IReceiver('james'))
# email.set_content(MyMl('Hello, there!'))
# print(email)


email = Email('IM')
email.set_sender(ISender('qmal'))
email.set_receiver(IReceiver('james'))
content = MyMl('Hello, there!')
email.set_content(content)
print(email)
