class password_manager:
    def __init__(self):
        self.list=[]
    def get_password(self):
       if self.list:
            return self.list[-1]
       return None
    def set_password(self,new):
        if new not in self.list:
            self.list.append(new)
            return True
        return False
    def is_correct(self,p):
        return p==self.get_password()
pm= password_manager()
print(pm.set_password("abcd"))  
print(pm.set_password("abcd"))
print(pm.set_password("fegt"))
print(pm.set_password("a26784"))
print(pm.get_password())
print(pm.is_correct("abcd"))
    
