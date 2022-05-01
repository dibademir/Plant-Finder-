global climateTypes
climateTypes = {
  "Tropical": ["ebony", "palm", "teak"],
  "Dry": ["cactus", "lantana", "astrantia"],
  "Temperate": ["lichen", "moss", "ferns"],
  "Continental": ["maple", "lilac", "camellia"],
  "Polar": ["sedge", "lichen", "moss"]
}

global vegetationTypes
vegetationTypes = {
  "Forest": ["pines", "larches", "spruces"],
  "Grassland": ["needlegrass", "grama", "galleta"],
  "Tundra": ["bearberry", "arctic willow", "labrador tea"],
  "Desert": ["brittlebush", "creosote bush", "barrel cactus"],
  "Ice sheet": ["moss", "lichen", "liverworts"]
}

global plantTypes
plantTypes = {
    "Corn": ["0-150", "Sandy", "Yes", "Yes", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Tomato_je.jpg/440px-Tomato_je.jpg"],
    "Cotton": ["0-150", "Sandy", "Yes", "No", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/CottonPlant.JPG/360px-CottonPlant.JPG"],
    "Rice": ["0-150", "Loamy", "Yes", "Yes", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/White%2C_Brown%2C_Red_%26_Wild_rice.jpg/600px-White%2C_Brown%2C_Red_%26_Wild_rice.jpg"],
    "Vegetables": ["0-150", "Loamy", "Yes", "No", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Marketvegetables.jpg/440px-Marketvegetables.jpg"],
    "Soybean": ["0-150", "Sandy", "No", "Yes", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Soybean.USDA.jpg/440px-Soybean.USDA.jpg"],
    "Tree nuts": ["0-150", "Sandy", "No", "No", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chestnut.jpg/580px-Chestnut.jpg"],
    "Sugar and sweeteners": ["0-150", "Loamy", "No", "Yes", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sucre_blanc_cassonade_complet_rapadura.jpg/440px-Sucre_blanc_cassonade_complet_rapadura.jpg"],
    "Pulses": ["0-150", "Loamy", "No", "No", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Various_legumes.jpg/400px-Various_legumes.jpg"],
    "Wheat": ["150-350", "Sandy", "Yes", "Yes", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Wheat_close-up.JPG/440px-Wheat_close-up.JPG"],
    "Potatoes": ["150-350", "Sandy", "Yes", "No", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Patates.jpg/440px-Patates.jpg"],
    "Cassava": ["150-350", "Loamy", "Yes", "Yes", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Manihot_esculenta_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-090.jpg/440px-Manihot_esculenta_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-090.jpg"],
    "Yams": ["150-350", "Loamy", "Yes", "No", "https://www.farmersalmanac.com/wp-content/uploads/2020/11/yam-sweetpot.jpg"],
    "Plantains": ["150-350", "Sandy", "No", "Yes", "https://hips.hearstapps.com/amv-prod-tpw.s3.amazonaws.com/wp-content/uploads/2015/09/whats-the-deal-with-plantains-00.jpg"],
    "Sorghum": ["150-350", "Sandy", "No", "No", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sorghum.jpg/440px-Sorghum.jpg"],
    "Sweet potatoes": ["150-350", "Loamy", "No", "Yes", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Ipomoea_batatas_006.JPG/440px-Ipomoea_batatas_006.JPG"],
    "Hay": ["150-350", "Loamy", "No", "No", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Roundbale1.jpg/400px-Roundbale1.jpg"]
}

def plantfinder(choice):
    print("Input the following information to know what plant to grow")
    print("Press 1 if you want to find the correct plant type for your region.")
    print("Press 2 if you want to list the climate types")
    print("Press 3 if you want to list the vegetation types")
    print("Press 4 if you want to see the list of plants in a particular climate or vegetation type")
    print("Press 5 if you want to add a new climate type and the plants grown in it")
    print("Press 6 if you want to add a new vegetation type and the plants grown in it")

    if choice == 1:
        rain_question = (f"""
             Approximately how many days of rain do you have in a year?
             A) 0-150
             B) 150-350
             Answer: 
             """)
        print(rain_question, end="")
        rain = input()
        soil_question = (f"""
             What is the structure of the soil you plan to work on?
             A) Sandy
             D) Loamy 
             Answer:
             """)
        print(soil_question, end="")
        soil = input()
        snowfall_question = (f"""
             Do you get any snowfall?
             A) Yes 
             B) No
             Answer:
             """)
        print(snowfall_question, end="")
        snowfall = input()
        machinery_question = (f"""
             Do you have access to machinery?
             A) Yes 
             B) No
             Answer:
             """)
        print(machinery_question, end="")
        machinery = input()

        for plant in plantTypes.keys():
            if rain == plantTypes[plant][0] and soil == plantTypes[plant][1] and snowfall == plantTypes[plant][2] and machinery == plantTypes[plant][3]:
                print(f"This is the recommended plant types for you: {plant}. You can see the plant by clicking the link: {plantTypes[plant][4]}")

    elif choice == 2:
        for climate in climateTypes.keys():
            print(climate)

    elif choice == 3:
        for vegetation in vegetationTypes.keys():
            print(vegetation)

    elif choice == 4:
        climate_input = input("Write down a climate that you want to see the plants under.")
        vegetation_input = input("Write down a vegetation that you want to see the plants under.")

        print(f"{climate_input} and Plant Types")
        counter1 = 1
        for plant in climateTypes[climate_input]:
            print(counter1, plant)
            counter1 += 1

        print(f"{vegetation_input} and Plant Types")
        counter2 = 1
        for plant in vegetationTypes[vegetation_input]:
            print(counter2, plant)
            counter2 += 1

    elif choice == 5:
        add_climate = input("What climate type do you want to add?")
        if add_climate in climateTypes:
            print("This climate type already exists")
        else:
            new_plants = []
            print("Write down 3 new plants that are grown in the climate you have added")
            for i in range(3):
                plant = input("Enter {}. plant that grows in {} climate".format(i+1, add_climate))
                new_plants.append(plant)
            climateTypes[add_climate] = new_plants
            print("You have added the {} climate and the plants that can be grown.".format(add_climate))

    elif choice == 6:
        add_vegetation = input("What vegetation type do you want to add?")
        if add_vegetation in vegetationTypes:
            print("This vegetation type already exists")
        else:
            new_plants = []
            print("Write down 3 new plants that are grown in the vegetation type you have added")
            for i in range(3):
                plant = input("Enter {}. plant that grows in {} vegetation type".format(i + 1, add_vegetation))
                new_plants.append(plant)
            vegetationTypes[add_vegetation] = new_plants
            print("You have added the {} vegetation type and the plants that can be grown.".format(add_vegetation))



def repetition():
    continuing = input("Do you want to continue?")
    choice = int(input("Write down a number: "))
    if continuing == "Yes":
        plantfinder(choice)
        repetition()
    else:
        quit()

repetition()