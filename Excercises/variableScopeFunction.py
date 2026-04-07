from Excercises.variableScopeFunctionTemperature import water_state

FREEZING_POINT = 0
BOILING_POINT  = 100

if __name__ == "__main__":
    print(water_state(100))
    print(water_state(1))
    print(water_state(200))