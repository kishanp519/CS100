# 1. B
# 2. D
# 3. B
# 4. E
# 5. E
# 6. A
# 7. C
# 8. C
# 9. E
# 10.A

# 11A
class MealPlan:
    '''This class illustrates a meal plan object of foods and their calories'''

    def __init__(self, name):
        self.name = name
        self.foods = {}

    def addFood(self, food, calories):
        self.foods[food] = calories

    def getCalorieCount(self):
        calorieSum = 0
        for key in self.foods:
            calorieSum += self.foods[key]
        return calorieSum
        # or
        # return sum(self.foods.values())


# 11B
import meal_plan

breakfastMealPlan = meal_plan.MealPlan("breakfast")
breakfastMealPlan.addFood("sausage", 200)
breakfastMealPlan.addFood("eggs", 100)
breakfastMealPlan.addFood("coffee", 50)
print(breakfastMealPlan.getCalorieCount())


# 12
def initialMatch(text):
    d = {}
    words = text.split()
    for word in words:
        if word not in d:
            d[word] = []
    for word in words:
        for key in d:
            if key[0] == word[0] and word != key and word not in d[key]:
                d[key].append(word)
                break
    return d


# 13
def fileStats(inFile, outFile):
    f = open(inFile)
    out = open(outFile, 'w')
    words = f.read().split()
    d = {}
    for word in words:
        if len(word) not in d:
            d[len(word)] = [word]
        else:
            if word not in d[len(word)]:
                d[len(word)].append(word)
    for words in d.values():
        for word in words:
            out.write(word + ' ')
        out.write('\n')
    f.close()
    out.close()
