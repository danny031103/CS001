#Daniel Brito
#db4471
#Prof. Khye
#Assignment 11 Part 1
#######################

class Smartphone():

    def __init__(self, storage, name):
        self.__storage=storage
        self.__name=name
        self.__apps={}
        self.report()
        print()
        
    def add_app(self, app, size):
        if app in self.__apps:
            print(app, "is already installed")
        elif size>self.__storage:
            print("Cannot install ", app, ", not enough available space", sep='')
        else:
            self.__apps[app]=size
            self.__storage=self.__storage-size
            print(app, "has been installed")
            
    def remove_app(self, app):
        if app not in self.__apps:
            print("Cannot delete ", app, ", not installed", sep='')
        else:
            self.__storage+=self.__apps[app]
            del self.__apps[app]
            print(app, "has been deleted")

    def has_app(self, app):
        return app in self.__apps

    def get_available_space(self):
        return self.__storage-sum(self.__apps.values())

    def report(self):
        print("Name: ", self.__name, sep='')
        print("Capacity: ", self.__storage, sep='')
        print("Available space: ", self.get_available_space(), sep='')
        print("Apps installed: ", len(self.__apps), sep='')
        for app, size in sorted(self.__apps.items()):
            print("* ", app, " is using ", size, " GB", sep='')
        print()
        

x=True

while x==True:
    control=True
    storage = int(input("Size of your new smartphone (32, 64, or 128 GB): "))
    if storage!=32 and storage!=64 and storage!=128:
        print("Invalid size")
    name=str(input("Smartphone name? "))
    print(name, "has been built.")
    print()
    phone=Smartphone(storage, name)
    print()
    while control==True:
        choice=input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
        if choice == "r" or choice=="R":
            phone.report()
            
        elif choice == "a" or choice=="A":
            app=input("App name to add: ")
            app_lock=True
            while app_lock==True:
                size=input("App size in GB: ")
                if str(size).isnumeric():
                    app_lock=False
                    size = int(size)
                else:
                    continue
            phone.add_app(app, size)
            
        elif choice=="e" or choice=="E":
            app=input("App name to remove: ")
            if phone.has_app(app)==True:
                phone.remove_app(app)
            else:
                print("Cannot delete ", app, ", not installed", sep='')
                
        elif choice=="q" or choice=="Q":
            print("Goodbye!")
            x=False
            control=False
            
        else:
            continue



