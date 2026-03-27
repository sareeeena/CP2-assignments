from abc import ABC, abstractmethod

def audit_log(func):
    def wrapper(*args,**kwargs):
        print(f"[ADULT] Calling {func.__name__}")
        result=func(**args,**kwargs)
        print(f"[ADULT] Success")
        return result
    return wrapper

class MessageSender(ABC):
    _total_messages=0

@abstractmethod
def send(self,text):
    pass
@classmethod
def get_total(cls):
    return cls._total_messages

class EmailSender(MessageSender):
    def __init__(self,email_address):
        self.email_address =email_address

    @audit_log
    def send(self,text):
        MessageSender._total_messages += 1
        return f"Email to {self.email_address}: {text}"
    
    @classmethod
    def from_contact(cls,contact_string):
        contact,email=contact_string.split(':')
        return cls(email)
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email
    
class SMSSender(MessageSender):
    def __init__(self,phone_number):
        self.phone_number = phone_number

    @audit_log
    def send(self,text):
        MessageSender._total