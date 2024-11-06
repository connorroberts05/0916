class Car:
    def __init__(self, name, price, category, lifestyle_suitability, environment):
        self.name = name
        self.price = price
        self.category = category
        self.lifestyle_suitability = lifestyle_suitability
        self.environment = environment


class Person:
    def __init__(self, age, budget, lifestyle, environment):
        self.age = age
        self.budget = budget
        self.lifestyle = lifestyle
        self.environment = environment

def match_price(person_budget, car_price):
    if car_price <= person_budget:
        return 1.0  # Perfect match
    elif car_price <= person_budget + 5000:  # Slightly over budget
        return 0.8
    else:
        return 0.0  # No match

def match_lifestyle(person_lifestyle, car_lifestyle_suitability):
    if person_lifestyle == car_lifestyle_suitability:
        return 1.0
    else:
        return 0.5  # Partial match

def match_age(person_age, car_category):
    if person_age <= 30 and car_category == 'compact':
        return 1.0
    elif 30 < person_age <= 50 and car_category in ['sedan', 'SUV']:
        return 1.0
    elif person_age > 50 and car_category in ['luxury', 'sedan']:
        return 1.0
    else:
        return 0.5  # Partial match
    
def match_environment(person_environment, car_environment):
    if person_environment == car_environment:
      return 1.0
    else:
        return 0.5  

def recommend_cars(person, cars):
    recommendations = []
    for car in cars:
        price_score = match_price(person.budget, car.price)
        lifestyle_score = match_lifestyle(person.lifestyle, car.lifestyle_suitability)
        age_score = match_age(person.age, car.category)
        environment_score = match_environment(person.environment, car.environment)

        total_score = (0.6 * price_score) + (0.3 * lifestyle_score) +(0.3 * environment_score ) + (0.1 * age_score)
        recommendations.append((car.name, total_score))
    
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:5]  # Return top 5 matches

# Example usage:
cars = [
    Car("Toyota Camry", 25000, "sedan", "commuter", "urban"),
    Car("Honda Accord", 28000, "sedan", "commuter", "urban"),
    Car("Tesla Model 3", 45000, "electric", "commuter", "urban"),
    Car("Hyundai Sonata", 25000, "sedan", "commuter", "suburb"),
    Car("BMW 3 Series", 45000, "sedan", "commuter", "urban"),
    Car("Mercedes-Benz C-Class", 50000, "sedan", "commuter", "urban"),
    Car("Nissan Altima", 26000, "sedan", "commuter", "suburb"),
    Car("Audi A4", 40000, "sedan", "commuter", "urban"),
    Car("Mazda 3", 24000, "sedan", "commuter", "city"),
    Car("Chevrolet Malibu", 27000, "sedan", "commuter", "suburb"),

    Car("Toyota RAV4", 30000, "SUV", "family", "suburb"),
    Car("Honda CR-V", 32000, "SUV", "family", "suburb"),
    Car("Ford Escape", 28000, "SUV", "commuter", "city"),
    Car("Chevrolet Equinox", 33000, "SUV", "family", "suburb"),
    Car("BMW X5", 60000, "SUV", "family", "urban"),
    Car("Jeep Grand Cherokee", 45000, "SUV", "adventure", "rural"),
    Car("Hyundai Tucson", 29000, "SUV", "family", "suburb"),
    Car("Kia Sportage", 28000, "SUV", "family", "suburb"),
    Car("Nissan Rogue", 32000, "SUV", "family", "suburb"),
    Car("Subaru Outback", 35000, "SUV", "adventure", "rural"),

    Car("Ford F-150", 35000, "truck", "work", "rural"),
    Car("Ram 1500", 40000, "truck", "work", "rural"),
    Car("Chevrolet Silverado 1500", 37000, "truck", "work", "rural"),
    Car("Toyota Tacoma", 35000, "truck", "adventure", "rural"),
    Car("GMC Sierra 1500", 45000, "truck", "work", "rural"),

    Car("Tesla Model Y", 55000, "electric", "family", "urban"),
    Car("Ford Mustang Mach-E", 48000, "electric", "commuter", "urban"),
    Car("Volkswagen ID.4", 40000, "electric", "family", "suburb"),
    Car("Rivian R1T", 73000, "electric", "adventure", "rural"),
    Car("Lucid Air", 80000, "electric", "commuter", "urban"),

    Car("Chevrolet Bolt EV", 35000, "electric", "commuter", "city"),
    Car("BMW i4", 60000, "electric", "commuter", "urban"),
    Car("Audi e-Tron", 75000, "electric", "commuter", "urban"),
    Car("Porsche Taycan", 90000, "electric", "commuter", "urban"),
    Car("Ford F-150 Lightning", 60000, "electric", "work", "rural")
]


person = Person(age=30, budget=30000, lifestyle="commuter", environment="city")

top_cars = recommend_cars(person, cars)
print(top_cars)
