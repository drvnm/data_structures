class TreeNode:
    def __init__(self, data):
        # data van de Node, list van children een optionele parent
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        # voeg child toe aan children en zet child parent member naar self
        child.parent = self
        self.children.append(child)

    def get_level(self):
        # telt het aantal parents
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        print(self.get_level() * ' ' + '|_', self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_products():
    root = TreeNode("Electronic")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root


root = build_products()
root.print_tree()