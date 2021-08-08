from PIL import Image, ImageDraw, ImageFont, ImageColor
import tabulate
import typing
import random
import string

# Important: Always put out new version on PyPI before pushing to github

DEFAULT = "(default)"


class PasswordCard(object):
    """
    Generates a Password Card

    Functions:
      get_password: gets the password for [Keyword]
      save: creates an image containing the table
      raw: returns the raw card data

    Variables:
      version: version
      __version__: version
      __card: raw card data

    Magic Functions:
      __init__: initialises the password card
      __getitem__: getitem (card[row, column])
      __eq__: gets the string of [other] and self and compares them
      __str__: converts the card data to a more readable format
      __repr__: repr

    Unlisted:
      __keyword_length: keyword_length for repr
      __segment_length: segment_length for repr
      __seed: seed for repr
    """
    __version__, version = ["1.3.1"] * 2

    def __init__(self, keyword_length: int or str, segment_length: int = DEFAULT, seed=DEFAULT):
        """
        :param keyword_length: has to be the length of the keyword
        :param segment_length: segment length
        :param seed: seed for random.seed
        """
        self.__keyword_length = keyword_length
        self.__segment_length = segment_length
        self.__seed = seed

        # check keyword_lengths type
        if isinstance(keyword_length, str):
            keyword_length = len(keyword_length)
        elif not isinstance(keyword_length, int) or isinstance(keyword_length, bool):
            raise TypeError(f"keyword_length expected int or str; got '{type(keyword_length).__name__}'")
        if segment_length == DEFAULT:
            segment_length = 3
        if seed == DEFAULT:
            seed = None

        self.__card, printable = [["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "ZY",
                                   "."]], string.ascii_lowercase + string.ascii_uppercase + string.digits + "{%}?!.," \
                                                                                                            "_;\\'[]# "

        # Setting seed
        if not callable(seed):
            random.seed(seed)
        else:
            raise TypeError(f"Expected seed to be of type not callable; but got {type(seed).__name__}")

        # Creating card
        for i in range(keyword_length):
            self.__card.append([''.join(random.choices(printable, k=segment_length + i - i)) for i in
                                range(10)])  # + i - i because "unused variable"

    def save(
            self,
            filename: str,
            font_size: int = DEFAULT,
            background: str = DEFAULT,
            font: str = DEFAULT,
            font_color: str = DEFAULT,
            txt: bool = DEFAULT
    ):
        """
        Saves the card as a png or txt

        :param filename: filename
        :param font: font
        :param font_size: font size
        :param font_color: font color
        :param txt: set to true if you dont want to convert the card to a png
        :param background: set the background (in hex)
        """
        text = self.__str__()

        if txt == DEFAULT:
            txt = False
        if txt:
            with open(filename, "w", errors="ignore") as file:
                file.write(text)
            return

        # load font
        if font == DEFAULT:
            font = f"{__file__.replace('PasswordCardGenerator.py', '')}CONSOLA.TTF"
        if font_size == DEFAULT:
            font_size = 15
        font = ImageFont.truetype(font, font_size)

        # get background
        if background == DEFAULT:
            background = ImageColor.getrgb("white")
        else:
            if background.lower() == "transparent":
                background = (0, 0, 0, 0)
            else:
                background = ImageColor.getrgb(background)

        # get font color
        if font_color == DEFAULT:
            font_color = ImageColor.getrgb("black")
        else:
            font_color = ImageColor.getrgb(font_color)

        # determine the size that the image should have
        size, lines = {"x": 0, "y": 0}, []
        for line in text.split("\n"):
            lines.append(font.getsize(line)[0] + 20)
        size["x"] = max(lines)
        size["y"] = int(len(text.split("\n")) * font.getsize(text)[1] * 1.067)

        # create image
        img = Image.new("RGBA", tuple(size.values()), background)

        # write text
        pen = ImageDraw.Draw(img)
        pen.text(
            (10, 10),
            text,
            fill=font_color,
            font=font,
        )

        # save image
        img.save(filename)

        # in case you need a filename generator:
        """
        from random import randint
        from os import path
        
        filename = f"card_{randint(1000, 100000000)}.png"
        while path.exists(filename):
            filename = f"card_{randint(1000, 100000000)}.png"
        """

    def raw(self) -> typing.List[typing.List[str]]:
        """
        Returns self.card
        """
        return self.__card

    def get_password(self, keyword: str) -> str:
        """
        Gets the password for [keyword]
        """
        password, o, keyword = "", 1, keyword.upper()
        # check if keyword has a good length
        for i in range(len(keyword)):
            o += 1
        if o > len(self.__card):
            raise NameError("Keyword is to long!")
        else:
            o = 1

        for char in keyword:
            # get position of keyword char
            pos = None
            for i in range(len(self.__card[0])):
                if char in self.__card[0][i]:
                    pos = i
                    break
            # when position not found raise "invalid keyword"
            if pos is None:
                raise NameError("Invalid Keyword!")

            password += self.__card[o][pos]
            o += 1

        return password

    def __getitem__(self, row_column: typing.Tuple[int or str, int] or int or str) -> str or typing.List[str]:
        # check if only the row is given
        only_row = False
        if not isinstance(row_column, tuple):
            row, column = row_column, None
            only_row = True

        # check that not more than 2 ([1, 2]) opt where given
        elif len(row_column) > 2:
            row_column = str(row_column).replace("(", "[").replace(")", "]")
            raise TypeError(f"Expected [row, column]; got {row_column}")
        else:
            row, column = row_column

        # check types of row and column
        if not isinstance(row, int):
            # if type of row is str and in card headers
            if str(row) in self.__card[0]:
                # get the index of the str
                row = self.__card[0].index(str(row))
            else:
                raise ValueError("Invalid row!")
        else:
            row -= 1
        # check size of row
        if row > len(self.__card[0]) - 1:
            raise IndexError("Row to big!")

        # if not only the row was given
        if not only_row:
            # check type of column
            if not isinstance(column, int):
                raise IndexError("Column has to be of type int!")
            # check size of column
            elif column > len(self.__card) - 1:
                raise IndexError("Column to big!")

            # check size of column and row
            if column <= 0:
                raise IndexError("Column to small!")
            if row < 0:
                raise IndexError("Row to small!")

            return self.__card[column][row]
        else:
            ret = []
            for column in self.__card[1:]:
                ret.append(column[row])

            return ret

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self) -> str:
        tabulated_card = tabulate.tabulate(
            self.__card,
            headers="firstrow",
            showindex="always",
            tablefmt="github"
        )

        # because tabulates showindex starts at 0 i have to do this
        # so it can start from 1
        # initialising card with the standard abc | def ...
        # and setting i to 1
        card, i = '\n'.join(tabulated_card.split("\n")[:2]) + '\n', 1
        for line in tabulated_card.split("\n")[2:]:
            # if the number is 1 digit more replace 1 more space and replace the "wrong" index with i
            # else replace the "wrong" index with i
            if len(str(i)) > len(str(i - 1)):
                card += line.replace(f" {i - 1}", str(i), 1) + '\n'
            else:
                card += line.replace(str(i - 1), str(i), 1) + '\n'
            i += 1

        return card

    def __repr__(self):
        ret = f"PasswordCard(keyword_length={self.__keyword_length}"
        if self.__segment_length is not DEFAULT:
            ret += f", segment_length={self.__segment_length}"
        if self.__seed is not DEFAULT:
            ret += f", seed={self.__seed}"
        ret += ")"

        return repr(ret)
