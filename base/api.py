import requests
import json


class API:
    endpoint: str
    current_version: str

    def __init__(self) -> None:
        self.endpoint = "https://pokeapi.co"
        self.current_version = "v2"

    def url(self, path: str) -> str:
        return f"{self.endpoint}/api/{self.current_version}/{path}"

    def get_search(self, register_id: int = None, name: str = None):
        return register_id if register_id is not None else name

    def get(self, path: str):
        endpoint = self.url(path)
        print(f"Endpoint {endpoint}")
        response = requests.get(endpoint)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Content: {response.content}")


class PokemonAPI(API):

    def main_information(self, pokemon_id: int = None, name: str = None):
        search = self.get_search(pokemon_id, name)
        path = f"pokemon/{search}/"
        response = self.get(path)
        return response

    def natures(self, nature_id: int = None, name: str = None):
        search = self.get_search(nature_id, name)
        path = f"nature/{search}/"
        response = self.get(path)
        return response


class MovesAPI(API):

    def main_information(self, movement_id: int = None, name: str = None):
        search = self.get_search(movement_id, name)
        path = f"move/{search}/"
        response = self.get(path)
        return response


class MoveCategoryAPI(API):

    def main_information(self, movement_id: int = None, name: str = None):
        search = self.get_search(movement_id, name)
        path = f"move-category/{search}/"
        response = self.get(path)
        return response


class MoveAilmentAPI(API):

    def main_information(self, ailment_id: int = None, name: str = None):
        search = self.get_search(ailment_id, name)
        path = f"move-ailment/{search}/"
        response = self.get(path)
        return response


class MoveTargetAPI(API):

    def main_information(self, movement_id: int = None, name: str = None):
        search = self.get_search(movement_id, name)
        path = f"move-target/{search}/"
        response = self.get(path)
        return response


def get_name_formatted(initial: str):
    move_category_name = initial.replace("+", " ").replace("-", " ").title()
    move_category_name_wh_spaces = move_category_name.replace(" ", "")
    return move_category_name, move_category_name_wh_spaces


pokeapi = PokemonAPI()
charmander = pokeapi.main_information(pokemon_id=1)
json.dumps(charmander)
nature = pokeapi.natures(nature_id=1)
json.dumps(nature)

move_api = MovesAPI()
classes = ""
for index in range(1, 200):
    movement = move_api.main_information(movement_id=index)
    """if movement["meta"]["healing"] not in [0, None]:
        print(json.dumps(movement))
        break"""

    interfaces = ["Movement"]
    categories = []

    name, name_ws = get_name_formatted(movement['name'])
    move_type = movement['type']['name']
    power = movement.get('power', 0)
    if power == None:
        power = 0
    acu = movement['accuracy']
    pp = movement['pp']
    print(f"Name: {movement['name']} Type: {movement['type']['name']}")
    if movement['damage_class']['name'] == "physical":
        base = "MOVEMENT_BASE_PHYSICAL"
    elif movement['damage_class']['name'] == "special":
        base = "MOVEMENT_BASE_SPECIAL"
    else:
        base = "MOVEMENT_BASE_STATUS"

    attack_fields = ""
    if power > 0:
        interfaces.append("DamageMovement")
        attack_fields = f"""
        self.damage = {str(power)}"""
    elif movement["meta"].get("stat_chance", 0) > 0:
        categories.append("NetGoodStats")

    cate_name, cate_ws_spaces = get_name_formatted(movement["meta"]["category"]["name"])
    target_name, target_ws_spaces = get_name_formatted(movement["target"]["name"])

    drain_attributes = ""
    if movement['meta']['drain'] not in [0, None]:
        interfaces.append("DrainMovement")
        drain_attributes = f"""
        self.drain = {movement['meta']['drain']}
        """

    healing_attributes = ""
    if movement['meta']['healing'] not in [0, None]:
        drain_attributes = f"""
        self.healing = {movement['meta']['healing']}
        """

    hits_movement_attributes = ""
    if movement['meta']['max_hits'] not in [0, None]:
        interfaces.append("HitsMovement")
        hits_movement_attributes = f"""
        
        self.max_hits = {movement['meta']['max_hits']}
        self.min_hits = {movement['meta']['min_hits']}
        """

    turns_movement_attributes = ""
    if movement['meta']['max_turns'] not in [0, None]:
        interfaces.append("TurnsMovement")
        turns_movement_attributes = f"""

        self.max_turns = {movement['meta']['max_turns']}
        self.min_turns = {movement['meta']['min_turns']}
        """

    stat_change_attributes = ""
    if len(movement["stat_changes"]) > 0:
        interfaces.append("StateChangeMovement")
        stat_changes = []
        for stat in movement["stat_changes"]:
            stat_changes.append(f"""
            StateChangeField(change={stat["change"]}, stat="{stat["stat"]["name"]}")
            """)

        chance = movement['meta']['stat_chance'] if movement['meta'].get('stat_chance', 0) > 0 else movement["accuracy"]

        stat_change_attributes = f"""
        
        self.stat_chance = {chance}
        self.stat_change = [{", ".join(stat_changes)}]
        """

    ailment_chance_attributes = ""
    if movement["meta"].get("ailment_chance", 0) > 0:
        interfaces.append("AilmentMovement")
        ailment, aliment_ws = get_name_formatted(movement["meta"]["ailment"]["name"])
        ailment_chance_attributes = f"""
        
        self.ailment_chance = {movement['meta']['ailment_chance']}
        self.ailment = {aliment_ws}
        """

    classes += F"""
class {name_ws}({", ".join(interfaces)}):

    def __init__(self):
        self.name = self.__class__.__name__
        self.external_id = {movement['id']}
        
        self.type = {move_type.upper()}{attack_fields}
        self.base = {base}
        self.accuracy = {acu}
        self.power_points = {str(pp)}
        
        self.priority = {movement['priority']}
        self.critical_level = {movement['meta']['crit_rate']}
        
        self.category = {cate_ws_spaces}
        self.target = {target_ws_spaces}
        {drain_attributes}{healing_attributes}
        self.flinch_chance = {movement['meta']['flinch_chance']}
        {hits_movement_attributes}{turns_movement_attributes}{stat_change_attributes}{ailment_chance_attributes}


        """


classes = ""
move_category_api = MoveCategoryAPI()
for index in range(0, 14):
    move_category = move_category_api.main_information(index)
    if move_category is None:
        break
    name, name_wh_spaces = get_name_formatted(move_category["name"])

    classes += F"""
    class {name_wh_spaces}(Category):
    
        def __init__(self):
            self.name = "{name}"
            self.description = "{move_category["descriptions"][0]["description"]}"

        def execute(self, attacker: Pokemon, defender: Pokemon, movement):
            pass


            """

classes = ""
move_ailment_api = MoveAilmentAPI()
for index in range(0, 50):
    move_ailment = move_ailment_api.main_information(index)
    if move_ailment is not None:
        name, name_wh = get_name_formatted(move_ailment["name"])
        print(name_wh)

        classes += F"""
class {name_wh}(Ailment):

    def __init__(self, chance: int):
        self.chance = chance
        self.name = "{name}"

    def execute(self, defender: Pokemon):
        pass


    """


classes = ""
move_target_api = MoveTargetAPI()
for index in range(0, 50):
    move_target = move_target_api.main_information(index)
    if move_target is not None:
        name, name_wh = get_name_formatted(move_target["name"])
        print(name_wh)

        description = ""
        for des in move_target["descriptions"]:
            if des["language"]["name"] == "en":
                description = des["description"]

        classes += F"""
class {name_wh}(Target):
    def __init__(self):
        self.name = "{name}"
        self.description = "{description}"


    """

path = "/Users/jgarcia/PycharmProjects/pythonProject/src/core/movements/"

# open text file
text_file = open(f'{path}first200.txt', "w")

# write string to file
text_file.write(classes)

# close file
text_file.close()