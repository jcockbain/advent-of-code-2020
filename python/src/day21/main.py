from src.common.file_utils import get_path, read_integers, read_lines


class Recipe():
    def __init__(self, recipe):
        self.ingredients, self.allergens = self.process_input(recipe)

    def process_input(self, recipe):
        ing, allergens = recipe.split(" (contains ")
        ing_list = ing.strip().split(" ")
        all_list = allergens.strip(")").split(", ")
        return ing_list, all_list


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    recipes = [Recipe(line) for line in lines]
    matched = get_matching(recipes)

    res = 0
    matched_ing = matched.values()
    for arr in [r.ingredients for r in recipes]:
        for i in arr:
            if i not in matched_ing:
                res += 1

    return res


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    recipes = [Recipe(line) for line in lines]
    matched = get_matching(recipes)

    ing_list = [matched[k] for k in sorted(matched)]

    return ",".join(ing_list)


def get_matching(recipes):

    allergens_set = set()

    for s in [r.allergens for r in recipes]:
        for a in s:
            allergens_set.add(a)

    allergens_match = {}
    for r in recipes:
        for a in r.allergens:
            if a not in allergens_match:
                allergens_match[a] = r.ingredients[:]
            else:
                allergens_match[a] = [
                    i for i in allergens_match[a] if i in r.ingredients]

    matched = {}
    while len(matched) < len(allergens_set):
        for a in allergens_match:
            if len(allergens_match[a]) == 1:
                remove_ing = allergens_match[a][0]
                matched[a] = remove_ing
                remove_all = a
                break

        for a in allergens_match:
            if remove_ing in allergens_match[a]:
                allergens_match[a].remove(remove_ing)

        del allergens_match[remove_all]

    return matched


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
