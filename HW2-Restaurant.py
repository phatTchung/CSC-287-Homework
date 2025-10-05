# TODO: Define the Staff base class
# TODO: Define the Chef subclass
# TODO: Define the Waiter subclass
# TODO: Define the staff_shift function

def main():
    # Generic staff member
    s = Staff("Alex Johnson", "S-001")
    
    # Chef
    c = Chef("Gordon Ramsay", "C-101", "Italian cuisine")
    
    # Waiter
    w = Waiter("Emily Clarke", "W-202", [1, 3, 5])
    
    # Test all staff members
    staff_shift(s)
    staff_shift(c)
    staff_shift(w)

if __name__ == "__main__":
    main()
