from pydantic import BaseModal
class Blog(BaseModal):
    title:str
    body:str