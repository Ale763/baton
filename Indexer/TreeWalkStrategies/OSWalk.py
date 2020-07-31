import os


class OSWalkStrategy:
    def __init__(self):
        pass

    def traverse(self, p_dir, p_depth=0):
        contents = os.listdir(p_dir)
        for item in contents:
            print("\t" * p_depth + item)
            if os.path.isdir(os.path.join(p_dir, item)):
                self.traverse(p_dir + "\\" + item, p_depth + 1)