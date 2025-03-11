# Notify when there are no more trays to remove, but it seems to be missing that step. Can you identify what is gone wrong and apply a fix?
# Stack add and remove element exercise

class CafeteriaStack:
    def __init__(self):
        self.stack = []
    
    def add_tray(self, tray_id):
        self.stack.append(tray_id)
    
    def remove_tray(self):
        if not self.stack:
             return "No more trays!"
        else:
            tray_id = self.stack[-1]
            self.stack.pop()
            return tray_id
            

# Sample usage
cafeteria = CafeteriaStack()
cafeteria.add_tray("Tray_4")  # Adding a tray to the stack
print(cafeteria.remove_tray())  # This should print "Tray_4"
print(cafeteria.remove_tray()) # Prints: "No more trays!"
