from collections import deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {recipe: [] for recipe in recipes}
        in_degree = {recipe: 0 for recipe in recipes}
        available = set(supplies)
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                if ingredient not in available:
                    graph.setdefault(ingredient, []).append(recipe)
                    in_degree[recipe] += 1
        queue = deque([recipe for recipe in recipes if in_degree[recipe] == 0])
        result = []
        while queue:
            current_recipe = queue.popleft()
            result.append(current_recipe)
            for dependent_recipe in graph[current_recipe]:
                in_degree[dependent_recipe] -= 1
                if in_degree[dependent_recipe] == 0:
                    queue.append(dependent_recipe)

        return result
