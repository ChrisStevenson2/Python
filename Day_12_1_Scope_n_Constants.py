################### Scope ####################

enemies = 1

def increase_enemies():
  # next two lines may increase problem in program - you may not know where the enemies variable is defined and errors can develop over time
  # global enemies
  # enemies += 2

  # better to have it do this instead

  print(f"enemies inside function: {enemies}")
  return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Scope 

# defined outside a function
# similar to having an apple tree planted outside of a fenced yard and available for everyone

player_health = 10

# Local Scope

# defined inside a function
# similar to having an apple tree planted within a fenced yard and only available to that function
def game():
  def drink_potion():
    potion_strength = 2
    print(player_health)
  
  drink_potion()

print(player_health)


#
#
#
#

################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

