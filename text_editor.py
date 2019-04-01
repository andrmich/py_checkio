from copy import deepcopy

class Text:

    def __init__(self):
        self.text = ''
        self.font = None

    def write(self, new_text):
        self.text += new_text

    def set_font(self, font_name):
        self.font = font_name

    def show(self):
        if self.font is None:
            return self.text
        else:
            return f'[{self.font}]{self.text}[{self.font}]'

    def restore(self, prev_version):
        self.font = prev_version.font
        self.text = prev_version.text


# class SavedText:
#
#     def __init__(self):
#         self.versions = []
#
#     def save_text(self, text):
#         self.versions.append(deepcopy(text))
#
#     def get_version(self, version_number):
#         return self.versions[version_number]

class SavedText(list):

    def save_text(self, text):
        self.append(deepcopy(text))

    def get_version(self, version_number):
        return self[version_number]




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
