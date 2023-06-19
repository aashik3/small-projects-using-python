class RentalProperty:
    def __init__(self, property_id, address, bedrooms, bathrooms, rent):
        self.property_id = property_id
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.rent = rent

class RentalManager:
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def display_properties(self):
        if not self.properties:
            print("No properties found.")
        else:
            print("Property ID\tAddress\t\tBedrooms\tBathrooms\tRent")
            for property in self.properties:
                print(f"{property.property_id}\t\t{property.address}\t{property.bedrooms}\t\t{property.bathrooms}\t\t{property.rent}")

    def search_property(self, property_id):
        for property in self.properties:
            if property.property_id == property_id:
                print("Property found:")
                print("Address:", property.address)
                print("Bedrooms:", property.bedrooms)
                print("Bathrooms:", property.bathrooms)
                print("Rent:", property.rent)
                return

        print("Property not found.")

def main():
    manager = RentalManager()

    while True:
        print("\nHome Rental Management System")
        print("1. Add Property")
        print("2. Display Properties")
        print("3. Search Property")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            property_id = input("Enter property ID: ")
            address = input("Enter property address: ")
            bedrooms = int(input("Enter number of bedrooms: "))
            bathrooms = int(input("Enter number of bathrooms: "))
            rent = float(input("Enter monthly rent amount: "))

            property = RentalProperty(property_id, address, bedrooms, bathrooms, rent)
            manager.add_property(property)
            print("Property added successfully!")

        elif choice == '2':
            manager.display_properties()

        elif choice == '3':
            property_id = input("Enter property ID to search: ")
            manager.search_property(property_id)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
