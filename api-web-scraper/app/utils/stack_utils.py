from app.model.stack import Stack

def get_stack_tree(stacks: list[Stack]) -> dict[str, dict[str, list[str]]]:
    tree: dict[str, dict[str, list[str]]] = {}

    for item in stacks:
        subcategory = tree.setdefault(item.category, {})
        stacks_values  = subcategory.setdefault(item.subcategory, [])
        if item.stack not in stacks_values:
            stacks_values.append(item.stack)

    return tree