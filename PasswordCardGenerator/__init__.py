from string import ascii_lowercase as al, ascii_uppercase as au, digits as d
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, List
from tabulate import tabulate
from random import choices


# Important: Always put out new version on PyPI before pushing to github


class PasswordCard(object):
    """
    Generates a Password Card

    Functions:
      get_password: gets the password for [Keyword]
      save: creates an image containing the table
    """
    __version__, version = ["1.2.0"]*2

    def __init__(self, keyword_length: int, segment_length: int = 3):
        """
        :param keyword_length: has to be the length of the keyword
        """
        self.card, printable = [["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "ZY",
                                 "."]], al + au + d + "{%}?!.,_;\\'[]#"
        for i in range(keyword_length):
            self.card.append([''.join(choices(printable, k=segment_length + i - i)) for i in
                              range(10)])  # + i - i because "unused variable"

    def get_password(self, keyword: str) -> str:
        """
        Gets the password for [keyword]
        """
        password, o, keyword = "", 1, keyword.upper()
        for char in keyword:
            # get position of keyword char
            pos = None
            for i in range(len(self.card[0])):
                if char in self.card[0][i]:
                    pos = i
                    break
            if pos is None:
                raise NameError("Invalid Keyword!")

            try:
                password += self.card[o][pos]
                o += 1
            except IndexError:
                raise NameError("Keyword is to long!") from None

        return password

    def save(self, filename: str, font: str = f"{__file__.replace('__init__.py', '')}CONSOLA.TTF", font_size: int = 15,
             txt: bool = False):
        """
        Saves the card as a png or txt

        :param filename: filename
        :param font: font
        :param font_size: font size
        :param txt: set to true if you dont want to convert the card to a png
        """
        text = self.__str__()

        if txt:
            with open(filename, "w", errors="ignore") as file:
                file.write(text)
            return

        # load font
        font = ImageFont.truetype(font, font_size)

        # determine the size that the image should have
        size, lines = {"x": 0, "y": 0}, []
        for line in text.split("\n"):
            lines.append(font.getsize(line)[0] + 20)
        size["x"] = max(lines)
        size["y"] = int(len(text.split("\n")) * font.getsize(text)[1] * 1.067)

        # create image
        img = Image.new("RGB", tuple(size.values()), color="white")

        # write text
        pen = ImageDraw.Draw(img)
        pen.text(
            (10, 10),
            text,
            fill=(0, 0, 0),
            font=font,
        )

        # save image
        img.save(filename)

        # in case you need a filename generator:
        """
        filename = f"card_{randint(1000, 100000000)}.png"
        while path.exists(filename):
            filename = f"card_{randint(1000, 100000000)}.png"
        """

    def __getitem__(self, row_column: Tuple[int or str, int]) -> str:
        row, column = row_column
        if not isinstance(row, int):
            if str(row) in self.card[0]:
                row = self.card[0].index(str(row))
            else:
                raise ValueError("Invalid row!")
        else:
            row -= 1
        if row > len(self.card[0]) - 1:
            raise IndexError("Row to big!")

        if not isinstance(column, int):
            raise IndexError("Column has to be of type int!")
        elif column > len(self.card) - 1:
            raise IndexError("Column to big!")

        if column <= 0:
            raise IndexError("Column to small!")
        if row < 0:
            raise IndexError("Row to small!")

        return self.card[column][row]

    def __str__(self) -> str:
        tabulated_card = tabulate(
            self.card,
            headers="firstrow",
            showindex="always",
            tablefmt="github"
        )

        # because tabulates showindex starts at 0 i have to do this
        # so it can start from 1. but there is a catch: if your card has 100
        # as the keyword_length or 1000 or 10000 and so on, the last
        # number looks a bit weird (normally '| 1 |...', bug: '|1 |')
        card, i = '\n'.join(tabulated_card.split("\n")[:2]) + '\n', 1
        for line in tabulated_card.split("\n")[2:]:
            if len(str(i)) > len(str(i - 1)):
                card += line.replace(f" {i - 1}", str(i)) + '\n'
            else:
                card += line.replace(str(i - 1), str(i)) + '\n'
            i += 1

        return card

    def __repr__(self) -> List[List[str]]:
        return self.card
