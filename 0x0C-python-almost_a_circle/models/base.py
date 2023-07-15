#!/usr/bin/python3
"""
A module that creates a base class
"""


class Base:
    """
    A base class
    """

    __nb_objects = 0  # A private class attribute

    def __init__(self, id=None):
        """
        Instance method thar initializes Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes
        already set based on a dictionary input
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            instance = None
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from a JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                obj_dicts = json.loads(json_data)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def to_csv_string(list_objs):
        """
        Return the CSV string representation of list_objs
        """
        if list_objs is None or len(list_objs) == 0:
            return ""
        cls_name = list_objs[0].__class__.__name__
        fieldnames = list_objs[0].to_dictionary().keys()
        csv_string = f"{cls_name}\n"
        csv_string += ",".join(fieldnames) + "\n"
        for obj in list_objs:
            csv_string += ",".join(str(value) for value in
                                   obj.to_dictionary().values()) + "\n"
        return csv_string

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize and save the list_objs to a CSV file
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        csv_string = cls.to_csv_string(list_objs)
        with open(filename, "w") as file:
            file.write(csv_string)

    @classmethod
    def from_csv_string(cls, csv_string):
        """
        Deserialize the CSV string and return a list of instances
        """
        if csv_string == "":
            return []
        lines = csv_string.strip().split("\n")
        cls_name = lines[0]
        fieldnames = lines[1].split(",")
        obj_dicts = []
        for line in lines[2:]:
            values = line.split(",")
            obj_dict = {field: value for field, value in zip(fieldnames,
                                                             values)}
            obj_dicts.append(obj_dict)
        return [cls.create(**obj_dict) for obj_dict in obj_dicts]

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize and load instances from a CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                csv_string = file.read()
                return cls.from_csv_string(csv_string)
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw the rectangles and squares using Turtle graphics
        """
        window = turtle.Screen()
        window.title("Rectangles and Squares")
        window.bgcolor("white")
        window.setup(width=800, height=600)
        window.setworldcoordinates(0, 0, 800, 600)

        pen = turtle.Turtle()
        pen.speed(0)
        pen.penup()

        # Draw rectangles
        for rectangle in list_rectangles:
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("blue")
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.right(90)
                pen.forward(rectangle.height)
                pen.right(90)
            pen.end_fill()
            pen.penup()

        # Draw squares
        for square in list_squares:
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)
            pen.end_fill()
            pen.penup()

        turtle.done()
