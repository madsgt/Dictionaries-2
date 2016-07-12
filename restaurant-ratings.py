
restaurant_ratings = {}



open_file = open("./scores.txt")



for line in open_file:

    line = line.rstrip()
    words = line.split(":")

    restuarant_name = words[0]
    restaurant_rating = words[1]

    restaurant_ratings[restuarant_name] = restaurant_rating

for add_restaurant_name in restuarant_name:

    add_restaurant_name = raw_input("Do you want to add a new Restaurant e.g Yes or No or Quit: ")


# the code above is for first exercise of dictionaries_restaurant ratings, the one below is further study

    if add_restaurant_name == "Yes":
        new_restaurant_name = raw_input(" Please enter the Restaurant: ")
        new_rating = int(raw_input("Please enter a Rating: "))

        restaurant_ratings[new_restaurant_name] = new_rating
        print sorted(restaurant_ratings)

    elif add_restaurant_name == "Quit":
        print sorted(restaurant_ratings)
        break
    else:
        print sorted(restaurant_ratings)


    
# sorted_ratings = sorted(restaurant_ratings)

# print sorted_ratings

        
